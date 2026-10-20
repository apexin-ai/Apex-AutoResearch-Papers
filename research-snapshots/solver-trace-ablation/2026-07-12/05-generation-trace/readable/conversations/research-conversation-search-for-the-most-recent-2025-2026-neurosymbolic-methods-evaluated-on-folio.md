# Research conversation: Search for the most recent (2025-2026) neurosymbolic methods evaluated on FOLIO and ProofWriter to check if the proposal

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a68adc42956348749.jsonl`
- **Structured JSON:** [`f4aa101b93c06542f61c.json`](../../sessions/f4/f4aa101b93c06542f61c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-10T22:10:21.568Z_

Search for the most recent (2025-2026) neurosymbolic methods evaluated on FOLIO and ProofWriter to check if the proposal has missed any important competing work. Focus especially on:

1. Any papers from Feb-May 2026 that use counterexample-guided or solver-feedback approaches for NL reasoning
2. Any papers that evaluate abduction on ProofWriter specifically

Use WebSearch to:
1. Search for "FOLIO benchmark neurosymbolic 2026 state of the art"
2. Search for "neurosymbolic logical reasoning FOLIO ProofWriter 2026"
3. Search for "MAD-LOGIC ICLR 2026" to verify this paper exists
4. Search for "Adaptive LLM-Symbolic Reasoning EACL 2026" to verify this exists
5. Search for "NL2Logic AST-guided translation first-order logic 2026" to verify the NL2Logic paper

Report what you find, especially any papers the proposal may have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "11bcedf5-b1d0-4875-ab12-c8bf1593f607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T22:10:22.677Z_

I'll search for recent neurosymbolic methods evaluated on FOLIO and ProofWriter to help identify any competing work the proposal may have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11bcedf5-b1d0-4875-ab12-c8bf1593f607",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauerGRLYj9X7GQtipZww",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4176f76a-b881-4bcb-a43c-c750574b7689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VKMXu5RxucWNvhkMZ5Xf4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 661,
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

_source line 3 · 2026-05-10T22:10:22.881Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mt3S3GrbbZSPyHM8ae2rwF`</summary>

```json
{
  "query": "FOLIO benchmark neurosymbolic 2026 state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4176f76a-b881-4bcb-a43c-c750574b7689",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauerGRLYj9X7GQtipZww",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3397b6c1-29d3-4344-ae5d-b0a163461eeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VKMXu5RxucWNvhkMZ5Xf4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 661,
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

_source line 4 · 2026-05-10T22:10:22.894Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C2nRERKnHSuVdSMgz8ULQJ`</summary>

```json
{
  "query": "neurosymbolic logical reasoning FOLIO ProofWriter 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3397b6c1-29d3-4344-ae5d-b0a163461eeb",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauerGRLYj9X7GQtipZww",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "267a04e5-0993-43fb-98c8-3963bced179b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VKMXu5RxucWNvhkMZ5Xf4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 661,
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

_source line 5 · 2026-05-10T22:10:23.111Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GvUJhnnP6yUYtTd8AU8qFT`</summary>

```json
{
  "query": "MAD-LOGIC ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "267a04e5-0993-43fb-98c8-3963bced179b",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauerGRLYj9X7GQtipZww",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c985f72-8eb9-4377-8da7-0a5fe1a1ec77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VKMXu5RxucWNvhkMZ5Xf4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 661,
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

_source line 6 · 2026-05-10T22:10:23.480Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F6YFCbyMGqAZLHLnXpAKa1`</summary>

```json
{
  "query": "Adaptive LLM-Symbolic Reasoning EACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c985f72-8eb9-4377-8da7-0a5fe1a1ec77",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauerGRLYj9X7GQtipZww",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "afb378b3-8a08-4777-a3b1-3d282a15275c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VKMXu5RxucWNvhkMZ5Xf4G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 13789,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 661
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 298,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 661,
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

_source line 7 · 2026-05-10T22:10:23.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019txfdz8XHFkrRbuT11E8qD`</summary>

```json
{
  "query": "NL2Logic AST-guided translation first-order logic 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afb378b3-8a08-4777-a3b1-3d282a15275c",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauerGRLYj9X7GQtipZww",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d3304289-9e62-4c42-b7c9-4b7a6fb93e68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VKMXu5RxucWNvhkMZ5Xf4G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 13789,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 661
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 298,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 661,
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

_source line 8 · 2026-05-10T22:10:29.717Z_

<details><summary>↩ Tool result · `toolu_01Mt3S3GrbbZSPyHM8ae2rwF`</summary>

```text
Web search results for query: "FOLIO benchmark neurosymbolic 2026 state of the art"

