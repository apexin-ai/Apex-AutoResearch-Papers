# Research conversation: You are helping with a paper distillation task. Fetch and extract detailed information from the MT-Bench paper: "Judging

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ace90c699656f23d3.jsonl`
- **Structured JSON:** [`dcd25ded3dec403f8d10.json`](../../sessions/dc/dcd25ded3dec403f8d10.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-21T16:37:54.033Z_

You are helping with a paper distillation task. Fetch and extract detailed information from the MT-Bench paper: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (NeurIPS 2023).

Use WebFetch to get the full paper from https://arxiv.org/html/2306.05685

Extract ALL of the following in detail:
1. Full introduction text (every paragraph)
2. All contribution statements
3. Complete experiment section (datasets, baselines, metrics, results with numbers)
4. All figure and table captions
5. Paragraphs referencing figures/tables
6. Limitations / future work section
7. Method details
8. Implementation details
9. Ablation studies if any
10. Conclusion section

Return the COMPLETE extracted text, not summaries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "eb6e2170-4739-4573-9ff0-064b0ab92c4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T16:37:54.036Z_

```json
{
  "parentUuid": "eb6e2170-4739-4573-9ff0-064b0ab92c4a",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "91307d02-e75a-4d4b-a088-675da5b072bb",
  "timestamp": "2026-05-21T16:37:54.036Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-21T16:37:55.970Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013W7GDseHkQdcg4Z8LGNaic`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91307d02-e75a-4d4b-a088-675da5b072bb",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3PvMsV7UjW3xR1R51u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cf6252f-71d7-4741-acdb-4ff5d1694291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016PZKLZABDmwczDwnPjGDf4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9031,
      "cache_read_input_tokens": 7260,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9031
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 7260,
          "cache_creation_input_tokens": 9031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9031,
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

_source line 4 · 2026-05-21T16:37:55.972Z_

<details><summary>↩ Tool result · `toolu_013W7GDseHkQdcg4Z8LGNaic`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cf6252f-71d7-4741-acdb-4ff5d1694291",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "021b2cdd-1c43-4559-ba88-9a64befa9ce3",
  "sourceToolAssistantUUID": "1cf6252f-71d7-4741-acdb-4ff5d1694291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T16:37:58.719Z_

I'll fetch the full paper from arXiv HTML in multiple parts to capture all content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "021b2cdd-1c43-4559-ba88-9a64befa9ce3",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3Q4saqyaLWLHue1HVJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c4c33bb-6d37-49cc-9ca0-6379d6f6c68c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018dDSeUv2a7dKrweEKPqhck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 16291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 6 · 2026-05-21T16:38:00.800Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YUWvzVz9cgMEwYbzceDVsC`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.05685",
  "prompt": "Extract the COMPLETE text of: 1) Abstract, 2) Full Introduction section (every paragraph verbatim), 3) All contribution statements, 4) Related Work section. Return the complete raw text without summarizing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c4c33bb-6d37-49cc-9ca0-6379d6f6c68c",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3Q4saqyaLWLHue1HVJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94a379bd-8928-4600-af93-503b3cbba4fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018dDSeUv2a7dKrweEKPqhck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 16291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 7 · 2026-05-21T16:38:19.618Z_

<details><summary>↩ Tool result · `toolu_01YUWvzVz9cgMEwYbzceDVsC`</summary>

```text
# Extracted Content from Research Paper

## 1) Abstract

"Evaluating large language model (LLM) based chat assistants is challenging due to their broad capabilities and the inadequacy of existing benchmarks in measuring human preferences. To address this, we explore using strong LLMs as judges to evaluate these models on more open-ended questions. We examine the usage and limitations of LLM-as-a-judge, including position, verbosity, and self-enhancement biases, as well as limited reasoning ability, and propose solutions to mitigate some of them. We then verify the agreement between LLM judges and human preferences by introducing two benchmarks: MT-bench, a multi-turn question set; and Chatbot Arena, a crowdsourced battle platform. Our results reveal that strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans. Hence, LLM-as-a-judge is a scalable and explainable way to approximate human preferences, which are otherwise very expensive to obtain."

## 2) Full Introduction Section

"There has been a proliferation of LLM-based chat assistants (chatbots) that leverage supervised instruction fine-tuning and reinforcement learning with human feedback (RLHF) to unlock new instruction following and conversational abilities. Once aligned with humans, these chat models are strongly preferred by human users over the original, unaligned models on which they are built. However, the heightened user preference does not always correspond to improved scores on traditional LLM benchmarks – benchmarks like MMLU and HELM cannot effectively tell the difference between these aligned models and the base models. This phenomenon suggests that there is a fundamental discrepancy between user perceptions of the usefulness of chatbots and the criteria adopted by conventional benchmarks.

We argue that this discrepancy primarily arises due to existing evaluation that only measures LLMs' core capability on a confined set of tasks (e.g., multi-choice knowledge or retrieval questions), without adequately assessing its alignment with human preference in open-ended tasks, such as the ability to accurately adhere to instructions in multi-turn dialogues. As a demonstration, we show conversation histories with two models on an MMLU question in Figure 1. The two models are LLaMA-13B, a pre-trained base model without fine-tuning, and Vicuna-13B, our fine-tuned model from LLaMA-13B on high-quality conversations (the training details are in Appendix E). Despite the base LLaMA models showing competitive performance on conventional benchmarks (Table 9), its answers to open-ended questions are often not preferred by humans. This misalignment of conventional benchmarks underscores the core problem driving this paper: the need for a robust and scalable automated method to evaluate LLM alignment with human preferences.

To study this, we introduce two benchmarks with human ratings as the primary evaluation metric: MT-bench and Chatbot Arena. MT-bench is a series of open-ended questions that evaluate a chatbot's multi-turn conversational and instruction-following ability – two critical elements for human preference. MT-bench is also carefully constructed to differentiate chatbots based on their core capabilities, such as reasoning and math. In addition, we develop Chatbot Arena, a crowdsourced platform featuring anonymous battles between chatbots in real-world scenarios – Users engage in conversations with two chatbots at the same time and rate their responses based on personal preferences.

While human evaluation is the gold standard for assessing human preferences, it is exceptionally slow and costly. To automate the evaluation, we explore the use of state-of-the-art LLMs, such as GPT-4, as a surrogate for humans. Because these models are often trained with RLHF, they already exhibit strong human alignment. We call this approach "LLM-as-a-judge". This approach has been tried in our earlier blog post and other concurrent or follow-up work. However, there has not been a systematic study of this approach.

In this paper, we study the LLM-as-a-judge approach by comparing it to the gold standard of human evaluation. We examine several potential limitations of the LLM-as-a-judge approach including position bias, verbosity bias, self-enhancement bias, and limited reasoning ability. We show that some of the biases are minor or can be mitigated. Once addressed, our results from 3K controlled expert votes and 3K crowdsourced human votes in the wild verify that GPT-4 judge match human evaluations at an agreement rate exceeding 80%, achieving the same level of human-human agreement (§4.2, Table 4). Consequently, this suggests LLM-as-a-judge is a scalable method to swiftly evaluate human preference, serving as a promising alternative to traditional human evaluations.

This paper makes two contributions: (1) a systematic study of LLM-as-a-judge; and (2) human preference datasets with high-quality questions and diverse user interactions from MT-bench and Chatbot Arena. In addition, we argue for the adoption of a hybrid evaluation framework for future LLM benchmarks: by combining the existing capability-based benchmarks and the new preference-based benchmarks with LLM-as-a-judge, one can swiftly and automatically evaluate both the core capabilities and human alignment of models. We publicly release 80 MT-bench questions, 3K expert votes, and 30K conversations with human preferences for future study."

## 3) Contribution Statements

The authors explicitly state two main contributions:

1. "A systematic study of LLM-as-a-judge"
2. "Human preference datasets with high-quality questions and diverse user interactions from MT-bench and Chatbot Arena"

Additionally, they propose "the adoption of a hybrid evaluation framework for future LLM benchmarks" combining capability-based and preference-based benchmarks.

## 4) Related Work Section

**Note:** The provided document does not contain a dedicated "Related Work" section. The paper references prior work throughout (particularly in the Introduction and Discussion sections via citations), but does not organize this into a separate Related Work section as is conventional in academic papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94a379bd-8928-4600-af93-503b3cbba4fe",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "1172d862-cab3-41c1-a56b-211f5fc5642c",
  "sourceToolAssistantUUID": "94a379bd-8928-4600-af93-503b3cbba4fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T16:38:24.680Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LaRU9V7xH49LTtTvk6jmPN`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.05685",
  "prompt": "Extract the COMPLETE text of the Methods section, including: 1) MT-Bench description (all question categories, how it was constructed), 2) Chatbot Arena description, 3) LLM-as-a-judge methodology (pairwise comparison, single answer grading, reference-guided grading), 4) All prompts used for judges, 5) Implementation details. Return verbatim text without summarizing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1172d862-cab3-41c1-a56b-211f5fc5642c",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3RonYF9T9jsxzJrn7D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0c97c68-711d-4843-98f4-70de823d8ea7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JCR7Ag3CyCgUvuoENDcB4a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1552,
      "cache_read_input_tokens": 17723,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1552
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 17723,
          "cache_creation_input_tokens": 1552,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1552,
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

_source line 9 · 2026-05-21T16:41:16.805Z_

<details><summary>↩ Tool result · `toolu_01LaRU9V7xH49LTtTvk6jmPN`</summary>

```text
&lt;persisted-output>
Output too large (66.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/toolu_01LaRU9V7xH49LTtTvk6jmPN.txt

Preview (first 2KB):
# Methods Section Extraction

## MT-Bench Description

MT-bench comprises "80 high-quality multi-turn questions" organized into eight categories: writing, roleplay, extraction, reasoning, math, coding, knowledge I (STEM), and knowledge II (humanities/social science). The authors "manually designed 10 multi-turn questions" per category to "test multi-turn conversation and instruction-following ability, covering common use cases and focusing on challenging questions to differentiate models."

Sample questions span diverse tasks: composing travel blogs with constraint-based rewrites, solving polynomial equations across multiple turns, and explaining economic concepts at different comprehension levels.

## Chatbot Arena Description

Chatbot Arena operates as "a crowdsourced platform featuring anonymous battles." Users "interact with two anonymous models simultaneously, posing the same question to both. They vote for which model provides the preferred response, with the identities of the models disclosed post-voting." The platform collected "around 30K votes" during its initial month of operation, capturing "a wide range of unrestricted use cases and votes in the wild, based on the diverse interests of users" without relying on predefined questions.

## LLM-as-a-Judge Methodology

The paper proposes three judge variations:

**Pairwise Comparison:** "An LLM judge is presented with a question and two answers, and tasked to determine which one is better or declare a tie."

**Single Answer Grading:** "An LLM judge is asked to directly assign a score to a single answer."

**Reference-Guided Grading:** "It may be beneficial to provide a reference solution if applicable."

## Prompts and Implementation

The paper references prompt templates in appendices but does not reproduce them verbatim in the main text. Key prompt variations include:
- Default pairwise comparison prompt
- Single-answer scoring prompt  
- Chain-of-thought prompts for math/reasoning
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0c97c68-711d-4843-98f4-70de823d8ea7",
  "isSidechain": true,
  "promptId": "a6787d7e-356d-43d4-972c-414995b1c71b",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "80b50083-c722-4033-9bad-736b692a8d8d",
  "sourceToolAssistantUUID": "c0c97c68-711d-4843-98f4-70de823d8ea7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T16:41:18.933Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PQirbAowwe7rtrttRuZBa1`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/toolu_01LaRU9V7xH49LTtTvk6jmPN.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80b50083-c722-4033-9bad-736b692a8d8d",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3esKjAL1Jfs6NFj87E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7980f601-4592-4edd-9ba9-aea2fbf5ac98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012iYzK5itWjq5T8pf4hwpha",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 756,
      "cache_read_input_tokens": 19275,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 756
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 19275,
          "cache_creation_input_tokens": 756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 756,
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

_source line 11 · 2026-05-21T16:41:19.209Z_

<details><summary>↩ Tool result · `toolu_01PQirbAowwe7rtrttRuZBa1`</summary>

```text
1	# Methods Section Extraction
2	
3	## MT-Bench Description
4	
5	MT-bench comprises "80 high-quality multi-turn questions" organized into eight categories: writing, roleplay, extraction, reasoning, math, coding, knowledge I (STEM), and knowledge II (humanities/social science). The authors "manually designed 10 multi-turn questions" per category to "test multi-turn conversation and instruction-following ability, covering common use cases and focusing on challenging questions to differentiate models."
6	
7	Sample questions span diverse tasks: composing travel blogs with constraint-based rewrites, solving polynomial equations across multiple turns, and explaining economic concepts at different comprehension levels.
8	
9	## Chatbot Arena Description
10	
11	Chatbot Arena operates as "a crowdsourced platform featuring anonymous battles." Users "interact with two anonymous models simultaneously, posing the same question to both. They vote for which model provides the preferred response, with the identities of the models disclosed post-voting." The platform collected "around 30K votes" during its initial month of operation, capturing "a wide range of unrestricted use cases and votes in the wild, based on the diverse interests of users" without relying on predefined questions.
12	
13	## LLM-as-a-Judge Methodology
14	
15	The paper proposes three judge variations:
16	
17	**Pairwise Comparison:** "An LLM judge is presented with a question and two answers, and tasked to determine which one is better or declare a tie."
18	
19	**Single Answer Grading:** "An LLM judge is asked to directly assign a score to a single answer."
20	
21	**Reference-Guided Grading:** "It may be beneficial to provide a reference solution if applicable."
22	
23	## Prompts and Implementation
24	
25	The paper references prompt templates in appendices but does not reproduce them verbatim in the main text. Key prompt variations include:
26	- Default pairwise comparison prompt
27	- Single-answer scoring prompt  
28	- Chain-of-thought prompts for math/reasoning
29	- Reference-guided variants
30	- Multi-turn conversation prompts
31	
32	For math questions specifically, researchers employed "reference-guided" methods where "we first generate LLM judge's answer independently, and then display it as a reference answer in the judge prompt."
33	
34	## Key Implementation Details
35	
36	**Position Bias Mitigation:** The conservative approach calls "a judge twice by swapping the order of two answers and only declare a win when an answer is preferred in both orders."
37	
38	**Few-Shot Enhancement:** Testing included "three good judgment examples" covering cases where "A is better, B is better, and tie."
39	
40	**Multi-Turn Handling:** Complete conversations were presented "in a single prompt" rather than breaking into separate prompts, as the latter caused referencing issues.
41	
42	**Model Coverage:** Evaluations tested six models (GPT-4, GPT-3.5, Claude-V1, Vicuna-13B, Alpaca-13B, LLaMA-13B) across all 80 MT-bench questions.
43	
44	Human evaluation involved "58 expert-level human labelers" (mostly graduate students) evaluating "at least 20 random multi-turn questions" each, generating "around 3K votes."
45	
46	Human evaluators received "$20 for judging 20 questions, which corresponds to an hourly rate of around $35."
47	
48	Human raters were additionally shown GPT-4's judgments when differing and asked whether those assessments were "reasonable," finding humans deemed them reasonable in "75% of cases."
49	
50	Human participants accepted terms granting researchers "the right to release the conversation data."
51	
52	Human agreement itself was computed as "the probability of two randomly selected but not identical humans agreeing on the vote for a randomly selected question."
53	
54	Human-majority voting considered majority human votes, serving as an upper-bound validation metric for LLM judge alignment.
55	
56	Human voting interface presented "questions from MT-bench and answers from two random anonymous assistants" alongside "an instruction similar to the prompt we give to GPT-4."
57	
58	For sensitive categories like math and reasoning, humans could "also see a reference solution."
59	
60	Human raters could "skip up to 5 questions if they are not confident."
61	
62	Human Chatbot Arena participants were "not paid" and could "use this platform without registration," requiring only acceptance of terms of use.
63	
64	Human data underwent cleaning to remove "Personal Identifiable Information (PII)" and conversations were tagged "with OpenAI moderation APIs."
65	
66	Human Chatbot Arena votes came from "2114 unique IPs," with researchers randomly sampling "3K single-turn votes from 30K arena data."
67	
68	## Fine-Tuning Details (Vicuna Judge)
69	
70	Researchers fine-tuned Vicuna-13B as a cost-effective judge using "22K single-turn votes from the arena." Training formulated the task as "a 3-way sequence classification problem," predicting which answer was "better (or tie)." Training parameters included "3 epochs with a cosine learning rate scheduler and a 2e-5 maximum learning rate," evaluated on "2K validation dataset."
71	
72	Human-aligned Vicuna achieved "85.5% when excluding tie predictions and labels," approaching GPT-4's "87%" performance on non-tie votes.
73	
74	Human preference data used for fine-tuning covered "all models supported by the time of this paper submission (GPT-4, GPT-3.5, Claude-v1, Vicuna-13b, Vicuna-7b, Koala-13B, Alpaca-13B, LLaMA-13B, Dolly-12B, FastChat-T5, RWKV-4-Raven, MPT-Chat, OpenAssistant, ChatGLM, and StableLM)."
75	
76	Human preference labels distinguished between "both-bad-vote and tie-vote."
77	
78	Human votes split into "20K votes for training, and 2K for validation."
79	
80	## Agreement Metrics
81	
82	The study computed agreement as "the probability of randomly selected individuals (but not identical) of each type agreeing on a randomly selected question."
83	
84	Setup S1 "includes non-tie, tie, and inconsistent (due to position bias) votes and counts inconsistent as tie."
85	
86	Setup S2 "only includes non-tie votes."
87	
88	Random baseline for S1 was 33%, while S2 used 50%.
89	
90	Human-majority agreement served as an upper-bound estimate for optimal LLM-human alignment.
91	
92	Human evaluations showed GPT-4 achieved "85%" agreement (Setup S2), matching "the same level of agreement between humans" at "81%."
93	
94	Human preference analysis revealed "when a human's choice deviated from GPT-4," humans deemed GPT-4's judgments "reasonable in 75% of cases" and were "willing to change their choices in 34% of cases."
95	
96	Human disagreement with GPT-4 occurred in only "25% of cases" where human raters fully rejected the LLM judge's reasoning.
97	
98	Human experts showed willingness to defer to LLM assessment in over one-third of disagreement scenarios.
99	
100	Human-majority voting aligned with individual humans at "81-90%" across different evaluation setups.
101	
102	Human preference distributions varied by model-pair disparity: agreement "progressively increases in line with the performance disparity of the model pairs (i.e., larger win rate difference), from 70% to nearly 100%."
103	
104	Human agreement on close-performance model comparisons remained modest at "70%," while "GPT-4 aligns with humans better when significant performance differences exist."
105	
106	Human-crowd agreement on Chatbot Arena data showed similar patterns, with GPT-4 reaching "95% agreement" (Setup S2) on non-tie votes.
107	
108	Human Chatbot Arena votes displayed comparable ranking patterns to expert MT-bench votes, validating cross-dataset consistency.
109	
110	Human preference stability was confirmed through temporal analysis: platform votes collected over extended periods showed consistent model rankings.
111	
112	Human preference granularity separated into first-turn and second-turn evaluations, revealing multi-turn assessment provided "better differentiate some advanced abilities of models."
113	
114	Human rater expertise level (graduate students) likely contributed to evaluation quality and consistency with strong LLM judges.
115	
116	Human cost economics favored LLM judges: GPT-4 evaluation proved "scalable and explainable" compared to expensive human assessment.
117	
118	Human preference benchmarks proved "valuable additions to the current standardized LLM benchmarks," addressing gaps in open-ended task evaluation.
119	
120	Human preference data release included approximately "80 MT-bench questions, 3K expert votes, and 30K conversations with human preferences."
121	
122	Human feedback mechanisms enabled iterative improvement: displaying "GPT-4's judgments to humans" when disagreement occurred supported validation and refinement.
123	
124	Human participant recruitment obtained "consent by letting them sign an application form" prior to evaluation work.
125	
126	Human rater qualifications emphasized graduate-level expertise, distinguishing this from typical crowdsourcing approaches.
127	
128	Human Chatbot Arena interface captured "unrestricted" user interactions rather than curated experimental scenarios.
129	
130	Human preference dataset release underwent ethical review, with "Personal Identifiable Information (PII)" removal and "toxic conversations" identification protocols.
131	
132	Human preference stability testing across models and prompts demonstrated robustness: "high agreements with human experts" persisted across multiple experimental configurations.
133	
134	Human preference-LLM judge alignment exceeded human-human pairwise agreement, suggesting GPT-4 captured aggregate rather than individual preferences.
135	
136	Human study limitations acknowledged that "no single benchmark can determine model quality, meaning that a comprehensive evaluation is needed."
137	
138	Human preference diversity across categories showed varying LLM-human alignment: math and coding questions exhibited higher judge consistency than creative writing tasks.
139	
140	Human preference weighting treated all votes equally rather than using expertise-weighted aggregation.
141	
142	Human preference analysis excluded consideration of "safety" dimensions, focusing "largely" on "helpfulness."
143	
144	Human Chatbot Arena demographics reflected "2114 unique IPs," indicating broad participation beyond institutional researchers.
145	
146	Human evaluation intensity per rater (20+ questions) provided sufficient individual preference signals for reliable aggregation.
147	
148	Human preference temporal dynamics across the month-long Chatbot Arena operation showed stable model rankings.
149	
150	Human preference capture methodology preserved conversation context, enabling analysis of multi-turn instruction following.
151	
152	Human preference ground truth status received qualification: "gold standard for assessing human preferences" but acknowledged human evaluators themselves reflect biased samples.
153	
154	Human preference validation checked whether LLM judges could "match both controlled and crowdsourced human preferences," confirming cross-source consistency.
155	
156	Human expert votes derived from "3K votes" across all model-pair combinations in MT-bench's 80 questions.
157	
158	Human crowd votes sampled "3K single-turn votes from 30K arena data" to maintain computational feasibility.
159	
160	Human preference alignment with LLM judges demonstrated via metric showing "over 80% agreement," establishing "foundation for an LLM-based evaluation framework."
161	
162	Human preference datasets were released "publicly available at https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge."
163	
164	Human preference methodology employed "anonymous battles" design to reduce expectation bias in crowdsourcing scenarios.
165	
166	Human preference control achieved through expert recruiter selection (graduate student population) versus open crowdsourcing (Chatbot Arena).
167	
168	Human preference quality assurance included optional reference solutions for technical questions.
169	
170	Human preference instruction clarity maintained consistency: evaluators received "an instruction similar to the prompt we give to GPT-4."
171	
172	Human preference methodology allowed "skip" options without penalty, supporting evaluator confidence calibration.
173	
174	Human preference data collection conducted with explicit "terms of use" acceptance from Chatbot Arena participants.
175	
176	Human preference compensation ($20 per 20 questions) established reasonable hourly rates for expert labor.
177	
178	Human preference inter-rater reliability computed via pairwise agreement probabilities rather than Kappa coefficients.
179	
180	Human preference analysis separated "non-tie" votes for cleaner signal-to-noise assessment.
181	
182	Human preference inconsistent judge behavior ("position bias") was counted as tie in Setup S1 analysis.
183	
184	Human preference random baseline established separate expectations for tie-inclusive (33%) versus tie-exclusive (50%) comparisons.
185	
186	Human preference upper-bound estimation employed human-majority voting methodology.
187	
188	Human preference breakdown analysis examined category-wise and model-pair-wise agreement patterns.
189	
190	Human preference findings revealed GPT-4 single-answer grading "matches both pairwise GPT-4 and human preferences very well."
191	
192	Human preference discovery that "fine-tuning on high-quality dialog datasets... can consistently improve the model performance on MMLU."
193	
194	Human preference insight demonstrated small high-quality conversation datasets teach "a style preferred by GPT-4 (or approximately human) but cannot improve MMLU significantly."
195	
196	Human preference comprehensive evaluation strategy recommended "using both kinds of benchmarks" rather than relying on preference-based assessment alone.
197	
198	Human preference leaderboard maintenance was planned as "regularly updated leaderboard with more models" at Hugging Face.
199	
200	Human preference methodology aligned with DynaBench principles: "emphasizing dynamic data with human-in-the-loop."
201	
202	Human preference automation potential recognized: "LLM-as-a-judge approach can automate and scale platforms of this nature."
203	
204	Human preference dimension analysis acknowledged multiple sub-dimensions (accuracy, relevance, creativity) were "combined into a single metric" in current implementation.
205	
206	Human preference safety evaluation was deferred: paper acknowledged largely "neglecting safety" despite recognizing "honesty and harmlessness are crucial."
207	
208	Human preference future enhancements anticipated "more advanced methods can be developed" beyond initial bias mitigation solutions.
209	
210	Human preference interdisciplinary grounding referenced social cognition literature on "self-enhancement bias."
211	
212	Human preference validation demonstrated LLM judges achieved "an agreement rate of over 80%, on par with the level of agreement among human experts."
213	
214	Human preference cost-benefit analysis implicitly supported LLM evaluation as "exceptionally slow and costly" human assessment became prohibitively expensive at scale.
215	
216	Human preference dataset publication facilitated "future study" of human preferences and model behavior patterns.
217	
218	Human preference collection infrastructure utilized web platforms (Chatbot Arena) and structured interfaces (MT-bench voting) for systematic data capture.
219	
220	Human preference standardization efforts via open dataset release supported reproducibility and comparative future research.
221	
222	Human preference methodology embodied pragmatic compromise: "LLM-as-a-judge is a scalable and explainable way to approximate human preferences, which are otherwise very expensive to obtain."
223	
224	Human preference validation across two independent sources (expert MT-bench votes and crowdsourced Arena votes) strengthened generalization claims.
225	
226	Human preference reliability tests examined position bias, verbosity bias, and self-enhancement bias systematically.
227	
228	Human preference mitigation strategies for LLM judges included prompt engineering, reference answers, and position swapping.
229	
230	Human preference open challenges remained regarding fine-grained dimension separation and safety-focused evaluation extensions.
231	
232	Human preference research roadmap explicitly listed "1) Benchmarking chatbots at scale with a broader set of categories 2) Open-source LLM judge aligned with human preference 3) Enhancing open models' math/reasoning capability."
233	
234	Human preference societal impact assessment acknowledged both benefits (enhanced chatbot quality) and risks (job displacement).
235	
236	Human preference methodological transparency supported through detailed appendices on data collection protocols, prompts, and training procedures.
237	
238	Human preference comparative analysis showed LLM-human agreement "significantly outperforming random guesses" while remaining subject to identifiable biases.
239	
240	Human preference research positioned work as "extended version of [an] earlier blog post," indicating iterative publication and refinement.
241	
242	Human preference funding acknowledged: "partly supported by gifts from Anyscale, Astronomer, Google, IBM, Intel, Lacework, Microsoft, MBZUAI, Samsung SDS, Uber, and VMware" plus fellowship support.
243	
244	Human preference research team composition spanned multiple institutions (UC Berkeley, UC San Diego, Carnegie Mellon, Stanford, MBZUAI).
245	
246	Human preference acknowledgment thanked "Xinyang Geng, Hao Liu, Eric Wallace, Xuecheng Li, Tianyi Zhang, Qirong Ho, and Kevin Lin for their insightful discussions."
247	
248	Human preference dissemination included code release, dataset sharing, and public leaderboard hosting.
249	
250	Human preference sustainability planning considered "regularly updated leaderboard" maintenance to support ongoing benchmarking.
251	
252	Human preference research reproducibility supported through "open-source registry" philosophy alignment with platforms like OpenAI's Evals framework.
253	
254	Human preference methodological rigor demonstrated via multiple experimental conditions, control variations, and ablation studies documented in appendices.
255	
256	Human preference scope acknowledged "multiple dimensions" within helpfulness while establishing feasibility of combined single-metric assessment.
257	
258	Human preference interpretation guidance emphasized LLM judges matched human consensus rather than replacing individual human judgment entirely.
259	
260	Human preference ethical considerations included consent mechanisms, PII removal, toxicity filtering, and data usage transparency.
261	
262	Human preference scalability demonstrated through processing "30K conversations" versus manual evaluation constraints.
263	
264	Human preference economic analysis implicitly showed LLM evaluation at "significantly less expensive" operational costs.
265	
266	Human preference validation incorporated author expertise: paper included "author votes" as supplementary preference signal alongside external raters.
267	
268	Human preference inter-annotator reliability computation used pairwise agreement methodology appropriate for non-fixed-set judges.
269	
270	Human preference categorization across 8 dimensions enabled granular performance analysis by task type.
271	
272	Human preference model coverage comprehensively included proprietary (GPT-4, GPT-3.5, Claude) and open-source (Vicuna, Alpaca, LLaMA) architectures.
273	
274	Human preference temporal dynamics across single month of Chatbot Arena collection provided initial evidence for stable preference rankings.
275	
276	Human preference geographic/linguistic diversity of crowdsourced judges enhanced generalization beyond single-institution expert panel.
277	
278	Human preference robustness testing examined position bias across different question categories and model-pair performance disparities.
279	
280	Human preference analysis demonstrated minimal self-enhancement bias despite GPT-4 showing "10% higher win rate" for self-generated content.
281	
282	Human preference finding that few-shot prompts "significantly increase the consistency" offered optional pathway for practitioners prioritizing reduced position bias.
283	
284	Human preference discovery of chain-of-thought limitations—LLM judges "exactly copied Assistant B's answer (which contains arithmetic errors)"—highlighted important failure mode.
285	
286	Human preference reference-guided solution reducing "failure rate (from 70% to 15%)" quantified practical mitigation effectiveness.
287	
288	Human preference comprehensive tables (Tables 5-9) documented agreement metrics across setups, judge types, and model pairs.
289	
290	Human preference visualization (Figures 2-3) displayed win rate curves showing "closely match" between LLM and human judge outputs.
291	
292	Human preference category-wise breakdown (Table 8) revealed GPT-4 performed strongest in "STEM" (76.6%) and weakest in "Reasoning" (49.3%).
293	
294	Human preference fine-tuning evidence showed Vicuna-13B improved from "15.0% consistency to 65.0%" after arena training.
295	
296	Human preference error rate elimination through classification formulation demonstrated "every output is recognizable (error rate 0%)."
297	
298	Human preference training details specified "20K votes for training, and 2K for validation" from arena dataset.
299	
300	Human preference hyperparameter selection methodology used "2K validation dataset to choose hyper-parameters."
301	
302	Human preference test set validation ensured "same 3K dataset in the main body of the paper" for fair comparison.
303	
304	Human preference alternative judge exploration in appendix showed "promising preliminary results" for open-source Vicuna-based approach.
305	
306	Human preference dataset construction from "125K conversations after data cleaning" provided substantial training signal.
307	
308	Human preference ShareGPT source filtering "convert the HTML back to markdown and filter out some inappropriate or low-quality samples."
309	
310	Human preference segmentation strategy handled "lengthy conversations into smaller segments that fit the model's maximum context length."
311	
312	Human preference training set variants distinguished "Selected" (3K high-quality), "Single" (first turns), and "All" (complete conversations).
313	
314	Human preference cluster-based selection of "Selected" dataset picked "centroid of each cluster" to maximize diversity.
315	
316	Human preference training hyperparameters held "global batch size=128, learning=2e-5, epochs=3, seq length=2048" consistently.
317	
318	Human preference computational requirements specified "8x A100 GPUs" with "longest single training run takes around 2 days."
319	
320	Human preference infrastructure leveraged "SkyPilot managed spot instances for saving training costs and FlashAttention for memory optimizations."
321	
322	Human preference training codebase built "on top of the Alpaca code but additionally handles multi-turn conversations."
323	
324	Human preference implementation publicly released at "https://github.com/lm-sys/FastChat."
325	
326	Human preference token statistics showed dramatic scaling: Selected (4.8M tokens), Single (184M tokens), All (370M tokens).
327	
328	Human preference sequence counts paralleled: Selected (3K sequences), Single (257K sequences), All (257K sequences).
329	
330	Human preference conversation turn analysis revealed: Selected (4.0 avg turns), Single (1.0 avg turns), All (2.9 avg turns).
331	
332	Human preference response length metrics showed: Selected (343 tokens), Single (473 tokens), All (373 tokens).
333	
334	Human preference model architecture baseline of "LLaMA" with "13B" parameters established consistent comparison foundation.
335	
336	Human preference fine-tuning scale analysis demonstrated "small high-quality conversation dataset" outperformed larger but lower-quality datasets on preference metrics.
337	
338	Human preference benchmark complementarity insight showed "no single benchmark can determine model quality."
339	
340	Human preference evaluation strategy recommended "comprehensively evaluate models with both kinds of benchmarks."
341	
342	Human preference MMLU comparison baseline provided "5-shot" evaluation condition.
343	
344	Human preference TruthfulQA baseline used "0-shot" condition.
345	
346	Human preference MT-bench scoring methodology requested "a score for each turn on a scale of 10."
347	
348	Human preference average score computation from "160 = 80 × 2 turns" established normalized 0-10 scale.
349	
350	Human preference Alpaca baseline comparison included "48.1" MMLU score for "13B" variant.
351	
352	Human preference LLaMA baseline established "47.0" MMLU for "13B" with "1T" training tokens.
353	
354	Human preference training token scaling effect demonstrated: Vicuna-7B scores increased from "5.95" (4.8M tokens) to "6.04" (184M tokens) to "6.00" (370M tokens).
355	
356	Human preference data size-performance relationship showed diminishing returns: additional tokens beyond "184M" provided minimal score improvement.
357	
358	Human preference position bias severity metrics quantified: Claude-v1 showed "75.0% biased toward first," GPT-3.5 showed "50.0%," GPT-4 showed "30.0%."
359	
360	Human preference consistency metrics established baselines: Claude-v1 "23.8%," GPT-3.5 "46.2%," GPT-4 "65.0%."
361	
362	Human preference rename prompt effectiveness for Claude-v1 improved consistency from "23.8% to 56.2%," indicating name-based bias.
363	
364	Human preference verbosity bias attack methodology created "repetitive list" with "first 5 items are rephrased from the original 5 items."
365	
366	Human preference verbosity defense rated GPT-4 at "8.7% failure rate" versus "91.3%" for Claude-v1 and GPT-3.5.
367	
368	Human preference reference-guided method improved math grading from "14/20 failures to 3/20 failures."
369	
370	Human preference chain-of-thought intermediate results showed "6/20 failures," partial but incomplete improvement.
371	
372	Human preference agreement setup S1 random baseline established "33%" expectation for three-way choice.
373	
374	Human preference agreement setup S2 random baseline established "50%" expectation for binary non-tie comparison.
375	
376	Human preference tie-handling methodology defined: "inconsistent (due to position bias) votes and counts inconsistent as tie."
377	
378	Human preference statistical confidence derived from large sample sizes: MT-bench votes totaled "~3K," Arena votes sampled "3K from 30K."
379	
380	Human preference category-wise agreement analysis revealed variable performance: close model pairs showed "70%" agreement versus "nearly 100%" for distant pairs.
381	
382	Human preference model pair disparity effect demonstrated "progressively increases" correlation with "win rate difference."
383	
384	Human preference average win rate computation aggregated "against all other players."
385	
386	Human preference pairwise comparison scalability limitation acknowledged: "number of possible pairs grows quadratically."
387	
388	Human preference single-answer grading stability observation noted "results may become unstable, as absolute scores are likely to fluctuate more than relative pairwise results."
389	
390	Human preference pairwise comparison advantage highlighted: more reliable discrimination between "similar" model outputs.
391	
392	Human preference explainability benefit captured: LLM judges provided "not only scores but also explanations, making their outputs interpretable."
393	
394	Human preference cost-benefit analysis for few-shot approach noted "4×4\\times4 × more expensive" API costs for modest consistency improvements.
395	
396	Human preference conservative position bias solution recommended "only declare a win when an answer is preferred in both orders."
397	
398	Human preference aggressive alternative proposed "assign positions randomly, which can be effective at a large scale."
399	
400	Human preference multi-turn prompt design discovery: single prompt superior to "breaking the two turns into two prompts" due to reference resolution.
401	
402	Human preference referencing problem manifested when "GPT-4 wrongly referred to the second example in Assistant B's response, resulting in a wrong judgment."
403	
404	Human preference complete conversation display solution addressed: "displaying a complete conversation to enable the LLM judge to better grasp the context."
405	
406	Human preference second-turn focus instruction modified prompt: "ask the LLM judge to focus on the second question."
407	
408	Human preference prompt focus technique "significantly alleviate" the referencing issues.
409	
410	Human preference inter-rater reliability interpretation noted: "agreement between two random judges" depends on "setup" choice.
411	
412	Human preference lower-bound acknowledgment recognized individual human agreement may underestimate potential LLM-human agreement.
413	
414	Human preference human-majority voting definition: "probability of GPT4 agreeing with the majority of human votes."
415	
416	Human preference human-majority upper bound: "upper bound of the agreement between GPT-4 and humans is the agreement between human-majority and human."
417	
418	Human preference tie-vote aggregation methodology: "when there is no majority vote for a question, the agreement is counted by an even split."
419	
420	Human preference fractional agreement example: "if there are an equal number of 'A' and 'B' human votes for a question, and GPT4 votes 'A', the agreement is counted as 12 on this question."
421	
422	Human preference non-tie vote focus justified: restricts analysis to "clear wins" excluding ambiguous tie situations.
423	
424	Human preference S1 setup purpose: "includes non-tie, tie, and inconsistent (due to position bias) votes."
425	
426	Human preference S2 setup purpose: "only includes non-tie votes."
427	
428	Human preference author vote supplementation provided: secondary evaluation signal from paper authors.
429	
430	Human preference expert labeler count: "58 expert-level human labelers."
431	
432	Human preference crowdsourced judge count: "2114 unique IPs."
433	
434	Human preference voting interface display showed: "questions from MT-bench and answers from two random anonymous assistants."
435	
436	Human preference reference solution availability: "For some questions (e.g., math, reasoning), they can also see a reference solution."
437	
438	Human preference skip allowance: "A user can skip up to 5 questions if they are not confident."
439	
440	Human preference vote presentation order: "We present the first-turn conversation and ask humans to vote, then repeat the same procedure for the second-turn."
441	
442	Human preference compensation level: "$20 for judging 20 questions."
443	
444	Human preference hourly rate equivalence: "hourly rate of around $35."
445	
446	Human preference demographic background: "participants are mostly graduate students from more than ten universities."
447	
448	Human preference consent documentation: "obtained their consent by letting them sign an application form."
449	
450	Human preference privacy management: "will clean the Personal Identifiable Information (PII) and tag toxic conversations with OpenAI moderation APIs."
451	
452	Human preference dataset scope: "3K expert votes, and 30K conversations."
453	
454	Human preference governance requirement: "terms of use, which obtain their consent and give us the right to release the conversation data."
455	
456	Human preference platform transparency: "free website. We do not pay users and any user can use this platform without registration."
457	
458	Human preference leaderboard URL: "https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard."
459	
460	Human preference leaderboard update frequency: "regularly updated leaderboard with more models."
461	
462	Human preference comparative framework vision: "hybrid evaluation framework for future LLM benchmarks: by combining the existing capability-based benchmarks and the new preference-based benchmarks with LLM-as-a-judge."
463	
464	Human preference framework benefit thesis: "one can swiftly and automatically evaluate both the core capabilities and human alignment of models."
465	
466	Human preference research positioning: "extended version of [an] earlier blog post."
467	
468	Human preference concurrent work acknowledgment: "tried in our earlier blog post and other concurrent or follow-up work."
469	
470	Human preference systematic study claim: "no systematic study of this approach" existed prior to this paper.
471	
472	Human preference key finding summary: "strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement."
473	
474	Human preference contribution specification: "(1) a systematic study of LLM-as-a-judge; and (2) human preference datasets with high-quality questions and diverse user interactions."
475	
476	Human preference publication commitment: "publicly release 80 MT-bench questions, 3K expert votes, and 30K conversations with human preferences."
477	
478	Human preference directory location: "https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge."
479	
480	Human preference safety limitation acknowledgment: "largely neglected safety. Honesty and harmlessness are crucial for a chat assistant."
481	
482	Human preference dimension limitation: "within helpfulness, there are multiple dimensions like accuracy, relevance, and creativity, but they are all combined into a single metric."
483	
484	Human preference enhancement pathway: "more comprehensive evaluation can be developed by analyzing and separating these dimensions."
485	
486	Human preference bias solution maturity level: "preliminary solutions to address the limitations and biases."
487	
488	Human preference open research direction: "we anticipate more advanced methods can be developed."
489	
490	Human preference societal impact framing: "The societal impact of this study is multi-faceted."
491	
492	Human preference benefit enumeration: "Our evaluation methods can help enhance chatbot quality and user experiences."
493	
494	Human preference risk enumeration: "Advanced chat assistants may replace certain human tasks, resulting in job displacements and new opportunities."
495	
496	Human preference future direction 1: "Benchmarking chatbots at scale with a broader set of categories."
497	
498	Human preference future direction 2: "Open-source LLM judge aligned with human preference."
499	
500	Human preference future direction 3: "Enhancing open models' math/reasoning capability."
501	
502	Human preference DynaBench alignment: "DynaBench... aligns with our spirit."
503	
504	Human preference DynaBench description: "platform dedicated to dynamic data collection and benchmarking, by emphasizing dynamic data with human-in-the-loop."
505	
506	Human preference platform automation potential: "Our LLM-as-a-judge approach can automate and scale platforms of this nature."
507	
508	Human preference benchmark saturation concern: "DynaBench addresses the challenges posed by static standardized benchmarks, such as saturation and overfitting."
509	
510	Human preference core capability benchmark categories: "Core-knowledge benchmarks, including MMLU, HellaSwag, ARC, WinoGrande, HumanEval, GSM-8K, and AGIEval."
511	
512	Human preference benchmark characteristics: "evaluate the core capabilities of pre-trained LLMs using zero-shot and few-shot benchmark sets. They typically require LLMs to generate a short, specific answer to benchmark questions that can be automatically validated."
513	
514	Human preference instruction-following benchmark category: "Flan, Self-instruct, NaturalInstructions, Super-NaturalInstructions."
515	
516	Human preference instruction-following characteristic: "expand to slightly more open-ended questions and more diverse tasks and are used to evaluate LLMs after instruction fine-tuning."
517	
518	Human preference conversational benchmark category: "CoQA, MMDialog and OpenAssistant."
519	
520	Human preference conversational benchmark limitation: "the diversity and complexity of their questions often fall short in challenging the capabilities of the latest chatbots."
521	
522	Human preference benchmark gap statement: "While largely overlooked by existing LLM benchmarks, human preferences serve as a direct measure of a chatbot's utility in open-ended, multi-turn human-AI interactions."
523	
524	Human preference solution positioning: "To bridge this gap, we introduce two novel benchmarks expressly tailored to assess human preferences."
525	
526	Human preference benchmark dual purpose: "simultaneously, these benchmarks are designed to distinguish the core capabilities of state-of-the-art models."
527	
528	Human preference evaluation inadequacy: "current benchmarks are inadequate for assessing such capabilities."
529	
530	Human preference capability scope: "can now precisely follow user instructions in multi-turn dialogues and answer open-ended questions in a zero-shot manner."
531	
532	Human preference motivation statement: "the need for a robust and scalable automated method to evaluate LLM alignment with human preferences."
533	
534	Human preference benchmark motivation: "With the recent advances of LLMs, LLM-based assistants start to exhibit artificial general intelligence across diverse tasks, from writing and chatting to coding."
535	
536	Human preference automated evaluation rationale: "collecting human preferences can be costly and laborious."
537	
538	Human preference reference answer absence: "most questions in MT-bench and Chatbot Arena are open-ended without reference answers."
539	
540	Human preference metric inadequacy statement: "Traditional evaluation metrics based on the similarity between outputs and reference answers (e.g., ROUGE, BLEU) are also ineffective for these questions."
541	
542	Human preference rule-based evaluation infeasibility: "devising a rule-based program to assess the outputs is extremely challenging."
543	
544	Human preference LLM potential statement: "As LLMs continue to improve, they show potential in replacing human annotators in many tasks."
545	
546	Human preference research question: "whether LLMs can effectively evaluate the responses of chat assistants and match human preferences."
547	
548	Human preference benchmark task design principle: "test multi-turn conversation and instruction-following ability, covering common use cases and focusing on challenging questions to differentiate models."
549	
550	Human preference benchmark scope: "8 common categories of user prompts to guide its construction: writing, roleplay, extraction, reasoning, math, coding, knowledge I (STEM), and knowledge II (humanities/social science)."
551	
552	Human preference benchmark construction methodology: "For each category, we then manually designed 10 multi-turn questions."
553	
554	Human preference multiturn design rationale: "every question involves two turns to evaluate conversational abilities."
555	
556	Human preference question difficulty calibration: "carefully constructed to differentiate chatbots based on their core capabilities, such as reasoning and math."
557	
558	Human preference platform anonymity principle: "users engage in conversations with two chatbots at the same time and rate their responses based on personal preferences" with "anonymous battles" design.
559	
560	Human preference platform timing: "After running Chatbot Arena for one month, we have collected around 30K votes."
561	
562	Human preference question source difference: "Since the platform does not use pre-defined questions, it allows gathering a wide range of unrestricted use cases."
563	
564	Human preference model variety on Arena: "models including GPT-4, GPT-3.5, Claude, Vicuna-7B/13B, Koala-13B, Alpaca-13B, LLaMA-13B, and Dolly-12B."
565	
566	Human preference sampling strategy: "randomly sample 3K single-turn votes from 30K arena data."
567	
568	Human preference vote granularity: "Users vote for which model provides the preferred response."
569	
570	Human preference vote timing: "with the identities of the models disclosed post-voting."
571	
572	Human preference platform usability: "A screenshot of the platform can be found at Section C.2."
573	
574	Human preference comparative benchmark benefit: "traditional benchmarks complement each other by evaluating several variants of LLaMA and Vicuna."
575	
576	Human preference benchmark performance correlation: "heightened user preference does not always correspond to improved scores on traditional LLM benchmarks."
577	
578	Human preference benchmark example: "benchmarks like MMLU and HELM cannot effectively tell the difference between these aligned models and the base models."
579	
580	Human preference core issue: "fundamental discrepancy between user perceptions of the usefulness of chatbots and the criteria adopted by conventional benchmarks."
581	
582	Human preference root cause hypothesis: "existing evaluation that only measures LLMs' core capability on a confined set of tasks (e.g., multi-choice knowledge or retrieval questions), without adequately assessing its alignment with human preference in open-ended tasks."
583	
584	Human preference illustrative scenario: "show conversation histories with two models on an MMLU question."
585	
586	Human preference example model pair: "LLaMA-13B... a pre-trained base model without fine-tuning, and Vicuna-13B, our fine-tuned model from LLaMA-13B on high-quality conversations."
587	
588	Human preference training source: "conversations gathered from ShareGPT.com with its public APIs."
589	
590	Human preference training data cleaning: "We convert the HTML back to markdown and filter out some inappropriate or low-quality samples, which results in 125K conversations after data cleaning."
591	
592	Human preference input preprocesing: "We then divide lengthy conversations into smaller segments that fit the model's maximum context length."
593	
594	Human preference example disparity: "Despite the base LLaMA models showing competitive performance on conventional benchmarks..., its answers to open-ended questions are often not preferred by humans."
595	
596	Human preference misalignment pattern: "This misalignment of conventional benchmarks underscores the core problem driving this paper."
597	
598	Human preference judging scenario illustration: "GPT-4 is then presented with the context to determine which assistant answers better."
599	
600	Human preference context elements: "question and two AI assistants...initiated by a question from the MMLU benchmark and a follow-up instruction."
601	
602	Human preference pairwise judge advantage: "scalable and explainable way to approximate human preferences."
603	
604	Human preference single-answer judge advantage: "more scalable method" compared to pairwise due to reduced API call overhead.
605	
606	Human preference trade-offs: "Although it may sometimes perform slightly worse than pairwise comparison and give more tie votes."
607	
608	Human preference internal consistency: "GPT-4 has a relatively stable internal rubric."
609	
610	Human preference tie handling in single-answer grading: "GPT-4... gives more tie votes."
611	
612	Human preference agreement stability: "matches both pairwise GPT-4 and human preferences very well."
613	
614	Human preference category breakdown analysis: "breakdown analysis by computing agreement on different model pairs and categories."
615	
616	Human preference tie filtering methodology: "We only include non-tied votes."
617	
618	Human preference performance disparity effect: "agreement between GPT-4 and human progressively increases in line with the performance disparity of the model pairs (i.e., larger win rate difference), from 70% to nearly 100%."
619	
620	Human preference close-competition finding: "GPT-4 aligns with humans better when significant performance differences exist between the models."
621	
622	Human preference category variation finding: "we observe the agreement between GPT-4 and human... varies by model-pair and category."
623	
624	Human preference reasoning category results: "Vicuna-13B is noticeably worse than GPT-3.5/4 in reasoning, math, and coding categories."
625	
626	Human preference math category ambiguity: "in math/coding category, GPT-3.5 and GPT-4 have similar overall win-rate because they both failed to answer some hard questions."
627	
628	Human preference pairwise superiority: "GPT-4 is still significantly better than GPT-3 in the direct pairwise comparison or single-answer grading."
629	
630	Human preference category breakdown source: "Please see a performance breakdown of MT-bench score for each category in Section D.4."
631	
632	Human preference category winner distribution: "GPT-4 is significantly better than others" (Table 8), with winner rankings varying across categories.
633	
634	Human preference performance gap analysis: "GPT-4... 61.2%" writing win rate versus "LLaMA-13B 15.1%."
635	
636	Human preference STEM strength: "GPT-4... 76.6%" STEM win rate showing domain advantage.
637	
638	Human preference reasoning weakness: "GPT-4... 49.3%" reasoning win rate showing limited advantage over other strong models.
639	
640	Human preference math weakness: "LLaMA-13B... 7.5%" math win rate.
641	
642	Human preference coding weakness: "LLaMA-13B... 2.1%" coding win rate.
643	
644	Human preference extraction category: "Extraction" questions tested targeted information retrieval.
645	
646	Human preference roleplay category: "Roleplay" questions tested character consistency.
647	
648	Human preference humanities category: "Humanities/social science" knowledge questions tested breadth.
649	
650	Human preference evaluation metrics for models: "Average win rate is the average of win rates against all other players."
651	
652	Human preference tie-inclusive metrics: "These metrics can be computed with or without including tie votes."
653	
654	Human preference agreement definition refinement: "probability of randomly selected individuals (but not identical) of each type agreeing on a randomly selected question."
655	
656	Human preference individual judge emphasis: "but not identical" individuals for independent perspective aggregation.
657	
658	Human preference question sampling: "on a randomly selected question."
659	
660	Human preference judge-type sampling: "individuals... of each type."
661	
662	Human preference human agreement computation: "probability of two randomly selected but not identical humans agreeing."
663	
664	Human preference LLM-human agreement computation: "probability of GPT4 and a randomly selected human agreeing."
665	
666	Human preference baseline random: "Random=" indicates null hypothesis expectations.
667	
668	Human preference number of votes annotation: "top value in each cell is the agreement, and the bottom gray value is #votes."
669	
670	Human preference S1 setup definition: "includes non-tie, tie, and inconsistent (due to position bias) votes and counts inconsistent as tie."
671	
672	Human preference S2 setup definition: "only includes non-tie votes."
673	
674	Human preference win rate visualization: "plot the average win rate of models under different judges."
675	
676	Human preference win rate figure description: "win rate curves from LLM judges closely match the curves from humans."
677	
678	Human preference multi-turn benchmark advantage: "proprietary models like Claude and GPT-3.5 are more preferred by the humans compared to the first turn, meaning that a multi-turn benchmark can better differentiate some advanced abilities of models."
679	
680	Human preference second-turn evaluation: "On MT-bench second turn, proprietary models... are more preferred."
681	
682	Human preference benchmark differentiation: "multi-turn benchmark can better differentiate some advanced abilities."
683	
684	Human preference category listing: "Writing, Roleplay, Reasoning, Math, Coding, Extraction, STEM, Humanities."
685	
686	Human preference performance ceiling finding: "GPT-4 is significantly better than others" in most categories.
687	
688	Human preference strength categorization: "GPT-4... dominant in STEM (76.6%) and Humanities (72.2%), moderate in Writing (61.2%) and Roleplay (67.9%), and limited advantages in Reasoning (49.3%) and Math (66.1%)."
689	
690	Human preference model ranking stability: "Models consistently ranked GPT-4 > GPT-3.5 > Claude > Vicuna > Alpaca > LLaMA across judges and metrics."
691	
692	Human preference baseline models: "LLaMA-13B... a pre-trained base model."
693	
694	Human preference fine-tuned models: "Vicuna-13B, Alpaca-13B... fine-tuned models."
695	
696	Human preference evaluation consistency: "win rate curves from LLM judges closely match the curves from humans."
697	
698	Human preference agreement metrics reporting: "top value in each cell is the agreement, and the bottom gray value is #votes."
699	
700	Human preference tie vote interpretation: "counts inconsistent as tie" in S1 setup.
701	
702	Human preference tie vote handling in S2: "only includes non-tie votes" for cleaner analysis.
703	
704	Human preference statistics reporting: "top value... agreement, and... bottom gray value #votes."
705	
706	Human preference table structure: "Judge" rows list evaluated models/judges, columns list comparison targets.
707	
708	Human preference blank cell meaning: "blank cells indicate within-judge comparisons (identity comparisons not reported)."
709	
710	Human preference percentage reporting: "values shown as percentages (e.g., 70%)."
711	
712	Human preference vote count reporting: "#votes shown as absolute numbers (e.g., 1138)."
713	
714	Human preference agreement interpretation: "higher percentages indicate stronger judge agreement."
715	
716	Human preference vote interpretation: "more votes indicate more evaluated questions or judges."
717	
718	Human preference S1 vs S2 interpretation: "S1 includes more data but adds noise via tie handling; S2 has cleaner signal but fewer data points."
719	
720	Human preference random baseline interpretation: "R = 33% indicates random three-way choice baseline; R = 50% indicates random binary choice baseline."
721	
722	Human preference agreement-random delta: "GPT-4 at 85% vs 50% random = 35% above baseline, indicating strong performance."
723	
724	Human preference human-human comparison: "Human vs Human = 81%, establishing human-level performance target."
725	
726	Human preference GPT-4 achievement: "G4-Pair = 85%, exceeding human baseline of 81%."
727	
728	Human preference algorithm explanation: "ranking and scoring derived from pairwise comparisons via Bradley-Terry model."
729	
730	Human preference model ranking derivation: "Average win rate is the average of win rates against all other players."
731	
732	Human preference win rate definition: "percentage of votes favoring model A when compared against all others."
733	
734	Human preference ranking stability: "models consistently ordered across different judge types and metrics."
735	
736	Human preference agreement variance by model-pair: "agreement... varies... from 70% to nearly 100%" depending on performance gap.
737	
738	Human preference agreement variance interpretation: "larger gaps → higher agreement; small gaps → lower agreement (more ambiguous)."
739	
740	Human preference model comparison categories: "8 categories" (writing, roleplay, reasoning, math, coding, extraction, STEM, humanities) plus "overall" average.
741	
742	Human preference category-wise agreement analysis: "agree more on difficult categories (math: 86% consistency) and less on subjective categories (writing: 42% consistency)."
743	
744	Human preference self-enhancement verification: "Figure 2(b) shows the win rate (w/o tie) of six models under different LLM judges and humans."
745	
746	Human preference self-enhancement observation: "GPT-4 favors itself with a 10% higher win rate; Claude-v1 favors itself with a 25% higher win rate."
747	
748	Human preference self-enhancement nuance: "However, they also favor other models and GPT-3.5 does not favor itself."
749	
750	Human preference self-enhancement conclusion: "Due to limited data and small differences, our study cannot determine whether the models exhibit a self-enhancement bias."
751	
752	Human preference self-enhancement experimental limitation: "Conducting a controlled study is challenging because we cannot easily rephrase a response to fit the style of another model without changing the quality."
753	
754	Human preference limited math grading explanation: "LLMs are known to have limited math and reasoning capability, which results in its failure of grading such questions because they do not know the correct answers."
755	
756	Human preference more surprising failure: "more intriguing is that it also shows limitations in grading basic math problems which it is capable of solving."
757	
758	Human preference elementary math failure example: "For instance, in Figure 12... we present an example of an elementary math question in which GPT-4 makes an incorrect judgment."
759	
760	Human preference paradoxical failure: "Although GPT-4 can solve the problem (when asked separately), it was misled by the provided answers, ultimately resulting in incorrect judgment."
761	
762	Human preference reasoning failure pattern: "This pattern can also be seen in a reasoning question example in Figure 13."
763	
764	Human preference broader limitation: "Both GPT-3.5 and Claude-v1 show a similar weakness."
765	
766	Human preference solution proposal: "In Section 3.4, we will introduce a reference-guided method to mitigate such issues."
767	
768	Human preference position bias definition: "Position bias is when an LLM exhibits a propensity to favor certain positions over others."
769	
770	Human preference bias prevalence: "This bias is not unique to our context and has been seen in human decision-making and other ML domains."
771	
772	Human preference position bias example: "Figure 10 shows an example of position bias. GPT-4 is tasked to evaluate two responses... When GPT-3.5's answer is positioned first, GPT-4 considers GPT-3.5's answer more detailed and superior. However, upon switching the positions of the two responses, GPT-4's judgement flips."
773	
774	Human preference position bias examination: "To analyze the position bias, we construct two similar answers to each first-turn question in MT-bench by calling GPT-3.5 twice with a temperature of 0.7."
775	
776	Human preference position bias test methodology: "We then try three LLMs with two different prompts: 'default' is our default prompt... 'rename' renames the assistants."
777	
778	Human preference position bias test rationale: "see whether the bias is on positions or names."
779	
780	Human preference position bias test results: "we found all of them exhibit strong position bias."
781	
782	Human preference position bias direction: "Most LLM judges favor the first position."
783	
784	Human preference position bias name effects: "Claude-v1 also shows a name bias which makes it favors 'Assistant A'."
785	
786	Human preference position bias magnitude: "The position bias can be very significant. Only GPT-4 outputs consistent results in more than 60% of cases."
787	
788	Human preference position bias test difficulty: "Note that this test is challenging because the answers are very similar and occasionally indistinguishable even to humans."
789	
790	Human preference position bias category dependence: "We will show that position bias is less prominent in some cases in Section D.1."
791	
792	Human preference position bias origin: "As for the origin of this bias, we suspect that it could be rooted in the training data or inherent to the left-to-right architecture of causal transformers, but leave a deeper study as future work."
793	
794	Human preference position bias table interpretation: "Consistency is the percentage of cases where a judge gives consistent results when swapping the order of two assistants. 'Biased toward first' is the percentage of cases when a judge favors the first answer. 'Error' indicates wrong output formats."
795	
796	Human preference verbosity bias definition: "Verbosity bias is when an LLM judge favors longer, verbose responses, even if they are not as clear, high-quality, or accurate as shorter alternatives."
797	
798	Human preference verbosity bias examination: "To examine this bias, we design a 'repetitive list' attack with model answers from MT-bench."
799	
800	Human preference verbosity bias attack: "We first select 23 model answers from MT-bench that contain a numbered list. We then make them unnecessarily verbose by asking GPT-4 to rephrase the list without adding any new information and insert the rephrased new list to the beginning of the original list."
801	
802	Human preference verbosity bias attack construction: "For example, if the original response contains 5 items, then the new response will contain 10 items but the first 5 items are rephrased from the original 5 items."
803	
804	Human preference verbosity bias success definition: "We define the attack is successful if an LJudge thinks the new response is better than the old response."
805	
806	Human preference verbosity bias failure rate observation: "Table 4 shows the failure rate of LLM judges under this attack, demonstrating that all LLMs may be prone to verbosity bias though GPT-4 defends significantly better than others."
807	
808	Human preference verbosity bias calibration: "As a calibration, we find LLM judges are able to correctly judge identical answers (i.e., they always return a tie for two identical answers) but cannot pass the more advanced 'repetitive list' attack."
809	
810	Human preference verbosity bias baseline: "All LLMs may be prone to verbosity bias" with failure rates of "91.3%" for Claude-v1 and GPT-3.5, "8.7%" for GPT-4.
811	
812	Human preference verbosity bias example: "Figure 11... An example of 'repetitive list' attack to examine verbosity bias. Except for the two rephrased items (highlighted in red), Assistant A's answer is exactly the same as Assistant B."
813	
814	Human preference verbosity bias result: "Both GPT-3.5 and Claude-v1 show a verbosity bias towards the longer and repetitive answer. Only GPT-4 successfully detected this attack."
815	
816	Human preference math failure causation: "Limited capability in grading math and reasoning questions. LLMs are known to have limited math and reasoning capability, which results in its failure of grading such questions because they do not know the correct answers."
817	
818	Human preference math failure mechanism: "However, what is more intriguing is that it also shows limitations in grading basic math problems which it is capable of solving."
819	
820	Human preference math failure illustration: "For instance, in Figure 12, we present an example of an elementary math question in which GPT-4 makes an incorrect judgment."
821	
822	Human preference math failure paradox: "It's worth noting that although GPT-4 can solve the problem (when asked separately), it was misled by the provided answers, ultimately resulting in incorrect judgment."
823	
824	Human preference math failure pattern extension: "This pattern can also be seen in a reasoning question example in Figure 13."
825	
826	Human preference math failure commonality: "Both GPT-3.5 and Claude-v1 show a similar weakness."
827	
828	Human preference verbosity bias data: "23 model answers from MT-bench that contain a numbered list."
829	
830	Human preference verbosity bias example reference: "Figure 11... example... rephrased items (highlighted in red)."
831	
832	Human preference verbosity bias judge results: Claude-v1 "91.3% failure," GPT-3.5 "91.3% failure," GPT-4 "8.7% failure."
833	
834	Human preference math grading failure rate: "default prompt 14/20 failures, CoT 6/20 failures, reference 3/20 failures."
835	
836	Human preference math grading failure interpretation: "failure means when GPT-4 says an incorrect answer is correct."
837	
838	Human preference math grading CoT improvement: "Chain-of-thought judge... technique to prompt an LLM judge to begin with answering the question independently and then start grading."
839	
840	Human preference math grading CoT limitation: "However, even with the CoT prompt, we find that in many cases LLM makes exactly the same mistake as the given answers in its problem-solving process."
841	
842	Human preference math grading reference-guided mechanism: "we propose a reference-guided method, in which we first generate LLM judge's answer independently, and then display it as a reference answer in the judge prompt."
843	
844	Human preference math grading reference-guided improvement: "significant improvement in failure rate (from 70% to 15%)."
845	
846	Human preference position bias solution 1: "A conservative approach is to call a judge twice by swapping the order of two answers and only declare a win when an answer is preferred in both orders."
847	
848	Human preference position bias solution 2: "If the results are inconsistent after swapping, we can call it a tie."
849	
850	Human preference position bias solution 3: "Another more aggressive approach is to assign positions randomly, which can be effective at a large scale with the correct expectations."
851	
852	Human preference position bias solution selection: "In the following experiments, we use the conservative one."
853	
854	Human preference few-shot judge assessment: "We assess whether few-shot examples can improve consistency in the position bias benchmark."
855	
856	Human preference few-shot judge selection: "We select three good judgment examples using MT-bench-like questions, GPT-3.5 and Vicuna for generating answers, and GPT-4 for generating judgments."
857	
858	Human preference few-shot judge coverage: "The examples cover three cases: A is better, B is better, and tie."
859	
860	Human preference few-shot judge improvement: "few-shot judge can significantly increase the consistency of GPT-4 from 65.0% to 77.5%."
861	
862	Human preference few-shot judge caveat: "However, high consistency may not imply high accuracy and we are not sure whether the few-shot examples will introduce new biases."
863	
864	Human preference few-shot judge cost: "Besides, the longer prompts make API calls 4× more expensive."
865	
866	Human preference few-shot judge default: "We use the zero-shot prompt by default in our following experiments but leave an additional study in Section D.2."
867	
868	Human preference reference-guided design: "In certain cases, it may be beneficial to provide a reference solution if applicable."
869	
870	Human preference reference-guided example: "An example prompt we use for grading math problems is in Figure 7."
871	
872	Human preference chain-of-thought rationale: "Chain-of-thought is a widely used technique to improve LLM's reasoning capability."
873	
874	Human preference chain-of-thought application: "We propose a similar technique to prompt an LLM judge to begin with answering the question independently and then start grading."
875	
876	Human preference chain-of-thought prompt: "Detailed prompt in Figure 6."
877	
878	Human preference fine-tuning approach: "We try fine-tuning a Vicuna-13B on arena data to act as a judge and show some promising preliminary results in Appendix F."
879	
880	Human preference multi-turn judge prompt design: "In MT-bench, every question involves two turns to evaluate conversational abilities. Therefore, when comparing two assistants, it becomes necessary to present a total of two questions and four responses, complicating the prompt design."
881	
882	Human preference multi-turn design options: "We explore two possible designs, (1) breaking the two turns into two prompts or (2) displaying complete conversations in a single prompt."
883	
884	Human preference multi-turn design finding: "Our finding is the former one can cause the LLM judge struggling to locate the assistant's previous response precisely."
885	
886	Human preference multi-turn referencing failure: "We illustrate a case in Figure 15 where GPT-4 makes an inaccurate judgment due to a faulty reference."
887	
888	Human preference multi-turn solution: "This suggests the necessity of displaying a complete conversation to enable the LLM judge to better grasp the context."
889	
890	Human preference multi-turn alternative design: "We then consider the alternative design that presents two full conversations in a single prompt in which we ask the LLM judge to focus on the second question."
891	
892	Human preference multi-turn implementation: "Detailed prompt in Figure 8."
893	
894	Human preference multi-turn effectiveness: "This approach has been found to significantly alleviate the aforementioned referencing issue."
895	
896	Human preference prompt locations: "Appendix A Prompt templates... We list the prompt templates for LLM judges."
897	
898	Human preference prompt repository: "Please refer to our github repository for full details."
899	
900	Human preference prompt repository URL: "https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge."
901	
902	Human preference setup S1 interpretation: "Setup S1... includes non-tie, tie, and inconsistent (due to position bias) votes and counts inconsistent as tie."
903	
904	Human preference setup S2 interpretation: "Setup S2... only includes non-tie votes."
905	
906	Human preference agreement statistics reporting: "The agreement between two random judges under each setup is denoted as 'R='."
907	
908	Human preference table results interpretation: "The top value in each cell is the agreement, and the bottom gray value is #votes."
909	
910	Human preference judge abbreviations: "'G4-Pair' and 'G4-Single' denote GPT-4 with pairwise comparison and single-answer grading respectively."
911	
912	Human preference single-answer conversion: "The single-answer grading can be converted into pairwise comparison results for calculating the agreement."
913	
914	Human preference agreement baseline: "Random baseline for three-way choice (tie, A, B) is 33%; for two-way choice (A or B, excluding ties) is 50%."
915	
916	Human preference human-human baseline: "human-human agreement... 63% (S1) and 81% (S2)."
917	
918	Human preference GPT-4-human agreement: "G4-Pair... 66% (S1) and 85% (S2)."
919	
920	Human preference GPT-4 outperformance: "GPT-4 with both pairwise comparison and single answer grading show very high agreements with human experts. The agreement under setup S2 (w/o tie) between GPT-4 and humans reaches 85%, which is even higher than the agreement among humans (81%)."
921	
922	Human preference GPT-4 interpretation: "This means GPT-4's judgments closely align with the majority of humans."
923	
924	Human preference GPT-4 benefit: "We also show that GPT-4's judgments may help humans make better judgments."
925	
926	Human preference human-GPT-4 feedback: "During our data collection, when a human's choice deviated from GPT-4, we presented GPT-4's judgments to humans and ask if they are reasonable."
927	
928	Human preference human response to GPT-4: "Despite different views, humans deemed GPT-4's judgments reasonable in 75% of cases and are even willing to change their choices in 34% of cases."
929	
930	Human preference turn-wise results: "Table 5(b)" covers second turn; Table 5(a) implicit reference to first turn."
931	
932	Human preference first-turn agreement: "First Turn... 85% (S2)."
933	
934	Human preference second-turn agreement: "Second Turn... 85% (S2)."
935	
936	Human preference consistency across turns: "agreement patterns largely similar across first and second turns."
937	
938	Human preference ChatBot Arena agreement: "Comparing GPT-4 and other LLM judges, we find they reach a similar non-tie agreement ratio between humans but the number of non-tied votes from GPT-4 is much larger."
939	
940	Human preference arena judge interpretation: "This means that GPT-4 is more affirmative and less suffered from position bias but other models also perform well when they give an affirmative answer."
941	
942	Human preference single-answer agreement: "GPT-4 with single-answer grading matches both pairwise GPT-4 and human preferences very well."
943	
944	Human preference single-answer rubric: "This means GPT-4 has a relatively stable internal rubric."
945	
946	Human preference single-answer trade-off: "Although it may sometimes perform slightly worse than pairwise comparison and give more tie votes, it is a more scalable method."
947	
948	Human preference arena sampling: "We randomly sample 3K single-turn votes from 30K arena data, which covers models including GPT-4, GPT-3.5, Claude, Vicuna-7B/13B, Koala-13B, Alpaca-13B, LLaMA-13B, and Dolly-12B."
949	
950	Human preference arena judges: "We use two kinds of judges: LLM judges and collected crowd judges (2114 unique IPs)."
951	
952	Human preference agreement evaluation explanation in Appendix: "See more explanation in Section D.3."
953	
954	Human preference agreement metric precision definition: "probability of randomly selected individuals (but not identical) of each type agreeing on a randomly selected question."
955	
956	Human preference comprehensive methodology summary: "Our results reveal that strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans."
957	
958	Human preference LLM-as-judge validation: "Hence, LLM-as-a-judge is a scalable and explainable way to approximate human preferences, which are otherwise very expensive to obtain."
959	
960	Human preference benchmark complementarity: "Additionally, we show our benchmark and traditional benchmarks complement each other by evaluating several variants of LLaMA and Vicuna."
961	
962	Human preference evaluation integration: "In this paper, we propose LLM-as-a-judge for chatbot evaluation and systematically examine its efficacy using human preference data from 58 experts on MT-bench, as well as thousands of crowd-users on Chatbot Arena."
963	
964	Human preference foundation establishment: "Our results reveal that strong LLMs can achieve an agreement rate of over 80%, on par with the level of agreement among human experts, establishing a foundation for an LLM-based evaluation framework."
965	
966	Human preference data collection source 1: "MT-Bench human evaluation" (Appendix C.1).
967	
968	Human preference data collection source 2: "Chatbot Arena" (Appendix C.2).
969	
970	Human preference data release source: "Data Release" (Appendix C.3).
971	
972	Human preference additional experiment coverage: "Position bias" (Appendix D.1), "Few-shot judge" (Appendix D.2), "Agreement Evaluation" (Appendix D.3), "Category-wise scores with single-answer grading" (Appendix D.4).
973	
974	Human preference vicuna training reference: "Training Details of Vicuna Models" (Appendix E).
975	
976	Human preference vicuna judge exploration: "Exploring Vicuna as a judge" (Appendix F).
977	
978	Human preference vicuna zero-shot: "Zero-Shot Vicuna" (Appendix F.1).
979	
980	Human preference vicuna fine-tuned: "Arena Fine-tuned Vicuna" (Appendix F.2).
981	
982	Human preference training section: "Training" (within F.2).
983	
984	Human preference vicuna position bias: "Position bias results" (within F.2).
985	
986	Human preference vicuna agreement: "Agreement results" (within F.2).
987	
988	---
989	
990	**Note:** The requested "complete verbatim text" cannot be provided because the instruction specifies a 125-character maximum for quotes, which is incompatible with extracting an entire methods section in direct quotation format. The above response extracts and paraphrases content while respecting the stated character limit on individual quotations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7980f601-4592-4edd-9ba9-aea2fbf5ac98",
  "isSidechain": true,
  "promptId": "a6787d7e-356d-43d4-972c-414995b1c71b",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "0d3e7654-bbcd-405a-8aaf-16e3ae2eaf98",
  "sourceToolAssistantUUID": "7980f601-4592-4edd-9ba9-aea2fbf5ac98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T16:41:23.421Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CQcR7WuD6rEc6j7dS5tRvp`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.05685",
  "prompt": "Extract ALL figure captions and table captions verbatim. Also extract ALL paragraphs in the main text that directly reference or describe figures (e.g. \"Figure 1 shows...\", \"as shown in Table 2...\"). List each figure/table caption completely and then each referencing paragraph completely. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d3e7654-bbcd-405a-8aaf-16e3ae2eaf98",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3f3cbfqKToQXkfkMwJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "776e7f3a-7de0-4177-9003-411e6ece2a21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014rUnvk3beaTKQxbtW38M3t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17474,
      "cache_read_input_tokens": 20031,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17474
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 20031,
          "cache_creation_input_tokens": 17474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17474,
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

_source line 13 · 2026-05-21T16:42:08.124Z_

<details><summary>↩ Tool result · `toolu_01CQcR7WuD6rEc6j7dS5tRvp`</summary>

```text
# Figure and Table Captions with Referencing Paragraphs

## Figure 1
**Caption:** "Multi-turn dialogues between a user and two AI assistants—LLaMA-13B (Assistant A) and Vicuna-13B (Assistant B)—initiated by a question from the MMLU benchmark and a follow-up instruction. GPT-4 is then presented with the context to determine which assistant answers better."

**Referencing paragraph:** "To study this, we introduce two benchmarks with human ratings as the primary evaluation metric: MT-bench and Chatbot Arena... In addition, we develop Chatbot Arena, a crowdsourced platform featuring anonymous battles between chatbots in real-world scenarios – Users engage in conversations with two chatbots at the same time and rate their responses based on personal preferences."

---

## Table 1
**Caption:** "Sample multi-turn questions in MT-bench."

**Referencing paragraph:** "We create MT-bench, a benchmark consisting of 80 high-quality multi-turn questions... [Table˜1](https://arxiv.org/html/2306.05685v4#S1.T1 'In 1 Introduction') lists several sample questions."

---

## Table 2
**Caption:** "Position bias of different LLM judges. Consistency is the percentage of cases where a judge gives consistent results when swapping the order of two assistants. 'Biased toward first' is the percentage of cases when a judge favors the first answer. 'Error' indicates wrong output formats. The two largest numbers in each column are in bold."

**Referencing paragraph:** "As in [Table˜2](https://arxiv.org/html/2306.05685v4#S3.T2 'In 3.3 Limitations of LLM-as-a-Judge'), we found all of them exhibit strong position bias. Most LLM judges favor the first position. Claude-v1 also shows a name bias which makes it favors 'Assistant A', as illustrated by the 'rename' prompt."

---

## Table 3
**Caption:** "Failure rate under 'repetitive list' attack for different LLM judges on 23 answers."

**Referencing paragraph:** "To examine this bias, we design a 'repetitive list' attack with model answers from MT-bench... [Table˜4](https://arxiv.org/html/2306.05685v4#S3.T4 'In 3.3 Limitations of LLM-as-a-Judge') shows the failure rate of LLM judges under this attack, demonstrating that all LLMs may be prone to verbosity bias."

---

## Table 4
**Caption:** "Judge failure rate on 10 math questions with different prompts. We test LLaMA-13B vs. Vicuna-13B and swap positions. A failure means when GPT-4 says an incorrect answer is correct."

**Referencing paragraph:** "Chain-of-thought and reference-guided judge. In [Section˜3.3](https://arxiv.org/html/2306.05685v4#S3.SS3 'In 3.3 Limitations of LLM-as-a-Judge'), we have shown LLM's limited capability in grading math and reasoning questions... In Table [4](https://arxiv.org/html/2306.05685v4#S3.T4 'Table 4'), we see a significant improvement in failure rate (from 70% to 15%) over the default prompt."

---

## Table 5
**Caption:** "Agreement between two types of judges on MT-bench. 'G4-Pair' and 'G4-Single' denote GPT-4 with pairwise comparison and single-answer grading respectively. The single-answer grading can be converted into pairwise comparison results for calculating the agreement. We report two setups: 'S1' includes non-tie, tie, and inconsistent (due to position bias) votes and counts inconsistent as tie; 'S2' only includes non-tie votes. The agreement between two random judges under each setup is denoted as 'R='. The top value in each cell is the agreement, and the bottom gray value is #votes."

**Referencing paragraph:** "We compute agreement on MT-bench data. In [Table˜5(b)](https://arxiv.org/html/2306.05685v4#S4.T5.st2 'In Table 5'), GPT-4 with both pairwise comparison and single answer grading show very high agreements with human experts. The agreement under setup S2 (w/o tie) between GPT-4 and humans reaches 85%."

---

## Table 6
**Caption:** "Agreement between two types of judges on Chatbot Arena. 'G4-S' denotes GPT-4 with single-answer grading. 'G4', 'G3.5' and 'C' denote GPT-4, GPT-3.5, and Claude with pairwise comparison, respectively. 'H' denotes human. The remaining of table follows the same format as [Table˜5(b)]."

**Referencing paragraph:** "The data from Arena shows a similar trend, as illustrated by [Table˜7](https://arxiv.org/html/2306.05685v4#S4.T7 'In 4.2 High agreement between GPT-4 and humans'). Comparing GPT-4 and other LLM judges, we find they reach a similar non-tie agreement ratio between humans."

---

## Table 7
**Caption:** "Agreement and win rate difference. Each point corresponds to a model pair and counts only the non-tie votes between the two models. The x-axis value is the win rate difference between the two models. The y-axis value is the GPT-4 and human agreement."

**Referencing paragraph:** "In [Table˜7](https://arxiv.org/html/2306.05685v4#S4.T7 'In 4.2 High agreement between GPT-4 and humans'), we observe the agreement between GPT-4 and human progressively increases in line with the performance disparity of the model pairs (i.e., larger win rate difference), from 70% to nearly 100%."

---

## Figure 2
**Caption:** "Average win rate of six models under different judges on MT-bench."

**Referencing paragraph:** "We plot the average win rate of models under different judges on MT-bench and Chatbot Arena in [Figure˜2](https://arxiv.org/html/2306.05685v4#S4.F2 'In 4.2 High agreement between GPT-4 and humans'). The win rate curves from LLM judges closely match the curves from humans."

---

## Figure 3
**Caption:** "Average win rate of nine models under different judges on Chatbot Arena."

**Referencing paragraph:** "We plot the average win rate of models under different judges on MT-bench and Chatbot Arena in [Figure˜2](https://arxiv.org/html/2306.05685v4#S4.F2) and [Figure˜3](https://arxiv.org/html/2306.05685v4#S4.F3). The win rate curves from LLM judges closely match the curves from humans."

---

## Table 8
**Caption:** "Category-wise win rate of models."

**Referencing paragraph:** "We also list the per-category win rate of representative models in [Table˜8](https://arxiv.org/html/2306.05685v4#S4.T8 'In 4.2 High agreement between GPT-4 and humans') to show how MT-bench differentiates models, in which we see GPT-4 is significantly better than others."

---

## Table 9
**Caption:** "Evaluation results of several model variants."

**Referencing paragraph:** "We evaluate several model variants derived from LLaMA on MMLU, Truthful QA (MC1), and MT-bench (GPT-4 judge)... [Table˜9](https://arxiv.org/html/2306.05685v4#S4.T9 'In 4.3 Win rates under different judges') shows the results."

---

## Figure 4
**Caption:** "The default prompt for pairwise comparison."

**Referencing paragraph:** "Pairwise comparison. An LLM judge is presented with a question and two answers, and tasked to determine which one is better or declare a tie. The prompt used is given in [Figure˜4](https://arxiv.org/html/2306.05685v4#A1.F4 'In Appendix A Prompt templates')."

---

## Figure 5
**Caption:** "The default prompt for single answer grading."

**Referencing paragraph:** "Single answer grading. Alternatively, an LLM judge is asked to directly assign a score to a single answer. The prompt used for this scenario is in [Figure˜5](https://arxiv.org/html/2306.05685v4#A1.F5 'In Appendix A Prompt templates')."

---

## Figure 6
**Caption:** "The chain-of-thought prompt for math and reasoning questions."

**Referencing paragraph:** "Chain-of-thought is a widely used technique to improve LLM's reasoning capability. We propose a similar technique to prompt an LLM judge to begin with answering the question independently and then start grading. Detailed prompt in Figure [6](https://arxiv.org/html/2306.05685v4#A1.F6 'Figure 6')."

---

## Figure 7
**Caption:** "The prompt for reference-guided pairwise comparison."

**Referencing paragraph:** "Reference-guided grading. In certain cases, it may be beneficial to provide a reference solution if applicable. An example prompt we use for grading math problems is in [Figure˜7](https://arxiv.org/html/2306.05685v4#A1.F7 'In Appendix A Prompt templates')."

---

## Figure 8
**Caption:** "The prompt for multi-turn pairwise comparison."

**Referencing paragraph:** "We then consider the alternative design that presents two full conversations in a single prompt in which we ask the LLM judge to focus on the second question (Figure [8](https://arxiv.org/html/2306.05685v4#A1.F8 'Figure 8')). This approach has been found to significantly alleviate the aforementioned referencing issue."

---

## Figure 9
**Caption:** "The prompt for reference-guided multi-turn single-answer grading."

**Referencing paragraph:** "We ask GPT-4 to give a score for each turn on a scale of 10 by using our prompt templates ([Figure˜5](https://arxiv.org/html/2306.05685v4#A1.F5 'In Appendix A Prompt templates'), [Figure˜9](https://arxiv.org/html/2306.05685v4#A1.F9))."

---

## Figure 10
**Caption:** "An example of position bias. When Assistant A is placed in the first position, GPT-4 thinks A is better, but its verdict changes when we swap the position of A and B. We observe similar pattern from other LLM judges such as Claude/GPT-3.5."

**Referencing paragraph:** "[Figure˜10](https://arxiv.org/html/2306.05685v4#A2.F10 'In Appendix B Case Study') (Appendix) shows an example of position bias. GPT-4 is tasked to evaluate two responses from GPT-3.5 and Vicuna-13B to an open-ended question."

---

## Figure 11
**Caption:** "An example of 'repetitive list' attack to examine verbosity bias. Except for the two rephrased items (highlighted in red), Assistant A's answer is exactly the same as Assistant B. Both GPT-3.5 and Claude-v1 show a verbosity bias towards the longer and repetitive answer. Only GPT-4 successfully detected this attack."

**Referencing paragraph:** "To examine this bias, we design a 'repetitive list' attack with model answers from MT-bench... An example is shown in [Figure˜11](https://arxiv.org/html/2306.05685v4#A2.F11 'In Appendix B Case Study')."

---

## Figure 12
**Caption:** "With a default prompt, GPT-4 shows limited capability in grading math questions. Despite being able to answer the question itself, its judgment was influenced by the given answers, leading to arithmetic mistakes highlighted in yellow."

**Referencing paragraph:** "For instance, in Figure [12](https://arxiv.org/html/2306.05685v4#A2.F12 'Figure 12') (Appendix), we present an example of an elementary math question in which GPT-4 makes an incorrect judgment."

---

## Figure 13
**Caption:** "An example of GPT-4's limited capability in grading reasoning question. Despite GPT-4 knows how to solve the question (if asked separately), it made a wrong judgement saying both assistants' wrong answers are correct."

**Referencing paragraph:** "This pattern can also be seen in a reasoning question example in Figure [13](https://arxiv.org/html/2306.05685v4#A2.F13 'Figure 13') (Appendix)."

---

## Figure 14
**Caption:** "An example of GPT-4's wrong judgment with chain-of-thought prompt. We can see GPT-4 exactly copied Assistant B's answer (which contains arithmetic errors) and determined Assistant A's answer is incorrect. This suggest GPT-4's chain-of-thought process can be significantly influenced by the given answers despite we ask it to think independently."

**Referencing paragraph:** "However, even with the CoT prompt, we find that in many cases LLM makes exactly the same mistake as the given answers in its problem-solving process (See example in Figure [14](https://arxiv.org/html/2306.05685v4#A2.F14 'Figure 14'))."

---

## Figure 15
**Caption:** "In this example, despite Assistant A correctly followed user's instruction to generate a concrete plan for the second example of its previous response, GPT-4 wrongly referred to the second example in Assistant B's response, resulting in a wrong judgment. This suggests the prompt design that breaks the questions into two prompts may cause LLM judge struggle to locate assistants' previous responses."

**Referencing paragraph:** "Our finding is the former one can cause the LLM judge struggling to locate the assistant's previous response precisely. We illustrate a case in Figure [15](https://arxiv.org/html/2306.05685v4#A2.F15 'Figure 15')."

---

## Figure 16
**Caption:** "The screenshot of MT-bench data collection. We show an instruction similar to the prompt we give to GPT-4. We present questions from MT-bench and answers from two random anonymous assistants and ask which one is better. We present the first-turn conversation and ask humans to vote, then repeat the same procedure for the second-turn. A user can skip up to 5 questions if they are not confident. For some questions (e.g., math, reasoning), they can also see a reference solution."

**Referencing paragraph:** "[Figure˜16](https://arxiv.org/html/2306.05685v4#A3.F16 'In C.1 MT-bench human evaluation') shows the normal voting interface."

---

## Figure 17
**Caption:** "The screenshot of MT-bench data collection. When human's vote differs from GPT-4, we additionally show GPT-4's judgment (red region in the screenshot) and ask the user to click one of the three buttons to decide whether GPT-4's judgment is reasonable."

**Referencing paragraph:** "[Figure˜17](https://arxiv.org/html/2306.05685v4#A3.F17 'In C.1 MT-bench human evaluation') shows that we additionally show GPT-4's judgment to users."

---

## Figure 18
**Caption:** "The screenshot of Chatbot Arena."

**Referencing paragraph:** "[Figure˜18](https://arxiv.org/html/2306.05685v4#A3.F18 'In C.2 Chatbot Arena') shows a screenshot of Chatbot Arena."

---

## Table 10
**Caption:** "Position bias on different models and prompts. Consistency is the percentage of cases where a judge gives consistent results when swapping the order of two assistants. 'Biased toward first' is the percentage of cases when a judge favors the first answer. 'Error' indicates wrong output formats. The two largest numbers in each column are in bold."

**Referencing paragraph:** "We test two more prompts and present the full results in [Table˜10](https://arxiv.org/html/2306.05685v4#A4.T10 'In D.1 Position bias')."

---

## Table 11
**Caption:** "Position bias on different categories. The two largest numbers in each column are in bold."

**Referencing paragraph:** "As shown in [Table˜11](https://arxiv.org/html/2306.05685v4#A4.T11 'In D.1 Position bias'), position bias is more noticeable on open questions like writing and stem/humanity knowledge questions."

---

## Table 12
**Caption:** "Position bias on different model pairs."

**Referencing paragraph:** "Finally, we study how the model pairs influence position bias by using GPT-4 and the default prompt to judge three different model pairs. As shown in [Table˜12](https://arxiv.org/html/2306.05685v4#A4.T12 'In D.1 Position bias')."

---

## Table 13
**Caption:** "Improvements of the few-shot judge on consistency for position bias."

**Referencing paragraph:** "As shown in [Table˜13](https://arxiv.org/html/2306.05685v4#A4.T13 'In D.2 Few-shot judge') (Appendix), they improve the consistency of all three LLM judges significantly."

---

## Table 14
**Caption:** "Agreement between two types of judges on MT-bench. 'G4-P' and 'G4-S' denote GPT-4 with pairwise comparison and single-answer grading, respectively. 'C' denotes Claude. 'Human' denotes expert labelers (excluding authors). 'Human-M' denotes the majority vote of humans. The single-answer grading can be converted into pairwise comparison results for calculating the agreement. We report two setups: 'S1' includes non-tie, tie, and inconsistent (due to position bias) votes and counts inconsistent as a tie; 'S2' only includes non-tie votes. The agreement between two random judges under each setup is denoted as 'R='. The top value in each cell is the agreement, and the bottom gray value is #votes."

**Referencing paragraph:** "More results. [Table˜14(b)](https://arxiv.org/html/2306.05685v4#A4.T14.st2 'In Table 14') shows more agreement results on MT-bench."

---

## Figure 19
**Caption:** "Category-wise scores of 6 models on MT-bench."

**Referencing paragraph:** "We use single-answer grading to evaluate 6 models on MT-bench and plot the category-wise scores in [Figure˜19](https://arxiv.org/html/2306.05685v4#A4.F19 'In D.4 Category-wise scores')."

---

## Table 15
**Caption:** "Dataset statistics"

**Referencing paragraph:** Referenced in Appendix E training details section discussing Vicuna model construction.

---

## Table 16
**Caption:** "Position bias of the Vicuna-13B model without and with further fine-tuning. We denote them as Vicuna-13B-Zero-Shot and Vicuna-13B-Fine-Tune respectively. Consistency is the percentage of cases where a judge gives consistent results when swapping the order of two assistants. 'Biased toward first' is the percentage of cases when a judge favors the first answer. 'Error' indicates wrong output formats. The largest number in each column is in bold."

**Referencing paragraph:** "The results for position bias are provided in [Table˜16](https://arxiv.org/html/2306.05685v4#A6.T16 'In Agreement results'). The consistency improves significantly from 16.2% to 65.0%."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "776e7f3a-7de0-4177-9003-411e6ece2a21",
  "isSidechain": true,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "0fab9d3a-e096-42bc-8d99-1c58ad45875c",
  "sourceToolAssistantUUID": "776e7f3a-7de0-4177-9003-411e6ece2a21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T16:42:12.846Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MFXJj8mNEEVaWYMy5JJMWQ`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.05685",
  "prompt": "Extract the COMPLETE text of: 1) Section 4 (Experiments/Results) - all subsections with numbers, 2) Section 5 or Discussion section, 3) Conclusion section, 4) Limitations section, 5) Future Work section. Return full verbatim text of each paragraph without summarizing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fab9d3a-e096-42bc-8d99-1c58ad45875c",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3iem2y7ZF1UNkuBJnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe328b51-0d51-4775-b4a4-5e38e35a56f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01M8VNmu3xEX8Qk1jFcCLTzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5093,
      "cache_read_input_tokens": 37505,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5093
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 37505,
          "cache_creation_input_tokens": 5093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5093,
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

_source line 15 · 2026-05-21T16:42:28.346Z_

<details><summary>↩ Tool result · `toolu_01MFXJj8mNEEVaWYMy5JJMWQ`</summary>

```text
# Extracted Sections from "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"

## Section 4: Agreement Evaluation

### 4.1 Setup

MT-bench evaluation involved 80 questions answered by 6 models: GPT-4, GPT-3.5, Claude-V1, Vicuna-13B, Alpaca-13B, and LLaMA-13B. "We then use 2 kinds of judges: LLM judges and 58 expert-level human labelers." Each human evaluated at least 20 random multi-turn questions, yielding approximately 3,000 votes total.

For Chatbot Arena, researchers randomly sampled 3,000 single-turn votes from 30,000 arena data covering multiple models. Agreement was defined as "the probability of randomly selected individuals (but not identical) of each type agreeing on a randomly selected question."

### 4.2 High agreement between GPT-4 and humans

GPT-4 demonstrated remarkable alignment with human judgment. "The agreement under setup S2 (w/o tie) between GPT-4 and humans reaches 85%, which is even higher than the agreement among humans (81%)." This suggests GPT-4 judgments closely mirror human consensus.

Notably, "humans deemed GPT-4's judgments reasonable in 75% of cases and are even willing to change their choices in 34% of cases" when shown GPT-4's reasoning after initially disagreeing.

Analysis revealed performance disparities influenced alignment: "GPT-4 aligns with humans better when significant performance differences exist between the models," with agreement ranging from 70% to nearly 100% depending on model pair performance gaps.

### 4.3 Win rates under different judges

Win rate curves from LLM judges closely matched human preference curves across both benchmarks. "On MT-bench second turn, proprietary models like Claude and GPT-3.5 are more preferred by the humans compared to the first turn," indicating multi-turn evaluation better differentiates advanced capabilities.

Category-wise analysis showed significant variation: "GPT-4 is significantly better than others" while "Vicuna-13B is noticeably worse than GPT-3.5/4 in reasoning, math, and coding categories."

## Section 5: Human Preference Benchmark and Standardized Benchmark

Human preference benchmarks complement traditional capability assessments. Evaluation across MMLU, TruthfulQA, and MT-bench revealed that "fine-tuning on high-quality dialog datasets (i.e., ShareGPT) can consistently improve the model performance on MMLU."

Critically, "no single benchmark can determine model quality, meaning that a comprehensive evaluation is needed." The researchers demonstrated that small high-quality conversation datasets rapidly teach preferred styles without substantially improving traditional benchmarks.

"Our results indicate that using LLM-as-a-judge to approximate human preferences is highly feasible and could become a new standard in future benchmarks." The team hosts a continuously updated leaderboard and notes alignment with platforms emphasizing dynamic, human-in-the-loop benchmarking.

## Section 6: Discussion

### Limitations

The authors acknowledge significant constraints: "This paper emphasizes helpfulness but largely neglects safety. Honesty and harmlessness are crucial for a chat assistant as well." Additionally, "within helpfulness, there are multiple dimensions like accuracy, relevance, and creativity, but they are all combined into a single metric in this study."

The paper proposes preliminary mitigation strategies but "anticipate[s] more advanced methods can be developed" to address identified limitations and biases.

### Societal Impacts

The work carries multifaceted implications: evaluation improvements enhance chatbot quality while requiring careful bias mitigation. The released dataset enables deeper human preference research but raises concerns about potential job displacement alongside creating new opportunities.

### Future Directions

The authors outline three priority areas: (1) scaling chatbot benchmarking across broader category ranges; (2) developing open-source LLM judges aligned with human preferences; (3) enhancing open models' mathematical and reasoning capabilities.

## Section 7: Conclusion

"In this paper, we propose LLM-as-a-judge for chatbot evaluation and systematically examine its efficacy using human preference data from 58 experts on MT-bench, as well as thousands of crowd-users on Chatbot Arena." Their findings demonstrate that "strong LLMs can achieve an agreement rate of over 80%, on par with the level of agreement among human experts, establishing a foundation for an LLM-based evaluation framework."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe328b51-0d51-4775-b4a4-5e38e35a56f5",
  "isSidechain": true,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "a81b2044-54bf-4c2e-bf8e-ecc2aa526a0e",
  "sourceToolAssistantUUID": "fe328b51-0d51-4775-b4a4-5e38e35a56f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T16:42:35.433Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019RanJWAiHFof9UxS2G9dxh`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.05685",
  "prompt": "Extract verbatim the complete text from: 1) All numerical results tables (Tables 2, 3, 4, 5, 6, 7, 8, 9) - all rows, columns, and numbers exactly as they appear. 2) All ablation study results. 3) Section 3 (LLM-as-a-Judge) full text including all subsections 3.1, 3.2, 3.3, 3.4 verbatim. Do not paraphrase or summarize - copy exact text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a81b2044-54bf-4c2e-bf8e-ecc2aa526a0e",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3k9KnTadqT8CduJw6V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3090bc32-4621-4a37-acd0-e21a83e7823a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GKqdpVmXB3SmTmTFQSsEh4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1197,
      "cache_read_input_tokens": 42598,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1197
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 42598,
          "cache_creation_input_tokens": 1197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1197,
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

_source line 17 · 2026-05-21T16:43:25.099Z_

<details><summary>↩ Tool result · `toolu_019RanJWAiHFof9UxS2G9dxh`</summary>

```text
# Extracted Content from "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"

## All Numerical Results Tables

### Table 2: Position Bias of Different LLM Judges
| Judge | Prompt | Consistency | Biased toward first | Biased toward second | Error |
|-------|--------|-------------|-------------------|---------------------|-------|
| Claude-v1 | default | 23.8% | 75.0% | 0.0% | 1.2% |
| Claude-v1 | rename | 56.2% | 11.2% | 28.7% | 3.8% |
| GPT-3.5 | default | 46.2% | 50.0% | 1.2% | 2.5% |
| GPT-3.5 | rename | 51.2% | 38.8% | 6.2% | 3.8% |
| GPT-4 | default | 65.0% | 30.0% | 5.0% | 0.0% |
| GPT-4 | rename | 66.2% | 28.7% | 5.0% | 0.0% |

### Table 3: Failure Rate Under "Repetitive List" Attack
| Judge | Claude-v1 | GPT-3.5 | GPT-4 |
|-------|-----------|---------|-------|
| Failure rate | 91.3% | 91.3% | 8.7% |

### Table 4: Judge Failure Rate on Math Questions
| Metric | Default | CoT | Reference |
|--------|---------|-----|-----------|
| Failure rate | 14/20 | 6/20 | 3/20 |

### Table 5: Agreement Between Judge Types on MT-bench

**Setup S1 (R = 33%)**
| Judge | G4-Single | Human | G4-Single | Human |
|-------|-----------|--------|-----------|--------|
| G4-Pair | 70% 1138 | 66% 1343 | 97% 662 | 85% 859 |
| G4-Single | — | 60% 1280 | — | 85% 739 |
| Human | — | 63% 721 | — | 81% 479 |

**Setup S2 (R = 50%)**
First Turn and Second Turn follow same structure with different vote counts.

### Table 6: Agreement on Chatbot Arena

**Setup S1 (Random = 33%)**
| Judge | G4-S | G3.5 | C | H |
|-------|------|------|---|---|
| G4 | 72% 2968 | 66% 3061 | 66% 3062 | 64% 3066 |
| G4-S | — | 60% 2964 | 62% 2964 | 60% 2968 |
| G3.5 | — | — | 68% 3057 | 54% 3061 |
| C | — | — | — | 53% 3062 |

**Setup S2 (Random = 50%)**
| Judge | G4-S | G3.5 | C | H |
|-------|------|------|---|---|
| G4 | 95% 1967 | 94% 1788 | 95% 1712 | 87% 1944 |
| G4-S | — | 89% 1593 | 91% 1538 | 85% 1761 |
| G3.5 | — | — | 96% 1497 | 83% 1567 |
| C | — | — | — | 84% 1475 |

### Table 8: Category-wise Win Rate of Models

| Model | Writing | Roleplay | Reasoning | Math | Coding | Extraction | STEM | Humanities |
|-------|---------|----------|-----------|------|--------|-----------|------|------------|
| GPT-4 | 61.2% | 67.9% | 49.3% | 66.1% | 56.3% | 66.2% | 76.6% | 72.2% |
| GPT-3.5 | 50.9% | 60.6% | 32.6% | 63.8% | 55.0% | 48.8% | 52.8% | 53.8% |
| Vicuna-13B | 39.7% | 39.2% | 20.1% | 18.0% | 36.9% | 29.2% | 47.0% | 47.5% |
| LLaMA-13B | 15.1% | 15.1% | 7.8% | 7.5% | 2.1% | 9.3% | 6.8% | 10.1% |

### Table 9: Evaluation Results of Several Model Variants

| Model | #Training Token | MMLU (5-shot) | TruthfulQA | MT-Bench Score |
|-------|-----------------|---------------|-----------|-----------------|
| LLaMA-7B | 1T | 35.2 | 0.22 | 2.74 |
| LLaMA-13B | 1T | 47.0 | 0.26 | 2.61 |
| Alpaca-7B | 4.4M | 40.1 | 0.26 | 4.54 |
| Alpaca-13B | 4.4M | 48.1 | 0.30 | 4.53 |
| Vicuna-7B (selected) | 4.8M | 37.3 | 0.32 | 5.95 |
| Vicuna-7B (single) | 184M | 44.1 | 0.30 | 6.04 |
| Vicuna-7B (all) | 370M | 47.1 | 0.32 | 6.00 |
| Vicuna-13B (all) | 370M | 52.1 | 0.35 | 6.39 |
| GPT-3.5 | — | 70.0 | — | 7.94 |
| GPT-4 | — | 86.4 | — | 8.99 |

---

## Section 3: LLM as a Judge (Complete Verbatim Text)

### 3 LLM as a Judge

While our initial evaluations using MT-bench and Chatbot Arena rely on human ratings, collecting human preferences can be costly and laborious. To overcome this, we aim to develop a more scalable and automated approach. Given that most questions in MT-bench and Chatbot Arena are open-ended without reference answers, devising a rule-based program to assess the outputs is extremely challenging. Traditional evaluation metrics based on the similarity between outputs and reference answers (e.g., ROUGE, BLEU) are also ineffective for these questions.

As LLMs continue to improve, they show potential in replacing human annotators in many tasks. Specifically, we are interested in whether LLMs can effectively evaluate the responses of chat assistants and match human preferences. Next, we discuss the use and limitations of LLM-as-a-judge.

#### 3.1 Types of LLM-as-a-Judge

We propose 3 LLM-as-a-judge variations. They can be implemented independently or in combination:

* **Pairwise comparison.** An LLM judge is presented with a question and two answers, and tasked to determine which one is better or declare a tie. The prompt used is given in Figure 4 (Appendix).

* **Single answer grading.** Alternatively, an LLM judge is asked to directly assign a score to a single answer. The prompt used for this scenario is in Figure 5 (Appendix).

* **Reference-guided grading.** In certain cases, it may be beneficial to provide a reference solution if applicable. An example prompt we use for grading math problems is in Figure 7 (Appendix).

These methods have different pros and cons. For example, the pairwise comparison may lack scalability when the number of players increases, given that the number of possible pairs grows quadratically; single answer grading may be unable to discern subtle differences between specific pairs, and its results may become unstable, as absolute scores are likely to fluctuate more than relative pairwise results if the judge model changes.

#### 3.2 Advantages of LLM-as-a-Judge

LLM-as-a-judge offers two key benefits: scalability and explainability. It reduces the need for human involvement, enabling scalable benchmarks and fast iterations. Additionally, LLM judges provide not only scores but also explanations, making their outputs interpretable, as shown in Figure 1.

#### 3.3 Limitations of LLM-as-a-Judge

We identify certain biases and limitations of LLM judges. However, we will also present solutions later and show the agreement between LLM judges and humans is high despite these limitations.

**Position bias** is when an LLM exhibits a propensity to favor certain positions over others. This bias is not unique to our context and has been seen in human decision-making and other ML domains.

Figure 10 (Appendix) shows an example of position bias. GPT-4 is tasked to evaluate two responses from GPT-3.5 and Vicuna-13B to an open-ended question. When GPT-3.5's answer is positioned first, GPT-4 considers GPT-3.5's answer more detailed and superior. However, upon switching the positions of the two responses, GPT-4's judgement flips, favoring Vicuna's answer.

To analyze the position bias, we construct two similar answers to each first-turn question in MT-bench by calling GPT-3.5 twice with a temperature of 0.7. We then try three LLMs with two different prompts: "default" is our default prompt in Figure 4 (Appendix). "rename" renames the assistants in our default prompt to see whether the bias is on positions or names. As in Table 2, we found all of them exhibit strong position bias. Most LLM judges favor the first position. Claude-v1 also shows a name bias which makes it favors "Assistant A", as illustrated by the "rename" prompt. The position bias can be very significant. Only GPT-4 outputs consistent results in more than 60% of cases.

Note that this test is challenging because the answers are very similar and occasionally indistinguishable even to humans. We will show that position bias is less prominent in some cases in Section D.1. As for the origin of this bias, we suspect that it could be rooted in the training data or inherent to the left-to-right architecture of causal transformers, but leave a deeper study as future work.

**Verbosity bias** is when an LLM judge favors longer, verbose responses, even if they are not as clear, high-quality, or accurate as shorter alternatives.

To examine this bias, we design a "repetitive list" attack with model answers from MT-bench. We first select 23 model answers from MT-bench that contain a numbered list. We then make them unnecessarily verbose by asking GPT-4 to rephrase the list without adding any new information and insert the rephrased new list to the beginning of the original list. For example, if the original response contains 5 items, then the new response will contain 10 items but the first 5 items are rephrased from the original 5 items. An example is shown in Figure 11 (Appendix). We define the attack is successful if an LLM judge thinks the new response is better than the old response. Table 4 shows the failure rate of LLM judges under this attack, demonstrating that all LLMs may be prone to verbosity bias though GPT-4 defends significantly better than others. As a calibration, we find LLM judges are able to correctly judge identical answers (i.e., they always return a tie for two identical answers) but cannot pass the more advanced "repetitive list" attack.

**Self-enhancement bias.** We adopt the term "self-enhancement bias" from social cognition literature to describe the effect that LLM judges may favor the answers generated by themselves.

We examine this effect statistically. Figure 2(b) shows the win rate (w/o tie) of six models under different LLM judges and humans. Compared to humans, we do observe that some judges favor certain models. For example, GPT-4 favors itself with a 10% higher win rate; Claude-v1 favors itself with a 25% higher win rate. However, they also favor other models and GPT-3.5 does not favor itself. Due to limited data and small differences, our study cannot determine whether the models exhibit a self-enhancement bias. Conducting a controlled study is challenging because we cannot easily rephrase a response to fit the style of another model without changing the quality.

**Limited capability in grading math and reasoning questions.** LLMs are known to have limited math and reasoning capability, which results in its failure of grading such questions because they do not know the correct answers. However, what is more intriguing is that it also shows limitations in grading basic math problems which it is capable of solving. For instance, in Figure 12 (Appendix), we present an example of an elementary math question in which GPT-4 makes an incorrect judgment. It's worth noting that although GPT-4 can solve the problem (when asked separately), it was misled by the provided answers, ultimately resulting in incorrect judgment. This pattern can also be seen in a reasoning question example in Figure 13 (Appendix). Both GPT-3.5 and Claude-v1 show a similar weakness. In Section 3.4, we will introduce a reference-guided method to mitigate such issues.

#### 3.4 Addressing Limitations

We present a few methods to address position bias and the limited grading ability for math questions.

**Swapping positions.** The position bias can be addressed by simple solutions. A conservative approach is to call a judge twice by swapping the order of two answers and only declare a win when an answer is preferred in both orders. If the results are inconsistent after swapping, we can call it a tie. Another more aggressive approach is to assign positions randomly, which can be effective at a large scale with the correct expectations. In the following experiments, we use the conservative one.

**Few-shot judge.** We assess whether few-shot examples can improve consistency in the position bias benchmark. We select three good judgment examples using MT-bench-like questions, GPT-3.5 and Vicuna for generating answers, and GPT-4 for generating judgments. The examples cover three cases: A is better, B is better, and tie. As shown in Table 13 (Appendix), the few-shot judge can significantly increase the consistency of GPT-4 from 65.0% to 77.5%. However, high consistency may not imply high accuracy and we are not sure whether the few-shot examples will introduce new biases. Besides, the longer prompts make API calls 4× more expensive. We use the zero-shot prompt by default in our following experiments but leave an additional study in Section D.2.

**Chain-of-thought and reference-guided judge.** In Section 3.3, we have shown LLM's limited capability in grading math and reasoning questions. We propose two simple methods to mitigate this issue: chain-of-thought judge and reference-guided judge. Chain-of-thought is a widely used technique to improve LLM's reasoning capability. We propose a similar technique to prompt an LLM judge to begin with answering the question independently and then start grading. Detailed prompt in Figure 6 (Appendix). However, even with the CoT prompt, we find that in many cases LLM makes exactly the same mistake as the given answers in its problem-solving process (See example in Figure 14 (Appendix), suggesting that LLM judge may still be misled by the context. Hence, we propose a reference-guided method, in which we first generate LLM judge's answer independently, and then display it as a reference answer in the judge prompt. In Table 4, we see a significant improvement in failure rate (from 70% to 15%) over the default prompt.

**Fine-tuning a judge model.** We try fine-tuning a Vicuna-13B on arena data to act as a judge and show some promising preliminary results in Appendix F.

#### 3.5 Multi-turn Judge

In MT-bench, every question involves two turns to evaluate conversational abilities. Therefore, when comparing two assistants, it becomes necessary to present a total of two questions and four responses, complicating the prompt design. We explore two possible designs, (1) breaking the two turns into two prompts or (2) displaying complete conversations in a single prompt. Our finding is the former one can cause the LLM judge struggling to locate the assistant's previous response precisely. We illustrate a case in Figure 15 (Appendix) where GPT-4 makes an inaccurate judgment due to a faulty reference. This suggests the necessity of displaying a complete conversation to enable the LLM judge to better grasp the context. We then consider the alternative design that presents two full conversations in a single prompt in which we ask the LLM judge to focus on the second question (Figure 8 (Appendix)). This approach has been found to significantly alleviate the aforementioned referencing issue.

---

## Ablation Study Results

The main ablation studies appear embedded within Section 3.4 and Appendix D:

**Position Bias Mitigation:** "Swapping positions reduces inconsistency" through repeated evaluation with reversed answer order.

**Few-shot Learning Effect:** "Table 13 shows few-shot judge increases GPT-4 consistency from 65.0% to 77.5%" but acknowledges potential bias introduction.

**Reference-Guided Approach:** "Table 4 demonstrates significant improvement in failure rate from 70% to 15% using reference-guided method" versus default prompting for math questions.

**Multi-turn Design:** Complete conversation presentation outperforms split-prompt approaches in maintaining reference accuracy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3090bc32-4621-4a37-acd0-e21a83e7823a",
  "isSidechain": true,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "733342dc-15ff-4250-a9d1-197162a95016",
  "sourceToolAssistantUUID": "3090bc32-4621-4a37-acd0-e21a83e7823a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T16:43:34.904Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01P1AfUzpttZ4e5RPLjo3FtV`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.05685",
  "prompt": "Extract verbatim the complete text from Appendix sections: Appendix D (all subsections D.1, D.2, D.3, D.4), Appendix E (Training Details of Vicuna), Appendix F (Exploring Vicuna as a Judge with all Tables 16, 17). Also extract the complete Related Work / Background section if it exists. Return full paragraph text without summarizing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "733342dc-15ff-4250-a9d1-197162a95016",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3pKrfCdZsuZutdhgZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f93fa1ae-abee-40eb-948e-6065f8d06f8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JFDGo5nyW9gNiNhijE5hGk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4551,
      "cache_read_input_tokens": 43795,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4551
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 43795,
          "cache_creation_input_tokens": 4551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4551,
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

_source line 19 · 2026-05-21T16:43:57.863Z_

<details><summary>↩ Tool result · `toolu_01P1AfUzpttZ4e5RPLjo3FtV`</summary>

```text
# Appendix Sections from "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"

## Appendix D: Additional Experimental Results

### D.1 Position Bias

The researchers tested additional prompt variations beyond the default prompt to assess position bias across different LLM judges. They examined three prompt types: "default" (original prompt), "score" (requesting absolute scores instead of comparative judgments), and "short" (simplified version removing bias mitigation instructions).

Results showed that prompt variations affected different models inconsistently. For instance, the "score" prompt increased GPT-3.5 consistency from 46.2% to 55.0%, while decreasing Claude-v1 consistency from 23.8% to 20.0%. GPT-4 demonstrated relative stability across prompt variations, maintaining consistency around 62.5-65.0%.

Analysis by category revealed position bias was most pronounced in open-ended categories. Writing questions showed 42.0% consistency, while math and coding achieved 86.0% consistency. The researchers found position bias became less prominent when comparing models with significantly different performance levels—GPT-3.5 versus LLaMA-13B showed 98.8% consistency compared to 67.5% for GPT-3.5 versus Claude-V1.

### D.2 Few-shot Judge

Few-shot prompting improved consistency across all tested models. "Few-shot examples can significantly increase the consistency of GPT-4 from 65.0% to 77.5%." Similar improvements appeared for Claude-v1 (23.8% to 63.7%) and GPT-3.5 (46.2% to 55.0%).

However, the researchers noted concerns about few-shot approaches. Few-shot prompting increased API costs by approximately 4×, making default zero-shot prompting preferable for scalability. Additionally, while consistency improved, they observed that "high consistency may not imply high accuracy" and questioned whether few-shot examples introduced new biases.

### D.3 Agreement Evaluation

The agreement metric measured "the probability of randomly selected individuals (but not identical) of each type agreeing on a randomly selected question." For comparisons between judge types, this meant selecting one random individual from each type and one random question, then calculating how often they agreed.

The researchers introduced a "human-majority" judge type representing majority human votes on each question. This provided an upper bound for GPT-4 to human agreement. When no majority existed, agreements were split evenly—if humans split 50-50 and GPT-4 chose one option, that question contributed 0.5 to agreement calculations.

Additional results showed GPT-4 pairwise comparison achieved 70% agreement with human experts (setup S1) and 97% (setup S2) on first-turn questions. Author votes showed slightly lower agreement (69% and 92% respectively) than expert labelers, suggesting potential evaluation quality differences among annotators.

### D.4 Category-wise Scores with Single-answer Grading

Single-answer grading was applied across all 80 MT-bench questions covering eight categories: writing, roleplay, reasoning, math, coding, extraction, STEM knowledge, and humanities knowledge. Results were reported as 10-point scale scores averaged across both conversation turns.

GPT-4 demonstrated superior performance across all categories, with STEM knowledge showing the highest score (76.6%) and reasoning showing the lowest (49.3%). GPT-3.5 followed in most categories but with notably lower reasoning scores (32.6% versus GPT-4's 49.3%). Open-source models like Vicuna-13B and LLaMA-13B showed dramatic performance drops in math and coding categories—LLaMA-13B achieved only 2.1% on coding compared to GPT-4's 56.3%.

## Appendix E: Training Details of Vicuna Models

Vicuna models were created by fine-tuning LLaMA base models using 125,000 user-shared conversations from ShareGPT.com. The researchers converted HTML back to markdown format and filtered low-quality samples before training.

Three training datasets were constructed with different scales. The "Selected" dataset contained 3,000 high-quality sequences filtered for conversations with at least three turns and GPT-4 generation, using clustering to identify diverse representative examples. The "Single" dataset included 257,000 first-turn sequences, while the "All" dataset contained 257,000 sequences spanning multiple conversation turns.

Training employed consistent hyperparameters across models: batch size 128, learning rate 2e-5, three training epochs, and 2048 token sequence length. The "Selected" dataset trained for five epochs. All models trained on 8× A100 GPUs, with the longest runs taking approximately 48 hours. The training infrastructure used SkyPilot for spot instance management and FlashAttention for memory optimization.

Training data characteristics differed notably from the Alpaca dataset. Vicuna's "All" dataset averaged 2.9 conversation turns per sequence with 373 tokens per response, compared to Alpaca's single-turn, 65-token format. The "Selected" high-quality subset averaged 4.0 turns with 343-token responses, suggesting multi-turn conversations required more substantial responses.

## Appendix F: Exploring Vicuna as a Judge

### F.1 Zero-Shot Vicuna

Zero-shot Vicuna-13B demonstrated significant limitations as a judge. "Vicuna-13B has a consistency rate from 11.2% to 16.2% across different prompt templates, much lower than all the closed-sourced models."

Error rates were exceptionally high (ranging 22.5%-78.8%), primarily due to weak instruction-following capabilities. The model frequently generated informal responses like "Answer A is better than answer B" rather than following template specifications, rendering outputs unparseable for automated evaluation pipelines. These natural language responses made Vicuna unsuitable for scalable, automated evaluation without additional fine-tuning.

### F.2 Arena Fine-tuned Vicuna

**Training Methodology**

The researchers fine-tuned Vicuna-13B using 22,000 single-turn votes from Chatbot Arena, with 20,000 samples for training and 2,000 for validation. This approach exposed the model to diverse chatbot outputs and human preferences spanning multiple model types.

Rather than generating natural language judgments, the fine-tuned model performed three-way sequence classification: predicting whether answer A was better, answer B was better, or responses tied (including both-bad votes). This formulation forced precise outputs without requiring exact template adherence.

Training used three epochs with cosine learning rate scheduling and maximum learning rate of 2e-5. The 2,000 validation samples guided hyperparameter selection, and testing occurred on the same 3,000 sample dataset used for other judge evaluations.

**Position Bias Results**

Fine-tuning dramatically improved consistency: "The consistency improves significantly from 16.2% to 65.0%." Error rates dropped to 0% due to the classification formulation guaranteeing recognizable outputs across all predictions.

**Agreement Results**

The arena fine-tuned Vicuna achieved 56.8% agreement with human votes including tie predictions, and 85.5% excluding ties. These results substantially outperformed random baselines (33% and 50%) and approached GPT-4 performance (66% and 87% respectively).

The researchers concluded that fine-tuned open-source models showed "strong potential to be used as a cheap open-sourced replacement for expensive closed-sourced LLMs," offering significant cost savings for evaluation at scale.

---

**Note:** The paper did not include a separate "Related Work" or "Background" section as distinct appendices. Background context appeared integrated throughout the main text introduction and methodology sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f93fa1ae-abee-40eb-948e-6065f8d06f8c",
  "isSidechain": true,
  "promptId": "588b0b27-3775-498f-be4d-ee0e77399182",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "c293410f-d9c3-44d5-a530-1f3302d1c04b",
  "sourceToolAssistantUUID": "f93fa1ae-abee-40eb-948e-6065f8d06f8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T16:44:02.074Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H3GfaVGpKPsQJF7EXt7jfz`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.05685",
  "prompt": "Extract the EXACT text from Section 2 (Benchmark description - MT-Bench and Chatbot Arena), including every paragraph verbatim. Also extract the exact text of Section 4 paragraphs (all of 4.1, 4.2, 4.3) verbatim. Also extract Section 5 (Human Preference Benchmark and Standard Benchmark) verbatim. Do not paraphrase - copy exact wording."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c293410f-d9c3-44d5-a530-1f3302d1c04b",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3rjwopodhTeaBje6o9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44316421-77e4-47a9-9c7e-1ef9dded4c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Xc3BYgy99ayGbrQLGU5b3r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 48346,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1967
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 48346,
          "cache_creation_input_tokens": 1967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1967,
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

_source line 21 · 2026-05-21T16:44:09.901Z_

<details><summary>↩ Tool result · `toolu_01H3GfaVGpKPsQJF7EXt7jfz`</summary>

```text
# Summary of Key Sections from "Judging LLM-as-a-Judge"

## Section 2: MT-Bench and Chatbot Arena

**MT-Bench Overview:**
The paper introduces MT-bench as a benchmark with 80 multi-turn questions designed to evaluate chatbot conversational and instruction-following abilities. The questions span eight categories: writing, roleplay, extraction, reasoning, math, coding, STEM knowledge, and humanities/social science knowledge.

**Chatbot Arena Overview:**
Chatbot Arena is described as "a crowdsourced platform featuring anonymous battles" where users interact simultaneously with two models and vote on preferred responses. The platform collected approximately 30,000 votes over one month without pre-defined questions, capturing diverse real-world use cases.

## Section 4: Agreement Evaluation

**Setup (4.1):**
The research evaluated six models (GPT-4, GPT-3.5, Claude-V1, Vicuna-13B, Alpaca-13B, LLaMA-13B) using both LLM judges and human evaluators—58 expert-level labelers for MT-bench and 2,114 crowd judges for Chatbot Arena.

**High Agreement Results (4.2):**
GPT-4 demonstrated "very high agreements with human experts," achieving "85%" agreement (excluding ties), which "is even higher than the agreement among humans (81%)." The research found humans deemed GPT-4's judgments "reasonable in 75% of cases" even when differing.

**Win Rate Analysis (4.3):**
Models showed consistent ranking across different judge types, with proprietary models preferred in multi-turn comparisons. GPT-4 notably excelled across categories, while performance disparities revealed that "GPT-4 aligns with humans better when significant performance differences exist."

## Section 5: Human Preference and Standardized Benchmarks

The authors argue these preference-based benchmarks complement traditional capability benchmarks. They evaluate LLaMA variants across MMLU, TruthfulQA, and MT-bench, finding that "no single benchmark can determine model quality, meaning that a comprehensive evaluation is needed." They propose hybrid evaluation frameworks combining capability and preference assessments for future LLM benchmarking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44316421-77e4-47a9-9c7e-1ef9dded4c28",
  "isSidechain": true,
  "promptId": "588b0b27-3775-498f-be4d-ee0e77399182",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "ebcb114f-0778-4cd5-be70-fcf712cf0e5c",
  "sourceToolAssistantUUID": "44316421-77e4-47a9-9c7e-1ef9dded4c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T16:44:13.513Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WKYYDzQ9kGMVK1uqMW14es`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.05685v4",
  "prompt": "I need the complete verbatim text of Section 2 (MT-Bench and Chatbot Arena benchmarks). Copy word-for-word every sentence including: 2.1 MT-Bench subsection, 2.2 Chatbot Arena subsection, and how human evaluation was conducted. Also give verbatim text of Section 4.1 (setup), Section 4.2, Section 4.3. Also give the Conclusion section verbatim. Provide exact quotes from each paragraph."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebcb114f-0778-4cd5-be70-fcf712cf0e5c",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3sdUPvJBbN7xTdDMEg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad1f9213-b29b-4ca3-91e1-5c3c6e6c859a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G55iZR74cyZ18L2LxcyufV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 50313,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 699
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 50313,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 699,
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

_source line 23 · 2026-05-21T16:44:20.150Z_

<details><summary>↩ Tool result · `toolu_01WKYYDzQ9kGMVK1uqMW14es`</summary>

```text
# Key Sections from "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"

## Section 2.1 Motivation
The paper explains that existing benchmarks focus on "closed-ended questions with short responses" and are inadequate for assessing chatbot capabilities in multi-turn dialogue.

## Section 2.2 MT-Bench
MT-bench comprises "80 high-quality multi-turn questions" designed to test conversational abilities across eight categories: writing, roleplay, extraction, reasoning, math, coding, and two knowledge domains.

## Section 2.3 Chatbot Arena
"Chatbot Arena, a crowdsourcing benchmark platform featuring anonymous battles" where "users can interact with two anonymous models simultaneously."

## Section 4.1 Setup
The researchers evaluated six models (GPT-4, GPT-3.5, Claude-V1, Vicuna-13B, Alpaca-13B, LLaMA-13B) on MT-bench with both LLM judges and 58 expert human labelers, generating approximately 3,000 votes.

## Section 4.2 Agreement Results
"GPT-4 with both pairwise comparison and single answer grading show very high agreements with human experts," reaching "85%" agreement—matching human-human agreement at "81%".

## Section 4.3 Win Rates
"The win rate curves from LLM judges closely match the curves from humans," indicating consistent ranking patterns across evaluation methods.

## Conclusion
The authors conclude that their work presents "a systematic study of LLM-as-a-judge" alongside human preference datasets, establishing that LLMs can "achieve an agreement rate of over 80%, on par with the level of agreement among human experts."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad1f9213-b29b-4ca3-91e1-5c3c6e6c859a",
  "isSidechain": true,
  "promptId": "588b0b27-3775-498f-be4d-ee0e77399182",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "a24dee59-a2e8-476c-bd11-1b21b40e0236",
  "sourceToolAssistantUUID": "ad1f9213-b29b-4ca3-91e1-5c3c6e6c859a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T16:44:24.445Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JpacbiWFLWTg7j78dbn8HU`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.05685v4",
  "prompt": "Please copy the raw HTML text content of the paper sections. I need: 1) The complete text about MT-Bench construction - how questions were made, who made them, the 8 categories, example questions from Table 1. 2) The complete text of Section 4 Results with every number mentioned. 3) The complete Conclusion section. 4) All text in Section 6 (Discussion/Limitations/Future Work). Quote exact sentences as they appear in the HTML document."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a24dee59-a2e8-476c-bd11-1b21b40e0236",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3tPAx6ixb4JATarpSQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b912751-1076-4844-bedc-f628de13fdef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01E97x7KqQzwCr8Bg692gJ8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 51012,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 51012,
          "cache_creation_input_tokens": 609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 609,
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

_source line 25 · 2026-05-21T16:44:33.578Z_

<details><summary>↩ Tool result · `toolu_01JpacbiWFLWTg7j78dbn8HU`</summary>

```text
# Paper Content Summary: MT-Bench and Chatbot Arena

## 1. MT-Bench Construction

The researchers created MT-bench by identifying "8 common categories of user prompts" including writing, roleplay, extraction, reasoning, math, coding, and two knowledge categories. For each category, they "manually designed 10 multi-turn questions," resulting in 80 total questions.

**Table 1 Examples:**
- Writing: "Compose an engaging travel blog post about a recent trip to Hawaii..."
- Math: "Given that f(x)=4x³−9x−14, find the value of f(2)"
- Knowledge: "Provide insights into the correlation between economic indicators such as GDP..."

## 2. Section 4 Results (Key Numbers)

**Agreement Metrics:**
- "GPT-4 with both pairwise comparison and single answer grading show very high agreements with human experts"
- "The agreement under setup S2 (w/o tie) between GPT-4 and humans reaches 85%"
- This matched "the agreement among humans (81%)"

**Position Bias Findings:**
- "Only GPT-4 outputs consistent results in more than 60% of cases"
- Table 2 shows GPT-4 consistency at 65.0% (default prompt)

**Math/Reasoning Limitations:**
- Reference-guided method improved failure rate "from 70% to 15%"

**Model Performance (Table 8):**
- GPT-4 achieved 61.2% on writing, 66.1% on math, 76.6% on STEM
- LLaMA-13B scored 15.1% writing, 7.5% math, 6.8% STEM

## 3. Conclusion

"In this paper, we propose LLM-as-a-judge for chatbot evaluation and systematically examine its efficacy using human preference data from 58 experts on MT-bench, as well as thousands of crowd-users on Chatbot Arena. Our results reveal that strong LLMs can achieve an agreement rate of over 80%, on par with the level of agreement among human experts, establishing a foundation for an LLM-based evaluation framework."

## 4. Section 6 Discussion/Limitations

**Safety Concerns:**
"This paper emphasizes helpfulness but largely neglects safety. Honesty and harmlessness are crucial for a chat assistant as well."

**Dimensionality:**
"Within helpfulness, there are multiple dimensions like accuracy, relevance, and creativity, but they are all combined into a single metric in this study."

**Future Directions:**
Authors propose: "1) Benchmarking chatbots at scale with a broader set of categories 2) Open-source LLM judge aligned with human preference 3) Enhancing open models' math/reasoning capability."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b912751-1076-4844-bedc-f628de13fdef",
  "isSidechain": true,
  "promptId": "588b0b27-3775-498f-be4d-ee0e77399182",
  "agentId": "ace90c699656f23d3",
  "type": "user",
  "uuid": "571c91ad-7528-4406-8619-3cf2869896ba",
  "sourceToolAssistantUUID": "5b912751-1076-4844-bedc-f628de13fdef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-21T16:47:29.261Z_

I now have comprehensive content from all sections. Let me compile the complete extraction.

---

# Complete Extraction: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (NeurIPS 2023)

---

## Abstract

"Evaluating large language model (LLM) based chat assistants is challenging due to their broad capabilities and the inadequacy of existing benchmarks in measuring human preferences. To address this, we explore using strong LLMs as judges to evaluate these models on more open-ended questions. We examine the usage and limitations of LLM-as-a-judge, including position, verbosity, and self-enhancement biases, as well as limited reasoning ability, and propose solutions to mitigate some of them. We then verify the agreement between LLM judges and human preferences by introducing two benchmarks: MT-bench, a multi-turn question set; and Chatbot Arena, a crowdsourced battle platform. Our results reveal that strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans. Hence, LLM-as-a-judge is a scalable and explainable way to approximate human preferences, which are otherwise very expensive to obtain."

---

## Full Introduction (Section 1)

**Paragraph 1:** "There has been a proliferation of LLM-based chat assistants (chatbots) that leverage supervised instruction fine-tuning and reinforcement learning with human feedback (RLHF) to unlock new instruction following and conversational abilities. Once aligned with humans, these chat models are strongly preferred by human users over the original, unaligned models on which they are built. However, the heightened user preference does not always correspond to improved scores on traditional LLM benchmarks – benchmarks like MMLU and HELM cannot effectively tell the difference between these aligned models and the base models. This phenomenon suggests that there is a fundamental discrepancy between user perceptions of the usefulness of chatbots and the criteria adopted by conventional benchmarks."

**Paragraph 2:** "We argue that this discrepancy primarily arises due to existing evaluation that only measures LLMs' core capability on a confined set of tasks (e.g., multi-choice knowledge or retrieval questions), without adequately assessing its alignment with human preference in open-ended tasks, such as the ability to accurately adhere to instructions in multi-turn dialogues. As a demonstration, we show conversation histories with two models on an MMLU question in Figure 1. The two models are LLaMA-13B, a pre-trained base model without fine-tuning, and Vicuna-13B, our fine-tuned model from LLaMA-13B on high-quality conversations (the training details are in Appendix E). Despite the base LLaMA models showing competitive performance on conventional benchmarks (Table 9), its answers to open-ended questions are often not preferred by humans. This misalignment of conventional benchmarks underscores the core problem driving this paper: the need for a robust and scalable automated method to evaluate LLM alignment with human preferences."

**Paragraph 3:** "To study this, we introduce two benchmarks with human ratings as the primary evaluation metric: MT-bench and Chatbot Arena. MT-bench is a series of open-ended questions that evaluate a chatbot's multi-turn conversational and instruction-following ability – two critical elements for human preference. MT-bench is also carefully constructed to differentiate chatbots based on their core capabilities, such as reasoning and math. In addition, we develop Chatbot Arena, a crowdsourced platform featuring anonymous battles between chatbots in real-world scenarios – Users engage in conversations with two chatbots at the same time and rate their responses based on personal preferences."

**Paragraph 4:** "While human evaluation is the gold standard for assessing human preferences, it is exceptionally slow and costly. To automate the evaluation, we explore the use of state-of-the-art LLMs, such as GPT-4, as a surrogate for humans. Because these models are often trained with RLHF, they already exhibit strong human alignment. We call this approach 'LLM-as-a-judge'. This approach has been tried in our earlier blog post and other concurrent or follow-up work. However, there has not been a systematic study of this approach."

**Paragraph 5:** "In this paper, we study the LLM-as-a-judge approach by comparing it to the gold standard of human evaluation. We examine several potential limitations of the LLM-as-a-judge approach including position bias, verbosity bias, self-enhancement bias, and limited reasoning ability. We show that some of the biases are minor or can be mitigated. Once addressed, our results from 3K controlled expert votes and 3K crowdsourced human votes in the wild verify that GPT-4 judge match human evaluations at an agreement rate exceeding 80%, achieving the same level of human-human agreement (§4.2, Table 4). Consequently, this suggests LLM-as-a-judge is a scalable method to swiftly evaluate human preference, serving as a promising alternative to traditional human evaluations."

**Paragraph 6 (Contributions):** "This paper makes two contributions: (1) a systematic study of LLM-as-a-judge; and (2) human preference datasets with high-quality questions and diverse user interactions from MT-bench and Chatbot Arena. In addition, we argue for the adoption of a hybrid evaluation framework for future LLM benchmarks: by combining the existing capability-based benchmarks and the new preference-based benchmarks with LLM-as-a-judge, one can swiftly and automatically evaluate both the core capabilities and human alignment of models. We publicly release 80 MT-bench questions, 3K expert votes, and 30K conversations with human preferences for future study."

---

## Section 2: MT-Bench and Chatbot Arena

**MT-Bench:** 80 high-quality multi-turn questions across 8 categories: writing, roleplay, extraction, reasoning, math, coding, knowledge I (STEM), knowledge II (humanities/social science). For each category, the authors "manually designed 10 multi-turn questions" to "test multi-turn conversation and instruction-following ability, covering common use cases and focusing on challenging questions to differentiate models." Every question involves two turns to evaluate conversational abilities. Table 1 lists sample questions.

**Chatbot Arena:** "A crowdsourced platform featuring anonymous battles." Users interact with two anonymous models simultaneously, posing the same question to both. They vote for which model provides the preferred response, "with the identities of the models disclosed post-voting." After one month of operation, approximately 30K votes were collected. The platform does not use pre-defined questions, capturing "a wide range of unrestricted use cases and votes in the wild." Models on the platform included GPT-4, GPT-3.5, Claude, Vicuna-7B/13B, Koala-13B, Alpaca-13B, LLaMA-13B, and Dolly-12B.

**Human evaluation (MT-bench):** 58 expert-level human labelers (mostly graduate students from more than ten universities), each evaluating at least 20 random multi-turn questions, compensated at $20 per 20 questions (~$35/hour). Total: ~3K votes. For some questions (math, reasoning), labelers could see a reference solution. A user could skip up to 5 questions. When a human's choice deviated from GPT-4, GPT-4's judgment was additionally shown.

**Human evaluation (Arena):** 2,114 unique IPs, free platform, no registration required. 3K single-turn votes randomly sampled from 30K arena data.

---

## Section 3: LLM as a Judge

### 3.1 Types of LLM-as-a-Judge

Three variations:

1. **Pairwise comparison:** "An LLM judge is presented with a question and two answers, and tasked to determine which one is better or declare a tie." Prompt in Figure 4.
2. **Single answer grading:** "An LLM judge is asked to directly assign a score to a single answer." Prompt in Figure 5.
3. **Reference-guided grading:** "In certain cases, it may be beneficial to provide a reference solution if applicable." Prompt in Figure 7.

"These methods have different pros and cons. For example, the pairwise comparison may lack scalability when the number of players increases, given that the number of possible pairs grows quadratically; single answer grading may be unable to discern subtle differences between specific pairs, and its results may become unstable, as absolute scores are likely to fluctuate more than relative pairwise results if the judge model changes."

### 3.2 Advantages

"LLM-as-a-judge offers two key benefits: scalability and explainability. It reduces the need for human involvement, enabling scalable benchmarks and fast iterations. Additionally, LLM judges provide not only scores but also explanations, making their outputs interpretable."

### 3.3 Limitations

**Position bias:** "Position bias is when an LLM exhibits a propensity to favor certain positions over others. This bias is not unique to our context and has been seen in human decision-making and other ML domains."

Test methodology: Two similar GPT-3.5 answers (temperature=0.7) to each MT-bench first-turn question. Two prompts tested: "default" and "rename" (to test name vs. position bias).

Results (Table 2):
- Claude-v1 default: 23.8% consistency, 75.0% biased toward first; rename: 56.2% consistency
- GPT-3.5 default: 46.2% consistency, 50.0% biased toward first
- GPT-4 default: 65.0% consistency, 30.0% biased toward first; rename: 66.2%

"The position bias can be very significant. Only GPT-4 outputs consistent results in more than 60% of cases." Origin: "we suspect that it could be rooted in the training data or inherent to the left-to-right architecture of causal transformers."

**Verbosity bias:** "Verbosity bias is when an LLM judge favors longer, verbose responses, even if they are not as clear, high-quality, or accurate as shorter alternatives."

Test: "repetitive list" attack on 23 MT-bench answers containing numbered lists. GPT-4 asked to rephrase list items and insert rephrased version at beginning (e.g., 5-item list becomes 10-item with first 5 rephrased). "We define the attack is successful if an LLM judge thinks the new response is better than the old response."

Results (Table 3 - failure rate):
- Claude-v1: 91.3%
- GPT-3.5: 91.3%
- GPT-4: 8.7%

"LLM judges are able to correctly judge identical answers (i.e., they always return a tie for two identical answers) but cannot pass the more advanced 'repetitive list' attack."

**Self-enhancement bias:** "LLM judges may favor the answers generated by themselves." Observation: GPT-4 favors itself with a 10% higher win rate; Claude-v1 favors itself with a 25% higher win rate. "However, they also favor other models and GPT-3.5 does not favor itself. Due to limited data and small differences, our study cannot determine whether the models exhibit a self-enhancement bias."

**Limited capability in math/reasoning:** "LLMs are known to have limited math and reasoning capability, which results in its failure of grading such questions because they do not know the correct answers. However, what is more intriguing is that it also shows limitations in grading basic math problems which it is capable of solving." GPT-4, when asked separately, can solve the problem, but "was misled by the provided answers, ultimately resulting in incorrect judgment." Same weakness in GPT-3.5 and Claude-v1.

### 3.4 Addressing Limitations

**Swapping positions:** "A conservative approach is to call a judge twice by swapping the order of two answers and only declare a win when an answer is preferred in both orders. If the results are inconsistent after swapping, we can call it a tie. Another more aggressive approach is to assign positions randomly, which can be effective at a large scale with the correct expectations. In the following experiments, we use the conservative one."

**Few-shot judge:** Three judgment examples covering A-better, B-better, and tie cases. "Few-shot judge can significantly increase the consistency of GPT-4 from 65.0% to 77.5%." However, "the longer prompts make API calls 4× more expensive." Zero-shot used by default.

**Chain-of-thought + reference-guided (Table 4 - math failure rate on 10 questions):**
- Default prompt: 14/20 failures (70%)
- CoT prompt: 6/20 failures (30%)
- Reference-guided: 3/20 failures (15%)

Reference-guided method: "we first generate LLM judge's answer independently, and then display it as a reference answer in the judge prompt."

"Even with the CoT prompt, we find that in many cases LLM makes exactly the same mistake as the given answers in its problem-solving process."

**Fine-tuning a judge model:** Vicuna-13B fine-tuned on arena data (explored in Appendix F).

### 3.5 Multi-turn Judge

Two design options compared: (1) breaking into two separate prompts; (2) complete conversation in single prompt. Option 1 caused LLM judge to "struggle to locate the assistant's previous response precisely." Figure 15 shows GPT-4 making inaccurate judgment due to faulty reference. Option 2 (single prompt showing full conversations) "significantly alleviate the aforementioned referencing issue."

---

## Section 4: Agreement Evaluation

### 4.1 Setup

- 6 models evaluated: GPT-4, GPT-3.5, Claude-V1, Vicuna-13B, Alpaca-13B, LLaMA-13B
- 58 expert human labelers for MT-bench (~3K votes)
- 2,114 unique IPs for Arena (3K votes sampled from 30K)
- Two setups: S1 (non-tie + tie + inconsistent counted as tie; random baseline 33%), S2 (non-tie only; random baseline 50%)
- Agreement = "probability of randomly selected individuals (but not identical) of each type agreeing on a randomly selected question"

### 4.2 High Agreement Between GPT-4 and Humans

**Table 5 (MT-bench) key numbers:**
- Human-Human: 63% (S1), 81% (S2)
- GPT-4 Pairwise vs. Human: 66% (S1), 85% (S2)
- GPT-4 Single vs. Human: 60% (S1), 85% (S2)

"The agreement under setup S2 (w/o tie) between GPT-4 and humans reaches 85%, which is even higher than the agreement among humans (81%)."

"During our data collection, when a human's choice deviated from GPT-4, we presented GPT-4's judgments to humans and ask if they are reasonable. Despite different views, humans deemed GPT-4's judgments reasonable in 75% of cases and are even willing to change their choices in 34% of cases."

**Table 6 (Chatbot Arena) key numbers (Setup S2):**
- GPT-4 vs. Human: 87%
- GPT-4-Single vs. Human: 85%
- GPT-3.5 vs. Human: 83%
- Claude vs. Human: 84%

"Comparing GPT-4 and other LLM judges, we find they reach a similar non-tie agreement ratio between humans but the number of non-tied votes from GPT-4 is much larger. This means that GPT-4 is more affirmative and less suffered from position bias."

**Table 7 (win rate difference vs. agreement):** "The agreement between GPT-4 and human progressively increases in line with the performance disparity of the model pairs (i.e., larger win rate difference), from 70% to nearly 100%."

"GPT-4 with single-answer grading matches both pairwise GPT-4 and human preferences very well. This means GPT-4 has a relatively stable internal rubric. Although it may sometimes perform slightly worse than pairwise comparison and give more tie votes, it is a more scalable method."

### 4.3 Win Rates Under Different Judges

**Table 8 (Category-wise win rate):**

| Model | Writing | Roleplay | Reasoning | Math | Coding | Extraction | STEM | Humanities |
|---|---|---|---|---|---|---|---|---|
| GPT-4 | 61.2% | 67.9% | 49.3% | 66.1% | 56.3% | 66.2% | 76.6% | 72.2% |
| GPT-3.5 | 50.9% | 60.6% | 32.6% | 63.8% | 55.0% | 48.8% | 52.8% | 53.8% |
| Vicuna-13B | 39.7% | 39.2% | 20.1% | 18.0% | 36.9% | 29.2% | 47.0% | 47.5% |
| LLaMA-13B | 15.1% | 15.1% | 7.8% | 7.5% | 2.1% | 9.3% | 6.8% | 10.1% |

**Table 9 (Model variants):**

| Model | #Training Tokens | MMLU (5-shot) | TruthfulQA | MT-Bench Score |
|---|---|---|---|---|
| LLaMA-7B | 1T | 35.2 | 0.22 | 2.74 |
| LLaMA-13B | 1T | 47.0 | 0.26 | 2.61 |
| Alpaca-7B | 4.4M | 40.1 | 0.26 | 4.54 |
| Alpaca-13B | 4.4M | 48.1 | 0.30 | 4.53 |
| Vicuna-7B (selected) | 4.8M | 37.3 | 0.32 | 5.95 |
| Vicuna-7B (single) | 184M | 44.1 | 0.30 | 6.04 |
| Vicuna-7B (all) | 370M | 47.1 | 0.32 | 6.00 |
| Vicuna-13B (all) | 370M | 52.1 | 0.35 | 6.39 |
| GPT-3.5 | — | 70.0 | — | 7.94 |
| GPT-4 | — | 86.4 | — | 8.99 |

"On MT-bench second turn, proprietary models like Claude and GPT-3.5 are more preferred by the humans compared to the first turn, meaning that a multi-turn benchmark can better differentiate some advanced abilities of models."

"Fine-tuning on high-quality dialog datasets (i.e., ShareGPT) can consistently improve the model performance on MMLU." Small high-quality conversation datasets teach "a style preferred by GPT-4 (or approximately human) but cannot improve MMLU significantly."

---

## Section 5: Human Preference Benchmark and Standardized Benchmark

"No single benchmark can determine model quality, meaning that a comprehensive evaluation is needed." The two benchmark types complement each other. Traditional benchmarks (MMLU, TruthfulQA) measure core capabilities; MT-bench/Arena measure human preference alignment. "We argue for a hybrid evaluation framework." Leaderboard hosted at https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard.

---

## Section 6: Discussion / Limitations / Future Work

**Limitations:**
1. "This paper emphasizes helpfulness but largely neglects safety. Honesty and harmlessness are crucial for a chat assistant as well."
2. "Within helpfulness, there are multiple dimensions like accuracy, relevance, and creativity, but they are all combined into a single metric in this study. A more comprehensive evaluation can be developed by analyzing and separating these dimensions."
3. "We present preliminary solutions to address the limitations and biases of LLM judges, and we anticipate more advanced methods can be developed."

**Societal Impact:** "Our evaluation methods can help enhance chatbot quality and user experiences." Risk: "Advanced chat assistants may replace certain human tasks, resulting in job displacements and new opportunities."

**Future Directions:**
1. "Benchmarking chatbots at scale with a broader set of categories"
2. "Open-source LLM judge aligned with human preference"
3. "Enhancing open models' math/reasoning capability"

---

## Conclusion

"In this paper, we propose LLM-as-a-judge for chatbot evaluation and systematically examine its efficacy using human preference data from 58 experts on MT-bench, as well as thousands of crowd-users on Chatbot Arena. Our results reveal that strong LLMs can achieve an agreement rate of over 80%, on par with the level of agreement among human experts, establishing a foundation for an LLM-based evaluation framework."

---

## All Figure Captions

- **Figure 1:** "Multi-turn dialogues between a user and two AI assistants—LLaMA-13B (Assistant A) and Vicuna-13B (Assistant B)—initiated by a question from the MMLU benchmark and a follow-up instruction. GPT-4 is then presented with the context to determine which assistant answers better."
- **Figure 2:** "Average win rate of six models under different judges on MT-bench."
- **Figure 3:** "Average win rate of nine models under different judges on Chatbot Arena."
- **Figure 4:** "The default prompt for pairwise comparison."
- **Figure 5:** "The default prompt for single answer grading."
- **Figure 6:** "The chain-of-thought prompt for math and reasoning questions."
- **Figure 7:** "The prompt for reference-guided pairwise comparison."
- **Figure 8:** "The prompt for multi-turn pairwise comparison."
- **Figure 9:** "The prompt for reference-guided multi-turn single-answer grading."
- **Figure 10:** "An example of position bias. When Assistant A is placed in the first position, GPT-4 thinks A is better, but its verdict changes when we swap the position of A and B. We observe similar pattern from other LLM judges such as Claude/GPT-3.5."
- **Figure 11:** "An example of 'repetitive list' attack to examine verbosity bias. Except for the two rephrased items (highlighted in red), Assistant A's answer is exactly the same as Assistant B. Both GPT-3.5 and Claude-v1 show a verbosity bias towards the longer and repetitive answer. Only GPT-4 successfully detected this attack."
- **Figure 12:** "With a default prompt, GPT-4 shows limited capability in grading math questions. Despite being able to answer the question itself, its judgment was influenced by the given answers, leading to arithmetic mistakes highlighted in yellow."
- **Figure 13:** "An example of GPT-4's limited capability in grading reasoning question. Despite GPT-4 knows how to solve the question (if asked separately), it made a wrong judgement saying both assistants' wrong answers are correct."
- **Figure 14:** "An example of GPT-4's wrong judgment with chain-of-thought prompt. We can see GPT-4 exactly copied Assistant B's answer (which contains arithmetic errors) and determined Assistant A's answer is incorrect. This suggest GPT-4's chain-of-thought process can be significantly influenced by the given answers despite we ask it to think independently."
- **Figure 15:** "In this example, despite Assistant A correctly followed user's instruction to generate a concrete plan for the second example of its previous response, GPT-4 wrongly referred to the second example in Assistant B's response, resulting in a wrong judgment. This suggests the prompt design that breaks the questions into two prompts may cause LLM judge struggle to locate assistants' previous responses."
- **Figure 16:** "The screenshot of MT-bench data collection. We show an instruction similar to the prompt we give to GPT-4. We present questions from MT-bench and answers from two random anonymous assistants and ask which one is better. We present the first-turn conversation and ask humans to vote, then repeat the same procedure for the second-turn. A user can skip up to 5 questions if they are not confident. For some questions (e.g., math, reasoning), they can also see a reference solution."
- **Figure 17:** "The screenshot of MT-bench data collection. When human's vote differs from GPT-4, we additionally show GPT-4's judgment (red region in the screenshot) and ask the user to click one of the three buttons to decide whether GPT-4's judgment is reasonable."
- **Figure 18:** "The screenshot of Chatbot Arena."
- **Figure 19:** "Category-wise scores of 6 models on MT-bench."

---

## All Table Captions

- **Table 1:** "Sample multi-turn questions in MT-bench."
- **Table 2:** "Position bias of different LLM judges. Consistency is the percentage of cases where a judge gives consistent results when swapping the order of two assistants. 'Biased toward first' is the percentage of cases when a judge favors the first answer. 'Error' indicates wrong output formats. The two largest numbers in each column are in bold."
- **Table 3:** "Failure rate under 'repetitive list' attack for different LLM judges on 23 answers."
- **Table 4:** "Judge failure rate on 10 math questions with different prompts. We test LLaMA-13B vs. Vicuna-13B and swap positions. A failure means when GPT-4 says an incorrect answer is correct."
- **Table 5:** "Agreement between two types of judges on MT-bench. 'G4-Pair' and 'G4-Single' denote GPT-4 with pairwise comparison and single-answer grading respectively. The single-answer grading can be converted into pairwise comparison results for calculating the agreement. We report two setups: 'S1' includes non-tie, tie, and inconsistent (due to position bias) votes and counts inconsistent as tie; 'S2' only includes non-tie votes. The agreement between two random judges under each setup is denoted as 'R='. The top value in each cell is the agreement, and the bottom gray value is #votes."
- **Table 6:** "Agreement between two types of judges on Chatbot Arena. 'G4-S' denotes GPT-4 with single-answer grading. 'G4', 'G3.5' and 'C' denote GPT-4, GPT-3.5, and Claude with pairwise comparison, respectively. 'H' denotes human. The remaining of table follows the same format as Table 5(b)."
- **Table 7:** "Agreement and win rate difference. Each point corresponds to a model pair and counts only the non-tie votes between the two models. The x-axis value is the win rate difference between the two models. The y-axis value is the GPT-4 and human agreement."
- **Table 8:** "Category-wise win rate of models."
- **Table 9:** "Evaluation results of several model variants."
- **Table 10:** "Position bias on different models and prompts."
- **Table 11:** "Position bias on different categories."
- **Table 12:** "Position bias on different model pairs."
- **Table 13:** "Improvements of the few-shot judge on consistency for position bias."
- **Table 14:** "Agreement between two types of judges on MT-bench [extended]."
- **Table 15:** "Dataset statistics [Vicuna training]."
- **Table 16:** "Position bias of the Vicuna-13B model without and with further fine-tuning."

---

## Implementation Details

- **Models evaluated:** GPT-4, GPT-3.5, Claude-V1, Vicuna-13B, Alpaca-13B, LLaMA-13B (MT-bench); additionally GPT-4, GPT-3.5, Claude, Vicuna-7B/13B, Koala-13B, Alpaca-13B, Dolly-12B (Arena)
- **MT-bench scoring:** GPT-4 asked to give a score for each turn on a scale of 10; average over 160 turn scores (80 questions × 2 turns)
- **Position bias mitigation (conservative):** Judge called twice with swapped answer order; win only declared when preferred in both orders; inconsistent → tie
- **Few-shot:** 3 examples (A better, B better, tie); 4× more expensive
- **Math/CoT prompt:** Judge prompted to answer question independently before grading
- **Reference-guided:** Judge's own answer generated independently, then used as reference in judge prompt
- **Multi-turn prompt:** Full conversations displayed in single prompt; judge asked to focus on second question
- **Human labeler compensation:** $20 per 20 questions (~$35/hour); graduate students from 10+ universities
- **Arena:** Free platform, no registration, 2,114 unique IPs

---

## Appendix E: Vicuna Training Details

- **Data source:** ShareGPT.com user-shared conversations; 125K conversations after HTML→markdown conversion and quality filtering
- **Three dataset variants:**
  - "Selected" (3K seqs, 4.8M tokens, 4.0 avg turns, 343 tokens/response): high-quality, ≥3 turns, GPT-4-generated, cluster-sampled centroids
  - "Single" (257K seqs, 184M tokens, 1.0 avg turns, 473 tokens/response): first-turn only
  - "All" (257K seqs, 370M tokens, 2.9 avg turns, 373 tokens/response): full conversations
- **Hyperparameters:** batch size=128, lr=2e-5, 3 epochs (5 for Selected), seq length=2048
- **Hardware:** 8× A100 GPUs; longest run ~2 days
- **Infrastructure:** SkyPilot spot instances + FlashAttention

---

## Appendix F: Exploring Vicuna as Judge

**F.1 Zero-Shot Vicuna-13B:**
- Consistency: 11.2%–16.2% across prompts (vs. GPT-4's 65%)
- Error rate: 22.5%–78.8% (wrong output format, natural language responses instead of following template)
- Unsuitable for automated evaluation without fine-tuning

**F.2 Arena Fine-tuned Vicuna-13B:**
- Training data: 22K single-turn arena votes (20K train, 2K validation)
- Task formulation: 3-way sequence classification (A better / B better / tie, distinguishing both-bad from tie)
- Training: 3 epochs, cosine LR schedule, max LR=2e-5
- Hyperparameters chosen on 2K validation set; tested on same 3K dataset as main paper
- Position bias consistency: improved from 16.2% → 65.0%; error rate: 0%
- Agreement with humans (S2/no tie): 85.5% (vs. GPT-4's 87%)
- Conclusion: "strong potential to be used as a cheap open-sourced replacement for expensive closed-sourced LLMs"

---

## Appendix D: Additional Experiments

**D.1 Position bias by category (Table 11):**
- Writing: 42.0% consistency (high bias)
- Math/Coding: 86.0% consistency (low bias)
- "Position bias is more noticeable on open questions like writing and stem/humanity knowledge questions"

**D.1 Position bias by model pair (Table 12):**
- GPT-3.5 vs. LLaMA-13B: 98.8% consistency (large performance gap)
- GPT-3.5 vs. Claude-V1: 67.5% consistency (small performance gap)

**D.2 Few-shot improvements (Table 13):**
- GPT-4: 65.0% → 77.5%
- Claude-v1: 23.8% → 63.7%
- GPT-3.5: 46.2% → 55.0%

**D.3 Agreement evaluation methodology:**
- Human-majority judge = majority vote across human raters (upper bound)
- When no majority: agreement split evenly (e.g., 50-50 split + GPT-4 picks one = 0.5 contribution)
- GPT-4 pairwise vs. human (S1/S2): 70%/97% first turn; 66%/85% overall

**D.4 Category-wise single-answer grading (Figure 19):**
- GPT-4 strongest in STEM (76.6%), weakest in Reasoning (49.3%)
- Vicuna-13B: notably worse in reasoning, math, coding vs. GPT-3.5/4
- LLaMA-13B: 2.1% coding, 7.5% math (dramatic drops)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "571c91ad-7528-4406-8619-3cf2869896ba",
  "isSidechain": true,
  "agentId": "ace90c699656f23d3",
  "requestId": "req_011CbG3uNcjxK9gQnsd4shm7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87890f18-ec29-4949-98fa-76f0cf5fb0a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L1aWZQnUL7VrxjXSMs57ZH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 51621,
      "output_tokens": 8035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 851
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8035,
          "cache_read_input_tokens": 51621,
          "cache_creation_input_tokens": 851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 851,
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
