# Research conversation: You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) pape

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aaa614c25b326e871.jsonl`
- **Structured JSON:** [`7f3f05b810370da29586.json`](../../sessions/7f/7f3f05b810370da29586.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

62 recorded events

### User

_source line 1 · 2026-05-26T10:22:09.512Z_

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

1. key=cohen1988statistical
title: Statistical Power Analysis for the Behavioral Sciences
author: Cohen, Jacob
publisher: Lawrence Erlbaum Associates, edition 2nd
year: 1988

2. key=detectgpt
title: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature
authors: Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea
venue: ICML 2023

3. key=gltr
title: GLTR: Statistical Detection and Visualization of Generated Text
authors: Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.
venue: ACL System Demonstrations 2019

4. key=dna_gpt
title: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text
authors: Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng
venue: ICLR 2024

5. key=binoculars
title: Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text
authors: Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom
venue: ICML 2024

6. key=fast_detectgpt
title: Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature
authors: Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue
venue: ICLR 2024

7. key=ld_score
title: Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection
authors: Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul
journal: arXiv preprint arXiv:2605.01647
year: 2026

8. key=diveye
title: Diversity Boosts AI-Generated Text Detection
authors: Basani, Advik Raj and Chen, Pin-Yu
venue: ICLR 2026
eprint: 2509.18880

9. key=feat_aug_transformer
title: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
authors: Mady, Mohamed and Reschke, Johannes and Schuller, Björn
journal: arXiv preprint arXiv:2605.03969
year: 2026

10. key=reliable_detection
title: Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks
authors: Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil
journal: Transactions on Machine Learning Research, year 2025

11. key=paraphrase_evades
title: Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense
authors: Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit
venue: NeurIPS 2023

12. key=detection_possibilities
title: Position: On the Possibilities of AI-Generated Text Detection
authors: Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong
venue: ICML 2024


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "0abc6351-b1a0-4d0b-962c-c968bdbd0f95",
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

_source line 2 · 2026-05-26T10:22:09.518Z_

```json
{
  "parentUuid": "0abc6351-b1a0-4d0b-962c-c968bdbd0f95",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
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
  "uuid": "d05379bb-e258-49e9-b99d-2f07e3e6a585",
  "timestamp": "2026-05-26T10:22:09.518Z",
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

_source line 3 · 2026-05-26T10:22:12.298Z_



I'll verify each bibliography entry using web searches. Let me search for all entries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d05379bb-e258-49e9-b99d-2f07e3e6a585",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1neTbZ2XbTJPaWHSd5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d999d3e-2e9b-4be6-9bb9-b7bb38394cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRHNiibeicJ9qCdJ9yYmkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17417,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17417,
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

_source line 4 · 2026-05-26T10:22:12.470Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01V92kf42Ps2uGoN6fCQYine`</summary>

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
  "parentUuid": "5d999d3e-2e9b-4be6-9bb9-b7bb38394cb2",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1neTbZ2XbTJPaWHSd5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86d82322-4f60-4913-9a1f-d5bdbd9b1bee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRHNiibeicJ9qCdJ9yYmkM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17417,
      "cache_read_input_tokens": 0,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 96,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17417,
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

_source line 5 · 2026-05-26T10:22:12.475Z_

<details><summary>↩ Tool result · `toolu_01V92kf42Ps2uGoN6fCQYine`</summary>

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
  "parentUuid": "86d82322-4f60-4913-9a1f-d5bdbd9b1bee",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "ec410da1-c7f4-4cbf-8746-970abeb8b336",
  "sourceToolAssistantUUID": "86d82322-4f60-4913-9a1f-d5bdbd9b1bee",
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

_source line 6 · 2026-05-26T10:22:15.254Z_



Now let me search for all 12 entries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec410da1-c7f4-4cbf-8746-970abeb8b336",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1nsUBaXMcxJ2FYqv41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4523ed51-ff5f-4c4c-b423-d93eaf678d02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQxcbeDUpMEaP2C358pqT5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 17417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1459,
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

_source line 7 · 2026-05-26T10:22:15.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0155Da2mNtoMLwJ3CMK43q2m`</summary>

```json
{
  "query": "\"Statistical Power Analysis for the Behavioral Sciences\" Cohen Jacob 1988 Lawrence Erlbaum"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4523ed51-ff5f-4c4c-b423-d93eaf678d02",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1nsUBaXMcxJ2FYqv41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "177826f7-446b-43a6-bb5a-d0ca76ce2047",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQxcbeDUpMEaP2C358pqT5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 17417,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 17417,
          "cache_creation_input_tokens": 1459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1459,
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

_source line 8 · 2026-05-26T10:22:23.301Z_

<details><summary>↩ Tool result · `toolu_0155Da2mNtoMLwJ3CMK43q2m`</summary>

```text
Web search results for query: ""Statistical Power Analysis for the Behavioral Sciences" Cohen Jacob 1988 Lawrence Erlbaum"

Links: [{"title":"Statistical Power Analysis for the Behavioral Sciences | Jacob Cohen |","url":"https://www.taylorfrancis.com/books/mono/10.4324/9780203771587/statistical-power-analysis-behavioral-sciences-jacob-cohen"},{"title":"Statistical Power Analysis for the Behavioral Sciences - 2nd Edition -","url":"https://www.routledge.com/Statistical-Power-Analysis-for-the-Behavioral-Sciences/Cohen/p/book/9780805802832"},{"title":"Statistical Power Analysis for the Behavioral Sciences (2nd Edition): Cohen, Jacob: 9780805802832: Amazon.com: Books","url":"https://www.amazon.com/Statistical-Power-Analysis-Behavioral-Sciences/dp/0805802835"},{"title":"Statistical Power Analysis for the Behavioral Sciences - Jacob Cohen - Google Books","url":"https://books.google.com/books/about/Statistical_Power_Analysis_for_the_Behav.html?id=gA04ngAACAAJ"},{"title":"Statistical Power Analysis for the Behavioral Sciences","url":"https://utstat.toronto.edu/~brunner/oldclass/378f16/readings/CohenPower.pdf"},{"title":"Statistical Power Analysis for the Behavioral Sciences || - DOKUMEN.PUB","url":"https://dokumen.pub/statistical-power-analysis-for-the-behavioral-sciences.html"},{"title":"Statistical power analysis for the behavioral sciences : Cohen, Jacob, 1923-1998 : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/statisticalpower0000cohe_j0l3"},{"title":"Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Hillsdale, NJ Lawrence Erlbaum Associates, Publishers. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/ReferencesPapers?ReferenceID=2041144"},{"title":"Statistical Power Analysis for the Behavioral Sciences (2nd Edition) - Cohen, Jacob: 9780805802832 - AbeBooks","url":"https://www.abebooks.com/9780805802832/Statistical-Power-Analysis-Behavioral-Sciences-0805802835/plp"}]

The search has returned results for the book you're looking for. Here's what I found:

"Statistical Power Analysis for the Behavioral Sciences" (Second Edition) was published in 1988 by Jacob Cohen, with Lawrence Erlbaum Associates as the publisher. It is a nontechnical guide to power analysis in research planning that provides users of applied statistics with the tools they need for more effective analysis.

The Second Edition includes a chapter covering power analysis in set correlation and multivariate methods, and a chapter considering effect size, psychometric reliability, and the efficacy of "qualifying" dependent variables. The hardcover edition has 590 pages and ISBN 9780805802832.

The book is available through various academic publishers including Taylor & Francis and Routledge, and can be found on platforms like Amazon and AbeBooks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "177826f7-446b-43a6-bb5a-d0ca76ce2047",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "0503dc1b-6755-4693-bc69-83846ad66017",
  "sourceToolAssistantUUID": "177826f7-446b-43a6-bb5a-d0ca76ce2047",
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

_source line 9 · 2026-05-26T10:22:25.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018dAyyQ2AbgQzzDHBgk9tW8`</summary>

```json
{
  "query": "\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\" Mitchell ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0503dc1b-6755-4693-bc69-83846ad66017",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1ofNSRuwuFoNYyM3Fu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71f498c2-c671-4ee1-9f81-148c60c10a6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gdxiDau2AFYnrBdMqzJ9V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 865,
      "cache_read_input_tokens": 18876,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 865
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 18876,
          "cache_creation_input_tokens": 865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 865,
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

_source line 10 · 2026-05-26T10:22:35.187Z_

<details><summary>↩ Tool result · `toolu_018dAyyQ2AbgQzzDHBgk9tW8`</summary>

```text
Web search results for query: ""DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature" Mitchell ICML 2023"

Links: [{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"GitHub - eric-mitchell/detect-gpt: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature · GitHub","url":"https://github.com/eric-mitchell/detect-gpt"},{"title":"(PDF) DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://www.researchgate.net/publication/367461943_DetectGPT_Zero-Shot_Machine-Generated_Text_Detection_using_Probability_Curvature"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230111305M/abstract"},{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"ICML Oral DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://icml.cc/virtual/2023/oral/25525"},{"title":"FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"}]

I found the paper! Here's information about it based on the search results:

**Paper Overview:**

The paper was published in the Proceedings of the 40th International Conference on Machine Learning, PMLR 202:24950-24962, 2023. The authors are Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, and Chelsea Finn.

**Key Contribution:**

The paper demonstrates that text sampled from an LLM tends to occupy negative curvature regions of the model's log probability function. The researchers define a new curvature-based criterion for judging if a passage is generated from a given LLM.

**Methodology:**

The approach uses only log probabilities computed by the model of interest and random perturbations of the passage from another generic pre-trained language model (e.g., T5). DetectGPT does not require training a separate classifier, collecting a dataset of real or generated passages, or explicitly watermarking generated text.

**Performance:**

DetectGPT is more discriminative than existing zero-shot methods for model sample detection, notably improving detection of fake news articles generated by 20B parameter GPT-NeoX from 0.81 AUROC for the strongest zero-shot baseline to 0.95 AUROC for DetectGPT.

The paper is available on arXiv (2301.11305) and the code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71f498c2-c671-4ee1-9f81-148c60c10a6c",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "9c48b64c-69e4-472b-a8e5-f1138b35b373",
  "sourceToolAssistantUUID": "71f498c2-c671-4ee1-9f81-148c60c10a6c",
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

_source line 11 · 2026-05-26T10:22:38.204Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019KzmieYzvyhdAsiUw3Qqyo`</summary>

```json
{
  "query": "\"GLTR: Statistical Detection and Visualization of Generated Text\" Gehrmann Strobelt Rush ACL 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c48b64c-69e4-472b-a8e5-f1138b35b373",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1pYBNTebqw9YMyYA9m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4a5c5eb-5d01-4e8b-8276-735cae249918",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Costfi3AMfQiHFqECo449p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1027,
      "cache_read_input_tokens": 19741,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1027
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 19741,
          "cache_creation_input_tokens": 1027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1027,
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

_source line 12 · 2026-05-26T10:22:51.845Z_

<details><summary>↩ Tool result · `toolu_019KzmieYzvyhdAsiUw3Qqyo`</summary>

```text
Web search results for query: ""GLTR: Statistical Detection and Visualization of Generated Text" Gehrmann Strobelt Rush ACL 2019"

Links: [{"title":"GLTR: Statistical Detection and Visualization of Generated Text - ACL Anthology","url":"https://aclanthology.org/P19-3019/"},{"title":"[1906.04043] GLTR: Statistical Detection and Visualization of Generated Text","url":"https://arxiv.org/abs/1906.04043"},{"title":"GLTR: Statistical detection and visualization of generated text for ACL 2019 - IBM Research","url":"https://research.ibm.com/publications/gltr-statistical-detection-and-visualization-of-generated-text"},{"title":"[PDF] GLTR: Statistical Detection and Visualization of Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLTR:-Statistical-Detection-and-Visualization-of-Gehrmann-Strobelt/867db5097ad6aaef098c60b0845785b440eca49a"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text","url":"https://scholar.harvard.edu/files/gehrmann/files/acl_demo_2019_gltr_statistical_detection_of_fake_text_5.pdf"},{"title":"GLTR from MIT-IBM Watson AI Lab and HarvardNLP","url":"http://gltr.io/"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text | Sebastian Gehrmann","url":"https://scholar.harvard.edu/gehrmann/publications/gltr-statistical-detection-and-visualization-generated-text"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text | Request PDF","url":"https://www.researchgate.net/publication/335781128_GLTR_Statistical_Detection_and_Visualization_of_Generated_Text"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190604043G/abstract"},{"title":"[Quick Review] GLTR: Statistical Detection and Visualization of Generated Text","url":"https://liner.com/review/gltr-statistical-detection-and-visualization-generated-text"}]

I found the paper! Here's what I found about "GLTR: Statistical Detection and Visualization of Generated Text":

The paper was authored by Sebastian Gehrmann, Hendrik Strobelt, and Alexander Rush, and titled "GLTR: Statistical Detection and Visualization of Generated Text," published in Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations, pages 111–116, Florence, Italy in 2019.

**Overview:**
GLTR is a tool to support humans in detecting whether a text was generated by a model, applying a suite of baseline statistical methods that can detect generation artifacts across multiple sampling schemes.

**Key Results:**
In a human-subjects study, the annotation scheme provided by GLTR improved the human detection-rate of fake text from 54% to 72% without any prior training.

**Methods:**
GLTR employs three simple tests: word probability, absolute rank of a word, and entropy of the predicted distribution, to identify generation artifacts.

**Impact:**
GLTR is open-source and publicly deployed, and has already been widely used to detect generated outputs.

The paper is available through the ACL Anthology, arXiv, and the live GLTR tool can be accessed at gltr.io.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4a5c5eb-5d01-4e8b-8276-735cae249918",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "482594f8-7c31-4de7-8fd1-7fa16d2f93f6",
  "sourceToolAssistantUUID": "c4a5c5eb-5d01-4e8b-8276-735cae249918",
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

_source line 13 · 2026-05-26T10:22:54.625Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TFhHseRZctcsyv6DYFPoEh`</summary>

```json
{
  "query": "\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\" Yang ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "482594f8-7c31-4de7-8fd1-7fa16d2f93f6",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1qmR8Tu6hQxbgmdiG8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "516fc6d9-4538-418e-94ef-6d4d13e2aa64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2j29QSjkyo7f7e7zSJULy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 20768,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 20768,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 944,
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

_source line 14 · 2026-05-26T10:23:01.853Z_

<details><summary>↩ Tool result · `toolu_01TFhHseRZctcsyv6DYFPoEh`</summary>

```text
Web search results for query: ""DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text" Yang ICLR 2024"

Links: [{"title":"[2305.17359] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://arxiv.org/abs/2305.17359"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | OpenReview","url":"https://openreview.net/forum?id=Xlayxj2fWp"},{"title":"ICLR Poster DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://iclr.cc/virtual/2024/poster/18444"},{"title":"dblp: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.","url":"https://dblp1.uni-trier.de/rec/conf/iclr/Yang0WPWC24.html"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.nec-labs.com/blog/dna-gpt-divergent-n-gram-analysis-for-training-free-detection-of-gpt-generated-text/"},{"title":"(PDF) DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.researchgate.net/publication/371136931_DNA-GPT_Divergent_N-Gram_Analysis_for_Training-Free_Detection_of_GPT-Generated_Text"},{"title":"[PDF] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DNA-GPT:-Divergent-N-Gram-Analysis-for-Detection-of-Yang-Cheng/08145978da4c8912f4a05444a6bbf048778dc4af"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free ...","url":"https://arxiv.org/pdf/2305.17359"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://paperreading.club/page?id=167623"}]

I found comprehensive information about the paper "DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text" by Yang et al., which was presented at ICLR 2024.

## Overview

DNA-GPT is a novel training-free detection strategy designed to distinguish between human-written and GPT-generated text.

## Methodology

The method works by truncating text in the middle and using only the preceding portion as input to LLMs to regenerate the new remaining parts. By analyzing the differences between the original and new remaining parts through N-gram analysis in black-box or probability divergence in white-box, it illustrates significant discrepancies between machine-generated and human-written text.

## Key Advantages

Conventional training-based methods have limitations in flexibility, particularly when adapting to new domains, and they often lack explanatory power, which DNA-GPT addresses as a training-free approach.

## Performance

The authors conducted extensive experiments on advanced LLMs from OpenAI, including text-davinci-003, GPT-3.5-turbo, and GPT-4, as well as open-source models such as GPT-NeoX-20B and LLaMa-13B. The zero-shot approach exhibits state-of-the-art performance in distinguishing between human and GPT-generated text on four English and one German dataset, outperforming OpenAI's own classifier.

## Additional Features

The methods provide reasonable explanations and evidence to support claims, which is a unique feature of explainable detection.

The code for this project is available on GitHub at https://github.com/Xianjun-Yang/DNA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "516fc6d9-4538-418e-94ef-6d4d13e2aa64",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "6dbcd916-8fd0-4a09-8b8b-5ab4fdd31f91",
  "sourceToolAssistantUUID": "516fc6d9-4538-418e-94ef-6d4d13e2aa64",
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

_source line 15 · 2026-05-26T10:23:04.541Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EwrvHR9XdKxzyXLszxwUSJ`</summary>

```json
{
  "query": "\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\" Hans ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dbcd916-8fd0-4a09-8b8b-5ab4fdd31f91",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1rWB8H7fi9tcheTMyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91b6091d-e604-4e82-a95f-5284bef4a3f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015hKBfjvBfnC4okSbCXHYhJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1112,
      "cache_read_input_tokens": 21712,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1112
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 21712,
          "cache_creation_input_tokens": 1112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1112,
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

_source line 16 · 2026-05-26T10:23:14.848Z_

<details><summary>↩ Tool result · `toolu_01EwrvHR9XdKxzyXLszxwUSJ`</summary>

```text
Web search results for query: ""Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" Hans ICML 2024"

Links: [{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text - Zilliz Learn","url":"https://zilliz.com/learn/spotting-llms-with-binoculars-zero-shot-detection-of-machine-generated-text"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/html/2401.12070v3"},{"title":"Paper page - Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://huggingface.co/papers/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | OpenReview","url":"https://openreview.net/forum?id=iARAKITHTH"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://proceedings.mlr.press/v235/hans24a.html"},{"title":"[2401.12070v2] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v2"},{"title":"[Literature Review] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://www.themoonlight.io/en/review/spotting-llms-with-binoculars-zero-shot-detection-of-machine-generated-text"}]

I found comprehensive information about this paper. Here are the key details:

## Paper Overview

"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" is by Abhimanyu Hans and 7 other authors.

## Core Method

The paper proposes that a score based on contrasting two closely related language models is highly accurate at separating human-generated and machine-generated text, requiring only simple calculations using a pair of pre-trained LLMs. Specifically, the Binoculars detector works by computing log perplexity using an "observer" LLM, then computing next-token predictions using a "performer" LLM and their perplexity according to the observer (called cross-perplexity), with the ratio of perplexity to cross-perplexity being a powerful signal to detect LLM-text.

## Key Results

The method, called Binoculars, achieves state-of-the-art accuracy without any training data. Over a wide range of document types, Binoculars detects over 90% of generated samples from ChatGPT (and other LLMs) at a false positive rate of 0.01%, despite not being trained on any ChatGPT data.

## Capabilities

It is capable of spotting machine text from a range of modern LLMs without any model-specific modifications, and it overcomes common challenges, such as prompt dependency, and maintains robustness against stylistic variations and adversarial text modifications.

The code for this paper is available on GitHub at https://github.com/ahans30/Binoculars.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91b6091d-e604-4e82-a95f-5284bef4a3f7",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "aaabdfc5-7c14-40ee-b808-212c20864503",
  "sourceToolAssistantUUID": "91b6091d-e604-4e82-a95f-5284bef4a3f7",
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

_source line 17 · 2026-05-26T10:23:17.329Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NyoiiGyoyqrWhwooCfKmDo`</summary>

```json
{
  "query": "\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\" Bao ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaabdfc5-7c14-40ee-b808-212c20864503",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1sTipEdki11puJtwUs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c2c8a14-79e7-4710-9a38-15d2c8434521",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WF5bXGTGXiGcKxQcKq93A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 22824,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 965
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 22824,
          "cache_creation_input_tokens": 965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 965,
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

_source line 18 · 2026-05-26T10:23:22.335Z_

<details><summary>↩ Tool result · `toolu_01NyoiiGyoyqrWhwooCfKmDo`</summary>

```text
Web search results for query: ""Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature" Bao ICLR 2024"

Links: [{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"ICLR Poster Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://iclr.cc/virtual/2024/poster/19201"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | OpenReview","url":"https://openreview.net/forum?id=Bpcgcr8E8Z"},{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/6b8c6f846c3575e1d1ad496abea28826-Abstract-Conference.html"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_FAST-DETECTGPT_EFFICIENT_ZERO-SHOT_DETEC-_TION_OF_MACHINE-GENERATED_TEXT_VIA_CONDI-_TIONAL_PROBABILITY_CURVATURE"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | alphaXiv","url":"https://www.alphaxiv.org/abs/2310.05130"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/html/2310.05130v3"}]

Based on the search results, here's information about the Fast-DetectGPT paper:

## Overview

The paper introduces the concept of conditional probability curvature to explain discrepancies in word choices between LLMs and humans, and presents Fast-DetectGPT, an optimized zero-shot detector that substitutes DetectGPT's perturbation step with a more efficient sampling step.

## Key Motivation

The leading zero-shot detector, DetectGPT, showcases commendable performance but is marred by its intensive computational costs.

## Performance Results

Fast-DetectGPT surpasses DetectGPT by a relative around 75% in both the white-box and black-box settings and accelerates the detection process by a factor of 340.

## Resources

The paper has been published at ICLR 2024, and the code is available on GitHub at https://github.com/baoguangsheng/fast-detect-gpt. You can also find the paper on arXiv (2310.05130) and the OpenReview platform where it was submitted.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c2c8a14-79e7-4710-9a38-15d2c8434521",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "a2fda3cc-ff00-4912-b576-40e18faedc07",
  "sourceToolAssistantUUID": "4c2c8a14-79e7-4710-9a38-15d2c8434521",
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

_source line 19 · 2026-05-26T10:23:25.002Z_

Now let me check the author list for Fast-DetectGPT and search for the remaining entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2fda3cc-ff00-4912-b576-40e18faedc07",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1t1jQV4BT9MLDdHwNM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ef1eedd-edc8-4780-9243-bb236bb504f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtBX78k2pAB8xvLHyzoAa7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1000,
      "cache_read_input_tokens": 23789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1000,
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

_source line 20 · 2026-05-26T10:23:25.600Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cka4VZQ6v3fZgzCBxVeBYp`</summary>

```json
{
  "query": "Fast-DetectGPT Bao Guangsheng authors list ICLR 2024 arxiv 2310.05130"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ef1eedd-edc8-4780-9243-bb236bb504f3",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1t1jQV4BT9MLDdHwNM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4b6c18a-90f5-4dbe-bbd5-28ba160bb373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtBX78k2pAB8xvLHyzoAa7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1000,
      "cache_read_input_tokens": 23789,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1000
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 23789,
          "cache_creation_input_tokens": 1000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1000,
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

_source line 21 · 2026-05-26T10:23:31.602Z_

<details><summary>↩ Tool result · `toolu_01Cka4VZQ6v3fZgzCBxVeBYp`</summary>

```text
Web search results for query: "Fast-DetectGPT Bao Guangsheng authors list ICLR 2024 arxiv 2310.05130"

Links: [{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"[2310.05130v3] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130v3"},{"title":"[2310.05130v2] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130v2"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/html/2310.05130v3"},{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"Paper page - Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://huggingface.co/papers/2310.05130"},{"title":"Fast, Interpretable AI-Generated Text Detection Using Style Embeddings","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/GiuliaZoeSocolofRitikaKacholia.pdf"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_FAST-DETECTGPT_EFFICIENT_ZERO-SHOT_DETEC-_TION_OF_MACHINE-GENERATED_TEXT_VIA_CONDI-_TIONAL_PROBABILITY_CURVATURE"},{"title":"Guangsheng Bao PhD Candidate Advisor: Prof. Yue Zhang","url":"https://baoguangsheng.github.io/assets/pdf/cv.pdf"}]

Based on the search results, here is the authors list for the Fast-DetectGPT paper (arXiv 2310.05130) published at ICLR 2024:

The authors are: Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4b6c18a-90f5-4dbe-bbd5-28ba160bb373",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "46f2908c-15b7-424e-917c-d4abdaa5ada3",
  "sourceToolAssistantUUID": "c4b6c18a-90f5-4dbe-bbd5-28ba160bb373",
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

_source line 22 · 2026-05-26T10:23:35.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MtS9QX4QM5YQHQzCvAZBzQ`</summary>

```json
{
  "query": "\"Beyond Perplexity: Character Distribution Signatures\" MDTA Benchmark Narayanasamy arXiv 2605.01647"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46f2908c-15b7-424e-917c-d4abdaa5ada3",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1thLeKbNcbsmC4PBQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4de6808-0d42-432b-b157-08e4c1310b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MLr1V2aVj8Vmm1rtTjaV7u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 24789,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 976
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 24789,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 976,
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

_source line 23 · 2026-05-26T10:23:45.322Z_

<details><summary>↩ Tool result · `toolu_01MtS9QX4QM5YQHQzCvAZBzQ`</summary>

```text
Web search results for query: ""Beyond Perplexity: Character Distribution Signatures" MDTA Benchmark Narayanasamy arXiv 2605.01647"

Links: [{"title":"[2605.01647] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647"},{"title":"[2605.01647v1] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647v1"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/html/2605.01647v1"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260501647N/abstract"},{"title":"[2605.13652] Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training","url":"https://arxiv.org/abs/2605.13652"},{"title":"Beyond Perplexity: A Lightweight Benchmark for Knowledge Retention in","url":"https://arxiv.org/pdf/2601.03505"}]

I found the paper! Here are the key details about this research:

## Paper Overview

The paper is titled "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection" by Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber, and Fardina Fathmiul Alam from the University of Maryland, College Park.

## Main Contribution

Training-free AI text detection methods primarily rely on model log-probabilities through approaches like Binoculars and DNA-DetectLLM. However, these methods face a fundamental ceiling as models are optimized through RLHF to produce human-like probability distributions. The authors introduce an alternative detection signal based on character distribution signatures.

They provide theoretical foundations showing that AI models, trained on massive domain-balanced corpora, approximate global character patterns while humans exhibit domain-specialized distributions, creating a "Wall of Separation" where human-AI divergence significantly exceeds AI-AI divergence.

## The MDTA Benchmark

The Models-Domains-Temperatures-Adversarial (MDTA) benchmark consists of 642,274 prompt-aligned samples across 4 models, 5 domains, 3 temperature settings, and 3 adversarial strategies, substantially expanding the HC3 dataset with modern model responses and targeted adversarial attacks.

The paper was submitted on May 3, 2026 and is under review at COLM 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4de6808-0d42-432b-b157-08e4c1310b45",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "963eae3e-298c-4e76-8af9-d1e5de548afa",
  "sourceToolAssistantUUID": "b4de6808-0d42-432b-b157-08e4c1310b45",
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

_source line 24 · 2026-05-26T10:23:48.607Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GgCF6YJZF9r2vYjam7JUm6`</summary>

```json
{
  "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen Pin-Yu ICLR 2026 arXiv 2509.18880"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "963eae3e-298c-4e76-8af9-d1e5de548afa",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1ui1MheJB9bkZfwDwJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f79858ee-d008-44db-b973-ed2a113e1fa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FuvDAJkZwJEPuQU5ZEyLCY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 25765,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 796
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 25765,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 796,
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

_source line 25 · 2026-05-26T10:23:58.600Z_

<details><summary>↩ Tool result · `toolu_01GgCF6YJZF9r2vYjam7JUm6`</summary>

```text
Web search results for query: ""Diversity Boosts AI-Generated Text Detection" Basani Chen Pin-Yu ICLR 2026 arXiv 2509.18880"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"Pin-Yu Chen on X: \"Happy to see this work published at @TmlrOrg We show that diversity-driven features (computed by a very small LM, such as GPT-2) are powerful for detecting AI-written content. Try out our online detector at https://t.co/7sLfMdcmDG Kudos to Advik for leading this work.\" / X","url":"https://x.com/pinyuchenTW/status/2031014939846995984"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection","url":"https://ceur-ws.org/Vol-4038/paper_282.pdf"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"}]

I found the paper you're looking for! Here's what I found about the research:

**Paper Details:**
The paper "Diversity Boosts AI-Generated Text Detection" was submitted on September 23, 2025 and last revised on February 25, 2026, authored by Advik Raj Basani and Pin-Yu Chen. It was published as a conference paper at ICLR 2026. The arXiv identifier is 2509.18880.

**Research Overview:**
The paper proposes DivEye, a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features. The research is motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs.

**Key Results:**
The method outperforms existing zero-shot detectors by up to 33.2% and achieves competitive performance with fine-tuned baselines across multiple benchmarks.

**Application:**
While prior detectors often rely on token-level likelihoods or opaque black-box classifiers, these approaches struggle against high-quality generations and offer little interpretability, which the DivEye framework addresses through its interpretable statistical features.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f79858ee-d008-44db-b973-ed2a113e1fa7",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "239947eb-f80f-4f72-be3c-af36db1c395d",
  "sourceToolAssistantUUID": "f79858ee-d008-44db-b973-ed2a113e1fa7",
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

_source line 26 · 2026-05-26T10:24:02.037Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011SYhDi4LkApogs5AFydHD3`</summary>

```json
{
  "query": "\"Feature-Augmented Transformers for Robust AI-Text Detection\" Mady Reschke Schuller arXiv 2605.03969"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "239947eb-f80f-4f72-be3c-af36db1c395d",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1vgrRxe5KEZZGreCW5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ff6406f-29d2-40fa-b76c-b98dae197284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEZ5zWP28YvmCVDeXh4n5K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 26561,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1024
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 26561,
          "cache_creation_input_tokens": 1024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1024,
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

_source line 27 · 2026-05-26T10:24:12.184Z_

<details><summary>↩ Tool result · `toolu_011SYhDi4LkApogs5AFydHD3`</summary>

```text
Web search results for query: ""Feature-Augmented Transformers for Robust AI-Text Detection" Mady Reschke Schuller arXiv 2605.03969"

Links: [{"title":"[2605.03969] Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/abs/2605.03969"},{"title":"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/html/2605.03969"},{"title":"[2410.08113] Robust AI-Generated Text Detection by Restricted Embeddings","url":"https://arxiv.org/abs/2410.08113"},{"title":"[2507.05157] AI Generated Text Detection Using Instruction Fine-tuned Large Language and Transformer-Based Models","url":"https://arxiv.org/abs/2507.05157"},{"title":"Adaptive Ensembles of Fine-Tuned Transformers for LLM-Generated Text Detection","url":"https://arxiv.org/html/2403.13335v1"},{"title":"[2601.03812] AI Generated Text Detection","url":"https://arxiv.org/abs/2601.03812"},{"title":"[2509.20375] Assessing Classical Machine Learning and Transformer-based Approaches for Detecting AI-Generated Research Text","url":"https://arxiv.org/abs/2509.20375"},{"title":"Enhancing Text Authenticity: A Novel Hybrid Approach for AI-Generated Text Detection","url":"https://arxiv.org/html/2406.06558v1"},{"title":"Efficient detection of AI-generated scientific abstracts with a lightweight transformer | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-35203-3"},{"title":"[2403.13335] Adaptive Ensembles of Fine-Tuned Transformers for LLM-Generated Text Detection","url":"https://arxiv.org/abs/2403.13335"}]

I found the paper! Here are the key details about the paper from arXiv:

**Title:** Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators

**Authors:** Mohamed Mady, Johannes Reschke, Björn Schuller

**arXiv ID:** 2605.03969 (submitted May 5, 2026)

**Key Findings:**

AI-generated text is produced at scale across diverse domains and heterogeneous generators, making robustness to distribution shift a central requirement for reliable detection. The researchers address this challenge by training transformer-based detectors on HC3 PLUS and adopting a deployment-realistic fixed-threshold protocol.

The study reveals that near-ceiling in-domain performance (up to 99.5% balanced accuracy) degrades significantly under cross-dataset and generator shift, exposing strong complementary failure modes across backbones.

**Main Contribution:** Feature augmentation via attention-based linguistic feature fusion improves transfer, with their best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4.

The paper addresses an important problem in AI text detection—while models perform well on known datasets, their performance drops significantly when tested on new domains and generators, and the proposed feature augmentation approach helps mitigate this issue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ff6406f-29d2-40fa-b76c-b98dae197284",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "4f00bf4c-1f66-4e28-bf8d-eee62341b2ba",
  "sourceToolAssistantUUID": "5ff6406f-29d2-40fa-b76c-b98dae197284",
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

_source line 28 · 2026-05-26T10:24:15.669Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LttooxdQW6QsUrd2Twoxew`</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected?\" Sadasivan Kumar Balasubramanian Wang Feizi TMLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f00bf4c-1f66-4e28-bf8d-eee62341b2ba",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1whbrbZ82STrYBZHqC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c27c72c8-f864-4dd0-96c8-3550a75c3c3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tFDzgxxb472BoGtewMaJ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 27585,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 27585,
          "cache_creation_input_tokens": 917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 917,
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

_source line 29 · 2026-05-26T10:24:23.257Z_

<details><summary>↩ Tool result · `toolu_01LttooxdQW6QsUrd2Twoxew`</summary>

```text
Web search results for query: ""Can AI-Generated Text be Reliably Detected?" Sadasivan Kumar Balasubramanian Wang Feizi TMLR 2025"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** "Can AI-Generated Text be Reliably Detected?"

**Authors:** Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi

**Venue:** Action editor: Kamalika Chaudhuri (TMLR - Transactions on Machine Learning Research)

**Summary:**
The paper stress-tests the robustness of AI text detectors in the presence of an attacker. It introduces a recursive paraphrasing attack to stress test AI text detectors and provides a theoretical framework connecting detector performance to the distribution distance between human and AI-generated text.

The paper addresses the critical challenge of detecting AI-generated text and demonstrates that these detectors are not reliable in practical scenarios.

You can find the paper at: https://openreview.net/forum?id=OOgsAZdFOt


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c27c72c8-f864-4dd0-96c8-3550a75c3c3e",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "64d49e70-f656-42d2-a0ac-552620c450c5",
  "sourceToolAssistantUUID": "c27c72c8-f864-4dd0-96c8-3550a75c3c3e",
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

_source line 30 · 2026-05-26T10:24:27.013Z_

I need to check the exact title in the bib entry — the bib says "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" while there seems to be a shorter version too. Let me also check the year more carefully, and verify the remaining entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64d49e70-f656-42d2-a0ac-552620c450c5",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1xWDH7p5tq2DqWWoc9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "959c9521-37c2-4cfa-96fc-33881d088853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168cuh5AEqVUscSVnoPSeJx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 28502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 909,
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

_source line 31 · 2026-05-26T10:24:27.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013gSnFqWLZHbLqBJKuy9WsN`</summary>

```json
{
  "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" TMLR publication year 2025 OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "959c9521-37c2-4cfa-96fc-33881d088853",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1xWDH7p5tq2DqWWoc9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f942dd79-8431-4188-b219-009ccc967202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168cuh5AEqVUscSVnoPSeJx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 28502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 909,
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

### Tool result

_source line 32 · 2026-05-26T10:24:35.093Z_

<details><summary>↩ Tool result · `toolu_013gSnFqWLZHbLqBJKuy9WsN`</summary>

```text
Web search results for query: "Sadasivan "Can AI-Generated Text be Reliably Detected" TMLR publication year 2025 OpenReview"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? Stress ...","url":"https://openreview.net/pdf/a06fe5303ab3d0c635e565d4eae91e5ab7ac8175.pdf"}]

Based on the search results, I found the paper you're looking for:

"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" is by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi.

The paper was published at TMLR (Transactions on Machine Learning Research). According to the search results, the submission was previously submitted to TMLR, and the revised version was published in October 2024. The original arXiv version appeared in 2023. The OpenReview link for the TMLR publication is: https://openreview.net/forum?id=OOgsAZdFOt


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f942dd79-8431-4188-b219-009ccc967202",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "4098b364-cf91-4246-82da-3ebddc220853",
  "sourceToolAssistantUUID": "f942dd79-8431-4188-b219-009ccc967202",
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

_source line 33 · 2026-05-26T10:24:38.229Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CAsYRqsCfGgGSGfwBMu4ep`</summary>

```json
{
  "query": "\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\" Krishna NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4098b364-cf91-4246-82da-3ebddc220853",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1yNrYV8zS5GPSnUHz6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8441436-4be0-4c98-92bc-49597c9bfca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MfYA8DWn9Qf1jE6L2giktc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 29411,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 924
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 29411,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 924,
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

_source line 34 · 2026-05-26T10:24:47.336Z_

<details><summary>↩ Tool result · `toolu_01CAsYRqsCfGgGSGfwBMu4ep`</summary>

```text
Web search results for query: ""Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense" Krishna NeurIPS 2023"

Links: [{"title":"GitHub - martiansideofthemoon/ai-detection-paraphrases: Official repository for our NeurIPS 2023 paper \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\" (https://arxiv.org/abs/2303.13408). · GitHub","url":"https://github.com/martiansideofthemoon/ai-detection-paraphrases"},{"title":"NeurIPS Poster Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://neurips.cc/virtual/2023/poster/71402"},{"title":"[2303.13408] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408"},{"title":"[PDF] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Paraphrasing-evades-detectors-of-AI-generated-text,-Krishna-Song/1c13af186d1e177b85ef1ec3fc7b8d33ec314cfd"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://arxiv.org/pdf/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Request PDF","url":"https://www.researchgate.net/publication/369477232_Paraphrasing_evades_detectors_of_AI-generated_text_but_retrieval_is_an_effective_defense"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://papers.nips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230313408K/abstract"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** "Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense" by Kalpesh Krishna, Yixiao Song, Marzena Karpinska, John Wieting, and Mohit Iyyer

**Venue:** Advances in Neural Information Processing Systems 36 (NeurIPS 2023)

**Key Findings:**

The authors built a 11B parameter paraphrase generation model (DIPPER) that can paraphrase paragraphs, condition on surrounding context, and control lexical diversity and content reordering.

Paraphrasing text generated by three large language models (including GPT3.5-davinci-003) with DIPPER successfully evades several detectors, including watermarking, GPTZero, DetectGPT, and OpenAI's text classifier. For example, DIPPER drops detection accuracy of DetectGPT from 70.3% to 4.6% (at a constant false positive rate of 1%), without appreciably modifying the input semantics.

**Defense Mechanism:** Using a database of 15M generations from a fine-tuned T5-XXL model, the retrieval-based defense can detect 80% to 97% of paraphrased generations across different settings while only classifying 1% of human-written sequences as AI-generated.

The official repository and paper are available on [arXiv](https://arxiv.org/abs/2303.13408) and [GitHub](https://github.com/martiansideofthemoon/ai-detection-paraphrases).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8441436-4be0-4c98-92bc-49597c9bfca4",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "292808ec-19e7-40d8-a7dd-c37b8f6c5689",
  "sourceToolAssistantUUID": "c8441436-4be0-4c98-92bc-49597c9bfca4",
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

_source line 35 · 2026-05-26T10:24:50.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YRvvBmSuF6CEnaorgHFY8e`</summary>

```json
{
  "query": "\"Position: On the Possibilities of AI-Generated Text Detection\" Chakraborty Bedi Zhu An Manocha Huang ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "292808ec-19e7-40d8-a7dd-c37b8f6c5689",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR1zJ5aZy1FEWDZRK2f8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c81e50d-e81e-4ade-be1a-df7618f466b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzTP5g7GgoviLseN9W15np",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1110,
      "cache_read_input_tokens": 30335,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1110
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 30335,
          "cache_creation_input_tokens": 1110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1110,
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

_source line 36 · 2026-05-26T10:25:06.370Z_

<details><summary>↩ Tool result · `toolu_01YRvvBmSuF6CEnaorgHFY8e`</summary>

```text
Web search results for query: ""Position: On the Possibilities of AI-Generated Text Detection" Chakraborty Bedi Zhu An Manocha Huang ICML 2024"

Links: [{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://proceedings.mlr.press/v235/chakraborty24a.html"},{"title":"[2304.04736] On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/abs/2304.04736"},{"title":"ICML Poster Position: On the Possibilities of AI-Generated Text Detection","url":"https://icml.cc/virtual/2024/poster/34689"},{"title":"[PDF] On the Possibilities of AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Possibilities-of-AI-Generated-Text-Detection-Chakraborty-Bedi/59ae4e4ff7a27010554081e478d9ee707d16d583"},{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://raw.githubusercontent.com/mlresearch/v235/main/assets/chakraborty24a/chakraborty24a.pdf"},{"title":"Position: On the possibilities of AI-generated text detection","url":"https://dl.acm.org/doi/10.5555/3692070.3692305"},{"title":"On the Possibilities of AI-Generated Text Detection: A Sample Complexity Analysis | OpenReview","url":"https://openreview.net/forum?id=oxEER3kZ9M"},{"title":"Position: On the Possibilities of AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=CJbhtpcyGL"},{"title":"On the Possibilities of AI-Generated Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230404736C/abstract"},{"title":"On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/pdf/2304.04736"}]

I found the paper you're looking for. Here's what I discovered:

**Title:** Position: On the Possibilities of AI-Generated Text Detection

**Authors:** Souradip Chakraborty, Amrit Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, Furong Huang

**Publication:** Proceedings of the 41st International Conference on Machine Learning, PMLR 235:6093-6115, 2024

**Main Findings:**

The study addresses the challenge of distinguishing human-written text from Large Language Model (LLM) outputs, providing evidence that this differentiation is consistently feasible, except when human and machine text distributions are indistinguishable across their entire support.

Employing information theory, the researchers show that while detecting machine-generated text becomes harder as it nears human quality, it remains possible with adequate text data. They introduce guidelines on the required text data quantity, either through sample size or sequence length, for reliable AI text detection, through derivations of sample complexity bounds.

The paper is officially published at the ICML 2024 proceedings and is available through multiple sources including arXiv and the ICML conference website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c81e50d-e81e-4ade-be1a-df7618f466b5",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "9250d1c7-c45f-42c7-90f0-c5bf6917e7f6",
  "sourceToolAssistantUUID": "8c81e50d-e81e-4ade-be1a-df7618f466b5",
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

_source line 37 · 2026-05-26T10:25:09.465Z_

Now let me check the DNA-GPT author list more carefully, as the bib entry includes "Haifeng Chen" which I want to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9250d1c7-c45f-42c7-90f0-c5bf6917e7f6",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR21gXjBgjZeYxz5jPnV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e27f3568-eaf1-4802-a931-7558d46e6074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WhoBDTKrZqvFFhQRnY6HY6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 31445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 903,
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

_source line 38 · 2026-05-26T10:25:10.249Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015gBddtshaoyR2njAT36CAw`</summary>

```json
{
  "query": "DNA-GPT Yang Xianjun full author list arxiv 2305.17359 ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e27f3568-eaf1-4802-a931-7558d46e6074",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR21gXjBgjZeYxz5jPnV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01677190-3a23-4391-bcff-05644029aaa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WhoBDTKrZqvFFhQRnY6HY6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 31445,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 113,
          "cache_read_input_tokens": 31445,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 903,
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

_source line 39 · 2026-05-26T10:25:17.315Z_

<details><summary>↩ Tool result · `toolu_015gBddtshaoyR2njAT36CAw`</summary>

```text
Web search results for query: "DNA-GPT Yang Xianjun full author list arxiv 2305.17359 ICLR 2024"

Links: [{"title":"[2305.17359] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://arxiv.org/abs/2305.17359"},{"title":"Paper page - DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://huggingface.co/papers/2305.17359"},{"title":"(PDF) DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.researchgate.net/publication/371136931_DNA-GPT_Divergent_N-Gram_Analysis_for_Training-Free_Detection_of_GPT-Generated_Text"},{"title":"GitHub - Xianjun-Yang/DNA-GPT: Offiical codes for DNA-GPT (ICLR 2024)","url":"https://github.com/Xianjun-Yang/DNA-GPT"},{"title":"[PDF] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DNA-GPT:-Divergent-N-Gram-Analysis-for-Detection-of-Yang-Cheng/08145978da4c8912f4a05444a6bbf048778dc4af"},{"title":"DNA-GPT/DNA-GPT-dist.py at main · Xianjun-Yang/DNA-GPT","url":"https://github.com/Xianjun-Yang/DNA-GPT/blob/main/DNA-GPT-dist.py"},{"title":"publications | Xianjun Yang","url":"https://xianjun-yang.github.io/publications/"},{"title":"DNA-GPT/README.md at main · Xianjun-Yang/DNA-GPT","url":"https://github.com/Xianjun-Yang/DNA-GPT/blob/main/README.md"},{"title":"dblp: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.","url":"https://dblp.org/rec/journals/corr/abs-2305-17359.html"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free ...","url":"https://arxiv.org/pdf/2305.17359"}]

Based on the search results, I found the full author list for the DNA-GPT paper (arxiv 2305.17359):

The authors are: Xianjun Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, and Haifeng Chen.

However, I should note a discrepancy: Most sources list only 5 authors (Xianjun Yang, Wei Cheng, Linda Petzold, William Yang Wang, and Haifeng Chen), but the arXiv abstract page mentions Yue Wu as an additional author. The paper was submitted on May 27, 2023, with the latest version on October 4, 2023, and was published at ICLR 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01677190-3a23-4391-bcff-05644029aaa0",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "71f5b76f-6c47-45f5-b7ee-50056bdcdfa6",
  "sourceToolAssistantUUID": "01677190-3a23-4391-bcff-05644029aaa0",
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

_source line 40 · 2026-05-26T10:25:19.947Z_

Now let me verify the Binoculars author list more carefully, and the TMLR year for the reliable_detection paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71f5b76f-6c47-45f5-b7ee-50056bdcdfa6",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR22VMYnV2VhgNbHVggt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ac0c5dc-96a4-4643-811d-51113be6f6c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iZ7Q4wM6Taa1wALd5zrA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 32348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1049,
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

_source line 41 · 2026-05-26T10:25:20.808Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019LNEs2jk7n5NzJQquPq1KQ`</summary>

```json
{
  "query": "Binoculars Hans Schwarzschild Cherepanova authors full list arxiv 2401.12070"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ac0c5dc-96a4-4643-811d-51113be6f6c8",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR22VMYnV2VhgNbHVggt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2873d784-794d-4e75-a956-72f8086de304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iZ7Q4wM6Taa1wALd5zrA4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 32348,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1049
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 32348,
          "cache_creation_input_tokens": 1049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1049,
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

_source line 42 · 2026-05-26T10:25:27.147Z_

<details><summary>↩ Tool result · `toolu_019LNEs2jk7n5NzJQquPq1KQ`</summary>

```text
Web search results for query: "Binoculars Hans Schwarzschild Cherepanova authors full list arxiv 2401.12070"

Links: [{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"[PDF] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Spotting-LLMs-With-Binoculars:-Zero-Shot-Detection-Hans-Schwarzschild/8dafb105a0cec1956443003eeea9fcf13c0ffa99"},{"title":"[2401.12070v2] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v2"},{"title":"[2401.12070v1] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v1"},{"title":"Google Académico","url":"https://scholar.google.com/scholar?q=Abhimanyu+Hans%2C+Avi+Schwarzschild%2C+Valeriia+Cherepanova%2C+Hamid+Kazemi%2C+Aniruddha+Saha%2C+Micah+Goldblum%2C+Jonas+Geiping%2C+and+Tom+Goldstein.+2024.+Spotting+llms+with+binoculars%3A+Zero-shot+detection+of+machine-generated+text.+arXiv+preprint+arXiv%3A2401.12070%282024%29."},{"title":"Paper page - Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://huggingface.co/papers/2401.12070"},{"title":"Binoculars/README.md at main · ahans30/Binoculars","url":"https://github.com/ahans30/Binoculars/blob/main/README.md"},{"title":"Publications - Valeriia Cherepanova - GitHub Pages","url":"https://vcherepanova.github.io/publications/"}]

Based on the search results, the full list of authors for the arxiv paper 2401.12070 "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" is: Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2873d784-794d-4e75-a956-72f8086de304",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "f7d0a8c3-c71a-4d98-a738-8ab14b816862",
  "sourceToolAssistantUUID": "2873d784-794d-4e75-a956-72f8086de304",
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

_source line 43 · 2026-05-26T10:25:29.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HP9W5M2zXUzpNkP1NnQ7vu`</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan TMLR accepted date 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7d0a8c3-c71a-4d98-a738-8ab14b816862",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR23DNQ466uHUfBwS7xQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b88da480-ddfc-4fd0-b6d3-2cb05a0fcd7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGVzZNNvdtutZG3xZoduRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 33397,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 33397,
          "cache_creation_input_tokens": 917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 917,
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

_source line 44 · 2026-05-26T10:25:38.468Z_

<details><summary>↩ Tool result · `toolu_01HP9W5M2zXUzpNkP1NnQ7vu`</summary>

```text
Web search results for query: ""Can AI-Generated Text be Reliably Detected" Sadasivan TMLR accepted date 2024 2025"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2024"}]

Based on the search results, I found information about the paper "Can AI-Generated Text be Reliably Detected?" by Sadasivan and colleagues:

**Paper Details:**
The paper is authored by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi.

**TMLR Status:**
The paper was previously submitted to TMLR, with the note that "all reviewers appreciated the technical developments of the paper and think this could be an exciting paper that addresses a very important and timely challenge". The authors modified the title to "Can AI-Generated Text be Reliably Detected?" following the reviews. The OpenReview page shows an update date of October 20, 2024.

**Main Contributions:**
The paper introduces a recursive paraphrasing attack to stress test the robustness of AI text detectors and provides a theoretical framework connecting the AUROC of the best possible detector to the Total Variation distance between human and AI text distributions.

**Key Finding:**
The authors show that these detectors are not reliable in practical scenarios, demonstrating that a recursive paraphrasing attack can break a whole range of detectors, including those using watermarking schemes, neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b88da480-ddfc-4fd0-b6d3-2cb05a0fcd7c",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "1c978068-4ab6-477d-8c92-74e8903e4595",
  "sourceToolAssistantUUID": "b88da480-ddfc-4fd0-b6d3-2cb05a0fcd7c",
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

_source line 45 · 2026-05-26T10:25:41.776Z_

Let me check the exact TMLR acceptance date and the title discrepancy more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c978068-4ab6-477d-8c92-74e8903e4595",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR243oCk48VgCX6mmikL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52171913-f4da-4465-abce-b6e3ebf209c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bbi3q6m8GZNAyY5iT6yCnC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 34314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 853,
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

_source line 46 · 2026-05-26T10:25:42.287Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FdeebR3pheorCqm8y8Wrse`</summary>

```json
{
  "query": "site:openreview.net \"OOgsAZdFOt\" TMLR accepted \"Stress Testing\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52171913-f4da-4465-abce-b6e3ebf209c3",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR243oCk48VgCX6mmikL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c88fc60-2b07-44b2-851e-29492c9ca7bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bbi3q6m8GZNAyY5iT6yCnC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 34314,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 853
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 34314,
          "cache_creation_input_tokens": 853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 853,
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

_source line 47 · 2026-05-26T10:25:47.778Z_

<details><summary>↩ Tool result · `toolu_01FdeebR3pheorCqm8y8Wrse`</summary>

```text
Web search results for query: "site:openreview.net "OOgsAZdFOt" TMLR accepted "Stress Testing""

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"TMLR - Transactions on Machine Learning Research","url":"https://openreview.net/group?id=TMLR"},{"title":"TMLR Event Certifications | OpenReview","url":"https://openreview.net/group?id=TMLR%2FEvent_Certifications&event=automl.cc%2FAutoML%2F2023%2FJournal_Track"},{"title":"Under review as submission to TMLR","url":"https://openreview.net/pdf/fa3ba1455b83eae92616443009ac0403a7409507.pdf"},{"title":"TMLR Submissions","url":"https://openreview.net/submissions?venue=TMLR"},{"title":"TMLR Expert Reviewers | OpenReview","url":"https://openreview.net/group?id=TMLR/Expert_Reviewers"},{"title":"TMLR | OpenReview","url":"https://dev.openreview.net/group?id=.TMLR"},{"title":"TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering | OpenReview","url":"https://openreview.net/forum?id=fXn4Rk8B3l"},{"title":"TMLR Submissions | OpenReview","url":"https://openreview.net/submissions?page=62&venue=TMLR"},{"title":"The Adaptive Stress Testing Formulation Mark Koren mkoren@stanford.edu","url":"https://openreview.net/pdf?id=rJgoNK-oaE"}]

Based on the search results, I found the paper you're looking for. The paper titled "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" is available at https://openreview.net/forum?id=OOgsAZdFOt on OpenReview.

The paper stress-tests the robustness of AI text detectors in the presence of an attacker. This is a TMLR submission that was previously submitted and has been updated based on reviewer feedback.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c88fc60-2b07-44b2-851e-29492c9ca7bb",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "ea21e433-43d8-432a-bdc4-350e548bb007",
  "sourceToolAssistantUUID": "4c88fc60-2b07-44b2-851e-29492c9ca7bb",
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

_source line 48 · 2026-05-26T10:25:50.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N7mcvpqP1ont73hDM4pv1q`</summary>

```json
{
  "query": "Sadasivan \"Stress Testing AI Text Detectors\" TMLR 2025 published accepted March"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea21e433-43d8-432a-bdc4-350e548bb007",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR24jcbbcCVAgqLFC3aK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d3e8fba-4ad0-4554-9850-3c1e806ce440",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012khUwiD6MaUw2mmseK6oNT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 35167,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 746
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 35167,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 746,
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

_source line 49 · 2026-05-26T10:25:59.282Z_

<details><summary>↩ Tool result · `toolu_01N7mcvpqP1ont73hDM4pv1q`</summary>

```text
Web search results for query: "Sadasivan "Stress Testing AI Text Detectors" TMLR 2025 published accepted March"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Stress-Sadasivan-Kumar/42f7d83e6c20fd4aaf3e3f53b18ab7db221ee300"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"M-DAIGT: A Shared Task on Multi-Domain Detection of AI-Generated Text","url":"https://arxiv.org/pdf/2511.11340"},{"title":"A Practical Examination of AI-Generated Text Detectors for Large   Language Models","url":"https://arxiv.org/pdf/2412.05139"},{"title":"Adversarial Attacks on AI-Generated Text Detection Models: A Token   Probability-Based Approach Using Embeddings","url":"https://arxiv.org/pdf/2501.18998"}]

Based on the search results, I found the paper you're looking for:

"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi was accepted and published at TMLR on March 13, 2025. The action editor was Kamalika Chaudhuri.

The paper introduces recursive paraphrasing attack to stress test the robustness of AI text detectors in the presence of an attacker, and provides a theoretical framework connecting the AUROC of the best possible detector to the Total Variation distance between human and AI text distributions.

The paper is available on OpenReview at: https://openreview.net/forum?id=OOgsAZdFOt


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d3e8fba-4ad0-4554-9850-3c1e806ce440",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "c1da6519-3304-4118-9b78-5b84c81629a6",
  "sourceToolAssistantUUID": "8d3e8fba-4ad0-4554-9850-3c1e806ce440",
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

_source line 50 · 2026-05-26T10:26:02.783Z_

Now let me verify the "Paraphrasing Evades" paper's exact title capitalization — the bib says "Paraphrasing Evades" with capital E, but the actual paper seems to use lowercase "evades".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1da6519-3304-4118-9b78-5b84c81629a6",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR25aoJNygegz1Vg7FCD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d96057a4-1d17-4058-a8aa-b58a3dafdea1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2LXyuTqYAtazU6T4jxiRf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 35913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 814,
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

_source line 51 · 2026-05-26T10:26:03.246Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KWYNKfKo1JRfp26HS7GQcz`</summary>

```json
{
  "query": "Krishna \"Paraphrasing evades detectors\" NeurIPS 2023 exact title capitalization proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d96057a4-1d17-4058-a8aa-b58a3dafdea1",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR25aoJNygegz1Vg7FCD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d544c30-4102-45bb-b8e6-b43fc6cdc27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2LXyuTqYAtazU6T4jxiRf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 35913,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 814
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 35913,
          "cache_creation_input_tokens": 814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 814,
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

_source line 52 · 2026-05-26T10:26:10.189Z_

<details><summary>↩ Tool result · `toolu_01KWYNKfKo1JRfp26HS7GQcz`</summary>

```text
Web search results for query: "Krishna "Paraphrasing evades detectors" NeurIPS 2023 exact title capitalization proceedings"

Links: [{"title":"NeurIPS Poster Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://neurips.cc/virtual/2023/poster/71402"},{"title":"GitHub - martiansideofthemoon/ai-detection-paraphrases: Official repository for our NeurIPS 2023 paper \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\" (https://arxiv.org/abs/2303.13408). · GitHub","url":"https://github.com/martiansideofthemoon/ai-detection-paraphrases"},{"title":"[PDF] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Paraphrasing-evades-detectors-of-AI-generated-text,-Krishna-Song/1c13af186d1e177b85ef1ec3fc7b8d33ec314cfd"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | OpenReview","url":"https://openreview.net/forum?id=WbFhFvjjKj"},{"title":"[2303.13408] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://papers.nips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://openreview.net/pdf?id=WbFhFvjjKj"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Request PDF","url":"https://www.researchgate.net/publication/369477232_Paraphrasing_evades_detectors_of_AI-generated_text_but_retrieval_is_an_effective_defense"},{"title":"No Free Lunch in LLM Watermarking: Trade-offs in Watermarking Design Choices","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/fa86a9c7b9f341716ccb679d1aeb9afa-Paper-Conference.pdf"}]

I found the paper you're looking for. Based on the search results, here is the exact title with proper capitalization as it appears in the NeurIPS 2023 proceedings:

"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense" by Kalpesh Krishna, Yixiao Song, Marzena Karpinska, John Wieting, and Mohit Iyyer, published in Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Main Conference Track.

The paper is available in the official NeurIPS proceedings at: https://papers.nips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d544c30-4102-45bb-b8e6-b43fc6cdc27c",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "4e5cbec0-2a5f-4206-9d31-055d30f12058",
  "sourceToolAssistantUUID": "9d544c30-4102-45bb-b8e6-b43fc6cdc27c",
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

_source line 53 · 2026-05-26T10:26:13.926Z_

Now let me also verify the DivEye paper venue — the bib says ICLR 2026, but an earlier search result mentioned TMLR and ICML 2025. Let me check more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e5cbec0-2a5f-4206-9d31-055d30f12058",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR26PPVCMKWzyDDdWEuR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9d53521-8487-49a0-ae21-2cfbc3a16502",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWMcTGP8qBWqvpfThRPEnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 36727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1025,
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

_source line 54 · 2026-05-26T10:26:14.461Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sv21S7zrtJxGdMrr5kBj4d`</summary>

```json
{
  "query": "DivEye \"Diversity Boosts AI-Generated Text Detection\" Basani venue ICLR 2026 TMLR published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9d53521-8487-49a0-ae21-2cfbc3a16502",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR26PPVCMKWzyDDdWEuR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa7972d2-cba4-4cbc-913b-ca7d6235dfa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWMcTGP8qBWqvpfThRPEnZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 36727,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1025
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 36727,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1025,
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

_source line 55 · 2026-05-26T10:26:24.083Z_

<details><summary>↩ Tool result · `toolu_01Sv21S7zrtJxGdMrr5kBj4d`</summary>

```text
Web search results for query: "DivEye "Diversity Boosts AI-Generated Text Detection" Basani venue ICLR 2026 TMLR published"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"DivEye","url":"https://diveye.vercel.app/"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"}]

Based on the search results, I found information about DivEye and the paper "Diversity Boosts AI-Generated Text Detection":

**Paper Details:**
The paper is authored by Advik Raj Basani from Birla Institute of Technology and Science, Goa and Pin-Yu Chen from IBM Research.

**Regarding Publication Venue:**
The search results show conflicting information about the venue:
- One source (GitHub) indicates the paper was published at "Data in Generative Models - The Bad, the Ugly, and the Greats" in 2025
- Another source (OpenReview) shows a different submission ID (DNgsOhGZBI) on OpenReview
- The paper also appeared as an arXiv preprint (2509.18880) submitted on September 23, 2025

The search results do not clearly confirm publication at ICLR 2026 or TMLR specifically. The GitHub repository mentions "TMLR '26" in the header, but the formal citation indicates a 2025 workshop venue. If you're looking for specific publication venue information, you may want to check OpenReview or the official conference proceedings directly.

**Main Contribution:**
DivEye is a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features, motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa7972d2-cba4-4cbc-913b-ca7d6235dfa6",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "4fe1f3b9-577a-4647-828d-fc2885367764",
  "sourceToolAssistantUUID": "fa7972d2-cba4-4cbc-913b-ca7d6235dfa6",
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

_source line 56 · 2026-05-26T10:26:26.880Z_

The GitHub repo says "TMLR '26", not ICLR 2026. Let me confirm this.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fe1f3b9-577a-4647-828d-fc2885367764",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR27Qq5R3zD28KPUDdja",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0881c09f-6e51-4842-a17c-c217a61034ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQtnTDpkkEmsjJ36UqN5U3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 37752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1095,
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

_source line 57 · 2026-05-26T10:26:27.231Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0194D7cf1BJv1pphQ3MjYxx4`</summary>

```json
{
  "query": "site:github.com/IBM/diveye TMLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0881c09f-6e51-4842-a17c-c217a61034ec",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR27Qq5R3zD28KPUDdja",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22d90739-6ec1-465b-9420-cb9919cfa4d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQtnTDpkkEmsjJ36UqN5U3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 37752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1095,
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

### Tool result

_source line 58 · 2026-05-26T10:26:33.398Z_

<details><summary>↩ Tool result · `toolu_0194D7cf1BJv1pphQ3MjYxx4`</summary>

```text
Web search results for query: "site:github.com/IBM/diveye TMLR 2026"

Links: [{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"Published in Transactions on Machine Learning Research (02/2026)","url":"https://arxiv.org/pdf/2509.18880"},{"title":"IBM on GitHub","url":"https://ibm.github.io/"},{"title":"TMLR Group · GitHub","url":"https://github.com/tmlr-group"},{"title":"International Business Machines · GitHub","url":"https://github.com/IBM"},{"title":"tmlr-2026 · GitHub Topics · GitHub","url":"https://github.com/topics/tmlr-2026"},{"title":"GitHub Enterprise - IBM","url":"https://github.ibm.com/login"},{"title":"IBM repositories · GitHub","url":"https://github.com/orgs/IBM/repositories"},{"title":"tmlr · GitHub Topics · GitHub","url":"https://github.com/topics/tmlr"},{"title":"IBM Security · GitHub","url":"https://github.com/ibm-security"}]

Based on the search results, I found relevant information about the IBM/diveye repository with TMLR 2026:

The repository is an official implementation of DivEye for the paper "Diversity Boosts AI-Generated Text Detection" which was accepted at TMLR '26 and ICML, Data in Generative Models (DIG-BUG) '25.

DivEye is motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs, and it captures this signal through a set of interpretable statistical features. The method outperforms existing zero-shot detectors by up to 33.2% and achieves competitive performance with fine-tuned baselines across multiple benchmarks.

DivEye is robust to paraphrasing and adversarial attacks, generalizes well across domains and models, and improves the performance of existing detectors by up to 18.7% when used as an auxiliary signal.

The GitHub repository is available at: https://github.com/IBM/diveye


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22d90739-6ec1-465b-9420-cb9919cfa4d4",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "3dbb9e71-6f6e-4b67-9236-8887e34523e4",
  "sourceToolAssistantUUID": "22d90739-6ec1-465b-9420-cb9919cfa4d4",
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

_source line 59 · 2026-05-26T10:26:37.116Z_

Good — the DivEye paper was published in TMLR (02/2026), NOT ICLR 2026. The bib entry has the wrong venue. Let me also check the "reliable_detection" title more carefully — there seem to be two versions of the paper title.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dbb9e71-6f6e-4b67-9236-8887e34523e4",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR286fDPZcZ6p3sh9sji",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5993265-5ee5-4b8f-9ef5-9413a576ddff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mob9CQGtRBTgiVSvSYF9Fj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 673,
      "cache_read_input_tokens": 38847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 673,
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

_source line 60 · 2026-05-26T10:26:37.439Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018TLLEkDuwsEg77VZ7uRDCx`</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected?\" shorter title without \"Stress Testing\" Sadasivan TMLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5993265-5ee5-4b8f-9ef5-9413a576ddff",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR286fDPZcZ6p3sh9sji",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31b7fa16-8e4f-486b-8ca5-5f5babddde7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mob9CQGtRBTgiVSvSYF9Fj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 673,
      "cache_read_input_tokens": 38847,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 673
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 38847,
          "cache_creation_input_tokens": 673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 673,
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

_source line 61 · 2026-05-26T10:26:45.933Z_

<details><summary>↩ Tool result · `toolu_018TLLEkDuwsEg77VZ7uRDCx`</summary>

```text
Web search results for query: ""Can AI-Generated Text be Reliably Detected?" shorter title without "Stress Testing" Sadasivan TMLR"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2023"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"}]

I found the paper you're looking for! Here's what I found:

**Paper Title:** "Can AI-Generated Text be Reliably Detected?"

**Authors:** Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi

**Publication:** Published at TMLR (Transactions on Machine Learning Research) with Kamalika Chaudhuri as the action editor

**Main Findings:** The paper shows that these detectors are not reliable in practical scenarios, developing a recursive paraphrasing attack to break a range of detectors, including watermarking schemes, neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.

**Additional Insights:** The paper provides a theoretical connection between the AUROC of the best possible detector and the Total Variation distance between human and AI text distributions.

The paper's arXiv version is available at: https://arxiv.org/abs/2303.11156
The full TMLR version is available at: https://openreview.net/forum?id=OOgsAZdFOt


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31b7fa16-8e4f-486b-8ca5-5f5babddde7d",
  "isSidechain": true,
  "promptId": "025a5fed-e9df-496c-a5ea-7dafa404a039",
  "agentId": "aaa614c25b326e871",
  "type": "user",
  "uuid": "d34befa7-7239-44dd-ad46-c9d7854eac7c",
  "sourceToolAssistantUUID": "31b7fa16-8e4f-486b-8ca5-5f5babddde7d",
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

_source line 62 · 2026-05-26T10:27:26.609Z_

The TMLR accepted version has the longer title "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" — which matches the bib entry. Now I have all the information I need. Let me compile the results.

Here are the verification results for all 12 bibliography entries:

---

### [cohen1988statistical] — Statistical Power Analysis for the Behavioral Sciences (1988)
- **Exists**: ✓
- **Authors**: ✓ (Jacob Cohen)
- **Year**: ✓ (1988, 2nd edition)
- **Title**: ✓
- **Venue**: ✓ (Lawrence Erlbaum Associates, 2nd edition)
- **Notes**: Classic reference book. No issues found.

### [detectgpt] — DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature (2023)
- **Exists**: ✓
- **Authors**: ✓ (Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn)
- **Year**: ✓ (2023)
- **Title**: ✓
- **Venue**: ✓ (ICML 2023, PMLR 202:24950-24962)
- **Notes**: No issues found.

### [gltr] — GLTR: Statistical Detection and Visualization of Generated Text (2019)
- **Exists**: ✓
- **Authors**: ✓ (Sebastian Gehrmann, Hendrik Strobelt, Alexander M. Rush)
- **Year**: ✓ (2019)
- **Title**: ✓
- **Venue**: ✓ (ACL 2019, System Demonstrations, pages 111-116)
- **Notes**: No issues found.

### [dna_gpt] — DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text (2024)
- **Exists**: ✓
- **Authors**: ✓ (Xianjun Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, Haifeng Chen)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (ICLR 2024)
- **Notes**: No issues found.

### [binoculars] — Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text (2024)
- **Exists**: ✓
- **Authors**: ✓ (Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, Tom Goldstein)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (ICML 2024, PMLR 235)
- **Notes**: No issues found.

### [fast_detectgpt] — Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature (2024)
- **Exists**: ✓
- **Authors**: ✓ (Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, Yue Zhang)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (ICLR 2024)
- **Notes**: No issues found.

### [ld_score] — Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (2026)
- **Exists**: ✓
- **Authors**: ✓ (Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber, Fardina Fathmiul Alam)
- **Year**: ✓ (2026, submitted May 3, 2026)
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2605.01647; under review at COLM 2026)
- **Notes**: No issues found.

### [diveye] — Diversity Boosts AI-Generated Text Detection (2026)
- **Exists**: ✓
- **Authors**: ✓ (Advik Raj Basani, Pin-Yu Chen)
- **Year**: ✓ (published 02/2026)
- **Title**: ✓
- **Venue**: **✗** — The bib entry says **ICLR 2026**, but the actual venue is **TMLR (Transactions on Machine Learning Research)**, published February 2026. The GitHub repo ([IBM/diveye](https://github.com/IBM/diveye)) explicitly states "[TMLR '26]". The arXiv PDF header also says "Published in Transactions on Machine Learning Research (02/2026)". This needs to be corrected.
- **Notes**: Venue must be changed from `ICLR 2026` to `Transactions on Machine Learning Research` with year 2026. The eprint 2509.18880 is correct.

### [feat_aug_transformer] — Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators (2026)
- **Exists**: ✓
- **Authors**: ✓ (Mohamed Mady, Johannes Reschke, Bjorn Schuller)
- **Year**: ✓ (2026, submitted May 5, 2026)
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2605.03969)
- **Notes**: No issues found.

### [reliable_detection] — Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks (2025)
- **Exists**: ✓
- **Authors**: ✓ (Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi)
- **Year**: ✓ (accepted/published at TMLR March 13, 2025)
- **Title**: ✓
- **Venue**: ✓ (Transactions on Machine Learning Research, 2025)
- **Notes**: No issues found.

### [paraphrase_evades] — Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense (2023)
- **Exists**: ✓
- **Authors**: ✓ (Kalpesh Krishna, Yixiao Song, Marzena Karpinska, John Wieting, Mohit Iyyer)
- **Year**: ✓ (2023)
- **Title**: ✓ (Note: the official NeurIPS proceedings use lowercase "evades" — "Paraphrasing evades detectors..." — but this is a BibTeX title-casing matter, not an accuracy issue.)
- **Venue**: ✓ (NeurIPS 2023)
- **Notes**: No issues found.

### [detection_possibilities] — Position: On the Possibilities of AI-Generated Text Detection (2024)
- **Exists**: ✓
- **Authors**: ✓ (Souradip Chakraborty, Amrit Singh Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, Furong Huang)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (ICML 2024, PMLR 235:6093-6115)
- **Notes**: No issues found.

---

**Summary**: 11 out of 12 entries are fully correct. **1 entry requires a fix**:

- **[diveye]**: Venue is wrong. Change from `ICLR 2026` to `Transactions on Machine Learning Research` (TMLR), year 2026. The paper was published in TMLR in February 2026 (not at ICLR 2026).

Sources:
- [Cohen 1988 - Routledge](https://www.routledge.com/Statistical-Power-Analysis-for-the-Behavioral-Sciences/Cohen/p/book/9780805802832)
- [DetectGPT - ICML Proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)
- [GLTR - ACL Anthology](https://aclanthology.org/P19-3019/)
- [DNA-GPT - arXiv](https://arxiv.org/abs/2305.17359)
- [Binoculars - ICML Proceedings](https://proceedings.mlr.press/v235/hans24a.html)
- [Fast-DetectGPT - OpenReview](https://openreview.net/forum?id=Bpcgcr8E8Z)
- [LD Score - arXiv](https://arxiv.org/abs/2605.01647)
- [DivEye - GitHub IBM/diveye](https://github.com/IBM/diveye)
- [DivEye - arXiv](https://arxiv.org/abs/2509.18880)
- [Feature-Augmented Transformers - arXiv](https://arxiv.org/abs/2605.03969)
- [Reliable Detection - OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt)
- [Paraphrasing Evades - NeurIPS Proceedings](https://papers.nips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html)
- [Detection Possibilities - ICML Proceedings](https://proceedings.mlr.press/v235/chakraborty24a.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d34befa7-7239-44dd-ad46-c9d7854eac7c",
  "isSidechain": true,
  "agentId": "aaa614c25b326e871",
  "requestId": "req_011CbR292DbaYNHWdy4dbV5V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a97c028a-0f26-4165-8723-347cec677d99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "15e38019-3588-43dd-b100-6a61dcca1f79",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FoL7QatENkUuxxhsHxTRK7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 39520,
      "output_tokens": 2496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2496,
          "cache_read_input_tokens": 39520,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1020,
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
