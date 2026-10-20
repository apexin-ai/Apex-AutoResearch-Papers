# Research conversation: You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) pape

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af55cc1ef7f9aae6f.jsonl`
- **Structured JSON:** [`1d4d005071b48001d42f.json`](../../sessions/1d/1d4d005071b48001d42f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-26T10:22:37.666Z_

You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `"paper title" first_author_lastname` or `paper title site:arxiv.org`.

Return results in this exact format for each entry:
### [key] — title (year)
- **Exists**: ✓/✗
- **Authors**: ✓/✗ (detail if wrong)
- **Year**: ✓/✗ (detail if wrong)
- **Title**: ✓/✗ (detail if wrong)
- **Venue**: ✓/✗ (detail if wrong)
- **Notes**: ...

Here are the entries to verify:

13. key=intrinsic_dim_detection
title: Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts
authors: Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina
venue: NeurIPS 2023

14. key=seqxgpt
title: SeqXGPT: Sentence-Level AI-Generated Text Detection
authors: Wang, Pengyu and Li, Linyang and Ren, Ke and Jiang, Botian and Zhang, Dong and Qiu, Xipeng
venue: EMNLP 2023

15. key=grover
title: Defending Against Neural Fake News
authors: Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin
venue: NeurIPS 2019

16. key=release_strategies
title: Release Strategies and the Social Impacts of Language Models
authors: Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine
journal: arXiv preprint arXiv:1908.09203, year 2019

17. key=beyond_binary
title: Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement
authors: Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou
venue: ACM Web Conference 2025

18. key=semeval2024_task8
title: SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection
authors: Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav
venue: SemEval 2024

19. key=self_consuming_mad
title: Self-Consuming Generative Models Go MAD
authors: Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.
venue: ICLR 2024

20. key=curse_of_recursion
title: AI models collapse when trained on recursively generated data
authors: Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin
journal: Nature, volume 631, pages 755-759, year 2024

21. key=dohmatob_tale_of_tails
title: A Tale of Tails: Model Collapse as a Change of Scaling Laws
authors: Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, François and Kempe, Julia
venue: ICML 2024

22. key=strong_model_collapse
title: Strong Model Collapse
authors: Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia
venue: ICLR 2025

23. key=model_collapse_avoidable
title: Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data
authors: Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi
venue: COLM 2024

24. key=schaeffer_collapse_position
title: Position: Model Collapse Does Not Mean What You Think
authors: Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi
journal: arXiv preprint arXiv:2503.03150, year 2025


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "c864cf58-375a-413d-8004-08d8c4f4ec4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-26T10:22:37.669Z_

```json
{
  "parentUuid": "c864cf58-375a-413d-8004-08d8c4f4ec4a",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c80f9ab4-67a5-4c5e-a276-6c4a4385cf31",
  "timestamp": "2026-05-26T10:22:37.669Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-26T10:22:40.663Z_



I'll verify all 12 bibliography entries by searching for each one. Let me run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c80f9ab4-67a5-4c5e-a276-6c4a4385cf31",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1pitJXHqBUoXQews4P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea7c3061-b699-471f-a54a-b14ef616a2bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011p4RzNM8EyKRVmYwJMhu2J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8530,
      "cache_read_input_tokens": 9194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8530,
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

_source line 4 · 2026-05-26T10:22:40.695Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LjYQNhwuFrGiWuoMyLet63`</summary>

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
  "parentUuid": "ea7c3061-b699-471f-a54a-b14ef616a2bc",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1pitJXHqBUoXQews4P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d431503-56e4-49b1-ae49-656fd36f407c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011p4RzNM8EyKRVmYwJMhu2J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8530,
      "cache_read_input_tokens": 9194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8530,
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

### Tool result

_source line 5 · 2026-05-26T10:22:40.697Z_

<details><summary>↩ Tool result · `toolu_01LjYQNhwuFrGiWuoMyLet63`</summary>

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
  "parentUuid": "2d431503-56e4-49b1-ae49-656fd36f407c",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "0aa7a2c4-204a-47e6-aa22-6a3aead0b98e",
  "sourceToolAssistantUUID": "2d431503-56e4-49b1-ae49-656fd36f407c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-26T10:22:43.010Z_



Now let me search for all 12 entries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0aa7a2c4-204a-47e6-aa22-6a3aead0b98e",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1pwzqoupXY2t8qAMsT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77def06d-05f7-41eb-920f-655bc86ef40b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lg1rWhr5yNVkchqjdfD9N3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1463,
      "cache_read_input_tokens": 17724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1463,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-26T10:22:43.498Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Bs2SsKPV12YpnJDR1gs6A`</summary>

```json
{
  "query": "\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\" Tulchinskii NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77def06d-05f7-41eb-920f-655bc86ef40b",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1pwzqoupXY2t8qAMsT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6526338-b026-46f5-9293-08e5e4d4244c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lg1rWhr5yNVkchqjdfD9N3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1463,
      "cache_read_input_tokens": 17724,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1463
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 17724,
          "cache_creation_input_tokens": 1463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1463,
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

_source line 8 · 2026-05-26T10:22:50.771Z_

<details><summary>↩ Tool result · `toolu_015Bs2SsKPV12YpnJDR1gs6A`</summary>

```text
Web search results for query: ""Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" Tulchinskii NeurIPS 2023"

Links: [{"title":"NeurIPS Poster Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://neurips.cc/virtual/2023/poster/72624"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/7baa48bc166aa2013d78cbdc15010530-Abstract-Conference.html"},{"title":"[2306.04723] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/abs/2306.04723"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | OpenReview","url":"https://openreview.net/forum?id=8uOZ0kNji6"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/pdf/2306.04723"},{"title":"Intrinsic dimension estimation for robust detection of AI-generated texts | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667828"},{"title":"[PDF] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/a5fab19553e623e8787383cb3da76b8a3c42a8f4"},{"title":"[Quick Review] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://liner.com/review/intrinsic-dimension-estimation-for-robust-detection-of-aigenerated-texts"},{"title":"Are AI Detectors Good Enough? A Survey on Quality of Datasets with","url":"https://openreview.net/pdf?id=WDhwO4Hhq2"}]

I found the paper you're looking for! Here's what I found:

The paper "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" was authored by Eduard Tulchinskii, Kristian Kuznetsov, Laida Kushnareva, Daniil Cherniavskii, Sergey Nikolenko, Evgeny Burnaev, Serguei Barannikov, and Irina Piontkovskaya, and was presented at NeurIPS 2023.

**Key Findings:**

The paper proposes the intrinsic dimensionality of the manifold underlying the set of embeddings of a given text sample as an invariant of human texts. The average intrinsic dimensionality of fluent texts in natural language hovers around the value 9 for several alphabet-based languages and around 7 for Chinese, while the average intrinsic dimensionality of AI-generated texts for each language is approximately 1.5 lower.

**Methodology:**

The approach uses intrinsic dimensionality value, obtained by Persistent Homology Dimension estimation, as a scoring function to separate generated and natural texts.

**Performance:**

The PHD-based classifier outperforms baselines with a large margin: +10% for GPT-3.5, +14% for OPT.

The paper is available on arXiv (2306.04723) and through the official NeurIPS proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6526338-b026-46f5-9293-08e5e4d4244c",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "19a91ef9-b097-4576-bef5-20f2a30ecda3",
  "sourceToolAssistantUUID": "f6526338-b026-46f5-9293-08e5e4d4244c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T10:22:53.120Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TEHMhW2MQTBUYeJkMfLxCu`</summary>

```json
{
  "query": "\"SeqXGPT: Sentence-Level AI-Generated Text Detection\" Wang Pengyu EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19a91ef9-b097-4576-bef5-20f2a30ecda3",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1qgmqKvUURNMuDJYML",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19fa9fde-357a-4d64-9d9e-0bab74f84742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcdifsS72RoPGJbFzfnrpf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 19187,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 995
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 19187,
          "cache_creation_input_tokens": 995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 995,
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

_source line 10 · 2026-05-26T10:23:02.295Z_

<details><summary>↩ Tool result · `toolu_01TEHMhW2MQTBUYeJkMfLxCu`</summary>

```text
Web search results for query: ""SeqXGPT: Sentence-Level AI-Generated Text Detection" Wang Pengyu EMNLP 2023"

Links: [{"title":"SeqXGPT: Sentence-Level AI-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.73/"},{"title":"[2310.08903] SeqXGPT: Sentence-Level AI-Generated Text Detection","url":"https://arxiv.org/abs/2310.08903"},{"title":"SeqXGPT: Sentence-Level AI-Generated Text Detection | Request PDF","url":"https://www.researchgate.net/publication/376393940_SeqXGPT_Sentence-Level_AI-Generated_Text_Detection"},{"title":"[Quick Review] SeqXGPT: Sentence-Level AI-Generated Text Detection","url":"https://liner.com/review/seqxgpt-sentencelevel-aigenerated-text-detection"},{"title":"GitHub - Jihuai-wpy/SeqXGPT: SeqXGPT: An advance method for sentence-level AI-generated text detection.","url":"https://github.com/Jihuai-wpy/SeqXGPT"},{"title":"Paper page - SeqXGPT: Sentence-Level AI-Generated Text Detection","url":"https://huggingface.co/papers/2310.08903"},{"title":"SeqXGPT: Sentence-Level AI-Generated Text Detection","url":"https://arxiv.org/html/2310.08903v2"},{"title":"SeqXGPT: Sentence-Level AI-Generated Text Detection | Papers With Code","url":"https://paperswithcode.com/paper/seqxgpt-sentence-level-ai-generated-text"}]

I found comprehensive information about this paper. Here's what I found:

## SeqXGPT: Sentence-Level AI-Generated Text Detection

SeqXGPT is a paper by Pengyu Wang, Linyang Li, Ke Ren, Botian Jiang, Dong Zhang, and Xipeng Qiu, published at EMNLP 2023. It was published in the Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 1144–1156, in Singapore.

### Problem and Approach

The paper introduces a sentence-level detection challenge by synthesizing a dataset that contains documents that are polished with LLMs, where the documents contain sentences written by humans and sentences modified by LLMs. SeqXGPT is built based on convolution and self-attention networks and is tested in both sentence and document-level detection challenges.

### Key Results

Experimental results show that previous methods struggle in solving sentence-level AIGT detection, while their method not only significantly surpasses baseline methods in both sentence and document-level detection challenges but also exhibits strong generalization capabilities.

### Technical Details

The model uses a list of log probabilities of tokens extracted from a white-box language model as features and processes these features through convolutional networks and self-attention networks to achieve fine-grained classification of the text.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19fa9fde-357a-4d64-9d9e-0bab74f84742",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "bb108be2-d032-41cc-8ba1-68f543760f4f",
  "sourceToolAssistantUUID": "19fa9fde-357a-4d64-9d9e-0bab74f84742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T10:23:04.812Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UGqEQiri6Ma76iBUVwMrVp`</summary>

```json
{
  "query": "\"Defending Against Neural Fake News\" Zellers Rowan NeurIPS 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb108be2-d032-41cc-8ba1-68f543760f4f",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1rY6DcWtGy7jJhaBFo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab1e47f8-fea7-4e06-9ff1-b3238e428410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YN9n8v9wYSqhpVwUX2ukH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 868,
      "cache_read_input_tokens": 20182,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 868
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 20182,
          "cache_creation_input_tokens": 868,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 868,
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

_source line 12 · 2026-05-26T10:23:11.045Z_

<details><summary>↩ Tool result · `toolu_01UGqEQiri6Ma76iBUVwMrVp`</summary>

```text
Web search results for query: ""Defending Against Neural Fake News" Zellers Rowan NeurIPS 2019"

Links: [{"title":"Grover - Defending Against Neural Fake News","url":"https://rowanzellers.com/grover/"},{"title":"Defending Against Neural Fake News","url":"https://papers.neurips.cc/paper_files/paper/2019/file/3e9f0fc9b2f89e043bc6233994dfcf76-Paper.pdf"},{"title":"Reviews: Defending Against Neural Fake News","url":"https://proceedings.neurips.cc/paper/2019/file/3e9f0fc9b2f89e043bc6233994dfcf76-Reviews.html"},{"title":"GitHub - rowanz/grover: Code for Defending Against Neural Fake News, https://rowanzellers.com/grover/ · GitHub","url":"https://github.com/rowanz/grover"},{"title":"Defending Against Neural Fake News - researchr publication","url":"https://researchr.org/publication/ZellersHRBFRC19"},{"title":"Defending against neural fake news | Proceedings of the 33rd International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3454287.3455099"},{"title":"Defending Against Neural Fake News","url":"http://rowanzellers.com/grover/?domain=wired.com&date=June+1%2C+2019&authors=&title=Deep+Yearning+and+Artificial+Righteousness+now+generating+sermons&article=We"},{"title":"[1905.12616] Defending Against Neural Fake News","url":"https://arxiv.org/abs/1905.12616"},{"title":"[PDF] Defending Against Neural Fake News | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Defending-Against-Neural-Fake-News-Zellers-Holtzman/ad7129af0644dbcafa9aa2f111cb76526ea444a1"}]

I found the research paper you're looking for! Here are the key details:

**Paper Title:** Defending Against Neural Fake News

**Authors:** Rowan Zellers, Ari Holtzman, Hannah Rashkin, Yonatan Bisk, Ali Farhadi, Franziska Roesner, and Yejin Choi

**Publication:** Published in Advances in Neural Information Processing Systems 32 in 2019

**Main Contribution:** The paper introduced Grover, a state-of-the-art model for detecting neural fake news. The paper addresses dual-use concerns in natural language generation, noting that while applications like summarization and translation are positive, the underlying technology might enable adversaries to generate neural fake news: targeted propaganda that closely mimics the style of real news.

**Key Finding:** Because of the underlying mechanics of current text generation systems, strong disinformation detectors will also be strong disinformation generators.

The paper is available at multiple locations including arXiv and the NeurIPS proceedings, and the models have been publicly released.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab1e47f8-fea7-4e06-9ff1-b3238e428410",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "ffb44c57-e159-477d-8026-31e1e6ed2be7",
  "sourceToolAssistantUUID": "ab1e47f8-fea7-4e06-9ff1-b3238e428410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T10:23:14.014Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DS5VqpwYuDgwSAqCn2Zobe`</summary>

```json
{
  "query": "\"Release Strategies and the Social Impacts of Language Models\" Solaiman arXiv 1908.09203"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffb44c57-e159-477d-8026-31e1e6ed2be7",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1sBWzYoirS8tQn8DKJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c0c7f83-1318-4ae7-96c4-c028c04972de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oYKxPfv269hvzPuJh3qtb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 21050,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 21050,
          "cache_creation_input_tokens": 847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 847,
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

_source line 14 · 2026-05-26T10:23:22.625Z_

<details><summary>↩ Tool result · `toolu_01DS5VqpwYuDgwSAqCn2Zobe`</summary>

```text
Web search results for query: ""Release Strategies and the Social Impacts of Language Models" Solaiman arXiv 1908.09203"

Links: [{"title":"[1908.09203] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203"},{"title":"Release Strategies and the Social Impacts of Language ...","url":"https://arxiv.org/pdf/1908.09203"},{"title":"[1908.09203v1] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v1"},{"title":"[1908.09203v2] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v2"},{"title":"[PDF] Release Strategies and the Social Impacts of Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Release-Strategies-and-the-Social-Impacts-of-Models-Solaiman-Brundage/c7462e0ee928f095a7fc40b91f1e7557d283ae8e"},{"title":"Paper page - Release Strategies and the Social Impacts of Language Models","url":"https://huggingface.co/papers/1908.09203"},{"title":"Release Strategies and the Social Impacts of Language Models | Request PDF","url":"https://www.researchgate.net/publication/335419868_Release_Strategies_and_the_Social_Impacts_of_Language_Models"},{"title":"link the \"Release Strategies and the Social Impacts of Language Models\" paper · openai-community/roberta-large-openai-detector at 913a6ec","url":"https://huggingface.co/openai-community/roberta-large-openai-detector/commit/913a6ec95e2254ae3b31b2037de05a2ac23583e1"}]

I found the paper for you! Here's what I found about it:

**"Release Strategies and the Social Impacts of Language Models"** (arXiv 1908.09203)

This report discusses OpenAI's work related to the release of its GPT-2 language model, authored by Irene Solaiman and 14 other co-authors including Miles Brundage, Jack Clark, Amanda Askell, and others.

**Key Focus:**

The paper discusses staged release, which allows time between model releases to conduct risk and benefit analyses as model sizes increased, and also discusses ongoing partnership-based research and provides recommendations for better coordination and responsible publication in AI.

Large language models have a range of beneficial uses, such as assisting in prose, poetry, and programming, and analyzing dataset biases, but their flexibility and generative capabilities also raise misuse concerns.

The paper was originally submitted on August 24, 2019, and you can access it directly on arXiv at https://arxiv.org/abs/1908.09203.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c0c7f83-1318-4ae7-96c4-c028c04972de",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "cb3edd17-76c1-4eb4-af8b-b5f62f80f956",
  "sourceToolAssistantUUID": "8c0c7f83-1318-4ae7-96c4-c028c04972de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T10:23:25.700Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UipiQNZJqGEQhnFN926wtr`</summary>

```json
{
  "query": "\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition\" Cheng Zihao ACM Web Conference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb3edd17-76c1-4eb4-af8b-b5f62f80f956",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1t31Jaboqy3qNH4vbv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b19f8c5-0fa5-49ad-9e04-bb5f7fe87b22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkXkxZhxkhwkLRtMLsMvtD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 21897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 816,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T10:23:34.389Z_

<details><summary>↩ Tool result · `toolu_01UipiQNZJqGEQhnFN926wtr`</summary>

```text
Web search results for query: ""Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition" Cheng Zihao ACM Web Conference 2025"

Links: [{"title":"[2410.14259] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/html/2410.14259v2"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text","url":"https://arxiv.org/pdf/2410.14259"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714770"},{"title":"[2410.14259v1] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259v1"},{"title":"Computation and Language Oct 2024","url":"https://arxiv.org/list/cs.CL/2024-10?skip=1225&show=500"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement – Own Your AI","url":"https://ownyourai.com/beyond-binary-towards-fine-grained-llm-generated-text-detection-via-role-recognition-and-involvement-measurement/"}]

I found the paper you're looking for! Here are the key details:

"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement" is a paper by Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, and Haizhou Li, presented at the ACM Web Conference 2025 (WWW '25) in April 28-May 2, 2025, in Sydney, NSW, Australia.

**Paper Overview:**

The paper addresses the rapid development of large language models (LLMs) like ChatGPT and the widespread presence of LLM-generated content on social media platforms, raising concerns about misinformation, data biases, and privacy violations. Current methods often focus on binary classification, failing to address the complexities of real-world scenarios like human-LLM collaboration.

The researchers propose a new paradigm for detecting LLM-generated content that introduces two novel tasks: LLM Role Recognition (LLM-RR), a multi-class classification task that identifies specific roles of LLMs.

**Available Sources:**

The paper is available on:
- arXiv (arxiv.org/abs/2410.14259)
- ACM Digital Library (dl.acm.org/doi/10.1145/3696410.3714770)

You can access the full PDF and additional details from these sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b19f8c5-0fa5-49ad-9e04-bb5f7fe87b22",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "57d7dd02-745b-4448-a3f8-0be460d59002",
  "sourceToolAssistantUUID": "7b19f8c5-0fa5-49ad-9e04-bb5f7fe87b22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T10:23:37.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KMUr1Wey7hKH4hSPdbL9DY`</summary>

```json
{
  "query": "\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\" Wang Yuxia"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57d7dd02-745b-4448-a3f8-0be460d59002",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1tuKiqyVZBWYgochnu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94668777-3a23-4119-8871-a0cb1d6d2acb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5fAh94HVY9broG6LXh7qH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 22713,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 22713,
          "cache_creation_input_tokens": 873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 873,
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

_source line 18 · 2026-05-26T10:23:54.631Z_

<details><summary>↩ Tool result · `toolu_01KMUr1Wey7hKH4hSPdbL9DY`</summary>

```text
Web search results for query: ""SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection" Wang Yuxia"

Links: [{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"SemEval-2024 Tasks | SemEval-2024","url":"https://semeval.github.io/SemEval2024/tasks.html"},{"title":"[PDF] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/c56eab12bd00e2fe28868af21d518044d66df00d"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/semeval-2024-task-8-multidomain-multimodel-and-multilingual-machi"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/bfca76cf8884cdacbcb4db85e0b442bc"},{"title":"Semeval-2024 task 8: Multigenerator, multidomain, and multilingual black-box machine-generated text detection","url":"https://airi.net/articles/semeval-2024-task-8-multigenerator-multidomain-and-multilingual-black-box-machine-generated-text-det/"}]

I found detailed information about SemEval-2024 Task 8. Here are the key findings:

## Overview

SemEval-2024 Task 8 was on Multigenerator, Multidomain, and Multilingual Machine-Generated Text Detection. The task was organized by Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, and Thomas Arnold.

## Task Structure

The task featured three subtasks. Subtask A is a binary classification task determining whether a text is written by a human or generated by a machine, with two tracks: a monolingual track focused solely on English texts and a multilingual track. Subtask B is to detect the exact source of a text, discerning whether it is written by a human or generated by a specific LLM. Subtask C aims to identify the changing point within a text, at which the authorship transitions from human to machine.

## Participation

The task attracted a large number of participants: subtask A monolingual (126), subtask A multilingual (59), subtask B (70), and subtask C (30).

## Publication

The task was published in Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024), pages 2057–2079, Mexico City, Mexico.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94668777-3a23-4119-8871-a0cb1d6d2acb",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "d0d5ac7c-03d2-4458-9623-4de22d8b1340",
  "sourceToolAssistantUUID": "94668777-3a23-4119-8871-a0cb1d6d2acb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T10:23:57.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01197V6vAt46DHjcXphH5v6q`</summary>

```json
{
  "query": "\"Self-Consuming Generative Models Go MAD\" Alemohammad ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0d5ac7c-03d2-4458-9623-4de22d8b1340",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1vPrEcYmbknB2t9eG1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5fab395-16ca-4ec0-a2f8-a9028ac8c589",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hmvf45a4u8nFq7mpEtEzF6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 23586,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1040
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 23586,
          "cache_creation_input_tokens": 1040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1040,
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

_source line 20 · 2026-05-26T10:24:04.538Z_

<details><summary>↩ Tool result · `toolu_01197V6vAt46DHjcXphH5v6q`</summary>

```text
Web search results for query: ""Self-Consuming Generative Models Go MAD" Alemohammad ICLR 2024"

Links: [{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming Generative Models Go MAD | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10570494"},{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://richb.rice.edu/2023/07/12/self-consuming-generative-models-go-mad/"},{"title":"ICLR Poster Self-Consuming Generative Models Go MAD","url":"https://iclr.cc/virtual/2024/poster/18592"},{"title":"Two Papers at ICLR 2024","url":"https://dsp.rice.edu/2024/03/16/two-papers-at-iclr/"}]

I found the paper! Here's a summary of the search results:

"Self-Consuming Generative Models Go MAD" is a paper by Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk, and it was published at the International Conference on Learning Representations (ICLR) in January 2024.

The paper addresses a critical problem in generative AI. Advances in generative AI have led to the temptation to use AI-synthesized data to train next-generation models, and repeating this process creates an autophagous ("self-consuming") loop whose properties are poorly understood.

The key finding of the research is that without enough fresh real data in each generation of an autophagous loop, future generative models are doomed to have their quality (precision) or diversity (recall) progressively decrease, a condition termed Model Autophagy Disorder (MAD), by analogy to mad cow disease.

You can access the full paper at: https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5fab395-16ca-4ec0-a2f8-a9028ac8c589",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "9032d0c1-67c4-466e-b5c4-418686db7964",
  "sourceToolAssistantUUID": "f5fab395-16ca-4ec0-a2f8-a9028ac8c589",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T10:24:07.171Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0154cSD9TKSVj4gPAUjmf8dW`</summary>

```json
{
  "query": "\"AI models collapse when trained on recursively generated data\" Shumailov Nature 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9032d0c1-67c4-466e-b5c4-418686db7964",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1w8CBTGdkpxK3ZonCc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5eefe1e6-11ed-49e4-b908-2082da0e9675",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAaDtUhbiFmauGkw7hgHNg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 24626,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 24626,
          "cache_creation_input_tokens": 1039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1039,
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

_source line 22 · 2026-05-26T10:24:16.068Z_

<details><summary>↩ Tool result · `toolu_0154cSD9TKSVj4gPAUjmf8dW`</summary>

```text
Web search results for query: ""AI models collapse when trained on recursively generated data" Shumailov Nature 2024"

Links: [{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"},{"title":"[PDF] AI models collapse when trained on recursively generated data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AI-models-collapse-when-trained-on-recursively-data-Shumailov-Shumaylov/603d3f90fc40f79ff51258f0295de3ec5107f73e"},{"title":"A note on “AI models collapse when trained on recursively generated data” | by Ali Borji | Medium","url":"https://medium.com/@aliborji/a-note-on-ai-models-collapse-when-trained-on-recursively-generated-data-5bee1de1ab87"},{"title":"AI models collapse when trained on recursively generated data","url":"https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/pdf/2410.12954"},{"title":"Using AI to train AI: Model collapse could be coming for LLMs, say researchers","url":"https://techxplore.com/news/2024-07-ai-collapse-llms.html"}]

I found the research you're looking for. Here are the key findings:

The paper "AI models collapse when trained on recursively generated data" by Shumailov et al. was published in Nature 631, 755–759 (2024).

Analysis shows that indiscriminately training generative artificial intelligence on real and generated content, usually done by scraping data from the Internet, can lead to a collapse in the ability of the models to generate diverse high-quality output.

The research found that indiscriminate use of model-generated content in training causes irreversible defects in the resulting models, in which tails of the original content distribution disappear, and this effect can occur in LLMs as well as in variational autoencoders and Gaussian mixture models.

The study demonstrates that repeatedly training a generative model on synthetic data leads to model collapse, and this finding has generated considerable interest and debate, particularly given that current models have nearly exhausted the available data.

The full paper is available at https://www.nature.com/articles/s41586-024-07566-y (though access may be restricted depending on your institution's subscription).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5eefe1e6-11ed-49e4-b908-2082da0e9675",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "53cbf7bd-4028-4608-9eca-531c5e46e8cd",
  "sourceToolAssistantUUID": "5eefe1e6-11ed-49e4-b908-2082da0e9675",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T10:24:19.114Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RvcDXoKpYDJeNTjWvksj3N`</summary>

```json
{
  "query": "\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" Dohmatob ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53cbf7bd-4028-4608-9eca-531c5e46e8cd",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1wyTbex7JCv3LuiQpw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fab295ea-0e04-4950-a617-f210fcb01dfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SG2XcFBQeFBqhmb8dWsih4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 25665,
      "output_tokens": 81,
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
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 25665,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 896,
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

_source line 24 · 2026-05-26T10:24:26.571Z_

<details><summary>↩ Tool result · `toolu_01RvcDXoKpYDJeNTjWvksj3N`</summary>

```text
Web search results for query: ""A Tale of Tails: Model Collapse as a Change of Scaling Laws" Dohmatob ICML 2024"

Links: [{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"[Quick Review] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://liner.com/review/tale-tails-model-collapse-as-change-scaling-laws"},{"title":"ICML Poster A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://icml.cc/virtual/2024/poster/34339"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws"},{"title":"A tale of tails: model collapse as a change of scaling laws","url":"https://dl.acm.org/doi/10.5555/3692070.3692515"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534888-tale-tails-model-collapse-change-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/html/2402.07043v2"}]

I found the paper! Here's what I discovered:

"A Tale of Tails: Model Collapse as a Change of Scaling Laws" is a paper by Dohmatob, Feng, Yang, Charton, and Kempe, presented at the 41st International Conference on Machine Learning (ICML 2024).

**Overview:**

The paper develops a theoretical framework of model collapse through the lens of scaling laws. The motivation is that as popular AI models are widely used, the ecosystem of online data will progressively contain increased amounts of synthesized data, raising the question of how scaling laws will change when synthetic data enters the training corpus.

**Key Findings:**

The researchers discover a wide range of decay phenomena, analyzing loss of scaling, shifted scaling with number of generations, the "un-learning" of skills, and grokking when mixing human and synthesized data. Notably, their results show that even the smallest fraction of synthetic data (e.g., as little as 1% of the total training dataset) can still lead to model collapse: larger and larger training sets do not enhance performance.

**Mitigation Strategy:**

The paper shows that mixing AI-generated data with even a small amount of clean data mitigates model collapse by introducing a grokking phenomenon.

The paper is available on arXiv and through the ICML proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fab295ea-0e04-4950-a617-f210fcb01dfe",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "ab39a014-7780-4986-8cec-3f951cfbbf5c",
  "sourceToolAssistantUUID": "fab295ea-0e04-4950-a617-f210fcb01dfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T10:24:29.590Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012U8VBbRznhdXJx32EE3GLU`</summary>

```json
{
  "query": "\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" Dohmatob authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab39a014-7780-4986-8cec-3f951cfbbf5c",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1xkeSmwuW3vsZippQY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aff6200c-836f-4a7a-9c6a-fdee78051f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fd8Zd76Cc9bKdXX5B9puep",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 923,
      "cache_read_input_tokens": 26561,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 923
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 26561,
          "cache_creation_input_tokens": 923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 923,
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

_source line 26 · 2026-05-26T10:24:36.754Z_

<details><summary>↩ Tool result · `toolu_012U8VBbRznhdXJx32EE3GLU`</summary>

```text
Web search results for query: ""A Tale of Tails: Model Collapse as a Change of Scaling Laws" Dohmatob authors full list"

Links: [{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/html/2402.07043v2"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534888-tale-tails-model-collapse-change-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://openreview.net/pdf/c028ead5595978096e7ba1f2c41cc3bb709058f9.pdf"},{"title":"A tale of tails: model collapse as a change of scaling laws","url":"https://dl.acm.org/doi/10.5555/3692070.3692515"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tale-tails-model-collapse-as-change-scaling"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws"},{"title":"Paper page - A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://huggingface.co/papers/2402.07043"},{"title":"Elvis DOHMATOB on LinkedIn: A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://www.linkedin.com/posts/elvis-dohmatob-53bba979_a-tale-of-tails-model-collapse-as-a-change-activity-7163099409554079744-Fx1e"}]

Based on the search results, the authors of "A Tale of Tails: Model Collapse as a Change of Scaling Laws" are Dohmatob, E., Feng, Y., Yang, P., Charton, F., and Kempe, J.

The full list of authors is:
1. **Elvis Dohmatob**
2. **Yunzhen Feng**
3. **Pu Yang**
4. **Francois Charton**
5. **Julia Kempe**

The paper was published in the Proceedings of the 41st International Conference on Machine Learning in 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aff6200c-836f-4a7a-9c6a-fdee78051f8b",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "aedeeb92-b9bf-459c-a302-878d6f3cbf7e",
  "sourceToolAssistantUUID": "aff6200c-836f-4a7a-9c6a-fdee78051f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T10:24:39.127Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B4JQBsCe2mj6kFAgZaPY64`</summary>

```json
{
  "query": "\"Strong Model Collapse\" Dohmatob Elvis ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aedeeb92-b9bf-459c-a302-878d6f3cbf7e",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1yVuSvUKScTpwFmsHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27c72f1c-d376-4423-880b-9bdef9b552f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zC4WQyFDYGy8fFPkbQv7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 844,
      "cache_read_input_tokens": 27484,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 844
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 27484,
          "cache_creation_input_tokens": 844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 844,
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

_source line 28 · 2026-05-26T10:24:48.041Z_

<details><summary>↩ Tool result · `toolu_01B4JQBsCe2mj6kFAgZaPY64`</summary>

```text
Web search results for query: ""Strong Model Collapse" Dohmatob Elvis ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://par.nsf.gov/servlets/purl/10649434"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=MQXrTMonT1"},{"title":"Elvis Dohmatob - Concordia University","url":"https://www.concordia.ca/faculty/elvis-dohmatob.html"},{"title":"dblp: Elvis Dohmatob","url":"https://dblp.org/pid/134/9794.html"},{"title":"Elvis Dohmatob (@dohmatobelvis) / Posts / X","url":"https://x.com/dohmatobelvis?lang=en"}]

I found the paper! Here's what I found about "Strong Model Collapse" by Elvis Dohmatob and colleagues at ICLR 2025:

## Overview

The paper is authored by Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, and Julia Kempe from Meta FAIR, Concordia University, Mila, NYU, and UCLA.

## Main Findings

The paper considers a supervised regression setting and establishes a strong form of the model collapse phenomenon, a critical performance degradation due to synthetic data in the training corpus.

The key results show that even the smallest fraction of synthetic data (e.g., as little as 1 per 1000) can still lead to model collapse: larger and larger training sets do not enhance performance.

## Research Questions

The authors further investigate whether increasing model size, an approach aligned with current trends in training large language models, exacerbates or mitigates model collapse.

The paper has been published at ICLR 2025 and is also available on arXiv (arXiv:2410.04840).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27c72f1c-d376-4423-880b-9bdef9b552f5",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "b023ae58-48ba-48d1-94c2-59314df0bd2e",
  "sourceToolAssistantUUID": "27c72f1c-d376-4423-880b-9bdef9b552f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T10:24:50.817Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015rHBS9NBq8TUkLJ7SPDLCe`</summary>

```json
{
  "query": "\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\" Gerstgrasser"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b023ae58-48ba-48d1-94c2-59314df0bd2e",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR1zLCKx67ZCVFXxtjg5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bb90864-70c3-4c86-83c6-27ed91dc1935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017mRgQjUvbApDmkPmh6PzX6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 28328,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 28328,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 716,
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

_source line 30 · 2026-05-26T10:24:57.175Z_

<details><summary>↩ Tool result · `toolu_015rHBS9NBq8TUkLJ7SPDLCe`</summary>

```text
Web search results for query: ""Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" Gerstgrasser"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"Experts divided over training AI with more data from AI • The Register","url":"https://www.theregister.com/2024/05/09/ai_model_collapse/"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by","url":"https://openreview.net/pdf/264715d321dd6b63cbc356483cbb650791eb374b.pdf"}]

I found the research paper you were looking for. Here are the key details:

"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" is authored by Matthias Gerstgrasser and 13 other authors.

**Main Findings:**

The paper addresses what happens when generative models are trained on their own generated outputs, and examines the phenomenon of model collapse, where performance progressively degrades with each model-data feedback iteration.

The research notes that previous studies largely assumed new data replaces old data over time, but a more realistic assumption is that data accumulate over time.

**Key Results:**

The findings show that if data accumulates and models train on a mixture of "real" and synthetic data, model collapse no longer occurs, demonstrated experimentally on causal transformers for language modeling, diffusion models for molecule generation, and variational autoencoders on image data, as well as theoretically for linear regression.

These results suggest that the "curse of recursion" may not be as dire as previously portrayed – provided synthetic data are accumulated alongside real data, rather than replacing real data only.

The paper was published on arXiv on April 29, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bb90864-70c3-4c86-83c6-27ed91dc1935",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "76bc7644-ba73-40c1-9052-205a0b7a138c",
  "sourceToolAssistantUUID": "7bb90864-70c3-4c86-83c6-27ed91dc1935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T10:25:00.350Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MveS84a7RbJKNq5J4bhGNV`</summary>

```json
{
  "query": "\"Is Model Collapse Inevitable?\" Gerstgrasser COLM 2024 conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76bc7644-ba73-40c1-9052-205a0b7a138c",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR211DMFeDFw5SpQ87Gq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4c563b5-8f38-40ad-af7d-c18f97fb27df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B1G1v7wLDpMYBEXiBaCEm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 902,
      "cache_read_input_tokens": 29044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 902,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T10:25:10.516Z_

<details><summary>↩ Tool result · `toolu_01MveS84a7RbJKNq5J4bhGNV`</summary>

```text
Web search results for query: ""Is Model Collapse Inevitable?" Gerstgrasser COLM 2024 conference"

Links: [{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Experts divided over training AI with more data from AI • The Register","url":"https://www.theregister.com/2024/05/09/ai_model_collapse/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai"},{"title":"COLM 2024: Accepted Papers","url":"http://2024.colmweb.org/AcceptedPapers.html"},{"title":"When Models Don't Collapse: On the Consistency of Iterative MLE","url":"https://arxiv.org/pdf/2505.19046"}]

Based on the search results, here's information about the paper "Is Model Collapse Inevitable?" by Gerstgrasser et al. from COLM 2024:

## Paper Overview

The paper was authored by Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, and 10 other researchers, and was published at the COLM 2024 Conference.

## Research Question and Context

The paper addresses what happens when generative models are trained on their own generated outputs. Recent investigations into model-data feedback loops had proposed that such loops would lead to model collapse, under which performance progressively degrades with each model-data feedback iteration until fitted models become useless.

## Key Finding

The paper's central contribution challenges the inevitability of model collapse by examining a critical assumption in prior work. Those previous studies largely assumed that new data replace old data over time, where an arguably more realistic assumption is that data accumulate over time.

The research shows that if data are replaced, test error increases with the number of model-fitting iterations, but if data instead accumulate, the test error has a finite upper bound independent of the number of iterations, meaning model collapse no longer occurs.

In summary, the paper demonstrates that **model collapse is not inevitable** when data from multiple generations of models are accumulated together with real data, rather than replacing the original data entirely.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4c563b5-8f38-40ad-af7d-c18f97fb27df",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "41470c59-9190-49be-b9f4-dd3f35a9e5b0",
  "sourceToolAssistantUUID": "b4c563b5-8f38-40ad-af7d-c18f97fb27df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T10:25:13.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UcRBuYpa8jkFeHsAJ5pkps`</summary>

```json
{
  "query": "\"Position: Model Collapse Does Not Mean What You Think\" Schaeffer Rylan arXiv 2503.03150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41470c59-9190-49be-b9f4-dd3f35a9e5b0",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR21zRkJ7XcHBbCf47Gr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3551a18f-796b-4ffa-a322-e4c615663fbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TdABe1rE4QcCzbp5ApRUdE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1102,
      "cache_read_input_tokens": 29946,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1102
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 29946,
          "cache_creation_input_tokens": 1102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1102,
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

_source line 34 · 2026-05-26T10:25:21.866Z_

<details><summary>↩ Tool result · `toolu_01UcRBuYpa8jkFeHsAJ5pkps`</summary>

```text
Web search results for query: ""Position: Model Collapse Does Not Mean What You Think" Schaeffer Rylan arXiv 2503.03150"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model TrainingAuthors ordered alphabetically. Author contributions are listed at the end.","url":"https://arxiv.org/html/2502.08924v2"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v1"},{"title":"Recursive Training Loops in LLMs: How training data properties modulate distribution shift in generated data?","url":"https://arxiv.org/html/2504.03814v4"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Computers and Society Mar 2025","url":"https://arxiv.org/list/cs.CY/2025-03?skip=300&show=25"}]

I found the paper you were looking for. Here's what the research is about:

## "Position: Model Collapse Does Not Mean What You Think"

This paper addresses concerns about model collapse, which is a degradation in future generative models' performance when trained on synthetic data generated by earlier models. 

### Main Arguments

The authors contend that the widespread narrative around model collapse fundamentally misunderstands the scientific evidence. Their key contribution is that research on model collapse actually encompasses eight distinct and at times conflicting definitions of model collapse, and inconsistent terminology within and between papers has hindered building a comprehensive understanding.

### Paper Details

**Authors:** Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo

**arXiv ID:** 2503.03150

**Posted:** March 18, 2025

The paper is available at https://arxiv.org/abs/2503.03150 and has been cited by several subsequent research papers on related topics like model collapse and training on synthetic data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3551a18f-796b-4ffa-a322-e4c615663fbd",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "b19be04d-81c6-4c7f-914c-d6144c6b2ff5",
  "sourceToolAssistantUUID": "3551a18f-796b-4ffa-a322-e4c615663fbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-26T10:25:24.834Z_

Now let me verify a few details I want to be precise about. Let me check the SemEval-2024 author list and the Shumailov Nature paper details more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b19be04d-81c6-4c7f-914c-d6144c6b2ff5",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR22pnLzazDZvep86VFg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fdc3cdc-b6a0-4852-960f-132dc2a0a6c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015p1gDu2bTPKQyWjFqEqKBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 31048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 874,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 36 · 2026-05-26T10:25:25.906Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VbLwUbrAPRzQps6ijT99k8`</summary>

```json
{
  "query": "SemEval-2024 Task 8 Wang Yuxia authors Whitehouse Chenxi ACL Anthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fdc3cdc-b6a0-4852-960f-132dc2a0a6c9",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR22pnLzazDZvep86VFg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5e78025-ed96-4616-b568-af92a9baa5f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015p1gDu2bTPKQyWjFqEqKBz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 31048,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 31048,
          "cache_creation_input_tokens": 874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 874,
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

_source line 37 · 2026-05-26T10:25:35.649Z_

<details><summary>↩ Tool result · `toolu_01VbLwUbrAPRzQps6ijT99k8`</summary>

```text
Web search results for query: "SemEval-2024 Task 8 Wang Yuxia authors Whitehouse Chenxi ACL Anthology"

Links: [{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"SemEval-2024 Task 8: Multigenerator, Multidomain, and ...","url":"https://github.com/mbzuai-nlp/SemEval2024-task8"},{"title":"SemEval-2024 Tasks | SemEval-2024","url":"https://semeval.github.io/SemEval2024/tasks.html"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/semeval-2024-task-8-multidomain-multimodel-and-multilingual-machi"},{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"Team QUST at SemEval-2024 Task 8: A Comprehensive Study of Monolingual and Multilingual Approaches for Detecting AI-generated Text - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.71/"}]

I found the information you're looking for! SemEval-2024 Task 8 is on Multidomain, Multimodel and Multilingual Machine-Generated Text Detection, authored by Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, and Thomas Arnold. 

Chenxi Whitehouse is also listed as one of the authors in the official bibtex entry, along with Alham Fikri Aji, Nizar Habash, Iryna Gurevych, and Preslav Nakov.

The paper is available on the ACL Anthology at aclanthology.org/2024.semeval-1.279, and was published in the Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024) in Mexico City.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5e78025-ed96-4616-b568-af92a9baa5f1",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "0d06dd3f-f847-44ad-9920-decdfaca9ad6",
  "sourceToolAssistantUUID": "f5e78025-ed96-4616-b568-af92a9baa5f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T10:25:38.597Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R7SJUpZWHPK8Jm2XVBXaEY`</summary>

```json
{
  "query": "Shumailov \"AI models collapse\" Nature volume 631 pages 755"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d06dd3f-f847-44ad-9920-decdfaca9ad6",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR23qjfkzQECbDF8ESkb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "605579ed-b688-447b-a874-bd9396644c8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ro5fzu441fS6uv62qVLyN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 31922,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 31922,
          "cache_creation_input_tokens": 848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 848,
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

_source line 39 · 2026-05-26T10:25:47.253Z_

<details><summary>↩ Tool result · `toolu_01R7SJUpZWHPK8Jm2XVBXaEY`</summary>

```text
Web search results for query: "Shumailov "AI models collapse" Nature volume 631 pages 755"

Links: [{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"AI models collapse when trained on recursively generated data - ORA - Oxford University Research Archive","url":"https://ora.ox.ac.uk/objects/uuid:fa1155e9-c2ff-436a-8391-455b622f4e64"},{"title":"AI model collapse might be prevented by studying human language transmission","url":"https://www.nature.com/articles/d41586-024-03023-y"},{"title":"AI models collapse when trained on recursively generated data - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/ai-models-collapse-when-trained-on-recursively-generated-data/"},{"title":"AI models collapse when trained on recursively generated data","url":"https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf"},{"title":"(PDF) AI models collapse when trained on recursively generated data","url":"https://www.researchgate.net/publication/382526401_AI_models_collapse_when_trained_on_recursively_generated_data"},{"title":"AI models fed AI-generated data quickly spew nonsense","url":"https://www.nature.com/articles/d41586-024-02420-7"},{"title":"[PDF] AI models collapse when trained on recursively generated data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AI-models-collapse-when-trained-on-recursively-data-Shumailov-Shumaylov/603d3f90fc40f79ff51258f0295de3ec5107f73e"}]

I found the paper you were looking for. Here are the key details:

The paper was published in Nature volume 631, pages 755-759 (2024), authored by Shumailov, I., Shumaylov, Z., Zhao, Y. et al.

The paper's title is "AI models collapse when trained on recursively generated data."

The research demonstrates that indiscriminately training generative artificial intelligence on real and generated content, usually done by scraping data from the Internet, can lead to a collapse in the ability of the models to generate diverse high-quality output. More specifically, using data generated by one AI model to train others eventually leads to 'model collapse', in which the models lose information about the real world, with language models that are trained iteratively producing probable sentences too frequently and generating meaningless word sequences.

The paper is available through Nature's official publication at https://www.nature.com/articles/s41586-024-07566-y


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "605579ed-b688-447b-a874-bd9396644c8f",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "61972b84-9908-45ee-b10d-6b8eb18babb2",
  "sourceToolAssistantUUID": "605579ed-b688-447b-a874-bd9396644c8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-26T10:25:50.321Z_

Now let me verify the `release_strategies` author list more carefully, and also check one detail about the `beyond_binary` paper's authors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61972b84-9908-45ee-b10d-6b8eb18babb2",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR24hVMVEZx548XSYL4M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "113eb3df-399f-477f-ac74-77608081f162",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJejR7ajn6LAnMeRjYv1iJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 977,
      "cache_read_input_tokens": 32770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 977,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 41 · 2026-05-26T10:25:50.814Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pq7E2b5K5bXr2RicJjZyCY`</summary>

```json
{
  "query": "arxiv 1908.09203 \"Release Strategies\" Solaiman full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "113eb3df-399f-477f-ac74-77608081f162",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR24hVMVEZx548XSYL4M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45a80371-be1a-460f-a3b5-90f0c3dcfb02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJejR7ajn6LAnMeRjYv1iJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 977,
      "cache_read_input_tokens": 32770,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 977
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 32770,
          "cache_creation_input_tokens": 977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 977,
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

_source line 42 · 2026-05-26T10:25:57.199Z_

<details><summary>↩ Tool result · `toolu_01Pq7E2b5K5bXr2RicJjZyCY`</summary>

```text
Web search results for query: "arxiv 1908.09203 "Release Strategies" Solaiman full author list"

Links: [{"title":"[1908.09203] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203"},{"title":"[1908.09203v2] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v2"},{"title":"[1908.09203v1] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v1"},{"title":"Release Strategies and the Social Impacts of Language ...","url":"https://arxiv.org/pdf/1908.09203"},{"title":"[PDF] Release Strategies and the Social Impacts of Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Release-Strategies-and-the-Social-Impacts-of-Models-Solaiman-Brundage/c7462e0ee928f095a7fc40b91f1e7557d283ae8e"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=I.+Solaiman+%2C+%E2%80%98Release+Strategies+and+the+Social+Impacts+of+Language+Models%E2%80%99.+arXiv%2C+Nov.+12%2C+2019.+Accessed%3A+Feb.+21%2C+2023.+%5BOnline%5D.+Available%3A+http%3A%2F%2Farxiv.org%2Fabs%2F1908.09203"},{"title":"Release Strategies and the Social Impacts of Language Models","url":"https://www.catalyzex.com/paper/arxiv:1908.09203"},{"title":"Paper page - Release Strategies and the Social Impacts of Language Models","url":"https://huggingface.co/papers/1908.09203"},{"title":"Natural Fingerprints of Large Language Models","url":"https://arxiv.org/html/2504.14871v2"},{"title":"Human Variability vs. Machine Consistency: A Linguistic Analysis of Texts Generated by Humans and Large Language Models","url":"https://arxiv.org/html/2412.03025"}]

The full author list for arxiv 1908.09203 "Release Strategies and the Social Impacts of Language Models" is: Irene Solaiman, Miles Brundage, Jack Clark, Amanda Askell, Ariel Herbert-Voss, Jeff Wu, Alec Radford, Gretchen Krueger, Jong Wook Kim, Sarah Kreps, Miles McCain, Alex Newhouse, Jason Blazakis, Kris McGuffie, and Jasmine Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45a80371-be1a-460f-a3b5-90f0c3dcfb02",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "f6fd5e7a-3f9e-4223-b5ce-6a38ad3016dd",
  "sourceToolAssistantUUID": "45a80371-be1a-460f-a3b5-90f0c3dcfb02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:26:00.022Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HNTHT2TiL4Dk4MBt4j55LC`</summary>

```json
{
  "query": "\"Schaeffer\" \"Kazdan\" \"Arulandu\" \"Model Collapse Does Not Mean\" authors Caleb Alvan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6fd5e7a-3f9e-4223-b5ce-6a38ad3016dd",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR25Rq3oxyyovg37FntE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef13d035-3b3c-4b05-9c53-4ebc4d6f071b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qy8Lc8uT499deorTy1DmuX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 33747,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 837
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 33747,
          "cache_creation_input_tokens": 837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 837,
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

_source line 44 · 2026-05-26T10:26:08.434Z_

<details><summary>↩ Tool result · `toolu_01HNTHT2TiL4Dk4MBt4j55LC`</summary>

```text
Web search results for query: ""Schaeffer" "Kazdan" "Arulandu" "Model Collapse Does Not Mean" authors Caleb Alvan"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"[Literature Review] Position: Model Collapse Does Not Mean What You Think","url":"https://www.themoonlight.io/en/review/position-model-collapse-does-not-mean-what-you-think"},{"title":"1 Introduction","url":"https://arxiv.org/html/2503.03150v2"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model TrainingAuthors ordered alphabetically. Author contributions are listed at the end.","url":"https://arxiv.org/html/2502.08924v2"},{"title":"Sanmi Koyejo, Rylan Schaeffer, Joshua Kazdan, Alvan Arlando, Angelina Wang · Model Collapse Does Not Mean What You Think","url":"https://slideslive.com/39038994/model-collapse-does-not-mean-what-you-think"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v1"},{"title":"Model collapse occurs under some definitions, but does not occur under... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Model-collapse-occurs-under-some-definitions-but-does-not-occur-under-others-for-the_tbl1_389617145"},{"title":"Alvan Caleb Arulandu","url":"https://arxiv.org/search/?searchtype=author&query=Alvan+Caleb+Arulandu"}]

Based on the search results, I found the paper you're looking for:

**"Position: Model Collapse Does Not Mean What You Think"** by Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo

The paper addresses concerns over model collapse, which is a degradation in future generative models' performance when trained on synthetic data generated by earlier models. 

The authors highlight that research on model collapse actually encompasses eight distinct and at times conflicting definitions of model collapse, and argue that inconsistent terminology within and between papers has hindered building a comprehensive understanding of model collapse.

In this position piece, the authors contend that the widespread narrative about model collapse fundamentally misunderstands the scientific evidence.

The paper was published on arXiv on March 18, 2025, with arXiv identifier 2503.03150.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef13d035-3b3c-4b05-9c53-4ebc4d6f071b",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "af55cc1ef7f9aae6f",
  "type": "user",
  "uuid": "47ef4c2c-4266-42fa-970f-5cb7099214d7",
  "sourceToolAssistantUUID": "ef13d035-3b3c-4b05-9c53-4ebc4d6f071b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-26T10:26:47.515Z_

Now I have all the information needed. Let me compile the verification results.

Here are the verification results for all 12 bibliography entries:

---

### [intrinsic_dim_detection] — Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts (2023)
- **Exists**: ✓
- **Authors**: ✓ (Tulchinskii, Kuznetsov, Kushnareva, Cherniavskii, Nikolenko, Burnaev, Barannikov, Piontkovskaya -- all confirmed via NeurIPS proceedings)
- **Year**: ✓ (2023)
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2023)
- **Notes**: Confirmed at [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/7baa48bc166aa2013d78cbdc15010530-Abstract-Conference.html) and [arXiv:2306.04723](https://arxiv.org/abs/2306.04723).

---

### [seqxgpt] — SeqXGPT: Sentence-Level AI-Generated Text Detection (2023)
- **Exists**: ✓
- **Authors**: ✓ (Wang Pengyu, Li Linyang, Ren Ke, Jiang Botian, Zhang Dong, Qiu Xipeng -- all confirmed via [ACL Anthology](https://aclanthology.org/2023.emnlp-main.73/))
- **Year**: ✓ (2023)
- **Title**: ✓
- **Venue**: ✓ (EMNLP 2023)
- **Notes**: All clean.

---

### [grover] — Defending Against Neural Fake News (2019)
- **Exists**: ✓
- **Authors**: ✓ (Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi -- all confirmed)
- **Year**: ✓ (2019)
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2019)
- **Notes**: All clean. [arXiv:1905.12616](https://arxiv.org/abs/1905.12616).

---

### [release_strategies] — Release Strategies and the Social Impacts of Language Models (2019)
- **Exists**: ✓
- **Authors**: ✓ (Solaiman, Brundage, Clark, Askell, Herbert-Voss, Wu, Radford, Krueger, Kim, Kreps, McCain, Newhouse, Blazakis, McGuffie, Wang -- all 15 authors confirmed via [arXiv:1908.09203](https://arxiv.org/abs/1908.09203))
- **Year**: ✓ (2019)
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:1908.09203)
- **Notes**: All clean.

---

### [beyond_binary] — Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement (2025)
- **Exists**: ✓
- **Authors**: ✓ (Cheng Zihao, Zhou Li, Jiang Feng, Wang Benyou, Li Haizhou -- confirmed via [ACM DL](https://dl.acm.org/doi/10.1145/3696410.3714770))
- **Year**: ✓ (2025)
- **Title**: ✓
- **Venue**: ✓ (ACM Web Conference 2025 / WWW '25)
- **Notes**: All clean.

---

### [semeval2024_task8] — SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection (2024)
- **Exists**: ✓
- **Authors**: ✓ (Wang, Mansurov, Ivanov, Su, Shelmanov, Tsvigun, Afzal, Mahmoud, Puccetti, Arnold, Whitehouse, Aji, Habash, Gurevych, Nakov -- all 15 authors confirmed via [ACL Anthology](https://aclanthology.org/2024.semeval-1.279/))
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (SemEval 2024, published in Proceedings of the 18th International Workshop on Semantic Evaluation)
- **Notes**: All clean.

---

### [self_consuming_mad] — Self-Consuming Generative Models Go MAD (2024)
- **Exists**: ✓
- **Authors**: ✓ (Alemohammad, Casco-Rodriguez, Luzi, Humayun, Babaei, LeJeune, Siahkoohi, Baraniuk -- all confirmed via [ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf))
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (ICLR 2024)
- **Notes**: All clean.

---

### [curse_of_recursion] — AI models collapse when trained on recursively generated data (2024)
- **Exists**: ✓
- **Authors**: ✓ (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal -- confirmed via [Nature](https://www.nature.com/articles/s41586-024-07566-y))
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (Nature, volume 631, pages 755--759)
- **Notes**: All clean.

---

### [dohmatob_tale_of_tails] — A Tale of Tails: Model Collapse as a Change of Scaling Laws (2024)
- **Exists**: ✓
- **Authors**: ✗ -- The bib entry lists "Charton, Fran\c{c}ois" but the actual author name is **Fran\c{c}ois Charton** (verify the LaTeX encoding is correct). All 5 authors (Dohmatob, Feng, Yang, Charton, Kempe) are confirmed via [ICML proceedings](https://proceedings.mlr.press/v235/dohmatob24b.html).
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (ICML 2024)
- **Notes**: Authors are correct. Just ensure the accent on "Fran\c{c}ois" renders properly in LaTeX.

---

### [strong_model_collapse] — Strong Model Collapse (2025)
- **Exists**: ✓
- **Authors**: ✓ (Dohmatob Elvis, Feng Yunzhen, Subramonian Arjun, Kempe Julia -- all confirmed via [ICLR 2025 proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf))
- **Year**: ✓ (2025)
- **Title**: ✓
- **Venue**: ✓ (ICLR 2025)
- **Notes**: All clean.

---

### [model_collapse_avoidable] — Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (2024)
- **Exists**: ✓
- **Authors**: ✓ (Gerstgrasser, Schaeffer, Dey, Rafailov, Sleight, Hughes, Korbak, Agrawal, Pai, Gromov, Roberts, Yang, Donoho, Koyejo -- all 14 authors confirmed via [OpenReview](https://openreview.net/forum?id=5B2K4LRgmz))
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (COLM 2024)
- **Notes**: All clean.

---

### [schaeffer_collapse_position] — Position: Model Collapse Does Not Mean What You Think (2025)
- **Exists**: ✓
- **Authors**: ✓ (Schaeffer Rylan, Kazdan Joshua, Arulandu Alvan Caleb, Koyejo Sanmi -- all 4 authors confirmed via [arXiv:2503.03150](https://arxiv.org/abs/2503.03150))
- **Year**: ✓ (2025)
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2503.03150)
- **Notes**: All clean.

---

**Summary**: All 12 entries are verified as correct. No hallucinated authors, wrong years, incorrect titles, or wrong venues were found. The only minor note is to ensure the LaTeX accent on "Fran\c{c}ois" in the `dohmatob_tale_of_tails` entry renders correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47ef4c2c-4266-42fa-970f-5cb7099214d7",
  "isSidechain": true,
  "agentId": "af55cc1ef7f9aae6f",
  "requestId": "req_011CbR26Ft35PRUrSjV6nfMS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e8bd169-56c8-4e41-b5fe-6b26fbdf144b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6wAY1QQKWjM1V9W4aopXx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 34584,
      "output_tokens": 2361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2361,
          "cache_read_input_tokens": 34584,
          "cache_creation_input_tokens": 847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 847,
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
