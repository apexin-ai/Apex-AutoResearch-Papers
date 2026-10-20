# Research conversation: Search the web for recent papers (2025-2026) on these topics to check for concurrent work: 1. "semantic mutation augment

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a705267f44e982e29.jsonl`
- **Structured JSON:** [`28e3fd9c74b585c35109.json`](../../sessions/28/28e3fd9c74b585c35109.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-10T05:14:34.952Z_

Search the web for recent papers (2025-2026) on these topics to check for concurrent work:
1. "semantic mutation augmentation fault localization" 2026
2. "contrastive learning fault localization robustness LLM" 2026
3. "semantics-preserving mutation code robustness training" 2026
4. arXiv submissions in the last 3 months on LLM fault localization robustness

Also search for:
- "best open source LLM code 2026" to find current SOTA code models
- "SOTA code LLM benchmark 2026"

Return all relevant paper titles, venues, dates, and any GitHub repos found. Be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fd027e93-49f6-4bed-af5b-d09550947dd0",
  "agentId": "a705267f44e982e29",
  "type": "user",
  "uuid": "5370a447-d9e4-4789-94b7-36e973b5b670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T05:14:36.203Z_

I'll conduct a comprehensive search for recent papers and resources on these topics. Let me search systematically across all the areas you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5370a447-d9e4-4789-94b7-36e973b5b670",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKPdaMNqX6n8cFsfkfr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f136a218-5105-43f1-a188-6bca4a8ee625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013F1PoJ9pfmaWEfjYf8FGfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16739,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16739,
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

_source line 3 · 2026-05-10T05:14:36.422Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BfXKyg1rSFP1HexmZ2x7Gs`</summary>

```json
{
  "query": "semantic mutation augmentation fault localization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f136a218-5105-43f1-a188-6bca4a8ee625",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKPdaMNqX6n8cFsfkfr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "865a25e1-b66a-4f12-95f4-f45e9cc1535e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013F1PoJ9pfmaWEfjYf8FGfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16739,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16739,
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

_source line 4 · 2026-05-10T05:14:36.637Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GYTyaasxwLYSHv1Vq2exRS`</summary>

```json
{
  "query": "contrastive learning fault localization robustness LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "865a25e1-b66a-4f12-95f4-f45e9cc1535e",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKPdaMNqX6n8cFsfkfr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a35fe97c-673e-4783-a985-91daea506fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013F1PoJ9pfmaWEfjYf8FGfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16739,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16739,
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

_source line 5 · 2026-05-10T05:14:36.868Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ltg2Ytew8qdXaokW2Sjcox`</summary>

```json
{
  "query": "semantics-preserving mutation code robustness training 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a35fe97c-673e-4783-a985-91daea506fd5",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKPdaMNqX6n8cFsfkfr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "52c58cac-5402-4432-9fab-425ca74b24b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013F1PoJ9pfmaWEfjYf8FGfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16739,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16739,
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

_source line 6 · 2026-05-10T05:14:37.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WPTFATa8Q8TfSVasp96kMS`</summary>

```json
{
  "query": "arXiv LLM fault localization robustness last 3 months 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52c58cac-5402-4432-9fab-425ca74b24b2",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKPdaMNqX6n8cFsfkfr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "336de3f6-f104-420f-bb11-0e1bca0dd17a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013F1PoJ9pfmaWEfjYf8FGfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16739,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16739,
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

_source line 7 · 2026-05-10T05:14:37.038Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PvNxKFuCv7vVRWFCrK1D82`</summary>

```json
{
  "query": "best open source LLM code models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "336de3f6-f104-420f-bb11-0e1bca0dd17a",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKPdaMNqX6n8cFsfkfr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "09133020-c99c-440f-af44-e14bdce08d42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013F1PoJ9pfmaWEfjYf8FGfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16739,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16739,
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

_source line 8 · 2026-05-10T05:14:37.190Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ETvzSWdA4BbdgNkecJ7Et9`</summary>

```json
{
  "query": "SOTA code LLM benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09133020-c99c-440f-af44-e14bdce08d42",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKPdaMNqX6n8cFsfkfr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a475eb7f-85fe-44e2-9120-f754fa3eac35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013F1PoJ9pfmaWEfjYf8FGfg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16739,
      "cache_read_input_tokens": 0,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16739
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 330,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16739,
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

_source line 9 · 2026-05-10T05:14:43.600Z_

<details><summary>↩ Tool result · `toolu_01WPTFATa8Q8TfSVasp96kMS`</summary>

```text
Web search results for query: "arXiv LLM fault localization robustness last 3 months 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372v3"},{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"Order Matters! An Empirical Study on Large Language Models’ Input Order Bias in Software Fault Localization","url":"https://arxiv.org/html/2412.18750"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/html/2403.16362v1"},{"title":"[2504.04372v3] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372v3"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"},{"title":"[2604.07362] LLM-Generated Fault Scenarios for Evaluating Perception-Driven Lane Following in Autonomous Edge Systems","url":"https://arxiv.org/abs/2604.07362"},{"title":"Improving LLM-Based Fault Localization with External Memory and Project Context","url":"https://arxiv.org/html/2506.03585v1"},{"title":"[2504.04372] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372"}]

Based on my search for recent arXiv papers on LLM fault localization robustness from the last 3 months of 2026, here are the key findings:

## Recent Research on LLM Fault Localization Robustness

**Most Recent and Relevant Study:**

A large-scale empirical investigation of LLMs' ability to reason about code for fault localization was conducted using an automated evaluation framework that dynamically generates controlled, previously unseen fault localization tasks to evaluate both accuracy and robustness of LLMs' code reasoning for fault localization. The study evaluated 10 state-of-the-art LLMs on 1300 Java and Python programs.

**Key Finding on Robustness:**

