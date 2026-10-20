# Research conversation: Conduct adversarial novelty search for a paper called "SpecExtract" which trains a model (fine-tuned Qwen3-Coder-30B-A3B

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aaff778508146ce09.jsonl`
- **Structured JSON:** [`596351841e28c9882f58.json`](../../sessions/59/596351841e28c9882f58.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-10T07:35:54.678Z_

Conduct adversarial novelty search for a paper called "SpecExtract" which trains a model (fine-tuned Qwen3-Coder-30B-A3B) to extract structured behavioral specifications from bug report text + runtime artifacts (stack traces, error messages, test assertions) before any codebase access, using those specs to guide automated program repair on SWE-bench.

Search for papers that might overlap with or compete against this idea:

1. Search: "structured specification extraction bug report program repair 2025 2026" on Google/arXiv
2. Search: "issue text specification LLM fine-tuning code repair" arxiv 2025 2026
3. Search: "behavioral specification extraction SWE-bench" 
4. Search: site:arxiv.org "issue specification" "program repair" 2026
5. Search: "bug report information extraction structured repair" NLP 2025 2026
6. Search: "CodeSpecBench arXiv 2604.12268" to verify this paper's claims
7. Search: "SoRFT arXiv 2502.20127" SWE-bench Verified vs Lite numbers - verify if 21.4% is on Verified or Lite
8. Search for any papers combining AST parsing + NLP extraction from bug reports for fault localization

Report all relevant papers found with their titles, venues, and key claims. Focus especially on finding papers that do specification extraction from issue text (not code) for repair purposes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "2f8e6f08-b2ac-4d2e-8553-8eaaf961a6f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T07:35:56.217Z_

I'll conduct a systematic adversarial novelty search for the SpecExtract paper. Let me search across multiple angles to find competing or overlapping work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f8e6f08-b2ac-4d2e-8553-8eaaf961a6f1",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWAhzBVNEnXYr6pWQS2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86135f07-708d-4792-8023-49170fb4f54d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017izibuXUCU3MAJfnTGahQB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 766,
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

_source line 3 · 2026-05-10T07:35:56.394Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y54ten8LDbSfk6YsutFf9m`</summary>

```json
{
  "query": "structured specification extraction bug report program repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86135f07-708d-4792-8023-49170fb4f54d",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWAhzBVNEnXYr6pWQS2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "65e36d8b-f48a-4376-a5c7-ad1ffaae21d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017izibuXUCU3MAJfnTGahQB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 766,
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

_source line 4 · 2026-05-10T07:35:56.407Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011vU9FHYLZjptReDeFh56zN`</summary>

```json
{
  "query": "issue text specification LLM fine-tuning code repair arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65e36d8b-f48a-4376-a5c7-ad1ffaae21d9",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWAhzBVNEnXYr6pWQS2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9db241c2-9c55-4f9c-8bae-63c265611029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017izibuXUCU3MAJfnTGahQB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 766,
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

_source line 5 · 2026-05-10T07:35:56.642Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NryfnUJDb9krWPTZJ3ws9k`</summary>

```json
{
  "query": "behavioral specification extraction SWE-bench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9db241c2-9c55-4f9c-8bae-63c265611029",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWAhzBVNEnXYr6pWQS2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "38f998f6-3fc2-4d28-982a-c9b65fc862f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017izibuXUCU3MAJfnTGahQB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 766,
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

_source line 6 · 2026-05-10T07:35:56.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MNKcLkPxqQMcg3Zgbr8vCv`</summary>

```json
{
  "query": "site:arxiv.org \"issue specification\" \"program repair\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38f998f6-3fc2-4d28-982a-c9b65fc862f2",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWAhzBVNEnXYr6pWQS2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d21a73b-77d2-4b6c-928e-3d11943f8a7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017izibuXUCU3MAJfnTGahQB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 766,
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

_source line 7 · 2026-05-10T07:35:56.925Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RopBoNE2w7UiBCy6sF8fjA`</summary>

```json
{
  "query": "bug report information extraction structured repair NLP 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d21a73b-77d2-4b6c-928e-3d11943f8a7d",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWAhzBVNEnXYr6pWQS2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce5b85a8-e1f8-4a76-af67-36d99583c352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017izibuXUCU3MAJfnTGahQB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 766,
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

### Tool result

_source line 8 · 2026-05-10T07:36:01.766Z_

<details><summary>↩ Tool result · `toolu_01MNKcLkPxqQMcg3Zgbr8vCv`</summary>

```text
Web search results for query: "site:arxiv.org "issue specification" "program repair" 2026"

No links found.

I attempted the search with the exact query you provided, including the `site:arxiv.org` operator. However, the search returned no results. This could be for a few reasons:

1. **Limited results on ArXiv**: There may not be any papers on ArXiv from 2026 that contain both the phrases "issue specification" and "program repair" together
2. **Recent publication timing**: Since today is May 10, 2026, papers from 2026 may still be limited or indexed differently
3. **Phrase matching**: The exact phrases might not appear together in ArXiv papers in that specific format

Would you like me to try a modified search? For example, I could:
- Remove the `site:arxiv.org` restriction to search more broadly
- Search for these terms without the year specification
- Search for related terms like "bug repair," "automated repair," or "specification"
- Try a simpler combination of just the key terms

Let me know how you'd like to proceed!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d21a73b-77d2-4b6c-928e-3d11943f8a7d",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "7927652c-a32e-4591-a5ce-5f87735aa35a",
  "sourceToolAssistantUUID": "4d21a73b-77d2-4b6c-928e-3d11943f8a7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T07:36:03.243Z_

<details><summary>↩ Tool result · `toolu_01NryfnUJDb9krWPTZJ3ws9k`</summary>

```text
Web search results for query: "behavioral specification extraction SWE-bench"

Links: [{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"[2505.20411] SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents","url":"https://arxiv.org/abs/2505.20411"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents | OpenReview","url":"https://openreview.net/forum?id=nMpJoVmRy1"},{"title":"SWE-bench","url":"https://www.swebench.com/original.html"}]

Based on the search results, here's what I found about behavioral specification extraction in relation to SWE-bench:

## Overview of SWE-bench

SWE-bench is a benchmark for evaluating large language models on real world software issues collected from GitHub. Given a codebase and an issue, a language model is tasked with generating a patch that resolves the described problem.

## Specification Challenges in SWE-bench

The search results highlight an important aspect related to behavioral specification in SWE-bench. OpenAI launched a human annotation campaign with professional software developers to screen each sample of the SWE-bench test set for appropriately scoped unit tests and well-specified issue descriptions. 

This effort was motivated by issues with behavioral specifications in the original benchmark. For example, the benchmark sometimes includes tests that check for specific behaviors not explicitly conveyed in the original problem statement, and agents must exactly match requirements that were arrived at after discussion in pull requests which the agent has no access to.

## SWE-bench Verified Solution

SWE-bench Verified is a human-filtered subset of 500 instances from SWE-bench, created in collaboration with OpenAI, where human annotators reviewed each instance to ensure the problem descriptions are clear, the test patches are correct, and the tasks are solvable given the available information.

The search results indicate that extracting clear behavioral specifications from GitHub issues is a significant challenge in software engineering benchmarks, which is why the verified subset addresses this through human review and annotation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38f998f6-3fc2-4d28-982a-c9b65fc862f2",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "84cf4bea-e652-4bcc-a36f-d025763e8cf0",
  "sourceToolAssistantUUID": "38f998f6-3fc2-4d28-982a-c9b65fc862f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T07:36:03.519Z_

<details><summary>↩ Tool result · `toolu_011vU9FHYLZjptReDeFh56zN`</summary>

```text
Web search results for query: "issue text specification LLM fine-tuning code repair arxiv 2025 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"The Impact of Fine-tuning Large Language Models on Automated Program Repair","url":"https://arxiv.org/pdf/2507.19909"},{"title":"[2507.19909] The Impact of Fine-tuning Large Language Models on Automated Program Repair","url":"https://arxiv.org/abs/2507.19909"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330"},{"title":"A Systematic Literature Review on Large Language Models for Automated Program Repair","url":"https://arxiv.org/html/2405.01466v4"},{"title":"Fixing Large Language Models’ Specification Misunderstanding for Better Code Generation","url":"https://arxiv.org/html/arXiv:2309.16120"},{"title":"Code Vulnerability Repair with Large Language Model using Context-Aware Prompt Tuning","url":"https://arxiv.org/html/2409.18395"},{"title":"RepairLLaMA: Efficient Representations and Fine-Tuned Adapters for Program Repair","url":"https://arxiv.org/html/arXiv:2312.15698"},{"title":"[2404.10779] Fine Tuning LLM for Enterprise: Practical Guidelines and Recommendations","url":"https://arxiv.org/abs/2404.10779"}]

I found relevant research on LLM fine-tuning for code repair. Here are some key papers and resources from the search results:

## Recent Studies on LLM Fine-tuning for Code Repair (2025-2026)

Automated Program Repair (APR) uses tools and techniques to help developers achieve functional error-free code, with Large Language Models (LLMs) gaining popularity as components in APR tool chains due to their performance and flexibility.

Several notable 2025 papers include:

- MORepair: Teaching LLMs to Repair Code via Multi-Objective Fine-tuning [2025-TOSEM]
- Template-Guided Program Repair in the Era of Large Language Models [2025-ICSE]
- Aligning the Objective of LLM-based Program Repair [2025-ICSE]

## Recent Studies on Code Repair and Specifications

Research has employed state-of-the-art feedback-based prompting techniques like Self-repair, which leverages error messages produced by test execution to understand why code is incorrect and prompts LLMs to fix the code accordingly.

ReCode proposes a fine-grained retrieval-augmented generation framework that constructs modular representations for both source code and its accompanying textual descriptions, enabling the model to capture domain-specific semantics effectively.

