# Research conversation: I'm conducting an adversarial review of a research proposal called "SeMutFL: Contrastive Mutation Augmentation for Surfa

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a3f1dbc964cde1dc5.jsonl`
- **Structured JSON:** [`f711c70bdd599075b48a.json`](../../sessions/f7/f711c70bdd599075b48a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-10T06:25:51.681Z_

I'm conducting an adversarial review of a research proposal called "SeMutFL: Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding in Fault Localization." I need you to search for and verify several claims. Please conduct the following searches and report what you find:

1. Search for arXiv paper 2504.04372 - "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models" - does it exist and does it report a 78% failure rate under semantic-preserving mutations?

2. Search for arXiv paper 2505.10443 - "Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?" - does it exist and does it show performance drops up to 70% across nine LLMs?

3. Search for RGFL (arXiv 2601.18044) - "Reasoning Guided Fault Localization for LLM-Based Automated Program Repair" - does it exist and does it report 85% Hit@1 on SWE-bench Verified?

4. Search for arXiv 2602.11411 - "Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data" - does it exist and does it apply NLP-level perturbations (typos, synonyms, back-translation) rather than semantic-preserving code mutations?

5. Search for any NEW papers from March-May 2026 that address surface-form robustness in fault localization via contrastive learning or mutation augmentation for LLMs. Try searches like:
   - "fault localization robustness contrastive 2026"
   - "semantic mutation augmentation code LLM 2026"
   - "code understanding surface-form invariance training 2026"
   - site:arxiv.org "fault localization" "contrastive" "mutation" 2026

6. Search for SWE-Gym (arXiv 2412.21139) - specifically verify: does it describe training with 491 trajectories × 18,578 avg tokens for 32B LoRA on H100 hardware? Does Table 8 contain these token statistics?

Report findings concisely for each item.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "41ce2739-23ff-4d13-9aaf-24f12e36477c",
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

_source line 2 · 2026-05-10T06:25:52.891Z_

I'll conduct a thorough search for these papers and claims. Let me start by searching for each arXiv paper and related information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41ce2739-23ff-4d13-9aaf-24f12e36477c",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQptSaxUfn3pZ9BByur",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d2f669b6-2f4e-4331-92a4-030f67785f76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017wa7QkvSWQFn99SnjntYhh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 947,
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

_source line 3 · 2026-05-10T06:25:53.365Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HjVGsY4n5dqqTGD6g7UoNz`</summary>

```json
{
  "query": "arXiv 2504.04372 \"Assessing the Impact of Code Changes on the Fault Localizability\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2f669b6-2f4e-4331-92a4-030f67785f76",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQptSaxUfn3pZ9BByur",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "16ecb4d2-15f9-443d-ba31-de7b16809859",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017wa7QkvSWQFn99SnjntYhh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 947,
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

_source line 4 · 2026-05-10T06:25:53.389Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017NHNZSgNq6xKvkSDmgHYPh`</summary>

```json
{
  "query": "arXiv 2505.10443 \"Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16ecb4d2-15f9-443d-ba31-de7b16809859",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQptSaxUfn3pZ9BByur",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad4a9ac0-c942-437d-8b4a-17660d207a4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017wa7QkvSWQFn99SnjntYhh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 947,
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

_source line 5 · 2026-05-10T06:25:53.538Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lsdvn7j3jBCCpWd1RppVPK`</summary>

```json
{
  "query": "arXiv 2601.18044 RGFL \"Reasoning Guided Fault Localization\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad4a9ac0-c942-437d-8b4a-17660d207a4e",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQptSaxUfn3pZ9BByur",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04dbf558-d04e-4635-8499-4922dcf3c014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017wa7QkvSWQFn99SnjntYhh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 947,
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

_source line 6 · 2026-05-10T06:25:53.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DTTcV5BG7cbXFEqspDBFwo`</summary>

```json
{
  "query": "arXiv 2602.11411 \"Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04dbf558-d04e-4635-8499-4922dcf3c014",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQptSaxUfn3pZ9BByur",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a4fb78b7-aca2-44cb-9ae4-094465fdc7b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017wa7QkvSWQFn99SnjntYhh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 16155,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 947
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 947,
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

_source line 7 · 2026-05-10T06:25:53.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KShyYo7MyWTvAGUQJV74t8`</summary>

```json
{
  "query": "arXiv 2412.21139 SWE-Gym \"491 trajectories\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4fb78b7-aca2-44cb-9ae4-094465fdc7b8",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQptSaxUfn3pZ9BByur",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7dd82fd5-00fe-4c94-9ef2-6dd6949aca65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017wa7QkvSWQFn99SnjntYhh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 16155,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 947
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 947,
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

_source line 8 · 2026-05-10T06:25:58.636Z_

<details><summary>↩ Tool result · `toolu_01HjVGsY4n5dqqTGD6g7UoNz`</summary>

```text
Web search results for query: "arXiv 2504.04372 "Assessing the Impact of Code Changes on the Fault Localizability""

