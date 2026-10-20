# Research conversation: Search for any work that combines multi-view information bottleneck (or augmentation consistency) with token selection/p

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a644a44cbd3bce4c6.jsonl`
- **Structured JSON:** [`b1497ae9e9339c03b35a.json`](../../sessions/b1/b1497ae9e9339c03b35a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-14T06:22:46.479Z_

Search for any work that combines multi-view information bottleneck (or augmentation consistency) with token selection/pruning for robustness. This is the core novelty claim of a paper I'm reviewing. Search for:

1. "multi-view information bottleneck token selection" or "augmentation consistent token pruning"
2. "contrastive token selection robustness" or "invariant token selection augmentation"
3. "augmentation consistency loss token pruning" 
4. Also search for "TCA token condensation test-time adaptation" (arXiv 2410.14729) - this may be a close competitor showing token condensation improves distribution shift robustness

Also check: is there any work applying information bottleneck specifically at the TOKEN level (not representation level) in vision transformers? Search for "token level information bottleneck ViT" or "per-token variational information bottleneck".

Use WebSearch. Report any papers found that directly combine these concepts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "b46f04aa-c161-4bc5-8790-11323e6e6df4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T06:22:46.487Z_

```json
{
  "parentUuid": "b46f04aa-c161-4bc5-8790-11323e6e6df4",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
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
  "uuid": "60a613ff-d2b8-4ad5-8387-a08b57e2c6f6",
  "timestamp": "2026-05-14T06:22:46.487Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T06:22:49.744Z_



I'll search for papers combining these specific concepts. Let me first load the WebSearch tool, then run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60a613ff-d2b8-4ad5-8387-a08b57e2c6f6",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1ypu9sYCkgvp7JKYemy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2eb5859f-4430-4080-b194-17fab63fd307",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKgcvAG7SWERtb6LjP5PWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 768,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 4 · 2026-05-14T06:22:49.987Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011xXWuC379To6WdzPePR2ou`</summary>

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
  "parentUuid": "2eb5859f-4430-4080-b194-17fab63fd307",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1ypu9sYCkgvp7JKYemy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e08e98a1-6f98-49bc-8438-4ce672a6e7c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKgcvAG7SWERtb6LjP5PWr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 8223,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 768
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 768,
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

_source line 5 · 2026-05-14T06:22:49.991Z_

<details><summary>↩ Tool result · `toolu_011xXWuC379To6WdzPePR2ou`</summary>

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
  "parentUuid": "e08e98a1-6f98-49bc-8438-4ce672a6e7c7",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "af955d0e-3de9-4357-b81a-f19e4489de6c",
  "sourceToolAssistantUUID": "e08e98a1-6f98-49bc-8438-4ce672a6e7c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T06:22:52.292Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af955d0e-3de9-4357-b81a-f19e4489de6c",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yqABkBgeQXRmCYVnmY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e977fecb-1980-4dce-90c4-127d74a12022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CEAG9obfuLfyqceJr3Wc7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 7 · 2026-05-14T06:22:52.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TsReXjD6Hd7zW9biLpnjeY`</summary>

```json
{
  "query": "multi-view information bottleneck token selection vision transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e977fecb-1980-4dce-90c4-127d74a12022",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yqABkBgeQXRmCYVnmY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97f83d1f-1472-485c-ba38-7269f2310f54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CEAG9obfuLfyqceJr3Wc7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 8 · 2026-05-14T06:22:53.238Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LcMyzu6bn4hZd5t9RAd5GT`</summary>

```json
{
  "query": "augmentation consistent token pruning robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97f83d1f-1472-485c-ba38-7269f2310f54",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yqABkBgeQXRmCYVnmY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e149332-031a-41df-a65a-71c9af0f57e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CEAG9obfuLfyqceJr3Wc7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 9 · 2026-05-14T06:22:53.689Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VEXumNEQiAJ2Ce9Lrb83h5`</summary>

```json
{
  "query": "contrastive token selection robustness invariant token selection augmentation ViT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e149332-031a-41df-a65a-71c9af0f57e9",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yqABkBgeQXRmCYVnmY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae0a25fc-c05e-4b13-af15-e9e1cc7466a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CEAG9obfuLfyqceJr3Wc7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 10 · 2026-05-14T06:22:54.180Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PqQo7witeWJJpidrSXQQZG`</summary>

```json
{
  "query": "augmentation consistency loss token pruning vision transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae0a25fc-c05e-4b13-af15-e9e1cc7466a6",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yqABkBgeQXRmCYVnmY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34d022bf-80dd-40d5-8138-16169c42daeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CEAG9obfuLfyqceJr3Wc7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1420,
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

_source line 11 · 2026-05-14T06:22:54.644Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cdg17q2BAQSKurfKEXWSh7`</summary>

```json
{
  "query": "TCA token condensation test-time adaptation arXiv 2410.14729"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34d022bf-80dd-40d5-8138-16169c42daeb",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yqABkBgeQXRmCYVnmY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2e6fe50-b8d3-432e-a127-a1477befced1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CEAG9obfuLfyqceJr3Wc7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8991,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1420
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 315,
          "cache_read_input_tokens": 8991,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1420,
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

_source line 12 · 2026-05-14T06:22:54.652Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013apR9V8ca7FC3nkU5C69ou`</summary>

```json
{
  "query": "token level information bottleneck ViT per-token variational information bottleneck"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2e6fe50-b8d3-432e-a127-a1477befced1",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yqABkBgeQXRmCYVnmY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c34e2d31-3440-4a28-8f5a-906f4c1504a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CEAG9obfuLfyqceJr3Wc7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 8991,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1420
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 315,
          "cache_read_input_tokens": 8991,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1420,
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

_source line 13 · 2026-05-14T06:23:00.707Z_

<details><summary>↩ Tool result · `toolu_01VEXumNEQiAJ2Ce9Lrb83h5`</summary>

```text
Web search results for query: "contrastive token selection robustness invariant token selection augmentation ViT"

Links: [{"title":"[2008.05659] What Should Not Be Contrastive in Contrastive Learning","url":"https://ar5iv.labs.arxiv.org/html/2008.05659"},{"title":"Understanding and Improving Robustness of Vision ...","url":"https://papers.neurips.cc/paper_files/paper/2022/file/67662aa16456e0df65ab001136f92fd0-Paper-Conference.pdf"},{"title":"Keras documentation: Learning to tokenize in Vision Transformers","url":"https://keras.io/examples/vision/token_learner/"},{"title":"Improving Shift Invariance in Convolutional Neural Networks with","url":"https://openaccess.thecvf.com/content/WACV2025/papers/Saha_Improving_Shift_Invariance_in_Convolutional_Neural_Networks_with_Translation_Invariant_WACV_2025_paper.pdf"},{"title":"A-ViT: Adaptive Tokens for Efﬁcient Vision Transformer Hongxu Yin Arash Vahdat","url":"https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.pdf"},{"title":"Analyzing Data Augmentation Techniques for Contrastive Learning in Recommender Models[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202505.0245/v1/download"},{"title":"[2101.11986] Tokens-to-Token ViT: Training Vision Transformers from Scratch on ImageNet","url":"https://arxiv.org/abs/2101.11986"},{"title":"TFS-ViT: Token-Level Feature Stylization for Domain Generalization","url":"https://arxiv.org/html/2303.15698v3"},{"title":"Tokens-to-Token ViT: Training Vision Transformers from Scratch on ImageNet","url":"https://openaccess.thecvf.com/content/ICCV2021/papers/Yuan_Tokens-to-Token_ViT_Training_Vision_Transformers_From_Scratch_on_ImageNet_ICCV_2021_paper.pdf"},{"title":"The Role of ViT Design and Training in Robustness To ...","url":"https://daiqi1989.github.io/assets/pdf/TMM_final_Robustness.pdf"}]

Based on the search results, I found several relevant papers addressing topics related to your query about contrastive learning, token selection, robustness, and Vision Transformers (ViT):

## Key Findings

**Contrastive Learning and Robustness:**
A method for contrastive learning achieves better performance against state-of-the-art baselines and demonstrates superior transferability, generalizability and robustness across tasks and categories. One approach learns both transformation dependent and invariant representations by constructing multiple embeddings, each of which is not contrastive to a single type of transformation.

**Vision Transformer Robustness:**
Patch-based negative augmentation consistently improves robustness of ViTs on ImageNet based robustness benchmarks and is complementary to traditional positive data augmentation techniques and batch-based negative examples in contrastive learning.

**Token-Level Approaches:**
Token-level feature stylization approaches have been developed to improve the generalization capabilities of ViTs in out-of-distribution scenarios, using attention maps in multi-head self-attention layers to guide augmentation toward relevant regions.

A-ViT enables adaptive token computation for vision transformers by augmenting the transformer block with an adaptive halting module that computes a halting probability per token.

The results cover several related areas: contrastive learning frameworks, invariance properties, data augmentation strategies for ViTs, and token-level mechanisms for improving model robustness and efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae0a25fc-c05e-4b13-af15-e9e1cc7466a6",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "87eb49e7-93bd-4d4e-b433-1b7e2fd4e858",
  "sourceToolAssistantUUID": "ae0a25fc-c05e-4b13-af15-e9e1cc7466a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T06:23:00.828Z_

<details><summary>↩ Tool result · `toolu_01LcMyzu6bn4hZd5t9RAd5GT`</summary>

```text
Web search results for query: "augmentation consistent token pruning robustness"

Links: [{"title":"Where Do Tokens Go? Understanding Pruning Behaviors in STEP at High Resolutions","url":"https://arxiv.org/html/2509.14165v1"},{"title":"Joint Token Pruning and Squeezing Towards More Aggressive Compression of","url":"https://openaccess.thecvf.com/content/CVPR2023/papers/Wei_Joint_Token_Pruning_and_Squeezing_Towards_More_Aggressive_Compression_of_CVPR_2023_paper.pdf"},{"title":"Learned Token Pruning for Efficient Transformer Inference Sehoon Kim Sheng Shen","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/EECS-2023-119.pdf"},{"title":"A SIMILARITY- BASED TOKEN PRUNING FOR VISION ...","url":"https://openreview.net/notes/edits/attachment?id=7I9FCztgnH&name=pdf"},{"title":"Spatio-Temporal Token Pruning for Efficient High-Resolution GUI Agents","url":"https://arxiv.org/html/2602.23235"},{"title":"Token-Level Pruning in Attention Models[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202503.0590"},{"title":"[2602.17196] EntropyPrune: Matrix Entropy Guided Visual Token Pruning for Multimodal Large Language Models","url":"https://arxiv.org/abs/2602.17196"},{"title":"Revisiting Token Pruning for Object Detection and Instance Segmentation","url":"https://arxiv.org/html/2306.07050v3"},{"title":"Automatic pruning rate adjustment for dynamic token reduction in vision transformer | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-025-06265-z"},{"title":"Common-token Optimized Model Pruning Across Channels ...","url":"https://arxiv.org/pdf/2509.06836"}]

The search results reveal several relevant research papers on token pruning and robustness. Here's a summary of the key findings:

## Overview of Token Pruning Research

Token pruning has emerged as an effective technique to enhance the efficiency of transformers by dynamically removing less informative tokens during inference, thereby reducing computational complexity while maintaining competitive accuracy.

## Augmentation-Consistent Pruning

A particularly relevant finding concerns augmentation consistency in token pruning. One approach prunes non-essential tokens while preserving crucial semantic consistency across different augmented views of the same image, significantly enhancing training efficiency without compromising accuracy. This method addresses a critical issue in self-supervised learning where asymmetric pruning may occur where tokens containing the same semantic information across two branches are pruned inconsistently, causing a mismatch in the representations and potentially impairing the model's ability to learn robust features.

## Robustness and Token Reactivation

Reactivating pruned tokens in the backbone on demand can improve model performance by adapting to layer-wise attention and recovering mis-pruned tokens for better robustness. This flexibility allows pruning to be more robust, as mis-pruned tokens have the opportunity to become active again.

## Gradient-Based Approaches

Saliency-based pruning removes tokens with the smallest gradient magnitudes, as they contribute the least to model predictions, while Hessian-based pruning uses higher-order derivatives to measure the curvature of the loss function.

These approaches collectively address the challenge of maintaining robustness while achieving computational efficiency through intelligent token reduction strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e149332-031a-41df-a65a-71c9af0f57e9",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "640771e6-2aab-4574-b140-fcddea7829f6",
  "sourceToolAssistantUUID": "2e149332-031a-41df-a65a-71c9af0f57e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T06:23:01.574Z_

<details><summary>↩ Tool result · `toolu_013apR9V8ca7FC3nkU5C69ou`</summary>

```text
Web search results for query: "token level information bottleneck ViT per-token variational information bottleneck"

Links: [{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"[1612.00410] Deep Variational Information Bottleneck","url":"https://arxiv.org/abs/1612.00410"},{"title":"Deep Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=HyxQzBceg"},{"title":"EFFICIENT VISION TRANSFORMER BY INFORMATION ...","url":"https://openreview.net/pdf?id=Jwgw3znxT3"},{"title":"Deep Variational Information Bottleneck | Request PDF","url":"https://www.researchgate.net/publication/311299697_Deep_Variational_Information_Bottleneck"},{"title":"[PDF] Variational Information Bottleneck for Effective Low-Resource Fine-Tuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Variational-Information-Bottleneck-for-Effective-Mahabadi-Belinkov/a4b9530c820b5fdb9edd869555cc7a2c2a1d21ad"},{"title":"Comprehensive Information Bottleneck for Unveiling Universal Attribution to","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Hong_Comprehensive_Information_Bottleneck_for_Unveiling_Universal_Attribution_to_Interpret_Vision_CVPR_2025_paper.pdf"},{"title":"Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/html/2407.15219v1"},{"title":"Variational Information Bottleneck Explained - kevin frans blog","url":"https://kvfrans.com/variational-information-bottleneck-explained/"},{"title":"Revisiting the Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=w10KdRwcMk"}]

I've found relevant research on your query. Here are the key findings:

## Information Bottleneck Methods for Vision Transformers

A recent approach called Transformer with Information Bottleneck inspired Token Merging (IBTM) performs token merging in a learnable scheme. IBTM is compatible with many popular and compact transformer networks, such as MobileViT and EfficientViT, and it reduces the FLOPs and the inference time of the vision transformers while maintaining or even improving the prediction accuracy.

The IBTM is motivated by the reduction of the Information Bottleneck (IB), and a novel and separable variational upper bound for the IB loss is derived. The principle of IB is to maximize the mutual information between merged tokens and task labels while minimizing the mutual information between the merged tokens and input. IB encourages the network to learn merged tokens more correlated with the class labels while reducing their correlation with the input.

## Deep Variational Information Bottleneck Foundation

A variational approach allows parameterizing the information bottleneck model using a neural network and leverage the reparameterization trick for efficient training, called "Deep Variational Information Bottleneck" or Deep VIB. Models trained with the VIB objective outperform those trained with other forms of regularization, in terms of generalization performance and robustness to adversarial attack.

## Recent Token Merging Work

A Transformer with Learnable Token Merging (LTM) performs token merging in a learnable scheme. A novel and separable variational upper bound for the IB loss is derived, and token merging masks are generated to reduce such variational upper bound for the IB loss.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c34e2d31-3440-4a28-8f5a-906f4c1504a0",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "104d29c6-4b93-4fee-b1de-e7012e26ca97",
  "sourceToolAssistantUUID": "c34e2d31-3440-4a28-8f5a-906f4c1504a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T06:23:01.748Z_

<details><summary>↩ Tool result · `toolu_01TsReXjD6Hd7zW9biLpnjeY`</summary>

```text
Web search results for query: "multi-view information bottleneck token selection vision transformer"

Links: [{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"LEARNING ROBUST REPRESENTATIONS VIA MULTI- ...","url":"https://openreview.net/pdf?id=B1xwcyHFDr"},{"title":"[2507.04388] Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers","url":"https://arxiv.org/abs/2507.04388"},{"title":"Comprehensive Information Bottleneck for Unveiling Universal Attribution to","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Hong_Comprehensive_Information_Bottleneck_for_Unveiling_Universal_Attribution_to_Interpret_Vision_CVPR_2025_paper.pdf"},{"title":"Elastic Attention Cores for Scalable Vision Transformers","url":"https://arxiv.org/html/2605.12491"},{"title":"Context-Aware Token Selection and Packing for Enhanced Vision Transformer","url":"https://arxiv.org/html/2410.23608"},{"title":"Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/html/2407.15219v1"},{"title":"Making Vision Transformers Efficient from A Token Sparsification View","url":"https://openaccess.thecvf.com/content/CVPR2023/papers/Chang_Making_Vision_Transformers_Efficient_From_a_Token_Sparsification_View_CVPR_2023_paper.pdf"},{"title":"Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers","url":"https://arxiv.org/html/2507.04388"},{"title":"Visual Transformer with Differentiable Channel Selection: An Information Bottleneck Inspired Approach","url":"https://proceedings.mlr.press/v235/wang24ak.html"}]

Based on the web search results, here are the key findings related to multi-view information bottleneck token selection in vision transformers:

## Information Bottleneck Inspired Token Merging

A novel transformer block called IBTM (Transformer with Information Bottleneck inspired Token Merging) performs token merging in a learnable scheme. The IBTM is motivated by the reduction of the Information Bottleneck (IB), and a novel and separable variational upper bound for the IB loss is derived, with the architecture of the mask module designed to reduce this upper bound.

## Token Selection and Efficiency

A sparse attention mechanism called Select and Pack Attention (SPA) dynamically selects informative tokens from images using a linear gating layer and packs them together to enable efficient GPU batch training and inference. This mechanism includes a multi-scale selection label to explicitly supervise token selection.

## Multi-View Information Bottleneck

The information bottleneck method has been extended to the unsupervised multi-view setting, based on the assumption that each view provides the same task-relevant information, allowing one to improve generalization by discarding all information not shared by both views from the representation.

## Comprehensive Information Bottleneck for Vision Transformers

A comprehensive information bottleneck (CoIBA) discovers the relevant information in each targeted layer by applying information bottleneck in multiple targeted layers and estimating comprehensive information by sharing a parametric damping ratio across the layers.

These approaches collectively demonstrate how information bottleneck principles can be applied to optimize vision transformers through intelligent token selection and merging strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97f83d1f-1472-485c-ba38-7269f2310f54",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "63fb5814-d291-4249-b0a3-44320cde7b42",
  "sourceToolAssistantUUID": "97f83d1f-1472-485c-ba38-7269f2310f54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T06:23:02.068Z_

<details><summary>↩ Tool result · `toolu_01PqQo7witeWJJpidrSXQQZG`</summary>

```text
Web search results for query: "augmentation consistency loss token pruning vision transformer"

Links: [{"title":"Automatic pruning rate adjustment for dynamic token reduction in vision transformer | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-025-06265-z"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425010711"},{"title":"Which Tokens to Use? Investigating Token Reduction in Vision Transformers","url":"https://openaccess.thecvf.com/content/ICCV2023W/NIVT/papers/Haurum_Which_Tokens_to_Use_Investigating_Token_Reduction_in_Vision_Transformers_ICCVW_2023_paper.pdf"},{"title":"Learned Token Pruning for Efficient Transformer Inference Sehoon Kim Sheng Shen","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/EECS-2023-119.pdf"},{"title":"Token Transforming: A Unified and Training-Free Token Compression Framework for Vision Transformer Acceleration","url":"https://arxiv.org/html/2506.05709"},{"title":"Efficient Token Compression for Vision Transformer with Spatial Information Preserved","url":"https://arxiv.org/html/2503.23455v1"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification | OpenReview","url":"https://openreview.net/forum?id=kR95DuwwXHZ"},{"title":"Revisiting Token Pruning for Object Detection and Instance ...","url":"https://rpg.ifi.uzh.ch/docs/WACV24_Liu.pdf"},{"title":"Joint Token Pruning and Squeezing Towards More Aggressive Compression of","url":"https://openaccess.thecvf.com/content/CVPR2023/papers/Wei_Joint_Token_Pruning_and_Squeezing_Towards_More_Aggressive_Compression_of_CVPR_2023_paper.pdf"},{"title":"Token Pruning within the Attention Mechanism for Efficient Vision Transformers","url":"https://ceur-ws.org/Vol-4082/paper8.pdf"}]

I've found research on token pruning in Vision Transformers. Here are the key findings from the search results:

## Token Pruning in Vision Transformers

The search results reveal several approaches to token pruning for Vision Transformer acceleration:

**Main Token Reduction Methods:**
Prior work on sparsification of the input token sequence is divided into two primary paradigms: token pruning and token merging.

**Notable Approaches:**

1. **Dynamic Token Sparsification:** A dynamic token sparsification framework prunes redundant tokens progressively and dynamically for vision transformer acceleration. This method can reduce 31%-37% FLOPs while the accuracy drop is within 0.5%.

2. **Token Merging vs. Pruning:** ToMe uses lightweight soft bipartite matching to merge similar tokens and achieves twice the throughput without re-training with a slight accuracy loss.

3. **Learned Token Pruning:** Soft pruning schemes are nearly identical in behavior to hard pruning, yet their differentiable form allows for backpropagation and gradient-based optimizations.

4. **Recent Framework Approaches:** A many-to-many Token Transforming framework serves as a generalization of all existing methods and reserves the most information, even enabling training-free acceleration.

**Combining Pruning and Merging:** The Prune and Merge method seamlessly combines token pruning and merging, effectively reducing the overall token count while mitigating information loss.

The research shows that token pruning is an active area addressing the computational challenges of Vision Transformers while maintaining reasonable accuracy levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34d022bf-80dd-40d5-8138-16169c42daeb",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "2ae7b214-ee62-4175-9a55-aff8937e6c42",
  "sourceToolAssistantUUID": "34d022bf-80dd-40d5-8138-16169c42daeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T06:23:02.851Z_

<details><summary>↩ Tool result · `toolu_01Cdg17q2BAQSKurfKEXWSh7`</summary>

```text
Web search results for query: "TCA token condensation test-time adaptation arXiv 2410.14729"

Links: [{"title":"[2410.14729] Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/abs/2410.14729"},{"title":"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/html/2410.14729v3"},{"title":"[2410.14729v3] Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/abs/2410.14729v3"},{"title":"Paper page - Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://huggingface.co/papers/2410.14729"},{"title":"GitHub - Jo-wang/TCA: Official repo for ICCV 2025 paper \"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation\"","url":"https://github.com/Jo-wang/TCA"},{"title":"(PDF) Tokens on Demand: Token Condensation as Training-free Test-time Adaptation","url":"https://www.researchgate.net/publication/385107712_Tokens_on_Demand_Token_Condensation_as_Training-free_Test-time_Adaptation"},{"title":"Is Less More? Exploring Token Condensation as Training-free ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Is_Less_More_Exploring_Token_Condensation_as_Training-free_Test-time_Adaptation_ICCV_2025_paper.pdf"},{"title":"Tokens on Demand: Token Condensation as Training-free Test-time Adaptation | OpenReview","url":"https://openreview.net/forum?id=EK1yOLL7GA&noteId=aa1fhh8o1I"},{"title":"Computer Science Oct 2024","url":"https://arxiv.org/list/cs/2024-10?skip=7300&show=1000"},{"title":"Computation and Language Oct 2024","url":"https://www.arxiv.org/list/cs.CL/2024-10?skip=2350&show=50"}]

I found comprehensive information about the TCA (Token Condensation as Adaptation) paper. Here are the key details:

## Paper Overview

The paper "Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation" was published on arXiv as 2410.14729, and was accepted to ICCV 2025.

## Key Contributions

TCA (Token Condensation as Adaptation) is a training-free adaptation method that condenses token representation by introducing reservoir-based domain anchor tokens for information-preserving token reduction and logits correction.

## Problem and Motivation

While CLIP excels at learning generalizable image representations, it often falls short in zero-shot inference on certain downstream datasets. Traditional test-time adaptation (TTA) mitigates this by adjusting components like normalization layers or context prompts, yet it typically requires large batch sizes and extensive augmentations, leading to high computational costs.

## Performance Results

TCA achieves up to a 21.4% performance improvement over the strongest baseline on cross-dataset benchmark and the CIFAR-100-Corrupted dataset while reducing GFLOPs by 12.2% to 48.9%, with minimal hyperparameter dependency on both CLIP and SigLIP series.

## Technical Approach

To adapt visual embeddings to text embeddings during test-time, TCA utilizes a domain-aware token reservoir (DTR) to retain historical &lt;cls> tokens with the lowest uncertainty as domain anchor tokens.

The authors are Zixin Wang, Dong Gong, Sen Wang, Zi Huang, and Yadan Luo, and the official implementation is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2e6fe50-b8d3-432e-a127-a1477befced1",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "ac5a00cd-817c-4cf8-bee1-99b930a429b6",
  "sourceToolAssistantUUID": "e2e6fe50-b8d3-432e-a127-a1477befced1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T06:23:05.421Z_

Good, I have initial results. Let me now run more targeted follow-up searches to dig deeper into the specific intersection of these concepts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac5a00cd-817c-4cf8-bee1-99b930a429b6",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yr72GzHitNurQ5QM1K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fb5233a-3d74-426a-86bd-80815e1cb1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LPgEX3D6g4Prwe9wtALDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 977,
      "cache_creation_input_tokens": 5184,
      "cache_read_input_tokens": 10411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5184,
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

_source line 20 · 2026-05-14T06:23:06.370Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HXen3D4tVhC3ZrGDp2yrFk`</summary>

```json
{
  "query": "\"information bottleneck\" \"token merging\" IBTM vision transformer robustness augmentation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fb5233a-3d74-426a-86bd-80815e1cb1fd",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yr72GzHitNurQ5QM1K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21b49aba-1d41-493a-82e0-0627d4d589ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LPgEX3D6g4Prwe9wtALDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 977,
      "cache_creation_input_tokens": 5184,
      "cache_read_input_tokens": 10411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5184,
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

_source line 21 · 2026-05-14T06:23:06.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LfkweUA2WqQxFb3mfv8CiK`</summary>

```json
{
  "query": "multi-view consistency token selection self-supervised ViT robust distribution shift"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21b49aba-1d41-493a-82e0-0627d4d589ca",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yr72GzHitNurQ5QM1K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "628b9a7f-3797-417d-b697-8a22565051a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LPgEX3D6g4Prwe9wtALDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 977,
      "cache_creation_input_tokens": 5184,
      "cache_read_input_tokens": 10411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5184,
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

_source line 22 · 2026-05-14T06:23:07.784Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LBn2YqkFPfPjm2J4mQVzkp`</summary>

```json
{
  "query": "\"token pruning\" \"augmentation invariance\" OR \"view consistency\" OR \"multi-view\" robust vision transformer 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "628b9a7f-3797-417d-b697-8a22565051a5",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yr72GzHitNurQ5QM1K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbd980c5-4e54-42f6-8bbd-0297423f304b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LPgEX3D6g4Prwe9wtALDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 977,
      "cache_creation_input_tokens": 5184,
      "cache_read_input_tokens": 10411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5184,
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

_source line 23 · 2026-05-14T06:23:08.320Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MgVwDmvY3QZzAyE7YVd31q`</summary>

```json
{
  "query": "TFS-ViT token feature stylization domain generalization token-level augmentation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbd980c5-4e54-42f6-8bbd-0297423f304b",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yr72GzHitNurQ5QM1K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c496bcbd-2c06-4a0a-915c-2b2153bc05f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LPgEX3D6g4Prwe9wtALDN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 977,
      "cache_creation_input_tokens": 5184,
      "cache_read_input_tokens": 10411,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5184
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 977,
          "output_tokens": 268,
          "cache_read_input_tokens": 10411,
          "cache_creation_input_tokens": 5184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5184,
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

_source line 24 · 2026-05-14T06:23:13.419Z_

<details><summary>↩ Tool result · `toolu_01HXen3D4tVhC3ZrGDp2yrFk`</summary>

```text
Web search results for query: ""information bottleneck" "token merging" IBTM vision transformer robustness augmentation"

Links: [{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"EFFICIENT VISION TRANSFORMER BY INFORMATION ...","url":"https://openreview.net/pdf?id=Jwgw3znxT3"},{"title":"Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/html/2407.15219v1"},{"title":"Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950v1"},{"title":"1 Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/pdf/2407.15219"},{"title":"StructSAM: Structure- and Spectrum-Preserving Token Merging for Segment Anything Models","url":"https://arxiv.org/html/2603.07307"},{"title":"Efficient Visual Transformer by Learnable Token Merging - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40663671/"},{"title":"Efficient Vision Transformer via Token Merger","url":"https://www.researchgate.net/publication/372343417_Efficient_Vision_Transformer_via_Token_Merger"},{"title":"[2407.15219] Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/abs/2407.15219"},{"title":"Efficient Token Compression for Vision Transformer with Spatial Information Preserved","url":"https://arxiv.org/html/2503.23455v1"}]

Based on the web search results, I found relevant research on Information Bottleneck inspired Token Merging (IBTM) for vision transformers. Here are the key findings:

## IBTM Overview

IBTM (Transformer with Information Bottleneck inspired Token Merging) is a novel and compact transformer block that performs token merging in a learnable scheme.

## Core Approach

The IBTM is motivated by the reduction of the Information Bottleneck (IB), and a novel and separable variational upper bound for the IB loss is derived, with the architecture of mask module designed to reduce the derived upper bound for the IB loss.

The principle of IB is to maximize the mutual information between merged tokens and labels while minimizing the mutual information between merged tokens and input.

## Performance and Compatibility

IBTM is compatible with many popular and compact transformer networks, such as MobileViT and EfficientViT, and reduces the FLOPs and inference time of vision transformers while maintaining or even improving prediction accuracy, with experiments replacing transformer blocks in MobileViT, EfficientViT, ViT, and Swin.

Extensive results on image classification and object detection evidence that IBTM renders compact and efficient vision transformers with comparable or much better prediction accuracy than the original vision transformers.

## Robustness Benefits

Extensive empirical and theoretical works have evidenced that models respecting the IB principle enjoy compelling generalization. This connects the IBTM approach to robustness through its adherence to information bottleneck principles, which promote better generalization capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21b49aba-1d41-493a-82e0-0627d4d589ca",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "b217b514-07f0-49cf-a383-44d95f13d8f4",
  "sourceToolAssistantUUID": "21b49aba-1d41-493a-82e0-0627d4d589ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T06:23:13.715Z_

<details><summary>↩ Tool result · `toolu_01LfkweUA2WqQxFb3mfv8CiK`</summary>

```text
Web search results for query: "multi-view consistency token selection self-supervised ViT robust distribution shift"

Links: [{"title":"Multi-View Consistency Self-Supervision","url":"https://www.emergentmind.com/topics/multi-view-consistency-self-supervision"},{"title":"CMC | MSA-ViT: A Multi-Scale Vision Transformer for Robust Malware Image Classification","url":"https://www.techscience.com/cmc/v87n3/66976"},{"title":"DINOv2 Backbone: Self-Supervised ViT","url":"https://www.emergentmind.com/topics/dinov2-backbone"},{"title":"GitHub - raoyongming/DynamicViT: [NeurIPS 2021] [T-PAMI] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification · GitHub","url":"https://github.com/raoyongming/DynamicViT"},{"title":"Adapting Self-Supervised Vision Transformers by Probing Attention-Conditioned Masking Consistency | OpenReview","url":"https://openreview.net/forum?id=OjS3nkNATOw"},{"title":"Making Vision Transformers Efficient from A Token Sparsification View","url":"https://openaccess.thecvf.com/content/CVPR2023/papers/Chang_Making_Vision_Transformers_Efficient_From_a_Token_Sparsification_View_CVPR_2023_paper.pdf"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification | OpenReview","url":"https://openreview.net/forum?id=jB0Nlbwlybm"},{"title":"A-ViT: Adaptive Tokens for Efﬁcient Vision Transformer Hongxu Yin Arash Vahdat","url":"https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.pdf"},{"title":"Transformer-in-Computer-Vision/list_old_20240323.md at main · Yangzhangcst/Transformer-in-Computer-Vision","url":"https://github.com/Yangzhangcst/Transformer-in-Computer-Vision/blob/main/list_old_20240323.md"},{"title":"Superpixel Tokenization for Vision Transformers: Preserving Semantic Integrity in Visual Tokens","url":"https://arxiv.org/html/2412.04680v1"}]

Based on the web search results, I found several relevant topics related to your query. Here's what the research covers:

## Multi-View Consistency and Self-Supervised Learning

Multi-view consistency self-supervision leads to representations substantially more robust to changes in viewpoint, lighting, context, and data distribution shifts than fully supervised baselines. The diversity of augmented or naturally occurring views drives the learning of invariant, discriminative features critical for transferability and performance on downstream tasks such as classification, retrieval, detection, and segmentation.

## Self-Supervised Vision Transformers and Distribution Shift

A combination of carefully curated datasets yields a highly diverse, balanced, and redundancy-minimized dataset—critical for producing all-purpose visual features robust to distribution shifts and downstream domain variations, which is foundational for achieving generalization on a wide array of image distributions and tasks. DINOv2 demonstrates particular strength on challenging out-of-distribution splits.

## Token Selection and Vision Transformers

Regarding token selection, DynamicViT proposes a dynamic token sparsification framework to prune redundant tokens progressively and dynamically for vision transformer acceleration. Additionally, recent work has focused on adapting Vision Transformers initialized with self-supervised learning, with approaches like PACMAC proposing adaptation algorithms inspired by SSL approaches based on learning from partial image inputs generated via masking or cropping.

These approaches collectively address robustness to distribution shifts through multi-view consistency, self-supervised pretraining, and efficient token processing in Vision Transformers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "628b9a7f-3797-417d-b697-8a22565051a5",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "ed2e9cb5-47b5-4b17-8d27-38dff2246103",
  "sourceToolAssistantUUID": "628b9a7f-3797-417d-b697-8a22565051a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T06:23:14.387Z_

<details><summary>↩ Tool result · `toolu_01MgVwDmvY3QZzAyE7YVd31q`</summary>

```text
Web search results for query: "TFS-ViT token feature stylization domain generalization token-level augmentation"

Links: [{"title":"[2303.15698] TFS-ViT: Token-Level Feature Stylization for Domain Generalization","url":"https://arxiv.org/abs/2303.15698"},{"title":"GitHub - Mehrdad-Noori/TFS-ViT_Token-level_Feature_Stylization: [PR 2024] TFS-ViT: Token-Level Feature Stylization for Domain Generalization","url":"https://github.com/Mehrdad-Noori/TFS-ViT_Token-level_Feature_Stylization"},{"title":"TFS-ViT: Token-level feature stylization for domain generalization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S003132032300910X"},{"title":"TFS-ViT: Token-Level Feature Stylization for Domain Generalization","url":"https://arxiv.org/html/2303.15698v3"},{"title":"TFS-ViT: : Token-level feature stylization for domain generalization: Pattern Recognition: Vol 149, No C","url":"https://dl.acm.org/doi/10.1016/j.patcog.2023.110213"},{"title":"TFS-ViT: Token-Level Feature Stylization for Domain Generalization | Request PDF","url":"https://www.researchgate.net/publication/369592652_TFS-ViT_Token-Level_Feature_Stylization_for_Domain_Generalization"},{"title":"TFS-ViT: Token-level feature stylization for domain generalization - Espace ÉTS","url":"https://espace2.etsmtl.ca/id/eprint/28284/"},{"title":"Vision Transformers in Domain Adaptation and Generalization: A Study of Robustness","url":"https://arxiv.org/html/2404.04452v1"},{"title":"Vision Transformers in Domain Adaptation and Domain Generalization: A study of Robustness","url":"https://arxiv.org/html/2404.04452"},{"title":"[PDF] Tokens-to-Token ViT: Training Vision Transformers from Scratch on ImageNet | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Tokens-to-Token-ViT:-Training-Vision-Transformers-Yuan-Chen/dbe077f8521ecbe0a1477d6148c726d4f053d9c9"}]

Based on the search results, here's what I found about TFS-ViT:

## TFS-ViT: Token-Level Feature Stylization for Domain Generalization

TFS-ViT is a token-level feature stylization approach for domain generalization that improves the performance of Vision Transformers (ViTs) to unseen data by synthesizing new domains.

### Key Features

The approach includes a novel strategy for attention-aware stylization, which uses the attention maps of class (CLS) tokens to compute and mix normalization statistics of tokens corresponding to different image regions.

The method selectively stylizes some tokens while leaving others unchanged to increase the diversity of generated samples during training, creating new combinations of stylized tokens while maintaining the underlying structure of the input tokens.

### Advantages

The proposed method is flexible to the choice of backbone model and can be easily applied to any ViT-based architecture with a negligible increase in computational complexity.

Comprehensive experiments show that the approach achieves state-of-the-art performance on five challenging benchmarks for domain generalization, and demonstrates its ability to deal with different types of domain shifts.

### Technical Implementation

The method transforms token features by blending normalization statistics from various domains and applies attention-aware stylization based on the attention maps of class tokens.

The paper was published in 2023 and is authored by Mehrdad Noori and colleagues. The implementation is publicly available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c496bcbd-2c06-4a0a-915c-2b2153bc05f2",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "87bdc983-8054-441b-a134-f2b4496d3ee6",
  "sourceToolAssistantUUID": "c496bcbd-2c06-4a0a-915c-2b2153bc05f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T06:23:16.120Z_

<details><summary>↩ Tool result · `toolu_01LBn2YqkFPfPjm2J4mQVzkp`</summary>

```text
Web search results for query: ""token pruning" "augmentation invariance" OR "view consistency" OR "multi-view" robust vision transformer 2024 2025"

Links: [{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425010711"},{"title":"Automatic pruning rate adjustment for dynamic token reduction in vision transformer | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-025-06265-z"},{"title":"BASED TOKEN PRUNING FOR VISION TRANSFORMERS ...","url":"https://openreview.net/pdf?id=GTcEe5fayC"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"[2403.02991] MADTP: Multimodal Alignment-Guided Dynamic Token Pruning for Accelerating Vision-Language Transformer","url":"https://arxiv.org/abs/2403.02991"},{"title":"Token Pruning in Transformers","url":"https://www.emergentmind.com/topics/token-pruning-framework"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"},{"title":"ToaSt: Token Channel Selection and Structured Pruning for Efficient ViT","url":"https://arxiv.org/html/2602.15720v1"},{"title":"Revisiting Token Pruning for Object Detection in ViTs - WACV 2024 - Studocu","url":"https://www.studocu.com/sg/document/nanyang-technological-university/deep-learning-and-applications/revisiting-token-pruning-for-object-detection-in-vits-wacv-2024/137582002"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network | Request PDF","url":"https://www.researchgate.net/publication/390526506_Efficient_token_pruning_in_vision_transformers_using_an_attention-based_multilayer_network"}]

I've performed a web search for your query on token pruning combined with augmentation invariance, view consistency, multi-view approaches, and robust vision transformers from 2024-2025. Here are the key findings:

## Recent Research on Token Pruning in Vision Transformers

**Core Token Pruning Methods:**
Vision Transformers (ViTs) have demonstrated excellent accuracy in image recognition, but require computationally expensive self-attention operations that increase quadratically with the number of tokens, leading to active research in token pruning for computational cost reduction.

**Multi-View and View Consistency Approaches:**

One significant recent development is SimPrune, which exploits consistency across different augmented views of the same image, addressing challenges where asymmetric pruning may occur when tokens containing the same semantic information across branches are pruned inconsistently. SimPrune with dynamic pruning strategy reduces 24% computation costs without compromising accuracy compared to the DINO baseline.

**Multimodal Approaches:**

Existing token pruning research for compressing Vision-Language Transformers mainly follows a single-modality-based scheme yet ignores the critical role of aligning different modalities for guiding the token pruning process, causing important tokens for one modality to be falsely pruned in another modality branch.

**Recent 2024-2025 Developments:**

Recent pruning approaches include similarity-based methods using inter-token similarity for adaptive per-layer rates, token transition methods that identify informative tokens, and context-aware pruning that integrates task-oriented signals for robust performance.

The search results indicate active research combining token pruning with robustness considerations, though papers explicitly combining all your specified keywords may be more specialized.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbd980c5-4e54-42f6-8bbd-0297423f304b",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "dcfb2051-990e-4db1-b1b0-22f95bdb1b05",
  "sourceToolAssistantUUID": "fbd980c5-4e54-42f6-8bbd-0297423f304b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-14T06:23:19.128Z_

Let me run a few more targeted searches to find the closest competitors to the specific novelty claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcfb2051-990e-4db1-b1b0-22f95bdb1b05",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1ys5hRjeS24V5PFxa8m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c7ceb12-c535-4d15-90da-3c94d999282d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dyqqv7MpeSPM6G5b3snnkj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 15595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4248,
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

_source line 29 · 2026-05-14T06:23:19.466Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QVWQu4YtRnC3P9Kw1MzXLa`</summary>

```json
{
  "query": "SimPrune token pruning self-supervised consistency augmentation DINO 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c7ceb12-c535-4d15-90da-3c94d999282d",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1ys5hRjeS24V5PFxa8m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3369e8c-54b0-4749-b4b4-55727d2f15de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dyqqv7MpeSPM6G5b3snnkj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 15595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4248,
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

_source line 30 · 2026-05-14T06:23:20.459Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kp3VubYQBpZ9YCcrzLp4mS`</summary>

```json
{
  "query": "\"information bottleneck\" token selection pruning robust out-of-distribution ViT 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3369e8c-54b0-4749-b4b4-55727d2f15de",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1ys5hRjeS24V5PFxa8m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56d4a80a-ef4f-4904-8e0a-58cab61347c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dyqqv7MpeSPM6G5b3snnkj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 15595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4248,
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

_source line 31 · 2026-05-14T06:23:20.995Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012NhpdGXCSsKFefS6zfyzUR`</summary>

```json
{
  "query": "token selection robustness corruption distribution shift vision transformer 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56d4a80a-ef4f-4904-8e0a-58cab61347c8",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1ys5hRjeS24V5PFxa8m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "034e2d13-1d17-4be3-88e8-23fe33f4faca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dyqqv7MpeSPM6G5b3snnkj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 15595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4248,
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

_source line 32 · 2026-05-14T06:23:21.783Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RQxxoJgw9PUsY7o77au2DB`</summary>

```json
{
  "query": "CoIBA comprehensive information bottleneck vision transformer token attribution CVPR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "034e2d13-1d17-4be3-88e8-23fe33f4faca",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1ys5hRjeS24V5PFxa8m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc8dfb5b-11da-415c-8af3-5269e59dce57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dyqqv7MpeSPM6G5b3snnkj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 4248,
      "cache_read_input_tokens": 15595,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4248
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1002,
          "output_tokens": 256,
          "cache_read_input_tokens": 15595,
          "cache_creation_input_tokens": 4248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4248,
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

_source line 33 · 2026-05-14T06:23:25.824Z_

<details><summary>↩ Tool result · `toolu_01QVWQu4YtRnC3P9Kw1MzXLa`</summary>

```text
Web search results for query: "SimPrune token pruning self-supervised consistency augmentation DINO 2024"

Links: [{"title":"BASED TOKEN PRUNING FOR VISION TRANSFORMERS ...","url":"https://openreview.net/pdf?id=GTcEe5fayC"},{"title":"A SIMILARITY- BASED TOKEN PRUNING FOR VISION ...","url":"https://openreview.net/notes/edits/attachment?id=7I9FCztgnH&name=pdf"},{"title":"Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning | OpenReview","url":"https://openreview.net/forum?id=GTcEe5fayC"},{"title":"ICLR Poster Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning","url":"https://iclr.cc/virtual/2025/poster/30276"},{"title":"Augmentations vs Algorithms: What Works in Self-Supervised Learning","url":"https://arxiv.org/html/2403.05726v1"},{"title":"DINO: Unlocking Emergent Visual Intelligence in Self-Supervised Vision Transformers | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/dino-unlocking-emergent-visual-intelligence-in-self-supervised-vision-transformers-fbb2be1d7344"},{"title":"Similarity-Aware Token Pruning: Your VLM but Faster","url":"https://arxiv.org/html/2503.11549v1"},{"title":"A Survey on Deep Neural Network Pruning","url":"https://www.computer.org/csdl/journal/tp/2024/12/10643325/1ZAxlmvgXzG"},{"title":"Exploiting CLIP Self-Consistency to Automate Image Augmentation for Safety","url":"https://openaccess.thecvf.com/content/CVPR2024W/SAIAD/papers/Gannamaneni_Exploiting_CLIP_Self-Consistency_to_Automate_Image_Augmentation_for_Safety_Critical_CVPRW_2024_paper.pdf"},{"title":"Prompt-based Dynamic Token Pruning to Guide Transformer Attention in Efficient Segmentation","url":"https://arxiv.org/html/2506.16369v1"}]

Based on the search results, I found detailed information about SimPrune, a novel token pruning approach for self-supervised learning.

## SimPrune Overview

SimPrune is a novel token pruning approach tailored specifically for self-supervised learning (SSL). The method utilizes cross-branch similarity to guide token pruning, maintaining crucial semantic consistency across different augmented views of the same image.

## Key Innovation

SSL's dual-branch encoders make traditional single-branch pruning strategies less effective, as they fail to account for critical cross-branch similarity information, leading to reduced accuracy in SSL. SimPrune addresses this by leveraging cross-branch similarity information to efficiently prune tokens, retaining essential semantic information across dual branches.

## DINO Integration

To adapt SimPrune to the DINOv2 framework, the token matching process first aligns the masked tokens in the view processed by the student model to their counterparts in the full view processed by the teacher model. Subsequently, it performs token matching for the remaining tokens. This approach ensures semantic consistency and prevents misalignment.

## Performance Results

SimPrune incorporates a difficulty-aware pruning strategy to enhance effectiveness. Experimental results show the approach effectively reduces training computation while maintaining accuracy, offering 24% savings in training costs compared to SSL baseline, without sacrificing accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3369e8c-54b0-4749-b4b4-55727d2f15de",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "ba0dc8fa-2e25-454f-b85b-3e0c1ba06876",
  "sourceToolAssistantUUID": "b3369e8c-54b0-4749-b4b4-55727d2f15de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T06:23:28.557Z_

<details><summary>↩ Tool result · `toolu_01Kp3VubYQBpZ9YCcrzLp4mS`</summary>

```text
Web search results for query: ""information bottleneck" token selection pruning robust out-of-distribution ViT 2024 2025"

Links: [{"title":"ToaSt: Token Channel Selection and Structured Pruning for Efficient ViT","url":"https://arxiv.org/html/2602.15720v1"},{"title":"EFFICIENT VISION TRANSFORMER BY INFORMATION ...","url":"https://openreview.net/pdf?id=Jwgw3znxT3"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425010711"},{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"ViTCoP: Accelerating Large Vision-Language Models via Visual and Textual Semantic Collaborative Pruning","url":"https://arxiv.org/html/2601.17818"},{"title":"Token Pruning in Transformers","url":"https://www.emergentmind.com/topics/token-pruning-framework"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"},{"title":"Automatic pruning rate adjustment for dynamic token reduction in vision transformer | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-025-06265-z"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Advancing Transformer Efficiency with Token Pruning[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202503.1577"}]

I've completed the web search for your query on information bottleneck, token selection/pruning, robustness, and out-of-distribution Vision Transformers from 2024-2025. Here are the key findings:

## Main Research Directions

**Information Bottleneck-Guided Token Merging:**
Recent work focuses on learning to merge tokens guided by the information bottleneck theory of deep learning. Specifically, the IBTM (Transformer with Information Bottleneck inspired Token Merging) performs token merging in a learnable scheme and is compatible with popular transformer networks like MobileViT and EfficientViT, reducing FLOPs and inference time while maintaining or improving accuracy.

**Token Pruning and Compression Methods:**
ToaSt employs activation-based statistics for structured removal in ViTs, achieving significant compression without heavy retraining costs. TRAM is the first approach using a multilayer network-based representation of attention matrices for token reduction and works with most ViTs without fine-tuning.

**Robustness and Out-of-Distribution Challenges:**
Token pruning raises concerns about model generalization and robustness, with pruned models potentially struggling when applied to out-of-distribution inputs due to domain shift sensitivity. A recent approach, CompTrack, uses information bottleneck guidance for low-rank dynamic token compression.

**Recent Trends:**
The emerging trend favors dynamic, context-sensitive, layerwise, and soft strategies that adapt token retention to input statistics and downstream constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56d4a80a-ef4f-4904-8e0a-58cab61347c8",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "9dfd4ab2-ed92-472a-8a2d-a65c2198bcb8",
  "sourceToolAssistantUUID": "56d4a80a-ef4f-4904-8e0a-58cab61347c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T06:23:29.282Z_

<details><summary>↩ Tool result · `toolu_012NhpdGXCSsKFefS6zfyzUR`</summary>

```text
Web search results for query: "token selection robustness corruption distribution shift vision transformer 2024 2025 arXiv"

Links: [{"title":"Robustness Tokens: Towards Adversarial Robustness of Transformers","url":"https://arxiv.org/html/2503.10191v1"},{"title":"[2303.11126] Robustifying Token Attention for Vision Transformers","url":"https://arxiv.org/abs/2303.11126"},{"title":"arXiv:2503.10191v1 [cs.LG] 13 Mar 2025","url":"https://arxiv.org/pdf/2503.10191"},{"title":"[2503.10191] Robustness Tokens: Towards Adversarial Robustness of Transformers","url":"https://arxiv.org/abs/2503.10191"},{"title":"The Robustness of Computer Vision Models against ...","url":"https://arxiv.org/pdf/2305.06024"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=850&show=2000"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425010711"},{"title":"Vision Transformers in Domain Adaptation and Generalization: A Study of Robustness","url":"https://arxiv.org/html/2404.04452v1"},{"title":"[2305.14840] Predicting Token Impact Towards Efficient Vision Transformer","url":"https://arxiv.org/abs/2305.14840"},{"title":"[2103.15670] On the Adversarial Robustness of Vision Transformers","url":"https://arxiv.org/abs/2103.15670"}]

I found several relevant papers on arXiv related to token selection, robustness, and vision transformers. Here are the key findings:

## Recent Papers (2024-2025)

**1. Robustness Tokens: Towards Adversarial Robustness of Transformers**
A novel approach specific to the transformer architecture that fine-tunes a few additional private tokens with low computational requirements instead of tuning model parameters as done in traditional adversarial training. The work shows that Robustness Tokens make Vision Transformer models significantly more robust to white-box adversarial attacks while also retaining the original downstream performances. This paper was accepted for publication at ECCV 2024 and posted on arXiv in March 2025 (arXiv:2503.10191).

**2. Robustifying Token Attention for Vision Transformers**
The attention mechanism of ViTs tends to rely on few important tokens (token overfocusing), and these tokens are not robust to corruptions, often leading to highly diverging attention patterns. The paper proposes Token-aware Average Pooling (TAP) module to encourage the local neighborhood of each token to take part in the attention mechanism, and an Attention Diversification Loss (ADL) to force output tokens to aggregate information from a diverse set of input tokens. It improves corruption robustness on ImageNet-C by 2.4% while improving accuracy by 0.4%.

**3. Vision Transformers in Domain Adaptation and Generalization: A Study of Robustness**
This comprehensive review from April 2024 examines how Vision Transformers handle distribution shifts, covering domain adaptation and generalization strategies.

These papers directly address your query about token selection robustness to corruption and distribution shift in vision transformers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "034e2d13-1d17-4be3-88e8-23fe33f4faca",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "ccd0a634-0c40-4ed1-bb4f-88cbf6265744",
  "sourceToolAssistantUUID": "034e2d13-1d17-4be3-88e8-23fe33f4faca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T06:23:29.510Z_

<details><summary>↩ Tool result · `toolu_01RQxxoJgw9PUsY7o77au2DB`</summary>

```text
Web search results for query: "CoIBA comprehensive information bottleneck vision transformer token attribution CVPR 2025"

Links: [{"title":"Comprehensive Information Bottleneck for Unveiling Universal Attribution to","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Hong_Comprehensive_Information_Bottleneck_for_Unveiling_Universal_Attribution_to_Interpret_Vision_CVPR_2025_paper.pdf"},{"title":"CVPR 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/CVPR2025/html/Hong_Comprehensive_Information_Bottleneck_for_Unveiling_Universal_Attribution_to_Interpret_Vision_CVPR_2025_paper.html"},{"title":"Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers","url":"https://arxiv.org/html/2507.04388"},{"title":"[2507.04388] Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers","url":"https://arxiv.org/abs/2507.04388"},{"title":"Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/11091818/11091608/11092428.pdf"},{"title":"Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers | Request PDF","url":"https://www.researchgate.net/publication/394647854_Comprehensive_Information_Bottleneck_for_Unveiling_Universal_Attribution_to_Interpret_Vision_Transformers"},{"title":"CVPR Poster Token Cropr: Faster ViTs for Quite a Few Tasks","url":"https://cvpr.thecvf.com/virtual/2025/poster/32592"},{"title":"Comprehensive Information Bottleneck for Unveiling ...","url":"https://www.computer.org/csdl/proceedings-article/cvpr/2025/436400aa166/299bt0i7dpm"},{"title":"GitHub - 52CV/CVPR-2025-Papers · GitHub","url":"https://github.com/52CV/CVPR-2025-Papers"},{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"}]

I found comprehensive information about CoIBA (Comprehensive Information Bottleneck for Attribution) presented at CVPR 2025. Here's what the research shows:

## Overview

CoIBA is a comprehensive information bottleneck method that discovers the relevant information in each targeted layer to explain the decision-making process.

## Core Approach

The core idea is applying information bottleneck in multiple targeted layers to estimate the comprehensive information by sharing a parametric damping ratio across the layers. Since a channel element placed in the same location but different layers captures different features, CoIBA uniformly perturbs all the channel elements in a single token representation, to handle the information of different layers with a shared parametric ratio.

## Key Differences from Prior Work

IBA obtains the relevant information in the specific bottleneck-inserted layer, thus obtaining layer-wise attribution maps necessarily requires iterative running over the layers. In contrast, CoIBA seeks the layer-wise relevant information from each bottleneck-inserted layer with a universal damping ratio.

## Performance

The attributions provided by CoIBA yield predominant correctness performance compared to baselines, with especially consistent increase in correctness from the Swin transformer demonstrating the generalizability of CoIBA. The extensive experimental results demonstrate the enhancement in faithfulness of the feature attributions provided by CoIBA.

## Citation

The paper was authored by Hong et al. and published at the Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) in June 2025, pages 25166-25175.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc8dfb5b-11da-415c-8af3-5269e59dce57",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "cf49f3bb-3bda-4047-96a2-2c8989f715a2",
  "sourceToolAssistantUUID": "cc8dfb5b-11da-415c-8af3-5269e59dce57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T06:23:32.609Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MuKjkBvhmTvvYnVLpPb37e`</summary>

```json
{
  "query": "multi-view information bottleneck contrastive learning token pruning selection combined 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf49f3bb-3bda-4047-96a2-2c8989f715a2",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yt4x4Qk1TppS2Em2Gh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d02831f-a62c-4f2c-99e5-cd96ddc92e77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QYNVmUezYqsGrvxJzuoYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4994,
      "cache_read_input_tokens": 19843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4994,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 38 · 2026-05-14T06:23:33.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NkxjqaKA2RG9GVWsF5x7jR`</summary>

```json
{
  "query": "\"view-consistent\" OR \"augmentation-consistent\" token selection pruning robustness OOD generalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d02831f-a62c-4f2c-99e5-cd96ddc92e77",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yt4x4Qk1TppS2Em2Gh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17b9f3ca-cea3-4143-92a3-89136fd11186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QYNVmUezYqsGrvxJzuoYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4994,
      "cache_read_input_tokens": 19843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4994,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 39 · 2026-05-14T06:23:33.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QQXKBtG5ypX1iF4L5vQ2eU`</summary>

```json
{
  "query": "variational information bottleneck per-token masking vision transformer robustness 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17b9f3ca-cea3-4143-92a3-89136fd11186",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yt4x4Qk1TppS2Em2Gh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b67c557d-f8f8-4c91-90d0-f58bfdd5c3a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QYNVmUezYqsGrvxJzuoYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4994,
      "cache_read_input_tokens": 19843,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4994
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 19843,
          "cache_creation_input_tokens": 4994,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4994,
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

_source line 40 · 2026-05-14T06:23:40.421Z_

<details><summary>↩ Tool result · `toolu_01QQXKBtG5ypX1iF4L5vQ2eU`</summary>

```text
Web search results for query: "variational information bottleneck per-token masking vision transformer robustness 2024"

Links: [{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"EFFICIENT VISION TRANSFORMER BY INFORMATION ...","url":"https://openreview.net/pdf?id=Jwgw3znxT3"},{"title":"Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/html/2407.15219"},{"title":"[2407.15219] Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/abs/2407.15219"},{"title":"Revisiting the Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=w10KdRwcMk"},{"title":"Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers | Request PDF","url":"https://www.researchgate.net/publication/394647854_Comprehensive_Information_Bottleneck_for_Unveiling_Universal_Attribution_to_Interpret_Vision_Transformers"},{"title":"Variational Vision Transformer with Anti-Over-Smoothing Strategy for Robust Face Recognition | Request PDF","url":"https://www.researchgate.net/publication/399722859_Variational_Vision_Transformer_with_Anti-Over-Smoothing_Strategy_for_Robust_Face_Recognition"},{"title":"Comprehensive Information Bottleneck for Unveiling Universal Attribution to","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Hong_Comprehensive_Information_Bottleneck_for_Unveiling_Universal_Attribution_to_Interpret_Vision_CVPR_2025_paper.pdf"},{"title":"Scale-space Tokenization for Improving the Robustness of Vision Transformers | Proceedings of the 31st ACM International Conference on Multimedia","url":"https://dl.acm.org/doi/10.1145/3581783.3612060"},{"title":"[2507.04388] Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers","url":"https://arxiv.org/abs/2507.04388"}]

Based on the web search results, I found several relevant research papers on variational information bottleneck approaches applied to vision transformers. Here are the key findings:

## Main Research Areas

**Information Bottleneck Inspired Token Merging:**

A novel approach derives a separable variational upper bound for the IB loss, with the architecture of mask modules designed to reduce this upper bound for token merging. LTM-Transformer performs token merging in a learnable scheme and reduces FLOPs and inference time while maintaining or improving prediction accuracy.

**Robustness Applications:**

Recent efforts have optimized supervised deep neural networks using a variational upper bound on the IB objective, leading to enhanced robustness to adversarial attacks. Additionally, models trained with the VIB objective outperform those trained with other forms of regularization in terms of generalization performance and robustness to adversarial attack.

**Vision Transformer Applications:**

Transformer blocks in popular visual transformers including MobileViT, EfficientViT, ViT, and Swin have been replaced with LTM-Transformer blocks, with the approach motivated by reduction of Information Bottleneck and a novel separable variational upper bound for the IB loss.

**Attribution and Interpretability:**

A comprehensive information bottleneck approach discovers relevant information in each targeted layer by applying information bottleneck in multiple layers while sharing a parametric damping ratio across layers.

These recent works (mostly from 2024) combine variational information bottleneck theory with practical techniques like token merging and masking to improve the efficiency and robustness of vision transformers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b67c557d-f8f8-4c91-90d0-f58bfdd5c3a3",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "f397fee1-556e-4eb8-b50e-fe8a7d180515",
  "sourceToolAssistantUUID": "b67c557d-f8f8-4c91-90d0-f58bfdd5c3a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T06:23:41.168Z_

<details><summary>↩ Tool result · `toolu_01MuKjkBvhmTvvYnVLpPb37e`</summary>

```text
Web search results for query: "multi-view information bottleneck contrastive learning token pruning selection combined 2024 2025"

Links: [{"title":"Contrastive Learning via Variational Information Bottleneck - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40392641/"},{"title":"arXiv:2504.09724v3 [cs.CV] 1 Jul 2025 Under Review ADVANCED REVIEW","url":"https://arxiv.org/pdf/2504.09724"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Differentiable Information Bottleneck for Deterministic Multi-view Clustering","url":"https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_Differentiable_Information_Bottleneck_for_Deterministic_Multi-view_Clustering_CVPR_2024_paper.pdf"},{"title":"LLaVA-Prumerge: Adaptive Token Reduction for Efficient Large Multimodal Models | Request PDF","url":"https://www.researchgate.net/publication/404418222_LLaVA-Prumerge_Adaptive_Token_Reduction_for_Efficient_Large_Multimodal_Models"},{"title":"Deep Variational Multivariate Information Bottleneck","url":"https://www.jmlr.org/papers/volume26/24-0204/24-0204.pdf"},{"title":"Information bottleneck fusion for deep multi-view clustering - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705124001862"},{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"},{"title":"Dual-channel optimized multi-view learning via information bottleneck - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705125011499"}]

I found several relevant research papers and resources related to your query. Here's what the search revealed:

## Key Research Areas

**Multi-view Information Bottleneck & Contrastive Learning:**

A framework called CLIMB (Contrastive Learning via variational InforMation Bottleneck) converts the contrastive learning objective to an information bottleneck problem solved via variation approximation. Using DINO as an instantiation, CLIMB achieves 4.5% and 3.5% gain under the k-NN classification metric with EfficientNet-B0 and ResNet-50 as backbones.

The IBFDMVC model for deep multi-view clustering adopts collaborative training where contrastive learning is first employed to enhance representation and IB theory is further used to reduce representation noise.

**Token Pruning and Selection (2024-2025):**

Recent papers in 2024-2025 include CompTrack (AAAI'26) on Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking, and CTR3D (3DV'26) on Cross-view Token Reduction for Dense Multi-view Generation.

Token reduction dynamically prunes, merges, or selectively processes tokens at inference time to optimize speed and memory usage.

**Vision Transformer Applications:**

IBTM (Transformer with Information Bottleneck inspired Token Merging) performs token merging in a learnable scheme, and reduces the FLOPs and inference time of vision transformers while maintaining or even improving prediction accuracy.

The research indicates an active intersection between multi-view learning, information bottleneck theory, contrastive learning approaches, and token optimization strategies across 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d02831f-a62c-4f2c-99e5-cd96ddc92e77",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "518c56b5-0105-4be2-b246-94cd12db9dec",
  "sourceToolAssistantUUID": "8d02831f-a62c-4f2c-99e5-cd96ddc92e77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T06:23:41.443Z_

<details><summary>↩ Tool result · `toolu_01NkxjqaKA2RG9GVWsF5x7jR`</summary>

```text
Web search results for query: ""view-consistent" OR "augmentation-consistent" token selection pruning robustness OOD generalization"

Links: [{"title":"Revisiting Token Pruning for Object Detection and Instance Segmentation","url":"https://arxiv.org/html/2306.07050v3"},{"title":"Towards improving robustness of compressed CNNs","url":"http://www.gatsby.ucl.ac.uk/~balaji/udl2021/accepted-papers/UDL2021-paper-026.pdf"},{"title":"[ICLR 2026] AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models","url":"https://paper.pnu-cvsp.com/AgilePruner/"},{"title":"A SIMILARITY- BASED TOKEN PRUNING FOR VISION ...","url":"https://openreview.net/notes/edits/attachment?id=7I9FCztgnH&name=pdf"},{"title":"Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs","url":"https://arxiv.org/html/2506.10967v1"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Revisiting Token Pruning for Object Detection and Instance Segmentation","url":"https://openaccess.thecvf.com/content/WACV2024/papers/Liu_Revisiting_Token_Pruning_for_Object_Detection_and_Instance_Segmentation_WACV_2024_paper.pdf"},{"title":"Revisiting Visual Token Pruning for Vision-Language Model ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Endo_Feather_the_Throttle_Revisiting_Visual_Token_Pruning_for_Vision-Language_Model_ICCV_2025_paper.pdf"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://arxiv.org/pdf/2502.11501"},{"title":"Automatic pruning rate adjustment for dynamic token reduction in vision transformer | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-025-06265-z"}]

Based on the web search results, I found several relevant papers and research on token selection and pruning with focus on robustness and generalization. Here are the key findings:

## Key Papers on Token Pruning with Robustness Focus

### 1. **SimPrune: A Similarity-Based Token Pruning Method**
SimPrune prunes non-essential tokens while preserving crucial semantic consistency across different augmented views of the same image, significantly enhancing training efficiency without compromising accuracy. This approach is particularly relevant to your query as it explicitly addresses "augmentation-consistency" in token selection.

The paper notes that asymmetric pruning may occur where tokens containing the same semantic information across two branches are pruned inconsistently, causing a mismatch in the representations and potentially impairing the model's ability to learn robust features.

### 2. **Recent Token Pruning Methods for Vision-Language Models**
Recent work evaluates adaptive pruning methods on various Large Vision-Language Models to demonstrate effectiveness and robustness across different benchmarks, with methods showing robust performance on simple images such as ScienceQA and on complex images such as POPE.

### 3. **OOD Robustness and Model Compression**
Research has highlighted that pruned models at high compression ratios can have very low OOD robustness, making them potentially useless in the real world, though this analysis only considered one unstructured method and no data augmentation.

### 4. **Token Reactivation for Robustness**
Token reactivation makes pruning more robust, as mis-pruned tokens have the opportunity to become active again.

The search results reveal an active research area combining token pruning with consistency constraints and robustness considerations, though I didn't find papers specifically titled with the exact "view-consistent" OR "augmentation-consistent" terminology you requested.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17b9f3ca-cea3-4143-92a3-89136fd11186",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "45a00333-39bc-4148-9583-62d27b333e98",
  "sourceToolAssistantUUID": "17b9f3ca-cea3-4143-92a3-89136fd11186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-14T06:23:44.963Z_

Let me do a final round of searches to make sure I've covered the space thoroughly, particularly for the CLIMB paper and any very recent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45a00333-39bc-4148-9583-62d27b333e98",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1ytxC3Z4QEQwP8sd4Vt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0470b867-3375-4e3f-a8b8-77439eb287b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9ANbNEZhQh7sAojdQqhn1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 994,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 24837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2299,
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

_source line 44 · 2026-05-14T06:23:45.490Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VqHngHDtQkrfUTTBGwcHE4`</summary>

```json
{
  "query": "CLIMB contrastive learning variational information bottleneck DINO token 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0470b867-3375-4e3f-a8b8-77439eb287b5",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1ytxC3Z4QEQwP8sd4Vt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0284fa07-2002-43d1-9b61-6e47e7b98784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9ANbNEZhQh7sAojdQqhn1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 994,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 24837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2299,
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

_source line 45 · 2026-05-14T06:23:46.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HPXnroDeMsC8Bm6YxcRyRD`</summary>

```json
{
  "query": "\"token condensation\" OR \"token reduction\" test-time robustness distribution shift CLIP ViT 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0284fa07-2002-43d1-9b61-6e47e7b98784",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1ytxC3Z4QEQwP8sd4Vt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c06d8b8-8f8f-4eb8-8f9b-8ac82a154cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9ANbNEZhQh7sAojdQqhn1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 994,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 24837,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2299
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 994,
          "output_tokens": 167,
          "cache_read_input_tokens": 24837,
          "cache_creation_input_tokens": 2299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2299,
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

_source line 46 · 2026-05-14T06:23:50.963Z_

<details><summary>↩ Tool result · `toolu_01VqHngHDtQkrfUTTBGwcHE4`</summary>

```text
Web search results for query: "CLIMB contrastive learning variational information bottleneck DINO token 2024 2025"

Links: [{"title":"Contrastive Learning via Variational Information Bottleneck - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40392641/"},{"title":"Deep Variational Multivariate Information Bottleneck","url":"https://www.jmlr.org/papers/volume26/24-0204/24-0204.pdf"},{"title":"Contrastive variational information bottleneck for aspect-based sentiment analysis - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095070512301050X"},{"title":"Understanding Self-supervised Learning via Information Bottleneck Principle | OpenReview","url":"https://openreview.net/forum?id=Xr6-DAhePa"},{"title":"Contrastive Graph Structure Learning via Information Bottleneck for Recommendation | OpenReview","url":"https://openreview.net/forum?id=lhl_rYNdiH6"},{"title":"Deep Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=HyxQzBceg"},{"title":"GitHub - ZIYU-DEEP/Awesome-Information-Bottleneck: This is a curated list for Information Bottleneck Principle, in memory of Professor Naftali Tishby. · GitHub","url":"https://github.com/ZIYU-DEEP/Awesome-Information-Bottleneck"},{"title":"Transcending the Annotation Bottleneck: AI-Powered Discovery in Biology and Medicine","url":"https://arxiv.org/html/2602.20100"},{"title":"Deep Variational Information Bottleneck | Request PDF","url":"https://www.researchgate.net/publication/311299697_Deep_Variational_Information_Bottleneck"},{"title":"Looking to Learn: Token-wise Dynamic Gating for Low-Resource Vision-Language Modelling","url":"https://arxiv.org/html/2510.08470"}]

Based on the search results, I found relevant information about CLIMB. Here's what I found:

## CLIMB: Contrastive Learning via Variational Information Bottleneck

CLIMB is a novel contrastive learning framework that stands for Contrastive Learning via variational InforMation Bottleneck. 

### Core Approach
The framework facilitates contrastive learning by reducing superfluous relevance between positive views through representation entropy minimization regularization over vanilla contrastive learning, which forces representations to retain the least information, thus alleviating superfluous relevance from irrelevant views.

### Technical Development
The framework is derived by converting the objective to an information bottleneck problem and solving via variational approximation.

### Performance Results
Using DINO as an instantiation, CLIMB achieves 4.5% and 3.5% gain under the k-NN classification metric with EfficientNet-B0 and ResNet-50 as backbones, respectively.

The search results indicate this is a recent contribution in the field of self-supervised and contrastive learning that combines information bottleneck theory with contrastive learning methods, with successful applications to vision models like DINO (which uses Vision Transformers).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0284fa07-2002-43d1-9b61-6e47e7b98784",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "4b2f32c7-b931-4ac1-aac9-014ba7d92d74",
  "sourceToolAssistantUUID": "0284fa07-2002-43d1-9b61-6e47e7b98784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T06:23:53.826Z_

<details><summary>↩ Tool result · `toolu_01HPXnroDeMsC8Bm6YxcRyRD`</summary>

```text
Web search results for query: ""token condensation" OR "token reduction" test-time robustness distribution shift CLIP ViT 2024 2025"

Links: [{"title":"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/html/2410.14729v3"},{"title":"Is Less More? Exploring Token Condensation as Training-free ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Is_Less_More_Exploring_Token_Condensation_as_Training-free_Test-time_Adaptation_ICCV_2025_paper.pdf"},{"title":"[2410.14729v3] Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/abs/2410.14729v3"},{"title":"GitHub - Jo-wang/TCA: Official repo for ICCV 2025 paper \"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation\"","url":"https://github.com/Jo-wang/TCA"},{"title":"[2410.14729] Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/abs/2410.14729"},{"title":"Track: Poster Session 1 & Exhibit Hall","url":"https://iccv.thecvf.com/virtual/2025/session/2873"},{"title":"Paper page - Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://huggingface.co/papers/2410.14729"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Which Tokens to Use? Investigating Token Reduction in Vision Transformers","url":"https://openaccess.thecvf.com/content/ICCV2023W/NIVT/papers/Haurum_Which_Tokens_to_Use_Investigating_Token_Reduction_in_Vision_Transformers_ICCVW_2023_paper.pdf"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425010711"}]

Based on the search results, I found a highly relevant paper that directly addresses your query. Here are the key findings:

## Primary Research: Token Condensation as Adaptation (TCA)

The core idea is that condensing inattentive tokens can effectively mitigate distribution shifts caused by visual-text misalignment. Token Condensation as Adaptation (TCA) is a training-free adaptation method that condenses token representation by introducing reservoir-based domain anchor tokens for information-preserving token reduction and logits correction.

### Test-Time Robustness and Distribution Shift

Token condensation techniques, originally designed to enhance vision transformer efficiency by refining token usage during inference, are being leveraged to improve test-time performance, with informative tokens improving visual-text alignment in VLMs like CLIP on unseen datasets. 

### Performance Results

TCA achieves up to a 21.4% performance improvement over the strongest baseline on cross-dataset benchmark and the CIFAR-100-Corrupted dataset while reducing GFLOPs by 12.2% to 48.9%, with minimal hyperparameter dependency on both CLIP and SigLIP series.

### Key Findings

Trends similar to ViT-B/16 are observed with the ViT-L/14 architecture, with TCA consistently surpassing baseline methods across multiple datasets while adhering to a limited GFLOPs budget.

This paper was published at ICCV 2025 and addresses exactly the intersection of token condensation/reduction, test-time robustness, and distribution shift handling in CLIP and ViT models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c06d8b8-8f8f-4eb8-8f9b-8ac82a154cdc",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "a644a44cbd3bce4c6",
  "type": "user",
  "uuid": "a60d535e-9c4c-44f0-a4f5-74a13d6825c3",
  "sourceToolAssistantUUID": "6c06d8b8-8f8f-4eb8-8f9b-8ac82a154cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-14T06:24:36.011Z_

Here is my comprehensive report on the literature search.

---

## Summary of Findings

I searched extensively for prior work that **directly combines multi-view/augmentation-consistency information bottleneck with token selection/pruning for robustness**. No single paper was found that unifies all three of these elements (multi-view IB + token selection + robustness). However, several papers address **pairwise combinations** of these ideas and are important for assessing the novelty claim.

---

### 1. Closest Related Work: Papers Combining Subsets of These Ideas

**SimPrune (ICLR 2025)** -- "Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning"
- [OpenReview](https://openreview.net/forum?id=GTcEe5fayC)
- This is arguably the **closest competitor**. SimPrune explicitly enforces **cross-branch (augmentation) consistency during token pruning** in self-supervised learning (DINO/DINOv2). It identifies that asymmetric pruning across two augmented views causes semantic mismatch, and proposes cross-branch similarity-guided pruning to maintain consistency. Reduces 24% training costs without accuracy loss.
- **Key overlap**: Augmentation consistency + token pruning. However, SimPrune's goal is training efficiency (not robustness/OOD), and it does not use an information bottleneck framework.

**IBTM (2024)** -- "Efficient Visual Transformer by Information Bottleneck Inspired Token Merging"
- [OpenReview](https://openreview.net/forum?id=Jwgw3znxT3) / [arXiv:2407.15219](https://arxiv.org/abs/2407.15219)
- Applies the **information bottleneck principle at the token level** to guide learnable token merging. Derives a separable variational upper bound for the IB loss and generates token merging masks to reduce it. Compatible with MobileViT, EfficientViT, ViT, Swin.
- **Key overlap**: Information bottleneck + token-level operation. However, it targets **efficiency** (not robustness) and does not use multi-view/augmentation consistency.

**CLIMB (2025)** -- "Contrastive Learning via Variational Information Bottleneck"
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/40392641/)
- Converts contrastive learning into an information bottleneck problem, reducing superfluous relevance between positive views via representation entropy minimization. Instantiated with DINO. Achieves 4.5%/3.5% gains on k-NN classification with EfficientNet-B0/ResNet-50.
- **Key overlap**: Multi-view IB + contrastive learning. However, it operates at the **representation level**, not the token level, and does not perform token selection/pruning.

**TCA (ICCV 2025)** -- "Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation" (arXiv:2410.14729)
- [arXiv](https://arxiv.org/abs/2410.14729) / [GitHub](https://github.com/Jo-wang/TCA)
- Demonstrates that **token condensation improves robustness to distribution shift** in CLIP/SigLIP at test time. Uses a domain-aware token reservoir and logits correction. Achieves up to 21.4% improvement on cross-dataset benchmarks and CIFAR-100-Corrupted while reducing GFLOPs by 12-49%.
- **Key overlap**: Token reduction + distribution shift robustness. This is a **strong competitor** on the "token selection improves robustness" claim, though it uses no information bottleneck or augmentation consistency -- it is a training-free, test-time method.

---

### 2. Information Bottleneck at the Token Level in ViTs

**CoIBA (CVPR 2025)** -- "Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers"
- [CVPR 2025 paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Hong_Comprehensive_Information_Bottleneck_for_Unveiling_Universal_Attribution_to_Interpret_Vision_CVPR_2025_paper.pdf)
- Applies information bottleneck at multiple layers of ViTs, uniformly perturbing channel elements in single token representations. However, this is for **interpretability/attribution**, not for token selection or robustness.

**IBTM** (described above) is the only work I found that applies a **variational IB objective specifically at the token level** for token merging decisions. No work was found applying a per-token variational information bottleneck explicitly for robustness.

---

### 3. Token-Level Approaches for Robustness (without IB)

**Robustness Tokens (ECCV 2024)** -- arXiv:2503.10191
- Adds learnable "robustness tokens" to ViTs for adversarial robustness, but these are additional tokens, not a selection/pruning mechanism.

**Robustifying Token Attention (2023)** -- arXiv:2303.11126
- Proposes Token-aware Average Pooling and Attention Diversification Loss to combat token overfocusing, improving corruption robustness on ImageNet-C by 2.4%.

**TFS-ViT (Pattern Recognition 2024)** -- "Token-Level Feature Stylization for Domain Generalization"
- [arXiv:2303.15698](https://arxiv.org/abs/2303.15698)
- Performs token-level feature stylization using attention-guided normalization statistics mixing for domain generalization. Selectively stylizes some tokens while leaving others unchanged. Achieves SOTA on 5 domain generalization benchmarks.
- **Key overlap**: Token-level augmentation + robustness/generalization. No IB framework, no token pruning.

---

### 4. Assessment of Novelty

Based on this search, the specific combination of:
- **(a)** Multi-view / augmentation-consistency objective (IB or contrastive)
- **(b)** Token selection / pruning mechanism
- **(c)** Targeting robustness / OOD generalization

appears to be **novel as a unified framework**. No paper was found that combines all three.

However, the reviewer should note these important caveats:

1. **SimPrune** combines (a) augmentation consistency + (b) token pruning, but targets efficiency rather than robustness. The conceptual leap from "augmentation-consistent token pruning for efficiency" to "augmentation-consistent token pruning for robustness" is incremental.

2. **TCA** combines (b) token condensation + (c) robustness to distribution shift, showing that fewer-but-better tokens improve OOD performance -- a direct competitor on the "token selection helps robustness" claim.

3. **IBTM** combines information bottleneck + token-level operations, providing the theoretical machinery. Extending it to multi-view settings is a natural step.

4. **CLIMB** combines multi-view IB + contrastive learning at the representation level. Moving this to the token level is also a natural extension.

The paper under review appears to be stitching together well-established components (multi-view IB from contrastive learning literature + token pruning from efficiency literature) and redirecting them toward robustness. The novelty is real but may be characterized as a **novel combination rather than a fundamentally new idea**.

Sources:
- [SimPrune - ICLR 2025](https://openreview.net/forum?id=GTcEe5fayC)
- [IBTM - Information Bottleneck Token Merging](https://openreview.net/forum?id=Jwgw3znxT3)
- [CLIMB - Contrastive Learning via Variational Information Bottleneck](https://pubmed.ncbi.nlm.nih.gov/40392641/)
- [TCA - Token Condensation as Test-time Adaptation (ICCV 2025)](https://arxiv.org/abs/2410.14729)
- [CoIBA - Comprehensive IB for ViT Attribution (CVPR 2025)](https://openaccess.thecvf.com/content/CVPR2025/papers/Hong_Comprehensive_Information_Bottleneck_for_Unveiling_Universal_Attribution_to_Interpret_Vision_CVPR_2025_paper.pdf)
- [Robustness Tokens (ECCV 2024)](https://arxiv.org/abs/2503.10191)
- [Robustifying Token Attention](https://arxiv.org/abs/2303.11126)
- [TFS-ViT - Token-Level Feature Stylization](https://arxiv.org/abs/2303.15698)
- [TCA GitHub Repository](https://github.com/Jo-wang/TCA)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a60d535e-9c4c-44f0-a4f5-74a13d6825c3",
  "isSidechain": true,
  "agentId": "a644a44cbd3bce4c6",
  "requestId": "req_011Cb1yurvZqdVpwMusu6MF3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca3fd4c1-20d8-4a58-bcec-06cdd16cba23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkrHQRi1acgBx2EdSWnuPx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3159,
      "cache_read_input_tokens": 27136,
      "output_tokens": 2203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3159
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2203,
          "cache_read_input_tokens": 27136,
          "cache_creation_input_tokens": 3159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3159,
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
