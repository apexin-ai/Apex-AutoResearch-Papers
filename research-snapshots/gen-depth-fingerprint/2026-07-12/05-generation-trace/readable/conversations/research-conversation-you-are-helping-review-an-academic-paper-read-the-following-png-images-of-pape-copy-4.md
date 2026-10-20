# Research conversation: You are helping review an academic paper. Read the following PNG images of paper pages and provide a DETAILED transcript

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a80a64196744bbcb9.jsonl`
- **Structured JSON:** [`18f6490389d582bf8230.json`](../../sessions/18/18f6490389d582bf8230.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-17T11:03:33.043Z_

You are helping review an academic paper. Read the following PNG images of paper pages and provide a DETAILED transcription/summary of all content. Focus especially on:
- Title, authors (if visible), abstract
- Introduction: main claims, contributions listed
- Method section: all technical details, equations, feature definitions
- Any tables or figures with their exact numbers and captions

Read these image files:
1. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p1.png
2. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p2.png
3. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p3.png
4. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p4.png

Report EVERYTHING you see - all text, all numbers, all technical details. Do not summarize - give me the full content. This is for a peer review and I need every detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "a80a64196744bbcb9",
  "type": "user",
  "uuid": "e95722bc-b45c-4ac3-81aa-b9a9fb9b54ef",
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

_source line 2 · 2026-05-17T11:03:33.047Z_

```json
{
  "parentUuid": "e95722bc-b45c-4ac3-81aa-b9a9fb9b54ef",
  "isSidechain": true,
  "agentId": "a80a64196744bbcb9",
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
  "uuid": "a709d133-9ee4-4c3d-8593-bf53b9ed8d1c",
  "timestamp": "2026-05-17T11:03:33.047Z",
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

_source line 3 · 2026-05-17T11:03:36.078Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GQqhSt7wjTiHYqmEETTB8j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a709d133-9ee4-4c3d-8593-bf53b9ed8d1c",
  "isSidechain": true,
  "agentId": "a80a64196744bbcb9",
  "requestId": "req_011Cb82fUhaJB5Nq2aUgfcLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39346641-018e-4d78-8c51-c432a4b405dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzfQG8r2dHuX2eBKmh9rvN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19020,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19020,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 4 · 2026-05-17T11:03:36.552Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TycramFvhZpyGvnDRNddAe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39346641-018e-4d78-8c51-c432a4b405dd",
  "isSidechain": true,
  "agentId": "a80a64196744bbcb9",
  "requestId": "req_011Cb82fUhaJB5Nq2aUgfcLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75cfc8cf-4b6f-45f4-bf1d-39707e8b0384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzfQG8r2dHuX2eBKmh9rvN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19020,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19020,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 5 · 2026-05-17T11:03:36.657Z_

<details><summary>↩ Tool result · `toolu_01GQqhSt7wjTiHYqmEETTB8j`</summary>

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
  "parentUuid": "39346641-018e-4d78-8c51-c432a4b405dd",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "a80a64196744bbcb9",
  "type": "user",
  "uuid": "51f3d354-7ab6-40a9-92c5-7a54cb7fbea8",
  "sourceToolAssistantUUID": "39346641-018e-4d78-8c51-c432a4b405dd",
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

_source line 6 · 2026-05-17T11:03:37.181Z_

<details><summary>↩ Tool result · `toolu_01TycramFvhZpyGvnDRNddAe`</summary>

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
  "parentUuid": "75cfc8cf-4b6f-45f4-bf1d-39707e8b0384",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "a80a64196744bbcb9",
  "type": "user",
  "uuid": "bb2f43aa-0a16-48fc-81d8-8d3f406613f4",
  "sourceToolAssistantUUID": "75cfc8cf-4b6f-45f4-bf1d-39707e8b0384",
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

### Tool call

_source line 7 · 2026-05-17T11:03:37.495Z_

<details open><summary>🔧 Tool call — Read · `toolu_015gJYA6LUy6s9LgzwzwLGzg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb2f43aa-0a16-48fc-81d8-8d3f406613f4",
  "isSidechain": true,
  "agentId": "a80a64196744bbcb9",
  "requestId": "req_011Cb82fUhaJB5Nq2aUgfcLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6dc072da-dc0b-453c-a332-e7cf243b22bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzfQG8r2dHuX2eBKmh9rvN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19020,
      "cache_read_input_tokens": 0,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19020,
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

_source line 8 · 2026-05-17T11:03:37.826Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T35YW4M8DAqn8nJkyxsgyQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dc072da-dc0b-453c-a332-e7cf243b22bd",
  "isSidechain": true,
  "agentId": "a80a64196744bbcb9",
  "requestId": "req_011Cb82fUhaJB5Nq2aUgfcLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38bd9be4-46ab-40de-bb80-9e5a2a3bff5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzfQG8r2dHuX2eBKmh9rvN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19020,
      "cache_read_input_tokens": 0,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19020,
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

_source line 9 · 2026-05-17T11:03:40.144Z_

<details><summary>↩ Tool result · `toolu_015gJYA6LUy6s9LgzwzwLGzg`</summary>

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
  "parentUuid": "6dc072da-dc0b-453c-a332-e7cf243b22bd",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "a80a64196744bbcb9",
  "type": "user",
  "uuid": "e618dc81-6973-4b02-b0a3-a8eeb6958cd2",
  "sourceToolAssistantUUID": "6dc072da-dc0b-453c-a332-e7cf243b22bd",
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

_source line 10 · 2026-05-17T11:03:40.928Z_

<details><summary>↩ Tool result · `toolu_01T35YW4M8DAqn8nJkyxsgyQ`</summary>

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
  "parentUuid": "38bd9be4-46ab-40de-bb80-9e5a2a3bff5f",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "a80a64196744bbcb9",
  "type": "user",
  "uuid": "d47e5a37-e92a-4423-9a9f-43099b345e12",
  "sourceToolAssistantUUID": "38bd9be4-46ab-40de-bb80-9e5a2a3bff5f",
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

_source line 11 · 2026-05-17T11:05:47.648Z_



Here is a detailed transcription of all four pages:

---

## PAGE 1

### Title
**Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains**

### Authors
**Anonymous ACL submission**

### Abstract

When LLM-generated text re-enters the web and seeds further generation, the resulting recursive chains exhibit progressively altered distributional properties, complicating provenance tracking and quality-aware data curation. We ask whether this drift is structured enough to estimate how many generative steps a text undergoes, framing this as *ordinal depth estimation* (classifying text as gen-0/gen-1/gen-2+ rather than binary real-vs.-synthetic). Studying eight base models from five families, we identify a *differential depth response*: central-tendency features (mean entropy, lexical diversity) drift monotonically with generation depth, while shape features (entropy max, vocabulary tail slope) remain near-stationary. This pattern is consistent with a location shift in the token-level NLL distribution that preserves distributional shape. Exploiting this complementarity, a 7-feature ensemble achieves 3-class macro F1 = 0.809 on heterogeneous cross-model chains and F1 = 0.762 under leave-one-generator-out evaluation across eight generators, significantly outperforming individual detectors baselines (p < 0.001). We further show that this structured drift does not translate into training-utility: depth-aware data curation offers no improvement over random subsampling at equal sample count.

### 1 Introduction

Web-crawled corpora increasingly contain LLM-generated text (estimates suggest that 7-17% of recent scientific papers and peer reviews contain substantial LLM-modified content (Liang et al., 2024a), and this proportion grows as generated text re-enters the web and seeds subsequent generation. The result is recursive generation chains whose outputs progressively diverge from human-written text. Understanding how distributional features evolve across generation depths is a prerequisite for characterizing text provenance, yet existing detectors (Bao et al., 2024; Hans et al., 2024; Narayamanan et al., 2026; Mitchell et al., 2023) provide only binary real-vs-synthetic decisions, conflating qualitatively different material: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.

We formalize ordinal depth estimation, classifying text by generational depth (gen-0 or gen-1 or gen-2+) rather than a binary label, and refer to the overall framework as *depth fingerprinting*. No existing method addresses this task in non-paraphrastic continuation chains.

The key finding is a *differential depth response* (DDR): when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.8B-8B parameters) transform text across recursive depths, central-tendency and diversity features (reference-model mean entropy, type-token ratio, hapax ratio) drift monotonically, while shape features (entropy max, tail decay) remain near-stationary. This pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution while preserving its shape: the softmax architecture and fixed sampling parameters constrain distributional shape regardless of input, while each successive generation compresses the location toward the model's preferred output distribution. We restrict to base (pretrained) models as a deliberate design choice, since instruction-tuning introduces confounds (length regulation, format constraints, safety-driven shaping) that obscure this intrinsic mechanism; preliminary experiments confirm substantially degraded depth signal under instruction tuning (§5).

The combination of drifting and stationary features yields a 7-feature ensemble that achieves 3-class macro F1 = 0.809 on heterogeneous cross-model chains and F1 = 0.762 under leave-one-

---

## PAGE 2

generator-out evaluation (binary F1 = 0.764 on cross-model chains), significantly outperforming individual detection baselines (p < 0.001). The signal is prompt-type dependent: continuation chains show stronger drift than elaboration or rewriting (§5).

**Our contributions are:**

1. **Task formulation.** We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for characterizing how distributional properties evolve across recursive generation.

2. **Empirical characterization.** We document differential depth response across eight generators from five families and show that a 7-feature ensemble exploiting this structure significantly outperforms all individual detection baselines (p < 0.001).

3. **Negative transfer to curation.** Despite the structured nature of depth-related distributional changes, depth-aware data curation does not improve downstream language model quality over random subsampling (Penedo et al., 2024; Soldaini et al., 2024).

### 2 Related Work

#### 2.1 AI-Generated Text Detection

Methods for distinguishing human-written from machine-generated text have evolved from statistical tests (Gehrmann et al., 2019; Zellers et al., 2019; Solaiman et al., 2019) to zero-shot reference-model approaches (Mitchell et al., 2023; Bao et al., 2024; Hans et al., 2024; Yang et al., 2024) and learned classifiers (Mady et al., 2026; Sadasivan et al., 2025; Narayamanan et al., 2026). Recent work pursues diverse signals including intrinsic dimensionality (Tulchinskii et al., 2023), surprisal diversity (Basani and Chen, 2026), and distributional gap measures (Pu et al., 2026; see Wu et al. (2025) and Jawahar et al. (2020) for surveys. A persistent limitation is that these methods produce binary (real vs. synthetic) decisions. Recent multi-class extensions (role recognition in human-LLM collaboration (Cheng et al., 2025), multi-generator attribution (Wang et al., 2024)) discriminate among different *sources* rather than recursive generation depth. Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table 4), because each captures a single distributional property that generalizes inconsistently (Krishna et al., 2023; Chakraborty et al., 2024). Our contribution is not a new detection method but the task formulation (ordinal depth estimation) and the finding that combining drifting and stationary features yields consistent cross-generator performance. This is orthogonal to source attribution (Uchendu et al., 2020; Munir et al., 2021), which identifies *which* model generated text; our LOGO evaluation decouples generator identity from depth.

#### 2.2 Model Collapse and Iterative Generation

Self-consuming generative models progressively lose distributional coverage (Alemohammad et al., 2024), and model collapse is inevitable without fresh human data (Shumailov et al., 2024), though careful data mining can mitigate this (Gerstgrasser et al., 2024; Dohmatob et al., 2025). These studies focus on *training-loop degradation*; our setting studies *inference chains*, where a fixed model generates text conditioned on its own prior output without retraining.

Two concurrent works are most directly relevant. Mohamed et al. (2025) analyze paraphrasing and translation chains, showing progressive information loss. Geng et al. (2026) demonstrate that semantic-preservation constraints induce attractor dynamics bounding distinguishable depth to approximately three classes. We differ in studying non-paraphrastic continuation chains, where the absence of semantic anchoring permits richer depth signal, and in focusing on estimating depth rather than characterizing convergence.

#### 2.3 Lexical Diversity and Stationarity

Declining lexical diversity in LLM-generated text is documented in both training (Guo et al., 2024a) and deployment (Padmakumar and He, 2023) settings. Our surface features (TTR and hapax ratio) are classical stylometric measures (Stamatatos, 2009; Koppel et al., 2009) that we apply to inference chains, showing monotonic diversity decline across depths without model retraining. We push beyond generator identity (Uchendu et al., 2020) to the depth dimension, and show that diversity declines monotonically even under top-p sampling (Holtzman et al., 2020).

#### 2.4 Data Quality and Provenance

Scalable data curation relies on quality signals (Xie et al., 2023; Wettig et al., 2024; Wenzek

---

## PAGE 3

et al., 2020); generation depth is a complementary provenance signal characterizing *how many steps removed* text is from a human source. Proactive watermarking (Kirchenbauer et al., 2023; Dathathri et al., 2024; Aaronson and Kirchner, 2022) embeds identifiable patterns, but watermark strength decays across multi-step chains (Arora et al., 2026), motivating passive-post-hoc methods like ours. At the feature level, our NLL analysis connects to Shi et al. (2024), who use the probability tail for membership inference; we analyze the full NLL distribution for ordinal depth estimation.

### 3 Method

#### 3.1 Task Formulation

Given a text *x*, the goal is to predict its *generation depth* d ∈ {0, 1, 2+}, where d=0 denotes human-written text, d=1 denotes first-generation LLM output conditioned on human text, and d≥2 denotes text produced by recursively conditioning an LLM on its own prior output at least twice. Formally, let C₀ be a reference corpus of human-written text. A generation chain of depth *k* is defined recursively: x⁰ ~ C₀, and x⁽ⁱ⁾ = G(x⁽ⁱ⁻¹⁾) for k ≥ 1, where G denotes stochastic LLM generation conditioned on its input. We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization. Depths beyond 2 are merged into a single 2+ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (§4.2).

#### 3.2 Generation Chain Construction

We construct generation chains using eight generators spanning five model families: Pythia (2.8B, 1B) (Biderman et al., 2023), OLMo (OLMo-2-1B) (Groeneveld et al., 2024), Qwen (Qwen1.5-7B, Qwen2.5-0.6B, Qwen3-8B-Base) (Qwen Team, 2025), Llama (Llama-3.2-3B) (Grattafiori et al., 2024), and Mistral (Mistral-7B-v0.3) (Jiang et al., 2023). This selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.

For each generator, we sample approximately 1,000 seed passages from English Wikipedia as C₀. The same pool of seed passages serves as gen-0 for all generators. We use shared seeds across generators to ensure that cross-generator comparisons control for input content, isolating the effect of the generation model from source text variation. In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train-test overlap for the gen-0 class. We address this with a supplementary binary evaluation excluding gen-0 entirely (§4.3). Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt "Continue the following text:\n\n{text}". All generation uses temperature τ=0.7, nucleus sampling with p=0.9, and maximum length of 256 new tokens. The theoretical yield is 8 × 1,000 × 5 = 40,000 texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 37,058 texts remain (Appendix A). For classification, depths 2-4 are collapsed into the 2+ class.

#### 3.3 Feature Extraction

The seven features are motivated by two complementary views of distributional drift. *Reference-model features* capture how the text's token-level surprise distribution shifts relative to a fixed model; *surface features* capture how lexical diversity contracts under recursive generation. Together, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes). This two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (§4.2).

We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.

**Reference-model features.** A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL)¹ for each text. Although Pythia-410M shares the GPT-NeoX architecture with two of the eight generators, cross-family reference model experiments (§4.2) confirm that depth features are not reference-specific (LOGO F1 varies by <0.013 across Pythia, OLMo, and Qwen references). From the resulting NLL sequence, we extract five statistics:

---

## PAGE 4

- **entropy mean**: mean token-level NLL, capturing the average predictability of the text under the reference model;
- **entropy std**: standard deviation of token-level NLL, measuring the spread of per-token surprise;
- **entropy max**: maximum token-level NLL, capturing the most surprising token;
- **entropy min**: minimum token-level NLL, capturing the most predictable token. As generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs. Although entropy min shows near-zero marginal impact in leave-one-feature-out analysis (ΔF1 = +0.01 pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance.
- **tail decay**: slope of the vocabulary-level averaged log-probability distribution in the mid-tail region (ranks 100-1000). For each text, we compute the mean log-probability of each vocabulary token across all positions under the reference model, sort tokens in descending order of mean log-probability, and fit a linear regression to ranks 100-1000. The slope captures how steeply the reference model's probability mass decays beyond high-probability tokens, characterizing the shape of the distribution tail.

**Surface features.** Two features capture lexical diversity without requiring a reference model:
- **TTR**: type-token ratio (number of unique word types divided by total tokens);
- **hapax ratio**: proportion of words appearing exactly once (hapax legomena).

**Feature complementarity.** The grouping reflects an empirical pattern we term *differential depth response*: central-tendency and diversity features (entropy mean, TTR, hapax ratio) show strong monotonic drift with generation depth (|ρ| = 0.60-0.63); entropy min and entropy std show moderate drift (|ρ| = 0.17-0.41); and shape features (entropy max, tail decay) remain near-stationary (|ρ| < 0.07). This differential behavior, consistent with recursive generation shifting the location of the NLL distribution while preserving distributional shape, motivates combining both feature types. As shown in §4, the full 7-feature set significantly outperforms either group alone.

---

¹ We use "entropy" as shorthand for token-level negative log-likelihood under the reference model, following convention in prior detection work. These are point-wise NLL values, not Shannon entropy of the full distribution.

---

#### 3.4 Evaluation Protocol

**Cross-validation.** To evaluate generalization to unseen generators, we use **Leave-One-Generator-Out (LOGO)** cross-validation: in each fold, one of the eight generators is held out for testing and the remaining seven provide training data. We additionally report **Leave-One-Family-Out (LOFO)** results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.

**Classifier.** We use XGBoost (Chen and Guestrin, 2016) as the classifier throughout. Gradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability. We use n_estimators=200, max_depth=6, and learning rate 0.1 for the 7-feature ensemble. All other settings in Table 4 (individual and multi-detector ensembles) use n_estimators=100 and max_depth=3 to avoid overfitting. LOGO F1 is stable across random seeds (std < 0.001 over 5 seeds), confirming that results are not sensitive to classifier initialization. Alternative classifiers (random forest, logistic regression) yield comparable performance (Appendix H), confirming that discriminative power resides in the features, not the classifier. We evaluated two ordinal-specific methods (CORAL (Cao et al., 2020), Frank-Hall ordinal ensemble (Frank and Hall, 2001)); neither significantly outperforms multiclass classification (CIs overlapping; §4), confirming that with only three ordinal levels, ordinal structure provides limited practical benefit.

**Metrics and statistical testing.** The primary metric is **macro-averaged F1** over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically larger gen-0 class. We report per-class F1 scores and 95% confidence intervals via percentile bootstrap (n=1,000), resampling at the document level within each held-out fold. For pairwise model comparisons (e.g., full features vs. ablated subsets), we use the **McNemar test** on disagreement tables. For comparisons against detection baselines, we use **paired bootstrap** significance tests. All reported p-values are two-sided. We report

---

That completes the detailed transcription of all four pages. Key elements:

- **Title**: "Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains"
- **Venue**: Anonymous ACL submission
- **Core concept**: Ordinal depth estimation (gen-0/gen-1/gen-2+ classification) using 7 features split into reference-model features (entropy mean/std/max/min, tail decay) and surface features (TTR, hapax ratio)
- **Key finding**: Differential Depth Response (DDR) -- central-tendency features drift monotonically while shape features remain stationary
- **Main result**: 3-class macro F1 = 0.809 cross-model, F1 = 0.762 LOGO
- **8 generators from 5 families**: Pythia (2.8B, 1B), OLMo (OLMo-2-1B), Qwen (Qwen1.5-7B, Qwen2.5-0.6B, Qwen3-8B-Base), Llama (Llama-3.2-3B), Mistral (Mistral-7B-v0.3)
- **Reference model**: Pythia-410M
- **Evaluation**: LOGO and LOFO cross-validation, XGBoost classifier, McNemar test and paired bootstrap for significance
- **3 contributions**: task formulation, empirical characterization with DDR, negative transfer to curation finding

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d47e5a37-e92a-4423-9a9f-43099b345e12",
  "isSidechain": true,
  "agentId": "a80a64196744bbcb9",
  "requestId": "req_011Cb82g4M8krcmkn6N5G74a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a7cb51a-67be-4139-890a-46ab0b3d3b1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wq7hSB3aou7pykFtdYghGB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 19020,
      "output_tokens": 4801,
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
          "output_tokens": 4801,
          "cache_read_input_tokens": 19020,
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
