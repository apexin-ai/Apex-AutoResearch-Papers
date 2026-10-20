# Research conversation: I need to verify specific numbers from two NLP/code papers for an adversarial review. Please search for: 1. **SoRFT pape

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ad56e0f2ccf31b19b.jsonl`
- **Structured JSON:** [`d0cf55d4cbce8d8e366c.json`](../../sessions/d0/d0cf55d4cbce8d8e366c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-10T06:57:10.188Z_

I need to verify specific numbers from two NLP/code papers for an adversarial review. Please search for:

1. **SoRFT paper** (arXiv 2502.20127, "SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning", ACL 2025): 
   - Search for the paper and find its actual performance numbers on SWE-bench Lite and SWE-bench Verified
   - The question is: does SoRFT-7B achieve 21.4% on SWE-bench Lite or SWE-bench Verified? And what is the number for the other benchmark?
   - Try: site:arxiv.org SoRFT subtask reinforced fine-tuning SWE-bench
   - Try: "SoRFT" SWE-bench Lite Verified results 2025

2. **SpecRover paper** (arXiv 2408.02232, ICSE 2025): 
   - Does it have a Section V-A or error analysis that identifies "51.7%" or "107/207" instances failing due to "ambiguous issue descriptions"?
   - Try: site:arxiv.org SpecRover code intent extraction LLM SWE-bench 2408.02232
   - Try: SpecRover ICSE 2025 failure analysis ambiguous issue description

Report back the actual numbers found for SoRFT, and what SpecRover's error analysis actually says (verbatim if possible).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "ad56e0f2ccf31b19b",
  "type": "user",
  "uuid": "8de1927b-ed01-4688-b5da-1bf0213b20f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T06:57:11.093Z_

I'll search for these papers and verify the specific numbers you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8de1927b-ed01-4688-b5da-1bf0213b20f1",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTDMqTTZsy7fH4Greds",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dbf64ef1-5633-417b-90c1-489292167d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X8pc753dyPjkS42BdVxBZC",
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

_source line 3 · 2026-05-10T06:57:11.315Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018k1FivA1oN7UDr2cpNW3aK`</summary>

```json
{
  "query": "site:arxiv.org SoRFT subtask reinforced fine-tuning SWE-bench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbf64ef1-5633-417b-90c1-489292167d9e",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTDMqTTZsy7fH4Greds",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "504d7ccd-9a0b-4abe-b77e-0c67900ab4fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X8pc753dyPjkS42BdVxBZC",
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

_source line 4 · 2026-05-10T06:57:11.535Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018UCzyWPSMQKwRCjN5R6eyq`</summary>

```json
{
  "query": "\"SoRFT\" SWE-bench Lite Verified results 2025 ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "504d7ccd-9a0b-4abe-b77e-0c67900ab4fe",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTDMqTTZsy7fH4Greds",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0ac2edbc-6b51-4c3b-91b1-1913ef93c5a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X8pc753dyPjkS42BdVxBZC",
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

_source line 5 · 2026-05-10T06:57:11.735Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017bauLnVoPFQnuej3j6eve2`</summary>

```json
{
  "query": "site:arxiv.org SpecRover code intent extraction 2408.02232"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ac2edbc-6b51-4c3b-91b1-1913ef93c5a7",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTDMqTTZsy7fH4Greds",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2708a677-335a-4de7-9ebc-39144b2c8d0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X8pc753dyPjkS42BdVxBZC",
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

_source line 6 · 2026-05-10T06:57:11.839Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B5TGa1U7oTA1m5DVTv3aXX`</summary>

```json
{
  "query": "SpecRover ICSE 2025 ambiguous issue description error analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2708a677-335a-4de7-9ebc-39144b2c8d0f",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTDMqTTZsy7fH4Greds",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6e9c459-f15b-435e-b637-e2ffd955d74b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X8pc753dyPjkS42BdVxBZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 16155,
      "output_tokens": 251,
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
          "output_tokens": 251,
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

_source line 7 · 2026-05-10T06:57:17.088Z_

<details><summary>↩ Tool result · `toolu_018k1FivA1oN7UDr2cpNW3aK`</summary>

```text
Web search results for query: "site:arxiv.org SoRFT subtask reinforced fine-tuning SWE-bench"