Semantic-preserving mutations (SPMs) cause an LLM to fail to localize the same fault it correctly localized earlier in 78% of cases, and LLMs' reasoning on the code found earlier in the context is noticeably better. These results suggest that LLMs' code-reasoning is tied to code features irrelevant to semantics.

**Other Recent Work (April 2026):**

A large-scale empirical study on 500 SWE-bench Verified instances was conducted using GPT-5-mini, evaluating 61 configurations that vary file-level, element-level, and line-level context. The results show that more context does not consistently improve repair performance, with file-level localization being the dominant factor, yielding a 15-17x improvement over a no-file baseline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "336de3f6-f104-420f-bb11-0e1bca0dd17a",
  "isSidechain": true,
  "promptId": "fd027e93-49f6-4bed-af5b-d09550947dd0",
  "agentId": "a705267f44e982e29",
  "type": "user",
  "uuid": "5361661d-a0c8-4524-9f11-1a1268ba7ae6",
  "sourceToolAssistantUUID": "336de3f6-f104-420f-bb11-0e1bca0dd17a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T05:14:43.939Z_

<details><summary>↩ Tool result · `toolu_01BfXKyg1rSFP1HexmZ2x7Gs`</summary>

```text
Web search results for query: "semantic mutation augmentation fault localization 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Mutation-oriented test data augmentation for GUI software fault localization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mutation-oriented-test-data-augmentation-for-GUI-Yu-Bai/8701a7308c7c4010f33f7e05d060c95663573517"},{"title":"A universal dimensionality optimization method for fault localization | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09738-z"},{"title":"FLIMs: Fault Localization Interference Mutants, Definition, ...","url":"https://arxiv.org/pdf/2511.23302"},{"title":"Context-aware Data Augmentation for Hardware Code Fault localization | ACM Transactions on Design Automation of Electronic Systems","url":"https://dl.acm.org/doi/10.1145/3725889"},{"title":"FLIMs: Fault Localization Interference Mutants, Definition, Recognition and Mitigation","url":"https://arxiv.org/html/2511.23302"},{"title":"GMBFL: Optimizing Mutation-Based Fault Localization via Graph Representation | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10336305/"},{"title":"CG-FL: A data augmentation approach using context-aware genetic algorithm for fault localization","url":"https://www.researchgate.net/publication/388493364_CG-FL_A_data_augmentation_approach_using_context-aware_genetic_algorithm_for_fault_localization"},{"title":"Boosting mutation-based fault localization by effectively generating Higher-Order Mutants - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950584924002659"},{"title":"Fault Localization via Fine-tuning Large Language Models with Mutation Generated Stack Traces","url":"https://arxiv.org/html/2501.18005v1"}]

Based on the search results, here's what I found regarding semantic mutation augmentation and fault localization research in 2026:

## Key 2026 Research Findings

A large-scale empirical investigation into the robustness of LLMs' fault localizability presents an end-to-end evaluation framework inspired by mutation testing that addresses limitations in current LLM evaluation including data contamination, scalability, automation, and extensibility.

For programs where LLMs successfully localize faults, semantic-preserving mutations (SPMs) are applied and rerun to assess the LLM's robustness and whether the LLM's reasoning relies on syntactic cues rather than semantics. Semantic-preserving mutations include identifier renaming, comment insertion or modification, formatting changes, and dead-code insertion.

### Key Findings on LLM Robustness

Semantic-preserving mutations cause an LLM to fail to localize the same fault it correctly localized earlier in 78% of cases. These results suggest that LLMs' code-reasoning is tied to code features irrelevant to semantics.

### Research Scale

From seed programs, researchers inject 4 fault types and apply 6 semantic-preserving mutations, generating 750,013 unique faulty programs spanning 245 million lines of code and approximately 3.8 billion tokens.

The research demonstrates significant challenges in using mutation-based techniques for evaluating LLM fault localization capabilities, revealing that LLMs rely heavily on superficial code features rather than true semantic understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "865a25e1-b66a-4f12-95f4-f45e9cc1535e",
  "isSidechain": true,
  "promptId": "fd027e93-49f6-4bed-af5b-d09550947dd0",
  "agentId": "a705267f44e982e29",
  "type": "user",
  "uuid": "5126f2e3-638a-49f9-8031-bc358baa3342",
  "sourceToolAssistantUUID": "865a25e1-b66a-4f12-95f4-f45e9cc1535e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T05:14:44.606Z_

<details><summary>↩ Tool result · `toolu_01GYTyaasxwLYSHv1Vq2exRS`</summary>

```text
Web search results for query: "contrastive learning fault localization robustness LLM 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Multi-view adaptive contrastive learning for information retrieval based fault localization | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00573-x"},{"title":"GitHub - CHAOZHAO-1/LLM-based-PHM: This is a reposotory that includes paper about LLM-based fault diagnosis and prognosis. (基于大模型的故障诊断和预测，持续更新)","url":"https://github.com/CHAOZHAO-1/LLM-based-PHM"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Improving Large Language Model Safety with Contrastive Representation Learning","url":"https://arxiv.org/html/2506.11938v1"},{"title":"Towards LLM-Based Failure Localization in Production-Scale Networks | Proceedings of the ACM SIGCOMM 2025 Conference","url":"https://dl.acm.org/doi/10.1145/3718958.3750505"},{"title":"[2506.11938] Improving Large Language Model Safety with Contrastive Representation Learning","url":"https://arxiv.org/abs/2506.11938"},{"title":"[2503.06648] Enhancing NLP Robustness and Generalization through LLM-Generated Contrast Sets: A Scalable Framework for Systematic Evaluation and Adversarial Training","url":"https://arxiv.org/abs/2503.06648"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/html/2403.16362v1"},{"title":"Downloads 2024","url":"https://icml.cc/Downloads/2024"}]

Based on the web search results, I found several relevant research works related to your query on contrastive learning, fault localization, robustness, and LLMs in 2026:

## Key Findings

**Fault Localization Robustness in LLMs:**
The first large-scale empirical investigation into the robustness of LLMs' fault localizability was accepted at ICST 2026. This study applies semantic-preserving mutations and finds that LLMs fail to localize the same fault they correctly localized earlier in 78% of cases, suggesting LLMs' code-reasoning is tied to code features irrelevant to semantics.

**Contrastive Learning for Fault Localization:**
A novel approach named Multi-View Adaptive Contrastive Learning for Information Retrieval Fault Localization (MACL-IRFL) was proposed to learn relationships for software fault localization. This model can improve over the best baseline up to 28.93%, 25.57% and 20.35% on Accuracy@1, MAP and MRR, respectively.

**LLM Safety via Contrastive Learning:**
A defense framework was proposed that formulates model defense as a contrastive representation learning problem using a triplet-based loss combined with adversarial hard negative mining to encourage separation between benign and harmful representations. This approach outperforms prior representation engineering-based defenses, improving robustness against both input-level and embedding-space attacks without compromising standard performance.

These research directions collectively address the intersection of contrastive learning techniques, fault localization challenges, and the robustness considerations essential for deploying LLMs in critical software engineering tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a35fe97c-673e-4783-a985-91daea506fd5",
  "isSidechain": true,
  "promptId": "fd027e93-49f6-4bed-af5b-d09550947dd0",
  "agentId": "a705267f44e982e29",
  "type": "user",
  "uuid": "5a137774-8fa3-431d-b957-51b113f53e7f",
  "sourceToolAssistantUUID": "a35fe97c-673e-4783-a985-91daea506fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T05:14:44.702Z_

<details><summary>↩ Tool result · `toolu_01ETvzSWdA4BbdgNkecJ7Et9`</summary>

```text
Web search results for query: "SOTA code LLM benchmark 2026"

Links: [{"title":"Code Generation Benchmarks 2026: SOTA LLMs for Programming | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"},{"title":"Best LLM for Coding in 2026: Ranked by Real Benchmarks | WhatLLM.org","url":"https://whatllm.org/best-llm-for-coding"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"},{"title":"How To Evaluate State‑Of‑The‑Art LLM Models: A Complete Guide | Deepchecks","url":"https://www.deepchecks.com/evaluate-state-of-the-art-llm-models/"},{"title":"Speed up inference with SOTA quantization techniques in TRT-LLM — TensorRT LLM","url":"https://nvidia.github.io/TensorRT-LLM/blogs/quantization-in-TRT-LLM.html"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Welcome llm-d to the CNCF: Evolving Kubernetes into SOTA AI infrastructure | CNCF","url":"https://www.cncf.io/blog/2026/03/24/welcome-llm-d-to-the-cncf-evolving-kubernetes-into-sota-ai-infrastructure/"}]

Based on the search results, here's what the current state-of-the-art for code LLM benchmarks looks like in 2026:

## Key Code Benchmarks

Code benchmarks come in three sizes: the smallest—HumanEval—asks the model to write a single function from a docstring; the middle tier—LiveCodeBench—uses fresh competitive-programming problems posted after the model's training cutoff; and the largest—SWE-bench Verified—hands the model a real GitHub issue and a real repository.

## Leading Models

As of 2026, GPT-5.5 (xhigh) leads coding benchmarks, while for open source alternatives, GLM-4.7 Thinking and DeepSeek V3.2 offer comparable performance at a fraction of the cost.

Claude Opus 4.7 shipped on 2026-04-16 and leads SWE-bench Verified at 87.6% under the Claude Code harness.

## Major Resources

Codesota is a callable registry with 17 research areas and 1,008 results that connects papers, code, datasets, models, and benchmark results in one public registry, accessible via an /api/sota endpoint. The Codesota frontier leaderboard tracks 8 benchmarks across 69 models, updated as of April 23, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a475eb7f-85fe-44e2-9120-f754fa3eac35",
  "isSidechain": true,
  "promptId": "fd027e93-49f6-4bed-af5b-d09550947dd0",
  "agentId": "a705267f44e982e29",
  "type": "user",
  "uuid": "57112474-74a0-4d32-b900-5f43202f495c",
  "sourceToolAssistantUUID": "a475eb7f-85fe-44e2-9120-f754fa3eac35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T05:14:44.865Z_

<details><summary>↩ Tool result · `toolu_01Ltg2Ytew8qdXaokW2Sjcox`</summary>

```text
Web search results for query: "semantics-preserving mutation code robustness training 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Semantic-Preserving Transformations as Mutation Operators","url":"https://arxiv.org/pdf/2503.23448"},{"title":"Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection","url":"https://arxiv.org/html/2503.23448"},{"title":"[2503.23448] Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection","url":"https://arxiv.org/abs/2503.23448"},{"title":"[2505.10443] Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?","url":"https://arxiv.org/abs/2505.10443"},{"title":"(PDF) Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection","url":"https://www.researchgate.net/publication/390353442_Semantic-Preserving_Transformations_as_Mutation_Operators_A_Study_on_Their_Effectiveness_in_Defect_Detection"},{"title":"Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?","url":"https://arxiv.org/html/2505.10443v1"},{"title":"How Accurately Do Large Language Models Understand Code?","url":"https://tahakhan.net/files/haroon_arxiv_25.pdf"},{"title":"Mutation Testing with Mutmut: Python for Code Reliability 2026","url":"https://johal.in/mutation-testing-with-mutmut-python-for-code-reliability-2026/"},{"title":"Exploiting Code Symmetries for Learning Program Semantics","url":"https://s2lab.cs.ucl.ac.uk/downloads/icml24-SymC.pdf"}]

