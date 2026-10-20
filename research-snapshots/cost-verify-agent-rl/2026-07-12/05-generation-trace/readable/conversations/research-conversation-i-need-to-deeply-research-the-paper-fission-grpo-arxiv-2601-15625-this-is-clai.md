# Research conversation: I need to deeply research the paper "Fission-GRPO" (arXiv:2601.15625). This is claimed to be an ACL 2026 paper titled "R

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a878e485d3c9127b8.jsonl`
- **Structured JSON:** [`a422bb56742b4f4c3ab7.json`](../../sessions/a4/a422bb56742b4f4c3ab7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-11T23:28:53.602Z_

I need to deeply research the paper "Fission-GRPO" (arXiv:2601.15625). This is claimed to be an ACL 2026 paper titled "Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors" by Zhiwei Zhang et al.

Please:
1. Use WebSearch to find this paper with queries like "Fission-GRPO arXiv 2601.15625", "Fission-GRPO error recovery tool use GRPO", and "Fission GRPO ACL 2026"
2. Use WebFetch to read the actual paper abstract and method sections from arxiv.org
3. Search for any follow-up work citing Fission-GRPO

I need to understand:
- What exactly is the "fission" mechanism? How does it create new training instances from failed trajectories?
- What is the "Error Simulator" they train?
- How do they resample G' parallel recovery attempts?
- What benchmarks do they use? What are their main results?
- Do they condition on error TYPE? Or just error occurrence?
- How does their branching differ from tree-based branching (ARPO, Tree-GRPO)?
- Is their code publicly available?

Report all findings in detail. If the paper doesn't exist at that arXiv ID, report that clearly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "8708317c-b142-49a0-9acd-28b3ce80d680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:28:53.606Z_

```json
{
  "parentUuid": "8708317c-b142-49a0-9acd-28b3ce80d680",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
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
  "uuid": "f0d626d3-30af-4c8e-a458-07f7f9df0164",
  "timestamp": "2026-05-11T23:28:53.606Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:28:59.356Z_



I'll research this paper thoroughly. Let me start by loading the WebSearch and WebFetch tools, then conduct multiple searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0d626d3-30af-4c8e-a458-07f7f9df0164",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CaweeXZb5iVdQtsvMdMn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb76107d-fa8e-46dd-a832-dcd1eebf2265",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Py4HaQqCe4bwLzm7aRop5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 866,
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

_source line 4 · 2026-05-11T23:28:59.594Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NPanf4mAkPkeJmhriPaUni`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb76107d-fa8e-46dd-a832-dcd1eebf2265",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CaweeXZb5iVdQtsvMdMn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee6fe88e-4449-4a02-9a48-2c781113d2cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Py4HaQqCe4bwLzm7aRop5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 866,
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

_source line 5 · 2026-05-11T23:28:59.604Z_

<details><summary>↩ Tool result · `toolu_01NPanf4mAkPkeJmhriPaUni`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parentUuid": "ee6fe88e-4449-4a02-9a48-2c781113d2cb",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "ed2fbd70-8338-47bb-b687-a9c83ccf919d",
  "sourceToolAssistantUUID": "ee6fe88e-4449-4a02-9a48-2c781113d2cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:29:02.709Z_



Now let me run multiple searches in parallel to find this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed2fbd70-8338-47bb-b687-a9c83ccf919d",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CaweeyxatpaHCBBi5fzRA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27c7712e-0a3a-417b-9d10-b59792bf88c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uaKkNdiVDRDmfMq8VTSc7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 7 · 2026-05-11T23:29:03.809Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VfditGdRLmw1Auoia9NAio`</summary>

```json
{
  "query": "Fission-GRPO arXiv 2601.15625"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27c7712e-0a3a-417b-9d10-b59792bf88c4",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CaweeyxatpaHCBBi5fzRA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3640f858-1860-4c83-8175-456c787bb8be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uaKkNdiVDRDmfMq8VTSc7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 8 · 2026-05-11T23:29:04.309Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011kZSp4ucHRZH174aVuNGWJ`</summary>

```json
{
  "query": "Fission-GRPO error recovery tool use GRPO reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3640f858-1860-4c83-8175-456c787bb8be",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CaweeyxatpaHCBBi5fzRA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3359ced-5597-41bf-8810-f9c29e85b29f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uaKkNdiVDRDmfMq8VTSc7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 9 · 2026-05-11T23:29:04.735Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DowcmKC93vHCJvnnY6oUgQ`</summary>

```json
{
  "query": "\"Fission-GRPO\" ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3359ced-5597-41bf-8810-f9c29e85b29f",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CaweeyxatpaHCBBi5fzRA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed10cf53-e003-4360-86e7-05446423f7ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uaKkNdiVDRDmfMq8VTSc7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9089,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 181,
          "cache_read_input_tokens": 9089,
          "cache_creation_input_tokens": 1916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1916,
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

_source line 10 · 2026-05-11T23:29:10.456Z_

<details><summary>↩ Tool result · `toolu_01DowcmKC93vHCJvnnY6oUgQ`</summary>

```text
Web search results for query: ""Fission-GRPO" ACL 2026"

Links: [{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"GitHub - ProgressLM/ProgressLM: [ACL 2026 Main] How far can VLMs go in understanding long-horizon action progress from just a single observation? A promising early exploration · GitHub","url":"https://github.com/ProgressLM/ProgressLM"},{"title":"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/html/2601.15625v1"},{"title":"[2601.15625] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625"},{"title":"Workshop on Fission Dynamics 2026 (11-May 15, 2026): Overview · 北京大学会议平台 (Indico)","url":"https://indico.pku.edu.cn/event/52/"},{"title":"Turn-Level Advantage Estimation with PPO for Improved ...","url":"https://aclanthology.org/2026.findings-eacl.328.pdf"},{"title":"GitHub - sustech-nlp/SPPO: [ACL 2026 Main] SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks official repos. · GitHub","url":"https://github.com/sustech-nlp/SPPO"},{"title":"ACL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2026%2FConference"},{"title":"Paper page - Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://huggingface.co/papers/2601.15625"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's what I found about Fission-GRPO and ACL 2026:

## Fission-GRPO Overview

Fission-GRPO is a framework that converts execution errors into corrective supervision within the RL training loop. The approach addresses a key problem with LLMs in tool use: Large language models can call tools effectively, yet they remain brittle in multi-turn execution, and this brittleness hinders reliable real-world deployment where execution errors are inherently inevitable.

## How It Works

The framework operates in three stages: Stage 1 performs standard GRPO exploration, Stage 2 augments failed rollouts with diagnostic feedback from a learned Error Simulator, and Stage 3 triggers a fission update where each error is expanded into parallel recovery attempts by resampling new rollouts conditioned on the augmented context.

## Performance Results

On the BFCL v4 Multi-Turn, Fission-GRPO improves the error recovery rate of Qwen3-8B by 5.7% absolute, yielding a 4% overall accuracy gain (42.75% to 46.75%) over GRPO and outperforming specialized tool-use agents.

While the search results confirm that Fission-GRPO is a recent research contribution (published in January 2026), I did not find specific information confirming it as an ACL 2026 conference paper. ACL 2026 will take place in San Diego, California, from July 2-7, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed10cf53-e003-4360-86e7-05446423f7ab",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "acb70138-bbb5-4f15-b70c-ba44cfb14c4e",
  "sourceToolAssistantUUID": "ed10cf53-e003-4360-86e7-05446423f7ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-11T23:29:11.061Z_

<details><summary>↩ Tool result · `toolu_01VfditGdRLmw1Auoia9NAio`</summary>

```text
Web search results for query: "Fission-GRPO arXiv 2601.15625"

Links: [{"title":"[2601.15625] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625"},{"title":"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/html/2601.15625"},{"title":"[Paper Note] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors, Zhiwei Zhang+, arXiv'26, 2026.01 · Issue #4277 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4277"},{"title":"[2601.23135] Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients","url":"https://arxiv.org/abs/2601.23135"},{"title":"Counterfactual Self-Questioning for Stable Policy Optimization in Language Models","url":"https://arxiv.org/html/2601.00885v1"},{"title":"On the extraction of fission mode properties from fragment mass distributions","url":"https://arxiv.org/html/2410.02187v1"},{"title":"[1705.00052] Nuclear Fission: from more phenomenology and adjusted parameters to more fundamental theory and increased predictive power","url":"https://arxiv.org/abs/1705.00052"},{"title":"CVeDRL: An Efficient Code Verifier via Difficulty-aware Reinforcement Learning","url":"https://arxiv.org/html/2601.22803"},{"title":"TAGRPO: Boosting GRPO on Image-to-Video Generation with Direct Trajectory Alignment","url":"https://arxiv.org/html/2601.05729"},{"title":"MTDrive: Multi-turn Interactive Reinforcement Learning for Autonomous Driving","url":"https://arxiv.org/html/2601.22930"}]

I found the paper for you! Here are the key details about Fission-GRPO (arXiv 2601.15625):

## Paper Overview

**Title:** "Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors"

**Authors:** Zhiwei Zhang and 8 other authors

**Publication Date:** January 22, 2026

## Problem Being Addressed

Large language models (LLMs) can call tools effectively, yet they remain brittle in multi-turn execution: following a tool call error, smaller models often degenerate into repetitive invalid re-invocations, failing to interpret error feedback and self-correct.

## Solution: Fission-GRPO Framework

The core mechanism fissions each failed trajectory into a new training instance by augmenting it with diagnostic feedback from a finetuned Error Simulator, then resampling recovery rollouts on-policy. This enables the model to learn from the precise errors it makes during exploration, rather than from static, pre-collected error cases.

## Results

On the BFCL v4 Multi-Turn, Fission-GRPO improves the error recovery rate of Qwen3-8B by 5.7% absolute, crucially, yielding a 4% overall accuracy gain (42.75% to 46.75%) over GRPO and outperforming specialized tool-use agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3640f858-1860-4c83-8175-456c787bb8be",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "69aefa50-ca54-40c0-a10e-53ca298c763f",
  "sourceToolAssistantUUID": "3640f858-1860-4c83-8175-456c787bb8be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:29:13.052Z_

<details><summary>↩ Tool result · `toolu_011kZSp4ucHRZH174aVuNGWJ`</summary>

```text
Web search results for query: "Fission-GRPO error recovery tool use GRPO reinforcement learning"

Links: [{"title":"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/html/2601.15625v1"},{"title":"[2601.15625] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625"},{"title":"[2601.15625v1] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625v1"},{"title":"[Paper Note] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors, Zhiwei Zhang+, arXiv'26, 2026.01 · Issue #4277 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4277"},{"title":"Paper page - Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://huggingface.co/papers/2601.15625"},{"title":"[Literature Review] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://www.themoonlight.io/en/review/robust-tool-use-via-fission-grpo-learning-to-recover-from-execution-errors"},{"title":"Reinforcement Learning (RL) Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical","url":"https://arxiv.org/pdf/2402.03300"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"}]

Based on the search results, here's what I found about Fission-GRPO:

## Overview

Fission-GRPO is a framework that converts execution errors into corrective supervision within the RL training loop. Large language models (LLMs) can call tools effectively, yet they remain brittle in multi-turn execution: following a tool call error, smaller models often degenerate into repetitive invalid re-invocations, failing to interpret error feedback and self-correct, which hinders reliable real-world deployment.

## The Problem It Addresses

Standard reinforcement learning (RL) treats errors as sparse negative rewards, providing no guidance on how to recover, while pre-collected synthetic error-correction datasets suffer from distribution mismatch with the model's on-policy error modes.

## How Fission-GRPO Works

The framework operates in three stages: Stage 1 performs standard GRPO exploration, sampling multiple rollouts per query. In Stage 2, failed rollouts are intercepted and augmented with diagnostic feedback from a learned Error Simulator, constructing corrective contexts. In Stage 3, each error is expanded into parallel recovery attempts by resampling new rollouts conditioned on the augmented context.

The Error Simulator is trained via supervised fine-tuning to produce realistic, context-aware diagnostics that resemble runtime error traces.

## Performance Results

On the BFCL v4 Multi-Turn benchmark, Fission-GRPO achieves state-of-the-art performance across the Qwen3 model family (1.7B, 4B, and 8B), consistently outperforming GRPO, DAPO, and Dr.GRPO baselines. For Qwen3-8B, the method improves the error recovery rate by 5.7% absolute, yielding a 4% overall accuracy gain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3359ced-5597-41bf-8810-f9c29e85b29f",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "8f647c74-0f77-4158-9e88-eb2f470b2803",
  "sourceToolAssistantUUID": "c3359ced-5597-41bf-8810-f9c29e85b29f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-11T23:29:16.634Z_

The paper exists. Now let me fetch the actual paper content for detailed technical understanding, and search for follow-up work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f647c74-0f77-4158-9e88-eb2f470b2803",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawefxjhKaKvhA69CZpMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c968ef0-67bf-4f31-967e-e97dd5f1e2f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122ZJ81e49ndWZcjz78MV2D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 941,
      "cache_creation_input_tokens": 2087,
      "cache_read_input_tokens": 11005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2087,
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

_source line 14 · 2026-05-11T23:29:18.527Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JYNHQWnv9JdNbhKuzeRbPr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.15625",
  "prompt": "Extract the complete abstract, all author names and affiliations, submission date, and any mentions of conference acceptance (ACL 2026 or other). Also extract any links to code repositories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c968ef0-67bf-4f31-967e-e97dd5f1e2f6",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawefxjhKaKvhA69CZpMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f018c1e8-4bb7-4291-bf50-b7c89696fad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122ZJ81e49ndWZcjz78MV2D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 941,
      "cache_creation_input_tokens": 2087,
      "cache_read_input_tokens": 11005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2087,
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

### Tool result

_source line 15 · 2026-05-11T23:29:23.693Z_

<details><summary>↩ Tool result · `toolu_01JYNHQWnv9JdNbhKuzeRbPr`</summary>

```text
# Paper Information

## Abstract
"Large language models (LLMs) can call tools effectively, yet they remain brittle in multi-turn execution: after a tool-call error, smaller models often fall into repetitive invalid re-invocations instead of interpreting the feedback and recovering." The authors propose Fission-GRPO, which transforms execution errors into corrective training instances. Testing shows improvements of 5.7% on error recovery and 4.0% overall accuracy for Qwen3-8B, with gains up to 17.4% on additional benchmarks.

## Authors
1. Zhiwei Zhang
2. Fei Zhao
3. Rui Wang
4. Zezhong Wang
5. Bin Liang
6. Jiakang Wang
7. Yao Hu
8. Shaosheng Cao
9. Kam-Fai Wong

**Affiliations**: Not provided in the accessible content.

## Submission Information
- **Initial Submission**: January 22, 2026
- **Latest Revision**: April 20, 2026 (v2)
- **arXiv ID**: 2601.15625

## Conference Acceptance
"Accepted to ACL 2026 Main Conference"

## Code Repositories
No code repository links were mentioned in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f018c1e8-4bb7-4291-bf50-b7c89696fad1",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "4f4afc5f-bc97-498d-8898-47b0378dfb0a",
  "sourceToolAssistantUUID": "f018c1e8-4bb7-4291-bf50-b7c89696fad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-11T23:29:24.364Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M9f6sbCgf7WcxUoi9urHoA`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.15625v1",
  "prompt": "Extract the full technical details of the paper including: 1) The complete fission mechanism - how exactly failed trajectories are split into new training instances, 2) The Error Simulator - how it is trained, what it produces, what data it uses, 3) How G' parallel recovery attempts are resampled - the exact procedure, 4) Whether they condition on error TYPE or just error occurrence, 5) All benchmarks used and their main quantitative results (tables if possible), 6) How their branching differs from tree-based approaches like ARPO or Tree-GRPO, 7) The reward function design, 8) Any ablation studies, 9) Code availability. Be as detailed and technical as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f4afc5f-bc97-498d-8898-47b0378dfb0a",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawefxjhKaKvhA69CZpMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d3b6bf3-e777-4216-b1b8-2c30a109dba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122ZJ81e49ndWZcjz78MV2D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 941,
      "cache_creation_input_tokens": 2087,
      "cache_read_input_tokens": 11005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2087,
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

_source line 17 · 2026-05-11T23:29:25.155Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ASKKMLwN8LGjiC998iPqfW`</summary>

```json
{
  "url": "https://huggingface.co/papers/2601.15625",
  "prompt": "Extract any discussion, community comments, links to code/models, and any additional details about the Fission-GRPO paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d3b6bf3-e777-4216-b1b8-2c30a109dba6",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawefxjhKaKvhA69CZpMH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f2debf7-1322-49e1-b10a-838f44dbbb62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122ZJ81e49ndWZcjz78MV2D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 941,
      "cache_creation_input_tokens": 2087,
      "cache_read_input_tokens": 11005,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2087
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 941,
          "output_tokens": 463,
          "cache_read_input_tokens": 11005,
          "cache_creation_input_tokens": 2087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2087,
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

_source line 18 · 2026-05-11T23:29:25.866Z_

<details><summary>↩ Tool result · `toolu_01ASKKMLwN8LGjiC998iPqfW`</summary>

```text
&lt;persisted-output>
Output too large (64.9KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-/3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c/tool-results/toolu_01ASKKMLwN8LGjiC998iPqfW.txt

Preview (first 2KB):
Title: Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors

URL Source: https://arxiv.org/html/2601.15625

Markdown Content:
Zhiwei Zhang 1, Fei Zhao 2, Rui Wang 1, Zezhong Wang 1, 

Bin Liang 1, Jiakang Wang 2, Yao Hu 2, Shaosheng Cao 2, Kam-Fai Wong 1
1 The Chinese University of Hong Kong, 

2 Xiaohongshu Inc. 

zhangzhiwei1019@link.cuhk.edu.hk, caoshaosheng@xiaohongshu.com

###### Abstract

Large language models (LLMs) can call tools effectively, yet they remain brittle in multi-turn execution: following a tool call error, smaller models often degenerate into repetitive invalid re-invocations, failing to interpret error feedback and self-correct. This brittleness hinders reliable real-world deployment, where the execution errors are inherently inevitable during tool interaction procedures. We identify a key limitation of current approaches: standard reinforcement learning (RL) treats errors as sparse negative rewards, providing no guidance on how to recover, while pre-collected synthetic error-correction datasets suffer from distribution mismatch with the model’s on-policy error modes. To bridge this gap, we propose Fission-GRPO, a framework that converts execution errors into corrective supervision within the RL training loop. Our core mechanism fissions each failed trajectory into a new training instance by augmenting it with diagnostic feedback from a finetuned Error Simulator, then resampling recovery rollouts on-policy. This enables the model to learn from the precise errors it makes during exploration, rather than from static, pre-collected error cases. On the BFCL v4 Multi-Turn, Fission-GRPO improves the error recovery rate of Qwen3-8B by 5.7% absolute, crucially, yielding a 4% overall accuracy gain (42.75% →\rightarrow 46.75%) over GRPO and outperforming specialized tool-use agents.

Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f2debf7-1322-49e1-b10a-838f44dbbb62",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "1b70c7a2-52d7-4db8-acea-d19c47064d6a",
  "sourceToolAssistantUUID": "5f2debf7-1322-49e1-b10a-838f44dbbb62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T23:29:47.375Z_

<details><summary>↩ Tool result · `toolu_01M9f6sbCgf7WcxUoi9urHoA`</summary>

```text
# Technical Details: Fission-GRPO Framework

## 1. Fission Mechanism

The core fission process converts failed trajectories into multiplied training instances. When an error is detected, the framework:

- Identifies trajectories where "Rcorr(τi) < δcorr ∨ Rfmt(τi) = 0"
- Constructs augmented context: xcorr = [x; τerr; f] (original query + failed call + diagnostic feedback)
- Resamples G′ parallel recovery attempts conditioned on this augmented context
- Treats each resampled trajectory as a new training signal

As stated: "This turns a single error case into multiple parallel recovery attempts, densifying training signals around the observed error."

## 2. Error Simulator

**Training Data:** ~2,000 instances from error logs, distilled from a larger pool, each containing:
- System prompt + tool specifications + dialogue state
- Failed tool call (τerr)
- Ground-truth call (τgt)
- Teacher-written diagnostic message (via Claude-Sonnet-4), filtered for quality

**Architecture:** Qwen3-32B model fine-tuned via SFT

**Output Constraints:** "Outputs are restricted to non-revealing error descriptions (e.g., 'parameter status expects value OPEN') rather than the full target call"

**Inference:** f ← Sφ(x, τerr, τgt)—consumes system+tools, dialogue history, ground truth, and failed attempt to produce concise feedback resembling runtime responses

The simulator is prevented from target leakage by constraining outputs to realistic error messages without exposing the correct solution.

## 3. G′ Resampling Procedure

**Exact procedure (Algorithm 1, lines 37-42):**
- Generate recovery group: {τ′j}j=1^G′ ∼ πθ(·|xcorr)
- Compute rewards for each recovery trajectory
- Calculate corrective advantages using within-group normalization:
  - μ′R ← (1/G′) Σ r′j
  - σ′R ← Std(r′j)
  - Â′j ← (r′j − μ′R) / (σ′R + ε)
- Apply GRPO-style clipped objective with KL penalty

The key insight: "Conditioning on explicit feedback f typically increases outcome diversity within the fission group, improving the usefulness of advantage estimates for recovery updates."

## 4. Conditioning Strategy

The framework conditions on **error occurrence + diagnostic feedback**, not error type categories. The two-level error filter distinguishes format validity (binary) from functional correctness (scalar threshold δcorr=1), but resampling uses the unified augmented context [x; τerr; f] without explicit error-type labeling.

## 5. Benchmarks & Results

**Benchmark:** BFCL v4 Multi-Turn (chosen specifically for "interactive error feedback mechanism: upon execution error, the environment provides explicit error traces and permits the agent up to 20 retries")

**Primary Results (Table 1):**

| Model | Method | Overall Acc |
|-------|--------|-------------|
| Qwen3-8B | GRPO | 42.75% |
| Qwen3-8B | Fission-GRPO | 46.75% |

Across all Qwen3 scales (1.7B/4B/8B), Fission-GRPO outperforms GRPO, DAPO, and Dr.GRPO. Notably, "Fission-GRPO (Qwen3-8B) significantly outperforms both ToolACE-2-8B (37.00%) and BitAgent-8B (37.75%)"

**Error Recovery Analysis (Figure 3):**
- Average error recovery improvement: +5.7% across categories
- Long Context: +11.8%
- One-shot success preserved/improved: +1.75% average

## 6. Differentiation from Tree-Based Approaches

The paper provides limited explicit comparison with tree-expansion methods. The key architectural distinction: Fission-GRPO uses a **closed-loop error simulator** integrated into RL training, whereas tree-based approaches typically rely on broader exploration. Fission focuses computational budget on diagnosed error recovery rather than exhaustive branching, maintaining "on-policy alignment with the model's evolving error distribution."

## 7. Reward Function Design

**Three-component composite reward R(τ,t):**

1. **Format Compliance (Rfmt):** Binary {0,1}, decaying weight wfmt(t) from 2→1
2. **Functional Correctness (Rcorr):** ∈[0,2]
   - Rcorr = α·I(N=N*) + (1−α)·(1/|M|)Σ F1(a,a*)
   - I(N=N*): correct function selection
   - F1: token-level overlap on matched parameters
   - Increasing weight wcorr(t) from 2→3
3. **Efficiency Regularization (Rlen):** ∈[0,1] via piecewise Gaussian with time-annealing

Weights change dynamically during training, shifting focus "from syntax to semantics as training progresses."

## 8. Ablation Studies

**Table 2 (Feedback Quality):**

Qwen3-8B results:
- GRPO baseline: 42.75%
- Fission-Static (generic error message): 44.00% (+1.25%)
- Fission-Dynamic (Error Simulator): 46.75% (+4.0%)

Gap between Static and Dynamic (marginal +2.75%) demonstrates necessity of precise diagnostic supervision.

**Section 4.5 (Trigger Frequency):**
Performance stable for small N (frequent triggers), degrades with sparse updates (large N). Miss Param and Long Context categories most sensitive to update frequency.

## 9. Code Availability

**Not explicitly mentioned in the paper.** The authors provide detailed hyperparameters (learning rate 1e-6, batch size 8, G=8, max prompt 12,800 tokens, max response 4,096 tokens) and promise to include Algorithm 1 pseudocode in appendices, but no repository or code release statement appears.

---

## Summary

Fission-GRPO's technical novelty centers on **online error diagnosis + multiplicative resampling**: intercepting model failures, augmenting them with simulated but realistic feedback, then spawning G′ parallel recovery attempts on-policy. This avoids static dataset distribution mismatch while avoiding target leakage through constrained error message generation. The 4% overall gain and 5.7% error recovery improvement on BFCL v4 Multi-Turn validate this approach for smaller models (8B scale).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d3b6bf3-e777-4216-b1b8-2c30a109dba6",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "8014cca6-edf1-4c97-9428-b25f96f25471",
  "sourceToolAssistantUUID": "7d3b6bf3-e777-4216-b1b8-2c30a109dba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-11T23:29:51.077Z_

Good, I have substantial details. Let me now search for follow-up work citing this paper, and also fetch more details from the paper notes and reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8014cca6-edf1-4c97-9428-b25f96f25471",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CaweiVTSkTsgRbFpasTLJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42641f91-5158-422c-95cf-b45fa90419b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmZcAfkSyoMa6PKgd726nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 666,
      "cache_creation_input_tokens": 3487,
      "cache_read_input_tokens": 13092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3487,
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

_source line 21 · 2026-05-11T23:29:51.792Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HCVWWJsAxpm19TQJesh6Vf`</summary>

```json
{
  "query": "citing \"Fission-GRPO\" OR \"2601.15625\" error recovery tool use 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42641f91-5158-422c-95cf-b45fa90419b2",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CaweiVTSkTsgRbFpasTLJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92442407-17ab-40fc-94eb-c6a4ab566b8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmZcAfkSyoMa6PKgd726nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 666,
      "cache_creation_input_tokens": 3487,
      "cache_read_input_tokens": 13092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3487,
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

_source line 22 · 2026-05-11T23:29:52.409Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E1wZkUEsg7SEJb9Tt7XHYL`</summary>

```json
{
  "query": "Fission-GRPO code github repository Zhiwei Zhang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92442407-17ab-40fc-94eb-c6a4ab566b8f",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CaweiVTSkTsgRbFpasTLJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aafab02d-6a1a-4239-8286-9c6bb2379d4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmZcAfkSyoMa6PKgd726nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 666,
      "cache_creation_input_tokens": 3487,
      "cache_read_input_tokens": 13092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3487,
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

_source line 23 · 2026-05-11T23:29:53.283Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HivqeCmmK22C8VSqJ8GgKG`</summary>

```json
{
  "query": "BFCL v4 multi-turn Fission-GRPO comparison tree-GRPO ARPO branching"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aafab02d-6a1a-4239-8286-9c6bb2379d4b",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CaweiVTSkTsgRbFpasTLJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecf44842-9559-4ea0-98de-ba878ed863ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmZcAfkSyoMa6PKgd726nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 666,
      "cache_creation_input_tokens": 3487,
      "cache_read_input_tokens": 13092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3487,
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

### Tool result

_source line 24 · 2026-05-11T23:29:58.717Z_

<details><summary>↩ Tool result · `toolu_01HCVWWJsAxpm19TQJesh6Vf`</summary>

```text
Web search results for query: "citing "Fission-GRPO" OR "2601.15625" error recovery tool use 2026"

Links: [{"title":"[2601.15625] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625"},{"title":"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/html/2601.15625"},{"title":"[Paper Note] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors, Zhiwei Zhang+, arXiv'26, 2026.01 · Issue #4277 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4277"},{"title":"Paper page - Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://huggingface.co/papers/2601.15625"},{"title":"[Literature Review] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://www.themoonlight.io/en/review/robust-tool-use-via-fission-grpo-learning-to-recover-from-execution-errors"},{"title":"Error Recovery Guide: fi-6110 - Fujitsu Global","url":"https://www.fujitsu.com/global/support/products/computing/peripheral/scanners/erg/agcerrback-61.html"},{"title":"Solved: [startnet] Error, Get failure from Dynamic Recovery Tool. - HP Support Community - 8937578","url":"https://h30434.www3.hp.com/t5/Notebook-Operating-System-and-Recovery/startnet-Error-Get-failure-from-Dynamic-Recovery-Tool/td-p/8937578"},{"title":"CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning","url":"https://arxiv.org/html/2601.15141"},{"title":"Can i get updated drivers for fission film scanner 6878 - Office Equipment & Supplies | Fixya","url":"https://www.fixya.com/support/t26547854-get_updated_drivers_fission_film_scanner"},{"title":"recovertool v2.00.33 l1224 for repairing Silicon Power USB stick - Flash Drive Repair","url":"http://www.flashdrive-repair.com/2014/09/recovertool-v20033l1224-Silicon-Power-repair-adata.html"}]

I found relevant results for your search query. Here's what I found about Fission-GRPO and paper 2601.15625:

## Fission-GRPO Overview

The paper titled "Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors" was submitted on January 22, 2026.

## Problem Being Addressed

Large language models can call tools effectively, yet they remain brittle in multi-turn execution: following a tool call error, smaller models often degenerate into repetitive invalid re-invocations, failing to interpret error feedback and self-correct.

## Solution Approach

Fission-GRPO is a framework that converts execution errors into corrective supervision within the RL training loop. The core mechanism fissions each failed trajectory into a new training instance by augmenting it with diagnostic feedback from a finetuned Error Simulator, then resampling recovery rollouts on-policy.

## Performance Results

On the BFCL v4 Multi-Turn, Fission-GRPO improves the error recovery rate of Qwen3-8B by 5.7% absolute, yielding a 4% overall accuracy gain (42.75% to 46.75%) over GRPO and outperforming specialized tool-use agents.

The paper is available on arXiv at https://arxiv.org/abs/2601.15625.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92442407-17ab-40fc-94eb-c6a4ab566b8f",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "fbc55516-5c6e-4635-9945-a049f4d42fdd",
  "sourceToolAssistantUUID": "92442407-17ab-40fc-94eb-c6a4ab566b8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T23:30:01.403Z_

<details><summary>↩ Tool result · `toolu_01E1wZkUEsg7SEJb9Tt7XHYL`</summary>

```text
Web search results for query: "Fission-GRPO code github repository Zhiwei Zhang"

Links: [{"title":"[Paper Note] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors, Zhiwei Zhang+, arXiv'26, 2026.01 · Issue #4277 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4277"},{"title":"[2601.15625v1] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625v1"},{"title":"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/html/2601.15625v1"},{"title":"[2601.15625] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625"},{"title":"Fission · GitHub","url":"https://github.com/fission-codes"},{"title":"GitHub - fission-codes/fission-codes: Status codes for smart contracts powering microservices for Web3","url":"https://github.com/fission-codes/fission-codes"},{"title":"Zhiwei-Z (BothSidesGotGlue) · GitHub","url":"https://github.com/Zhiwei-Z"},{"title":"GitHub - fission/fission: Fast and Simple Serverless Functions for Kubernetes · GitHub","url":"https://github.com/fission/fission"},{"title":"fission/README.md at master · fission/fission","url":"https://github.com/fission/fission/blob/master/README.md"},{"title":"SD Times GitHub Project of the Week: Fission - SD Times","url":"https://sdtimes.com/github/sd-times-github-project-week-fission/"}]

Based on the search results, I found information about the Fission-GRPO paper by Zhiwei Zhang and colleagues, but the search did not return a specific GitHub repository for the code.

## Research Paper Information

Fission-GRPO is a research paper authored by Zhiwei Zhang, Fei Zhao, Rui Wang, Zezhong Wang, Bin Liang, Jiakang Wang, Yao Hu, Shaosheng Cao, and Kam-Fai Wong. The paper is titled "Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors" and was published on arXiv on January 22, 2026 (arXiv paper 2601.15625).

## What Fission-GRPO Does

Fission-GRPO is a framework that converts execution errors into corrective supervision within the RL training loop, with its core mechanism fissioning each failed trajectory into a new training instance by augmenting it with diagnostic feedback from a finetuned Error Simulator, then resampling recovery rollouts on-policy.

## Note on GitHub Repository

The search results did not return a dedicated GitHub repository for the Fission-GRPO code. The paper is available on arXiv, but you may want to check the paper directly or contact the authors for code availability and repository information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aafab02d-6a1a-4239-8286-9c6bb2379d4b",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "86c63b46-fb68-47e1-9e6f-9bd911606ac2",
  "sourceToolAssistantUUID": "aafab02d-6a1a-4239-8286-9c6bb2379d4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T23:30:01.665Z_

<details><summary>↩ Tool result · `toolu_01HivqeCmmK22C8VSqJ8GgKG`</summary>

```text
Web search results for query: "BFCL v4 multi-turn Fission-GRPO comparison tree-GRPO ARPO branching"

Links: [{"title":"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/html/2601.15625v1"},{"title":"[Paper Note] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors, Zhiwei Zhang+, arXiv'26, 2026.01 · Issue #4277 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4277"},{"title":"RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents","url":"https://arxiv.org/html/2602.03025"},{"title":"Berkeley Function Calling Leaderboard (BFCL) V4","url":"https://gorilla.cs.berkeley.edu/leaderboard.html"},{"title":"BFCL V4 • Agentic Part 1: Web Search","url":"https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html"},{"title":"BFCL V4 • Memory","url":"https://gorilla.cs.berkeley.edu/blogs/16_bfcl_v4_memory.html"},{"title":"GitHub - speakleash/gorilla-bfcl-benchmark: FORK FOR = Gorilla: Training and Evaluating LLMs for Function Calls (Tool Calls) · GitHub","url":"https://github.com/speakleash/gorilla-bfcl-benchmark"},{"title":"gorilla/berkeley-function-call-leaderboard/bfcl_eval/data/BFCL_v4_multi_turn_base.json at main · ShishirPatil/gorilla","url":"https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/bfcl_eval/data/BFCL_v4_multi_turn_base.json"},{"title":"SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees","url":"https://arxiv.org/html/2602.06554"},{"title":"BFCL-v4 - EvalScope - Read the Docs","url":"https://evalscope.readthedocs.io/en/v1.2.0/third_party/bfcl_v4.html"}]

Based on the search results, I found information about BFCL v4 Multi-Turn and Fission-GRPO, but the search did not return specific information about tree-GRPO, ARPO, or branching methods. Let me provide what was found:

## BFCL v4 Multi-Turn and Fission-GRPO

Fission-GRPO is evaluated on the BFCL v4 Multi-Turn benchmark. On the BFCL v4 Multi-Turn, Fission-GRPO improves the error recovery rate of Qwen3-8B by 5.7% absolute, yielding a 4% overall accuracy gain.

Fission-GRPO is a framework that converts execution errors into corrective supervision within the RL training loop, with its core mechanism fissioning each failed trajectory into a new training instance by augmenting it with diagnostic feedback from a finetuned Error Simulator, then resampling recovery rollouts on-policy.

Fission-GRPO achieves state-of-the-art performance across the Qwen3 model family (1.7B, 4B, and 8B), consistently outperforming GRPO, DAPO, and Dr.GRPO baselines.

## Other GRPO Variants on BFCL v4

The search also returned information about RC-GRPO, another method evaluated on BFCL v4 Multi-Turn. However, I did not find specific information about tree-GRPO, ARPO, or branching comparison methods in the search results. If you're looking for information about those specific methods, you may want to search for them directly or provide more context about the papers you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecf44842-9559-4ea0-98de-ba878ed863ac",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "5b1d0c76-8bb3-43f8-8eed-8303d9e7ca1b",
  "sourceToolAssistantUUID": "ecf44842-9559-4ea0-98de-ba878ed863ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-11T23:30:05.061Z_

Let me fetch the literature review and the related RC-GRPO paper for more context on comparisons, and also look for citations via Semantic Scholar.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b1d0c76-8bb3-43f8-8eed-8303d9e7ca1b",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawejYaVn7h933HGHmvcS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d40b3bb-08cd-4cd6-9106-a676c739f95f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHGQcRoSD5WFfDTUjnsaA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 16579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3887,
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

_source line 28 · 2026-05-11T23:30:06.872Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JGgzBVwjpWdnFKPTH3QKfv`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/robust-tool-use-via-fission-grpo-learning-to-recover-from-execution-errors",
  "prompt": "Extract all technical details, criticisms, strengths/weaknesses analysis, and any comparison to other methods mentioned in this literature review of Fission-GRPO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d40b3bb-08cd-4cd6-9106-a676c739f95f",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawejYaVn7h933HGHmvcS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c54e0c5-f6bf-4810-811a-922c797fcdf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHGQcRoSD5WFfDTUjnsaA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 16579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3887,
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

_source line 29 · 2026-05-11T23:30:07.673Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fx9XEifSgTRD1rPPuxNPpj`</summary>

```json
{
  "query": "Semantic Scholar citations \"Robust Tool Use via Fission-GRPO\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c54e0c5-f6bf-4810-811a-922c797fcdf7",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawejYaVn7h933HGHmvcS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "421048af-4273-4d81-90ce-92976f1d53c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHGQcRoSD5WFfDTUjnsaA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 16579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3887,
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

_source line 30 · 2026-05-11T23:30:08.242Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S2mnp6A2Uopw9qfpE9ZKVp`</summary>

```json
{
  "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/4277",
  "prompt": "Extract all notes, summaries, and technical details about the Fission-GRPO paper from this paper notes page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "421048af-4273-4d81-90ce-92976f1d53c2",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawejYaVn7h933HGHmvcS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82ce53fb-a83a-4394-b64e-87302c2d7060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHGQcRoSD5WFfDTUjnsaA9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 16579,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 329,
          "cache_read_input_tokens": 16579,
          "cache_creation_input_tokens": 3887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3887,
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

_source line 31 · 2026-05-11T23:30:14.090Z_

<details><summary>↩ Tool result · `toolu_01S2mnp6A2Uopw9qfpE9ZKVp`</summary>

```text
# Fission-GRPO Paper Summary

## Core Problem
LLMs struggle with multi-turn tool execution. When errors occur, smaller models often repeat invalid attempts rather than interpreting feedback and self-correcting, limiting reliable real-world deployment.

## Key Innovation
Fission-GRPO converts execution errors into corrective training supervision within reinforcement learning. The framework "fissions each failed trajectory into a new training instance by augmenting it with diagnostic feedback from a finetuned Error Simulator, then resampling recovery rollouts on-policy."

## Technical Approach
- Uses an Error Simulator to provide diagnostic feedback on failures
- Learns from the model's actual errors during exploration rather than static pre-collected error datasets
- Addresses distribution mismatch between synthetic training data and real on-policy errors

## Results (BFCL v4 Multi-Turn)
- Qwen3-8B error recovery rate improved by 5.7 percentage points
- Overall accuracy increased 4% (42.75% → 46.75%) compared to GRPO baseline
- Outperformed specialized tool-use agents

## Authors
Zhiwei Zhang, Fei Zhao, Rui Wang, Zezhong Wang, Bin Liang, Jiakang Wang, Yao Hu, Shaosheng Cao, Kam-Fai Wong

**ArXiv**: 2601.15625
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82ce53fb-a83a-4394-b64e-87302c2d7060",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "64c5e3e8-5d91-493d-a314-3e87e0689ddc",
  "sourceToolAssistantUUID": "82ce53fb-a83a-4394-b64e-87302c2d7060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-11T23:30:14.643Z_

<details><summary>↩ Tool result · `toolu_01JGgzBVwjpWdnFKPTH3QKfv`</summary>

```text
# Fission-GRPO Technical Analysis

## Technical Details

**Core Framework:** The method employs three-stage closed-loop training. Stage 1 uses Group-Relative Policy Optimization (GRPO) with a composite reward function combining format compliance, functional correctness, and efficiency regularization. Stage 2 identifies errors and synthesizes corrective feedback via a fine-tuned Error Simulator. Stage 3 applies "fission updates"—"transforming a single error instance into multiple parallel recovery attempts" by resampling trajectories conditioned on error feedback.

**Key Innovation:** The Error Simulator ($S_\phi$) is a specialized Qwen3-32B model trained on ~2K instances to generate "concise, actionable runtime error strings" that provide diagnostic guidance without revealing solutions.

## Strengths

- **Substantial empirical gains:** Achieved "5.7% absolute improvement in error recovery rate" on Qwen3-8B, with overall accuracy increasing from 42.75% to 46.75%
- **On-policy alignment:** LIFO buffering ensures recent errors remain relevant to the model's current policy
- **Adaptive reward weighting:** Time-annealing weights transition from syntax to semantic focus during training
- **Qualitative improvements:** Models develop "active diagnostic strategies" rather than repetitive failures

## Weaknesses & Limitations

- **Simulator dependency:** Requires "2K instances" of teacher-written error messages; scalability unclear
- **Threshold sensitivity:** Error identification relies on tunable threshold $\delta_{corr}$; sensitivity analysis limited
- **Limited benchmark scope:** Evaluation restricted to BFCL v4 Multi-Turn; generalization untested
- **Computational overhead:** Multiplicative resampling via fission may increase training cost

## Comparisons to Baselines

Outperformed GRPO, DAPO, Dr.GRPO, ToolACE-2-8B, and BitAgent-8B across Qwen3 scales (1.7B-8B).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c54e0c5-f6bf-4810-811a-922c797fcdf7",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "e25e7897-e3ed-47fa-be53-104f8e8eb34b",
  "sourceToolAssistantUUID": "9c54e0c5-f6bf-4810-811a-922c797fcdf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-11T23:30:18.621Z_

<details><summary>↩ Tool result · `toolu_01Fx9XEifSgTRD1rPPuxNPpj`</summary>

```text
Web search results for query: "Semantic Scholar citations "Robust Tool Use via Fission-GRPO" 2026"

Links: [{"title":"[2601.15625] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625"},{"title":"[Paper Note] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors, Zhiwei Zhang+, arXiv'26, 2026.01 · Issue #4277 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4277"},{"title":"Paper page - Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://huggingface.co/papers/2601.15625"},{"title":"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/html/2601.15625"},{"title":"[Literature Review] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://www.themoonlight.io/en/review/robust-tool-use-via-fission-grpo-learning-to-recover-from-execution-errors"}]

I found search results for the "Robust Tool Use via Fission-GRPO" paper from 2026. Here's what I found:

## Paper Overview

The paper "Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors" was posted on arXiv on January 22, 2026 (arXiv paper 2601.15625). The paper was authored by Zhiwei Zhang and 8 other authors.

## Key Results

On the BFCL v4 Multi-Turn benchmark, Fission-GRPO improves the error recovery rate of Qwen3-8B by 5.7% absolute, yielding a 4% overall accuracy gain (42.75% to 46.75%) over GRPO and outperforming specialized tool-use agents.

## Main Contribution

The paper proposes Fission-GRPO, a framework that converts execution errors into corrective supervision within the RL training loop. The core mechanism fissions each failed trajectory into a new training instance by augmenting it with diagnostic feedback from a finetuned Error Simulator, then resampling recovery rollouts on-policy.

However, I should note that while I found information about the paper itself from sources like arXiv and Hugging Face, the search results did not contain specific Semantic Scholar citation count information. For detailed citation metrics on Semantic Scholar, you would need to visit the paper's Semantic Scholar page directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "421048af-4273-4d81-90ce-92976f1d53c2",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "e1e3363a-0330-4490-8ce5-b2195a92d84c",
  "sourceToolAssistantUUID": "421048af-4273-4d81-90ce-92976f1d53c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-11T23:30:23.158Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M98FWiCGW9g67uu9yrvhPz`</summary>

```json
{
  "url": "https://api.semanticscholar.org/graph/v1/paper/ArXiv:2601.15625?fields=title,citationCount,citations.title,citations.externalIds,citations.year",
  "prompt": "Extract the citation count and list all papers that cite this paper, including their titles and arXiv IDs if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1e3363a-0330-4490-8ce5-b2195a92d84c",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011Caweko3B42hMXtBhBxqVM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fff32576-acc1-473f-8981-5d72c6f42fc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpBctF5QPffmWsiQTbLpXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 352,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 20466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1544,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-11T23:30:23.482Z_

<details><summary>↩ Tool result · reported error · `toolu_01M98FWiCGW9g67uu9yrvhPz`</summary>

```text
Request failed with status code 429
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fff32576-acc1-473f-8981-5d72c6f42fc4",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "0d9957ab-76f0-4102-98fb-d46904eeda62",
  "toolUseResult": "Error: Request failed with status code 429",
  "sourceToolAssistantUUID": "fff32576-acc1-473f-8981-5d72c6f42fc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-11T23:30:28.253Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JdyNm1hbExp6BgZirbQZ4B`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.15625v1",
  "prompt": "Focus specifically on: 1) Section 2 (Related Work) - how do the authors compare their approach to tree-based methods, MCTS approaches, branching approaches like ARPO or Tree-GRPO? 2) The Error Simulator training procedure in detail - what exact data format, how many epochs, what loss function? 3) The LIFO buffer mechanism mentioned. 4) Algorithm 1 pseudocode details - how exactly is fission triggered, what is the trigger frequency N? 5) Any mention of code release or open-source plans. 6) The exact formula for the fission objective. 7) Any additional benchmarks beyond BFCL v4."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d9957ab-76f0-4102-98fb-d46904eeda62",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011Caweko3B42hMXtBhBxqVM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3f1dd39-ea06-4074-a929-f631964ad459",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpBctF5QPffmWsiQTbLpXH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 352,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 20466,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1544
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 352,
          "output_tokens": 359,
          "cache_read_input_tokens": 20466,
          "cache_creation_input_tokens": 1544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1544,
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

_source line 37 · 2026-05-11T23:30:40.535Z_

<details><summary>↩ Tool result · `toolu_01JdyNm1hbExp6BgZirbQZ4B`</summary>

````text
# Analysis of Fission-GRPO Paper: Key Technical Details

## 1. Related Work & Comparison to Tree-Based Methods

The Related Work section (§2) does **not mention tree-based methods, MCTS, ARPO, or Tree-GRPO**. The authors focus instead on:

- **RL for Tool Use**: Discussing GRPO, DAPO, and NGRPO as baseline approaches
- **Error-Driven Synthesis**: Comparing against static synthetic datasets (ToolACE, LoopTool) rather than dynamic exploration methods

The paper frames its contribution as addressing "distribution mismatch" in offline error corpora, but does not engage with branching or tree-search paradigms.

## 2. Error Simulator Training Details

The paper provides **limited specificity** on Error Simulator training:

- **Data construction**: "approximately 2K instances from error logs"
- **Format**: Each instance comprises "(i) system prompt + tool spec + dialogue state, (ii) model's failed tool call, (iii) ground-truth tool call, (iv) teacher-written diagnostic error message"
- **Implementation**: "Qwen3-32B model fine-tuned via SFT"
- **Quality filtering**: Applied but details not specified

**Missing details**: Number of epochs, learning rate, loss function, exact SFT objective, and validation metrics are not disclosed.

## 3. LIFO Buffer Mechanism

The LIFO buffer (§3.3.2) operates as follows:

> "All corrective samples are stored in a LIFO buffer ℬcorr, so that the most recent errors are consumed first during corrective updates."

This design "keeps the corrective batch distribution closer to the current policy πθ, improving the on-policy approximation." Deduplication occurs via hashing (x, τerr) pairs.

## 4. Algorithm 1 & Fission Trigger Frequency

**Trigger mechanism** (Line 33, Algorithm 1):
```
if |ℬ| ≥ Btrig then
```

The framework activates corrective updates when the LIFO buffer accumulates sufficient samples. The paper does **not explicitly define Btrig** in Algorithm 1, though §4.5 investigates sensitivity to trigger interval N (measured in "global steps"), finding performance stable across "small-to-moderate" intervals.

**No exact threshold values are provided in the pseudocode or main text.**

## 5. Code Release & Open-Source Plans

The paper **contains no mention of code release, GitHub repositories, or open-source plans**. No availability statement appears in the conclusion or limitations.

## 6. Fission Objective Formula

The corrective update objective (Eq. 6) is:

> "𝒥corr(θ) = 𝔼xcorr[(1/G′)∑ʲ⁼¹^G′ Â(τ′ⱼ)∇log πθ(τ′ⱼ|xcorr)]"

This applies standard GRPO-style optimization "over the corrective distribution" with multiplicative resampling of G′ recovery trajectories per error context. The paper does **not provide an alternative "fission-specific" objective distinct from GRPO**; the innovation lies in the contextual conditioning and multiplicative resampling rather than a novel loss function.

## 7. Benchmarks Beyond BFCL v4

Evaluation is **exclusively on BFCL v4 Multi-Turn**. The limitations section explicitly states:

> "We evaluate Fission-GRPO exclusively on the BFCL v4 Multi-Turn benchmark...Most existing tool-use benchmarks emphasize single-turn correctness without explicit retry mechanisms."

No additional benchmarks (StableToolBench, ToolLLM, etc.) are evaluated, though they are cited in related work.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3f1dd39-ea06-4074-a929-f631964ad459",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "0d4d2f0c-cfbe-440e-95d1-c6823f5f45a4",
  "sourceToolAssistantUUID": "f3f1dd39-ea06-4074-a929-f631964ad459",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-11T23:30:43.598Z_

Now let me check Semantic Scholar for citations and also look at the RC-GRPO paper which appears to be related follow-up work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d4d2f0c-cfbe-440e-95d1-c6823f5f45a4",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawenQjYjBKTw9psBnKhB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55f5f85d-7cd6-48aa-91ff-212cd132f481",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHQfSVz9iyj2UvzfehDT6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 22010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1786,
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

_source line 39 · 2026-05-11T23:30:44.590Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rk7qNv1WJjaCatUhoSDvqx`</summary>

```json
{
  "query": "papers citing Fission-GRPO 2601.15625 Semantic Scholar 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55f5f85d-7cd6-48aa-91ff-212cd132f481",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawenQjYjBKTw9psBnKhB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac51d985-70f4-418b-b71c-5065741b8b5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHQfSVz9iyj2UvzfehDT6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 22010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1786,
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

_source line 40 · 2026-05-11T23:30:46.422Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MAwfz9nJ6tjsD3jVxUDifa`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03025",
  "prompt": "Extract the title, authors, abstract, and whether this paper cites or compares against Fission-GRPO (arXiv 2601.15625). Also extract any details about how RC-GRPO relates to Fission-GRPO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac51d985-70f4-418b-b71c-5065741b8b5b",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011CawenQjYjBKTw9psBnKhB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0fa0ff5-ac6f-453e-89cf-9c0c66fbf8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHQfSVz9iyj2UvzfehDT6M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 22010,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1786
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 225,
          "cache_read_input_tokens": 22010,
          "cache_creation_input_tokens": 1786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1786,
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

_source line 41 · 2026-05-11T23:30:50.270Z_

<details><summary>↩ Tool result · `toolu_01Rk7qNv1WJjaCatUhoSDvqx`</summary>

```text
Web search results for query: "papers citing Fission-GRPO 2601.15625 Semantic Scholar 2026"

Links: [{"title":"[2601.15625] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625"},{"title":"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/html/2601.15625"},{"title":"[2601.03661] AMIR-GRPO: Inducing Implicit Preference Signals into GRPO","url":"https://arxiv.org/abs/2601.03661"},{"title":"Papers | Semantic Scholar","url":"https://www.semanticscholar.org/paper"},{"title":"Semantic Scholar | Product","url":"https://www.semanticscholar.org/product"},{"title":"Semantic Scholar | AI-Powered Research Tool","url":"https://www.semanticscholar.org/"},{"title":"Modeling, Calibration, and Verification of a Fission ...","url":"https://pdfs.semanticscholar.org/2fbb/0807adef6642870c0b43d682c0900749095d.pdf"},{"title":"Semantic Scholar - Academic Graph API","url":"https://api.semanticscholar.org/api-docs/"},{"title":"Semantic Scholar | Frequently Asked Questions","url":"https://www.semanticscholar.org/faq"},{"title":"[2601.22582] MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning","url":"https://arxiv.org/abs/2601.22582"}]

Based on my search results, I found information about the Fission-GRPO paper (arXiv:2601.15625). Fission-GRPO is a framework that converts execution errors into corrective supervision within the RL training loop, with a core mechanism that fissions each failed trajectory into a new training instance by augmenting it with diagnostic feedback from a finetuned Error Simulator, then resampling recovery rollouts on-policy.

However, the search results I obtained do not contain a specific list of papers that cite arXiv:2601.15625 on Semantic Scholar. To find papers that cite this work, you would need to:

1. Visit the arXiv page directly at https://arxiv.org/abs/2601.15625
2. Go to Semantic Scholar's page for this paper
3. Look for the "Cited by" section on either platform

Both platforms typically display citation information and allow you to see which papers have referenced this work. Since the paper was only submitted on January 22, 2026, there may be limited citations available at this early stage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac51d985-70f4-418b-b71c-5065741b8b5b",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "89a99bce-45b6-4c55-a645-ef003057baa0",
  "sourceToolAssistantUUID": "ac51d985-70f4-418b-b71c-5065741b8b5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-11T23:30:50.357Z_

<details><summary>↩ Tool result · `toolu_01MAwfz9nJ6tjsD3jVxUDifa`</summary>

```text
# RC-GRPO Paper Analysis

**Title:** "RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents"

**Authors:** Haitian Zhong, Jixiu Zhai, Lei Song, Jiang Bian, Qiang Liu, Tieniu Tan

**Abstract Summary:**
The paper addresses challenges in multi-turn tool calling for LLMs by proposing RC-GRPO. The method tackles the problem where "within-group reward variation is low" causing "vanishing updates" in standard GRPO approaches. It introduces a Reward-Conditioned Trajectory Policy (RCTP) that learns to generate trajectories of different quality levels based on special reward tokens, improving within-group diversity during reinforcement learning.

**Fission-GRPO Comparison:**
The provided content does not mention Fission-GRPO (arXiv 2601.15625) or provide any citations, comparisons, or relationships to that specific paper. There is no reference to this work in the abstract, author list, or visible metadata shown.

To determine whether RC-GRPO cites or compares against Fission-GRPO, you would need to access the full paper PDF or HTML version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0fa0ff5-ac6f-453e-89cf-9c0c66fbf8ac",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "f4305fd5-efcb-41aa-8862-c5cdcbba8fd4",
  "sourceToolAssistantUUID": "d0fa0ff5-ac6f-453e-89cf-9c0c66fbf8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-11T23:30:53.575Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HfGFqpWqzSX8JnkRkLpWcV`</summary>

```json
{
  "query": "\"CLEANER self-purified trajectories\" cite Fission-GRPO tool use error recovery 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4305fd5-efcb-41aa-8862-c5cdcbba8fd4",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011Caweo8iuRSYnZqyfYU9LC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36da0984-bae4-4134-8f1c-0b5dd4449ee8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HGciqCuFwYBHgk3CsPf2rY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1262,
      "cache_read_input_tokens": 23796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1262,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-11T23:30:54.474Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QN62x16Jiac2RuBSVg3p44`</summary>

```json
{
  "query": "SeeUPO sequence-level agentic RL Fission-GRPO comparison BFCL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36da0984-bae4-4134-8f1c-0b5dd4449ee8",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011Caweo8iuRSYnZqyfYU9LC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c51018c-f3ba-4a09-9718-6476c7009b7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HGciqCuFwYBHgk3CsPf2rY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1262,
      "cache_read_input_tokens": 23796,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1262
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 23796,
          "cache_creation_input_tokens": 1262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1262,
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

_source line 45 · 2026-05-11T23:31:01.470Z_

<details><summary>↩ Tool result · `toolu_01HfGFqpWqzSX8JnkRkLpWcV`</summary>

```text
Web search results for query: ""CLEANER self-purified trajectories" cite Fission-GRPO tool use error recovery 2026"

Links: [{"title":"CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning","url":"https://arxiv.org/html/2601.15141"},{"title":"Paper page - Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://huggingface.co/papers/2601.15625"},{"title":"Work in progress CLEANER: SELF-PURIFIED TRAJECTORIES BOOST","url":"https://arxiv.org/pdf/2601.15141"},{"title":"[2601.15141] CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning","url":"https://arxiv.org/abs/2601.15141"},{"title":"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/html/2601.15625"},{"title":"(PDF) CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning","url":"https://www.researchgate.net/publication/399962479_CLEANER_Self-Purified_Trajectories_Boost_Agentic_Reinforcement_Learning"},{"title":"[2601.15625v1] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625v1"},{"title":"[2601.15625] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/abs/2601.15625"},{"title":"[Paper Note] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors, Zhiwei Zhang+, arXiv'26, 2026.01 · Issue #4277 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4277"},{"title":"[Literature Review] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://www.themoonlight.io/en/review/robust-tool-use-via-fission-grpo-learning-to-recover-from-execution-errors"}]

Based on the web search results, here's information about CLEANER self-purified trajectories and Fission-GRPO tool use error recovery:

## CLEANER: Self-Purified Trajectories

CLEANER addresses challenges in agentic reinforcement learning by exploiting the model's intrinsic self-correction capabilities to eliminate error-contaminated context directly during data collection. At its core, the Similarity-Aware Adaptive Rollback (SAAR) mechanism autonomously constructs clean, purified trajectories by retrospectively replacing failures with successful self-corrections.

Based on semantic similarity, SAAR adaptively regulates replacement granularity from shallow execution repairs to deep reasoning substitutions. Empirical results on AIME24/25, GPQA, and LiveCodeBench show average accuracy gains of 6%, 3%, and 5% over baselines, and CLEANER matches state-of-the-art performance using only one-third of the training steps.

## Fission-GRPO: Tool Use Error Recovery

Fission-GRPO is a framework that converts execution errors into corrective supervision within the RL training loop. By intercepting errors, augmenting them with simulated feedback, and resampling recovery attempts, the approach enables smaller models to learn robust self-correction rather than collapsing into repetitive loops.

On the BFCL v4 Multi-Turn, Fission-GRPO improves the error recovery rate of Qwen3-8B by 5.7% absolute, yielding a 4% overall accuracy gain (42.75% to 46.75%) over GRPO and outperforming specialized tool-use agents.

Both papers represent recent advances in 2026 for improving robustness and efficiency in agentic reinforcement learning by handling execution errors and noisy trajectories during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36da0984-bae4-4134-8f1c-0b5dd4449ee8",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "326565fc-6c03-47cd-b336-85108d39fa1f",
  "sourceToolAssistantUUID": "36da0984-bae4-4134-8f1c-0b5dd4449ee8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-11T23:31:03.160Z_

<details><summary>↩ Tool result · `toolu_01QN62x16Jiac2RuBSVg3p44`</summary>

```text
Web search results for query: "SeeUPO sequence-level agentic RL Fission-GRPO comparison BFCL"

Links: [{"title":"SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees","url":"https://arxiv.org/html/2602.06554"},{"title":"Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors","url":"https://arxiv.org/html/2601.15625"},{"title":"[Paper Note] Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors, Zhiwei Zhang+, arXiv'26, 2026.01 · Issue #4277 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4277"},{"title":"AgentRL: Scaling Agentic Reinforcement Learning with a ...","url":"https://arxiv.org/pdf/2510.04206"},{"title":"GitHub - modelscope/AgentEvolver: AgentEvolver: Towards Efficient Self-Evolving Agent System · GitHub","url":"https://github.com/modelscope/AgentEvolver"},{"title":"Agentic Reasoning and Tool Integration for LLMs via Reinforcement Learning","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/AgenticReasoning.pdf"},{"title":"2025-07-29 Group Sequence Policy Optimization Chujie Zheng∗ Shixuan Liu","url":"https://arxiv.org/pdf/2507.18071"},{"title":"How Kimi, Cursor, and Chroma Train Agentic Models with RL","url":"https://www.philschmid.de/kimi-composer-context"},{"title":"Agentic Reinforced Policy Optimization","url":"https://arxiv.org/html/2507.19849v1"},{"title":"MUA-RL: Multi-turn User-interacting Agent Reinforcement ...","url":"https://arxiv.org/pdf/2508.18669"}]

Based on the web search results, here's what I found about these topics:

## SeeUPO: Sequence-Level Agentic RL

SeeUPO is a sequence-level algorithm that extends GRPO with sequence-level mechanisms. SeeUPO was evaluated on two multi-turn agentic benchmarks (AppWorld and BFCL v4), achieving 60.80% avg@4 and 72.85% pass@4 on Qwen3-14B, with relative improvements ranging from 43.3% to 54.6% compared to baseline methods.

Key advantages of SeeUPO include: SeeUPO maintains stable training curves without catastrophic failures, whereas both GRPO and GSPO exhibit significant performance collapse in certain settings, reflecting a fundamental limitation of existing critic-free methods in multi-turn scenarios due to advantage estimation bias. SeeUPO addresses these issues through its theoretically-grounded sequential update mechanism, which provides monotonic improvement guarantees and enables implicit turn-level credit assignment through advantage function decomposition.

## Fission-GRPO

Fission-GRPO is a framework that transforms execution errors into on-policy corrective supervision for multi-turn tool use by intercepting errors, augmenting them with simulated feedback, and resampling recovery attempts. On BFCL v4 Multi-Turn, Qwen3-8B achieves a 5.7% gain in error recovery and 4% overall accuracy improvement, outperforming specialized tool agents.

## Comparison on BFCL

Both methods were evaluated on the BFCL benchmark—SeeUPO used the BFCL v4 benchmark, while Fission-GRPO was evaluated exclusively on the BFCL v4 Multi-Turn benchmark because it features an interactive error feedback mechanism permitting retry attempts. The two methods target different aspects of agentic RL: SeeUPO focuses on training stability and convergence guarantees in multi-turn scenarios, while Fission-GRPO focuses on error recovery and self-correction capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c51018c-f3ba-4a09-9718-6476c7009b7c",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a878e485d3c9127b8",
  "type": "user",
  "uuid": "027b3721-cffa-49c5-a57c-9f73b5beb873",
  "sourceToolAssistantUUID": "2c51018c-f3ba-4a09-9718-6476c7009b7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-11T23:32:36.701Z_

Now I have comprehensive information. Here is the detailed research report.

---

## Detailed Research Report: Fission-GRPO (arXiv:2601.15625)

### Paper Verification

The paper **does exist** at arXiv:2601.15625. It is confirmed as:

- **Title:** "Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors"
- **Authors:** Zhiwei Zhang, Fei Zhao, Rui Wang, Zezhong Wang, Bin Liang, Jiakang Wang, Yao Hu, Shaosheng Cao, Kam-Fai Wong
- **Affiliations:** The Chinese University of Hong Kong (1) and Xiaohongshu Inc. (2)
- **Submitted:** January 22, 2026 (v1); revised April 20, 2026 (v2)
- **Conference:** **Accepted to ACL 2026 Main Conference** (confirmed on the arXiv abstract page)

---

### 1. What Exactly Is the "Fission" Mechanism?

The "fission" metaphor refers to splitting a single failed trajectory into multiple new training instances. The process operates in three stages within the GRPO training loop:

**Stage 1 -- Standard GRPO Exploration:** For each query x, the model samples G rollouts (G=8 in their setup). Each rollout is scored by a composite reward function. Trajectories failing the error filter (R_corr < delta_corr OR R_fmt = 0) are flagged.

**Stage 2 -- Error Augmentation:** Each failed trajectory tau_err is intercepted and augmented with diagnostic feedback f from the Error Simulator S_phi. The augmented context is constructed as: `x_corr = [x; tau_err; f]` (original query + failed tool call + simulated diagnostic feedback).

**Stage 3 -- Fission Update:** Each augmented error context is "fissioned" -- expanded into G' parallel recovery attempts by resampling new rollouts on-policy from the current model conditioned on x_corr. So a single error becomes G' new training trajectories, each attempting recovery from that specific error state with the benefit of the diagnostic feedback.

All corrective samples are stored in a **LIFO (Last-In-First-Out) buffer** (B_corr), ensuring that the most recent errors (closest to the current policy) are consumed first during corrective updates. Deduplication is applied via hashing (x, tau_err) pairs to avoid redundant training on identical error patterns.

The fission update is triggered when the buffer accumulates sufficient samples (|B| >= B_trig). The paper investigates trigger frequency sensitivity in Section 4.5 and finds performance is stable for small-to-moderate intervals but degrades with overly sparse triggering.

---

### 2. The Error Simulator

The Error Simulator (S_phi) is a critical component that generates realistic, context-aware error feedback resembling actual runtime error traces.

**Training data:** Approximately 2,000 instances distilled from error logs. Each instance contains:
1. System prompt + tool specifications + dialogue state
2. The model's failed tool call (tau_err)
3. The ground-truth correct call (tau_gt)
4. A teacher-written diagnostic message generated by Claude Sonnet 4, filtered for quality

**Architecture:** Qwen3-32B fine-tuned via supervised fine-tuning (SFT).

**Critical constraint -- No target leakage:** The simulator's outputs are explicitly restricted to "non-revealing error descriptions" (e.g., "parameter status expects value OPEN") rather than exposing the full correct tool call. This is essential -- if the simulator revealed the answer, the model would learn to pattern-match rather than reason about recovery.

**Inference:** `f <- S_phi(x, tau_err, tau_gt)` -- it consumes the system prompt, tools, dialogue history, ground truth, and the failed attempt to produce concise diagnostic feedback.

**Missing details:** The paper does not disclose the number of training epochs, learning rate, specific loss function, or validation metrics for the simulator training.

---

### 3. How G' Parallel Recovery Attempts Are Resampled

The resampling procedure (from Algorithm 1, lines 37-42) works as follows:

1. Construct the augmented corrective context: `x_corr = [x; tau_err; f]`
2. Sample G' new rollouts from the current policy: `{tau'_j}_{j=1}^{G'} ~ pi_theta(.|x_corr)`
3. Compute rewards for each recovery trajectory
4. Calculate corrective advantages using **within-group normalization**:
   - mu'_R = (1/G') * sum(r'_j)
   - sigma'_R = Std(r'_j)
   - A'_j = (r'_j - mu'_R) / (sigma'_R + epsilon)
5. Apply the corrective objective (Eq. 6): `J_corr(theta) = E_xcorr[(1/G') * sum_j A'(tau'_j) * grad log pi_theta(tau'_j|x_corr)]`

This is a standard GRPO-style clipped objective with KL penalty, applied over the corrective distribution. The innovation is not a novel loss function but rather the **contextual conditioning** (on error + feedback) and **multiplicative resampling** (one error becomes G' training signals).

The authors note that conditioning on explicit feedback f "typically increases outcome diversity within the fission group, improving the usefulness of advantage estimates for recovery updates."

---

### 4. Benchmarks and Main Results

**Benchmark:** Evaluation is **exclusively on BFCL v4 Multi-Turn**. The authors chose this because it features an "interactive error feedback mechanism: upon execution error, the environment provides explicit error traces and permits the agent up to 20 retries." The limitations section explicitly acknowledges this narrow evaluation scope.

**Primary Results (Table 1):**

| Model | Method | Overall Accuracy |
|---|---|---|
| Qwen3-8B | GRPO | 42.75% |
| Qwen3-8B | DAPO | ~41-42% |
| Qwen3-8B | Dr.GRPO | ~42-43% |
| Qwen3-8B | **Fission-GRPO** | **46.75%** |
| ToolACE-2-8B | Specialized | 37.00% |
| BitAgent-8B | Specialized | 37.75% |

Results are consistent across the Qwen3 family (1.7B, 4B, 8B), with Fission-GRPO outperforming all baselines at every scale.

**Error Recovery Analysis (Figure 3):**
- Average error recovery rate improvement: **+5.7%** across categories
- Long Context category: **+11.8%** improvement (most dramatic)
- One-shot success (getting it right on the first try) is also preserved/improved: **+1.75%** average

The abstract mentions "gains up to 17.4% on additional benchmarks" but the paper body evaluates only BFCL v4 Multi-Turn; this 17.4% figure likely refers to a specific error-category sub-split rather than a separate benchmark.

---

### 5. Error Type Conditioning

Fission-GRPO conditions on **error occurrence + diagnostic feedback content**, **not** on explicit error type categories. The error filter uses a two-level check:
- **Format validity** (R_fmt): Binary {0,1} -- is the output a well-formed tool call?
- **Functional correctness** (R_corr): Scalar threshold (delta_corr = 1) -- did the call do the right thing?

However, the resampling uses a **unified augmented context** `[x; tau_err; f]` without any explicit error-type labeling or categorization. The diagnostic feedback f implicitly encodes information about what went wrong, but there is no taxonomy of error types that conditions different recovery strategies.

---

### 6. How Branching Differs from Tree-Based Approaches (ARPO, Tree-GRPO)

This is a notable gap in the paper. The Related Work section (Section 2) **does not discuss tree-based methods, MCTS approaches, ARPO, or Tree-GRPO at all**. The authors position their work against:
- Standard RL baselines (GRPO, DAPO, Dr.GRPO)
- Static error-correction datasets (ToolACE, LoopTool)

Based on the technical details, the key architectural distinctions from tree-based approaches are:

1. **Targeted vs. exhaustive branching:** Tree-based methods (like MCTS or Tree-GRPO) branch at decision points to explore the full action space. Fission-GRPO branches **only at error points**, focusing computational budget specifically on diagnosed failure states.

2. **Simulator-augmented context:** Tree-based methods typically branch with the same context. Fission-GRPO augments the context with diagnostic feedback before branching, providing the model additional information about what went wrong.

3. **On-policy error alignment:** The LIFO buffer ensures the model trains on errors from its current policy distribution, not from a static exploration tree. As the policy improves, the error distribution shifts, and the fission targets shift with it.

4. **No backtracking:** Unlike tree search which explores alternative paths from earlier states, Fission-GRPO always conditions on the full failed trajectory plus feedback -- it's forward-looking recovery, not backward-looking exploration.

5. **Flat structure:** There is no tree data structure or recursive branching. Each error produces exactly one "fission group" of G' parallel attempts at the same level.

---

### 7. Reward Function Design

The composite reward R(tau, t) has three components with time-annealing weights:

1. **Format Compliance (R_fmt):** Binary {0,1}. Weight w_fmt(t) decays from 2 to 1 over training.
2. **Functional Correctness (R_corr):** Range [0,2]. Computed as `R_corr = alpha * I(N=N*) + (1-alpha) * (1/|M|) * sum F1(a, a*)` where I(N=N*) checks correct function selection and F1 measures token-level overlap on matched parameters. Weight w_corr(t) increases from 2 to 3.
3. **Efficiency Regularization (R_len):** Range [0,1] via piecewise Gaussian with time-annealing.

The dynamic weighting shifts focus "from syntax to semantics as training progresses."

---

### 8. Ablation Studies

**Table 2 -- Feedback Quality Ablation (Qwen3-8B):**

| Configuration | Overall Accuracy | Delta |
|---|---|---|
| GRPO baseline | 42.75% | -- |
| Fission-Static (generic error message) | 44.00% | +1.25% |
| Fission-Dynamic (learned Error Simulator) | 46.75% | +4.00% |

The +2.75% gap between Static and Dynamic demonstrates that the Error Simulator's precise, context-aware diagnostics are substantially more useful than generic "error occurred" messages. However, even generic feedback provides some benefit (+1.25%).

**Section 4.5 -- Trigger Frequency:** Performance is stable for small N (frequent fission triggers) but degrades with sparse updates (large N). The Miss Param and Long Context error categories are most sensitive to trigger frequency.

---

### 9. Code Availability

**No code has been released.** The paper contains no mention of a GitHub repository, code release, or open-source plans. No repository was found through GitHub searches. The authors do provide detailed hyperparameters (learning rate 1e-6, batch size 8, G=8, max prompt 12,800 tokens, max response 4,096 tokens) and Algorithm 1 pseudocode.

---

### 10. Follow-Up Work and Citations

Given the paper was posted in January 2026 (approximately 4 months ago), I was unable to find a specific citation count. Related concurrent work in the same space includes:

- **RC-GRPO** (arXiv:2602.03025) -- "Reward-Conditioned GRPO for Multi-Turn Tool Calling Agents" -- addresses a similar problem (vanishing updates in multi-turn GRPO) but via reward-conditioned trajectory generation rather than error-augmented fission. It does not appear to cite Fission-GRPO directly.
- **CLEANER** (arXiv:2601.15141) -- "Self-Purified Trajectories Boost Agentic Reinforcement Learning" -- a concurrent paper addressing error-contaminated trajectories via retrospective replacement rather than forward recovery.
- **SeeUPO** (arXiv:2602.06554) -- "Sequence-Level Agentic-RL with Convergence Guarantees" -- also evaluated on BFCL v4, focuses on training stability via sequential updates rather than error recovery specifically.

---

### Known Limitations and Criticisms

From the literature review and the paper's own discussion:

1. **Simulator dependency:** Requires ~2K teacher-written error instances (generated via Claude Sonnet 4); scalability to new tool domains is unclear.
2. **Threshold sensitivity:** Error identification depends on tunable delta_corr; sensitivity analysis is limited.
3. **Single benchmark:** Evaluated only on BFCL v4 Multi-Turn; generalization to other tool-use benchmarks, code execution, or web interaction is untested.
4. **Computational overhead:** Multiplicative resampling (G' extra rollouts per error) increases training cost, though the paper does not quantify this overhead.
5. **No tree-based comparison:** The paper does not engage with the tree-search/branching literature, leaving an important comparison gap.

---

Sources:
- [arXiv Abstract: Fission-GRPO](https://arxiv.org/abs/2601.15625)
- [arXiv HTML Full Paper](https://arxiv.org/html/2601.15625v1)
- [HuggingFace Paper Page](https://huggingface.co/papers/2601.15625)
- [Literature Review - Moonlight](https://www.themoonlight.io/en/review/robust-tool-use-via-fission-grpo-learning-to-recover-from-execution-errors)
- [Paper Notes by AkihikoWatanabe](https://github.com/AkihikoWatanabe/paper_notes/issues/4277)
- [RC-GRPO (related work)](https://arxiv.org/abs/2602.03025)
- [CLEANER (concurrent work)](https://arxiv.org/abs/2601.15141)
- [SeeUPO (concurrent work)](https://arxiv.org/abs/2602.06554)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "027b3721-cffa-49c5-a57c-9f73b5beb873",
  "isSidechain": true,
  "agentId": "a878e485d3c9127b8",
  "requestId": "req_011Cawep5VTwPrEJa1VfRFhc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41abbed6-acab-4c26-99b8-45eb94833446",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011k1FjzBiYvy7Prni4cyDA8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2276,
      "cache_read_input_tokens": 25058,
      "output_tokens": 3604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2276
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3604,
          "cache_read_input_tokens": 25058,
          "cache_creation_input_tokens": 2276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2276,
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