Links: [{"title":"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning","url":"https://arxiv.org/html/2502.20127"},{"title":"[2502.20127] SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning","url":"https://arxiv.org/abs/2502.20127"},{"title":"SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving","url":"https://arxiv.org/html/2601.01426v2"},{"title":"BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills","url":"https://arxiv.org/pdf/2510.19898"},{"title":"[2601.01426] SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving","url":"https://arxiv.org/abs/2601.01426"},{"title":"[2506.19767] SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning","url":"https://arxiv.org/abs/2506.19767"},{"title":"SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning","url":"https://arxiv.org/html/2506.19767v1"},{"title":"[2401.08967] ReFT: Reasoning with Reinforced Fine-Tuning","url":"https://arxiv.org/abs/2401.08967"},{"title":"REFT: Reasoning with REinforced Fine-Tuning","url":"https://arxiv.org/pdf/2401.08967"},{"title":"[2510.09872] WARC-Bench: Web Archive Based Benchmark for GUI Subtask Executions","url":"https://arxiv.org/abs/2510.09872"}]

I found relevant results for your search. Here are the key findings:

SoRFT (Subtask-oriented Reinforced Fine-Tuning) is a novel training approach to enhance the issue resolving capability of LLMs. It decomposes issue resolving into structured subtasks: file localization, function localization, line localization, and code edit generation.

SoRFT consists of two training stages: rejection-sampled supervised fine-tuning (SFT) and rule-based reinforcement learning (RL). In the SFT stage, a teacher LLM generates CoT data for each subtask and filters negative samples based on ground-truth answers, then performs supervised fine-tuning to help the model grasp the subtask structures, underlying reasoning mechanisms, and output formats essential for issue resolving. In the RL stage, scoring rules are defined based on ground-truth for each subtask, and the LLM's parameters are updated using reward-based optimization.

SoRFT-trained LLMs achieve state-of-the-art performance on SWE-Bench Verified and SWE-Bench Lite.

The paper was published on arxiv.org on February 27, 2025, with the identifier 2502.20127.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "504d7ccd-9a0b-4abe-b77e-0c67900ab4fe",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "ad56e0f2ccf31b19b",
  "type": "user",
  "uuid": "dae82078-68eb-4d5e-a1a3-426ac858b16b",
  "sourceToolAssistantUUID": "504d7ccd-9a0b-4abe-b77e-0c67900ab4fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T06:57:17.477Z_

<details><summary>↩ Tool result · `toolu_018UCzyWPSMQKwRCjN5R6eyq`</summary>

```text
Web search results for query: ""SoRFT" SWE-bench Lite Verified results 2025 ACL"

Links: [{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.559/"},{"title":"Rigorous Evaluation of Coding Agents on SWE-Bench","url":"https://aclanthology.org/2025.acl-long.189.pdf"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Results Viewer","url":"https://www.swebench.com/viewer.html"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified is Flawed Despite Expert Review: UTBoost Exposes Gaps in Test Coverage | by Daniel Kang | Medium","url":"https://medium.com/@danieldkang/swe-bench-verified-is-flawed-despite-expert-review-utboost-exposes-gaps-in-test-coverage-4b75c6b940c6"},{"title":"SWE-bench Lite","url":"https://www.swebench.com/lite.html"}]

Based on the web search results, here's what I found about SoRFT and its SWE-bench Lite and Verified results:

## SoRFT Overview

SoRFT significantly enhances issue-resolving performance, improves model generalization, and provides a cost-efficient alternative to commercial models. The work is by Zexiong Ma, Chao Peng, Pengfei Gao, Xiangxin Meng, Yanzhen Zou, Bing Xie and was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in 2025.

## Methodology

SoRFT consists of two training stages: (1) rejection-sampled supervised fine-tuning, where Chain of Thought (CoT) data is filtered using ground-truth before fine-tuning the LLM, and (2) rule-based reinforcement learning, which leverages PPO with ground-truth based rewards.

## Verified Results

The SoRFT-trained model achieves state-of-the-art (SOTA) performance among open-source models on both SWE-Bench Verified and SWE-Bench Lite, resolving 21.4% issues on SWE-Bench Verified with SoRFT-Qwen-7B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ac2edbc-6b51-4c3b-91b1-1913ef93c5a7",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "ad56e0f2ccf31b19b",
  "type": "user",
  "uuid": "7f45d1a1-6881-4931-be5d-b7167af80007",
  "sourceToolAssistantUUID": "0ac2edbc-6b51-4c3b-91b1-1913ef93c5a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T06:57:18.372Z_

<details><summary>↩ Tool result · `toolu_01B5TGa1U7oTA1m5DVTv3aXX`</summary>

```text
Web search results for query: "SpecRover ICSE 2025 ambiguous issue description error analysis"