Links: [{"title":"[2504.04372] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372"},{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"[2504.04372v3] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372v3"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372v3"},{"title":"Bytez","url":"https://bytez.com/docs/arxiv/2504.04372/paper"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250404372H/abstract"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2504.04372v3"},{"title":"How Accurately Do Large Language Models Understand Code?","url":"https://www.arxiv.org/pdf/2504.04372"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (ICST 2026 - Research Papers) - ICST 2026","url":"https://conf.researchr.org/details/icst-2026/icst-2026-research/30/Assessing-the-Impact-of-Code-Changes-on-the-Fault-Localizability-of-Large-Language-Mo"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://zenodo.org/records/18803969"}]

I found the research paper arXiv 2504.04372. Here's a summary of what it contains:

## Paper Overview

The paper is titled "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models" and was accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026).

## Main Research Focus

The paper examines how Generative Large Language Models (LLMs) are increasingly used in non-generative software maintenance tasks, such as fault localization (FL), and notes that success in FL depends on a model's ability to reason about program semantics beyond surface-level syntactic and lexical features, whereas widely used LLM benchmarks primarily evaluate code generation, which differs fundamentally from semantic program reasoning.

## Key Methodology

The researchers develop an evaluation framework inspired by mutation testing, where they inject unseen faults and ask LLMs to localize them, filter out underspecified programs, and for each program an LLM successfully localizes, they apply semantic-preserving mutations (SPMs) and rerun localization to assess the LLM's robustness.

## Key Findings

The researchers evaluated 10 state-of-the-art LLMs on approximately 1,300 Java and Python programs and observed that SPMs cause an LLM to fail to localize the same fault it correctly localized earlier in 78% of cases, with LLMs' reasoning on code found earlier in the context being noticeably better.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16ecb4d2-15f9-443d-ba31-de7b16809859",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "967d9c1d-7cf3-4c3e-b2f4-d1382f480eb6",
  "sourceToolAssistantUUID": "16ecb4d2-15f9-443d-ba31-de7b16809859",
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

_source line 9 · 2026-05-10T06:26:00.897Z_

<details><summary>↩ Tool result · `toolu_017NHNZSgNq6xKvkSDmgHYPh`</summary>

```text
Web search results for query: "arXiv 2505.10443 "Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations""

Links: [{"title":"[2505.10443] Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?","url":"https://arxiv.org/abs/2505.10443"},{"title":"Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?","url":"https://arxiv.org/html/2505.10443"},{"title":"Are Large Language Models Robust in Understanding Code Against","url":"https://arxiv.org/pdf/2505.10443"},{"title":"How Accurately Do Large Language Models Understand Code?","url":"https://arxiv.org/html/2504.04372v1"},{"title":"[2504.04372v1] How Accurately Do Large Language Models Understand Code?","url":"https://arxiv.org/abs/2504.04372v1"},{"title":"How Accurately Do Large Language Models Understand Code?","url":"https://www.arxiv.org/pdf/2504.04372"},{"title":"Assessing Code Understanding in LLMs","url":"https://arxiv.org/html/2504.00065"},{"title":"[2504.04372v3] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372v3"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372v3"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"}]

I found the paper you're looking for. Here's information about arXiv paper 2505.10443:

## Paper Overview

The paper titled "Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?" is authored by Pedro Orvalho and Marta Kwiatkowska.

## Main Research Question and Approach

The paper addresses the critical question of understanding the reasoning and robustness of LLMs in programming tasks, noting that while recent studies assess LLMs' ability to predict program outputs, most focus solely on accuracy without evaluating the reasoning, and that LLMs can arrive at correct answers through flawed logic on mathematical reasoning tasks.

## Methodology

The researchers evaluate whether state-of-the-art LLMs with up to 8B parameters can reason about Python programs by applying five semantics-preserving code mutations: renaming variables, mirroring comparison expressions, swapping if-else branches, converting for loops to while loops, and unrolling loop iterations. These mutations maintain program semantics while altering its syntax.

The study evaluated six LLMs and performed human expert analysis using LiveCodeBench to assess whether correct predictions are based on sound reasoning, and evaluated prediction stability across different code mutations on LiveCodeBench and CruxEval.

## Key Findings

The findings show that LLMs trained for code produce correct predictions based on flawed reasoning between 10% and 50% of cases. Furthermore, LLMs often change predictions in response to code mutations, indicating they do not yet exhibit stable, semantically grounded reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad4a9ac0-c942-437d-8b4a-17660d207a4e",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "0af7c124-4505-43dc-a947-25b8dba0902f",
  "sourceToolAssistantUUID": "ad4a9ac0-c942-437d-8b4a-17660d207a4e",
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

_source line 10 · 2026-05-10T06:26:01.328Z_

<details><summary>↩ Tool result · `toolu_01DTTcV5BG7cbXFEqspDBFwo`</summary>

```text
Web search results for query: "arXiv 2602.11411 "Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data""

Links: [{"title":"[2602.11411] Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data","url":"https://arxiv.org/abs/2602.11411"},{"title":"Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data","url":"https://arxiv.org/html/2602.11411"},{"title":"Assessing and Enhancing the Robustness of Large Language Models with Task Structure Variations for Logical Reasoning","url":"https://arxiv.org/html/2310.09430v5"},{"title":"Evaluating and Improving Robustness in Large Language Models: A Survey and Future Directions","url":"https://arxiv.org/html/2506.11111v2"},{"title":"Evaluating and Enhancing the Vulnerability Reasoning Capabilities of Large Language Models","url":"https://arxiv.org/html/2602.06687v1"},{"title":"Enhancing LLM Robustness to Perturbed Instructions: An Empirical Study","url":"https://arxiv.org/html/2504.02733"},{"title":"[2601.06341] Evaluating Robustness of Large Language Models in Enterprise Applications: Benchmarks for Perturbation Consistency Across Formats and Languages","url":"https://arxiv.org/abs/2601.06341"},{"title":"Robustness of Prompting: Enhancing Robustness of Large Language Models Against Prompting Attacks","url":"https://arxiv.org/html/2506.03627"},{"title":"Evaluating and Improving Robustness in Large Language Models: A","url":"https://arxiv.org/pdf/2506.11111"},{"title":"Understanding Artificial Theory of Mind: Perturbed Tasks and Reasoning in Large Language Models","url":"https://arxiv.org/html/2602.22072"}]

I found the paper! Here's what I discovered about arXiv paper 2602.11411:

## Paper Summary

**Title:** Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data

**Authors:** Yang Liu and 4 other authors

**Publication Date:** February 11, 2026

## Overview

The paper focuses on Large Language Models (LLMs) as indispensable tools for tasks such as code generation, completion, analysis, and bug fixing. The work aims to improve the robustness of LLMs for coding-related tasks against potential adversarial inputs, specifically investigating how fine-tuning LLMs with perturbed datasets impacts their robustness against input perturbations.

## Methodology

The researchers systematically evaluated LLM robustness by fine-tuning models using datasets perturbed at character-level, word-level, and sentence-level, comparing results against base models and models fine-tuned on unperturbed datasets.

## Key Findings

Fine-tuning LLMs with perturbed datasets significantly improves model robustness (RD usually drops around 4% - 6%), especially for models with relatively weak robustness. However, this fine-tuning process typically results in a slight performance decrease (pass@1 usually drops around 1% - 3%) compared to fine-tuning with unperturbed datasets, although occasional performance improvements are observed.

## Conclusion

Fine-tuning LLMs for coding tasks with perturbed data effectively enhances their robustness at the cost of a minor performance reduction, emphasizing the importance of balancing the robustness and performance of LLMs for coding applications.

You can access the full paper at: https://arxiv.org/abs/2602.11411


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4fb78b7-aca2-44cb-9ae4-094465fdc7b8",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "b07faa58-07f2-4766-8ef1-4de282ccedbb",
  "sourceToolAssistantUUID": "a4fb78b7-aca2-44cb-9ae4-094465fdc7b8",
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

_source line 11 · 2026-05-10T06:26:02.173Z_

<details><summary>↩ Tool result · `toolu_01Lsdvn7j3jBCCpWd1RppVPK`</summary>

```text
Web search results for query: "arXiv 2601.18044 RGFL "Reasoning Guided Fault Localization""

Links: [{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair","url":"https://www.arxiv.org/pdf/2601.18044"},{"title":"[2601.18044] RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/abs/2601.18044"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/html/2601.18044"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260118044S/abstract"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2601.18044"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models | Scilit","url":"https://www.scilit.com/publications/93a4ab9613be0ae41a0609c084a46a24"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization","url":"https://arxiv.org/html/2308.05487v3"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372v3"},{"title":"Explainable Fault Localization for Programming Assignments via LLM-Guided Annotation","url":"https://arxiv.org/html/2509.25676v1"},{"title":"Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization","url":"https://arxiv.org/html/2403.10507v1"}]

I found the paper you're looking for! Here's information about arXiv 2601.18044:

**Title:** RGFL: Reasoning Guided Fault Localization for Automated Program Repair

**Authors:** Melika Sepidband, Hamed Taherkhani, Hung Viet Pham, and Hadi Hemmati

**Submission Date:** 25 Jan 2026

**Overview:**
Fault Localization (FL) is a critical step in Automated Program Repair (APR), and its importance has increased with the rise of Large Language Model (LLM)-based repair agents. In realistic project-level repair scenarios, software repositories often span millions of tokens, far exceeding current LLM context limits. Consequently, models must first identify a small, relevant subset of code, making accurate FL essential for effective repair.

**Key Method:**
The method introduces a hierarchical reasoning module that generates structured, bug-specific explanations for candidate files and elements, and leverages these explanations in a two-stage ranking scheme combining LLM-based and embedding-based signals. RGFL is based on the observation that LLM-as-Judge ranking over many files or code elements is effective for filtering candidates, but often insufficient for precisely identifying the most relevant ones. To address this, RGFL introduces an explicit per-candidate reasoning stage: for each file or element individually, the LLM explains its functionality, and this explanation is causally related to the reported symptom.

**Results:**
On SWE-bench Verified, file-level Hit@1 improves from 71.4% to 85%, and MRR from 81.8% to 88.8%. At the element level, Exact Match under top-3 files increases from 36% to 69%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04dbf558-d04e-4635-8499-4922dcf3c014",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "8ac5e7f6-8636-4023-949c-7972147d7fcf",
  "sourceToolAssistantUUID": "04dbf558-d04e-4635-8499-4922dcf3c014",
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

_source line 12 · 2026-05-10T06:26:02.554Z_

<details><summary>↩ Tool result · `toolu_01KShyYo7MyWTvAGUQJV74t8`</summary>

```text
Web search results for query: "arXiv 2412.21139 SWE-Gym "491 trajectories""

Links: [{"title":"arXiv:2412.21139v2 [cs.SE] 6 Jun 2025","url":"https://arxiv.org/pdf/2412.21139"},{"title":"[2412.21139] Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://arxiv.org/abs/2412.21139"},{"title":"Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://arxiv.org/html/2412.21139v1"},{"title":"SWE-Gym (SWE-Gym)","url":"https://huggingface.co/SWE-Gym"},{"title":"Paper page - Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://huggingface.co/papers/2412.21139"},{"title":"GitHub - SWE-Gym/SWE-Gym: Code for Paper: Training Software Engineering Agents and Verifiers with SWE-Gym [ICML 2025] · GitHub","url":"https://github.com/SWE-Gym/SWE-Gym"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=lpFFpTbi9s"},{"title":"Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://nlp.cs.berkeley.edu/pubs/Pan-Wang-Neubig-Jaitly-Ji-Suhr-Zhang_2025_SWEGym_paper.pdf"},{"title":"Training Software Engineering Agents and Verifiers with SWE-Gym | OpenReview","url":"https://openreview.net/forum?id=Cq1BNvHx74"},{"title":"2026-02-03 SWE-Universe: Scale Real-World Verifiable Environments to Millions","url":"https://www.arxiv.org/pdf/2602.02361"}]

Based on the search results, here's what I found about arXiv 2412.21139 and the "491 trajectories":

The paper presents SWE-Gym, the first environment for training real-world software engineering (SWE) agents. SWE-Gym contains 2,438 real-world Python task instances, each comprising a codebase with an executable runtime environment, unit tests, and a task specified in natural language.

The 491 trajectories refer to the final training dataset, composed of 106 + 19 + 67 + 299 success trajectories collected through rejection sampling.

The researchers fine-tuned a 32B Qwen-2.5 coder model using only 491 agent-environment interaction trajectories sampled using SWE-Gym, and achieved substantial absolute improvements of +12.3% (to 15.3%) and +13.6% (to 20.6%) on SWE-Bench Lite and SWE-Bench Verified respectively.

The training time scaling shows consistent performance improvements as they obtain more training trajectories, with no signs of saturation at 491 trajectories.

When combined with verifiers trained on agent trajectories sampled from SWE-Gym, they achieved 32.0% and 26.0% on SWE-Bench Verified and Lite, respectively, reflecting a new state-of-the-art for open-weight SWE agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dd82fd5-00fe-4c94-9ef2-6dd6949aca65",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "66c3ad30-7007-4d6c-becd-7af01fea1a6e",
  "sourceToolAssistantUUID": "7dd82fd5-00fe-4c94-9ef2-6dd6949aca65",
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

_source line 13 · 2026-05-10T06:26:04.079Z_

Now let me search for recent papers from March-May 2026 addressing surface-form robustness and related topics:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66c3ad30-7007-4d6c-becd-7af01fea1a6e",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQqgrMHuuBgqowohkS1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea7c83a7-1fa8-4d64-a8fe-8057d9cddaaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019ibdejxhGD66U5wxu73CDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 17102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5803,
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

_source line 14 · 2026-05-10T06:26:04.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JYeHsXWzqSQbkwq8xJ3Qi2`</summary>

```json
{
  "query": "fault localization robustness contrastive 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea7c83a7-1fa8-4d64-a8fe-8057d9cddaaa",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQqgrMHuuBgqowohkS1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7e72da83-ddb2-414b-a0e7-840a0bf50da5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019ibdejxhGD66U5wxu73CDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 17102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5803,
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

_source line 15 · 2026-05-10T06:26:04.716Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ph13GAv1ZMnB6m3jCTUUtY`</summary>

```json
{
  "query": "semantic mutation augmentation code LLM 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e72da83-ddb2-414b-a0e7-840a0bf50da5",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQqgrMHuuBgqowohkS1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2eff1b06-b8ca-4ec5-b6bb-393d164cd99e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019ibdejxhGD66U5wxu73CDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 17102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5803,
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

_source line 16 · 2026-05-10T06:26:04.952Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017DbyMPNFkU4kN1NNKUR28k`</summary>

```json
{
  "query": "code understanding surface-form invariance training 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eff1b06-b8ca-4ec5-b6bb-393d164cd99e",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQqgrMHuuBgqowohkS1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c33142cc-ae88-482d-9eb9-180b57005bf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019ibdejxhGD66U5wxu73CDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 17102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5803,
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

_source line 17 · 2026-05-10T06:26:05.163Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G9QYvSc4jUJ9sfGPGHPZ5r`</summary>

```json
{
  "query": "\"surface-form\" robust \"fault localization\" LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c33142cc-ae88-482d-9eb9-180b57005bf6",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQqgrMHuuBgqowohkS1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "79cf0955-753d-47b8-97b3-ae9fb27cab4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019ibdejxhGD66U5wxu73CDo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 17102,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5803
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 252,
          "cache_read_input_tokens": 17102,
          "cache_creation_input_tokens": 5803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5803,
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

_source line 18 · 2026-05-10T06:26:10.090Z_

<details><summary>↩ Tool result · `toolu_017DbyMPNFkU4kN1NNKUR28k`</summary>

```text
Web search results for query: "code understanding surface-form invariance training 2026 site:arxiv.org"

Links: [{"title":"Causal Manifold Fairness: Enforcing Geometric Invariance in Representation Learning","url":"https://arxiv.org/html/2601.03032v1"},{"title":"Learning to Transform for Generalizable Instance-wise Invariance","url":"https://arxiv.org/html/2309.16672v3"},{"title":"Rethink Deep Learning with Invariance in Data Representation (Tutorial Proposal)","url":"https://arxiv.org/html/2412.04858v1"},{"title":"Understanding the Role of Invariance in Transfer Learning","url":"https://arxiv.org/html/2407.04325v1"},{"title":"Understanding Learning Invariance in Deep Linear Networks","url":"https://arxiv.org/pdf/2506.13714"},{"title":"[2309.16672] Learning to Transform for Generalizable Instance-wise Invariance","url":"https://arxiv.org/abs/2309.16672"},{"title":"JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2015 1","url":"https://arxiv.org/pdf/2103.15890"},{"title":"[1912.01447] Transform-Invariant Convolutional Neural Networks for Image Classification and Search","url":"https://arxiv.org/abs/1912.01447"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=10275&show=2000"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2409.02772"}]

I've performed the web search for your query about "code understanding surface-form invariance training 2026 site:arxiv.org". 

However, the search results do not contain any papers specifically about code understanding with surface-form invariance training from 2026. The results returned papers on related topics like invariance in deep learning, fairness in representation learning, and transfer learning, but none directly addressing code understanding with surface-form invariance training.

It's possible that:
1. Such a paper may not exist yet on arXiv (it's currently May 2026 in this context)
2. The paper might use different terminology than "surface-form invariance training"
3. The paper may not be indexed yet or may be using different keywords

If you're looking for papers on a specific topic related to code understanding and invariance, I'd be happy to search with different terms or help you refine the query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c33142cc-ae88-482d-9eb9-180b57005bf6",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "18b969af-423a-42c8-a4fd-c40100af78d6",
  "sourceToolAssistantUUID": "c33142cc-ae88-482d-9eb9-180b57005bf6",
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

_source line 19 · 2026-05-10T06:26:11.310Z_

<details><summary>↩ Tool result · `toolu_01JYeHsXWzqSQbkwq8xJ3Qi2`</summary>

```text
Web search results for query: "fault localization robustness contrastive 2026 site:arxiv.org"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"ROBUSTNESS EVALUATION OF MACHINE LEARNING MODELS FOR FAULT CLASSIFICATION AND LOCALIZATION IN POWER SYSTEM PROTECTION","url":"https://arxiv.org/html/2512.15385"},{"title":"Benchmarking Machine Learning Models for Fault Classification and Localization in Power System Protection","url":"https://arxiv.org/html/2510.00831"},{"title":"Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization","url":"https://arxiv.org/html/2409.12519"},{"title":"[2512.15385] Robustness Evaluation of Machine Learning Models for Fault Classification and Localization In Power System Protection","url":"https://arxiv.org/abs/2512.15385"},{"title":"Order Matters! An Empirical Study on Large Language Models’ Input Order Bias in Software Fault Localization","url":"https://arxiv.org/html/2412.18750"},{"title":"Domain-Aware Hierarchical Contrastive Learning for Semi-Supervised Generalization Fault Diagnosis","url":"https://arxiv.org/html/2604.20928"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372v3"},{"title":"USD: Unsupervised Soft Contrastive Learning for Fault Detection in Multivariate Time Series","url":"https://arxiv.org/html/2405.16258v1"},{"title":"(PDF) USD: Unsupervised Soft Contrastive Learning for ...","url":"https://arxiv.org/pdf/2405.16258"}]

I found several relevant papers on arxiv.org related to fault localization, robustness, and contrastive learning. Here are the key results:

## Most Relevant Results:

**1. "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models" (arxiv.org/html/2504.04372)**

This paper presents the first large-scale empirical investigation into the robustness of LLMs' fault localizability. The researchers apply semantic-preserving mutations (SPMs) and rerun localization to assess the LLM's robustness and whether the LLM's reasoning relies on syntactic cues rather than semantics. The results show that SPMs cause an LLM to fail to localize the same fault it correctly localized earlier in 78% of cases.

**2. "Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization" (arxiv.org/html/2409.12519)**

This paper proposes a novel approach named Multi-View Adaptive Contrastive Learning for Information Retrieval Fault Localization (MACL-IRFL) to learn relationships for software fault localization. The results show that the model can improve over the best baseline up to 28.93%, 25.57% and 20.35% on Accuracy@1, MAP and MRR, respectively.

**3. Other Relevant Papers:**

- "Order Matters! An Empirical Study on Large Language Models' Input Order Bias in Software Fault Localization" - studies input order bias in LLM-based fault localization
- Papers on contrastive learning for fault detection in time series data and power system protection applications


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e72da83-ddb2-414b-a0e7-840a0bf50da5",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "7d822a77-1f1d-4497-969a-c25af2079678",
  "sourceToolAssistantUUID": "7e72da83-ddb2-414b-a0e7-840a0bf50da5",
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

_source line 20 · 2026-05-10T06:26:12.337Z_

<details><summary>↩ Tool result · `toolu_01G9QYvSc4jUJ9sfGPGHPZ5r`</summary>

```text
Web search results for query: ""surface-form" robust "fault localization" LLM 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Towards Robust LLM Post-Training: Automatic Failure Management for Reinforcement Fine-Tuning","url":"https://arxiv.org/html/2605.04431"},{"title":"From Trace to Line: LLM Agent for Real-World OSS Vulnerability Localization","url":"https://arxiv.org/html/2510.02389v1"},{"title":"[2504.04372] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (ICST 2026 - Research Papers) - ICST 2026","url":"https://conf.researchr.org/details/icst-2026/icst-2026-research/30/Assessing-the-Impact-of-Code-Changes-on-the-Fault-Localizability-of-Large-Language-Mo"},{"title":"Towards LLM-Based Failure Localization in Production-Scale Networks | Proceedings of the ACM SIGCOMM 2025 Conference","url":"https://dl.acm.org/doi/10.1145/3718958.3750505"},{"title":"Explainable Fault Localization for Programming Assignments via LLM-Guided Annotation","url":"https://arxiv.org/html/2509.25676v1"},{"title":"[2504.04372v3] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372v3"},{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3660771"}]

Based on the search results, I found a highly relevant paper that directly addresses your query about surface-form robustness in fault localization with LLMs in 2026.

## Key Finding

The most relevant work is "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models," which presents the first large-scale empirical investigation into the robustness of LLMs' fault localizability, developing an end-to-end evaluation framework inspired by mutation testing.

## Main Results

Success in fault localization depends on a model's ability to reason about program semantics that are beyond surface-level syntactic and lexical features. However, the researchers apply semantic-preserving mutations (SPMs) and rerun localization to assess the LLM's robustness and whether the LLM's reasoning relies on syntactic cues rather than semantics.

The findings are striking: semantic-preserving mutations cause an LLM to fail to localize the same fault it correctly localized earlier in 78% of cases, and LLMs' reasoning on the code is tied to code features irrelevant to semantics.

## Scope of Study

The paper evaluates 10 state-of-the-art LLMs on 1300 Java and Python programs. The research addresses limitations in traditional fault localization benchmarks like Defect4J and BugsInPy, which are either not scalable or obsolete because their datasets have become part of LLM training data.

This paper was accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79cf0955-753d-47b8-97b3-ae9fb27cab4f",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "0ea10956-b1bd-431e-8725-363d309ae4af",
  "sourceToolAssistantUUID": "79cf0955-753d-47b8-97b3-ae9fb27cab4f",
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

_source line 21 · 2026-05-10T06:26:13.771Z_

<details><summary>↩ Tool result · `toolu_01Ph13GAv1ZMnB6m3jCTUUtY`</summary>

```text
Web search results for query: "semantic mutation augmentation code LLM 2026 site:arxiv.org"

Links: [{"title":"Increasing LLM Coding Capabilities through Diverse Synthetic Coding Tasks","url":"https://arxiv.org/html/2510.23208v1"},{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Fine-Tuning LLMs for Code Mutation: A New Era of Cyber Threats","url":"https://arxiv.org/html/2410.22293v1"},{"title":"[2506.17369] Re-Evaluating Code LLM Benchmarks Under Semantic Mutation","url":"https://arxiv.org/abs/2506.17369"},{"title":"Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided, Reasoning-Driven Input Mutation","url":"https://arxiv.org/html/2509.19533v1"},{"title":"Automatic Semantic Augmentation of Language Model Prompts (for Code Summarization)","url":"https://arxiv.org/html/2304.06815v3"},{"title":"LLM-Guided Genetic Improvement: Envisioning Semantic Aware Automated Software Evolution","url":"https://arxiv.org/html/2508.18089"},{"title":"Semantic-Preserving Transformations as Mutation Operators","url":"https://arxiv.org/pdf/2503.23448"},{"title":"[2304.06815] Automatic Semantic Augmentation of Language Model Prompts (for Code Summarization)","url":"https://arxiv.org/abs/2304.06815"},{"title":"TerraFormer: Automated Infrastructure-as-Code with LLMs Fine-Tuned via Policy-Guided Verifier Feedback","url":"https://arxiv.org/html/2601.08734"}]

I've completed the web search for "semantic mutation augmentation code LLM 2026 site:arxiv.org". Here are the results:

## Key Research Papers Found:

1. **Increasing LLM Coding Capabilities through Diverse Synthetic Coding Tasks** (October 2025)
   - Introduces a genetic instruction mutation algorithm that creates novel task variants without sacrificing correctness
   - Produces nearly 800k instruction–reasoning–code–test quadruplets, where each sample combines a task, a step-by-step reasoning trace, a working solution, and executable tests

2. **Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models** (March 2026, accepted at ICST 2026)
   - Injects 4 fault types and applies 6 semantic-preserving mutations, generating 750,013 unique faulty programs
   - Observes that semantic-preserving mutations cause LLMs to fail to localize the same fault in 78% of cases

3. **Re-Evaluating Code LLM Benchmarks Under Semantic Mutation** (June 2025)
   - Addresses how existing code benchmarks are prone to prompt sensitivity, where minor prompt variations could result in substantial performance variations

4. **Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided Input Mutation** (September 2025)
   - Describes an LLM service that performs semantic-aware mutations by targeting input sections most likely to reveal new code paths based on their structure and content

5. **LLM-Guided Genetic Improvement** (August 2025)
   - Proposes investigation of AI-powered genetic improvement aimed at incorporating semantic aware search by augmenting GI with automated clustering of LLM edits

6. **TerraFormer: Automated Infrastructure-as-Code with LLMs** (January 2026)
   - Presents TF-Mutn, the first Infrastructure-as-Code mutation dataset with 52,516 mutation instances


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2eff1b06-b8ca-4ec5-b6bb-393d164cd99e",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "e355b8ba-4216-460e-9a97-a2b29b56e8ca",
  "sourceToolAssistantUUID": "2eff1b06-b8ca-4ec5-b6bb-393d164cd99e",
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

_source line 22 · 2026-05-10T06:26:15.728Z_

Now let me fetch more details about the paper 2505.10443 to check for the specific claim about 70% performance drops:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e355b8ba-4216-460e-9a97-a2b29b56e8ca",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQrWubKuGUNXVnfgBLr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "94181e90-9058-4b4e-ba3d-519ebe054c98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PkSprfJERegspndjvwuVUs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1694,
      "cache_creation_input_tokens": 2324,
      "cache_read_input_tokens": 22905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2324,
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

_source line 23 · 2026-05-10T06:26:16.336Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U5duaQGceqPeEKP86cnmh5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.10443",
  "prompt": "What are the specific performance drops reported? Does it show drops up to 70% across nine LLMs? What are the exact percentages reported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94181e90-9058-4b4e-ba3d-519ebe054c98",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQrWubKuGUNXVnfgBLr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d890c6a6-efd5-4d3a-a860-6dd65b91a73f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PkSprfJERegspndjvwuVUs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1694,
      "cache_creation_input_tokens": 2324,
      "cache_read_input_tokens": 22905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2324,
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

_source line 24 · 2026-05-10T06:26:17.010Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V1fhnEWhnGEuUAEYUe4WJa`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.11411",
  "prompt": "What are the specific perturbation types applied? Does it mention typos, synonyms, back-translation, or other NLP-level perturbations? Does it use semantic-preserving code mutations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d890c6a6-efd5-4d3a-a860-6dd65b91a73f",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQrWubKuGUNXVnfgBLr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c188100-c232-402e-abc0-095713755cce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PkSprfJERegspndjvwuVUs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1694,
      "cache_creation_input_tokens": 2324,
      "cache_read_input_tokens": 22905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2324,
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

_source line 25 · 2026-05-10T06:26:17.898Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LYYbqztvvnmkXCoWaHSg5s`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.21139",
  "prompt": "Find Table 8 or token statistics. Does it describe training with 491 trajectories and 18,578 average tokens? What specific hardware and LoRA configuration is used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c188100-c232-402e-abc0-095713755cce",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQrWubKuGUNXVnfgBLr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3811d44b-5870-47f3-9aaf-7ca275919982",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PkSprfJERegspndjvwuVUs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1694,
      "cache_creation_input_tokens": 2324,
      "cache_read_input_tokens": 22905,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2324
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1694,
          "output_tokens": 355,
          "cache_read_input_tokens": 22905,
          "cache_creation_input_tokens": 2324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2324,
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

_source line 26 · 2026-05-10T06:26:19.957Z_

<details><summary>↩ Tool result · `toolu_01U5duaQGceqPeEKP86cnmh5`</summary>

```text
# Performance Drop Findings

The abstract states that "LLMs often change predictions in response to our code mutations, with performance drops reaching up to 70%, indicating that they do not yet exhibit stable, semantically grounded reasoning."

However, the provided content does **not specify exact percentages for individual models** or break down performance drops across the nine LLMs tested. The abstract only mentions the maximum observed drop (70%) without providing detailed per-model figures.

The document does indicate that "LLMs trained for code produce correct predictions based on flawed reasoning in between 10% and 50% of cases," which represents a different metric—the frequency of correct answers derived from unsound logic rather than absolute performance reductions.

To obtain specific performance drop percentages for each model, you would need to access the full paper's results tables and analysis sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d890c6a6-efd5-4d3a-a860-6dd65b91a73f",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "c2857117-36b6-460c-8823-f32942a862ab",
  "sourceToolAssistantUUID": "d890c6a6-efd5-4d3a-a860-6dd65b91a73f",
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

_source line 27 · 2026-05-10T06:26:20.123Z_

<details><summary>↩ Tool result · `toolu_01LYYbqztvvnmkXCoWaHSg5s`</summary>

```text
# Response

I cannot find Table 8 or token statistics describing the specific training configuration you mentioned (491 trajectories, 18,578 average tokens) in the provided web page content.

The page shows only the arXiv abstract and metadata for the paper "Training Software Engineering Agents and Verifiers with SWE-Gym." To locate Table 8 and hardware/LoRA configuration details, you would need to access the full PDF or HTML version of the paper, which are linked on this page but not included in the content provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3811d44b-5870-47f3-9aaf-7ca275919982",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "9ab034cd-5047-4e0b-a81c-7be5dfb7bd71",
  "sourceToolAssistantUUID": "3811d44b-5870-47f3-9aaf-7ca275919982",
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

_source line 28 · 2026-05-10T06:26:20.740Z_

<details><summary>↩ Tool result · `toolu_01V1fhnEWhnGEuUAEYUe4WJa`</summary>

```text
# Perturbation Types in the Paper

Based on the provided abstract, the paper mentions applying perturbations at **three levels**:

1. **Character-level** perturbations
2. **Word-level** perturbations
3. **Sentence-level** perturbations

However, the abstract does not specify the exact nature of these perturbations. It does not clarify whether they involve typos, synonyms, back-translation, semantic-preserving code mutations, or other specific techniques.

The abstract only states that researchers "systematically evaluated LLM robustness by fine-tuning models using datasets perturbed at character-level, word-level, and sentence-level" but provides no details about the mechanics of these perturbation methods. To understand the specific perturbation techniques employed, you would need to access the full paper PDF or HTML version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c188100-c232-402e-abc0-095713755cce",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "3ee032f0-f78f-4479-a37d-73062e7ea931",
  "sourceToolAssistantUUID": "9c188100-c232-402e-abc0-095713755cce",
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

_source line 29 · 2026-05-10T06:26:21.715Z_

Let me get the full paper versions to verify the specific details:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ee032f0-f78f-4479-a37d-73062e7ea931",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQs2a3LUWEJjUGDM2yy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d66d28d-6106-4f2e-99fa-9550b6c0a460",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013e6AtFL9T1K8gxY93LJbwF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 148,
      "cache_creation_input_tokens": 2470,
      "cache_read_input_tokens": 25229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2470,
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

_source line 30 · 2026-05-10T06:26:22.372Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SNZEykz17TYV312DGyvvKT`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.10443",
  "prompt": "Find exact performance drop percentages for each LLM tested. What are the nine LLMs and their specific performance drops?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d66d28d-6106-4f2e-99fa-9550b6c0a460",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQs2a3LUWEJjUGDM2yy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "37de55ff-f1ff-4288-a55a-e12d6db0d530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013e6AtFL9T1K8gxY93LJbwF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 148,
      "cache_creation_input_tokens": 2470,
      "cache_read_input_tokens": 25229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2470,
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

_source line 31 · 2026-05-10T06:26:22.783Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GXgiZTWXjkHM1x5zdqfwph`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.11411",
  "prompt": "What are the exact perturbation types? Describe the character-level, word-level, and sentence-level perturbations. Do they include typos, synonyms, back-translation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37de55ff-f1ff-4288-a55a-e12d6db0d530",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQs2a3LUWEJjUGDM2yy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5239112-3fef-429b-aedd-dc90706a5485",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013e6AtFL9T1K8gxY93LJbwF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 148,
      "cache_creation_input_tokens": 2470,
      "cache_read_input_tokens": 25229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2470,
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

_source line 32 · 2026-05-10T06:26:23.200Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WJW5ipJrRf3zCHNvGG5neY`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2412.21139",
  "prompt": "Find Table 8. What are the exact token statistics and training configuration? Does it show 491 trajectories and 18,578 average tokens? What is the exact hardware and LoRA configuration?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5239112-3fef-429b-aedd-dc90706a5485",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQs2a3LUWEJjUGDM2yy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a1958935-6ebe-4f63-b70d-dd6f6521f554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013e6AtFL9T1K8gxY93LJbwF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 148,
      "cache_creation_input_tokens": 2470,
      "cache_read_input_tokens": 25229,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2470
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 148,
          "output_tokens": 336,
          "cache_read_input_tokens": 25229,
          "cache_creation_input_tokens": 2470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2470,
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

_source line 33 · 2026-05-10T06:26:26.684Z_

<details><summary>↩ Tool result · `toolu_01WJW5ipJrRf3zCHNvGG5neY`</summary>

```text
I cannot locate Table 8 in the provided PDF content. The document appears to be a research paper about "Training Software Engineering Agents and Verifiers with SWE-Gym," but the text provided consists primarily of PDF structure metadata and encoded content streams rather than readable table data.

To find the specific token statistics, trajectory counts, hardware specifications, and LoRA configuration you're asking about, I would need access to the actual rendered content of Table 8, which is not clearly legible in this PDF metadata format.

If you have access to the paper, I'd recommend:
- Viewing the PDF directly in a reader
- Searching for "Table 8" using your PDF viewer's search function
- Checking the appendix sections if the table is referenced there

[Binary content (application/pdf, 575.4KB) also saved to /home/ubuntu/.claude-account-1/projects/-/818c6f04-ca23-4de4-b570-59c5989a81dd/tool-results/webfetch-1778394383218-x9ziam.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1958935-6ebe-4f63-b70d-dd6f6521f554",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "50f01888-d5c5-4abb-8db2-990ef560354b",
  "sourceToolAssistantUUID": "a1958935-6ebe-4f63-b70d-dd6f6521f554",
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

_source line 34 · 2026-05-10T06:26:27.257Z_

<details><summary>↩ Tool result · `toolu_01SNZEykz17TYV312DGyvvKT`</summary>

```text
# LLM Performance Drops Under Semantics-Preserving Mutations

The study evaluated **nine LLMs**:

**Open-source models:**
1. CodeGemma (7B)
2. GraniteCode (8B)
3. Mistral (7B)
4. Qwen2.5-Coder (7B)
5. Qwen3-Coder (30B)
6. SemCoder (7B)
7. Llama3.2 (3B)

**Proprietary models:**
8. GPT-5.2
9. Gemini-3

## Performance Drops (LiveCodeBench)

The largest performance degradation occurred with loop unrolling:

- **Qwen2.5-Coder**: −44.3 percentage points
- **Qwen3-Coder**: −35.1 points
- **SemCoder**: −32.8 points
- **GPT-5.2**: −68.1 points
- **Gemini-3**: −70.4 points
- **Llama3.2**: −29.2 points
- **CodeGemma**: −22.3 points
- **GraniteCode**: −26.5 points
- **Mistral**: −22.1 points

Loop conversion caused dramatic drops for proprietary models (Gemini-3: −44.7 points; GPT-5.2: −24.6 points), while variable renaming often improved performance, suggesting identifier names "strongly influence model behaviour" despite semantic irrelevance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37de55ff-f1ff-4288-a55a-e12d6db0d530",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "407fc543-6ce7-4341-a60a-2d097ab24bd4",
  "sourceToolAssistantUUID": "37de55ff-f1ff-4288-a55a-e12d6db0d530",
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

_source line 35 · 2026-05-10T06:26:27.581Z_

<details><summary>↩ Tool result · `toolu_01GXgiZTWXjkHM1x5zdqfwph`</summary>

```text
# Perturbation Types in the Study

Based on Table 1 in the document, the study employs nine distinct perturbation methods organized into three categories:

## Character-Level Perturbations (C1–C3)
These introduce typographical noise:
- **ButterFingers (C1)**: "Random character insertions/typos"
- **SwapCharacters (C2)**: "Character swaps within words"
- **ChangeCharCase (C3)**: "Case modifications"

## Word-Level Perturbations (W1–W3)
These alter lexical choices while preserving meaning:
- **SynonymInsertion (W1)**: "Insertion of synonyms"
- **SynonymSubstitution (W2)**: "Replacement with synonyms"
- **InflectionalVariation (W3)**: "Word inflection changes"

## Sentence-Level Perturbations (S1–S3)
These apply broader semantic transformations:
- **BackTranslation (S1)**: "Round-trip translation"
- **TenseTransformationPast (S2)**: "Conversion to past tense"
- **TenseTransformationFuture (S3)**: "Conversion to future tense"

The researchers also created aggregate datasets combining perturbations within each category level, plus one dataset merging all perturbation types for realistic mixed-noise scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5239112-3fef-429b-aedd-dc90706a5485",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "76871c8b-4862-4363-8fc4-2cede347d101",
  "sourceToolAssistantUUID": "d5239112-3fef-429b-aedd-dc90706a5485",
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

_source line 36 · 2026-05-10T06:26:28.752Z_

Let me search for additional details on SWE-Gym's Table 8 and configuration more directly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76871c8b-4862-4363-8fc4-2cede347d101",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQsXoh4WCKYyiKWk2Db",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fb46aa81-ccd6-447c-8c93-e59e795372b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UGtPGAynn5ta7FXdWBgQRb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 27699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 37 · 2026-05-10T06:26:29.188Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TayzYTvwphSVGpjrd2hMjt`</summary>

```json
{
  "query": "\"SWE-Gym\" \"Table 8\" \"491 trajectories\" \"18,578\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb46aa81-ccd6-447c-8c93-e59e795372b1",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQsXoh4WCKYyiKWk2Db",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c6a04d8f-d0ba-4122-bf8c-1102f925d998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UGtPGAynn5ta7FXdWBgQRb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 27699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 38 · 2026-05-10T06:26:29.603Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VUYFBTPm3H4Xmf2EApzjY1`</summary>

```json
{
  "query": "SWE-Gym \"32B\" LoRA \"H100\" training tokens trajectories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6a04d8f-d0ba-4122-bf8c-1102f925d998",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQsXoh4WCKYyiKWk2Db",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9d7054ee-c631-4ab8-a2f2-71e2d1af6674",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UGtPGAynn5ta7FXdWBgQRb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 27699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 39 · 2026-05-10T06:26:30.154Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JmG1dFYrM5qrKbtNvMLkYy`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.21139v1",
  "prompt": "Find the training configuration including number of trajectories, average tokens per trajectory, model size, LoRA parameters, and hardware used. Look for Table 8 or related statistics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d7054ee-c631-4ab8-a2f2-71e2d1af6674",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQsXoh4WCKYyiKWk2Db",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "411acba8-a534-47ee-badd-9a14adfd087b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UGtPGAynn5ta7FXdWBgQRb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 273,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 27699,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 273,
          "output_tokens": 257,
          "cache_read_input_tokens": 27699,
          "cache_creation_input_tokens": 1237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1237,
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

_source line 40 · 2026-05-10T06:26:36.151Z_

<details><summary>↩ Tool result · `toolu_01VUYFBTPm3H4Xmf2EApzjY1`</summary>

```text
Web search results for query: "SWE-Gym "32B" LoRA "H100" training tokens trajectories"

Links: [{"title":"Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://arxiv.org/html/2412.21139v2"},{"title":"Training Software Engineering Agents and Verifiers with ...","url":"https://arxiv.org/pdf/2412.21139"},{"title":"TRAINING SOFTWARE ENGINEERING AGENTS AND ...","url":"https://openreview.net/pdf?id=lpFFpTbi9s"},{"title":"Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://nlp.cs.berkeley.edu/pubs/Pan-Wang-Neubig-Jaitly-Ji-Suhr-Zhang_2025_SWEGym_paper.pdf"},{"title":"DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL","url":"https://www.together.ai/blog/deepswe"},{"title":"GitHub - SWE-Gym/SWE-Gym: Code for Paper: Training Software Engineering Agents and Verifiers with SWE-Gym [ICML 2025] · GitHub","url":"https://github.com/SWE-Gym/SWE-Gym"},{"title":"QeRL: Training 32B Models on Single H100 vs Three GPUs, Beating LoRA in Accuracy","url":"https://neurohive.io/en/state-of-the-art/qerl-2/"},{"title":"R2E-Gym: Scaling Open-Weights SWE Agents","url":"https://r2e-gym.github.io/"},{"title":"SWE-Gym/docs/OpenHands.md at main · SWE-Gym/SWE-Gym","url":"https://github.com/SWE-Gym/SWE-Gym/blob/main/docs/OpenHands.md"},{"title":"Keep the Tokens Flowing: Lessons from 16 Open-Source RL Libraries","url":"https://huggingface.co/blog/async-rl-training-landscape"}]

Based on the web search results, here's information about SWE-Gym with a 32B model using LoRA on H100 GPUs for training on trajectories:

## Training Configuration

For the 32B model, Unsloth is used with a single H100 GPU for LoRA fine-tuning. The configuration includes 5 epochs, batch size of 8, LoRA rank of 64, and a learning rate of 5 × 10⁻⁴.

## Training Data and Trajectories

Each iteration of the training procedure involves performing 30 high-temperature (1.0) rollouts per task on SWE-Gym-Lite and adding successful trajectories to the fine-tuning dataset, followed by fine-tuning the policy on these filtered trajectories.

Iterative rejection sampling fine-tuning is used for policy improvement, and after two iterations, further improvements are negligible.

## Performance Results

The 32B verifier improves from 19.7 to 26.3% resolution rate on SWE-Bench Lite when paired with a 32B policy. Additionally, fine-tuning the verifier model using LoRA with Unsloth performs better than full-parameter fine-tuning (29.8@8 versus 27.2@8), potentially due to regularization effects.

The research demonstrates that LoRA-based training is effective for efficiently fine-tuning 32B models on agent trajectories using limited compute resources like a single H100 GPU.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d7054ee-c631-4ab8-a2f2-71e2d1af6674",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "ac7474bd-1809-4c6e-a8da-a223ff844d6b",
  "sourceToolAssistantUUID": "9d7054ee-c631-4ab8-a2f2-71e2d1af6674",
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

_source line 41 · 2026-05-10T06:26:36.186Z_

<details><summary>↩ Tool result · `toolu_01JmG1dFYrM5qrKbtNvMLkYy`</summary>

```text
# SWE-Gym Training Configuration Summary

## Trajectory Statistics (Table 8)
For successful trajectories used in training:
- **Average Messages**: 39.9 per trajectory
- **Average Tokens**: 18,578.5 tokens per trajectory
- **Token Range**: 2,560 to 81,245 tokens

## Model and Training Setup

**Base Model**: Qwen-2.5-Coder-Instruct (7B, 14B, 32B variants)

**Training Data**: 491 successful agent trajectories sampled from SWE-Gym

**Hardware**: 2-8x NVIDIA H100 80G GPUs on Modal

## Training Hyperparameters

**Standard Fine-tuning**:
- Learning rate: 1e-4
- Epochs: 5 maximum
- Global batch size: 8
- Max context length: 32,768 tokens

**LoRA Fine-tuning** (verifier training):
- Max epochs: 2
- Uses Unsloth library for efficiency
- LoRA rank: 64 (for 32B model)
- Learning rate: 5×10⁻⁴

The document notes that "performance scales with the number of sampled trajectories up to our current limit of 491 trajectories, suggesting that performance is currently limited by sampling compute rather than SWE-Gym's size."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "411acba8-a534-47ee-badd-9a14adfd087b",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "f81b2f12-a504-472f-9bf6-bccc060804c3",
  "sourceToolAssistantUUID": "411acba8-a534-47ee-badd-9a14adfd087b",
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

_source line 42 · 2026-05-10T06:26:36.351Z_

<details><summary>↩ Tool result · `toolu_01TayzYTvwphSVGpjrd2hMjt`</summary>

```text
Web search results for query: ""SWE-Gym" "Table 8" "491 trajectories" "18,578""

Links: [{"title":"Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://nlp.cs.berkeley.edu/pubs/Pan-Wang-Neubig-Jaitly-Ji-Suhr-Zhang_2025_SWEGym_paper.pdf"},{"title":"Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://arxiv.org/html/2412.21139v1"},{"title":"Training Software Engineering Agents and Verifiers with ...","url":"https://arxiv.org/pdf/2412.21139"},{"title":"(PDF) Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://www.researchgate.net/publication/387540461_Training_Software_Engineering_Agents_and_Verifiers_with_SWE-Gym"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=lpFFpTbi9s"},{"title":"Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://openreview.net/pdf?id=Cq1BNvHx74"},{"title":"SWE-Gym (SWE-Gym)","url":"https://huggingface.co/SWE-Gym"},{"title":"GitHub - SWE-Gym/SWE-Gym: Code for Paper: Training Software Engineering Agents and Verifiers with SWE-Gym [ICML 2025] · GitHub","url":"https://github.com/SWE-Gym/SWE-Gym"},{"title":"Scaling Data for Software Engineering Agents - SWE-smith","url":"https://swesmith.com/blog.html"},{"title":"[2412.21139] Training Software Engineering Agents and Verifiers with SWE-Gym","url":"https://arxiv.org/abs/2412.21139"}]

I found the search results related to your query about SWE-Gym, Table 8, and the specific numbers you mentioned.

Table 8 shows statistics of SWE-Gym-sampled trajectories, with 491 resolved successful trajectories containing an average of 18,578.5 tokens. These 491 successful trajectories were rolled out where the agent successfully solved the given task from SWE-Gym. Each success trajectory, on average, has 39.9 LM completion messages (roughly 19 turns) and 18,578 tokens.

This data comes from the paper "Training Software Engineering Agents and Verifiers with SWE-Gym," which presents SWE-Gym, containing 2,438 real-world Python task instances, each comprising a codebase with an executable runtime environment, unit tests, and a task specified in natural language.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6a04d8f-d0ba-4122-bf8c-1102f925d998",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "69a773a9-a277-4057-ae82-99a083482a25",
  "sourceToolAssistantUUID": "c6a04d8f-d0ba-4122-bf8c-1102f925d998",
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

_source line 43 · 2026-05-10T06:26:38.271Z_

Perfect! Now let me do one more search to check for any emerging work on "SeMutFL" specifically or similar contrastive mutation approaches:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69a773a9-a277-4057-ae82-99a083482a25",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQtBRNtb8wgahER7eqR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "037d87fb-b63c-4018-b923-b1b4919a5da1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SimLwMogrnt76s1R5DsXiG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1287,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 28936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 44 · 2026-05-10T06:26:38.738Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HxD9CFW2CXvRWpF3kKVx5S`</summary>

```json
{
  "query": "\"SeMutFL\" \"Contrastive Mutation Augmentation\" fault localization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "037d87fb-b63c-4018-b923-b1b4919a5da1",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQtBRNtb8wgahER7eqR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea1e8ba4-b1ff-4add-ad38-50e7e91a14eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SimLwMogrnt76s1R5DsXiG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1287,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 28936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 45 · 2026-05-10T06:26:38.978Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KQYig12UjbWzPKhrXVx51H`</summary>

```json
{
  "query": "\"contrastive mutation\" \"fault localization\" \"code understanding\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea1e8ba4-b1ff-4add-ad38-50e7e91a14eb",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQtBRNtb8wgahER7eqR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dfe2b022-03a7-400f-89d2-8e01e02fc552",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SimLwMogrnt76s1R5DsXiG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1287,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 28936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 46 · 2026-05-10T06:26:39.182Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G4Nt2Z1xB7tpTEzS23RhN6`</summary>

```json
{
  "query": "contrastive learning fault localization mutation augmentation code LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfe2b022-03a7-400f-89d2-8e01e02fc552",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQtBRNtb8wgahER7eqR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2acd9768-2218-4271-bd23-715b6360c35e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SimLwMogrnt76s1R5DsXiG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1287,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 28936,
      "output_tokens": 206,
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
          "input_tokens": 1287,
          "output_tokens": 206,
          "cache_read_input_tokens": 28936,
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

_source line 47 · 2026-05-10T06:26:45.528Z_

<details><summary>↩ Tool result · `toolu_01HxD9CFW2CXvRWpF3kKVx5S`</summary>

```text
Web search results for query: ""SeMutFL" "Contrastive Mutation Augmentation" fault localization"

Links: [{"title":"Boosting mutation-based fault localization by effectively generating Higher-Order Mutants - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950584924002659"},{"title":"Boosting mutation-based fault localization by effectively generating Higher-Order Mutants | Information and Software Technology","url":"https://dl.acm.org/doi/abs/10.1016/j.infsof.2024.107660"},{"title":"Improving Mutation-Based Fault Localization via Mutant ...","url":"https://ksiresearch.org/seke/seke22paper/paper157.pdf"},{"title":"SupConFL: Fault Localization with Supervised Contrastive Learning | Request PDF","url":"https://www.researchgate.net/publication/374494097_SupConFL_Fault_Localization_with_Supervised_Contrastive_Learning"},{"title":"Multi-view adaptive contrastive learning for information retrieval based fault localization | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00573-x"},{"title":"Mutation-oriented test data augmentation for GUI software fault localization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S095058491300150X"},{"title":"Metallaxis-FL: Mutation-based fault localization | Request PDF","url":"https://www.researchgate.net/publication/259543317_Metallaxis-FL_Mutation-based_fault_localization"},{"title":"Improving the Performance of Mutation-based Fault Localization via Mutant Bias","url":"https://faculty.buct.edu.cn/_upload/article/files/a6/17/8d5e43d54e4887da82d915653f75/cbb9c7ee-c47d-42e2-9fe4-ab6239283bfc.pdf"},{"title":"Delta4Ms: Improving mutation‐based fault localization by eliminating mutant bias - Liu - 2024 - Software Testing, Verification and Reliability - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/stvr.1872"},{"title":"(PDF) Using Mutation in Fault Localization","url":"https://www.researchgate.net/publication/303563961_Using_Mutation_in_Fault_Localization"}]

Based on the web search results, I found several relevant papers on mutation-based fault localization, but the specific "SeMutFL" paper with "Contrastive Mutation Augmentation" was not directly found in these results. However, the search returned several related works on mutation-based fault localization techniques:

**Key Related Research Areas Found:**

1. **Mutation-Based Fault Localization (MBFL)**: MBFL demonstrates promising fault localization accuracy utilizing impact information of statements provided by First-Order-Mutants (FOMs).

2. **Higher-Order Mutants (HOMs)**: Researchers have proposed HOM generation methods (SFClu, SFDis, and SFDen) to simulate different multiple-faults and improve the effectiveness of MBFL in multiple-fault scenarios.

3. **Contrastive Learning Approaches**: A novel approach named Multi-View Adaptive Contrastive Learning for Information Retrieval Fault Localization (MACL-IRFL) has been proposed to learn relationships for software fault localization.

4. **Data Augmentation for Fault Localization**: A mutation-oriented test data augmentation technique uses novel mutation operators to iteratively mutate failing test cases to derive new test cases useful for fault localization.

The search results did not specifically contain a paper titled "SeMutFL" with "Contrastive Mutation Augmentation." If you're looking for a specific paper with that exact title, you may want to search academic databases like Google Scholar, DBLP, or ArXiv directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea1e8ba4-b1ff-4add-ad38-50e7e91a14eb",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "f31f5eb3-f06a-4fff-8ecb-9584cdeb6b04",
  "sourceToolAssistantUUID": "ea1e8ba4-b1ff-4add-ad38-50e7e91a14eb",
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

_source line 48 · 2026-05-10T06:26:46.159Z_

<details><summary>↩ Tool result · `toolu_01KQYig12UjbWzPKhrXVx51H`</summary>

```text
Web search results for query: ""contrastive mutation" "fault localization" "code understanding" 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Improving the Performance of Mutation-based Fault Localization via Mutant Bias","url":"https://faculty.buct.edu.cn/_upload/article/files/a6/17/8d5e43d54e4887da82d915653f75/cbb9c7ee-c47d-42e2-9fe4-ab6239283bfc.pdf"},{"title":"Multi-view adaptive contrastive learning for information retrieval based fault localization | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00573-x"},{"title":"SupConFL: Fault Localization with Supervised Contrastive Learning | Request PDF","url":"https://www.researchgate.net/publication/374494097_SupConFL_Fault_Localization_with_Supervised_Contrastive_Learning"},{"title":"(PDF) Delta4Ms: Improving mutation‐based fault localization by eliminating mutant bias","url":"https://www.researchgate.net/publication/377450512_Delta4Ms_Improving_mutation-based_fault_localization_by_eliminating_mutant_bias"},{"title":"FLIMs: Fault Localization Interference Mutants, Definition, ...","url":"https://arxiv.org/pdf/2511.23302"},{"title":"Boosting mutation-based fault localization by effectively generating Higher-Order Mutants | Information and Software Technology","url":"https://dl.acm.org/doi/abs/10.1016/j.infsof.2024.107660"},{"title":"DEFault++: Automated Fault Detection, Categorization, and Diagnosis for Transformer Architectures","url":"https://arxiv.org/html/2604.28118"},{"title":"Metallaxis-FL: Mutation-based fault localization | Request PDF","url":"https://www.researchgate.net/publication/259543317_Metallaxis-FL_Mutation-based_fault_localization"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (ICST 2026 - Research Papers) - ICST 2026","url":"https://conf.researchr.org/details/icst-2026/icst-2026-research/30/Assessing-the-Impact-of-Code-Changes-on-the-Fault-Localizability-of-Large-Language-Mo"}]

Based on the search results, here are the key findings related to your query about "contrastive mutation," "fault localization," and "code understanding" in 2026:

## Recent Research Findings

A paper accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) presents the first large-scale empirical investigation into the robustness of LLMs' fault localizability, developing an end-to-end evaluation framework inspired by mutation testing.

### Semantic-Preserving Mutations for Evaluating Code Understanding

The research applies semantic-preserving mutations (SPMs) to assess LLM robustness and whether the LLM's reasoning relies on syntactic cues rather than semantics. The study observed that SPMs cause an LLM to fail to localize the same fault it correctly localized earlier in 78% of cases, and that LLMs' reasoning on the code found earlier in the context is noticeably better.

### Contrastive Learning for Fault Localization

A recent approach named Multi-View Adaptive Contrastive Learning for Information Retrieval Fault Localization (MACL-IRFL) was proposed to learn relationships for software fault localization. Another 2026 work uses supervised contrastive learning combined with prototype matching to separate root causes within the same fault category.

These findings demonstrate active research into improving fault localization through advanced learning techniques and mutation-based evaluation methodologies in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfe2b022-03a7-400f-89d2-8e01e02fc552",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "bf5620e0-ef6c-4b42-ab88-fd3b9d88bd37",
  "sourceToolAssistantUUID": "dfe2b022-03a7-400f-89d2-8e01e02fc552",
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

_source line 49 · 2026-05-10T06:26:48.765Z_

<details><summary>↩ Tool result · `toolu_01G4Nt2Z1xB7tpTEzS23RhN6`</summary>

```text
Web search results for query: "contrastive learning fault localization mutation augmentation code LLM 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"GitHub - CHAOZHAO-1/LLM-based-PHM: This is a reposotory that includes paper about LLM-based fault diagnosis and prognosis. (基于大模型的故障诊断和预测，持续更新)","url":"https://github.com/CHAOZHAO-1/LLM-based-PHM"},{"title":"Multi-view adaptive contrastive learning for information retrieval based fault localization | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00573-x"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Leveraging Mutation Analysis for LLM-based Repair of Quantum Programs","url":"https://www.arxiv.org/pdf/2601.12273"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"[2504.04372] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372"},{"title":"Cellular-based Indoor Localization with Adapted LLM and Label-aware Contrastive Learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11058629"},{"title":"LA-UCL: LLM-Augmented Unsupervised Contrastive Learning Framework for Few-Shot Text Classification - ACL Anthology","url":"https://aclanthology.org/2024.lrec-main.890/"},{"title":"Machine Learning Jun 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-06?skip=1900&show=2000"}]

I found several relevant research results for your query. Here's what the web search revealed:

## Key Finding: 2026 ICST Paper on LLM Fault Localizability

The most directly relevant result is a large-scale empirical investigation into the robustness of LLMs' fault localizability that develops an end-to-end evaluation framework addressing limitations in LLM evaluation, including data contamination, scalability, automation, and extensibility. This research addresses dataset contamination by dynamically injecting faults into real-world seed programs to create unseen fault localization tasks using classical mutation testing, and applies semantic-preserving mutations (such as changes to comments and variable names, and the insertion of dead code) to faulty programs.

## Research Findings

The evaluation included 10 state-of-the-art LLMs on 750,013 fault localization tasks from over 1,300 Java and Python programs, finding that semantic-preserving mutations cause LLMs to fail on previously localized faults in 78% of cases.

## Related Work

The search also identified other recent approaches combining contrastive learning with fault localization: A Multi-View Adaptive Contrastive Learning approach for fault localization generates data augmentations from multiple views and uses graph neural networks to aggregate information about bug reports and source code.

These works represent current trends in applying mutation testing and contrastive learning techniques to evaluate and improve LLM performance on code understanding and fault localization tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2acd9768-2218-4271-bd23-715b6360c35e",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "a3f1dbc964cde1dc5",
  "type": "user",
  "uuid": "a326d244-c924-41c0-bd40-42aeb08b1638",
  "sourceToolAssistantUUID": "2acd9768-2218-4271-bd23-715b6360c35e",
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

_source line 50 · 2026-05-10T06:27:20.232Z_

Excellent. Now let me compile my findings into a comprehensive report for the user.

## Adversarial Review: Verification of Claims in "SeMutFL" Proposal

Based on my comprehensive search of arXiv and academic databases, here are my findings for each claim:

---

### 1. **arXiv 2504.04372 - "Assessing the Impact of Code Changes on the Fault Localizability"**

**Status: VERIFIED**

- **Existence**: Paper exists and was accepted at ICST 2026.
- **78% failure rate claim**: CONFIRMED. The paper reports that semantic-preserving mutations (SPMs) cause LLMs to fail to localize the same fault they correctly localized earlier in **78% of cases**.
- **Scope**: Evaluated 10 state-of-the-art LLMs on ~1,300 Java and Python programs, generating 750,013 unique faulty programs.

**Sources:**
- [arXiv 2504.04372 Abstract](https://arxiv.org/abs/2504.04372)
- [ICST 2026 Conference Paper](https://conf.researchr.org/details/icst-2026/icst-2026-research/30/Assessing-the-Impact-of-Code-Changes-on-the-Fault-Localizability-of-Large-Language-Mo)

---

### 2. **arXiv 2505.10443 - "Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?"**

**Status: PARTIALLY VERIFIED (with clarifications needed)**

- **Existence**: Paper exists.
- **Performance drops up to 70%**: CONFIRMED. Abstract states "performance drops reaching up to 70%."
- **Nine LLMs tested**: CONFIRMED. The study evaluated nine LLMs:
  - **Open-source**: CodeGemma (7B), GraniteCode (8B), Mistral (7B), Qwen2.5-Coder (7B), Qwen3-Coder (30B), SemCoder (7B), Llama3.2 (3B)
  - **Proprietary**: GPT-5.2, Gemini-3

- **Specific performance drops (LiveCodeBench, loop unrolling mutation)**:
  - Gemini-3: **−70.4 percentage points** (highest reported)
  - GPT-5.2: −68.1 points
  - Qwen2.5-Coder: −44.3 points
  - Qwen3-Coder: −35.1 points
  - Others: ranging from −22.1 to −32.8 points

**Important clarification**: The paper measures models' reasoning soundness (10-50% of correct answers derived from flawed logic) rather than purely performance degradation percentages across all mutations.

**Sources:**
- [arXiv 2505.10443 Abstract](https://arxiv.org/abs/2505.10443)
- [Full Paper HTML](https://arxiv.org/html/2505.10443)

---

### 3. **arXiv 2601.18044 - RGFL "Reasoning Guided Fault Localization"**

**Status: VERIFIED (with important clarification)**

- **Existence**: Paper exists.
- **Hit@1 claim (85%)**: PARTIALLY CONFIRMED, but context matters. The paper reports:
  - **File-level Hit@1**: Improves from 71.4% to **85%** (confirmed)
  - **File-level MRR**: Improves from 81.8% to 88.8%
  - **Element-level Exact Match@3**: Increases from 36% to 69%

**Important clarification**: The 85% is specifically for file-level Hit@1 on SWE-bench Verified, not a general performance metric. The method shows hierarchical improvements at different granularity levels.

**Sources:**
- [arXiv 2601.18044 Abstract](https://arxiv.org/abs/2601.18044)
- [Full Paper](https://arxiv.org/html/2601.18044)

---

### 4. **arXiv 2602.11411 - "Improving the Robustness of LLMs for Code Tasks via Fine-tuning with Perturbed Data"**

**Status: VERIFIED (with important distinction)**

- **Existence**: Paper exists.
- **Perturbation types**: CONFIRMED. The paper applies NLP-level perturbations (NOT semantic-preserving code mutations):

  **Character-level (C1-C3)**:
  - ButterFingers: Random character insertions/typos
  - SwapCharacters: Character swaps within words
  - ChangeCharCase: Case modifications

  **Word-level (W1-W3)**:
  - SynonymInsertion: Insertion of synonyms
  - SynonymSubstitution: Replacement with synonyms
  - InflectionalVariation: Word inflection changes

  **Sentence-level (S1-S3)**:
  - BackTranslation: Round-trip translation
  - TenseTransformationPast: Conversion to past tense
  - TenseTransformationFuture: Conversion to future tense

**Critical distinction**: This paper uses NLP-style perturbations (typos, synonyms, back-translation), NOT semantic-preserving code mutations like variable renaming, control flow transformations, or dead code insertion.

**Sources:**
- [arXiv 2602.11411 Abstract](https://arxiv.org/abs/2602.11411)
- [Full Paper HTML](https://arxiv.org/html/2602.11411)

---

### 5. **NEW Papers from March-May 2026 on Surface-Form Robustness**

**Status: LARGELY NEGATIVE SEARCH RESULTS**

I conducted extensive searches using multiple query combinations:
- "fault localization robustness contrastive 2026"
- "semantic mutation augmentation code LLM 2026"
- "code understanding surface-form invariance training 2026"
- "surface-form robust fault localization LLM 2026"

**Key findings:**

1. **No explicit "SeMutFL" paper found**: A paper with the exact title "SeMutFL: Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding in Fault Localization" does not appear in arXiv search results.

2. **Related work from early 2026**:
   - arXiv 2504.04372 (ICST 2026): Semantic-preserving mutations for robustness evaluation
   - arXiv 2506.17369 ("Re-Evaluating Code LLM Benchmarks Under Semantic Mutation"): June 2025, addresses semantic mutations
   - arXiv 2510.23208: "Increasing LLM Coding Capabilities through Diverse Synthetic Coding Tasks" (October 2025): Uses genetic instruction mutation

3. **No papers specifically combining "contrastive mutation" + "surface-form robustness" in fault localization**: The searches returned related work on mutation-based fault localization and contrastive learning separately, but not the specific combination described in your proposal title.

**Sources:**
- [arXiv Fault Localization Search Results](https://arxiv.org/search/?query=fault+localization+contrastive+mutation&searchtype=all)
- [Multi-View Adaptive Contrastive Learning (2409.12519)](https://arxiv.org/html/2409.12519)

---

### 6. **SWE-Gym (arXiv 2412.21139) - Training Configuration Verification**

**Status: VERIFIED**

- **Paper exists**: Yes, published at ICLR 2025.

- **Table 8 statistics - CONFIRMED**:
  - **491 trajectories**: Confirmed (491 resolved successful trajectories)
  - **18,578 average tokens**: CONFIRMED (18,578.5 tokens per trajectory)
  - **Additional metrics in Table 8**:
    - 39.9 LM completion messages per trajectory (~19 turns)
    - Token range: 2,560 to 81,245 tokens

- **Hardware and LoRA configuration - CONFIRMED**:
  - **Model**: Qwen-2.5-Coder (7B, 14B, 32B variants)
  - **Hardware**: 2-8x NVIDIA H100 80G GPUs on Modal
  - **LoRA training specifics** (for 32B verifier):
    - LoRA rank: 64
    - Learning rate: 5×10⁻⁴
    - Max epochs: 2
    - Uses Unsloth library
  - **Standard fine-tuning** (for policy):
    - Learning rate: 1e-4
    - Epochs: 5 maximum
    - Global batch size: 8
    - Max context length: 32,768 tokens

**Sources:**
- [SWE-Gym arXiv 2412.21139](https://arxiv.org/abs/2412.21139)
- [SWE-Gym HTML Version](https://arxiv.org/html/2412.21139v1)
- [Official Paper PDF](https://nlp.cs.berkeley.edu/pubs/Pan-Wang-Neubig-Jaitly-Ji-Suhr-Zhang_2025_SWEGym_paper.pdf)

---

## Summary for Adversarial Review

**Key findings for your proposal evaluation:**

1. ✓ The motivation papers (2504.04372, 2505.10443) with the claimed failure rates **do exist and are verified**.
2. ✓ RGFL (2601.18044) with 85% Hit@1 on SWE-bench **is verified** (file-level metric).
3. ✓ Paper 2602.11411 **exists but applies NLP perturbations, NOT semantic-preserving code mutations** — this is a critical distinction that undermines any claim it's a direct baseline.
4. ✗ **No existing "SeMutFL" paper** with "Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding" appears in March-May 2026 literature.
5. ✓ SWE-Gym table and configuration **fully verified**.

**Critical gap**: Your proposal's novelty claim hinges on the absence of prior work combining contrastive learning with semantic-preserving mutations for fault localization robustness. The search found ample work on each component separately (2504.04372 uses semantic mutations, MACL-IRFL uses contrastive learning), but no prior work combining both specifically for surface-form robustness in fault localization—which would support your proposal's novelty claim if the SeMutFL approach is genuinely new.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a326d244-c924-41c0-bd40-42aeb08b1638",
  "isSidechain": true,
  "agentId": "a3f1dbc964cde1dc5",
  "requestId": "req_011CatQu6UzTe1mYuLM97wkY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d4ab2e24-3e4f-4ea2-b903-ac42271edf09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KzR8sXL2NZC8zN4u5pwbYm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4615,
      "cache_read_input_tokens": 30328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4615,
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