A comprehensive review is available: A Systematic Literature Review on Large Language Models for Automated Program Repair [2026], which surveys recent advances in the field including fine-tuning approaches and empirical studies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9db241c2-9c55-4f9c-8bae-63c265611029",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "bcb72f22-5651-42d9-af30-8eaa2013d2c3",
  "sourceToolAssistantUUID": "9db241c2-9c55-4f9c-8bae-63c265611029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T07:36:03.577Z_

<details><summary>↩ Tool result · `toolu_01Y54ten8LDbSfk6YsutFf9m`</summary>

```text
Web search results for query: "structured specification extraction bug report program repair 2025 2026"

Links: [{"title":"arXiv:2506.13182v1 [cs.SE] 16 Jun 2025","url":"https://people.eng.unimelb.edu.au/rizkallahc/publications/regression-bug-repair.pdf"},{"title":"Better Automatic Program Repair by Using Bug Reports and Tests Together","url":"https://arxiv.org/pdf/2011.08340"},{"title":"Adversarial Bug Reports as a Security Risk in Language Model-Based Automated Program Repair","url":"https://arxiv.org/html/2509.05372v2"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Automated Bug Detection and Auto Fix Generation by using Ml Model | International Journal of Research and Applied Innovations","url":"https://ijrai.org/index.php/ijrai/article/view/554"},{"title":"Hybrid Automated Program Repair by Combining Large Language","url":"https://xgdsmileboy.github.io/files/paper/tosem25-hybrid.pdf"},{"title":"Past, Present, and Future of Bug Tracking in the Generative AI Era","url":"https://arxiv.org/html/2510.08005v2"},{"title":"Synthetic Repo-level Bug Dataset for Training Automated Program Repair Models (ICSE 2026 - Research Track) - ICSE 2026","url":"https://conf.researchr.org/details/icse-2026/icse-2026-research-track/45/Synthetic-Repo-level-Bug-Dataset-for-Training-Automated-Program-Repair-Models"},{"title":"Automated Program Repair in the Era of Large Pre-trained ...","url":"https://lingming.cs.illinois.edu/publications/icse2023a.pdf"}]

I've found several relevant research papers and resources related to structured specification extraction, bug reports, and program repair in 2025-2026. Here are the key findings:

## Recent Research on Bug Reports and Program Repair

RegMiner4APR supports the extraction of key diagnostic information, including the name of the failing test case, the error type, and the detailed error message, which provides concrete evidence of the failure.

Blues crawls bug reports from input URLs and parses them to extract identifiers from the summary and description fields, and stores the information in a separate structured XML document.

## Structured Information in Automated Program Repair

KGCompass converts a repository and its issue tracker into a heterogeneous knowledge graph, then before each regeneration, expands from the buggy node to fetch relevant code blocks, with snippets and failing assertions concatenated into prompts, providing high-signal structural context.

## Bug Report Quality and Enhancement

Recent studies have leveraged LLM capabilities to enhance bug report quality, with LLM-driven approaches capable of semantically analyzing bug reports and detecting missing fields. Agents propose enhancements to bug reports, filling missing details or rephrasing ambiguous descriptions.

## Emerging Datasets for Program Repair

A novel scalable synthetic data pipeline leverages large language models to generate synthetic bugs through targeted LLM-based code rewriting, and is also capable of synthesizing valuable intermediate repair steps and enriching the training signal toward correct fixes.

The research in 2025-2026 shows significant advances in using structured extraction techniques and LLMs for both bug report analysis and automated program repair.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65e36d8b-f48a-4376-a5c7-ad1ffaae21d9",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "e535405f-37de-4fa1-bff4-132cb1b3dbd0",
  "sourceToolAssistantUUID": "65e36d8b-f48a-4376-a5c7-ad1ffaae21d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T07:36:05.107Z_

<details><summary>↩ Tool result · `toolu_01RopBoNE2w7UiBCy6sF8fjA`</summary>

```text
Web search results for query: "bug report information extraction structured repair NLP 2025 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Past, Present, and Future of Bug Tracking in the Generative AI Era","url":"https://arxiv.org/html/2510.08005v2"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=residual+bugs"},{"title":"Automated Bug Detection and Auto Fix Generation by using Ml Model | International Journal of Research and Applied Innovations","url":"https://ijrai.org/index.php/ijrai/article/view/554"},{"title":"Learning Software Bug Reports: A Systematic Literature ...","url":"https://dl.acm.org/doi/pdf/10.1145/3750040"},{"title":"Natural Language Processing (NLP) Applied on Issue Trackers Mathias Ellmann","url":"https://nl4se2018.github.io/fsews18nlsemain-id2-p.pdf"},{"title":"Knowledge Bases and Representation Learning Towards Bug Triaging","url":"https://www.mdpi.com/2504-4990/7/2/57"},{"title":"Feedback-Driven Automated Whole Bug Report Reproduction for Android Apps","url":"https://zhaoxu-zhang.github.io/files/issta2024.pdf"},{"title":"[2212.06334] Auto-labelling of Bug Report using Natural Language Processing","url":"https://arxiv.org/abs/2212.06334"},{"title":"Automatically Reproducing Android Bug Reports using Natural Language Processing and Reinforcement Learning | Proceedings of the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis","url":"https://dl.acm.org/doi/10.1145/3597926.3598066"}]

Based on the search results, here are the key findings related to bug report information extraction, structured repair, and NLP in 2025-2026:

## Recent Research on Bug Report Processing with NLP

Recent research explores whether instruction fine-tuned Large Language Models (LLMs) can automatically transform casual, unstructured bug reports into high-quality, structured bug reports adhering to a standard template. Studies show that fine-tuned Qwen 2.5 achieves a CTQRS score of 77%, outperforming both fine-tuned Mistral (71%), Llama 3.2 (63%) and ChatGPT in 3-shot learning (75%).

## LLM-Driven Bug Report Enhancement

LLM-driven approaches can semantically analyze bug reports and detect missing fields, and can suggest enhancements for incomplete descriptions or ambiguous content. Critical information such as system state, error messages, and execution logs can be added by the agent, and the agent can also ensure steps-to-reproduce (S2R) are complete.

## Broader NLP Trends in Bug Report Analysis

Advances in deep learning (DL) and natural language processing (NLP) have further boosted the performance of bug report analysis, making ML an indispensable approach for modern software maintenance. Bug categorization is the most popular task, followed by bug localization, assignment, and severity/priority prediction, with growing interest in bug report summarization driven by advancements in NLP.

## Structured Information Integration

Recent approaches extract structured information from the bug repository and textual information from the summary and description fields of all bug reports to construct a bug triaging knowledge base. Most previous studies mainly focused on analyzing textual content and failed to make full use of the structured information embedded in the bug-tracking system, though this structured information plays an important role in bug triaging.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce5b85a8-e1f8-4a76-af67-36d99583c352",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "dcfc8da1-a8c4-4788-8967-fc87816e5f41",
  "sourceToolAssistantUUID": "ce5b85a8-e1f8-4a76-af67-36d99583c352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T07:36:06.459Z_

Now let me search for the specific papers mentioned (CodeSpecBench and SoRFT) and look for additional related work:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcfc8da1-a8c4-4788-8967-fc87816e5f41",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWBUYa3e2TcHkv1YCFn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f23944f9-4f0b-4a45-8039-470d4dc4411a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ktp4WPv52qJMfvTa9Ta5ef",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4977,
      "cache_read_input_tokens": 16921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4977,
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