Links: [{"title":"SpecRover: Code Intent Extraction via LLMs (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/68/SpecRover-Code-Intent-Extraction-via-LLMs"},{"title":"SpecRover: Code Intent Extraction via LLMs","url":"https://www.computer.org/csdl/proceedings-article/icse/2025/056900a617/251mFZysrIc"},{"title":"publications | Yuntong Zhang","url":"https://yuntongzhang.github.io/publications/"},{"title":"dblp: ICSE 2025","url":"https://dblp.org/db/conf/icse/icse2025.html"},{"title":"2025 IEEE/ACM 47th International Conference on Software ...","url":"https://www.computer.org/csdl/proceedings/icse/2025/215aVCUIQmY"},{"title":"[2408.02232] SpecRover: Code Intent Extraction via LLMs","url":"https://arxiv.org/abs/2408.02232"},{"title":"SpecRover: Code Intent Extraction via LLMs | Request PDF","url":"https://www.researchgate.net/publication/392958739_SpecRover_Code_Intent_Extraction_via_LLMs"},{"title":"Icse Specimen Paper 2025 English Literature | PDF","url":"https://www.scribd.com/document/733676869/ICSE-SPECIMEN-PAPER-2025-ENGLISH-LITERATURE"},{"title":"© 2025 IJRTI | Volume 10, Issue 1 January 2025 | ISSN: 2456-3315 IJRTI2501039","url":"https://www.ijrti.org/papers/IJRTI2501039.pdf"},{"title":"ICSE 2025 - Research Track - ICSE 2025","url":"https://conf.researchr.org/track/icse-2025/icse-2025-research-track"}]

Based on the search results, here's what I found about SpecRover at ICSE 2025:

## Overview of SpecRover

SpecRover addresses GitHub issues by conducting iterative code search accompanied by specification inference to infer intent from both project structure and behavior, with patches examined by a reviewer agent for vetting. The approach is built on the open-source LLM agent AutoCodeRover.

## Key Performance Results

In an evaluation on the full SWE-Bench consisting of 2294 GitHub issues, SpecRover shows more than 50% improvement in efficacy over AutoCodeRover. The approach demonstrates modest cost ($0.65 per issue) in resolving an average GitHub issue in SWE-Bench lite.

## Handling of Issue Descriptions

The production of explanation by SpecRover allows for a better "signal" to be given to the developer, on when the suggested patches can be accepted with confidence. This suggests the system addresses ambiguity in issue descriptions by providing clearer specifications and explanations about patch recommendations.

## Broader Significance

SpecRover seeks to demonstrate the continued importance of specification inference in automated program repair, even as program repair technologies enter the LLM era.

The search results provide general information about SpecRover's approach and results, but don't contain specific details about error analysis related to ambiguous issue descriptions. If you need more detailed information about that specific aspect, you may want to consult the full paper directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6e9c459-f15b-435e-b637-e2ffd955d74b",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "ad56e0f2ccf31b19b",
  "type": "user",
  "uuid": "71b82a3f-6295-4e18-9837-0c09054ee955",
  "sourceToolAssistantUUID": "d6e9c459-f15b-435e-b637-e2ffd955d74b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T06:57:19.236Z_

<details><summary>↩ Tool result · `toolu_017bauLnVoPFQnuej3j6eve2`</summary>

