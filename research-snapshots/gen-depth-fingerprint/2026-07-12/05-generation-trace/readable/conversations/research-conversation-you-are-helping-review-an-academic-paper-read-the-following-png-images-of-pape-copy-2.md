# Research conversation: You are helping review an academic paper. Read the following PNG images of paper appendix pages and provide a DETAILED t

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a75ed30f04a8f55c3.jsonl`
- **Structured JSON:** [`f412d2dbd7d51d6076da.json`](../../sessions/f4/f412d2dbd7d51d6076da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-17T11:03:45.576Z_

You are helping review an academic paper. Read the following PNG images of paper appendix pages and provide a DETAILED transcription/summary of all content. Focus especially on:
- All appendix sections
- Additional experimental results, downstream tasks
- Length confound analysis
- LOFO (Leave-One-Feature-Out) analysis
- Any other ablation or supplementary results
- Any tables and figures with exact numbers

Read these image files:
1. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p14.png
2. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p15.png
3. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p16.png
4. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p17.png

Report EVERYTHING you see - all text, all numbers, all technical details. Do not summarize - give me the full content. This is for a peer review and I need every detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "a75ed30f04a8f55c3",
  "type": "user",
  "uuid": "7948f92f-0a33-42c2-b7d9-6ce7aa301039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T11:03:45.578Z_

```json
{
  "parentUuid": "7948f92f-0a33-42c2-b7d9-6ce7aa301039",
  "isSidechain": true,
  "agentId": "a75ed30f04a8f55c3",
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
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
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
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "12ccc4d0-b3ae-4dcf-96dc-eb56b77be805",
  "timestamp": "2026-05-17T11:03:45.578Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-17T11:03:50.695Z_

<details open><summary>🔧 Tool call — Read · `toolu_018FFpqkALhWrLcRn4Vk18eS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12ccc4d0-b3ae-4dcf-96dc-eb56b77be805",
  "isSidechain": true,
  "agentId": "a75ed30f04a8f55c3",
  "requestId": "req_011Cb82gRwetsx16xR145eBa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66752835-67e1-4636-8ea8-fb867dd1e354",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcaN1w8cJXcDWvQpSAhQfn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9887,
      "cache_read_input_tokens": 9144,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 9144,
          "cache_creation_input_tokens": 9887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9887,
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

### Tool call

_source line 4 · 2026-05-17T11:03:51.146Z_

<details open><summary>🔧 Tool call — Read · `toolu_011dTcsyeaYdyhYLnryvNuhr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66752835-67e1-4636-8ea8-fb867dd1e354",
  "isSidechain": true,
  "agentId": "a75ed30f04a8f55c3",
  "requestId": "req_011Cb82gRwetsx16xR145eBa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "299f3d29-8ec7-45ea-8d97-6219752e7148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcaN1w8cJXcDWvQpSAhQfn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9887,
      "cache_read_input_tokens": 9144,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 9144,
          "cache_creation_input_tokens": 9887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9887,
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

### Tool call

_source line 5 · 2026-05-17T11:03:52.257Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H6qguhnX62R9AKH4U8qRpE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "299f3d29-8ec7-45ea-8d97-6219752e7148",
  "isSidechain": true,
  "agentId": "a75ed30f04a8f55c3",
  "requestId": "req_011Cb82gRwetsx16xR145eBa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41c25f07-5278-482c-a915-3c5a1f08ff18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcaN1w8cJXcDWvQpSAhQfn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9887,
      "cache_read_input_tokens": 9144,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 9144,
          "cache_creation_input_tokens": 9887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9887,
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

### Tool call

_source line 6 · 2026-05-17T11:03:52.261Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xe8dRcBMEVJ19pLGgx4fGF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41c25f07-5278-482c-a915-3c5a1f08ff18",
  "isSidechain": true,
  "agentId": "a75ed30f04a8f55c3",
  "requestId": "req_011Cb82gRwetsx16xR145eBa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d345020-b7bd-4727-8ecb-752bae071d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcaN1w8cJXcDWvQpSAhQfn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9887,
      "cache_read_input_tokens": 9144,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 9144,
          "cache_creation_input_tokens": 9887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9887,
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

_source line 7 · 2026-05-17T11:03:56.507Z_

<details><summary>↩ Tool result · `toolu_018FFpqkALhWrLcRn4Vk18eS`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66752835-67e1-4636-8ea8-fb867dd1e354",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "a75ed30f04a8f55c3",
  "type": "user",
  "uuid": "80636f43-01b4-43b1-9228-6fab23769315",
  "sourceToolAssistantUUID": "66752835-67e1-4636-8ea8-fb867dd1e354",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T11:03:56.900Z_

<details><summary>↩ Tool result · `toolu_011dTcsyeaYdyhYLnryvNuhr`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "299f3d29-8ec7-45ea-8d97-6219752e7148",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "a75ed30f04a8f55c3",
  "type": "user",
  "uuid": "1c74a935-edfa-4f17-a203-274568f33eee",
  "sourceToolAssistantUUID": "299f3d29-8ec7-45ea-8d97-6219752e7148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T11:03:57.153Z_

<details><summary>↩ Tool result · `toolu_01Xe8dRcBMEVJ19pLGgx4fGF`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d345020-b7bd-4727-8ecb-752bae071d6f",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "a75ed30f04a8f55c3",
  "type": "user",
  "uuid": "0040443e-ac46-4582-b747-5c6321d85a48",
  "sourceToolAssistantUUID": "9d345020-b7bd-4727-8ecb-752bae071d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T11:03:57.168Z_

<details><summary>↩ Tool result · `toolu_01H6qguhnX62R9AKH4U8qRpE`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41c25f07-5278-482c-a915-3c5a1f08ff18",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "a75ed30f04a8f55c3",
  "type": "user",
  "uuid": "aaeb2854-59ba-4a25-9721-2f313700c8e4",
  "sourceToolAssistantUUID": "41c25f07-5278-482c-a915-3c5a1f08ff18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-17T11:06:19.420Z_



Here is the full detailed transcription of all four appendix pages (pages 14-17):

---

## PAGE 14

### Table 9: Leave-one-feature-out ablation (6-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.

| Dropped feature | LOGO F1 | Δ vs Full |
|---|---|---|
| entropy_max | 0.774 | −1.50 pp |
| entropy_mean | 0.783 | −0.63 pp |
| ttr | 0.784 | −0.55 pp |
| hapax_ratio | 0.785 | −0.42 pp |
| tail_decay | 0.786 | −0.33 pp |
| entropy_std | 0.786 | −0.29 pp |
| entropy_min | 0.789 | −0.01 pp |
| Full (7 features) | 0.789 | — |

The text states: "entropy_min is fully redundant (Δ = +0.01 pp), consistent with its near-zero permutation importance (0.015). Six of seven features contribute positively to the ensemble, confirming that the 7-feature design is not over-specified."

### G Confusion Matrix

"Table 10 reports the aggregated confusion matrix from 6-generator leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth ≥ 2)."

### Table 10: Aggregated 3-class confusion matrix from 6-generator LOGO evaluation (N = 27,529). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8%) is 3× more frequent than as gen-0 (6.2%), indicating that gen-1 text already carries detectable recursive distortion.

| | Pred gen-0 | Pred gen-1 | Pred gen-2+ |
|---|---|---|---|
| True gen-0 | 5,911 (89.4%) | 510 (8.0%) | 173 (2.6%) |
| True gen-1 | 394 (6.2%) | 4,435 (70.5%) | 1,185 (18.8%) |
| True gen-2+ | 64 (0.4%) | 3,468 (23.7%) | 11,119 (75.9%) |

### H Classifier Sensitivity

"To verify that the depth signal resides in the features rather than the classifier, we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest in place of XGBoost (Table 11). All other settings (the same 7 features, 3-class labels, and class-balanced downsampling) are kept identical. For Logistic Regression we apply standard scaling to the features."

"Both tree-based classifiers achieve LOGO F1 ≈ 0.70, and even a linear model reaches 0.725, well above the 0.33 chance baseline for three classes. The per-generator ranking is also consistent across"

### Table 11: LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1. (6-generator LOGO; 3-class.)

| Classifier | Avg F1 | Llama-3 | Pt-4o | Pt-4.5p | Yi-1.5 | Mn-7B | Qw-3 | Qw-3B |
|---|---|---|---|---|---|---|---|---|
| XGBoost | 0.789 | 0.76 | 0.88 | 0.83 | 0.74 | 0.73 | 0.85 | — |
| RandomForest | 0.703 | 0.70 | 0.82 | 0.79 | 0.67 | 0.54 | 0.69 | — |
| LogReg | 0.725 | 0.71 | 0.83 | 0.78 | 0.61 | 0.68 | 0.73 | — |

"classifiers (Pythia-1B easiest, Qwen3-8B hardest), confirming that discriminative power originates in the entropy and lexical features, not in classifier capacity."

### Sampling Analysis

"To assess robustness to decoding hyperparameters, we regenerate Qwen3-1.7B continuation chains under three sampling configurations (the remaining five generators retain their default configurations) and re-evaluate the 6-generator LOGO protocol (Table 12)."

### Table 12: Depth classification under varying sampling parameters. All other settings match the default pipeline. (6-generator LOGO; 3-class and binary.)

| Config | Temp | Top-p | 3-class F1 | Binary F1 | entropy_mean ρ |
|---|---|---|---|---|---|
| Default | 0.6 | 0.9 | 0.789 | 0.786 | — |
| Default | 0.3 | 1.0 | 0.789 | 0.786 | −0.602 |
| Medium | 0.7 | 0.9 | 0.776 | 0.774 | −0.512 |
| Hot | 1.0 | 0.95 | 0.738 | 0.730 | −0.392 |

"The depth signal is robust to moderate sampling variation: low and default configurations differ by at most 0.3 pp in both 3-class and binary F1, and entropy-depth Spearman correlations remain strong (ρ < −0.40). At high temperature (t=1.0, top-p=0.95), classification degrades by approximately 5 pp and the entropy-depth correlation collapses to near zero (ρ = −0.002). This is consistent with the hypothesis that depth features are shaped by the sampling mechanism (§5): elevated temperature injects sufficient randomness to flatten the distributional drift that accumulates across generation steps, effectively masking the depth signal. The practical implication is that depth fingerprinting applies reliably under standard decoding regimes but should not be expected to generalize to high-entropy sampling settings."

### I Robustness to Text Perturbation

"We assess robustness to post-generation text modification by randomly replacing words at varying rates and re-evaluating the 8-generator LOGO pipeline (Table 13). Random word replacement represents a worst-case perturbation: real human"

---

## PAGE 15

"editing preserves semantic coherence, so practical degradation is expected to be substantially lower than these estimates."

### Table 13: Robustness to random word replacement under 8-gen LOGO evaluation (binary: gen-1 vs. gen-2+). Bootstrap 95% CI on binary F1 (n = 1000).

| Perturbation rate | Binary F1 | 95% CI | 3-class F1 |
|---|---|---|---|
| 0% (baseline) | 0.695 | [0.680, 0.710] | 0.737 |
| 5% | 0.610 | 0.635, 0.680 | — |
| 10% | 0.614 | [0.599, 0.629] | 0.697 |
| 20% | 0.501 | [0.576, 0.603] | 0.367 |

"Binary depth discrimination (gen-1 vs. gen-2+) degrades sub-linearly: the first 5% replacement causes the sharpest drop (−4.6pp), with diminishing marginal impact thereafter (−3.6 pp for 5%→10%, −2.3 pp for 10%→20%). At 10% replacement, binary F1 remains 0.614, well above the 0.50 random baseline, indicating that depth signal survives moderate perturbation."

"Three-class classification is more sensitive (0.737→0.367 at 20%), because distinguishing gen-0 from gen-1 relies heavily on lexical diversity features (TTR, hapax ratio) that are directly disrupted by word replacement. The binary metric, which excludes gen-0, is inherently more robust since it depends primarily on reference-model entropy features distributed across many tokens."

**Feature subset degradation.** "Table 14 compares perturbation robustness of the full 7-feature ensemble against an entropy-only subset (5 reference-model features). The higher unperturbed binary F1 of the entropy-only subset (0.833 vs. 0.695) reflects the strong discriminability of reference-model features for the coarse binary task (gen-1 vs. gen-2+); however, lexical features are essential for the finer-grained ordinal task (3-class F1: 0.737 vs. 0.688) and provide greater robustness under perturbation. At 20% replacement, the 7-feature ensemble surpasses entropy-only on binary F1 (0.591 vs. 0.569), despite starting from a lower baseline. Random word replacement dramatically alters per-token context, making entropy features (computed over the full token sequence) extremely sensitive to noise. Lexical features (TTR, hapax), as document-level summary statistics, are more stable under per-word perturbation and act as stabilizers in the full ensemble. The crossover confirms that degradation in the full feature set reflects genuine signal disruption rather than a lexical-feature artifact."

### Table 14: Feature subset degradation under random word replacement (8-gen LOGO). Entropy-only: 5 reference-model features. 7-feature: full ensemble including lexical features.

| Perturbk | Entr-only Bin | 7-feat Bin | Entropy-only 3-cl | 7-feat 3-cl |
|---|---|---|---|---|
| 0% | 0.833 | 0.695 | 0.688 | 0.737 |
| 5% | 0.667 | 0.636 | 0.488 | — |
| 10% | 0.587 | 0.614 | 0.457 | 0.672 |
| 20% | 0.569 | 0.591 | 0.372 | 0.367 |

**Baseline comparison.** "Table 15 compares robustness across detection methods under identical perturbation conditions (8-gen LOGO, binary F1: gen-1 vs. gen-2+)."

### Table 15: Robustness under random word replacement (8-gen LOGO, binary F1). Bold indicates highest F1 at each perturbation rate.

| Method | 0% | 10% | 20% |
|---|---|---|---|
| 7-feature ensemble | **0.695** | 0.600 | 0.614 | 0.961 (? unclear) |
| LD-Score | 0.672 | 0.643 | **0.877** (? unclear) | **0.671** |
| FastDetectGPT | 0.673 | 0.431 | 0.133 | — |
| Avg-LogProb | 0.537 | 0.433 | 0.068 (? unclear) | — |

"Robustness operates at chance-level on the binary task; its distinguishing figures are not meaningful."

"The 7-feature ensemble achieves the highest unperturbed binary F1 (0.695), but LD-Score surpasses it under perturbation due to near-zero degradation (−0.6 pp across the full 0%→20% range). FastDetectGPT and Avg-LogProb exhibit severe non-monotonic degradation at higher perturbation rates, likely because random perturbation introduces distributional artifacts that these token-level methods detect as anomalies. Avg-LogProb is the most fragile overall (−34.7 pp at 10%), while FastDetectGPT drops sharply at 5% (−13.4 pp) before partially recovering. LD-Score's near-invariance to perturbation, consistent with its reliance on corpus-level distributional divergence rather than token-level likelihoods. The 7-feature ensemble offers the highest starting performance among single-reference methods, with sublinear degradation (−10.4 pp at 20%)."

**LLM-simulated sentence regeneration.** "To test robustness under semantically coherent editing, we use Qwen3-0.6B-Base to randomly regenerate 1-3 sentences per passage (avg 1.69 sentences, ~50% edit distance) and re-evaluate the 8-gen LOGO pipeline. Binary F1 drops from 0.692 to 0.647 (−4.5 pp, 6.5% relative), 3-class F1 drops from 0.739 to 0.667 (−7.1 pp, 9.7% rel-"

---

## PAGE 16

"ative). The binary degradation (−4.5 pp) is nearly identical to that caused by 5% random word replacement (−4.6 pp), despite the LLM rephrase altering ~50% of characters. This asymmetry arises because LLM-generated replacements preserve the underlying statistical fingerprint of the generation process (entropy dynamics, depth-accumulated distributional drift), whereas random word substitution directly destroys local statistical signals. Depth fingerprinting thus captures deep generative structure that survives semantics-preserving edits."

**Seed complexity.** "Performance is stable across seed text complexity: stratifying seeds by vocabulary richness (TTR terciles) yields maximum F1 variation of 1.1 pp across groups."

### J Cross-Domain Generalization

"We evaluate whether depth signal generalizes beyond Wikipedia by constructing generation chains from three additional domains: News articles, Academic abstracts, and Code documentation. For each domain, we sample 500 seed texts and generate chains of depth 3 using three generators (Pythia-1B, Qwen3-1.7B, Mistral-7B). The same 7-feature ensemble and LOGO protocol are applied."

### Table 16: Cross-domain depth classification under LOGO evaluation (binary: gen-1 vs. gen-2+). Three generators × 200 seeds per domain. Bootstrap 95% CIs (n = 1000).

| Domain | Binary F1 | 95% CI | 3-class F1 |
|---|---|---|---|
| News | 0.784 | [0.757, 0.779] | 0.634 |
| Academic | 0.788 | [0.770, 0.804] | 0.691 |
| Code | 0.739 | [0.720, 0.757] | 0.622 |

"All three non-Wikipedia domains achieve binary F1 > 0.73 under leave-one-generator-out evaluation, demonstrating that depth signal is not an artifact of Wikipedia text properties."

**Domain × temperature interaction.** "Cross-domain generation used t=1.0, top-p=1.0 (vs. the main experiment's t=0.7, top-p=0.9). Supplementary evaluation at t=0.7 reveals a domain × temperature interaction: the main Wikipedia experiment favors lower temperature (t=0.7 yields +6 pp over t=1.0, Appendix H), while cross-domain evaluation favors higher temperature (t=1.0 yields +3 to +11 pp over t=0.7; News 0.746 vs. 0.712, Academic 0.739 vs. 0.628, Code"

"0.754 vs. 0.687). This asymmetry likely reflects reference-model calibration: Pythia-410M, trained predominantly on web text, detects subtle per-step drift in Wikipedia but requires larger distributional divergence (produced by higher temperature) to detect depth signal in out-of-distribution domains. This finding suggests that reference model selection is a key factor for cross-domain deployment of depth fingerprinting."

**3-class inversion as DDR evidence.** "In the cross-domain setting, 3-class F1 (0.62-0.65) falls below binary F1 (0.74-0.75), reversing the pattern observed in the main experiment (3-class 0.762 > binary 0.664). This inversion reflects degraded gen-0 vs. gen-1 separation: the Pythia-410M reference model is calibrated to Wikipedia text, so its baseline entropy estimates are less discriminative for out-of-domain human text, compressing the feature distance between gen-0 and gen-1. The binary task (gen-1 vs. gen-2+) is unaffected because both classes are generated under identical domain and decoding conditions; recurrence drift is a relative change that does not depend on absolute calibration. This pattern provides additional evidence that DDR captures generation-process invariants rather than domain-specific text properties: depth signal remains robust even when the human-vs-machine boundary becomes less distinct."

### K Error Analysis of Binary Classification

"We analyze the distribution and characteristics of binary classification errors (gen-1 vs. gen-2+) across the 8-generator LOGO evaluation (N = 29,095 samples, overall error rate 28.08%)."

**Error asymmetry.** "Errors are heavily asymmetric: 86.2% are false negatives (gen-2+ predicted as gen-1) and only 13.8% are false positives (gen-1 predicted as gen-2+). The classifier systematically under-predicts depth, consistent with the DDR framework: shallow gen-2+ samples that have not yet accumulated sufficient distributional drift are indistinguishable from gen-1."

**Prediction error rates.** "Error rates decrease monotonically with depth: depth-2 samples are the primary failure point (48.42% error rate), followed by depth 3 (29.17%) and depth 4 (20.32%). Depth-1 false positive rate is 7.11%. The monotonic decrease confirms that deeper generations accumulate progressively stronger fingerprints,"

---

## PAGE 17

"making the gen-1→gen-2 transition the hardest to detect."

**Per-generator variation.** "Table 17 shows error rates vary substantially across generators, correlating with model scale: larger models (Mistral-7B, Qwen3-8B) produce text closer to gen-1 characteristics, making depth discrimination harder."

### Table 17: Binary classification error rates by generator (8-gen LOGO). Sorted by error rate descending.

| Generator | Family | Samples | Errors | Error rate |
|---|---|---|---|---|
| Mistral-7B-0.1 | Mistral | 3,831 | 1,734 | 45.06% |
| Qwen3-8B | Qwen | 3,802 | 1,397 | 36.85% |
| Llama-3.2-1B | Llama | 3,685 | 1,112 | 30.18% |
| OLMo-2-0.5B | OLMo | 3,715 | 1,058 | 28.48% |
| Pythia-2.8B | Pythia | 3,611 | 866 | 23.96% |
| Qwen3-1.7B | Pythia (sic) | 3,811 | 831 | 21.81% |
| Pythia-1B | Pythia | 3,611 | 775 | 21.46% |
| Qwen3-0.6B | Qwen | 3,500 | 648 | 18.53% |

**Feature-level explanation.** "Mann-Whitney U tests comparing correctly vs. incorrectly classified samples reveal that the drifting features show significant distributional differences between correct and incorrect predictions: entropy_mean (p < 10^-10), TTR (p < 10^-20), and hapax_ratio (p < 10^-39). In contrast, shape features show no discriminating power: entropy_max (p = 0.584) and tail_decay (p = 0.653). Misclassified gen-2+ samples have systematically higher TTR (0.464 vs. 0.302 for correct) and entropy_mean (2.26 vs. 1.57), indicating they retain gen-1-like lexical diversity and have not undergone the distributional convergence characteristic of deeper generations. This is consistent with the DDR framework (§4.2): errors concentrate where depth-accumulated drift is insufficient, and shape features (which are near-stationary by design) provide no additional discriminative signal for error correction."

### L Downstream Utility

"Can depth-aware data curation improve downstream language model quality? We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table 18)."

"The results are unambiguous: data quantity dominates depth composition. Training on all 12,299 samples yields the lowest perplexity (2.335). At equal sample count (n = 3,951), random subsampling (2,367) *outperforms* both depth-stratified selection (depth 0-1: 2,387) and binary"

### Table 18: Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean ± std across 3 seeds). At equal sample count, random subsampling (2,367) outperforms depth-aware curation (depth 0-1: 2,387, binary filtered: 2,389).

| Variant | n | Test PPL |
|---|---|---|
| All depths | 12,299 | 2.335 ± 0.000 |
| Size-matched (random) | 3,951 | 2.367 ± 0.000 |
| Depth 0-1 only | 3,951 | 2.387 ± 0.000 |
| Binary filtered | 3,951 | 2.389 ± 0.000 |
| Depth 0 only | 997 | 2.848 ± 0.000 (? unclear) |

"selection filtering (2,389). Cross-seed variance is below 0.002 across all variants, confirming the robustness of this null result."

"Restricting training to human-only text (depth 0, n = 997) produces a sharp perplexity increase to 2.848, driven primarily by the 5× reduction in data volume rather than depth composition per se."

"A paired sign-flip test over 3 seeds yields p = 0.25 for size-matched vs. depth 0-1 (Δ ppl = 0.020); the test is severely underpowered (minimum achievable p-value with n = 3 is 1/2^3 = 0.125). All three seeds show size-matched < depth 0-1 (cross-seed variance below 0.002), providing consistent directional evidence despite inadequate statistical power. Cohen's d = −3.48 reflects the near-zero cross-seed variance, not practical importance: the absolute PPL difference is 0.020 on a baseline of 2.367."

"Knowing the generation depth of a document does not, by itself, make it more or less useful for training."

---

This completes the full transcription of all four appendix pages (14-17). The appendices covered are:

- **Table 9 (LOFO analysis)** - Leave-one-feature-out with 7 features
- **G: Confusion Matrix** (Table 10) - 3-class aggregated confusion matrix
- **H: Classifier Sensitivity** (Table 11) - XGBoost vs RandomForest vs LogReg; (Table 12) - Sampling parameter robustness
- **I: Robustness to Text Perturbation** (Tables 13, 14, 15) - Random word replacement, feature subset degradation, baseline comparison, LLM-simulated regeneration
- **J: Cross-Domain Generalization** (Table 16) - News, Academic, Code domains; domain x temperature interaction; 3-class inversion analysis
- **K: Error Analysis of Binary Classification** (Table 17) - Per-generator error rates, feature-level Mann-Whitney U tests
- **L: Downstream Utility** (Table 18) - Fine-tuning perplexity across data curation strategies, null result for depth-aware curation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaeb2854-59ba-4a25-9721-2f313700c8e4",
  "isSidechain": true,
  "agentId": "a75ed30f04a8f55c3",
  "requestId": "req_011Cb82hFm1PXLoUkpBzDpUb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f32e7e8b-79e6-40e3-b9b5-b772fbea9602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nw3enAPKamph6yTS2DHHHc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 19031,
      "output_tokens": 5979,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5979,
          "cache_read_input_tokens": 19031,
          "cache_creation_input_tokens": 2715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2715,
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