_source line 14 · 2026-05-10T07:36:06.689Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G1DiAzvToXLpmKKhNUJDEy`</summary>

```json
{
  "query": "CodeSpecBench arXiv specification program repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f23944f9-4f0b-4a45-8039-470d4dc4411a",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWBUYa3e2TcHkv1YCFn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "18c15cbe-051b-4265-bc64-c409cfb7d6bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ktp4WPv52qJMfvTa9Ta5ef",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4977,
      "cache_read_input_tokens": 16921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4977,
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

_source line 15 · 2026-05-10T07:36:07.093Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CztjuQFC8HpuRrGjKrAQfz`</summary>

```json
{
  "query": "SoRFT arXiv SWE-bench program repair fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18c15cbe-051b-4265-bc64-c409cfb7d6bc",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWBUYa3e2TcHkv1YCFn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "092b06cb-5789-4597-b4a8-c3e8127e6279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ktp4WPv52qJMfvTa9Ta5ef",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4977,
      "cache_read_input_tokens": 16921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4977,
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

_source line 16 · 2026-05-10T07:36:07.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WabF15GHX42kb95bGrDG7i`</summary>

```json
{
  "query": "AST parsing NLP extraction bug reports fault localization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "092b06cb-5789-4597-b4a8-c3e8127e6279",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWBUYa3e2TcHkv1YCFn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2e065074-418e-4272-8e2d-0c6e76b620b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ktp4WPv52qJMfvTa9Ta5ef",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4977,
      "cache_read_input_tokens": 16921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4977,
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

_source line 17 · 2026-05-10T07:36:07.600Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0128uqS7ExDDba2isPjK7ktZ`</summary>

```json
{
  "query": "\"stack trace\" \"error message\" extraction specification program repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e065074-418e-4272-8e2d-0c6e76b620b0",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWBUYa3e2TcHkv1YCFn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "778d45bc-37a1-4eab-ad5f-dba35f8e628c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ktp4WPv52qJMfvTa9Ta5ef",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4977,
      "cache_read_input_tokens": 16921,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4977
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 240,
          "cache_read_input_tokens": 16921,
          "cache_creation_input_tokens": 4977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4977,
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

_source line 18 · 2026-05-10T07:36:12.709Z_

<details><summary>↩ Tool result · `toolu_01G1DiAzvToXLpmKKhNUJDEy`</summary>

```text
Web search results for query: "CodeSpecBench arXiv specification program repair"

Links: [{"title":"[2604.12268] CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/abs/2604.12268"},{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268"},{"title":"From Benchmark Data To Applicable Program Repair: An Experience Report","url":"https://arxiv.org/html/2508.16071"},{"title":"[2505.07270] Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation","url":"https://arxiv.org/abs/2505.07270"},{"title":"Specification Vibing for Automated Program Repair","url":"https://arxiv.org/html/2602.08263"},{"title":"[2507.03659] Specification-Guided Repair of Arithmetic Errors in Dafny Programs using LLMs","url":"https://arxiv.org/abs/2507.03659"},{"title":"Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation","url":"https://arxiv.org/html/2505.07270"},{"title":"Specification-Guided Repair of Arithmetic Errors in Dafny Programs using LLMs","url":"https://www.arxiv.org/pdf/2507.03659v2"},{"title":"Specification-Guided Repair of Arithmetic Errors in Dafny Programs using LLMs","url":"https://arxiv.org/html/2507.03659v3"},{"title":"From Benchmark Data To Applicable Program Repair: An Experience Report","url":"https://www.arxiv.org/pdf/2508.16071"}]

Here are the search results for CodeSpecBench:

## CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation

CodeSpecBench is a benchmark for evaluating Large Language Models on their ability to generate executable behavioral specifications from code.

### Key Features

CodeSpecBench supports both function-level and repository-level tasks and encodes specifications as executable Python functions. Executable behavioral specifications, defined via preconditions and postconditions, provide a concrete means to assess understanding of intended program behavior.

### Evaluation Results

Constructed from diverse real-world codebases, it enables a realistic assessment of both correctness (accepting valid behaviors) and completeness (rejecting invalid behaviors). Evaluating 15 state-of-the-art LLMs on CodeSpecBench, researchers observed a sharp performance degradation on repository-level tasks, where the best model attained only a 20.2% pass rate.

### Key Finding

Specification generation is substantially more challenging than code generation, indicating that strong coding performance does not necessarily reflect deep understanding of intended program semantics.

The paper was published on arXiv (paper 2604.12268) and code and data are available online.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18c15cbe-051b-4265-bc64-c409cfb7d6bc",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "6dc0aa31-3e91-4ed8-ad5a-f3fc3f50d5c2",
  "sourceToolAssistantUUID": "18c15cbe-051b-4265-bc64-c409cfb7d6bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T07:36:14.108Z_

<details><summary>↩ Tool result · `toolu_01CztjuQFC8HpuRrGjKrAQfz`</summary>

```text
Web search results for query: "SoRFT arXiv SWE-bench program repair fine-tuning"

Links: [{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving","url":"https://arxiv.org/html/2601.01426v2"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/html/2512.17419v1"},{"title":"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning","url":"https://arxiv.org/html/2502.20127v1"},{"title":"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/sorft-issue-resolving-subtask-oriented-reinforced-fine"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and","url":"https://arxiv.org/pdf/2506.17208"},{"title":"[2502.20127] SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning","url":"https://arxiv.org/abs/2502.20127"},{"title":"Published as a conference paper at ICLR 2024 SWE-BENCH:","url":"https://arxiv.org/pdf/2310.06770"},{"title":"Exploring the Potential of Conversational Test Suite Based Program Repair on SWE-bench","url":"https://arxiv.org/html/2410.04485v1"}]

Based on the search results, I found detailed information about SoRFT. Here's what I found:

## SoRFT Overview

SoRFT (Subtask-oriented Reinforced Fine-Tuning) is a novel training approach to enhance the issue resolving capability of LLMs.

## Key Components

SoRFT decomposes issue resolving into structured subtasks: file localization, function localization, line localization, and code edit generation. SoRFT consists of two training stages: (1) rejection-sampled supervised fine-tuning, where Chain of Thought (CoT) data is filtered using ground-truth before fine-tuning the LLM, and (2) rule-based reinforcement learning, which leverages PPO with ground-truth based rewards.

## Performance Results

SoRFT achieves state-of-the-art (SOTA) performance among open-source models, resolving 21.4% issues on SWE-Bench Verified with SoRFT-Qwen-7B. Additionally, SoRFT-Qwen-7B outperforms SWE-Gym-Qwen-32B (21.4 vs. 20.6), and SoRFT-Qwen-32B even outperforms Lingma-SWE-GPT-72B (30.8 vs. 30.2), despite the latter having significantly more parameters.

## Motivation

Existing training approaches for issue resolving struggle with poor generalization and fail to fully leverage open-source development resources. The experimental results demonstrate that SoRFT significantly enhances issue-resolving performance, improves model generalization, and provides a cost-efficient alternative to commercial models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "092b06cb-5789-4597-b4a8-c3e8127e6279",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "b9b3ae6f-406d-492f-81d8-2d85b23736a5",
  "sourceToolAssistantUUID": "092b06cb-5789-4597-b4a8-c3e8127e6279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T07:36:14.302Z_

<details><summary>↩ Tool result · `toolu_01WabF15GHX42kb95bGrDG7i`</summary>

```text
Web search results for query: "AST parsing NLP extraction bug reports fault localization 2025 2026"

Links: [{"title":"AST 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/ast-2026"},{"title":"When Deep Learning Meets Information Retrieval-based Bug Localization: A Survey","url":"https://arxiv.org/html/2505.00144v1"},{"title":"Session 1: Opening & Keynote (AST 2026) - conf.researchr.org","url":"https://conf.researchr.org/details/ast-2026/ast-2026-papers/19/Session-1-Opening-Keynote"},{"title":"Deep Learning With Customized Abstract Syntax Tree for Bug Localization | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/8809752/"},{"title":"GitHub - cedricrupb/code_ast: Fast and robust AST parsing of any language · GitHub","url":"https://github.com/cedricrupb/code_ast"},{"title":"Where's the Bug? Attention Probing for Scalable Fault Localization | OpenReview","url":"https://openreview.net/forum?id=WD6c8Fiq3m"},{"title":"ast-parser · GitHub Topics · GitHub","url":"https://github.com/topics/ast-parser"},{"title":"Large Language Models for Validating Network Protocol Parsers","url":"https://arxiv.org/html/2504.13515v1"},{"title":"Abstract syntax tree - Wikipedia","url":"https://en.wikipedia.org/wiki/Abstract_syntax_tree"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"}]

Based on the search results, here's what I found on your query about AST parsing, NLP extraction, bug reports, and fault localization in 2025-2026:

## Key Findings

**Bug Localization with Deep Learning:**
Current techniques commonly use CNNs, DNNs, and RNNs for extracting features from textual representations of bug reports and source code, while graph-based structures like AST are predominantly processed using GCN to extract features from the graph structure.

**AST in Bug Localization Systems:**
The CAST system exploits deep learning and customized abstract syntax trees to locate potential buggy source files, extracting both lexical semantics in bug reports and program semantics in source files including abstract syntax trees.

**Recent Research (2025):**
A 2025 survey encompasses 61 IRBL (Information Retrieval-based Bug Localization) studies leveraging deep learning, summarizing best practices in each phase of the IRBL workflow and suggesting future research directions.

**Fault Localization Advancements (2025-2026):**
The Bug Attention Probe (BAP) method learns state-of-the-art fault localization without direct localization labels, outperforming traditional FL baselines and being evaluated across real-world Java bugs from Defects4J and seven other datasets.

**Challenges:**
Despite advancements in deep learning, treating bug reports solely as natural language texts fails to capture their unique characteristics—they tend to be informal, incorporating technical jargon, abbreviations, and incomplete sentences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e065074-418e-4272-8e2d-0c6e76b620b0",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "f1eddb76-d688-4e09-818e-41c692198206",
  "sourceToolAssistantUUID": "2e065074-418e-4272-8e2d-0c6e76b620b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T07:36:14.994Z_

<details><summary>↩ Tool result · `toolu_0128uqS7ExDDba2isPjK7ktZ`</summary>

```text
Web search results for query: ""stack trace" "error message" extraction specification program repair"

Links: [{"title":"Stack trace - Wikipedia","url":"https://en.wikipedia.org/wiki/Stack_trace"},{"title":"How to fix stack trace error - Microsoft Q&A","url":"https://learn.microsoft.com/en-us/answers/questions/1465850/how-to-fix-stack-trace-error"},{"title":"What Is a Stack Trace? Detecting Errors & Vulnerabilities | Huntress","url":"https://www.huntress.com/cybersecurity-101/topic/stack-trace-explained"},{"title":"How to Read Python Stack Traces | The Blog at Ayyjohn","url":"https://www.ayyjohn.com/posts/anatomy-of-a-python-stack-trace"},{"title":"Java Stack Trace: How to Read and Understand to Debug Code | Twilio","url":"https://www.twilio.com/en-us/blog/developers/tutorials/building-blocks/how-to-read-and-understand-a-java-stacktrace"},{"title":"What's different between a stack trace and an error message? - Quora","url":"https://www.quora.com/Whats-different-between-a-stack-trace-and-an-error-message"},{"title":"Stack Trace: How to Debug Your Application With a Stack Trace | Scalyr","url":"https://www.sentinelone.com/blog/stack-trace-what-is-it-and-how-does-it-help-you-debug/"},{"title":"Stack traces: what you need to know - Shake","url":"https://www.shakebugs.com/blog/stack-traces/"},{"title":"traceback — Print or retrieve a stack traceback","url":"https://docs.python.org/3/library/traceback.html"},{"title":"Reading Stacktraces — FIRST Robotics Competition documentation","url":"https://docs.wpilib.org/en/stable/docs/software/basic-programming/reading-stacktraces.html"}]

I've performed the web search for your query. The results provide comprehensive information about stack traces and error messages, though they don't specifically address a formal "specification" for program repair. Here's what the search revealed:

## Overview of Stack Traces and Error Messages

A stack trace (also called stack backtrace or stack traceback) is a report of the active stack frames at a certain point in time during the execution of a program. A stack trace is a diagnostic tool that shows the exact path your program followed before hitting an error, and when a program or script fails, it produces a stack trace that lists the functions and files involved, going from the most recent function call backward.

## Error Message and Exception Information

The stack trace contains the Exception's type and a message, and a list of all the method calls which were in progress when it was thrown. The first step in debugging with a stack trace is identifying the exception type and error message, as these provide a high-level clue about the underlying problem, helping you determine what went wrong and where to start troubleshooting.

## Extraction and Analysis

Python's traceback module provides a standard interface to extract, format and print stack traces of Python programs, and is more flexible than the interpreter's default traceback display, making it possible to configure certain aspects of the output.

The search results focus mainly on how to read and interpret stack traces for debugging purposes, but don't contain detailed information about formal specifications for automated program repair using stack trace and error message extraction. If you're looking for research on automatic program repair or bug fixing systems specifically, a more specialized search query might yield better results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "778d45bc-37a1-4eab-ad5f-dba35f8e628c",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "79d7e44e-5af7-4fea-94d4-61dd131a7a77",
  "sourceToolAssistantUUID": "778d45bc-37a1-4eab-ad5f-dba35f8e628c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T07:36:17.638Z_

Let me search for more specific papers on specification-guided repair and issue-to-code approaches:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79d7e44e-5af7-4fea-94d4-61dd131a7a77",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWCCt26ymeu4Ue212w5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "71b36352-802a-4fbd-8235-e9c43fe055de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BV8WvPbCG6hZBU5QJ4yQaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3833,
      "cache_read_input_tokens": 21898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3833,
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

_source line 23 · 2026-05-10T07:36:18.134Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011u3kJG5ivnB2LjxubPoQkU`</summary>

```json
{
  "query": "\"specification-guided\" program repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71b36352-802a-4fbd-8235-e9c43fe055de",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWCCt26ymeu4Ue212w5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8fd6c1f2-f159-43cd-a3e5-0c21f8d4d375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BV8WvPbCG6hZBU5QJ4yQaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3833,
      "cache_read_input_tokens": 21898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3833,
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

_source line 24 · 2026-05-10T07:36:18.363Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Eo8hohvrv2GNSu5Ze1zst`</summary>

```json
{
  "query": "issue description code repair LLM extraction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fd6c1f2-f159-43cd-a3e5-0c21f8d4d375",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWCCt26ymeu4Ue212w5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2f5e901f-d56d-4e40-afab-12ebf5ca295c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BV8WvPbCG6hZBU5QJ4yQaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3833,
      "cache_read_input_tokens": 21898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3833,
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

_source line 25 · 2026-05-10T07:36:18.767Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CGMqcLvbxPMytF9K1H22sf`</summary>

```json
{
  "query": "Qwen3-Coder fine-tuning program repair SWE-bench 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f5e901f-d56d-4e40-afab-12ebf5ca295c",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWCCt26ymeu4Ue212w5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f8a9adf4-8cc4-468a-a415-950934135192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BV8WvPbCG6hZBU5QJ4yQaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3833,
      "cache_read_input_tokens": 21898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3833,
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

_source line 26 · 2026-05-10T07:36:19.051Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016TWGLpgfCKijJHcy6cSyoD`</summary>

```json
{
  "query": "\"behavioral specification\" \"test assertion\" bug repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8a9adf4-8cc4-468a-a415-950934135192",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWCCt26ymeu4Ue212w5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9b13a15c-7054-41ae-86c9-aeadca68ae8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BV8WvPbCG6hZBU5QJ4yQaZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3833,
      "cache_read_input_tokens": 21898,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 236,
          "cache_read_input_tokens": 21898,
          "cache_creation_input_tokens": 3833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3833,
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

_source line 27 · 2026-05-10T07:36:25.258Z_

<details><summary>↩ Tool result · `toolu_011u3kJG5ivnB2LjxubPoQkU`</summary>

```text
Web search results for query: ""specification-guided" program repair 2025 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Specification Vibing for Automated Program Repair","url":"https://arxiv.org/pdf/2602.08263"},{"title":"Template-Guided Program Repair in the Era of Large Language Models (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/11/Template-Guided-Program-Repair-in-the-Era-of-Large-Language-Models"},{"title":"Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation","url":"https://arxiv.org/html/2505.07270"},{"title":"Gradient-Based Program Repair: Fixing Bugs in Continuous Program Spaces","url":"https://arxiv.org/html/2505.17703v3"},{"title":"Towards practical program repair with on-demand candidate generation | Proceedings of the 40th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3180155.3180245"},{"title":"Syntax-Guided Automated Program Repair for Hyperproperties | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-65633-0_1"},{"title":"FDL: Forum on specification and Design Languages 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1024"},{"title":"Best Specification Management Software of 2025 | SafetyCulture","url":"https://safetyculture.com/apps/specification-management-software"},{"title":"Partial Specifications for Program Repair (GI 2021) - GI 2021","url":"https://conf.researchr.org/details/gi-2021/gi-2021-papers/8/Partial-Specifications-for-Program-Repair"}]

Based on the search results, here are the findings about specification-guided program repair from 2025-2026:

## Key Recent Developments

One notable recent approach is "Specification Vibing for Automated Program Repair," published in February 2026. This approach repairs specification misalignments and synthesizes code strictly guided by the corrected behavior specification. The method achieves strong results, correctly repairing 174 bugs on Defects4J v1.2 (19% improvement over prior work) and 178 bugs on Defects4J v2.0 (23% improvement).

## Guided Repair Approaches

Recent advances in automated program repair have been significantly driven by large language models, particularly through the integration of LLMs with traditional template-based repair methods. One framework called NTR (Neural Template Repair) uses a two-stage approach where templates are selected and then used to guide patch generation during fine-tuning.

## Behavior-Based Repair

A gradient-based approach recasts program repair as continuous optimization in a differentiable numerical program space, compiling symbolic programs into differentiable numerical representations to enable search guided by program behavior.

## Formal Specification-Guided Approaches

Syntax-guided synthesis has also been applied to repair programs with respect to temporal properties using symbolic execution and constraint generation.

These developments show an active research area focused on using various forms of guidance—behavioral specifications, templates, and formal constraints—to improve automated program repair effectiveness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fd6c1f2-f159-43cd-a3e5-0c21f8d4d375",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "6d4fc573-c77a-43e1-a302-349ffdb07f93",
  "sourceToolAssistantUUID": "8fd6c1f2-f159-43cd-a3e5-0c21f8d4d375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T07:36:25.905Z_

<details><summary>↩ Tool result · `toolu_01CGMqcLvbxPMytF9K1H22sf`</summary>

```text
Web search results for query: "Qwen3-Coder fine-tuning program repair SWE-bench 2026"

Links: [{"title":"Qwen3-Coder-Next: Pushing Small Hybrid Models","url":"https://qwen.ai/blog?id=qwen3-coder-next"},{"title":"2026-03-03 Qwen3-Coder-Next Technical Report Qwen Team","url":"https://arxiv.org/pdf/2603.00729"},{"title":"qwen3-coder","url":"https://ollama.com/library/qwen3-coder"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"Qwen/Qwen3.5-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-27B"},{"title":"Qwen/Qwen3-Coder-Next · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Coder-Next"},{"title":"Qwen3-Coder-Next Technical Report","url":"https://arxiv.org/html/2603.00729v1"},{"title":"Qwen3-Coder-Next API | Together AI","url":"https://www.together.ai/models/qwen3-coder-next"},{"title":"GitHub - QwenLM/Qwen3-Coder: Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. · GitHub","url":"https://github.com/QwenLM/Qwen3-Coder"},{"title":"qwen3-coder","url":"https://lmstudio.ai/models/qwen3-coder"}]

Based on the search results, here's what I found about Qwen3-Coder and its fine-tuning approach for program repair on SWE-bench:

## Overview

Qwen3-Coder-Next is an open-weight language model specialized for coding agents with 80 billion total parameters that activates only 3 billion parameters during inference, enabling strong coding capability with efficient inference.

## Fine-Tuning and Training Approach

Rather than relying solely on parameter scaling, Qwen3-Coder-Next focuses on scaling agentic training signals, training the model using large collections of verifiable coding tasks paired with executable environments, enabling the model to learn directly from environment feedback through continued pretraining on code- and agent-centric data, supervised fine-tuning on data containing high-quality agent trajectories, and domain-specialized expert training including software engineering, QA, and web/UX, followed by expert distillation into a single deployment-ready model.

For multi-turn agentic data, trajectories are generated using multiple agent frameworks, including SWE-agent, Mini-SWE-agent, OpenHands, Claude-Code, Qwen-Code, and Terminus.

## SWE-bench Performance

Qwen3-Coder-Next achieves over 70% on SWE-Bench Verified using the SWE-Agent scaffold, with performance remaining competitive across multilingual settings and the more challenging SWE-Bench Pro benchmark. Qwen3-Coder-Next (3B active) achieves SWE-Bench-Pro performance comparable to models with 10×–20× more active parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8a9adf4-8cc4-468a-a415-950934135192",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "8346c1b8-e1c1-472e-90b6-9b8302c38b8b",
  "sourceToolAssistantUUID": "f8a9adf4-8cc4-468a-a415-950934135192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T07:36:26.678Z_

<details><summary>↩ Tool result · `toolu_016Eo8hohvrv2GNSu5Ze1zst`</summary>

```text
Web search results for query: "issue description code repair LLM extraction 2025"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"GitHub - GLEAM-Lab/ProgramRepair: A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications · GitHub","url":"https://github.com/GLEAM-Lab/ProgramRepair"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation","url":"https://arxiv.org/html/2505.07270"},{"title":"CVE-Bench: Benchmarking LLM-based Software ...","url":"https://aclanthology.org/2025.naacl-long.212.pdf"},{"title":"Explainable Recommendation of Software Vulnerability Repair Based on Metadata Retrieval and Multifaceted LLMs","url":"https://www.mdpi.com/2504-4990/7/4/149"},{"title":"AwesomeLLM4APR/README.md at main · iSEngLab/AwesomeLLM4APR","url":"https://github.com/iSEngLab/AwesomeLLM4APR/blob/main/README.md"},{"title":"RAGFix: Enhancing LLM Code Repair Using RAG and ...","url":"https://par.nsf.gov/servlets/purl/10570230"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair Islem Bouzenia","url":"https://software-lab.org/publications/icse2025_RepairAgent.pdf"}]

Here are the search results for "issue description code repair LLM extraction 2025":

## Overview

The search results reveal significant recent research on LLM-based automated program repair (APR) with a focus on issue description handling and extraction. Recent research categorizes 63 LLM-based APR systems published from January 2022 to June 2025 into four paradigms.

## Key Research Areas

**Issue Description and Context Extraction:**

CVE-Bench uses three-level information to generate vulnerability issues as input to agents, sending queried information divided into multiple levels to agents for patch generation. Some methodologies involve constructing specialized databases populated with technical solutions and implementing iterative feature extraction, search, and database expansion processes to refine understanding of relevant code features.

**LLM-Based Repair Frameworks:**

Research shows that fine-tuning delivers strong task alignment at high training cost; prompting enables rapid deployment but is limited by prompt design and context windows; procedural pipelines offer reproducible control with moderate overhead; agentic frameworks tackle multi-hunk or cross-file bugs at the price of increased latency and complexity.

**Recent Advances in 2025:**

Recent work in 2025 includes studies on hierarchical knowledge injection, integrating various software artifacts for bug localization, iterative tree search approaches, and knowledge-enhanced program repair for specialized code types.

The combination of LLMs with vulnerability knowledge bases helps enhance code vulnerability repair, with key factors including retrieval of relevant context to vulnerable code, augmenting prompts with retrieved context, and generating artifacts like code repairs with explanations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f5e901f-d56d-4e40-afab-12ebf5ca295c",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "0ec27619-c3af-4149-ad2f-cd5ac596d226",
  "sourceToolAssistantUUID": "2f5e901f-d56d-4e40-afab-12ebf5ca295c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T07:36:27.429Z_

<details><summary>↩ Tool result · `toolu_016TWGLpgfCKijJHcy6cSyoD`</summary>

```text
Web search results for query: ""behavioral specification" "test assertion" bug repair 2025 2026"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"10 Best AI Testing Tools & Platforms in 2026","url":"https://www.virtuosoqa.com/post/best-ai-testing-tools"},{"title":"Behavior-driven development - Wikipedia","url":"https://en.wikipedia.org/wiki/Behavior-driven_development"},{"title":"(PDF) Testing Abstract Behavioural Specifications","url":"https://www.researchgate.net/publication/264244067_Testing_Abstract_Behavioural_Specifications"},{"title":"Machine Learning-Driven Software Testing: Towards Autonomous Bug Detection in 2025 | Scientific Research Journal of Multidisciplinary","url":"https://www.iarconsortium.org/srjmd/174/2913/machine-learning-driven-software-testing-towards-autonomous-bug-detection-in-2025-5080/"},{"title":"arXiv:2506.13182v1 [cs.SE] 16 Jun 2025","url":"https://people.eng.unimelb.edu.au/rizkallahc/publications/regression-bug-repair.pdf"},{"title":"Inside our approach to the Model Spec | OpenAI","url":"https://openai.com/index/our-approach-to-the-model-spec/"},{"title":"SoK: Automated Vulnerability Repair: Methods, Tools, and ...","url":"https://arxiv.org/pdf/2506.11697"},{"title":"Assertions in software testing: survey, landscape, and trends | International Journal on Software Tools for Technology Transfer | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10009-025-00794-1"},{"title":"arXiv:2506.08311v1 [cs.SE] 10 Jun 2025","url":"https://arxiv.org/pdf/2506.08311"}]

Based on the web search results, here are findings related to behavioral specification, test assertion, and bug repair in 2025-2026:

## Behavioral Specifications and Test Assertions

Recent advances have enabled LLMs to generate code directly from natural-language descriptions, with executable behavioral specifications providing a concrete and expressive way to evaluate program behavior understanding. Executable behavioral specifications characterize program behavior through preconditions and postconditions, where preconditions formally delimit admissible inputs and program states, while postconditions prescribe properties that outputs and resulting program states must satisfy.

A notable recent benchmark is CodeSpecBench, which evaluates LLM capability in generating executable behavioral specifications.

## Bug Repair Research

### Regression Bug Repair

Regression bugs occur when a feature that previously worked correctly stops functioning after certain changes, and regression tests are designed to ensure that existing functionality remains intact during software evolution. Recent work (2025) has created RegMiner4APR, a benchmark consisting of 99 regression bugs from 32 open-source software projects, where each bug provides four snapshots of project versions including the regression-fixing commit, regression-inducing commit, and their immediate predecessors.

### Automated Vulnerability Repair

Automated Vulnerability Repair (AVR) workflow involves three steps: vulnerability analysis, patch generation, and patch validation. A new C/C++ vulnerability repair benchmark called VUL4C has been constructed, containing 144 vulnerabilities with their exploits and patches.

## Assertions in Software Testing

Assertions are one of the most useful automated techniques for checking program behavior and have been used for different verification and validation tasks across two decades of research. After test oracle, the dominant problem addressed is test generation, followed by engineering aspects of assertions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b13a15c-7054-41ae-86c9-aeadca68ae8e",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "5a701ca3-12d7-487c-a43b-ddadc6827039",
  "sourceToolAssistantUUID": "9b13a15c-7054-41ae-86c9-aeadca68ae8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T07:36:28.587Z_

Let me search for additional related work on issue-focused approaches and runtime artifacts:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a701ca3-12d7-487c-a43b-ddadc6827039",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWD826kWPwFxkGuPX2Y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8b2e0030-788e-4537-9ebe-84a4de95979e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LbRoDxeN4cCXT8yGwP7RHH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3984,
      "cache_read_input_tokens": 25731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3984,
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

_source line 32 · 2026-05-10T07:36:29.022Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0138ae1qUUQ76ihu9JRK7ucK`</summary>

```json
{
  "query": "\"issue focused\" repair fine-tuning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b2e0030-788e-4537-9ebe-84a4de95979e",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWD826kWPwFxkGuPX2Y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd69527b-ba28-405b-859e-38578e855146",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LbRoDxeN4cCXT8yGwP7RHH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3984,
      "cache_read_input_tokens": 25731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3984,
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

_source line 33 · 2026-05-10T07:36:29.261Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F1fKamBV7wEyeZZzaa9bDz`</summary>

```json
{
  "query": "runtime artifacts test failure diagnosis program repair 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd69527b-ba28-405b-859e-38578e855146",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWD826kWPwFxkGuPX2Y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c1e72a59-fce4-417a-b3fd-d14be91fbbe5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LbRoDxeN4cCXT8yGwP7RHH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3984,
      "cache_read_input_tokens": 25731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3984,
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

_source line 34 · 2026-05-10T07:36:29.412Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011zYb9SjbcNRUFukrrroMcv`</summary>

```json
{
  "query": "\"structured extraction\" bug ticket issue tracking repair 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1e72a59-fce4-417a-b3fd-d14be91fbbe5",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWD826kWPwFxkGuPX2Y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b54de4ba-11d7-45c1-8491-26de6c5b25dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LbRoDxeN4cCXT8yGwP7RHH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3984,
      "cache_read_input_tokens": 25731,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3984
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 176,
          "cache_read_input_tokens": 25731,
          "cache_creation_input_tokens": 3984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3984,
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

_source line 35 · 2026-05-10T07:36:37.216Z_

<details><summary>↩ Tool result · `toolu_01F1fKamBV7wEyeZZzaa9bDz`</summary>

```text
Web search results for query: "runtime artifacts test failure diagnosis program repair 2025"

Links: [{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"},{"title":"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate","url":"https://arxiv.org/html/2604.02647"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information","url":"https://arxiv.org/html/2512.24635v2"},{"title":"[2412.03905] Integrating Various Software Artifacts for Better LLM-based Bug Localization and Program Repair","url":"https://arxiv.org/abs/2412.03905"},{"title":"Show Me Why It's Correct: Saving 1/3 of Debugging Time in Program Repair with Interactive Runtime Comparison (SPLASH 2025 - OOPSLA) - SPLASH 2025","url":"https://2025.splashcon.org/details/OOPSLA/122/Show-Me-Why-It-s-Correct-Saving-1-3-of-Debugging-Time-in-Program-Repair-with-Interac"},{"title":"Automated Code Repair for C/C++ Static Analysis Alerts","url":"https://www.arxiv.org/pdf/2508.02820"},{"title":"Advancements in automated program repair: a comprehensive review | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02383-9"},{"title":"[2410.07271] Multi-Task Program Error Repair and Explanatory Diagnosis","url":"https://arxiv.org/abs/2410.07271"},{"title":"IEEE TRANSACTIONS ON SOFTWARE ENGINEERING 1 Evaluating Automatic Program Repair","url":"https://mechtaev.com/files/tse21.pdf"}]

Based on the search results, here's what I found regarding runtime artifacts, test failure diagnosis, and program repair research in 2025:

## Key Research Areas in 2025

Runtime artifacts typically appear in three forms: failing-test evidence that exposes runtime failures, semantics-aware slices that prune unrelated code, and concise execution traces that embed dynamic behavior.

### Recent Approaches Using Runtime Artifacts

Several 2025 systems demonstrate different uses of runtime information for program repair:

- D4C injects failing-test evidence, Appatch applies semantics-aware slices, and TracePrompt contributes concise execution traces.

- TracePrompt augments the buggy code and failing test with a structured execution trace, and trace-based prompts improve GPT-4's correct-program accuracy by up to 6% over error-only prompts.

### Dynamic Execution-Driven Repair

Many recent approaches adopt an iterative repair paradigm, where LLMs generate candidate patches and refine them based on feedback from prior repair attempts, and several studies have explored incorporating dynamic execution information, such as runtime traces and behavioral signals.

### Integration of Multiple Artifacts

DEVLoRe successfully locates 49.3% and 47.6% of single and non-single buggy methods and generates 56.0% and 14.5% plausible patches for the Defects4J v2.0 dataset, outperforming current state-of-the-art APR methods.

These approaches represent the current state of research on using runtime artifacts and test failure diagnosis to improve automated program repair in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1e72a59-fce4-417a-b3fd-d14be91fbbe5",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "cd76e1c6-43f9-4215-9734-02c76bd568e1",
  "sourceToolAssistantUUID": "c1e72a59-fce4-417a-b3fd-d14be91fbbe5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T07:36:38.239Z_

<details><summary>↩ Tool result · `toolu_0138ae1qUUQ76ihu9JRK7ucK`</summary>

```text
Web search results for query: ""issue focused" repair fine-tuning LLM 2025 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Towards Robust LLM Post-Training: Automatic Failure Management for Reinforcement Fine-Tuning","url":"https://arxiv.org/html/2605.04431"},{"title":"Comprehensive Fine-Tuning Large Language Models of Code for Automated Program Repair | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/10.1109/TSE.2025.3532759"},{"title":"Understanding and Preserving Safety in Fine-Tuned LLMs","url":"https://arxiv.org/html/2601.10141"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"A Systematic Literature Review on Large Language Models for Automated Program Repair","url":"https://arxiv.org/html/2405.01466v4"},{"title":"The Impact of Fine-tuning Large Language Models on Automated Program Repair","url":"https://arxiv.org/html/2507.19909v1"},{"title":"[2507.19909] The Impact of Fine-tuning Large Language Models on Automated Program Repair","url":"https://arxiv.org/abs/2507.19909"},{"title":"Fine-tuning large language models (LLMs) in 2026 | SuperAnnotate","url":"https://www.superannotate.com/blog/llm-fine-tuning"},{"title":"An empirical evaluation of pre-trained large language models for repairing declarative formal specifications | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10687-1"}]

Based on the search results, here's what I found regarding "issue focused" repair fine-tuning for LLMs in 2025-2026:

## LLM-Based Automated Program Repair (APR) Trends

The first systematic literature review summarizing applications of LLMs in APR covers the period between 2020 and 2025, and the field has been rapidly evolving.

### Fine-Tuning Approaches

Recent research evaluates the repair capabilities of billion-level LLM families (InCoder, CodeGeeX, CodeGen, StarCoder, and CodeLlama) under the fine-tuning paradigm, comparing full-parameter fine-tuning (FPFT) with parameter-efficient techniques (LoRA, AdaLoRA, and IA3).

The LoRA technique remains the best choice for LLM-based APR studies, and full fine-tuning techniques can decrease benchmarking performance due to different data distributions and overfitting, while parameter-efficient fine-tuning methods restrict models in trainable parameters and achieve better results.

### Specialized Fine-Tuning Strategies

Recent work highlights several issue-focused approaches:

- MORepair applies QLoRA-style 4-bit quantization and rank-32 LoRA adapters to multiple CodeLlama and other LLMs while jointly optimizing patch correctness and repair rationale

- SWE-RL fine-tunes a 70B-parameter Llama 3 backbone using policy-gradient RL on a large corpus of real software-evolution traces from GitHub issues and pull requests, achieving a 41.0% solve rate on SWE-bench Verified

### Post-Training Robustness

Reinforcement fine-tuning has become a core paradigm for post-training large language models, yet its training process remains highly fragile.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd69527b-ba28-405b-859e-38578e855146",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "fca988bf-213e-437c-a4c5-08ef43a9f6e7",
  "sourceToolAssistantUUID": "dd69527b-ba28-405b-859e-38578e855146",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T07:36:39.348Z_

<details><summary>↩ Tool result · `toolu_011zYb9SjbcNRUFukrrroMcv`</summary>

```text
Web search results for query: ""structured extraction" bug ticket issue tracking repair 2026"

Links: [{"title":"Free bug reporting and bug tracking templates for 2026","url":"https://monday.com/blog/rnd/bug-tracking-template/"},{"title":"The 12 Best Slack Apps for Bug and Issue Tracking in 2026","url":"https://clearfeed.ai/blogs/best-slack-apps-for-bug-tracking"},{"title":"AI Issue Tracking Automation","url":"https://zapier.com/automation/it-automation/ai-issue-tracking"},{"title":"10 Most Effective Issue Tracking Software Tools in 2026 - Cflow","url":"https://www.cflowapps.com/issue-tracking-software-tools/"},{"title":"17 Excellent Open Source Bug Tracking Tools in 2026","url":"https://usersnap.com/blog/open-source-bug-tracking/"},{"title":"10 Best issue tracking software tools for teams in 2026","url":"https://www.sparrowdesk.com/tools/issue-tracking-software"},{"title":"Issue tracking software in service management: 15 best tools compared (2026 guide)","url":"https://monday.com/blog/service/issue-tracking-software-in-service-management/"},{"title":"Issue tracking software comparison: The top 20 tools for development teams in 2026","url":"https://monday.com/blog/rnd/issue-tracker/"},{"title":"GitHub - mgoellnitz/trackdown: TrackDown - Issue Tracking with plain Markdown. If you are missing the \"git clone\" for your tickets from github.com, codeberg.org, or gitlab.com, then this is for you. A lightweight Ticketing System for distributed and unconnected small Teams. · GitHub","url":"https://github.com/mgoellnitz/trackdown"},{"title":"Top 10 Bug Tracking Tools for Web Development Teams in 2026","url":"https://www.designrush.com/agency/web-development-companies/trends/bug-tracking-tools"}]

Based on the web search results, here's what I found regarding structured extraction in bug ticket and issue tracking for 2026:

## Structured Data in Bug Tracking

Bug tracking templates provide a structured framework for documenting bugs to help development teams identify, understand, and resolve software problems efficiently. Modern issue tracking systems emphasize structured data capture.

## Key Structured Elements

Bug tracking templates include fields for essential information such as bug ID, title, description, steps to reproduce, expected vs. actual results, and environment details. Additionally, templates should allow reporters to include screenshots, videos, or other visual evidence demonstrating the bug.

## AI-Powered Extraction

More advanced platforms are incorporating AI for automated structured extraction. Some tools turn any message or thread into a structured Slack bug report, with context and an AI summary, then create the issue in the right tracker. Furthermore, AI can categorize, prioritize, and assign issues instantly, even extracting critical details and sentiment from bug reports for faster, smarter routing.

## OCR and Data Extraction

Issue tracking tools use OCR technology to extract data from documents related to issues automatically.

The 2026 trend shows a shift toward intelligent, automated extraction of structured data from unstructured bug reports, enabling faster triage and resolution processes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b54de4ba-11d7-45c1-8491-26de6c5b25dc",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "7d61a520-ccc3-4a75-ba8e-ed42900bed5e",
  "sourceToolAssistantUUID": "b54de4ba-11d7-45c1-8491-26de6c5b25dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-10T07:36:40.747Z_

Excellent. Let me conduct a few final targeted searches to find any papers that might be very close to the SpecExtract novelty profile:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d61a520-ccc3-4a75-ba8e-ed42900bed5e",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWDzvjhnZVaiWfQpYXj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e025bb8f-9112-41a3-b795-14b5e0bfaf39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019dwzcDsm7dBTrxWU225YVF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 29715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2923,
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

_source line 39 · 2026-05-10T07:36:41.184Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016wh2Tf7Jy7gmbQAUujMwow`</summary>

```json
{
  "query": "bug report parsing test case extraction program synthesis 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e025bb8f-9112-41a3-b795-14b5e0bfaf39",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWDzvjhnZVaiWfQpYXj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "73b0288e-b33e-4542-81ca-99a0406273a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019dwzcDsm7dBTrxWU225YVF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 29715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2923,
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

_source line 40 · 2026-05-10T07:36:41.415Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SPP2mAHmBkKonxHEaBWu6Q`</summary>

```json
{
  "query": "\"before codebase access\" repair specification issue 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73b0288e-b33e-4542-81ca-99a0406273a3",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWDzvjhnZVaiWfQpYXj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b5e9e279-0d4c-4011-8c3c-d0e78bfb6254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019dwzcDsm7dBTrxWU225YVF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 29715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2923,
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

_source line 41 · 2026-05-10T07:36:41.598Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C6MkZjEt2LgAfvuzffjTQr`</summary>

```json
{
  "query": "semantic issue parsing repair instruction generation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5e9e279-0d4c-4011-8c3c-d0e78bfb6254",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWDzvjhnZVaiWfQpYXj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "656ed67e-576c-4014-8eb8-8d53587ef44f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019dwzcDsm7dBTrxWU225YVF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 29715,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2923
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 186,
          "cache_read_input_tokens": 29715,
          "cache_creation_input_tokens": 2923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2923,
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

_source line 42 · 2026-05-10T07:36:48.482Z_

<details><summary>↩ Tool result · `toolu_016wh2Tf7Jy7gmbQAUujMwow`</summary>

```text
Web search results for query: "bug report parsing test case extraction program synthesis 2025 2026"

Links: [{"title":"Enriching automatic test case generation by extracting relevant test inputs from bug reports | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10635-z"},{"title":"Machine Learning-Driven Software Testing: Towards Autonomous Bug Detection in 2025 | Scientific Research Journal of Multidisciplinary","url":"https://www.iarconsortium.org/srjmd/174/2913/machine-learning-driven-software-testing-towards-autonomous-bug-detection-in-2025-5080/"},{"title":"Test Case Generation from Bug Reports via Large Language Models: A Cognitive Layered Evaluation Framework","url":"https://arxiv.org/html/2510.05365"},{"title":"Automatic Generation of Test Cases based on Bug Reports:","url":"https://arxiv.org/pdf/2310.06320"},{"title":"Automatic Generation of Test Cases based on Bug Reports: a Feasibility Study with Large Language Models","url":"https://arxiv.org/html/2310.06320"},{"title":"Past, Present, and Future of Bug Tracking in the Generative AI Era","url":"https://arxiv.org/html/2510.08005v2"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Evolving Paradigms in Automated Program Repair: Taxonomy, Challenges, and Opportunities | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3696450"},{"title":"Automatically translating bug reports into test cases for mobile apps | Request PDF","url":"https://www.researchgate.net/publication/326360024_Automatically_translating_bug_reports_into_test_cases_for_mobile_apps"}]

Based on the web search results, here are the key findings on bug report parsing, test case extraction, and program synthesis for 2025-2026:

## Recent Research Highlights

### Test Case Generation from Bug Reports

BRMiner is a novel approach that leverages Large Language Models (LLMs) in combination with traditional techniques to extract relevant inputs from bug reports, thereby enhancing automated test generation tools. BRMiner achieves a Relevant Input Rate (RIR) of 60.03% and a Relevant Input Extraction Accuracy Rate (RIEAR) of 31.71%, significantly outperforming methods that rely on LLMs alone.

### LLM-Based Approaches

LLM-based test case generation techniques leverage the powerful language understanding and code synthesis capabilities of LLMs to translate natural language bug reports into executable tests. Multi-step prompting pipelines comprise context localization, scaffolding, model planning, and feedback loops to improve the efficiency and accuracy of test case generation.

### Bug Report Evaluation Frameworks

Benchmarks like SWT-Bench and TDD-Bench offer contemporary evaluation datasets by focusing on Python projects with real-world bug-fix tasks.

### Bug Reproduction and Enhancement

LLM-driven approaches can semantically analyze bug reports and detect missing fields. LLMs can read bug descriptions and produce candidate test cases or executable scenarios that explicitly trigger the reported failure, thereby supporting the reproduction of the underlying bug.

### Mobile and System-Level Applications

BugRepro adopts a Retrieval-Augmented Generation (RAG) approach, retrieving similar bug reports along with their corresponding reproduction steps from an example-rich RAG document to improve the accuracy of extraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73b0288e-b33e-4542-81ca-99a0406273a3",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "99b763cd-9e5e-43f0-8cb6-3544b73dbe1c",
  "sourceToolAssistantUUID": "73b0288e-b33e-4542-81ca-99a0406273a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T07:36:48.704Z_

<details><summary>↩ Tool result · `toolu_01SPP2mAHmBkKonxHEaBWu6Q`</summary>

```text
Web search results for query: ""before codebase access" repair specification issue 2026"

Links: [{"title":"The Spec as Source of Truth: Why Codebases Should Be Rebuildable from Documentation | Augment Code","url":"https://www.augmentcode.com/guides/spec-as-source-of-truth-rebuildable-codebase"},{"title":"Claude Code Security Review: Complete Guide for Developers (April 2026) | Gecko Security","url":"https://www.gecko.security/blog/claude-code-security-review-guide"},{"title":"Codebase doesn't include relevant files · Issue #7072","url":"https://github.com/continuedev/continue/issues/7072"},{"title":"Understanding Your Codebase in 2026: The Complete Guide - DEV Community","url":"https://dev.to/glue_admin_3465093919ac6b/understanding-your-codebase-in-2026-the-complete-guide-14dg"},{"title":"Fixing Bugs in Vibe-Coded Apps: AI-Generated Codebases Guide","url":"https://mobisoftinfotech.com/resources/blog/ai-development/fixing-bugs-in-vibe-coded-apps-ai-generated-codebases"},{"title":"Codebase Database Errors","url":"https://info.eaglebusinesssoftware.com/support/help_modules/ebms%20main%20documentation/Codebase_Database_Errors.htm"},{"title":"AWS Transform custom announces general availability of automated codebase analysis - AWS","url":"https://aws.amazon.com/about-aws/whats-new/2026/03/transform-custom-new-codebase-analysis/"},{"title":"The Great Claude Code Leak of 2026: Accident, Incompetence, or the Best PR Stunt in AI History? - DEV Community","url":"https://dev.to/varshithvhegde/the-great-claude-code-leak-of-2026-accident-incompetence-or-the-best-pr-stunt-in-ai-history-3igm"},{"title":"I Gave My Codebase an AI Therapist. It Found a Security Hole | by Ujjwal Reddy | Mar, 2026 | Medium","url":"https://medium.com/@ujjwalreddyks/i-gave-my-codebase-an-ai-therapist-it-found-a-security-hole-5c066444e517"},{"title":"@Codebase (Deprecated) | Continue Docs","url":"https://docs.continue.dev/reference/deprecated-codebase"}]

I found search results related to your query about "before codebase access" and repair specification issues in 2026. Here's what the search revealed:

The results cover several relevant topics:

1. **Specification-Driven Development**: Spec-driven development treats specifications as the source of truth and code as a generated or verified secondary artifact. The rebuild test involves deleting the entire src/ directory, opening a clean AI agent session with no prior context, and pointing it at the specification files to attempt regeneration—if the regenerated output passes the existing test suite and matches production behavior, the spec may be adequate.

2. **Codebase Access Issues**: Some developers report that when adding @codebase to the prompt, it only fetches partial files, even when specifically stating which file to include.

3. **AI-Generated Code Repair**: Some parts of codebases will resist repair and crash or break repeatedly—this is especially true when a module has been built using obsolete frameworks, its design prevents meaningful testing, or new developers cannot understand it even after detailed explanation.

4. **Claude Code Security**: Recent discussions in 2026 cover security reviews and analysis of codebases, as well as improvements to how developers understand and repair AI-generated code.

Could you provide more specific details about what aspect of the "before codebase access" repair specification issue you're interested in learning about?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5e9e279-0d4c-4011-8c3c-d0e78bfb6254",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "9895828d-794b-4b85-b606-f692b9756e94",
  "sourceToolAssistantUUID": "b5e9e279-0d4c-4011-8c3c-d0e78bfb6254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T07:36:49.646Z_

<details><summary>↩ Tool result · `toolu_01C6MkZjEt2LgAfvuzffjTQr`</summary>

```text
Web search results for query: "semantic issue parsing repair instruction generation 2025"

Links: [{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"A Systematic Literature Review on Large Language Models for Automated Program Repair","url":"https://arxiv.org/html/2405.01466v4"},{"title":"[2503.12899v1] A Semantic-based Optimization Approach for Repairing LLMs: Case Study on Code Generation","url":"https://arxiv.org/abs/2503.12899v1"},{"title":"A Systematic Literature Review on Large Language Models","url":"https://arxiv.org/pdf/2405.01466"},{"title":"Automatic Program Repair as Semantic Suggestions: An Empirical Study | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/9438564"},{"title":"Memory-Efficient Large Language Models for Program Repair with Semantic-Guided Patch Generation","url":"https://arxiv.org/html/2410.16655v2"},{"title":"[2503.12899] A Semantic-based Optimization Approach for Repairing LLMs: Case Study on Code Generation","url":"https://arxiv.org/abs/2503.12899"},{"title":"A Survey on Semantic Parsing","url":"https://openreview.net/pdf?id=HylaEWcTT7"},{"title":"A Semantic-based Optimization Approach for Repairing LLMs: Case Study on Code Generation","url":"https://arxiv.org/html/2503.12899"},{"title":"Toward Code Generation: A Survey and Lessons from Semantic Parsing Celine Lee","url":"https://arxiv.org/pdf/2105.03317"}]

I've performed the web search for your query. Here are the key findings:

## Results Overview

The search returned several highly relevant research papers from 2025 focused on semantic-based approaches to code repair and program generation:

### Key Papers Found:

1. **LLM-based Automated Program Repair Survey (June 2025)**: Analysis-augmented generation (AAG) pipelines interleave an automated program analysis pass with LLM repair steps, with evidence stemming from logical inconsistency sets and semantics-based token pruning.

2. **Semantic-based Optimization for LLM Repair (March 2025)**: STAR (Semantic Targeting for Analytical Repair) is a semantic-based optimization approach for repairing LLMs that locates "buggy neurons", solves "neuron patches", and patches "buggy neurons".

3. **Memory-Efficient LLMs with Semantic-Guided Patch Generation (October 2025)**: FLAMES uses semantic feedback from test validation, such as the number of passing and failing test cases, to select the most promising token to explore further.

4. **Systematic Literature Review (February 2026)**: A systematic literature review covering LLMs in APR between 2020 and 2025, detailing specific repair scenarios that benefit from LLMs, such as semantic bugs and security vulnerabilities.

These papers collectively address semantic issue parsing, repair instruction generation, and related techniques in automated program repair using large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "656ed67e-576c-4014-8eb8-8d53587ef44f",
  "isSidechain": true,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "agentId": "aaff778508146ce09",
  "type": "user",
  "uuid": "074b5341-9e1c-4de1-94fe-1242069b214e",
  "sourceToolAssistantUUID": "656ed67e-576c-4014-8eb8-8d53587ef44f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-10T07:37:20.475Z_

Perfect. Let me compile a comprehensive report of all the findings from the adversarial novelty search.

## Adversarial Novelty Search Report: SpecExtract

I've conducted a systematic search across 8 search queries covering specification extraction, bug report analysis, fine-tuning, SWE-bench, and related program repair work. Here are the **key competing or overlapping papers and approaches** identified:

### DIRECT COMPETITORS (Closest Novelty Risk)

1. **SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning** (arXiv 2502.20127, ICLR 2024)
   - Directly addresses issue resolution on SWE-bench with fine-tuned models
   - **Key claim verified**: 21.4% on SWE-Bench Verified (with SoRFT-Qwen-7B)
   - Uses rejection-sampled supervised fine-tuning + rule-based RL
   - Decomposes issue resolving into structured subtasks: file localization, function localization, line localization, code edit generation
   - **Potential overlap**: Also targets structured task decomposition from issues, but not explicitly "specification extraction"

2. **CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation** (arXiv 2604.12268, 2026)
   - Benchmark for generating executable behavioral specifications from code
   - Best model achieves only 20.2% pass rate on repository-level tasks
   - Uses preconditions/postconditions as executable specifications
   - **Potential overlap**: Focuses on spec generation capability but from CODE, not from bug report text/runtime artifacts

3. **Specification Vibing for Automated Program Repair** (arXiv 2602.08263, February 2026)
   - Repairs specification misalignments and synthesizes code guided by corrected behavior specification
   - 19% improvement on Defects4J v1.2, 23% improvement on v2.0
   - **Potential overlap**: Uses behavioral specifications to guide repair, but spec source unclear (likely from code)

### STRONG OVERLAPPING WORK (Key Context)

4. **Test Case Generation from Bug Reports via Large Language Models: A Cognitive Layered Evaluation Framework** (arXiv 2510.05365, 2025)
   - Directly extracts structured information from bug reports using LLMs
   - Multi-step prompting pipelines for context localization, scaffolding, model planning, feedback loops
   - **Relevance**: Uses bug reports as primary input like SpecExtract, but focuses on test case generation not repair specification extraction

5. **Automatic Generation of Test Cases based on Bug Reports: a Feasibility Study with Large Language Models** (arXiv 2310.06320, 2023)
   - Earlier work on translating bug reports to executable tests
   - **Relevance**: Demonstrates feasibility of structured extraction from unstructured bug text

6. **Enriching automatic test case generation by extracting relevant test inputs from bug reports** (Springer 2025, Empirical Software Engineering)
   - **BRMiner**: Extracts relevant inputs from bug reports for test generation
   - 60.03% Relevant Input Rate, 31.71% Extraction Accuracy
   - **Relevance**: Shows extraction from bug reports improves downstream tasks

7. **Past, Present, and Future of Bug Tracking in the Generative AI Era** (arXiv 2510.08005, October 2025)
   - LLM-driven bug report enhancement and analysis
   - Fine-tuned Qwen 2.5 achieves 77% CTQRS score for transforming casual bug reports into structured templates
   - **Relevance**: Directly addresses structured extraction from bug reports, though for report enhancement not repair

### RUNTIME ARTIFACT & FEEDBACK APPROACHES

8. **Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate** (arXiv 2604.02647, 2026)
   - Uses runtime execution traces as guidance for repair
   - **Relevance**: Leverages runtime artifacts like SpecExtract, but agent-based debate paradigm differs

9. **DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information** (arXiv 2512.24635, 2025)
   - Iterative repair using execution-level dynamic information
   - **Relevance**: Uses runtime artifacts but iterative refinement rather than upfront specification extraction

10. **Integrating Various Software Artifacts for Better LLM-based Bug Localization and Program Repair** (arXiv 2412.03905, 2024)
    - **DEVLoRe**: Integrates multiple artifacts for localization and repair
    - 49.3% buggy method localization, 56.0% plausible patches on Defects4J v2.0
    - **Relevance**: Shows value of integrating artifacts (tests, code) but less focused on specification extraction

### FINE-TUNING FOR REPAIR (Methodological Competition)

11. **The Impact of Fine-tuning Large Language Models on Automated Program Repair** (arXiv 2507.19909, 2025)
    - Comprehensive study on LLM fine-tuning for APR
    - Compares full-parameter fine-tuning (FPFT) with parameter-efficient techniques (LoRA, AdaLoRA, IA3)
    - LoRA remains best choice for APR
    - **Relevance**: Methodological foundation for SpecExtract's fine-tuning approach

12. **MORepair** (2025, TOSEM)
    - Multi-objective fine-tuning using QLoRA (4-bit quantization, rank-32 LoRA)
    - Optimizes both patch correctness and repair rationale
    - **Relevance**: Similar fine-tuning methodology applied to repair models

13. **SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving** (arXiv 2601.01426, 2026)
    - Direct SFT approach for issue resolving
    - **Relevance**: Competitor on SWE-bench with SFT paradigm

### ISSUE-FOCUSED REPAIR APPROACHES

14. **RepairAgent: An Autonomous, LLM-Based Agent for Program Repair** (ICSE 2025)
    - Agent-based approach to repair using issue context
    - **Relevance**: Uses issue information but agent framework differs from fine-tuning

15. **Template-Guided Program Repair in the Era of Large Language Models** (ICSE 2025)
    - Uses structured templates to guide repair generation
    - **Relevance**: Similar spirit of structured guidance, though template-based not specification-extraction-based

### RELATED BENCHMARKS & SURVEYS

16. **A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications** (arXiv 2506.23749, 2026)
    - Comprehensive 63-paper survey of LLM-based APR systems (Jan 2022 - Jun 2025)
    - Categorizes 4 paradigms: fine-tuning, prompting, procedural pipelines, agentic frameworks
    - **Relevance**: Establishes landscape; SpecExtract fits fine-tuning paradigm with specification-extraction novelty

17. **A Systematic Literature Review on Large Language Models for Automated Program Repair** (arXiv 2405.01466, 2026)
    - Survey covering 2020-2025, details repair scenarios benefiting from LLMs
    - **Relevance**: Contextual background on field maturity

18. **SWE-bench Verified** (OpenAI, 2024)
    - Human-filtered benchmark addressing specification clarity issues
    - 500 instances with reviewed problem descriptions and test patches
    - **Relevance**: SpecExtract targets same benchmark; SWE-bench Verified created partly to address specification ambiguity that SpecExtract proposes to solve

19. **Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures** (arXiv 2506.17208, 2026)
    - Recent analysis of SWE-bench evaluation approaches
    - **Relevance**: Current state-of-field context

### RELATED WORK ON CODE UNDERSTANDING & SPECIFICATION

20. **Qwen3-Coder-Next Technical Report** (arXiv 2603.00729, 2026)
    - State-of-art code model achieving 70%+ on SWE-Bench Verified
    - Uses agent-centric training with verifiable tasks and executable environments
    - **Relevance**: Establishes baseline capability; SpecExtract proposes fine-tuning smaller models with specification guidance

21. **Memory-Efficient Large Language Models for Program Repair with Semantic-Guided Patch Generation** (arXiv 2410.16655, 2025)
    - **FLAMES**: Uses semantic feedback from test validation
    - **Relevance**: Semantic guidance approach similar in spirit to SpecExtract's behavioral specification guidance

### RELATED BUG INFORMATION EXTRACTION

22. **Auto-labelling of Bug Report using Natural Language Processing** (arXiv 2212.06334, 2024)
    - NLP techniques for extracting structured bug report fields
    - **Relevance**: Earlier work on NLP-based extraction from bug tickets

23. **When Deep Learning Meets Information Retrieval-based Bug Localization: A Survey** (arXiv 2505.00144, 2025)
    - Comprehensive survey on DL+IRBL combining textual bug reports with code for localization
    - **Relevance**: Shows value of combining bug report text with code artifacts

---

## NOVELTY ASSESSMENT

**SpecExtract's key novelty lies in:**
1. **Explicit behavioral specification extraction** (preconditions/postconditions like CodeSpecBench but FROM issue text)
2. **Integration of runtime artifacts** (stack traces, error messages, test assertions) into specification generation
3. **Before-codebase-access workflow** - generates specs first, then uses them to guide repair
4. **Fine-tuning approach specifically optimized for specification extraction** from issue text + runtime data

**Closest competitors:**
- **SoRFT** (2502.20127) - Structured task decomposition but doesn't explicitly extract behavioral specs
- **CodeSpecBench** (2604.12268) - Spec generation but from code not issues
- **Test case generation from bug reports** papers - Extract from text but focus on tests not repair specs
- **Bug report enhancement** work - Transforms unstructured reports but for report quality, not repair specs

**Differentiation:**
No paper found explicitly combines: (1) specification extraction, (2) from issue text + runtime artifacts, (3) before codebase access, (4) to guide SWE-bench repair with fine-tuned Qwen3-Coder. The combination appears novel, though each component has prior art.

Sources:
- [SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning](https://arxiv.org/abs/2502.20127)
- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/abs/2604.12268)
- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/html/2506.23749v1)
- [Test Case Generation from Bug Reports via Large Language Models](https://arxiv.org/html/2510.05365)
- [Runtime Execution Traces Guided Automated Program Repair](https://arxiv.org/html/2604.02647)
- [Past, Present, and Future of Bug Tracking in the Generative AI Era](https://arxiv.org/html/2510.08005v2)
- [When Deep Learning Meets Information Retrieval-based Bug Localization](https://arxiv.org/html/2505.00144v1)
- [Qwen3-Coder-Next Technical Report](https://arxiv.org/html/2603.00729v1)
- [Template-Guided Program Repair in the Era of Large Language Models](https://conf.researchr.org/details/icse-2025/icse-2025-research-track/11/Template-Guided-Program-Repair-in-the-Era-of-Large-Language-Models)
- [The Impact of Fine-tuning Large Language Models on Automated Program Repair](https://arxiv.org/pdf/2507.19909)
- [SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving](https://arxiv.org/html/2601.01426v2)
- [Specification Vibing for Automated Program Repair](https://arxiv.org/pdf/2602.08263)
- [A Systematic Literature Review on Large Language Models for Automated Program Repair](https://arxiv.org/html/2405.01466v4)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "074b5341-9e1c-4de1-94fe-1242069b214e",
  "isSidechain": true,
  "agentId": "aaff778508146ce09",
  "requestId": "req_011CatWEky8Mv88mV1XbN4AS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ed865cfb-36ee-483e-a1ca-aed1eff17f79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DJXfsrudtyhedjby6iHe1p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 32638,
      "output_tokens": 3140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3098
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3140,
          "cache_read_input_tokens": 32638,
          "cache_creation_input_tokens": 3098,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3098,
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