```text
Web search results for query: "site:arxiv.org SpecRover code intent extraction 2408.02232"

Links: [{"title":"[2408.02232] SpecRover: Code Intent Extraction via LLMs","url":"https://arxiv.org/abs/2408.02232"},{"title":"SpecRover: Code Intent Extraction via LLMs Haifeng Ruan* Yuntong Zhang*","url":"https://arxiv.org/pdf/2408.02232"},{"title":"SpecRover: Code Intent Extraction via LLMs *Joint first authors, ordered alphabetically.","url":"https://arxiv.org/html/2408.02232v3"},{"title":"Software Engineering Aug 2024","url":"https://www.arxiv.org/list/cs.SE/2024-08?skip=10&show=2000"},{"title":"Security Attacks on LLM-based Code Completion Tools","url":"https://arxiv.org/html/2408.11006"},{"title":"[2408.02674] On Feasibility of Intent Obfuscating Attacks","url":"https://arxiv.org/abs/2408.02674"},{"title":"Security Attacks on LLM-based Code Completion Tools Wen Cheng","url":"https://arxiv.org/pdf/2408.11006"},{"title":"[2408.03091] Modeling User Intent Beyond Trigger: Incorporating Uncertainty for Trigger-Induced Recommendation","url":"https://arxiv.org/abs/2408.03091"},{"title":"Computer Science Aug 2024","url":"https://arxiv.org/list/cs/2024-08?skip=2140&show=2000"},{"title":"[2408.09236v3] Hybrid Semantic Search: Unveiling User Intent Beyond Keywords","url":"https://arxiv.org/abs/2408.09236v3"}]

I found the paper! Here are the search results for SpecRover (arxiv paper 2408.02232):

**Paper Title:** SpecRover: Code Intent Extraction via LLMs by Haifeng Ruan, Yuntong Zhang, and Abhik Roychoudhury

**Overview:**
Autonomous program improvement typically involves automatically producing bug fixes and feature additions. Such program improvement can be accomplished by a combination of large language model (LLM) and program analysis capabilities, in the form of an LLM agent.

**Key Approach:**
The work examines efficient and low-cost workflows for iterative specification inference within an LLM agent. Given a GitHub issue to be resolved in a software project, the goal is to conduct iterative code search accompanied by specification inference - thereby inferring intent from both the project structure and behavior.

**Results:**
SpecRover (AutoCodeRover-v2) is built on the open-source LLM agent AutoCodeRover. In an evaluation on the full SWE-Bench consisting of 2294 GitHub issues, it shows more than 50% improvement in efficacy over AutoCodeRover. The work shows modest cost ($0.65 per issue) in resolving an average GitHub issue in SWE-Bench lite.

**Publication Status:**
The paper is to appear in ICSE 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2708a677-335a-4de7-9ebc-39144b2c8d0f",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "ad56e0f2ccf31b19b",
  "type": "user",
  "uuid": "7e69ebb4-5bc7-40d2-aaef-8605b949a171",
  "sourceToolAssistantUUID": "2708a677-335a-4de7-9ebc-39144b2c8d0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T06:57:20.626Z_

Now let me fetch the actual papers to get the precise numbers and error analysis you're asking about.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e69ebb4-5bc7-40d2-aaef-8605b949a171",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTE2UeyvC7VUDjqGSEF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3405b031-18c5-4c6b-9f53-794928c4e885",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019tfgt4gGjbAbC9VjLg8iqF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 932,
      "cache_creation_input_tokens": 3529,
      "cache_read_input_tokens": 16941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3529,
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

_source line 12 · 2026-05-10T06:57:21.513Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fg7MX9df16kWC8a33kZsgt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.20127",
  "prompt": "What are the exact performance numbers for SoRFT-7B on SWE-bench Lite and SWE-bench Verified? Report all percentage results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3405b031-18c5-4c6b-9f53-794928c4e885",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTE2UeyvC7VUDjqGSEF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff596587-defa-4698-b231-ab3e35222322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019tfgt4gGjbAbC9VjLg8iqF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 932,
      "cache_creation_input_tokens": 3529,
      "cache_read_input_tokens": 16941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3529,
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

_source line 13 · 2026-05-10T06:57:22.365Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019PFyJHQuJuXaxHFP1YyqFh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2408.02232",
  "prompt": "What does the error analysis say about failures due to ambiguous issue descriptions? Look for Section V-A or similar analysis sections with percentages or instance counts like 51.7% or 107/207."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff596587-defa-4698-b231-ab3e35222322",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTE2UeyvC7VUDjqGSEF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4eaf0f58-04a6-4523-b282-ed36744a7743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019tfgt4gGjbAbC9VjLg8iqF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 932,
      "cache_creation_input_tokens": 3529,
      "cache_read_input_tokens": 16941,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3529
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 932,
          "output_tokens": 246,
          "cache_read_input_tokens": 16941,
          "cache_creation_input_tokens": 3529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3529,
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

_source line 14 · 2026-05-10T06:57:25.346Z_

<details><summary>↩ Tool result · `toolu_019PFyJHQuJuXaxHFP1YyqFh`</summary>

```text
I cannot find the specific error analysis about failures due to ambiguous issue descriptions in the provided web page content. The page shows the abstract and metadata for the SpecRover paper, but does not include the full text of Section V-A or other analysis sections with specific percentages or instance counts.

