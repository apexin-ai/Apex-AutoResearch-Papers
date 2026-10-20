# Research conversation: I'm evaluating whether LLM judges can reliably annotate "diagnostic reasoning quality" in code repair trajectories. This

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5e1ca385a27e9225.jsonl`
- **Structured JSON:** [`0c740e51d524920af3e7.json`](../../sessions/0c/0c740e51d524920af3e7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-10T18:31:52.080Z_

I'm evaluating whether LLM judges can reliably annotate "diagnostic reasoning quality" in code repair trajectories. This is a key assumption in a paper I'm reviewing.

Please search for:
1. "LLM judge code correctness reliability" or "LLM as judge code quality" - how reliable are LLMs at judging code reasoning?
2. "inter-annotator agreement LLM judge" - what kappa values do LLM judges typically achieve?
3. "process reward model annotation quality" or "PRM label noise" - how noisy are PRM training labels?
4. "ThinkPRM arXiv 2504.16828" - verify this paper about data-efficient generative PRMs

I want to understand: Is it realistic to expect LLM judges to reliably distinguish "sound reasoning that led to a bad patch" from "unsound reasoning that happened to produce a good patch"? What does the literature say about LLM judge reliability for nuanced reasoning quality assessment?

Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a5e1ca385a27e9225",
  "type": "user",
  "uuid": "721e932c-fe15-460c-b4a6-49dea1c7ba25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:31:52.082Z_

```json
{
  "parentUuid": "721e932c-fe15-460c-b4a6-49dea1c7ba25",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e5f756cd-30f0-48e9-a713-82dd826b83b6",
  "timestamp": "2026-05-10T18:31:52.082Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T18:31:55.210Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01K1rp1cekKeZ7FQFMyXZVND`</summary>

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
  "parentUuid": "e5f756cd-30f0-48e9-a713-82dd826b83b6",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "requestId": "req_011CauNBupB2ZuT1Ca1cgitt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e07191ba-510c-4969-8cf9-3008d0549c83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TD2KWjMCbeBoSW9ZdfvX4x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 775
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 775,
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

_source line 4 · 2026-05-10T18:31:55.213Z_

<details><summary>↩ Tool result · `toolu_01K1rp1cekKeZ7FQFMyXZVND`</summary>

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
  "parentUuid": "e07191ba-510c-4969-8cf9-3008d0549c83",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a5e1ca385a27e9225",
  "type": "user",
  "uuid": "14fa4e7b-61d3-46da-92b5-b78e76ffcfb5",
  "sourceToolAssistantUUID": "e07191ba-510c-4969-8cf9-3008d0549c83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T18:31:58.381Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VDSsobc6HCk7ZuP3hSdb3H`</summary>

```json
{
  "query": "LLM judge code correctness reliability evaluation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14fa4e7b-61d3-46da-92b5-b78e76ffcfb5",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "requestId": "req_011CauNC9NWSeL6FGAVzNM6z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2ccfcc4-d4a7-444c-a973-3a31868dbb5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNMdWBhtu6uR1fvuEDN9NH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T18:31:58.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011ob9NZwZMWquPPJZr4iFSY`</summary>

```json
{
  "query": "inter-annotator agreement LLM judge kappa reliability 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2ccfcc4-d4a7-444c-a973-3a31868dbb5f",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "requestId": "req_011CauNC9NWSeL6FGAVzNM6z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acf1cba8-cfba-4f03-bd74-84031eb57cbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNMdWBhtu6uR1fvuEDN9NH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T18:31:59.378Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EnwLsCZJvoKNhCRGUqf4TT`</summary>

```json
{
  "query": "ThinkPRM arXiv 2504.16828 data-efficient generative process reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acf1cba8-cfba-4f03-bd74-84031eb57cbe",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "requestId": "req_011CauNC9NWSeL6FGAVzNM6z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ecb7efc-3073-4b08-9062-b1f43ced4a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNMdWBhtu6uR1fvuEDN9NH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T18:31:59.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019VQSWvJ2k3NEvmxm9srnw6`</summary>

```json
{
  "query": "process reward model annotation quality label noise PRM training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ecb7efc-3073-4b08-9062-b1f43ced4a8e",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "requestId": "req_011CauNC9NWSeL6FGAVzNM6z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "820365fd-5510-4aa3-8fc0-83dda980e45a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNMdWBhtu6uR1fvuEDN9NH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8998,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 8998,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 9 · 2026-05-10T18:32:05.900Z_

<details><summary>↩ Tool result · `toolu_01EnwLsCZJvoKNhCRGUqf4TT`</summary>

```text
Web search results for query: "ThinkPRM arXiv 2504.16828 data-efficient generative process reward model"

Links: [{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"},{"title":"ThinkPRM: Data-Efficient Process Reward Models","url":"https://www.emergentmind.com/papers/2504.16828"},{"title":"GitHub - mukhal/ThinkPRM: Process Reward Models That Think","url":"https://github.com/mukhal/thinkprm"},{"title":"Process Reward Models That Think | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.16828v4"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"THINKPRM: generative Process Reward Model for solution verification via long CoT Reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/thinkprm-generative-process-reward-model-for-solution-verification-via-long-cot-reasoning-2016f1e1387d"},{"title":"[2504.16828] Process Reward Models That Think - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2504.16828"},{"title":"launch/ThinkPRM-7B · Hugging Face","url":"https://huggingface.co/launch/ThinkPRM-7B"},{"title":"[2504.16828v1] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828v1"}]

I found detailed information about ThinkPRM (arXiv paper 2504.16828). Here's what I found:

## Overview

ThinkPRM is designed to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT).

## Key Features

ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs, outperforming LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks.

The verifiers are obtained by finetuning reasoning models over 1K synthetic verification CoTs filtered based on only 8K process labels from PRM800K.

## Performance Results

ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search. In out-of-domain evaluation on a subset of GPQA-Diamond and LiveCodeBench, ThinkPRM surpasses discriminative verifiers trained on the full PRM800K by 8% and 4.5%, respectively.

## Approach to Data Efficiency

Fine-tuning strong reasoning models on carefully curated, synthetic verification CoTs can yield verifiers that outperform models trained on much larger, traditionally labeled datasets, with process-based filtering (matching gold step labels) shown to be crucial for generating high-quality training data.

The code, data, and models are released at https://github.com/mukhal/thinkprm.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ecb7efc-3073-4b08-9062-b1f43ced4a8e",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a5e1ca385a27e9225",
  "type": "user",
  "uuid": "3dca179d-0d63-4c5e-9d02-4c789651259a",
  "sourceToolAssistantUUID": "3ecb7efc-3073-4b08-9062-b1f43ced4a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T18:32:06.180Z_

<details><summary>↩ Tool result · `toolu_01VDSsobc6HCk7ZuP3hSdb3H`</summary>

```text
Web search results for query: "LLM judge code correctness reliability evaluation 2024 2025"

Links: [{"title":"[2411.15594] A Survey on LLM-as-a-Judge","url":"https://arxiv.org/abs/2411.15594"},{"title":"LLM-as-a-judge: a complete guide to using LLMs for evaluations","url":"https://www.evidentlyai.com/llm-guide/llm-as-a-judge"},{"title":"LLM-as-a-Judge - Langfuse","url":"https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge"},{"title":"LLM-as-a-Judge: automated evaluation of search query parsing using large language models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12319771/"},{"title":"LLM-As-Judge: 7 Best Practices & Evaluation Templates","url":"https://www.montecarlodata.com/blog-llm-as-judge/"},{"title":"LLM-as-a-Judge Simply Explained: The Complete Guide to Run LLM Evals at Scale - Confident AI","url":"https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method"},{"title":"[2412.12509] Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge","url":"https://arxiv.org/abs/2412.12509"},{"title":"Judge Reliability Harness | RAND","url":"https://www.rand.org/pubs/tools/TLA4547-1.html"},{"title":"LLM as a Judge - Primer and Pre-Built Evaluators","url":"https://arize.com/llm-as-a-judge/"},{"title":"GitHub - CSHaitao/Awesome-LLMs-as-Judges: The official repo for paper, LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods. · GitHub","url":"https://github.com/CSHaitao/Awesome-LLMs-as-Judges"}]

Based on the search results, here's what recent research shows about LLM judges for code correctness and reliability evaluation:

## Key Findings on Code Correctness Evaluation

Research on LLMs evaluating code found that all major models performed better with one shot, but experienced declines when more examples were included. This suggests that prompt engineering with in-context examples requires careful calibration for code evaluation tasks.

LLM judges can assess code correctness against a known correct implementation, making them suitable for reference-based evaluations where ground truth exists.

## Reliability and Trustworthiness Concerns

Ensuring the reliability of LLM-as-a-Judge systems remains a significant challenge that requires careful design and standardization, with strategies needed to enhance reliability by improving consistency, mitigating biases, and adapting to diverse assessment scenarios.

Recent research has directly addressed reliability concerns. A novel framework for rigorously evaluating the reliability of LLM judgments using McDonald's omega has been introduced, evaluating the reliability of LLMs when judging the outputs of other LLMs on standard single-turn and multi-turn benchmarks while investigating the impact of temperature on reliability.

Research highlights reliability concerns including prompt sensitivity, verbosity bias, self-preference bias, miscalibration, and hallucination. To address these issues, the Judge Reliability Harness (JRH) was developed as an end-to-end framework for evaluating the reliability of automated LLM judges, generating and executing configurable test suites to systematically stress-test any LLM judge in situations where it may grade unreliably.

## Best Practices for Code Evaluation

Rather than simply asking an LLM-as-a-judge to output a score, requiring an explicit explanation or reasoning trace can be valuable, as chain-of-thought explanations tend to improve alignment with human judgements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2ccfcc4-d4a7-444c-a973-3a31868dbb5f",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a5e1ca385a27e9225",
  "type": "user",
  "uuid": "4deaaa6e-aefd-409e-b2fa-32a07ee12b35",
  "sourceToolAssistantUUID": "d2ccfcc4-d4a7-444c-a973-3a31868dbb5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T18:32:06.197Z_

<details><summary>↩ Tool result · `toolu_011ob9NZwZMWquPPJZr4iFSY`</summary>

```text
Web search results for query: "inter-annotator agreement LLM judge kappa reliability 2024"

Links: [{"title":"Judge’s Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement","url":"https://arxiv.org/html/2510.09738v1"},{"title":"Cohen, Fleiss & Krippendorff: IAA Metrics & Implementation - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/inter-annotator-agreement-kappa-alpha-reliability"},{"title":"Validating Annotation Agreement between Humans and LLMs | by Leanne Tan | AI Practice and Data Engineering Practice, GovTech | Medium","url":"https://medium.com/dsaid-govtech/validating-annotation-agreement-between-humans-and-llms-bc334245b1d9"},{"title":"Proceedings of the 9th Widening NLP Workshop, pages 251–267","url":"https://aclanthology.org/2025.winlp-main.37.pdf"},{"title":"Judge's Verdict: A Comprehensive Analysis of LLM ...","url":"https://arxiv.org/pdf/2510.09738"},{"title":"Inter-annotator Agreement","url":"https://www.researchgate.net/publication/318176345_Inter-annotator_Agreement"},{"title":"A Guide to Inter-rater Reliability and Annotator Agreement in AI","url":"https://imerit.net/resources/blog/human-vs-model-agreement-how-inter-rater-consistency-shapes-benchmark-reliability/"},{"title":"Inter-Annotator Agreement: An Introduction to Cohen’s Kappa Statistic | by Surge AI | Medium","url":"https://surge-ai.medium.com/inter-annotator-agreement-an-introduction-to-cohens-kappa-statistic-dcc15ffa5ac4"},{"title":"Inter-annotator Agreement Definition | OpenTrain AI Glossary","url":"https://www.opentrain.ai/glossary/inter-annotator-agreement/"},{"title":"Inter-Annotator Agreement: Building Datasets | Keymakr","url":"https://keymakr.com/blog/measuring-inter-annotator-agreement-building-trustworthy-datasets/"}]

I've performed a web search for your query on inter-annotator agreement, LLM judges, kappa reliability, and 2024 research. Here are the key findings:

## Recent Research on LLM Judges and Inter-Annotator Agreement

A comprehensive 2024-2025 study investigates whether LLMs can serve as reliable judges by comparing 54 different LLM judges against human annotators across 1,994 samples. 

### Key Methodological Innovations

Recent work has moved from correlation to agreement metrics, with researchers demonstrating that correlation alone is insufficient and progressing to Cohen's Kappa, which measures actual agreement rather than just linear relationships. A novel Turing Test for judges based on Cohen's Kappa agreement patterns asks "When mixed with human annotators, can we distinguish the LLM from typical human judges?" using z-score analysis of Cohen's Kappa values.

### Performance Benchmarks

Based on 1,994 items with 3 annotations each, the average human-human Cohen's Kappa is 0.801, establishing a benchmark for "human-level" performance. 27 Tier 1 judges demonstrate exceptional performance, with multiple models achieving high κ scores in the "substantial" to "almost perfect" range, including 4 models that are "super-consistent" and 23 models performing within human range.

### Practical Applications

As evaluation methodologies increasingly use LLMs as judges, the principles of chance-corrected agreement remain central, with validating an automated judge requiring measuring its agreement with human judgments using the same statistical rigor applied to human annotators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acf1cba8-cfba-4f03-bd74-84031eb57cbe",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a5e1ca385a27e9225",
  "type": "user",
  "uuid": "6bed2b14-e635-474f-acc5-3095d1649bde",
  "sourceToolAssistantUUID": "acf1cba8-cfba-4f03-bd74-84031eb57cbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:32:08.251Z_

<details><summary>↩ Tool result · `toolu_019VQSWvJ2k3NEvmxm9srnw6`</summary>

```text
Web search results for query: "process reward model annotation quality label noise PRM training"

Links: [{"title":"Towards Robust Process Reward Modeling via Noise-aware Learning","url":"https://arxiv.org/html/2601.12748"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"},{"title":"Free Process Rewards without Process Labels","url":"https://arxiv.org/html/2412.01981v1"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"FreePRM: Training Process Reward Models Without Ground Truth Process Labels - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250603570S/abstract"},{"title":"FreePRM: Training Process Reward Models Without ...","url":"https://www.arxiv.org/pdf/2506.03570"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"(PDF) Towards Robust Process Reward Modeling via Noise-aware Learning","url":"https://www.researchgate.net/publication/399932319_Towards_Robust_Process_Reward_Modeling_via_Noise-aware_Learning"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"DreamPRM-Code: Function-as-Step Process Reward Model with Label Correction for LLM Coding","url":"https://arxiv.org/html/2512.15000"}]

I've found comprehensive information on Process Reward Models (PRMs), annotation quality, label noise, and PRM training. Here's a summary of the key findings:

## Key Challenges in PRM Training

Building effective PRMs remains challenging due to the lack of scalable, high-quality annotations. Existing approaches rely on costly human labeling, LLM-based self-evaluation that is prone to hallucination, or Monte Carlo (MC) estimation, which infers step quality solely from rollout outcomes and often introduces noisy, misaligned supervision due to credit misattribution.

## Label Noise Issues

MCE assigns step-level labels by sampling K trajectories from a generative policy, but this procedure may produce false positives when an initially incorrect step is later corrected within a trajectory that still reaches the correct answer. Annotation models tend to both underestimate and overestimate step correctness due to limitations in their annotation capabilities.

## Recent Approaches to Address Noise

Several recent methods tackle annotation quality and label noise:

- **Reflection-aware correction**: One method addresses policy-dependent noise introduced by MCE through reflection-aware label correction during data annotation and noise-aware iterative training with selective label refinement.

- **Self-denoising frameworks**: SCAN introduces a self-denoising annotation framework that automatically detects and corrects noisy labels.

- **Weakly supervised approaches**: FreePRM generates pseudo step-level labels based on the correctness of final outcome, and employs Buffer Probability to eliminate impact of noise inherent in pseudo labeling.

- **Meta-learning label correction**: DreamPRM-Code introduces a meta-learning–based correction mechanism that leverages clean final-solution labels and performs bi-level optimization to refine intermediate labels.

PRM training remains sensitive to label quality, domain alignment, and overfitting to synthetic or LLM-generated errors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "820365fd-5510-4aa3-8fc0-83dda980e45a",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a5e1ca385a27e9225",
  "type": "user",
  "uuid": "b1d5bd66-a4f2-45c0-93a8-7e4eade59571",
  "sourceToolAssistantUUID": "820365fd-5510-4aa3-8fc0-83dda980e45a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T18:32:11.970Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017z5zSEYYxQayVW9nnAxcvx`</summary>

```json
{
  "query": "LLM judge reasoning quality assessment limitations bias nuanced evaluation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1d5bd66-a4f2-45c0-93a8-7e4eade59571",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "requestId": "req_011CauND6tiAzfZycSndy5wf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "754c5423-822a-479d-907b-6320b037bae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LwyDxtkoYsZ2kSjjPhUHb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3939,
      "cache_read_input_tokens": 10390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-10T18:32:12.699Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EvAPaPmmJh2Vdp3f5iK2gt`</summary>

```json
{
  "query": "\"LLM as judge\" code repair debugging reasoning evaluation reliability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "754c5423-822a-479d-907b-6320b037bae6",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "requestId": "req_011CauND6tiAzfZycSndy5wf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6133017-46dd-4a9c-bc0d-0eb2d5366a22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LwyDxtkoYsZ2kSjjPhUHb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3939,
      "cache_read_input_tokens": 10390,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3939
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 10390,
          "cache_creation_input_tokens": 3939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3939,
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

_source line 15 · 2026-05-10T18:32:20.473Z_

<details><summary>↩ Tool result · `toolu_017z5zSEYYxQayVW9nnAxcvx`</summary>

```text
Web search results for query: "LLM judge reasoning quality assessment limitations bias nuanced evaluation 2024 2025"

Links: [{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://llm-judge-bias.github.io/"},{"title":"Using LLMs for Evaluation - by Cameron R. Wolfe, Ph.D.","url":"https://cameronrwolfe.substack.com/p/llm-as-a-judge"},{"title":"A Survey on LLM-as-a-Judge","url":"https://arxiv.org/html/2411.15594v6"},{"title":"LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods","url":"https://arxiv.org/html/2412.05579v2"},{"title":"LLM-as-a-Judge: automated evaluation of search query parsing using large language models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12319771/"},{"title":"A Systematic Study of Position Bias in LLM-as-a-Judge","url":"https://aclanthology.org/2025.ijcnlp-long.18.pdf"},{"title":"LLM-as-a-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge | OpenReview","url":"https://openreview.net/forum?id=3GTtZFiajM"},{"title":"[2411.15594] A Survey on LLM-as-a-Judge","url":"https://arxiv.org/abs/2411.15594"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge [Quick Review]","url":"https://liner.com/review/justice-or-prejudice-quantifying-biases-in-llmasajudge"}]

I've successfully performed the web search on LLM judge reasoning quality assessment, limitations, bias, and nuanced evaluation. Here are the key findings from recent 2024-2025 research:

## Major Findings

**Core Limitations and Biases:**

LLM judges exhibit potential biases regarding verbosity (favoring longer responses), fallacy oversight (ignoring logical errors in reasoning), and sentiment preferences. Additionally, LLMs have questionable reasoning capabilities, sensitivity to minor changes in the prompt, and a tendency to generate verbose outputs.

**Position Bias Issues:**

Judges may systematically favor responses based on order (primacy/recency preference), with metrics like repetition stability, position consistency, and preference fairness characterizing this phenomenon, and in pairwise code judging, simply swapping the presentation order of responses can lead to accuracy shifts exceeding 10%.

**Reasoning Quality Assessment Challenges:**

Researchers have identified 12 key potential biases and proposed the CALM framework to systematically quantify each type of bias, finding that while advanced models achieve commendable overall performance, significant biases persist in certain specific tasks.

**Nuanced Assessment Capabilities:**

LLM-as-a-Judge can enhance evaluation reliability by addressing challenges such as bias mitigation, prompt engineering, and standardization of evaluation methodologies, with LLMs offering more nuanced assessments compared to rule-based or heuristic metrics, particularly in tasks requiring semantic alignment.

**Human-AI Collaboration:**

LLMs can work alongside human evaluators, combining the efficiency of automated evaluation with the nuanced judgment of human expertise, allowing human evaluators to mitigate potential biases in the LLM's output.

The research emphasizes that ensuring the reliability of LLM-as-a-Judge systems remains a significant challenge requiring careful design and standardization, with strategies including improving consistency, mitigating biases, and adapting to diverse assessment scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "754c5423-822a-479d-907b-6320b037bae6",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a5e1ca385a27e9225",
  "type": "user",
  "uuid": "aa276512-6dc3-4da4-858f-5f407b1b53d0",
  "sourceToolAssistantUUID": "754c5423-822a-479d-907b-6320b037bae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:32:24.516Z_

<details><summary>↩ Tool result · `toolu_01EvAPaPmmJh2Vdp3f5iK2gt`</summary>

```text
Web search results for query: ""LLM as judge" code repair debugging reasoning evaluation reliability"

Links: [{"title":"LLM-as-a-judge: a complete guide to using LLMs for evaluations","url":"https://www.evidentlyai.com/llm-guide/llm-as-a-judge"},{"title":"LLM-as-a-Judge for Human-AI Co-Creation: A Reliability-Aware Evaluation Framework for Coding","url":"https://arxiv.org/html/2604.27727"},{"title":"LLM-As-Judge: 7 Best Practices & Evaluation Templates","url":"https://www.montecarlodata.com/blog-llm-as-judge/"},{"title":"LLM-as-a-Judge - Langfuse","url":"https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge"},{"title":"Utilising LLM-as-a-Judge to Evaluate LLM-Generated Code by cbarkinozer | Softtech","url":"https://medium.com/softtechas/utilising-llm-as-a-judge-to-evaluate-llm-generated-code-451e9631c713"},{"title":"[2507.10535] CodeJudgeBench: Benchmarking LLM-as-a-Judge for Coding Tasks","url":"https://arxiv.org/abs/2507.10535"},{"title":"Uncovering Systematic Failures of LLMs in Verifying Code Against Natural Language Specifications","url":"https://arxiv.org/html/2508.12358v1"},{"title":"Reasoning Trajectories for Socratic Debugging of Student Code: From Misconceptions to Contradictions and Updated Beliefs","url":"https://arxiv.org/html/2511.00371v1"},{"title":"Exploring LLM-as-a-Judge - Weights & Biases","url":"https://wandb.ai/site/articles/exploring-llm-as-a-judge/"},{"title":"Benchmarking LLM-as-a-Judge for Coding Tasks","url":"https://arxiv.org/pdf/2507.10535"}]

I've completed a web search on "LLM as judge" code repair debugging reasoning evaluation reliability. Here are the key findings:

## Overview

LLM-as-a-judge is a common technique to evaluate LLM-powered products that emerged as a practical alternative to costly human evaluation when assessing open-ended text outputs. LLM-as-a-Judge is an evaluation methodology where an LLM is used to assess the quality of outputs produced by another LLM application, instead of relying solely on human reviewers or simple heuristic metrics.

## Reliability and Performance

Research shows mixed results regarding reliability:

- Strong LLM judges (such as GPT-5 class models) achieve 80-90% agreement with human evaluators on many quality dimensions, which is comparable to inter-annotator agreement between humans.

- However, for coding specifically, Most papers agree that LLMs struggle to judge if code works without running it, with even GPT-4-turbo frequently misclassifying wrong code as correct (False Positives) and correct code as wrong (False Negatives).

## Reasoning and Code Evaluation

Guiding LLMs to perform "slow thinking" via step-by-step analysis and taxonomy-based fault categorisation enables reliable code evaluation, with "thinking" models and large reasoning models (GPT-4o, Claude 3.5 Sonnet) significantly outperforming specialised, smaller judge models.

However, there's a paradox with complex prompts: When models are prompted to explain and propose fixes, models become significantly more prone to incorrectly classifying conforming code as erroneous, introducing reasoning and correction steps induces an overcorrection bias.

## Key Debugging Insights

Asking for reasoning helps improve evaluation quality and debugging. Additionally, retaining comments and reasoning in the full, unprocessed LLM response leads to improved judge performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6133017-46dd-4a9c-bc0d-0eb2d5366a22",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a5e1ca385a27e9225",
  "type": "user",
  "uuid": "308a71bd-dd1a-4a58-a1d7-a9d1cf179235",
  "sourceToolAssistantUUID": "d6133017-46dd-4a9c-bc0d-0eb2d5366a22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T18:32:28.052Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ASt1eYHr1gTPHG5nxCPBHe`</summary>

```json
{
  "query": "PRM800K label noise rate annotation accuracy human annotator disagreement process supervision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "308a71bd-dd1a-4a58-a1d7-a9d1cf179235",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "requestId": "req_011CauNEJVEy9R9TpLgf7BJ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5fe6257-77e5-4461-bb57-4b3fcc0a2aaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8GAo6HSzmJpBEXbo7Lfzy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 14329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2089,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T18:32:29.076Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015s5QAbtpkdghAy9rZgTESF`</summary>

```json
{
  "query": "\"Can You Trust LLM Judgments\" arXiv 2412.12509 reliability McDonald omega"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5fe6257-77e5-4461-bb57-4b3fcc0a2aaa",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "requestId": "req_011CauNEJVEy9R9TpLgf7BJ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34770fa8-7a66-42eb-91d6-73b1d5ccd751",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8GAo6HSzmJpBEXbo7Lfzy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 14329,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2089
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 14329,
          "cache_creation_input_tokens": 2089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2089,
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

_source line 19 · 2026-05-10T18:32:36.359Z_

<details><summary>↩ Tool result · `toolu_015s5QAbtpkdghAy9rZgTESF`</summary>

```text
Web search results for query: ""Can You Trust LLM Judgments" arXiv 2412.12509 reliability McDonald omega"

Links: [{"title":"[2412.12509] Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge","url":"https://arxiv.org/abs/2412.12509"},{"title":"Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge","url":"https://arxiv.org/html/2412.12509v2"},{"title":"[Literature Review] Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge","url":"https://www.themoonlight.io/en/review/can-you-trust-llm-judgments-reliability-of-llm-as-a-judge"},{"title":"Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge | alphaXiv","url":"https://www.alphaxiv.org/overview/2412.12509v2"},{"title":"Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge","url":"https://www.researchgate.net/publication/387141270_Can_You_Trust_LLM_Judgments_Reliability_of_LLM-as-a-Judge"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/html/2602.00521v1"},{"title":"Model grading • evalthat","url":"https://simonpcouch.github.io/evalthat/articles/model-grading.html"},{"title":"Who Judges the Judge? LLM Jury-on-Demand:","url":"https://arxiv.org/pdf/2512.01786"},{"title":"An Empirical Study of LLM-as-a-Judge: How Design Choices Impact Evaluation Reliability","url":"https://arxiv.org/html/2506.13639v1"},{"title":"Label Effects: Shared Heuristic Reliance in Trust Assessment by Humans and LLM-as-a-Judge","url":"https://arxiv.org/html/2604.05593"}]

Based on the search results, I found detailed information about the paper "Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge" (arXiv 2412.12509).

## Overview

The paper introduces a novel framework for rigorously evaluating the reliability of LLM judgments, leveraging McDonald's omega. The paper by Kayla Schroeder and Zach Wood-Doughty delves into the reliability of Large Language Models (LLMs) when functioning as evaluative judges.

## Key Problem

Large Language Models have become increasingly powerful and ubiquitous, but their stochastic nature poses challenges to the reliability of their outputs. While deterministic settings can improve consistency, they do not guarantee reliability, as a single sample from the model's probability distribution can still be misleading.

## Methodology

The paper introduces a novel framework for rigorously evaluating the reliability of LLM judgments, leveraging McDonald's omega. Metrics like Cronbach's alpha and McDonald's omega provide quantifiable measures of internal consistency, allowing assessment of the reliability of an LLM's evaluations by examining the consistency of its responses across a range of prompts or tasks.

The work pioneers the systematic investigation of the variability of an LLM evaluator's judgments solely by varying the random seed, holding all other parameters constant.

## Key Findings

The researchers evaluate the reliability of LLMs when judging the outputs of other LLMs on standard single-turn and multi-turn benchmarks, simultaneously investigating the impact of temperature on reliability. By analyzing these results, they demonstrate the limitations of fixed randomness and the importance of considering multiple samples, which has significant implications for downstream applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34770fa8-7a66-42eb-91d6-73b1d5ccd751",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a5e1ca385a27e9225",
  "type": "user",
  "uuid": "dd975b30-f730-4a1d-a31e-54380760c545",
  "sourceToolAssistantUUID": "34770fa8-7a66-42eb-91d6-73b1d5ccd751",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T18:32:37.504Z_

<details><summary>↩ Tool result · `toolu_01ASt1eYHr1gTPHG5nxCPBHe`</summary>

```text
Web search results for query: "PRM800K label noise rate annotation accuracy human annotator disagreement process supervision"

Links: [{"title":"PRM800K: A Process Supervision Dataset","url":"https://github.com/openai/prm800k"},{"title":"Improve Mathematical Reasoning in Language Models by ...","url":"https://arxiv.org/pdf/2406.06592"},{"title":"PRM800K download | SourceForge.net","url":"https://sourceforge.net/projects/prm800k.mirror/"},{"title":"Improve Mathematical Reasoning in Language Models by Automated Process Supervision","url":"https://arxiv.org/html/2406.06592v1"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prms"},{"title":"SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning","url":"https://openreview.net/pdf/90e683c8f88b8fe14fd41acb175f70e1cbcdd305.pdf"},{"title":"Supervised Training for PRMs — a brief dive into the training script | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/supervised-training-for-prms-a-brief-dive-into-the-training-script-64594d4bdc05"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://aclanthology.org/2025.emnlp-main.679.pdf"},{"title":"From Ground Truth to Measurement: A Statistical Framework for Human Labeling","url":"https://arxiv.org/html/2604.07591"},{"title":"GitHub - scottlogic-alex/prm800k-denorm: Script for processing OpenAI's PRM800K process supervision dataset into an Alpaca-style instruction-response format","url":"https://github.com/scottlogic-alex/prm800k-denorm/"}]

I found comprehensive information about PRM800K and related annotation topics. Here's what the search revealed:

## PRM800K Overview

PRM800K is a process supervision dataset containing 800,000 step-level correctness labels for model-generated solutions to problems from the MATH dataset.

## Annotation Quality and Label Noise

PRM800K and similar corpora employ domain experts for stepwise labeling, yielding gold-standard but costly labels (~10⁴–10⁵ samples). However, the precise impact of noise on PRM performance remains uncertain.

## Human Annotator Disagreement and Process Supervision

The research on annotation quality indicates that annotators may disagree with one another, make occasional mistakes, or interpret ambiguous inputs differently. From the perspective of model training, these discrepancies manifest as label noise.

In the context of process supervision, pool-based active learning approaches (e.g., ActPRM) select only high-uncertainty or disagreement cases for gold annotation, reducing overall labeling budget by over 50% while matching accuracy of full data regimes.

## Comparison with Automated Annotations

Methods such as MathShepherd, OmegaPRM, URSA apply symbolic solvers, MCTS, or runtime tests to pinpoint the first error or verify step correctness at scale. These methods introduce label noise due to misattribution and artifacts of non-human rationale.

Human-annotated PRM800K remains a benchmark, though with only 101K synthetic samples from the SCAN-Base dataset, generated by the 1.5B model, the Qwen2.5-Math-7B-SCAN-Base model outperforms PRMs trained on larger synthetic datasets and approaches the performance of PRMs trained on human-annotated data (PRM800K).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5fe6257-77e5-4461-bb57-4b3fcc0a2aaa",
  "isSidechain": true,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "agentId": "a5e1ca385a27e9225",
  "type": "user",
  "uuid": "b300dadd-a1b5-4393-bce8-0c768aee74a2",
  "sourceToolAssistantUUID": "c5fe6257-77e5-4461-bb57-4b3fcc0a2aaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T18:33:21.458Z_

Here is my synthesis of the literature on LLM judge reliability for diagnostic reasoning quality in code repair trajectories:

---

## Summary of Findings

### 1. LLM Judge Reliability for Code Correctness

The evidence is **mixed but cautionary** for your specific use case:

- **General agreement rates**: Top-tier LLM judges achieve Cohen's Kappa of ~0.8 with humans on straightforward evaluation tasks (comparable to human-human agreement). However, this is for relatively clear-cut quality dimensions, not nuanced reasoning assessment.
- **Code-specific weakness**: LLMs frequently misclassify wrong code as correct (false positives) and correct code as wrong (false negatives) when they cannot execute the code. This is a fundamental limitation for judging "diagnostic reasoning quality" without execution feedback.
- **Overcorrection bias**: When prompted to explain reasoning and propose fixes, models become *more* prone to incorrectly classifying conforming code as erroneous -- a direct concern for your scenario of distinguishing sound-but-unsuccessful reasoning from unsound-but-lucky reasoning.

### 2. Inter-Annotator Agreement (Kappa Values)

- A comprehensive study of 54 LLM judges across 1,994 samples found average human-human Cohen's Kappa of **0.801** as the benchmark.
- **27 Tier-1 judges** achieved "substantial" to "almost perfect" agreement (kappa in the 0.6-0.8+ range) on standard tasks.
- However, [arXiv 2412.12509](https://arxiv.org/abs/2412.12509) demonstrates that even at fixed temperature, varying only the random seed produces significant judgment variability -- reliability (McDonald's omega) degrades for more nuanced assessments.
- **Position bias** can shift accuracy by 10%+ in pairwise code judgments just from swapping presentation order.

### 3. PRM Label Noise

This is where the picture gets most concerning for your paper's assumption:

- **PRM800K** (the gold-standard process supervision dataset) uses expensive human expert annotation, yet Monte Carlo Estimation (MCE) methods used for scaling introduce **false positives** when an initially incorrect step is later corrected within a trajectory that still reaches the correct answer -- a direct analog to your "unsound reasoning that happened to produce a good patch" scenario.
- **Credit misattribution** is a known, fundamental problem: MCE assigns step-level labels based on rollout outcomes, leading to noisy, misaligned supervision.
- Recent papers (SCAN, FreePRM, DreamPRM-Code) all exist precisely because label noise is so severe that entire research programs focus on denoising PRM annotations.

### 4. ThinkPRM (arXiv 2504.16828) -- Verified

ThinkPRM is real and demonstrates that **generative verification via chain-of-thought outperforms discriminative PRMs** using only ~1% of PRM800K's process labels (fine-tuned on ~1K synthetic verification CoTs filtered using only 8K gold labels). Key results:
- Outperforms LLM-as-a-Judge baselines on ProcessBench, MATH-500, AIME '24
- Surpasses discriminative verifiers trained on full PRM800K by 8% (GPQA-Diamond) and 4.5% (LiveCodeBench) out-of-domain

This suggests that *if* you use a reasoning model as the judge (generating explicit verification traces), you get substantially better step-level assessment than naive LLM-as-a-Judge approaches.

---

## Direct Answer to Your Question

**Is it realistic to expect LLM judges to reliably distinguish "sound reasoning that led to a bad patch" from "unsound reasoning that happened to produce a good patch"?**

**Probably not with standard LLM-as-a-Judge setups.** The literature indicates:

1. **The exact failure mode you describe is a known problem**: MCE-based PRM labels suffer from precisely this credit misattribution -- correct outcomes mask incorrect intermediate steps, and incorrect outcomes mask correct intermediate reasoning.

2. **LLM judges without execution struggle with code correctness**: They cannot reliably determine whether code works without running it, making judgments about reasoning *quality* even harder.

3. **Achievable reliability degrades with task nuance**: Kappa values of 0.8 are for relatively clear evaluations. For "diagnostic reasoning quality" -- a subjective, multi-dimensional construct -- expect substantially lower agreement.

4. **Mitigation exists but requires care**: ThinkPRM-style generative verification (having the judge produce explicit reasoning traces about each step) significantly outperforms naive judging. Chain-of-thought evaluation and "slow thinking" prompts help, but introduce overcorrection bias.

**Bottom line**: The paper you're reviewing should acknowledge this as a significant threat to validity. LLM judges can *approximate* reasoning quality annotations, but the literature suggests 10-20%+ error rates on nuanced code reasoning distinctions, with systematic biases (verbosity preference, position effects, overcorrection) that could confound results. The strongest mitigation would be a ThinkPRM-style generative verifier with human-validated calibration on a subset.

---

Sources:
- [A Survey on LLM-as-a-Judge (arXiv 2411.15594)](https://arxiv.org/abs/2411.15594)
- [Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge (arXiv 2412.12509)](https://arxiv.org/abs/2412.12509)
- [Judge's Verdict: LLM Judge Capability Through Human Agreement](https://arxiv.org/html/2510.09738v1)
- [ThinkPRM: Process Reward Models That Think (arXiv 2504.16828)](https://arxiv.org/abs/2504.16828)
- [Towards Robust Process Reward Modeling via Noise-aware Learning](https://arxiv.org/html/2601.12748)
- [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://llm-judge-bias.github.io/)
- [LLM-as-a-Judge for Human-AI Co-Creation: A Reliability-Aware Evaluation Framework for Coding](https://arxiv.org/html/2604.27727)
- [CodeJudgeBench: Benchmarking LLM-as-a-Judge for Coding Tasks (arXiv 2507.10535)](https://arxiv.org/abs/2507.10535)
- [SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning](https://openreview.net/pdf/90e683c8f88b8fe14fd41acb175f70e1cbcdd305.pdf)
- [Free Process Rewards without Process Labels](https://arxiv.org/html/2412.01981v1)
- [RAND Judge Reliability Harness](https://www.rand.org/pubs/tools/TLA4547-1.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b300dadd-a1b5-4393-bce8-0c768aee74a2",
  "isSidechain": true,
  "agentId": "a5e1ca385a27e9225",
  "requestId": "req_011CauNFG7Q9U345wdGCaGMN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b01e135-09b3-45cc-81a0-660629db1389",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CotcafPa45UXEAKHgmwQN1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 16418,
      "output_tokens": 1672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1059
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 971,
          "output_tokens": 1672,
          "cache_read_input_tokens": 16418,
          "cache_creation_input_tokens": 1059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1059,
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