Based on the search results, I found several relevant papers and projects from 2026 and recent times related to semantics-preserving mutations and code robustness:

## Key Findings:

### 1. **Fault Localizability of LLMs (ICST 2026)**

A large-scale empirical investigation into the robustness of LLMs' fault localizability has been accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026), using an evaluation framework inspired by mutation testing. The study applies semantic-preserving mutations (SPMs) to assess the LLM's robustness and whether the LLM's reasoning relies on syntactic cues rather than semantics. SPMs include identifier renaming, comment insertion or modification, formatting changes, and dead-code insertion.

### 2. **Semantic-Preserving Transformations as Mutation Operators**

A study found 28 publications with 94 different transformations, but when implementing 39 transformations from four publications, a manual check revealed that 23 out of 39 transformations change code semantics. Semantic-preserving transformations can be used to extend the training dataset and improve a model's robustness.

### 3. **LLM Robustness Against Mutations (May 2025)**

LLMs trained for code produce correct predictions based on flawed reasoning between 10% and 50% of cases, and often change predictions in response to code mutations, indicating they do not yet exhibit stable, semantically grounded reasoning.

### 4. **Code Symmetries for Learning Program Semantics**

SYMC outperforms pre-trained baselines by 11.4% on average in defect prediction, demonstrating improved robustness through symmetry-based training approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52c58cac-5402-4432-9fab-425ca74b24b2",
  "isSidechain": true,
  "promptId": "fd027e93-49f6-4bed-af5b-d09550947dd0",
  "agentId": "a705267f44e982e29",
  "type": "user",
  "uuid": "70596c46-3be5-43c7-b75a-50e6870bb13d",
  "sourceToolAssistantUUID": "52c58cac-5402-4432-9fab-425ca74b24b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T05:14:46.020Z_