To access that detailed error analysis, you would need to view the full PDF or HTML version of the paper using the links provided on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eaf0f58-04a6-4523-b282-ed36744a7743",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "ad56e0f2ccf31b19b",
  "type": "user",
  "uuid": "b51b8a32-5cdd-4d5a-bf72-212e8d82555d",
  "sourceToolAssistantUUID": "4eaf0f58-04a6-4523-b282-ed36744a7743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T06:57:27.021Z_

<details><summary>↩ Tool result · `toolu_01Fg7MX9df16kWC8a33kZsgt`</summary>

```text
# Performance Results for SoRFT-7B

Based on the provided content, only one specific performance metric is mentioned:

**SWE-Bench Verified:** "resolve 21.4% issues on SWE-Bench Verified with SoRFT-Qwen-7B"

Unfortunately, the abstract does not provide the exact percentage result for SoRFT-7B on SWE-Bench Lite. The document only indicates that the model was evaluated on both benchmarks and achieved state-of-the-art performance among open-source models, but the specific Lite benchmark score is not included in this excerpt.

To find the complete performance numbers, you would need to access the full paper PDF or HTML version linked in the article.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff596587-defa-4698-b231-ab3e35222322",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "ad56e0f2ccf31b19b",
  "type": "user",
  "uuid": "0979833a-7ec3-40dd-9e63-3d6ee9fed011",
  "sourceToolAssistantUUID": "ff596587-defa-4698-b231-ab3e35222322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T06:57:28.279Z_

Let me try accessing the HTML versions and PDFs directly for more complete information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0979833a-7ec3-40dd-9e63-3d6ee9fed011",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTEbjQMwubKcuPLtWCw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "87930aa7-bb63-4b4b-9145-187b980da47a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QkFLX6Ps69UnCUMHZNSfej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 125,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 20470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 17 · 2026-05-10T06:57:28.953Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MjMAz29mxdHUhyQSmRENZM`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.20127",
  "prompt": "Find all performance results for SoRFT models on SWE-bench Lite and SWE-bench Verified. Include exact percentages in tables or results sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87930aa7-bb63-4b4b-9145-187b980da47a",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTEbjQMwubKcuPLtWCw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dde37ef7-fe04-478e-acc1-5df068bfff15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QkFLX6Ps69UnCUMHZNSfej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 125,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 20470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1375,
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

