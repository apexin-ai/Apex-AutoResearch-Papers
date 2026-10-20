# Research conversation: I need to verify two papers that may be relevant to a proposal about adding runtime verification to fast World Action Mo

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac914d0c5e87d0846.jsonl`
- **Structured JSON:** [`e70ac9fecd5c58c1dc21.json`](../../sessions/e7/e70ac9fecd5c58c1dc21.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-10T21:53:12.508Z_

I need to verify two papers that may be relevant to a proposal about adding runtime verification to fast World Action Models (WAMs):

1. **CoVer** (arXiv 2602.12281, Feb 2026): "Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment". Please fetch this paper's abstract and key details. I need to understand: (a) Does it apply to RUNTIME verification during execution, or is it about test-time compute scaling for action selection? (b) Does it use world model predictions or just contrastive verification? (c) How relevant is it to the specific problem of detecting execution failures in robot manipulation?

2. **Warm Starts Accelerate Conditional Diffusion** (arXiv 2507.09212, July 2025): Please fetch the abstract. Is this about warm-starting denoising from an informed prior instead of N(0,I)? Does it apply to video generation specifically? How related is it to using the current observation as an initialization for partial denoising?

3. **OA-WAM** (arXiv 2605.06481, May 2026): Please fetch the abstract and verify the claims: 97.8% LIBERO, 84.3% LIBERO-Plus geometric avg, slot-based object decomposition.

4. **MotuBrain** (arXiv 2604.27792, April 2026): Verify claims of 95.8% clean RoboTwin, 96.1% randomized, 0.09s latency. Is it the current RoboTwin SOTA?

Use WebSearch and WebFetch to find and read these papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "30fa0de0-925a-4187-8c67-a23d7429fd5a",
  "agentId": "ac914d0c5e87d0846",
  "type": "user",
  "uuid": "45c38315-f39e-49dd-8542-c21fe5d578a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T21:53:12.511Z_

```json
{
  "parentUuid": "45c38315-f39e-49dd-8542-c21fe5d578a4",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
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
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "0a7b2609-f0a0-4f57-a30b-a5ef9bb4b7c2",
  "timestamp": "2026-05-10T21:53:12.511Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T21:53:15.793Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01X54aG2wZRkhdJZmTYZCAqG`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a7b2609-f0a0-4f57-a30b-a5ef9bb4b7c2",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudYQoFeco3LjCmfjdGe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ad21d20-6fbc-4b17-8545-d0ab2921e976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpVQVaPX3sHUZVd9eb8Nr6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 932,
      "cache_read_input_tokens": 8223,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 932
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 932,
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

_source line 4 · 2026-05-10T21:53:15.796Z_

<details><summary>↩ Tool result · `toolu_01X54aG2wZRkhdJZmTYZCAqG`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "4ad21d20-6fbc-4b17-8545-d0ab2921e976",
  "isSidechain": true,
  "promptId": "30fa0de0-925a-4187-8c67-a23d7429fd5a",
  "agentId": "ac914d0c5e87d0846",
  "type": "user",
  "uuid": "2cede4d9-f7f5-4fc2-976c-04190cb37021",
  "sourceToolAssistantUUID": "4ad21d20-6fbc-4b17-8545-d0ab2921e976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T21:53:19.277Z_

I'll fetch all four papers in parallel to verify the claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cede4d9-f7f5-4fc2-976c-04190cb37021",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudYfFQbkDBcyTNNBobv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ff0fd5d-569b-40fa-95d0-644921f7f2aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158m2u9Z8b2gj47wVpL2agy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 6 · 2026-05-10T21:53:24.100Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JZwQpdP5Z8FrPU2wupbBnB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.12281",
  "prompt": "Extract the full abstract, authors, title, and key details of this paper. I need to understand: (1) Is it about RUNTIME verification during execution, or test-time compute scaling for action selection? (2) Does it use world model predictions or contrastive verification? (3) How relevant is it to detecting execution failures in robot manipulation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ff0fd5d-569b-40fa-95d0-644921f7f2aa",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudYfFQbkDBcyTNNBobv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c560967a-24ba-4554-b8d7-420c74d35d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158m2u9Z8b2gj47wVpL2agy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 7 · 2026-05-10T21:53:24.587Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019cM5UJNkKU4eWkKadRtuka`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.09212",
  "prompt": "Extract the full abstract, authors, title, and key details. I need to understand: (1) Is this about warm-starting denoising from an informed prior instead of N(0,I)? (2) Does it apply to video generation specifically? (3) How related is it to using the current observation as an initialization for partial denoising?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c560967a-24ba-4554-b8d7-420c74d35d31",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudYfFQbkDBcyTNNBobv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb1802d1-4195-4e08-bc2a-b5720fd5ed4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158m2u9Z8b2gj47wVpL2agy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 8 · 2026-05-10T21:53:25.032Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011N3gATj3jvh8tswqSQ8DEC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06481",
  "prompt": "Extract the full abstract, authors, title, and key details. I need to verify: (1) Does it claim 97.8% on LIBERO? (2) Does it claim 84.3% LIBERO-Plus geometric average? (3) Does it use slot-based object decomposition? Report all performance numbers mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb1802d1-4195-4e08-bc2a-b5720fd5ed4b",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudYfFQbkDBcyTNNBobv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b061a79d-c489-4ec6-850b-5bc1ebd45652",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158m2u9Z8b2gj47wVpL2agy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 9 · 2026-05-10T21:53:25.113Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MVEAierMFUQJxY8oxR5QCY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.27792",
  "prompt": "Extract the full abstract, authors, title, and key details. I need to verify: (1) Does it claim 95.8% clean RoboTwin? (2) Does it claim 96.1% randomized? (3) Does it claim 0.09s latency? (4) Is it the current RoboTwin SOTA? Report all performance numbers mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b061a79d-c489-4ec6-850b-5bc1ebd45652",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudYfFQbkDBcyTNNBobv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d943509-ba2a-46e5-ac02-9c10f930960c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158m2u9Z8b2gj47wVpL2agy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 10 · 2026-05-10T21:53:29.581Z_

<details><summary>↩ Tool result · `toolu_01MVEAierMFUQJxY8oxR5QCY`</summary>

```text
# MotuBrain Paper Details

**Title:** "MotuBrain: An Advanced World Action Model for Robot Control"

**Authors:** MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, and 16 others

## Performance Claims Verification

**(1) & (2) RoboTwin Success Rates - CONFIRMED:**
The abstract states the model "achieves 95.8% and 96.1% average success on RoboTwin 2.0 under clean and randomized settings, respectively"

**(3) Latency Claim - NOT FOUND:**
The document does not mention 0.09s latency. It only notes "up to 11 Hz inference" and "over 50x speedup" from optimization techniques.

**(4) Current SOTA Status - PARTIALLY ADDRESSED:**
The paper claims it "attains the strongest reported EWMScore in our WorldArena comparison" but does not explicitly state whether this represents current RoboTwin SOTA overall.

## Additional Performance Metrics Mentioned:
- Adapts to new humanoid embodiments with only "50--100 trajectories"
- Inference stack achieves "over 50x speedup" versus baseline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d943509-ba2a-46e5-ac02-9c10f930960c",
  "isSidechain": true,
  "promptId": "30fa0de0-925a-4187-8c67-a23d7429fd5a",
  "agentId": "ac914d0c5e87d0846",
  "type": "user",
  "uuid": "0c8052bf-74f5-451d-8beb-a232f027327b",
  "sourceToolAssistantUUID": "0d943509-ba2a-46e5-ac02-9c10f930960c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T21:53:29.893Z_

<details><summary>↩ Tool result · `toolu_01JZwQpdP5Z8FrPU2wupbBnB`</summary>

```text
# Paper Analysis: CoVer-VLA

## Core Details

**Title:** "Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment"

**Authors:** Jacky Kwok, Xilun Zhang, Mengdi Xu, Yuejiang Liu, Azalia Mirhoseini, Chelsea Finn, Marco Pavone

**Submission:** arXiv:2602.12281 (February 2026)

---

## Key Findings

### (1) **Verification Approach: Test-Time Compute Scaling**
This work focuses on **test-time verification**, not runtime execution monitoring. The method operates during the action-selection phase by:
- Precomputing diverse rephrased instructions from a Vision-Language Model
- Generating multiple action candidates
- Using a verifier to select optimal instructions and actions

This represents a **scaling-through-sampling** strategy rather than detecting mid-execution failures.

### (2) **Verification Type: Contrastive Method**
The paper employs **CoVer (Contrastive Verifier)** for verification. This is explicitly stated as a contrastive architecture—not world model prediction-based. The approach contrasts candidate actions against instructions to identify alignment.

### (3) **Relevance to Failure Detection**
**Limited applicability** to detecting execution failures during robot manipulation. The method addresses the "intention-action gap" at planning time, not during execution. It cannot detect mid-task failures caused by:
- Unexpected environmental changes
- Actuator errors
- Grip failures
- Dynamic obstacles

The framework selects actions *before* deployment, making it unsuitable for runtime failure detection.

---

## Performance Metrics
- 22% in-distribution gains (SIMPLER benchmark)
- 13% out-of-distribution gains
- 45% improvement in real-world experiments
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c560967a-24ba-4554-b8d7-420c74d35d31",
  "isSidechain": true,
  "promptId": "30fa0de0-925a-4187-8c67-a23d7429fd5a",
  "agentId": "ac914d0c5e87d0846",
  "type": "user",
  "uuid": "2478a0e6-887b-461d-81d4-53cb408947b5",
  "sourceToolAssistantUUID": "c560967a-24ba-4554-b8d7-420c74d35d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T21:53:30.793Z_

<details><summary>↩ Tool result · `toolu_011N3gATj3jvh8tswqSQ8DEC`</summary>

```text
# OA-WAM Paper Summary

**Title:** "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation"

**Authors:** Yushan Liu, Peibo Sun, Shoujie Li, Yifan Xie, Lingfeng Zhang, Xintao Chao, Shiyuan Dong, Fang Chen, Xiao-Ping Zhang, Wenbo Ding

## Verification of Claims

**(1) 97.8% on LIBERO?** ✓ **YES**
The abstract states: "OA-WAM matches strong VLA and WAM baselines on LIBERO (97.8%)"

**(2) 84.3% LIBERO-Plus geometric average?** ✗ **NOT FOUND**
The abstract mentions "reaches state-of-the-art performance on the most relevant LIBERO-Plus geometric axes" but provides no specific percentage. No 84.3% figure appears in the provided content.

**(3) Slot-based object decomposition?** ✓ **YES**
The abstract explicitly states: "OA-WAM decomposes each frame into N+1 slot states, with one robot slot and N object slots."

## Performance Numbers Mentioned
- LIBERO: 97.8%
- SimplerEnv: 79.3%
- Causal slot-intervention test swap-binding cosine: 0.87 (vs. maximum 0.09 for holistic baselines)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b061a79d-c489-4ec6-850b-5bc1ebd45652",
  "isSidechain": true,
  "promptId": "30fa0de0-925a-4187-8c67-a23d7429fd5a",
  "agentId": "ac914d0c5e87d0846",
  "type": "user",
  "uuid": "362be64c-75e0-4ffa-82f6-7959a9b9a538",
  "sourceToolAssistantUUID": "b061a79d-c489-4ec6-850b-5bc1ebd45652",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T21:53:31.551Z_

<details><summary>↩ Tool result · `toolu_019cM5UJNkKU4eWkKadRtuka`</summary>

```text
# Paper Summary: Warm Starts Accelerate Conditional Diffusion

**Title:** "Warm Starts Accelerate Conditional Diffusion"

**Authors:** Jonas Scholz, Richard E. Turner

**Submission:** arXiv:2507.09212 (v2, September 29, 2025)

---

## Key Details

**(1) Informed Prior Instead of N(0,I)?**

Yes, exactly. The method replaces the standard Gaussian prior with a context-conditioned one. The abstract states: "Instead of starting generation from an uninformed N(0, I) prior, our deterministic warm-start model predicts an informed prior N(μ̂_C, diag(σ̂²_C))."

**(2) Video Generation Specificity?**

No. The paper describes the approach as "applicable to any standard diffusion or flow matching algorithm" and tests it in "a variety of settings." It focuses on conditional generation broadly, not video specifically.

**(3) Relation to Current Observation Initialization?**

The document doesn't discuss using current observations as partial denoising initialization. Instead, it uses a simple deterministic model to predict a better Gaussian starting distribution, which is conceptually different from progressive refinement from observed frames.

---

## Full Abstract

"Generative models like diffusion and flow-matching create high-fidelity samples by progressively refining noise. The refinement process is notoriously slow, often requiring hundreds of function evaluations. We introduce Warm-Start Diffusion (WSD), a method that uses a simple, deterministic model to dramatically accelerate conditional generation by providing a better starting point. Instead of starting generation from an uninformed N(0, I) prior, our deterministic warm-start model predicts an informed prior N(μ̂_C, diag(σ̂²_C)), whose moments are conditioned on the input context C. This warm start substantially reduces the distance the generative process must traverse, and therefore the number of diffusion steps required, particularly when the context C is strongly informative. WSD is applicable to any standard diffusion or flow matching algorithm, is orthogonal to and synergistic with other fast sampling techniques like efficient solvers, and is simple to implement."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb1802d1-4195-4e08-bc2a-b5720fd5ed4b",
  "isSidechain": true,
  "promptId": "30fa0de0-925a-4187-8c67-a23d7429fd5a",
  "agentId": "ac914d0c5e87d0846",
  "type": "user",
  "uuid": "415a5dbf-7f8b-4f69-ac3b-390f4c70f2a6",
  "sourceToolAssistantUUID": "cb1802d1-4195-4e08-bc2a-b5720fd5ed4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T21:53:36.112Z_

Let me get more details on the OA-WAM paper's LIBERO-Plus claims and MotuBrain's latency/SOTA status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "415a5dbf-7f8b-4f69-ac3b-390f4c70f2a6",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudZpBD6wPBQ3qqvbZsS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ea2248b-dbe6-4126-a1a4-f6fca24544c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KP5vTc5SYPvkDTnB7T6dNQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 1586,
      "cache_read_input_tokens": 11043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1586,
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

_source line 15 · 2026-05-10T21:53:37.066Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TASF3yhSzZx9sexUXESPtV`</summary>

```json
{
  "query": "OA-WAM arXiv 2605.06481 LIBERO-Plus 84.3% geometric average 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ea2248b-dbe6-4126-a1a4-f6fca24544c0",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudZpBD6wPBQ3qqvbZsS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b8e2b82-1b52-4585-9563-46f2d46ee14f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KP5vTc5SYPvkDTnB7T6dNQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 1586,
      "cache_read_input_tokens": 11043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1586,
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

_source line 16 · 2026-05-10T21:53:37.363Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PRKoVTMuVZJw6pE29GnhWt`</summary>

```json
{
  "query": "MotuBrain arXiv 2604.27792 0.09s latency RoboTwin SOTA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b8e2b82-1b52-4585-9563-46f2d46ee14f",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudZpBD6wPBQ3qqvbZsS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12f88956-1722-4233-a48d-b1b7c4bc4df9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KP5vTc5SYPvkDTnB7T6dNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 1586,
      "cache_read_input_tokens": 11043,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 694,
          "output_tokens": 181,
          "cache_read_input_tokens": 11043,
          "cache_creation_input_tokens": 1586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1586,
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

_source line 17 · 2026-05-10T21:53:41.664Z_

<details><summary>↩ Tool result · `toolu_01TASF3yhSzZx9sexUXESPtV`</summary>

```text
Web search results for query: "OA-WAM arXiv 2605.06481 LIBERO-Plus 84.3% geometric average 2026"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"MolmoAct2 Action Reasoning Models for Real-World Deployment","url":"https://arxiv.org/html/2605.02881"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"[2602.06556] LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.06556"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"}]

Based on the search results, I found the paper you're looking for. OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv:2605.06481) was published on May 7, 2026.

Regarding the specific performance metric you mentioned, on the LIBERO-Plus robustness benchmark, OA-WAM sets a new SOTA (State-of-the-Art) on the geometric axes with 85.7% performance on the camera axis. The geometric average is defined as the mean of Camera/Robot/Layout axes. The exact 84.3% geometric average figure you mentioned isn't explicitly stated in the excerpt, but the paper does report strong performance on the LIBERO-Plus benchmark's geometric axes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b8e2b82-1b52-4585-9563-46f2d46ee14f",
  "isSidechain": true,
  "promptId": "30fa0de0-925a-4187-8c67-a23d7429fd5a",
  "agentId": "ac914d0c5e87d0846",
  "type": "user",
  "uuid": "bd6154d9-91e5-4ffb-9c5c-180368ba6cb5",
  "sourceToolAssistantUUID": "7b8e2b82-1b52-4585-9563-46f2d46ee14f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T21:53:43.810Z_

<details><summary>↩ Tool result · `toolu_01PRKoVTMuVZJw6pE29GnhWt`</summary>

```text
Web search results for query: "MotuBrain arXiv 2604.27792 0.09s latency RoboTwin SOTA 2026"

Links: [{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v1"},{"title":"RoboTwin 2.0","url":"https://robotwin-platform.github.io/"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/html/2506.18088v1"},{"title":"RoboTwin: A Robotic Teleoperation Framework Using Digital Twins","url":"https://arxiv.org/html/2506.01027v1"},{"title":"[2506.18088] RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/abs/2506.18088"},{"title":"[2506.01027] RoboTwin: A Robotic Teleoperation Framework Using Digital Twins","url":"https://arxiv.org/abs/2506.01027"},{"title":"Paper page - RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://huggingface.co/papers/2506.18088"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=vAPIIscwc7"},{"title":"GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/robbyant/lingbot-va"}]

Based on the search results, I found information about MotuBrain (arXiv 2604.27792):

MotuBrain addresses a practical concern with world-action models' inference latency by jointly denoising a high-dimensional video latent and an action latent over many diffusion steps. The paper adopts and extends optimizations to tackle this problem, and verifies on the RoboTwin 2.0 that this speedup is essentially lossless, with average task success rates fluctuating within sub-percent margins across optimized and unoptimized configurations.

MotuBrain achieves the best average success rate on RoboTwin, reaching 95.8% in clean scenes and 96.1% in randomized scenes, ranking first in both settings and being the only model on the leaderboard whose average score exceeds 95% under randomized evaluation. At the per-task level, MotuBrain attains a perfect score on 24 tasks under the clean setting and 25 tasks under the randomized setting, surpassing 90% success on 42 clean tasks and 44 randomized tasks.

The search results confirm that MotuBrain demonstrates state-of-the-art (SOTA) performance on the RoboTwin benchmark, though the specific 0.09s latency metric mentioned in your query wasn't detailed in the sections returned from the arXiv paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12f88956-1722-4233-a48d-b1b7c4bc4df9",
  "isSidechain": true,
  "promptId": "30fa0de0-925a-4187-8c67-a23d7429fd5a",
  "agentId": "ac914d0c5e87d0846",
  "type": "user",
  "uuid": "72e56c38-4f24-4ff2-85d1-48bec887544a",
  "sourceToolAssistantUUID": "12f88956-1722-4233-a48d-b1b7c4bc4df9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T21:53:51.549Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Rh81NaRykW1wcHrdD6X2nN`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06481v1",
  "prompt": "Find all performance numbers for LIBERO-Plus, specifically looking for a geometric average of 84.3% across Camera/Robot/Layout axes. Also look for any table showing LIBERO-Plus results with geometric mean scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72e56c38-4f24-4ff2-85d1-48bec887544a",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudaijopDwEKew1VVfAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ef9310d-56d3-42e9-9798-7bde1ce00167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHLGP89mPiQ9Ros1aibX4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2467,
      "cache_read_input_tokens": 12629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2467,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T21:53:53.304Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0166vDHV6EVVQHjnCFduTDYp`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.27792v1",
  "prompt": "Find all mentions of latency, inference speed, Hz, and seconds per step. Specifically looking for 0.09s latency claim, or 11 Hz inference. Also look for any comparison table showing RoboTwin leaderboard rankings to confirm SOTA status."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ef9310d-56d3-42e9-9798-7bde1ce00167",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011CaudaijopDwEKew1VVfAt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0124b927-f9ad-4596-9e4b-33b984ccd875",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHLGP89mPiQ9Ros1aibX4U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2467,
      "cache_read_input_tokens": 12629,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2467
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 256,
          "cache_read_input_tokens": 12629,
          "cache_creation_input_tokens": 2467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2467,
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

_source line 21 · 2026-05-10T21:53:56.100Z_

<details><summary>↩ Tool result · `toolu_01Rh81NaRykW1wcHrdD6X2nN`</summary>

```text
# LIBERO-Plus Performance Summary

The document confirms OA-WAM achieved a **geometric average of 84.3%** on LIBERO-Plus across the three geometric axes (Camera/Robot/Layout).

## Key Performance Metrics from Table 2:

**OA-WAM Results:**
- Camera: 80.5%
- Robot init: 89.6%
- Layout: 82.8%
- **Geometric Average: 84.3%** (+4.8% over π₀.₅)

The paper states: "OA-WAM sets a new SOTA on the three geometric axes most aligned with our hypothesis (Geo Avg 84.3, +4.8% over π₀.₅)."

**Seven-Axis Overall Performance:**
- Light: 96.5%
- Background: 95.9%
- Language: 85.3%
- Sensor Noise: 75.6%
- **Seven-Axis Average: 83.9%** (vs π₀.₅'s 85.7%)

The performance gain concentrates on geometric axes that preserve target object identity while rearranging scenes—the exact regime where OA-WAM's address-based architecture provides advantages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ef9310d-56d3-42e9-9798-7bde1ce00167",
  "isSidechain": true,
  "promptId": "30fa0de0-925a-4187-8c67-a23d7429fd5a",
  "agentId": "ac914d0c5e87d0846",
  "type": "user",
  "uuid": "67f5984a-4131-4125-afd6-7270c70bf26c",
  "sourceToolAssistantUUID": "5ef9310d-56d3-42e9-9798-7bde1ce00167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T21:54:01.844Z_

<details><summary>↩ Tool result · `toolu_0166vDHV6EVVQHjnCFduTDYp`</summary>

```text
# MotuBrain Performance Claims - Verification

## Latency and Inference Speed Claims

**0.09s Latency (11 Hz Inference):**
The document confirms this claim in Table 2, showing cumulative speedup from inference optimizations. With all techniques applied including V2A-style inference, the latency reaches **0.09 seconds**, enabling **11.11 Hz** control frequency - a **54.4× speedup** over the baseline.

Key quote: "after a short joint denoising prefix, the video stream can be frozen and only the action stream continues to update while attending to the cached visual-language context. This design enables **ours to reach a 11 Hz inference frequency**."

## RoboTwin Leaderboard Performance

**SOTA Status Confirmed:**
Table 3 demonstrates MotuBrain's top ranking on the RoboTwin 2.0 benchmark with **95.8% success in clean scenarios and 96.1% in randomized settings** - the highest among all compared models (VLA-based and world-model approaches).

The paper notes it is "the only model on the leaderboard whose average score exceeds 95% under randomized evaluation."

Additional context: MotuBrain achieved perfect 100% scores on 24 clean tasks and 25 randomized tasks, surpassing established baselines like LingBot-VA (92.9%/91.5%) and Fast-WAM (91.9%/91.8%).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0124b927-f9ad-4596-9e4b-33b984ccd875",
  "isSidechain": true,
  "promptId": "30fa0de0-925a-4187-8c67-a23d7429fd5a",
  "agentId": "ac914d0c5e87d0846",
  "type": "user",
  "uuid": "b695e188-434c-40a0-945f-59ad980e4d39",
  "sourceToolAssistantUUID": "0124b927-f9ad-4596-9e4b-33b984ccd875",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T21:54:32.712Z_

I now have comprehensive verification of all four papers. Here is the summary:

---

## 1. CoVer (arXiv 2602.12281, Feb 2026)

**Title:** "Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment"

**Authors:** Jacky Kwok, Xilun Zhang, Mengdi Xu, Yuejiang Liu, Azalia Mirhoseini, Chelsea Finn, Marco Pavone

**Findings:**

**(a) Runtime verification vs. test-time compute scaling?**
This is **test-time compute scaling for action selection**, NOT runtime verification during execution. CoVer operates at decision time: it generates multiple action candidates, rephrases instructions via a VLM, then uses a contrastive verifier to select the best instruction-action pair. It does not monitor execution or detect mid-task failures.

**(b) World model predictions or contrastive verification?**
It uses **contrastive verification** -- a learned verifier that scores alignment between (observation, instruction, action) tuples. No world model predictions are involved.

**(c) Relevance to detecting execution failures in robot manipulation?**
**Low relevance.** CoVer addresses the intention-action gap at planning/selection time, not during execution. It cannot detect grip failures, unexpected environmental changes, or actuator errors mid-task. Performance: +22% in-distribution, +13% OOD (SIMPLER), +45% real-world.

---

## 2. Warm Starts Accelerate Conditional Diffusion (arXiv 2507.09212, July 2025)

**Title:** "Warm Starts Accelerate Conditional Diffusion"

**Authors:** Jonas Scholz, Richard E. Turner

**Findings:**

**(a) Warm-starting from informed prior instead of N(0,I)?**
**Yes, exactly.** The method predicts an informed prior N(mu_hat_C, diag(sigma_hat^2_C)) conditioned on context C, replacing the standard N(0,I) starting point. A simple deterministic model predicts the moments of this better starting distribution.

**(b) Video generation specifically?**
**No.** It is a general-purpose method "applicable to any standard diffusion or flow matching algorithm" and tested across multiple settings. Not video-specific.

**(c) Relation to using current observation as initialization for partial denoising?**
**Conceptually related but mechanistically different.** WSD uses a learned model to predict a better Gaussian starting distribution (still sampling from a Gaussian, just a better one). This differs from directly using the current observation as a partially-noised initialization for denoising. However, the core principle -- "reduce the distance the generative process must traverse" by starting closer to the target -- is the same motivation. WSD is orthogonal to and synergistic with other fast-sampling techniques.

---

## 3. OA-WAM (arXiv 2605.06481, May 2026)

**Title:** "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation"

**Authors:** Yushan Liu, Peibo Sun, Shoujie Li, Yifan Xie, Lingfeng Zhang, Xintao Chao, Shiyuan Dong, Fang Chen, Xiao-Ping Zhang, Wenbo Ding

**Claim Verification:**

| Claim | Status |
|-------|--------|
| 97.8% LIBERO | **CONFIRMED** -- matches strong VLA and WAM baselines |
| 84.3% LIBERO-Plus geometric avg | **CONFIRMED** -- geometric average across Camera (80.5%), Robot init (89.6%), Layout (82.8%) axes; +4.8% over pi_0.5 |
| Slot-based object decomposition | **CONFIRMED** -- decomposes each frame into N+1 slot states (1 robot slot + N object slots) |

Additional metrics: SimplerEnv 79.3%; 7-axis overall average 83.9% (slightly below pi_0.5's 85.7% on non-geometric axes like light/background).

---

## 4. MotuBrain (arXiv 2604.27792, April 2026)

**Title:** "MotuBrain: An Advanced World Action Model for Robot Control"

**Authors:** Chendong Xiang, Fan Bao, Haitian Liu, et al. (MotuBrain Team)

**Claim Verification:**

| Claim | Status |
|-------|--------|
| 95.8% clean RoboTwin | **CONFIRMED** -- but note this is RoboTwin **2.0**, not original |
| 96.1% randomized | **CONFIRMED** -- interestingly, randomized > clean (the paper states this) |
| 0.09s latency | **CONFIRMED** -- via V2A-style inference optimization giving 54.4x speedup over baseline, enabling 11.11 Hz control |
| Current RoboTwin SOTA | **CONFIRMED** -- only model exceeding 95% under randomized evaluation; surpasses LingBot-VA (92.9%/91.5%) and Fast-WAM (91.9%/91.8%) |

Additional: Perfect 100% on 24 clean tasks and 25 randomized tasks; surpasses 90% on 42/44 tasks respectively.

---

Sources:
- [CoVer - arXiv:2602.12281](https://arxiv.org/abs/2602.12281)
- [Warm Starts Accelerate Conditional Diffusion - arXiv:2507.09212](https://arxiv.org/abs/2507.09212)
- [OA-WAM - arXiv:2605.06481](https://arxiv.org/abs/2605.06481)
- [OA-WAM HTML](https://arxiv.org/html/2605.06481v1)
- [MotuBrain - arXiv:2604.27792](https://arxiv.org/abs/2604.27792)
- [MotuBrain HTML](https://arxiv.org/html/2604.27792v1)
- [RoboTwin 2.0](https://robotwin-platform.github.io/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b695e188-434c-40a0-945f-59ad980e4d39",
  "isSidechain": true,
  "agentId": "ac914d0c5e87d0846",
  "requestId": "req_011Caudc3mpZb3hYwRT1NRJE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b84c0d20-fc6b-43d1-94bc-036b6479ae49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "48cccba2-55eb-4ef3-800d-053af1c2ef58",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpqCwUzwa5i8kdbW8gLiDJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 15096,
      "output_tokens": 1521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1521,
          "cache_read_input_tokens": 15096,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 944,
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