<details><summary>↩ Tool result · `toolu_01PvNxKFuCv7vVRWFCrK1D82`</summary>

```text
Web search results for query: "best open source LLM code models 2026"

Links: [{"title":"Best Open Source LLM Leaderboard 2026 | Open Source Model Rankings and Tier List | Onyx AI","url":"https://onyx.app/open-llm-leaderboard"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"The Best Open-Source LLMs for Agentic Coding in 2026 | MindStudio","url":"https://www.mindstudio.ai/blog/best-open-source-llms-agentic-coding-2026"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"Best LLM for Coding in 2026: Ranked by Real Benchmarks | WhatLLM.org","url":"https://whatllm.org/best-llm-for-coding"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"The Best Open Source LLMs for Coding in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-coding"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"}]

Based on the search results, here are the best open source LLM code models in 2026:

## Top Models for Coding

**For Overall Coding Excellence:**

Kimi K2.6 is the strongest coding-oriented open source model, while Qwen 3.6 Plus is the strongest overall performer for demanding agentic coding tasks with the longest context window in the class (1M tokens), reliable tool use, and benchmark scores that put it close to closed-source frontier models.

GLM-4.7 Thinking is the top open-weight coding model in 2026, free to self-host.

**For Software Engineering Tasks:**

MiniMax-M2.7 is designed for agentic workflows and performs competitively across the full software engineering benchmark suite against proprietary models like Claude Opus 4.6, going beyond code generation to correlate monitoring metrics and conduct trace analysis.

**Best Value API Option:**

DeepSeek V3.2 is the best value via API at $0.35/M tokens — matching proprietary models at 1/10th the cost.

**High-Performance Models:**

Kimi-Dev-72B achieves 60.4% on SWE-bench Verified, setting a state-of-the-art result among open-source models, optimized through large-scale reinforcement learning to autonomously patch real codebases.

DeepSeek V4, Kimi K2.6, Qwen 3.6 Plus, GLM 5.1, and others have closed the gap on closed-source frontier models in ways that matter for actual work: multi-step task completion, tool call accuracy, and recoverable failure modes.

**For Local/Consumer Hardware:**

Qwen 2.5 Coder 32B or Devstral Small 2 can handle the vast majority of code completion, generation, debugging, and refactoring tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09133020-c99c-440f-af44-e14bdce08d42",
  "isSidechain": true,
  "promptId": "fd027e93-49f6-4bed-af5b-d09550947dd0",
  "agentId": "a705267f44e982e29",
  "type": "user",
  "uuid": "d25bcd37-2a2b-455c-9a5f-ef863d1d6bff",
  "sourceToolAssistantUUID": "09133020-c99c-440f-af44-e14bdce08d42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T05:14:47.350Z_

Now let me do some additional targeted searches to ensure comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d25bcd37-2a2b-455c-9a5f-ef863d1d6bff",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKQTEXPQ48H2vRA2m8e",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "affd4b06-80b9-4687-9335-010fde46e310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NUQB4fK5xaaRLgmURU1Eoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 16739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6039,
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

_source line 16 · 2026-05-10T05:14:47.565Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WyMQmZkX2UPxgoN1R8PeCt`</summary>

```json
{
  "query": "arXiv fault localization LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "affd4b06-80b9-4687-9335-010fde46e310",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKQTEXPQ48H2vRA2m8e",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4006b1d0-4374-45d7-a57f-97f99ac80799",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NUQB4fK5xaaRLgmURU1Eoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 16739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6039,
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

_source line 17 · 2026-05-10T05:14:48.128Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016AhKC3MaviMXjvMiC9uTwV`</summary>

```json
{
  "query": "\"mutation testing\" \"code understanding\" LLM robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4006b1d0-4374-45d7-a57f-97f99ac80799",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKQTEXPQ48H2vRA2m8e",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "494a20c3-b17f-4e00-bb77-72c42481617c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NUQB4fK5xaaRLgmURU1Eoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 16739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6039,
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

_source line 18 · 2026-05-10T05:14:48.277Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015CjCCeMZ1CVihFzVYdwCPH`</summary>