Links: [{"title":"A Comprehensive Review of Neuro-symbolic AI for Robustness, Uncertainty Quantification, and Intervenability | Arabian Journal for Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13369-025-10887-3"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf"},{"title":"Call for Papers: Special Call for Neurosymbolic Benchmark Papers | Neurosymbolic Artificial Intelligence","url":"https://neurosymbolic-ai-journal.com/content/call-papers-special-call-neurosymbolic-benchmark-papers"},{"title":"Call for Papers: Special Issue on Explainable Neurosymbolic AI (X-NeSy) | Neurosymbolic Artificial Intelligence","url":"https://neurosymbolic-ai-journal.com/content/call-papers-special-issue-explainable-neurosymbolic-ai-x-nesy"},{"title":"Formal Languages and LLMs affect Neurosymbolic ...","url":"https://ceur-ws.org/Vol-4064/kgnesy-paper3.pdf"},{"title":"Neuro-Symbolic AI for Cybersecurity: State of the Art, Challenges, and Opportunities","url":"https://arxiv.org/html/2509.06921v2"},{"title":"[2602.16954v1] Neural Proposals, Symbolic Guarantees: Neuro-Symbolic Graph Generation with Hard Constraints","url":"https://arxiv.org/abs/2602.16954v1"},{"title":"Designing a neuro-symbolic dual-model architecture for explainable and resilient intrusion detection in IoT networks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-27076-9"},{"title":"Neuro-Symbolic Artificial Intelligence: A Task-Directed ...","url":"https://www.ijcai.org/proceedings/2025/1157.pdf"},{"title":"IOS Press Ebooks - Neuro-Symbolic Artificial Intelligence: The State of the Art","url":"https://ebooks.iospress.nl/volume/neuro-symbolic-artificial-intelligence-the-state-of-the-art"}]

Based on the search results, here's what I found about the FOLIO benchmark in the context of neurosymbolic AI research and state-of-the-art developments in 2026:

## FOLIO Benchmark Overview

FOLIO offers rich diversity in natural language expressions and more complex logic rules, but is limited in size due to the extensive human effort needed for creation. The process of creating FOLIO requires substantial human effort and is susceptible to syntactic typos and reasoning errors introduced during annotation.

## Recent Neurosymbolic Research Involving FOLIO

Recent neurosymbolic research has been using FOLIO to benchmark reasoning systems. In one study, 20 experiments were conducted on FOLIO (with some formal language approaches like Pyke and ASP unable to be measured). This research investigates how different formal languages and language models affect neurosymbolic reasoning performance on the benchmark.

## State-of-the-Art Developments

The neurosymbolic field more broadly has been advancing significantly. Novel neurosymbolic approaches, such as Logic-LM and LINC, report substantial improvements over pure LLM prompting. Additionally, neuro-symbolic AI is a hybrid paradigm that combines the learning capabilities of neural networks with the reasoning strengths of symbolic AI, offering enhanced interpretability, verifiability, and control for real-world deployment.

The field continues to be active in 2026, with recent calls for papers on neurosymbolic benchmarks and explainable neurosymbolic AI, indicating ongoing efforts to evaluate and advance these systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3397b6c1-29d3-4344-ae5d-b0a163461eeb",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "28a5e492-da17-4ea8-b024-368c37c11b0c",
  "sourceToolAssistantUUID": "3397b6c1-29d3-4344-ae5d-b0a163461eeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T22:10:30.091Z_

<details><summary>↩ Tool result · `toolu_01C2nRERKnHSuVdSMgz8ULQJ`</summary>

```text
Web search results for query: "neurosymbolic logical reasoning FOLIO ProofWriter 2026"

Links: [{"title":"Intermediate Languages Matter: Formal Choice Drives Neurosymbolic LLM Reasoning","url":"https://arxiv.org/html/2502.17216"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining","url":"https://openreview.net/pdf?id=h00GHjWDEp"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers | OpenReview","url":"https://openreview.net/forum?id=h00GHjWDEp"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning ...","url":"https://aclanthology.org/2023.emnlp-main.313.pdf"},{"title":"Intermediate Languages Matter: Formal Languages and LLMs affect Neurosymbolic Reasoning","url":"https://arxiv.org/html/2509.04083v1"},{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"[2310.15164] LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers","url":"https://arxiv.org/abs/2310.15164"},{"title":"Formal Languages and LLMs affect Neurosymbolic ...","url":"https://arxiv.org/pdf/2509.04083"},{"title":"LogicGraph : Benchmarking Multi-Path Logical Reasoning via Neuro-Symbolic Generation and Verification","url":"https://arxiv.org/html/2602.21044v1"},{"title":"RAG-Logic: Enhance Neuro-symbolic Approaches for Logical Reasoning with Retrieval-augmented Generation | OpenReview","url":"https://openreview.net/forum?id=FAUDgLi6RO"}]

Based on the search results, here's what I found about neurosymbolic logical reasoning with FOLIO and ProofWriter:

## Overview

Neurosymbolic approaches constrain the probabilistic nature to the translation step of a natural language-posed problem into a formal language, allowing the reasoning to remain deterministic.

## The Datasets

Three logical reasoning datasets—ProntoQA, ProofWriter, and FOLIO—are commonly used in this research area. FOLIO is a partly expert-written dataset where a random answer is correct with about 33% (OWA), with a test set of 204 samples. ProofWriter is a generated dataset with a reasoning depth of 5.

## Key Findings

The best results of FOL (First-Order Logic) beat the best ones of ASP and Pyke on both datasets for all LLMs. This indicates that the choice of formal language matters: first-order logic outperforms logic programming languages.

## Recent Advances (2026)

On ProofWriter, augmenting StarCoder+ with LINC outperforms GPT-3.5 and GPT-4 with Chain-of-Thought prompting by 38% and 10% respectively, and when used with GPT-4, LINC scores 26% higher than CoT on ProofWriter.

The research shows that combining language models with symbolic solvers through neurosymbolic approaches represents a promising direction for improving logical reasoning performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "267a04e5-0993-43fb-98c8-3963bced179b",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "e205d082-3550-4fce-8b66-5e4d7bf34130",
  "sourceToolAssistantUUID": "267a04e5-0993-43fb-98c8-3963bced179b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T22:10:30.587Z_

<details><summary>↩ Tool result · `toolu_01GvUJhnnP6yUYtTd8AU8qFT`</summary>

```text
Web search results for query: "MAD-LOGIC ICLR 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 MAD-LOGIC:","url":"https://openreview.net/pdf/9efc07a23e82c4f96fe3a0b53efc9cc078940f48.pdf"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"GitHub - HongduanTian/MAD-MM: [ICLR 2026] \"Multi-Agent Debate with Memory Masking\" · GitHub","url":"https://github.com/HongduanTian/MAD-MM"},{"title":"ICLR Poster Multi-Agent Debate with Memory Masking","url":"https://iclr.cc/virtual/2026/poster/10010659"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 Workshop","url":"https://sites.google.com/view/iclr-2026-llmreasoning"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"ICLR 2026 Scores Released: Reviewers Call It \"Crazy\", DeepMind Researchers Show Comeback from Desperate Situation","url":"https://eu.36kr.com/en/p/3551362253731718"}]

Based on the search results, here's what I found about MAD-LOGIC at ICLR 2026:

MAD-LOGIC: Multi-Agent Debate Enhances Symbolic Translation and Reasoning is a conference paper published at ICLR 2026, authored by Haocheng Yang, Fengxiang Cheng, Tianjun Yao, Mengyue Yang, Jiajun Chai, Xiaohan Wang, Guojun Yin, Wei Lin, Soummya Kar, Fenrong Liu, Haoxuan Li, and Yisen Wang from institutions including Peking University, NUS, Meituan, UvA, MBZUAI, University of Bristol, CMU, and Tsinghua University.

## Research Overview

Large language models (LLMs) struggle with complex logical reasoning. The authors propose a multi-agent debate framework to leverage the strengths of different symbolic languages and reasoning methods.

## Approach

The method translates a logical reasoning question into three distinct symbolic languages (LP, FOL, and SAT) in parallel, then leverages multi-agent debate to refine the final translations. Agents debate to refine their translations, ensuring translation accuracy for subsequent symbolic language-based solving with solvers such as Pyke, Prover9, and Z3. Agents based on results from symbolic language and natural language perform debates in multiple rounds to absorb the strengths of various methods, and a majority vote among agents is used to determine the final answer.

## Results

The method enhances logical question-answering performance while reducing computational cost.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c985f72-8eb9-4377-8da7-0a5fe1a1ec77",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "3a92db87-36fc-47a6-98cd-e1ac52263ee0",
  "sourceToolAssistantUUID": "4c985f72-8eb9-4377-8da7-0a5fe1a1ec77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T22:10:30.710Z_

<details><summary>↩ Tool result · `toolu_01F6YFCbyMGqAZLHLnXpAKa1`</summary>

```text
Web search results for query: "Adaptive LLM-Symbolic Reasoning EACL 2026"

Links: [{"title":"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.54/"},{"title":"Adaptive LLM-Symbolic Reasoning via Dynamic Logical ...","url":"https://aclanthology.org/2026.eacl-long.54.pdf"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"[2510.06774] Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition","url":"https://arxiv.org/abs/2510.06774"},{"title":"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition","url":"https://arxiv.org/html/2510.06774"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition","url":"https://www.arxiv.org/pdf/2510.06774"},{"title":"Leveraging LLM-GNN Integration for Open-World Question Answering over Knowledge Graphs for EACL 2026 - IBM Research","url":"https://research.ibm.com/publications/leveraging-llm-gnn-integration-for-open-world-question-answering-over-knowledge-graphs"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"New methods boost reasoning in small and large language models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/blog/new-methods-boost-reasoning-in-small-and-large-language-models/"}]

Based on my search results, I found detailed information about "Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition" presented at EACL 2026.

## Overview

The paper "Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition" by Lei Xu, Pierre Beckmann, Marco Valentino, and Andre Freitas was presented at the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026) in Rabat, Morocco.

## Problem and Approach

The work addresses the challenge that while neuro-symbolic NLP methods aim to leverage the complementary strengths of large language models and formal logical solvers, current approaches are mostly static in nature, with the integration of a target solver predetermined at design time.

To address this, the authors introduce an adaptive, multi-paradigm, neuro-symbolic inference framework that: (1) automatically identifies formal reasoning strategies from problems expressed in natural language; and (2) dynamically selects and applies specialized formal logical solvers via autoformalization interfaces.

## Key Results

Extensive experiments on individual and multi-paradigm reasoning tasks support the conclusion that LLMs are effective at predicting the necessary formal reasoning strategies with an accuracy above 90%.

This enables flexible integration with formal logical solvers, with the framework outperforming competing baselines by 17% and 6% compared to GPT-4o and DeepSeek-V3.1, respectively.

The code and data are available at https://github.com/idiap/adaptive_symbolic_reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afb378b3-8a08-4777-a3b1-3d282a15275c",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "e9480ada-497e-46f1-a9e4-645da5d0e860",
  "sourceToolAssistantUUID": "afb378b3-8a08-4777-a3b1-3d282a15275c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T22:10:30.984Z_

<details><summary>↩ Tool result · `toolu_019txfdz8XHFkrRbuT11E8qD`</summary>

```text
Web search results for query: "NL2Logic AST-guided translation first-order logic 2026"

Links: [{"title":"NL2LOGIC: AST-Guided Translation of Natural Language into","url":"https://www.arxiv.org/pdf/2602.13237"},{"title":"[2602.13237] NL2LOGIC: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models","url":"https://arxiv.org/abs/2602.13237"},{"title":"NL2LOGIC: AST-Guided Translation of Natural Language into ...","url":"https://people.cs.vt.edu/penggao/papers/nl2logic-eacl26findings.pdf"},{"title":"NL2Logic: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models","url":"https://arxiv.org/html/2602.13237"},{"title":"VT Security & Intelligence Lab · GitHub","url":"https://github.com/peng-gao-lab"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection | OpenReview","url":"https://openreview.net/forum?id=lBc3MXcGqZ"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic","url":"https://openreview.net/pdf?id=lBc3MXcGqZ"},{"title":"NL2LOGIC: AST-Guided Translation of Natural Language into ...","url":"https://ccsnow127.github.io/assets/pdf/nl2logic.pdf"},{"title":"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection","url":"https://arxiv.org/html/2405.02318v1/"}]

Based on the search results, I found relevant information about NL2Logic, a recent paper from 2026.

## NL2LOGIC Overview

NL2LOGIC is a first-order logic translation framework that introduces an abstract syntax tree as an intermediate representation, combining a recursive large language model based semantic parser with an abstract syntax tree guided generator that deterministically produces solver-ready logic code.

## Problem It Addresses

Automated reasoning is critical in domains such as law and governance, where verifying claims against facts in documents requires both accuracy and interpretability, and recent work adopts structured reasoning pipelines that translate natural language into first-order logic and delegate inference to automated solvers. However, existing methods suffer from fragile syntax control due to weak enforcement of global grammar constraints and low semantic faithfulness caused by insufficient clause-level semantic understanding.

## How It Works

The semantic parser decomposes each sentence into clauses and iteratively extracts first-order logic components (e.g., predicates, quantifiers, and logical connectives) to construct a First-Order Logic Abstract Syntax Tree (FOLAST), with parsing each clause iteratively enabling the model to make controlled, grammar-guided decisions. The AST-guided generator ensures syntactic correctness by deterministically compiling the FOLAST through a two-pass algorithm: the first pass registers all constants, variables, and relation signatures, while the second pass assembles scoped expressions following solver-specific grammar.

## Results

NL2Logic improves performance on natural language inference tasks by an average of 3 (the exact percentage appears to be cut off in the available text).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3304289-9e62-4c42-b7c9-4b7a6fb93e68",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "8bee7efc-a543-4e2c-aead-d815061bc1cd",
  "sourceToolAssistantUUID": "d3304289-9e62-4c42-b7c9-4b7a6fb93e68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T22:10:32.470Z_

Let me do additional targeted searches to find more specific papers on abduction, counterexample-guided approaches, and solver-feedback methods for these benchmarks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bee7efc-a543-4e2c-aead-d815061bc1cd",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauerxvQKfBJqu43pkjxy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f04a6165-9210-47ed-b151-a3a3aafa39f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D7S5Sc7J9oGcWE7NqRWkuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5640,
      "cache_read_input_tokens": 14450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5640,
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

_source line 14 · 2026-05-10T22:10:32.756Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CNUADNw21SMccb76xFcqUA`</summary>

```json
{
  "query": "abduction ProofWriter logical reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f04a6165-9210-47ed-b151-a3a3aafa39f0",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauerxvQKfBJqu43pkjxy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d1a4586f-f9cb-4b64-ab28-020845cbf376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D7S5Sc7J9oGcWE7NqRWkuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5640,
      "cache_read_input_tokens": 14450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5640,
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

_source line 15 · 2026-05-10T22:10:32.981Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GUqxnEdqq7y3EPu65EotRZ`</summary>

```json
{
  "query": "counterexample-guided natural language reasoning FOLIO 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1a4586f-f9cb-4b64-ab28-020845cbf376",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauerxvQKfBJqu43pkjxy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0a0ba4dc-03a7-42ae-8065-e96caa937d50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D7S5Sc7J9oGcWE7NqRWkuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5640,
      "cache_read_input_tokens": 14450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5640,
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

_source line 16 · 2026-05-10T22:10:33.156Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012vsj4j8Q4eEDoWhMGN2DY2`</summary>

```json
{
  "query": "solver feedback natural language logic translation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a0ba4dc-03a7-42ae-8065-e96caa937d50",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauerxvQKfBJqu43pkjxy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0ff68039-c67c-4e28-9b4b-9d607ef6f69a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D7S5Sc7J9oGcWE7NqRWkuY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5640,
      "cache_read_input_tokens": 14450,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 191,
          "cache_read_input_tokens": 14450,
          "cache_creation_input_tokens": 5640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5640,
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

_source line 17 · 2026-05-10T22:10:39.788Z_

<details><summary>↩ Tool result · `toolu_01GUqxnEdqq7y3EPu65EotRZ`</summary>

```text
Web search results for query: "counterexample-guided natural language reasoning FOLIO 2025 2026"

Links: [{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"[PDF] FOLIO: Natural Language Reasoning with First-Order Logic | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FOLIO:-Natural-Language-Reasoning-with-First-Order-Han-Schoelkopf/5581bf85386737bd3378eec68189759a05280bea"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"[2309.16436] Neuro Symbolic Reasoning for Planning: Counterexample Guided Inductive Synthesis using Large Language Models and Satisfiability Solving","url":"https://arxiv.org/abs/2309.16436"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://github.com/Yale-LILY/FOLIO"},{"title":"Harnessing the Power of Large Language Models for Natural Language to First-Order Logic Translation | OpenReview","url":"https://openreview.net/forum?id=QzQSR56JZr"},{"title":"Alignment Methods for Formal Logical Reasoning","url":"https://aclanthology.org/2025.mathnlp-main.8.pdf"},{"title":"SATBench: Benchmarking LLMs' Logical Reasoning via ...","url":"https://aclanthology.org/2025.emnlp-main.1716.pdf"}]

Based on the search results, I found information about FOLIO and related work on counterexample-guided reasoning with natural language:

## FOLIO: Natural Language Reasoning with First-Order Logic

FOLIO is a human-annotated, logically complex and diverse dataset for reasoning in natural language (NL), equipped with first-order logic (FOL) annotations, consisting of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

## Counterexample-Guided Approaches

The search results reveal relevant work on counterexample-guided methods for natural language reasoning. One approach uses satisfiability modulo theory (SMT) solvers as deductive reasoning engines to analyze generated solutions from LLMs, produce counterexamples when solutions are incorrect, and provide that feedback to the LLMs, with this interaction between inductive LLMs and deductive SMT solvers iteratively steering the LLM to generate the correct response.

## Recent Work (2025-2026)

The search results include recent papers from 2025. One 2025 paper on "Alignment Methods for Formal Logical Reasoning" references examples extracted from FOLIO. Additionally, a 2025 paper titled "SATBench" presents a benchmarking framework for evaluating LLMs' logical reasoning via automated methods, with a generation pipeline that samples CNF formulas followed by LLM-driven creation of story backgrounds and conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a0ba4dc-03a7-42ae-8065-e96caa937d50",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "6bbb0f36-8a85-496e-931e-b93787c5437b",
  "sourceToolAssistantUUID": "0a0ba4dc-03a7-42ae-8065-e96caa937d50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T22:10:40.002Z_

<details><summary>↩ Tool result · `toolu_01CNUADNw21SMccb76xFcqUA`</summary>

```text
Web search results for query: "abduction ProofWriter logical reasoning 2025 2026"

Links: [{"title":"Wiring the ‘Why’: A Unified Taxonomy and Survey of Abductive Reasoning in LLMs","url":"https://arxiv.org/html/2604.08016"},{"title":"Published as a conference paper at ICLR 2026 MAD-LOGIC:","url":"https://openreview.net/pdf/9efc07a23e82c4f96fe3a0b53efc9cc078940f48.pdf"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"Published in Transactions on Machine Learning Research (04/2025)","url":"https://openreview.net/pdf?id=d7W38UzUg0"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"Structured Abductive-Deductive-Inductive Reasoning for LLMs via Algebraic Invariants","url":"https://arxiv.org/html/2604.15727"},{"title":"(PDF) ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language","url":"https://www.academia.edu/97512358/ProofWriter_Generating_Implications_Proofs_and_Abductive_Statements_over_Natural_Language"},{"title":"grounded multi-perspective agent for llm logical reasoning","url":"https://arxiv.org/pdf/2509.24765"},{"title":"Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning","url":"https://arxiv.org/html/2603.17233v1"},{"title":"Aristotle: Mastering Logical Reasoning with A ...","url":"https://aclanthology.org/2025.acl-long.153.pdf"}]

Based on the search results, I found recent research on abduction and ProofWriter in the context of logical reasoning:

## Overview

ProofWriter is a representative example of datasets defined by explicit formal theory, rule bases, or constrained reasoning systems for abductive reasoning. ProofWriter is a synthetic dataset featuring natural language problems that assess and advance systematic neural logical deduction, supporting multi-hop inferences with varying proof depths under both Closed and Open World Assumption settings.

## Abduction in ProofWriter

ProofWriter supports abduction, which involves identifying minimal additional facts that would render an unprovable query entailed by the context. ProofWriter-style abduction is a structured reasoning setting where hypotheses are judged by whether they support a valid derivation under an explicit rule system.

## Recent Research and Challenges

Recent work continues to address limitations with ProofWriter. Prior work achieved only approximately 80% accuracy on ProofWriter. A multi-agent debate framework was proposed to address the limitations of existing single-agent logical reasoning methods by translating natural language logical questions into multiple symbolic languages like logic programming, first-order logic, and Boolean satisfiability, with agents debating to refine their translations for subsequent symbolic solver-based solving.

The Draft-and-Prune approach substantially strengthens auto-formalization-based reasoning on ProofWriter and other benchmarks without extra supervision.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1a4586f-f9cb-4b64-ab28-020845cbf376",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "5a0b1a11-65fb-4fd2-b0f7-817ba7701fc9",
  "sourceToolAssistantUUID": "d1a4586f-f9cb-4b64-ab28-020845cbf376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T22:10:40.980Z_

<details><summary>↩ Tool result · `toolu_012vsj4j8Q4eEDoWhMGN2DY2`</summary>

```text
Web search results for query: "solver feedback natural language logic translation 2026"

Links: [{"title":"ASP-Bench: From Natural Language to Logic ProgramsTo appear in the proceedings of the 2nd International Workshop on Neuro-Symbolic Software Engineering (NSE@ICSE 2026). Supported by the Austrian Science Fund (FWF) projects 10.55776/P36688 and 10.55776/COE12.","url":"https://arxiv.org/html/2602.01171v1"},{"title":"[2602.01171] ASP-Bench: From Natural Language to Logic Programs","url":"https://arxiv.org/abs/2602.01171"},{"title":"Natural Language to Formal Logic Translation","url":"https://www.emergentmind.com/topics/natural-language-to-formal-logic-translation"},{"title":"Are LLMs Stable Formal Logic Translators in Logical Reasoning Across Linguistically Diversified Texts?","url":"https://arxiv.org/html/2506.04575"},{"title":"[2305.15541] Harnessing the Power of Large Language Models for Natural Language to First-Order Logic Translation","url":"https://arxiv.org/abs/2305.15541"},{"title":"[2602.13237] NL2LOGIC: AST-Guided Translation of Natural Language into First-Order Logic with Large Language Models","url":"https://arxiv.org/abs/2602.13237"},{"title":"[2601.09446v1] Improving Symbolic Translation of Language Models for Logical Reasoning","url":"https://arxiv.org/abs/2601.09446v1"},{"title":"(PDF) Harnessing the Power of Large Language Models for Natural Language to First-Order Logic Translation","url":"https://www.researchgate.net/publication/371040473_Harnessing_the_Power_of_Large_Language_Models_for_Natural_Language_to_First-Order_Logic_Translation"},{"title":"A NEUROSYMBOLIC APPROACH TO NATURAL LANGUAGE FORMALIZATION AND VERIFICATION","url":"https://arxiv.org/pdf/2511.09008"},{"title":"Harnessing the Power of Large Language Models for Natural Language to First-Order Logic Translation | OpenReview","url":"https://openreview.net/forum?id=QzQSR56JZr"}]

I found several relevant results on this topic from 2026 research. Here's what the latest research shows:

## Key Findings on Solver Feedback and Natural Language Logic Translation

ASP-Bench is a benchmark for evaluating automated translation from natural language to Answer Set Programming, comprising 128 problem instances. The most significant advancement relates to using solver feedback in the translation process.

An autonomous LLM agent dynamically decides its actions based on solver feedback, using clingo error messages and failed test cases to iteratively repair and improve ASP programs across multiple reasoning-action cycles. This highlights the effectiveness of iterative refinement with solver feedback.

## Recent Approaches (2026)

NL2LOGIC introduces an abstract syntax tree as an intermediate representation, combining a recursive large language model based semantic parser with an abstract syntax tree guided generator that deterministically produces solver-ready logic code. NL2LOGIC achieves 99 percent syntactic accuracy and improves semantic correctness by up to 30 percent over state-of-the-art baselines.

Additionally, one mainstream approach translates natural language into formal logic and applies symbolic solvers for deduction, but LLM-based translators often fail to produce consistent symbolic representations when the same concept appears in different linguistic forms.

Incremental inference divides inference into two stages, predicate generation and FOL translation, providing greater control over model behavior and enhancing generation quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ff68039-c67c-4e28-9b4b-9d607ef6f69a",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "939dc312-a7ec-41f4-8961-ed6a186090a8",
  "sourceToolAssistantUUID": "0ff68039-c67c-4e28-9b4b-9d607ef6f69a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T22:10:42.087Z_

Let me search for a few more specific recent papers that might be relevant competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "939dc312-a7ec-41f4-8961-ed6a186090a8",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CaueshRXQhnnpLwBPxdqg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2c8d17da-cee9-499e-8145-bed8ef1f3727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0154pSna6s1mzDWtsGyvCvbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2885,
      "cache_read_input_tokens": 20090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2885,
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

_source line 21 · 2026-05-10T22:10:42.511Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E5BfkhetGPShMGbYf7SMHj`</summary>

```json
{
  "query": "\"Draft-and-Prune\" auto-formalization FOLIO ProofWriter 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c8d17da-cee9-499e-8145-bed8ef1f3727",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CaueshRXQhnnpLwBPxdqg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "661d2a87-022b-4c78-a112-ae35deda426e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0154pSna6s1mzDWtsGyvCvbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2885,
      "cache_read_input_tokens": 20090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2885,
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

_source line 22 · 2026-05-10T22:10:42.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013ngxefAQsJrQyKikUNfu7R`</summary>

```json
{
  "query": "\"Aristotle\" logical reasoning FOLIO ProofWriter 2025 ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "661d2a87-022b-4c78-a112-ae35deda426e",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CaueshRXQhnnpLwBPxdqg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "502908cb-b1a0-44e5-8ff4-4d9b9afc70a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0154pSna6s1mzDWtsGyvCvbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2885,
      "cache_read_input_tokens": 20090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2885,
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

_source line 23 · 2026-05-10T22:10:43.057Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018irEAjTMkPHVdBjimryPX9`</summary>

```json
{
  "query": "LINC ICLR 2025 first-order logic ProofWriter FOLIO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "502908cb-b1a0-44e5-8ff4-4d9b9afc70a7",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CaueshRXQhnnpLwBPxdqg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "28af7e1a-f46d-4a12-b4b6-1e77fe6abfef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0154pSna6s1mzDWtsGyvCvbm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2885,
      "cache_read_input_tokens": 20090,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2885
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 199,
          "cache_read_input_tokens": 20090,
          "cache_creation_input_tokens": 2885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2885,
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

_source line 24 · 2026-05-10T22:10:49.371Z_

<details><summary>↩ Tool result · `toolu_01E5BfkhetGPShMGbYf7SMHj`</summary>

```text
Web search results for query: ""Draft-and-Prune" auto-formalization FOLIO ProofWriter 2026"

Links: [{"title":"Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning","url":"https://arxiv.org/html/2603.17233v1"},{"title":"Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/draft-and-prune-improving-the-reliability-of-auto-formalization-for-logical-reasoning/"},{"title":"[2603.17233] Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning","url":"https://arxiv.org/abs/2603.17233"},{"title":"LTRAG: Enhancing Autoformalization and Self-refinement ...","url":"https://aclanthology.org/2025.findings-acl.126.pdf"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/html/2505.20047"},{"title":"Draft-and-Prune: Improving the Reliability of Auto-formalization for","url":"https://arxiv.org/pdf/2603.17233"},{"title":"Boosting Large Language Model Reasoning with Theorem Proving","url":"https://openreview.net/pdf?id=PPPyBgWeth"},{"title":"DRAFT, SKETCH, AND PROVE: GUIDING FORMAL ...","url":"https://wenda302.github.io/assets/pdf/draft_sketch_and_prove_guiding.pdf"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in ...","url":"https://arxiv.org/pdf/2505.20047"},{"title":"LeanReasoner: Boosting Complex Logical Reasoning with Lean","url":"https://arxiv.org/html/2403.13312"}]

Based on the search results, here's what I found about Draft-and-Prune auto-formalization:

## Draft-and-Prune Overview

Draft-and-Prune (D&P) is an inference-time framework that improves auto-formalization (AF)-based logical reasoning via diversity and verification. Auto-formalization translates natural-language reasoning problems into solver-executable programs, enabling symbolic solvers to perform sound logical deduction.

## How It Works

D&P first drafts multiple natural-language plans and conditions program generation on them, further pruning executable but contradictory or ambiguous formalizations, and aggregating predictions from surviving paths via majority voting.

## Performance on Benchmarks

Across four representative benchmarks (AR-LSAT, ProofWriter, PrOntoQA, LogicalDeduction), D&P substantially strengthens AF-based reasoning without extra supervision. More specifically, on AR-LSAT, in the AF-only setting, D&P achieves 78.43% accuracy with GPT-4 and 78.00% accuracy with GPT-4o, and D&P then attains near-ceiling performance on the other benchmarks, including 100% on PrOntoQA and LogicalDeduction.

## Research Timeline

The research paper was published on arXiv in March 2026 and is available through both the arXiv and Microsoft Research platforms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "661d2a87-022b-4c78-a112-ae35deda426e",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "3f9f32a5-1fa1-4a5f-81ea-896bc6910097",
  "sourceToolAssistantUUID": "661d2a87-022b-4c78-a112-ae35deda426e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T22:10:49.516Z_

<details><summary>↩ Tool result · `toolu_018irEAjTMkPHVdBjimryPX9`</summary>

```text
Web search results for query: "LINC ICLR 2025 first-order logic ProofWriter FOLIO"

Links: [{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://arxiv.org/pdf/2502.06563"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers | OpenReview","url":"https://openreview.net/forum?id=h00GHjWDEp"},{"title":"[2310.15164] LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers","url":"https://arxiv.org/abs/2310.15164"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning ...","url":"https://aclanthology.org/2023.emnlp-main.313.pdf"},{"title":"Paper page - LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers","url":"https://huggingface.co/papers/2310.15164"},{"title":"[PDF] LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LINC:-A-Neurosymbolic-Approach-for-Logical-by-with-Olausson-Gu/66d98dc2aad17c03532dbae21d05f098257cc2e2"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers - Paper Detail","url":"https://deeplearn.org/arxiv/423084/linc:-a-neurosymbolic-approach-for-logical-reasoning-by-combining-language-models-with-first-order-logic-provers"},{"title":"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.313/"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=3BoCwZFRJX"}]

Based on the search results, I can provide you with information about LINC and its relationship to these key components:

## LINC Overview

LINC (Logical Inference via Neurosymbolic Computation) is a neurosymbolic approach that investigates reformulating logical reasoning tasks as modular neurosymbolic programming.

## How LINC Works with First-Order Logic

In LINC, the LLM acts as a semantic parser, translating premises and conclusions from natural language to expressions in first-order logic. These expressions are then offloaded to an external theorem prover, which symbolically performs deductive inference.

## Performance on ProofWriter and FOLIO

LINC has shown notable results on these two important logical reasoning datasets:

- On ProofWriter, augmenting the comparatively small open-source StarCoder+ (15.5B parameters) with LINC even outperforms GPT-3.5 and GPT-4 with Chain-of-Thought (CoT) prompting by an absolute 38% and 10%, respectively

- When used with GPT-4, LINC scores 26% higher than CoT on ProofWriter while performing comparatively on FOLIO. Further analysis reveals that although both methods on average succeed roughly equally often on this dataset, they exhibit distinct and complementary failure modes.

The search results indicate that LINC was published at EMNLP 2023 and represents an important contribution to combining language models with symbolic reasoning through first-order logic, with the code being publicly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28af7e1a-f46d-4a12-b4b6-1e77fe6abfef",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "caf96883-4c3c-4669-848c-34f159cc4bfa",
  "sourceToolAssistantUUID": "28af7e1a-f46d-4a12-b4b6-1e77fe6abfef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T22:10:51.426Z_

<details><summary>↩ Tool result · `toolu_013ngxefAQsJrQyKikUNfu7R`</summary>

```text
Web search results for query: ""Aristotle" logical reasoning FOLIO ProofWriter 2025 ACL"

Links: [{"title":"Aristotle: Mastering Logical Reasoning with A ...","url":"https://aclanthology.org/2025.acl-long.153.pdf"},{"title":"GitHub - Aiden0526/Aristotle: Code and Data for ACL 2025 Paper \"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework\".","url":"https://github.com/Aiden0526/Aristotle"},{"title":"LogicPro: Improving Complex Logical Reasoning via ...","url":"https://aclanthology.org/2025.acl-long.1270.pdf"},{"title":"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework","url":"https://arxiv.org/html/2412.16953v2"},{"title":"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.153/"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://arxiv.org/pdf/2502.06563"},{"title":"From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning","url":"https://arxiv.org/html/2509.24765"},{"title":"Aristotle’s Logic (Stanford Encyclopedia of Philosophy)","url":"https://plato.stanford.edu/entries/aristotle-logic/"},{"title":"Logical Reasoning in Large Language Models: A Survey","url":"https://arxiv.org/pdf/2502.09100"},{"title":"grounded multi-perspective agent for llm logical reasoning","url":"https://arxiv.org/pdf/2509.24765"}]

Based on the web search results, here's what I found:

## Aristotle: A Logic-Complete Reasoning Framework

Aristotle is a logic-complete reasoning framework that consists of three key components: Logical Decomposer, Logical Search Router, and Logical Resolver, in which symbolic expressions and logical rules are comprehensively integrated into the entire reasoning process, significantly alleviating the bottlenecks of logical reasoning, i.e., reducing sub-task complexity, minimizing search errors, and resolving logical contradictions.

Experimental results demonstrate that Aristotle consistently outperforms state-of-the-art reasoning frameworks in both accuracy and efficiency, particularly excelling in complex logical reasoning scenarios.

### Performance on Benchmarks

The framework was evaluated on three logical reasoning datasets: ProntoQA, ProofWriter and LogicNLI. These datasets were chosen to reflect increasing levels of difficulty, with ProntoQA being the easiest, ProofWriter moderately complex, and LogicNLI the most challenging due to their intricate logical structures.

The approach achieves a 4.3% and 6.2% improvement over the second-best baseline on ProofWriter with GPT-4 and GPT-4o, respectively. On the most challenging dataset, LogicNLI, improvements of 6.3% for GPT-4 and 6.4% for GPT-4o are observed.

### Efficiency

Aristotle is designed to handle increased reasoning depth in an efficient and controlled manner. Each reasoning step in the framework consists of two operations. First, a search operation is performed using a deterministic rule-based method, which introduces minimal computational overhead and does not contribute additional token usage as reasoning depth increases. Second, a resolve operation is executed by the resolver module, which processes one reasoning step at a time and is the only component contributing to token-based computational cost.

This paper was published at the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "502908cb-b1a0-44e5-8ff4-4d9b9afc70a7",
  "isSidechain": true,
  "promptId": "808ad129-27e4-4631-b822-dfd91207786e",
  "agentId": "a68adc42956348749",
  "type": "user",
  "uuid": "d49d8c1c-616f-4c7f-9e2c-94a6f85674bf",
  "sourceToolAssistantUUID": "502908cb-b1a0-44e5-8ff4-4d9b9afc70a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T22:11:10.450Z_

## Summary of Recent Neurosymbolic Methods Evaluated on FOLIO and ProofWriter (2025-2026)

I've conducted comprehensive searches for competing work in the neurosymbolic logical reasoning space. Here's what I found:

### **Key Papers the Proposal Should Be Aware Of:**

#### **2026 Papers:**

1. **MAD-LOGIC (ICLR 2026)** - "Multi-Agent Debate Enhances Symbolic Translation and Reasoning"
   - Uses multi-agent debate framework to translate logical questions into three symbolic languages (LP, FOL, SAT) in parallel
   - Agents debate to refine translations before passing to solvers (Pyke, Prover9, Z3)
   - Uses solver feedback indirectly through debate mechanism
   - Evaluated on FOLIO and ProofWriter

2. **Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026)**
   - Dynamically selects formal reasoning strategies from natural language problems
   - Achieves >90% accuracy in predicting necessary formal reasoning strategies
   - Outperforms GPT-4o by 17% and DeepSeek-V3.1 by 6%
   - Multi-paradigm neuro-symbolic inference framework

3. **NL2LOGIC (EACL 2026 Findings)**
   - AST-guided translation using abstract syntax tree as intermediate representation
   - Combines recursive LLM semantic parser with AST-guided generator
   - Achieves 99% syntactic accuracy and 30% improvement in semantic correctness
   - Addresses syntax control and semantic faithfulness issues in NL-to-FOL translation

4. **ASP-Bench (NSE@ICSE 2026)**
   - Evaluates translation from natural language to Answer Set Programming
   - Features autonomous LLM agent that uses solver feedback (clingo error messages, failed test cases) to iteratively repair programs
   - Demonstrates effectiveness of iterative refinement with solver feedback

5. **Draft-and-Prune (arXiv March 2026)**
   - Inference-time framework for auto-formalization-based logical reasoning
   - Drafts multiple plans, generates programs, then prunes contradictory/ambiguous formalizations
   - Evaluated on AR-LSAT, ProofWriter, ProntoQA, and LogicalDeduction
   - Achieves near-ceiling on ProofWriter and other benchmarks

#### **2025 Papers:**

1. **Aristotle: Mastering Logical Reasoning (ACL 2025)**
   - Logic-complete decompose-search-resolve framework
   - Achieves 4.3-6.2% improvement over baselines on ProofWriter
   - Evaluated on ProofWriter, ProntoQA, and LogicNLI
   - Emphasizes logical decomposition and efficiency

2. **LINC (EMNLP 2023, widely cited 2025)**
   - Combines LLMs with first-order logic provers
   - StarCoder+ + LINC outperforms GPT-3.5/GPT-4 with CoT on ProofWriter by 38% and 10%
   - GPT-4 + LINC scores 26% higher than CoT on ProofWriter
   - Demonstrates complementary failure modes between neural and symbolic approaches

3. **"Wiring the 'Why': A Unified Taxonomy and Survey of Abductive Reasoning in LLMs" (2025)**
   - Comprehensive survey on abductive reasoning in LLMs
   - ProofWriter supports explicit abduction tasks
   - Recent work on structured abductive-deductive-inductive reasoning

4. **FoVer: First-Order Logic Verification (TACL 2025)**
   - First-order logic verification for natural language reasoning
   - Addresses verification of generated logical formulations

5. **"Grammars of Formal Uncertainty" (2025)**
   - Examines when to trust LLMs in automated reasoning tasks

### **Notable Patterns & Approaches to Consider:**

- **Counterexample-Guided Methods**: SMT solvers can produce counterexamples when LLM solutions are incorrect, feeding feedback back to LLMs iteratively
- **Solver Feedback Integration**: ASP-Bench and other recent work show effectiveness of using solver error messages and failed test cases for iterative refinement
- **Multi-Agent Debate**: MAD-LOGIC shows promise with agents debating across multiple symbolic language representations
- **AST/Grammar-Guided Generation**: Both NL2LOGIC and Draft-and-Prune use structured intermediate representations for better syntax control
- **Dynamic Solver Selection**: Adaptive LLM-Symbolic Reasoning automatically identifies the best reasoning strategy for each problem

### **Research Gaps the Proposal Might Address:**

- Most recent work focuses on **translation reliability** (syntax/semantics) but fewer explicitly study **iterative counterexample-guided refinement** at scale
- **Abduction** remains relatively underexplored compared to deduction - Wiring the 'Why' survey may indicate this is an emerging focus area
- **Solver feedback mechanisms** appear in newer work (ASP-Bench, Draft-and-Prune) but systematic evaluation of different feedback strategies is still limited
- **Cross-solver approaches** (like MAD-LOGIC's multi-language strategy) may represent a new direction

The proposals you're reviewing align well with active research directions, particularly if they emphasize solver feedback mechanisms or systematic abduction handling on ProofWriter.

Sources:
- [Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning](https://arxiv.org/html/2603.17233v1)
- [MAD-LOGIC at ICLR 2026](https://openreview.net/pdf/9efc07a23e82c4f96fe3a0b53efc9cc078940f48.pdf)
- [Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition](https://aclanthology.org/2026.eacl-long.54/)
- [NL2LOGIC: AST-Guided Translation of Natural Language into First-Order Logic](https://arxiv.org/abs/2602.13237)
- [Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework](https://aclanthology.org/2025.acl-long.153/)
- [LINC: A Neurosymbolic Approach for Logical Reasoning](https://aclanthology.org/2023.emnlp-main.313.pdf)
- [Wiring the 'Why': A Unified Taxonomy and Survey of Abductive Reasoning in LLMs](https://arxiv.org/html/2604.08016)
- [ASP-Bench: From Natural Language to Logic Programs](https://arxiv.org/abs/2602.01171)
- [FoVer: First-Order Logic Verification for Natural Language Reasoning](https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural)
- [Intermediate Languages Matter: Formal Choice Drives Neurosymbolic LLM Reasoning](https://arxiv.org/html/2502.17216)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d49d8c1c-616f-4c7f-9e2c-94a6f85674bf",
  "isSidechain": true,
  "agentId": "a68adc42956348749",
  "requestId": "req_011CauetUE44jLU8eGGPze9K",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "348f51b1-9ec0-4019-b571-e128cdd0edbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "539c541a-50bb-4c36-8db2-153433c29bbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H92M2tbEia7h1dd18J6rHH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1126,
      "cache_creation_input_tokens": 2043,
      "cache_read_input_tokens": 22975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2043,
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