_source line 18 · 2026-05-10T06:57:29.478Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018zytME31qD5NCXTy8MeekP`</summary>

```json
{
  "url": "https://arxiv.org/html/2408.02232v3",
  "prompt": "Find Section V-A or any error analysis section. What specific numbers or percentages are reported about failures due to ambiguous issue descriptions? Look for 51.7%, 107/207, or similar metrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dde37ef7-fe04-478e-acc1-5df068bfff15",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTEbjQMwubKcuPLtWCw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f9207a62-ca3c-49dd-a516-cc637594d66d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QkFLX6Ps69UnCUMHZNSfej",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 125,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 20470,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1375
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 125,
          "output_tokens": 246,
          "cache_read_input_tokens": 20470,
          "cache_creation_input_tokens": 1375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1375,
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

_source line 19 · 2026-05-10T06:57:32.490Z_

<details><summary>↩ Tool result · `toolu_01MjMAz29mxdHUhyQSmRENZM`</summary>

```text
# SoRFT Performance Results

## SWE-Bench Verified Results

| Model | %Resolved |
|-------|-----------|
| SoRFT-Qwen-7B | 21.4% |
| SoRFT-Qwen-32B | 30.8% |

## SWE-Bench Lite Results

| Model | %Resolved |
|-------|-----------|
| SoRFT-Qwen-7B | 14.0% |
| SoRFT-Qwen-32B | 24.0% |

## Key Performance Insights

The 7B model "outperforms SWE-Gym-Qwen-32B (21.4 vs. 20.6)" on Verified, while the 32B variant "outperforms Lingma-SWE-GPT-72B (30.8 vs. 30.2)" despite having fewer parameters.

Additionally, when trained with both supervised fine-tuning and reinforcement learning stages, SoRFT showed consistent improvements. On Verified, the 7B model improved from 18.0% (%Resolved with SFT alone) to 21.4%, while the 32B model advanced from 28.8% to 30.8%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dde37ef7-fe04-478e-acc1-5df068bfff15",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "ad56e0f2ccf31b19b",
  "type": "user",
  "uuid": "ac1d648b-8e7d-45bc-9013-2e27d4ff22ef",
  "sourceToolAssistantUUID": "dde37ef7-fe04-478e-acc1-5df068bfff15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T06:57:34.700Z_

<details><summary>↩ Tool result · `toolu_018zytME31qD5NCXTy8MeekP`</summary>

```text
I've reviewed Section V-A and the entire document carefully, searching for the specific metrics you mentioned (51.7%, 107/207, or similar failure analysis related to ambiguous issue descriptions).

**Finding:** These specific percentages do not appear in the document.

Section V-A ("RQ1: Overall Efficacy of Task Resolving") reports success metrics rather than failure analysis:
- SpecRover achieved "19.31% (443)" on full SWE-Bench
- "31.00% (93)" on SWE-Bench lite
- "50% improvement in efficacy over AutoCodeRover"

The document lacks a dedicated error analysis section that breaks down failures by root cause (such as ambiguous descriptions). While the paper discusses specification inference and patch validation extensively, it does not provide granular failure statistics categorized by ambiguity or other specific failure modes.

The closest relevant content discusses precision metrics in Table II, where "FN (false negative)" cases represent patches not accepted but actually correct, but these aren't tied to ambiguous descriptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9207a62-ca3c-49dd-a516-cc637594d66d",
  "isSidechain": true,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "agentId": "ad56e0f2ccf31b19b",
  "type": "user",
  "uuid": "3aad605b-f4da-4dd2-9464-84e1aa5c2859",
  "sourceToolAssistantUUID": "f9207a62-ca3c-49dd-a516-cc637594d66d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T06:57:40.357Z_

Perfect! I now have the key information. Let me report my findings:

## Verification Results

### SoRFT Paper (arXiv 2502.20127, ACL 2025)

**ANSWER TO YOUR FIRST QUESTION:** The 21.4% figure applies to **SWE-bench Verified**, not SWE-bench Lite.

**Exact Performance Numbers:**
- **SoRFT-Qwen-7B on SWE-bench Verified: 21.4%**
- **SoRFT-Qwen-7B on SWE-bench Lite: 14.0%**

For the larger model:
- SoRFT-Qwen-32B on SWE-bench Verified: 30.8%
- SoRFT-Qwen-32B on SWE-bench Lite: 24.0%

The paper notes that with RL training, the 7B model improved from 18.0% (SFT alone) to 21.4% on Verified.

### SpecRover Paper (arXiv 2408.02232, ICSE 2025)

**ANSWER TO YOUR SECOND QUESTION:** The specific numbers you mentioned (51.7% or 107/207) **do not appear** in the SpecRover paper.

**What the paper actually contains:**
The SpecRover paper reports overall success metrics (19.31% on full SWE-Bench, 31.00% on SWE-Bench Lite) and claims 50% improvement over AutoCodeRover. However, it **does not have a dedicated error analysis section** that breaks down failures by root cause, such as "ambiguous issue descriptions." While the paper discusses specification inference and patch validation, it does not provide granular failure statistics categorized by ambiguity or specific failure modes.

---

**For your adversarial review:** You should note that SoRFT's 21.4% result is on the more challenging SWE-bench Verified benchmark, not Lite. And the SpecRover paper appears not to contain the specific error analysis breakdown you're checking for—if those numbers exist, they may be in a different paper or appendix.

Sources:
- [SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv HTML)](https://arxiv.org/html/2502.20127)
- [SoRFT on arXiv](https://arxiv.org/abs/2502.20127)
- [SpecRover: Code Intent Extraction via LLMs (arXiv HTML)](https://arxiv.org/html/2408.02232v3)
- [SpecRover on arXiv](https://arxiv.org/abs/2408.02232)
- [SoRFT on ACL Anthology](https://aclanthology.org/2025.acl-long.559/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aad605b-f4da-4dd2-9464-84e1aa5c2859",
  "isSidechain": true,
  "agentId": "ad56e0f2ccf31b19b",
  "requestId": "req_011CatTFAZ76xyLfor4EhgoW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ae0353b9-4b7a-40f7-b265-be8872f7fa06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KKEc393qWnRWKBrGsxwg93",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 21845,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1067
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 696,
          "cache_read_input_tokens": 21845,
          "cache_creation_input_tokens": 1067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1067,
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