```json
{
  "query": "DeepSeek Qwen CodeLLaMA code models GitHub 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "494a20c3-b17f-4e00-bb77-72c42481617c",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKQTEXPQ48H2vRA2m8e",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9da381c-55f9-45a9-8577-2b9f3548a7e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NUQB4fK5xaaRLgmURU1Eoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 16739,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 906,
          "output_tokens": 183,
          "cache_read_input_tokens": 16739,
          "cache_creation_input_tokens": 6039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6039,
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

_source line 19 · 2026-05-10T05:14:55.347Z_

<details><summary>↩ Tool result · `toolu_01WyMQmZkX2UPxgoN1R8PeCt`</summary>

```text
Web search results for query: "arXiv fault localization LLM 2025 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/html/2403.16362v1"},{"title":"[2403.16362] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/abs/2403.16362"},{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"[2504.04372] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372"},{"title":"[2504.04372v3] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372v3"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481"},{"title":"[2506.03585] Improving LLM-Based Fault Localization with External Memory and Project Context","url":"https://arxiv.org/abs/2506.03585"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"},{"title":"Explainable Fault Localization for Programming Assignments via LLM-Guided Annotation","url":"https://arxiv.org/html/2509.25676v1"}]

Based on the search results, here are several recent arXiv papers on fault localization with LLMs from 2025-2026:

## Key Recent Papers

**1. Assessing the Impact of Code Changes on Fault Localizability of LLMs (2025-2026)**

This paper presents the first large-scale empirical investigation into the robustness of LLMs' fault localizability, developing an end-to-end evaluation framework that addresses limitations in current LLM evaluation. The study found that semantic-preserving mutations cause LLMs to fail to localize the same fault they correctly localized earlier in 78% of cases.

**2. On the Role of Fault Localization Context for LLM-Based Program Repair (April 2026)**

This paper conducted a large-scale empirical study on 500 SWE-bench Verified instances using GPT-5-mini, finding that more context does not consistently improve repair performance, with file-level localization yielding a 15-17x improvement over a no-file baseline.

**3. Improving LLM-Based Fault Localization with External Memory and Project Context (June 2025)**

MemFL is a novel approach that enhances LLM-based fault localization by integrating project-specific knowledge via external memory, including static summaries of the project and dynamic, iterative debugging insights. MemFL using GPT-4o-mini localized 12.7% more bugs than current LLM-based methods, achieving this improvement with just 21% of the execution time and 33% of the API cost.

**4. Explainable Fault Localization for Programming Assignments (September 2025)**

FLAME is a fine-grained, explainable fault localization method tailored for programming assignments that leverages contextual information to guide LLMs in identifying faulty code lines, with LLMs annotating faulty lines with detailed explanations rather than directly predicting line numbers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4006b1d0-4374-45d7-a57f-97f99ac80799",
  "isSidechain": true,
  "promptId": "fd027e93-49f6-4bed-af5b-d09550947dd0",
  "agentId": "a705267f44e982e29",
  "type": "user",
  "uuid": "0f1de7b8-aa2c-4c62-8d96-00ee467adf19",
  "sourceToolAssistantUUID": "4006b1d0-4374-45d7-a57f-97f99ac80799",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T05:14:56.356Z_

<details><summary>↩ Tool result · `toolu_016AhKC3MaviMXjvMiC9uTwV`</summary>

```text
Web search results for query: ""mutation testing" "code understanding" LLM robustness 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Mutation-Guided LLM-based Test Generation at Meta | Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering","url":"https://dl.acm.org/doi/10.1145/3696630.3728544"},{"title":"Meta Applies Mutation Testing with LLM to Improve Compliance Coverage - InfoQ","url":"https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/"},{"title":"Understanding and Bridging the Planner-Coder Gap: A Systematic Study on the Robustness of Multi-Agent Systems for Code Generation","url":"https://arxiv.org/html/2510.10460"},{"title":"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs","url":"https://arxiv.org/html/2401.05940v1"},{"title":"Towards Model-Driven Testing for Assuring the Quality of Large Language Models | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08620-4_12"},{"title":"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs | Proceedings of the IEEE/ACM 3rd International Conference on AI Engineering - Software Engineering for AI","url":"https://dl.acm.org/doi/10.1145/3644815.3644946"},{"title":"Evaluating LLM-Based Test Generation Under Software Evolution","url":"https://arxiv.org/html/2603.23443v1"},{"title":"Transforming QA: Mutahunter and the Power of LLM-Enhanced Mutation Testing | by abilash raghuram | CodeIntegrity Engineering | Medium","url":"https://medium.com/codeintegrity-engineering/transforming-qa-mutahunter-and-the-power-of-llm-enhanced-mutation-testing-18c1ea19add8"},{"title":"Evaluating LLM-Based Test Generation Under Software Evolution Sabaat Haroon","url":"https://arxiv.org/pdf/2603.23443"}]

Based on the web search results, here's what I found about mutation testing, code understanding, and LLM robustness in 2026:

## Recent Research Findings

Researchers have conducted the first large-scale empirical investigation into the robustness of LLMs' fault localizability, developing an end-to-end evaluation framework inspired by mutation testing that addresses limitations in current LLM evaluation, including data contamination, scalability, automation, and extensibility.

Semantic-preserving mutations (SPMs) are applied to assess LLM robustness and whether the LLM's reasoning relies on syntactic cues rather than semantics. The findings are concerning: SPMs cause an LLM to fail to localize the same fault it correctly localized earlier in 78% of cases.

## Code Understanding Evaluation

Mutation-based consistency testing has been proposed for evaluating the code understanding capability of LLMs in the IEEE/ACM 3rd International Conference on AI Engineering-Software Engineering for AI (2024).

A systematic empirical study using an automated mutation-based methodology with semantic-preserving mutation operators reveals substantial robustness flaws: semantically equivalent inputs cause drastic performance drops, with multi-agent systems failing to solve 7.9%–83.3% of problems they initially resolved successfully after applying semantic-preserving mutations.

## Practical Applications

Meta has applied large language models to mutation testing to improve compliance coverage across its software systems, integrating LLM-generated mutants and tests into Meta's Automated Compliance Hardening system (ACH). Meta's ACH system uses LLMs to generate realistic mutants and targeted tests, focusing on privacy, safety, and regulatory concerns, with an LLM-based equivalence detector filtering redundant mutants.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "494a20c3-b17f-4e00-bb77-72c42481617c",
  "isSidechain": true,
  "promptId": "fd027e93-49f6-4bed-af5b-d09550947dd0",
  "agentId": "a705267f44e982e29",
  "type": "user",
  "uuid": "b4b56a6e-af12-4e4a-ace0-fa9977c8c17c",
  "sourceToolAssistantUUID": "494a20c3-b17f-4e00-bb77-72c42481617c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T05:14:57.050Z_

<details><summary>↩ Tool result · `toolu_015CjCCeMZ1CVihFzVYdwCPH`</summary>

```text
Web search results for query: "DeepSeek Qwen CodeLLaMA code models GitHub 2026"

Links: [{"title":"GitHub - deepseek-ai/DeepSeek-Coder: DeepSeek Coder: Let the Code Write Itself · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder"},{"title":"10 Best Open-Source LLM Models (2025 Updated): Llama 4, Qwen 3 and DeepSeek R1","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Open-Source Code Language Models: DeepSeek, Qwen, and Beyond","url":"https://blog.premai.io/open-source-code-language-models-deepseek-qwen-and-beyond/"},{"title":"DeepSeek Coder","url":"https://deepseekcoder.github.io/"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder-V2: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder-V2"},{"title":"Best Local AI for Coding 2026: 10 Models Tested & Ranked | Local AI Master","url":"https://localaimaster.com/blog/best-local-ai-models-programming"},{"title":"GitHub - ollama/ollama: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. · GitHub","url":"https://github.com/ollama/ollama"},{"title":"library","url":"https://ollama.com/library"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"}]

Based on the search results, here's information about DeepSeek, Qwen, and CodeLLaMA code models available on GitHub in 2026:

## DeepSeek Code Models

DeepSeek Coder is composed of a series of code language models, each trained from scratch on 2T tokens, with a composition of 87% code and 13% natural language in both English and Chinese. The project provides various sizes of the code model, ranging from 1B to 33B versions.

DeepSeek-Coder-V2 is an open-source Mixture-of-Experts (MoE) code language model that achieves performance comparable to GPT4-Turbo in code-specific tasks, further pre-trained from an intermediate checkpoint of DeepSeek-V2 with additional 6 trillion tokens. DeepSeek-Coder-V2 expands its support for programming languages from 86 to 338, while extending the context length from 16K to 128K.

The V3.2 release scores 75.69 on LiveBench Coding Average and 46.67 on Agentic Coding, featuring 671 billion total parameters with 37 billion active, using a Mixture of Experts architecture and a 160K context window.

## Qwen Code Models

Alibaba's Qwen2.5-Coder series showcases a diverse range of models tailored for varying computational capacities, from 0.5B to 32B parameters, employing advanced pre-training on 5.5 trillion tokens, integrating file-level and repository-level instruction tuning.

Qwen3-Coder-Next is a coding-focused language model from Alibaba's Qwen team, optimized for agentic coding workflows and local development.

## Comparative Performance

For coding tasks, DeepSeek Coder V2 is noted as the specialist, while Qwen2.5 is also a strong choice. The recommendation for maximum quality is Qwen2.5-Coder-32B for maximum quality, or StarCoder 2-3B if it needs to run locally on a laptop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9da381c-55f9-45a9-8577-2b9f3548a7e2",
  "isSidechain": true,
  "promptId": "fd027e93-49f6-4bed-af5b-d09550947dd0",
  "agentId": "a705267f44e982e29",
  "type": "user",
  "uuid": "74fe8f08-70c4-4efe-8855-95893ce8aa38",
  "sourceToolAssistantUUID": "d9da381c-55f9-45a9-8577-2b9f3548a7e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T05:15:30.761Z_

Perfect! I have comprehensive search results. Let me compile all the findings with proper citations.

## Comprehensive Search Results

### RESEARCH PAPERS ON FAULT LOCALIZATION & ROBUSTNESS (2025-2026)

#### Core Papers on Semantic-Preserving Mutations and LLM Robustness

1. **Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models**
   - Accepted at: IEEE International Conference on Software Testing, Verification and Validation (ICST 2026)
   - arXiv: https://arxiv.org/abs/2504.04372
   - Key Finding: Semantic-preserving mutations cause LLMs to fail fault localization 78% of the time on previously successful cases
   - Scale: 750,013 faulty programs, 245 million lines of code, ~3.8 billion tokens
   - [HTML version](https://arxiv.org/html/2504.04372)

2. **Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection**
   - arXiv: https://arxiv.org/abs/2503.23448
   - Finding: Of 39 implemented transformations from 4 publications, 23 changed code semantics
   - [HTML version](https://arxiv.org/html/2503.23448)

3. **Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?**
   - arXiv: https://arxiv.org/abs/2505.10443
   - [HTML version](https://arxiv.org/html/2505.10443v1)
   - Finding: LLMs often change predictions in response to code mutations, lacking stable semantically-grounded reasoning

#### Recent LLM Fault Localization Papers (2025-2026)

4. **On the Role of Fault Localization Context for LLM-Based Program Repair**
   - arXiv: https://arxiv.org/abs/2604.05481v1
   - Published: April 2026
   - Study Scale: 500 SWE-bench Verified instances with GPT-5-mini
   - Key Finding: File-level localization yields 15-17x improvement over no-file baseline
   - [HTML version](https://arxiv.org/html/2604.05481)

5. **Improving LLM-Based Fault Localization with External Memory and Project Context**
   - arXiv: https://arxiv.org/abs/2506.03585
   - Published: June 2025
   - Method: MemFL - enhances fault localization via external memory with static/dynamic debugging insights
   - Results: 12.7% more bugs localized with 21% of execution time and 33% of API cost of current methods
   - [HTML version](https://arxiv.org/html/2506.03585v1)

6. **Explainable Fault Localization for Programming Assignments via LLM-Guided Annotation**
   - arXiv: https://arxiv.org/abs/2509.25676v1
   - Method: FLAME - fine-grained, explainable fault localization for programming assignments
   - [HTML version](https://arxiv.org/html/2509.25676v1)

7. **AgentFL: Scaling LLM-based Fault Localization to Project-Level Context**
   - arXiv: https://arxiv.org/abs/2403.16362
   - [HTML version](https://arxiv.org/html/2403.16362v1)

#### Mutation Testing & Code Understanding with LLMs

8. **Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs**
   - Published: IEEE/ACM 3rd International Conference on AI Engineering - Software Engineering for AI (2024)
   - arXiv: https://arxiv.org/abs/2401.05940v1
   - [HTML version](https://arxiv.org/html/2401.05940v1)
   - Focus: Evaluates code understanding through mutation-based testing

9. **Mutation-Guided LLM-based Test Generation at Meta**
   - Published: Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering
   - Available at: https://dl.acm.org/doi/10.1145/3696630.3728544
   - Context: Meta applied mutation testing with LLMs for compliance coverage improvement
   - Article: [Meta Applies Mutation Testing with LLM to Improve Compliance Coverage - InfoQ](https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/)
   - Key Innovation: LLM-based equivalence detector filtering redundant mutants

10. **Understanding and Bridging the Planner-Coder Gap: A Systematic Study on the Robustness of Multi-Agent Systems for Code Generation**
    - arXiv: https://arxiv.org/html/2510.10460
    - Finding: Multi-agent systems fail on 7.9%–83.3% of problems after semantic-preserving mutations

11. **Evaluating LLM-Based Test Generation Under Software Evolution**
    - arXiv: https://arxiv.org/abs/2603.23443
    - [PDF version](https://arxiv.org/pdf/2603.23443)
    - [HTML version](https://arxiv.org/html/2603.23443v1)

#### Contrastive Learning & IR-Based Approaches

12. **Multi-view adaptive contrastive learning for information retrieval based fault localization**
    - Published: Automated Software Engineering, Springer Nature
    - Available at: https://link.springer.com/article/10.1007/s10515-025-00573-x
    - Method: MACL-IRFL - multi-view adaptive contrastive learning
    - Results: Up to 28.93% improvement on Accuracy@1, 25.57% on MAP, 20.35% on MRR

13. **Improving Large Language Model Safety with Contrastive Representation Learning**
    - arXiv: https://arxiv.org/abs/2506.11938
    - [HTML version](https://arxiv.org/html/2506.11938v1)
    - Approach: Contrastive representation learning with triplet-based loss + adversarial hard negative mining

14. **Enhancing NLP Robustness and Generalization through LLM-Generated Contrast Sets**
    - arXiv: https://arxiv.org/abs/2503.06648
    - Framework: Scalable framework for systematic evaluation and adversarial training

---

### SOTA CODE LLM MODELS & BENCHMARKS (2026)

#### Leading Open-Source Code Models

**Top Performers for Code:**
- **Kimi K2.6** - Strongest coding-oriented open-source model
- **GLM-4.7 Thinking** - Top open-weight coding model in 2026, free to self-host
- **Qwen 3.6 Plus** - Strongest overall for demanding agentic coding (1M token context)
- **MiniMax-M2.7** - Optimized for agentic workflows, competitive with Claude Opus 4.6
- **DeepSeek V3.2** - Best value via API ($0.35/M tokens)
- **Kimi-Dev-72B** - 60.4% on SWE-bench Verified (SOTA among open-source)
- **Qwen 2.5 Coder 32B** / **Devstral Small 2** - Best for local/consumer hardware

#### GitHub Repositories for Code Models

1. **DeepSeek-Coder**
   - Repository: https://github.com/deepseek-ai/DeepSeek-Coder
   - Website: https://deepseekcoder.github.io/
   - Details: Series of models trained on 2T tokens (87% code, 13% natural language), 1B-33B versions
   - Latest: V3.2 with 160K context window, 671B total parameters (37B active)

2. **DeepSeek-Coder-V2**
   - Repository: https://github.com/deepseek-ai/DeepSeek-Coder-V2
   - Details: MoE code LLM comparable to GPT4-Turbo, 6 trillion additional tokens, 338 programming languages, 128K context

3. **Ollama Library**
   - Repository: https://github.com/ollama/ollama
   - Library: https://ollama.com/library
   - Supports: Kimi-K2.5, GLM-5, MiniMax, DeepSeek, Qwen, Gemma and other models

#### Code Benchmarks & Leaderboards

**Major Benchmarking Platforms:**

- **CodeSOTA** - https://www.codesota.com/
  - Registry: 17 research areas, 1,008 results
  - Benchmarks: 8 benchmarks across 69 models
  - Code Generation: https://www.codesota.com/code-generation
  - LLM Leaderboard: https://www.codesota.com/llm
  - Last Updated: April 23, 2026
  - API Access: /api/sota endpoint

- **Best LLM for Coding (WhatLLM.org)** - https://whatllm.org/best-llm-for-coding

- **Open Source LLM Leaderboard (Onyx AI)** - https://onyx.app/open-llm-leaderboard

- **Vellum LLM Leaderboard** - https://www.vellum.ai/llm-leaderboard

**Key Benchmarks Used:**
- HumanEval - Single function generation from docstring
- LiveCodeBench - Fresh competitive programming problems (post-training cutoff)
- SWE-bench Verified - Real GitHub issues and repositories
  - Claude Opus 4.7: 87.6% (released 2026-04-16)
  - GPT-5.5 (xhigh): Leads coding benchmarks

#### Comprehensive Comparisons

- **BentoML Blog**: [The Best Open-Source LLMs in 2026](https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models)
- **Till Freitag Blog**: [Open-Source LLMs Compared 2026 – 25+ Models](https://till-freitag.com/en/blog/open-source-llm-comparison)
- **Best Open-Source LLMs Agentic Coding**: https://www.mindstudio.ai/blog/best-open-source-llms-agentic-coding-2026
- **SiliconFlow**: [Best Open Source LLMs for Coding](https://www.siliconflow.com/articles/en/best-open-source-LLMs-for-coding)
- **Pinggy**: [Best Open Source Self-Hosted LLMs for Coding in 2026](https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/)
- **Kairntech**: [Top Open-Source LLMs 2026: The Best Models & Comparison](https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/)

#### Qwen Code Models (Alibaba)

- **Qwen2.5-Coder Series** (0.5B-32B)
  - 5.5 trillion tokens pre-training
  - File-level and repository-level instruction tuning
- **Qwen3-Coder-Next** - Coding-focused, optimized for agentic workflows

---

### SUMMARY OF CONCURRENT WORK

Your research on semantic mutation augmentation for fault localization is highly concurrent with active 2026 research:

1. **Direct Overlap**: The ICST 2026 paper on semantic-preserving mutations and LLM fault localization directly addresses your core topic
2. **Related Robustness Work**: Multiple papers (2505.10443, 2510.10460) evaluate LLM robustness under semantic transformations
3. **Application Context**: Recent work by Meta and others applies mutation testing with LLMs practically
4. **Contrastive Learning Angles**: Active research on contrastive approaches for fault localization robustness
5. **Infrastructure**: Latest code LLMs (DeepSeek V2/V3, Qwen 3.x, GLM-4.7) are optimal for training and evaluation

The field is actively exploring exactly this intersection—using semantics-preserving mutations to evaluate and improve LLM robustness for code understanding tasks.

Sources:
- [Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (arXiv 2504.04372)](https://arxiv.org/abs/2504.04372)
- [Semantic-Preserving Transformations as Mutation Operators (arXiv 2503.23448)](https://arxiv.org/abs/2503.23448)
- [Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations? (arXiv 2505.10443)](https://arxiv.org/abs/2505.10443)
- [On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481v1)](https://arxiv.org/abs/2604.05481v1)
- [Improving LLM-Based Fault Localization with External Memory and Project Context (arXiv 2506.03585)](https://arxiv.org/abs/2506.03585)
- [Explainable Fault Localization for Programming Assignments (arXiv 2509.25676v1)](https://arxiv.org/abs/2509.25676v1)
- [AgentFL: Scaling LLM-based Fault Localization (arXiv 2403.16362)](https://arxiv.org/abs/2403.16362)
- [Mutation-based Consistency Testing for Evaluating Code Understanding (arXiv 2401.05940v1)](https://arxiv.org/abs/2401.05940v1)
- [Mutation-Guided LLM-based Test Generation at Meta (ACM FSE)](https://dl.acm.org/doi/10.1145/3696630.3728544)
- [Understanding and Bridging the Planner-Coder Gap (arXiv 2510.10460)](https://arxiv.org/html/2510.10460)
- [Evaluating LLM-Based Test Generation Under Software Evolution (arXiv 2603.23443)](https://arxiv.org/abs/2603.23443)
- [Multi-view adaptive contrastive learning for fault localization (Springer ASE)](https://link.springer.com/article/10.1007/s10515-025-00573-x)
- [Improving LLM Safety with Contrastive Representation Learning (arXiv 2506.11938)](https://arxiv.org/abs/2506.11938)
- [Enhancing NLP Robustness through LLM-Generated Contrast Sets (arXiv 2503.06648)](https://arxiv.org/abs/2503.06648)
- [DeepSeek-Coder (GitHub)](https://github.com/deepseek-ai/DeepSeek-Coder)
- [DeepSeek-Coder-V2 (GitHub)](https://github.com/deepseek-ai/DeepSeek-Coder-V2)
- [Ollama (GitHub)](https://github.com/ollama/ollama)
- [CodeSOTA - State of the Art Code Models](https://www.codesota.com/)
- [Best LLM for Coding 2026 (WhatLLM)](https://whatllm.org/best-llm-for-coding)
- [BentoML: The Best Open-Source LLMs in 2026](https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74fe8f08-70c4-4efe-8855-95893ce8aa38",
  "isSidechain": true,
  "agentId": "a705267f44e982e29",
  "requestId": "req_011CatKRG9JoHqM4eNiCtj88",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fb3af222-18c3-4fa5-9a7d-243defa0bc4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72db8b4c-b4b5-4977-a136-86a994ca4635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WrccaMAteFdgkS3HS3Hp8g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4350,
      "cache_read_input_tokens": 22778,
      "output_tokens": 3971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4350
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3971,
          "cache_read_input_tokens": 22778,
          "cache_creation_input_tokens": 4350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4350,
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
