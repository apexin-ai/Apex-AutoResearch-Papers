# Research conversation: Read the following PNG images of a research paper and extract ALL text content verbatim (especially section titles, clai

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a20d3ac2b2042555e.jsonl`
- **Structured JSON:** [`ee300d1c25b5f013632b.json`](../../sessions/ee/ee300d1c25b5f013632b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-16T19:32:14.185Z_

Read the following PNG images of a research paper and extract ALL text content verbatim (especially section titles, claims, equations, and table/figure captions). Focus on: title, abstract, introduction, and beginning of methodology.

Read these files in order:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png

For each page, report:
- All section/subsection headings
- Key claims and qualifications (especially in abstract/intro - look for words like "preliminary", "initial", "limited")
- Any mention of cross-scale generalization, LoRA rank, feature importance, multicollinearity, VIF
- Table/figure content if present
- Footnotes

Return the FULL extracted text, preserving structure. Do not summarize.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a20d3ac2b2042555e",
  "type": "user",
  "uuid": "6c36a741-191f-42e9-a8a5-22554ad21e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T19:32:14.189Z_

```json
{
  "parentUuid": "6c36a741-191f-42e9-a8a5-22554ad21e43",
  "isSidechain": true,
  "agentId": "a20d3ac2b2042555e",
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
  "uuid": "6e369564-a6c6-49da-9872-64ff54fbca78",
  "timestamp": "2026-05-16T19:32:14.189Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T19:32:17.375Z_

<details open><summary>🔧 Tool call — Read · `toolu_016RWUKBjcRWnctPcpdec45o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e369564-a6c6-49da-9872-64ff54fbca78",
  "isSidechain": true,
  "agentId": "a20d3ac2b2042555e",
  "requestId": "req_011Cb6oeQTnJKF2EGmVFCg7X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5a755fa-bcd0-419a-a856-c247d83c4f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014bXsbhihX9ENSpKQJz4E3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16904,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16904,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 4 · 2026-05-16T19:32:17.837Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YBinNEDniY7MT3bLHf19aN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5a755fa-bcd0-419a-a856-c247d83c4f7c",
  "isSidechain": true,
  "agentId": "a20d3ac2b2042555e",
  "requestId": "req_011Cb6oeQTnJKF2EGmVFCg7X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80456928-8859-4f0e-8f2a-76974d703ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014bXsbhihX9ENSpKQJz4E3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16904,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16904,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 5 · 2026-05-16T19:32:18.117Z_

<details><summary>↩ Tool result · `toolu_016RWUKBjcRWnctPcpdec45o`</summary>

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
  "parentUuid": "d5a755fa-bcd0-419a-a856-c247d83c4f7c",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a20d3ac2b2042555e",
  "type": "user",
  "uuid": "3aae2077-3f6d-43c8-b178-f47536fee85c",
  "sourceToolAssistantUUID": "d5a755fa-bcd0-419a-a856-c247d83c4f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T19:32:18.775Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KR6adhRgM1H5sZC6rt2MP9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aae2077-3f6d-43c8-b178-f47536fee85c",
  "isSidechain": true,
  "agentId": "a20d3ac2b2042555e",
  "requestId": "req_011Cb6oeQTnJKF2EGmVFCg7X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "451806cc-b352-44a3-ba14-372df9e702f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014bXsbhihX9ENSpKQJz4E3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16904,
      "cache_read_input_tokens": 0,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16904,
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

_source line 7 · 2026-05-16T19:32:18.796Z_

<details><summary>↩ Tool result · `toolu_01YBinNEDniY7MT3bLHf19aN`</summary>

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
  "parentUuid": "80456928-8859-4f0e-8f2a-76974d703ea3",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a20d3ac2b2042555e",
  "type": "user",
  "uuid": "b8ab2d3c-8130-4176-b96f-b6776c7d000b",
  "sourceToolAssistantUUID": "80456928-8859-4f0e-8f2a-76974d703ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T19:32:19.125Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KF56YKtFbsHbT8TUaxTyeQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8ab2d3c-8130-4176-b96f-b6776c7d000b",
  "isSidechain": true,
  "agentId": "a20d3ac2b2042555e",
  "requestId": "req_011Cb6oeQTnJKF2EGmVFCg7X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18aefc91-c616-4467-9bb2-fa1e11638b2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014bXsbhihX9ENSpKQJz4E3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16904,
      "cache_read_input_tokens": 0,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16904,
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

_source line 9 · 2026-05-16T19:32:20.900Z_

<details><summary>↩ Tool result · `toolu_01KR6adhRgM1H5sZC6rt2MP9`</summary>

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
  "parentUuid": "451806cc-b352-44a3-ba14-372df9e702f1",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a20d3ac2b2042555e",
  "type": "user",
  "uuid": "a9cee899-c296-42b9-985c-a29b610d1081",
  "sourceToolAssistantUUID": "451806cc-b352-44a3-ba14-372df9e702f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T19:32:21.028Z_

<details><summary>↩ Tool result · `toolu_01KF56YKtFbsHbT8TUaxTyeQ`</summary>

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
  "parentUuid": "18aefc91-c616-4467-9bb2-fa1e11638b2e",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a20d3ac2b2042555e",
  "type": "user",
  "uuid": "d885fa45-f459-4037-afc0-1fe77a607e78",
  "sourceToolAssistantUUID": "18aefc91-c616-4467-9bb2-fa1e11638b2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-16T19:34:39.508Z_



## Page 1 — Full Extracted Text

---

**Title:** How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints

**Authors:** Anonymous ACL submission

---

### Abstract

As large language models increasingly train on web text containing their own outputs, a recursive model→data→model loop arises— yet no method estimates how many such iterations a text has undergone. We formalize recursive generation depth estimation as an ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths. From each passage we extract a compact statistical fingerprint—19 candidate features dominated by perplexity tail statistics, with the top 5 achieving 97.6% of full-set performance—compared against a fixed reference model (Pythia-1.4B). A Random Forest classifier achieves 70.8% four-class accuracy (chance = 25%; 58.8–82.6% when excluding the most perfectly separable d0 class), a zero-shot LLM baseline reaches only 36.2%, with 90th-percentile perplexity and surprisal variance emerging as consistent depth markers across the studied 3 × 3 grid (key 3 importance in 9/9 and 8/9 cells, respectively). Our Depth Degradation Atlas reveals that decoding strategy reshapes degradation trajectories more than merely attenuating them, and we define the *Effective Discriminable Depth* (EDD&lt;sub>T&lt;/sub>=1 for extended recursive finding, EDD&lt;sub>T&lt;/sub>=1 for extended recursive chains. Cross-model transfer reaches 66.4% and cross-strategy transfer 59.1%; temperature sampling induces a d0↔2 AUC inversion that we decompose into a *perceptual* scale component and a residual structural component. Cross-model recursive chains—where each depth is generated by a different architecture— achieve 84.75%, and extending to two 7B-scale generators yields 70.2% accuracy with monotonic AUC decay (EDD=4), while a second 7B architecture exhibits EDD≥5 with a non-monotonic trajectory possibly linked to instruction-tuning effects. Applied to WikiText-103/C4/C4 passages, all three model-specific classifiers achieve ≥98.5% d0 accuracy despite ≤62.1% domain shift in mean perplexity; on

C4 web-crawl text, false positive rates range from 4.7% to 22.4%, concentrated in template content.

---

### 1 Introduction

The text on which large language models are trained increasingly contains their own outputs. As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data (Shumailov et al., 2024; Alemohammad et al., 2024). This model→data→model cycle is no longer hypothetical—it is already occurring in the wild—yet we lack the ability to determine how many iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality (Dohmatob et al., 2024b).

Existing tools address but distinct problems. Binary detectors such as Binoculars (Hans et al., 2024), Fast-DetectGPT (Bao et al., 2024), and DwEye (Rasan and Chen, 2026) classify text as human-written or machine-generated, collapsing all depths d ≥ 1 into a single category. Watermarking (Kirchenbauer et al., 2023) requires proactive embedding and cannot be applied retroactively. The model collapse literature (Shumailov et al., 2024; Dohmatob et al., 2024b) assumes depth is known a priori; Dey et al. (2025) filter synthetic data via binary detection without distinguishing depths. No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.

Our key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are **universal and scale-variant** across the three model families and three decoding strategies studied. Speci-

---

## Page 2 — Full Extracted Text

---

cally, perplexity tail statistics—the 90th-percentile perplexity (P90_PPL) and surprisal variance (VAR_SURPRISAL)—emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 8/9 model-strategy configurations, respectively. Surprisingly, in one of two 7B models the AUC trajectory becomes non-monotonic, suggesting that instruction tuning after degradation dynamics rather than scale alone driving a qualitative shift.

We formalize recursive generation depth estimation as an ordinal classification task and introduce a lightweight pipeline to solve it. Given a text passage, we compute a feature vector from reference-model perplexity statistics—19 candidates capturing distributional location, spread, tail behavior, and lexical diversity, though high multicollinearity concentrates the signal in 4–5 effective dimensions (§4.2)—and classify it with a Random Forest into one of K + 1 depth classes (d=0 for human text through d = K for K-th generation text). To systematically characterize how recursive generation reshapes these features, we construct the *Depth Degradation Atlas*, a 3 × 3 grid of model families (Pythia-1.4B, OLMo-1B, GPT-2 XL) and decoding strategies (nucleus p = 0.95, temperature r = 0.6, top-k = 50), spanning 4 generation depths, totaling 180K samples. This atlas reveals strategy-dependent degradation trajectories—temperature sampling accelerates convergence toward a low-entropy attractor, while top-k attenuates the depth signal—and we introduce the *Effective Discriminable Depth* (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.

Our contributions are:

- **Task formalization and benchmark.** We define recursive generation depth estimation as ordinal classification, introduce the EDD metric, and construct a 180K-sample benchmark spanning 3 model families × 3 decoding strategies × 4 depths.

- **Depth Degradation Atlas.** A systematic 3 × 3 characterization reveals that P90_PPL and VAR_SURPRISAL are universal depth markers (top 2 in 9/9 and 8/9 cells), decoding strategy reshapes degradation trajectories qualitatively, and depth discrimination persists through EDD&lt;sub>T=4&lt;/sub> = 4 recursive steps.

- **Generalization across seven axes (four**

**in main text; three in appendix).** We demonstrate robustness beyond the training grid: cross-model recursive chains (84.75%— depth signal accumulates across heterogeneous model boundaries), cross-scale to two 7B architectures (70.2% and 60.1%, with divergent AUC trajectories), cross-domain transfer to arXiv (74.1%); temperature robustness τ ∈ {0.5, 0.9}, and reference model independence (Δ~3 pp). End-to-end transformers achieve only ~59% (~9pp below feature-based), confirming that perplexity tail features encode signal inaccessible to standard PLM representations.

---

### 2 Related Work

**Model Collapse Theory.** Shumailov et al. (2024) demonstrate that recursive training on model output erodes distributional tails; Dohmatob et al. (2024b) formalize tail narrowing vs. outage, with extensions to collapse (Dohmatob et al., 2025) and the regression case (Dohmatob et al., 2024a); the MAD framework (Alemohammad et al., 2024) quantifies precision-recall tradeoffs in self-consuming models. Mitigation includes data retention (Gerstgrasser et al., 2024), detection-based filtering (Drayson et al., 2025), and curated pipelines (Falafah et al., 2026); recent work further identifies non-monotone dynamics (Kazhe and Chakrabarty, 2026), fixed-point convergence (Marchi et al., 2024), contamination bounds (Wang et al., 2026), knowledge collapse (Krubia et al., 2025), special signatures (Gu et al., 2026), and self-improving loops (Schaffeder and Gatt, 2026). These works characterize degradation but assume depth is known; we address the inverse problem.

**AI Text Detection.** The detection literature (Wu et al., 2025) spans statistical methods—DetectGPT (Mitchell et al., 2023), Fast-DetectGPT (Bao et al., 2024), Binoculars (Hans et al., 2024), DwEye (Rasan and Chen, 2026), GLTR (Gehrmann et al., 2019)—model-based classifiers (Verma et al., 2024; Yang et al., 2024; Wang et al., 2024a), and watermarking (Kirchenbauer et al., 2023). Fundamental limits exist: paraphrasing reduces detection to near chance (Sadasivan et al., 2023), detection degrades under distribution shift (Palanoid et al., 2026), and a generator barrier bounds performance (Pu et al., 2026). All perform binary classification; our approach outputs ordinal depth labels.

---

## Page 3 — Full Extracted Text

---

**Adjacent Tasks.** Adjacent work addresses related but distinct problems: EditLens (Thai et al., 2026) estimates editing extent, Uchendo et al. (2020) classify which model generated text, LORI (Ye et al., 2025) benchmarks multimodal detection, and Mohamed et al. (2025) measure forward degradation in iterative generation; none estimates recursive depth. CORAL (Cao et al., 2020) and CLOE (Pitswalei et al., 2025) provide ordinal classification frameworks we adopt as baselines (§5).

**Decoding Strategy Effects.** Decoding strategies shape text statistics in ways relevant to depth: nucleus sampling maintains diversity (Holtzman et al., 2020), strategy effects are model-dependent (Garcia Assis et al., 2025; Wiher et al., 2022), parameters affect evaluation non-trivially (Pillutla et al., 2024), and Mirostat (Basu et al., 2021) dynamically regulates perplexity. Our atlas (§4) reveals these strategies induce qualitatively different degradation trajectories under recursive generation.

---

### 3 Method

#### 3.1 Problem Definition

Let f&lt;sub>θ&lt;/sub> denote a language model and D&lt;sub>0&lt;/sub> a corpus of human-written seed text. We define a recursive generation chain of depth k as the sequence D&lt;sub>0&lt;/sub>, D&lt;sub>1&lt;/sub>, ..., D&lt;sub>k&lt;/sub>, where each D&lt;sub>i&lt;/sub> (i ≥ 1) is produced by finetuning f&lt;sub>θ&lt;/sub> on D&lt;sub>i−1&lt;/sub> and sampling from the resulting model. Depth d=0 denotes human-written text; depth d=i (i ≥ 1) denotes text generated by a model trained on depth-(i − 1) data.

Given a text passage, the task is to estimate its recursive generation depth d ∈ {0, 1, ..., K}. This is an ordinal classification problem: depths carry a natural ordering, and d+1 is structurally closer to d+0 than d+3 is, since each generation step compounds distributional shift.

#### 3.2 Multi-Generational Benchmark Construction

We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.

**Model families.** We select three 1–1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2 XL (OpenAI, 1.5B). Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.

**Decoding strategies.** Each model is paired with three decoding strategies: nucleus sampling (p=0.95) (Holtzman et al., 2020), temperature sampling (τ=0.6), and top-k sampling (k=50). These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles. Our findings are limited to this grid; transfer to unested models, scales, or strategies is not established.

**Depth and scale.** The primary benchmark covers depths d0–d3 across all 3 × 3 = 9 model-strategy cells, with 5,000 samples per depth per cell (180K samples total). For depth extension experiments (§4), we extend one pipeline (Pythia-1.4B, nucleus) to d0–d5.

**Generation pipeline.** Starting from a Wikipedia subset as D&lt;sub>0&lt;/sub> (~50K articles), each generation cycle: (1) LoRA finetuning (He et al., 2022) on D&lt;sub>i−1&lt;/sub> (r=16, α=32, lr 2·10⁻⁵, 1 epoch, c-8 additional parameters); (2) sampling 5,000 passages (max 512 tokens, BOS-seeded, no prompt conditioning) under the prescribed decoding strategy; (3) feeds the next cycle. Each depth is produced by a model trained on prior-depth data, with no per-passage lineage across depths, ensuring cross-validation splits do not introduce leakage.

**Reference model.** All features (§3.3) are computed using a fixed reference model (Pythia-1.4B). For Pythia this constitutes self-model measurement; for OLMo and GPT-2 XL, cross-model. Self-model measurement confers no advantage; generalization to alternative references is in §5.

#### 3.3 Statistical Feature Construction

We extract a feature vector F(x) comprising 19 candidate features from the reference-model perplexity distribution over each passage x; ablation (§4.2) shows the top 5 achieve 97.6% of full-set performance, and variance inflation analysis reveals VIF>10 for 14–16 features, placing the effective independent dimensionality at 4–5. The features fall into four categories (Table 1):

*Perplexity statistics* (9 features) capture the per-token perplexity distribution via moments and quantiles (p10, p25, p90); tail quantiles prove especially informative as recursive finetuning erodes the high-perplexity tail (§4). *Surprisal statistics* (3): mean, variance, and entropy of − log p(token); surprisal

---

## Page 4 — Full Extracted Text

---

**Table 1:** The 19 statistical features comprising F(x), grouped by category. All perplexity and surprisal features are computed from the reference model (Pythia-1.4B).

| Category | Features | n |
|----------|----------|---|
| Perplexity | mean, var, skewness, kurtosis, statistics p10, p25, p50, p75, p90 | 9 |
| Surprisal | mean, var, entropy | 3 |
| Lexical | type-token ratio, hapax ratio, bigram entropy, trigram entropy | 4 |
| Repetition | repeated 2/3/4-gram fractions | 3 |

variance captures second-order structure not redundant with perplexity moments. *Lexical diversity* (4): type-token ratio, hapax ratio, bigram/trigram entropy. *Repetition* (3): repeated n-gram fractions for n ∈ {2, 3, 4}.

#### 3.4 Effective Discriminable Depth

Aggregate multi-class accuracy obscures whether discriminability degrades at specific depth boundaries. We introduce the *Effective Discriminable Depth* (EDD) to formalize the frontier beyond which adjacent depths become statistically indistinguishable.

**Pairwise discriminability.** For each adjacent pair (d, d+1), the pairwise discriminability AUC(d, d+1) is the ROC AUC of a dedicated binary Random Forest (500 trees, |√19| features/split, 5-fold stratified CV) trained on class-balanced data from F(x) to distinguish depth d from depth-(d+1) samples. Each pair uses an independent classifier, avoiding decision boundary dilution (§4.3).

**Definition 1** (Effective Discriminable Depth). The *Effective Discriminable Depth* at threshold T is:

EDD&lt;sub>T&lt;/sub> = max{d* : ∀ d ∈ {0,...,d*}, AUC(d, d+1) ≥ T}

where d* ∈ {0, ..., K−1}. If AUC(0,1) < T, then EDD&lt;sub>T&lt;/sub> = 0.

EDD&lt;sub>T&lt;/sub> is the deepest depth such that every adjacent pair remains discriminable at level T — the longest contiguous discriminable prefix¹. We set T = 0.75 as default; sensitivity at T ∈ {0.65, 0.70, 0.75, 0.80, 0.85} is reported in §4.

¹Empirically monotonic (§4); for non-monotonic profiles, this is conservative (Limitation).

---

**Table 2:** Four-class RF accuracy (%) across the 3 × 3 atlas, with d1→d3 three-class accuracy in parentheses (chance = 25% / 33%). Depth-0 recall exceeds 98% in all cells.

| | Nucleus | Temp τ=0.6 | Top-k |
|---|---|---|---|
| Pythia-1.4B | 78.2 (71.2) | 76.3 (70.6) | 69.6 (58.8) |
| OLMo-1B | 78.8 (73.0) | 82.0 (76.3) | 74.2 (66.1) |
| GPT-2 XL | 83.5 (79.6) | 85.4 (82.6) | 76.6 (69.5) |

**Classifiers.** Our primary classifier is a Random Forest (200 trees, 5-fold stratified CV); comparisons with CORAL (Cao et al., 2020), DwEye (Rasan and Chen, 2026), and other baselines in §5.

---

### 4 The Depth Degradation Atlas

The Depth Degradation Atlas maps how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies: 3 × 3 = 9 model-strategy cells at depths d ∈ {0, 1, 2, 3}, with extensions to d=5 for EDD validation (§4.3).

#### 4.1 In-Distribution Performance

Table 2 reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells. Accuracy ranges from 69.6% (Pythia, top-k) to 85.4% (GPT-2 XL, temperature), all exceeding the 25% chance baseline. GPT-2 XL achieves the highest accuracy under every strategy (76.6–85.4%), followed by OLMo (74.2–82.0%) and Pythia (69.6–78.2%). top-k yields the lowest in every model. The mean within-model strategy gap (4.4 pp) is comparable to the within-strategy model gap (7.1 pp)—decoding strategy and model family contribute roughly equally to performance variation.

Depth-0 recall exceeds 98% in all 9 cells; among generated depths, d2 consistently yields the lowest recall (46–73%), reflecting overlap with both adjacent classes (full per-class recall in Appendix A.3).

#### 4.2 Feature Consistency Across the Grid

Despite the 15.8 pp accuracy spread, a small feature family dominates universally. P90_PPL ranks top-2 by Gini importance in all 9 cells; VAR_SURPRISAL ranks in 8/9 under SHAP (79 Gini; full per-cell rankings in Table 16, Appendix A.15). Cross-model Spearman correlation averages ρ = 0.868; models agree on which features carry depth information. Feature ablation confirms concentration: top-2 features alone reach 91.1%

---

### Key observations across all 4 pages:

**Regarding qualifications/hedging language:**
- "Our findings are limited to this grid; transfer to untested models, scales, or strategies is not established." (p3)
- "Empirically monotonic (§4); for non-monotonic profiles, this is conservative (Limitation)." (footnote, p4)

**Regarding cross-scale generalization:**
- Abstract mentions "cross-scale to two 7B architectures (70.2% and 60.1%, with divergent AUC trajectories)" 
- Introduction mentions fingerprints are "universal and scale-variant"

**Regarding LoRA rank:**
- Page 3: "LoRA finetuning (He et al., 2022) on D_{i-1} (r=16, α=32, lr 2·10⁻⁵, 1 epoch, c-8 additional parameters)"

**Regarding feature importance and multicollinearity/VIF:**
- Page 2: "high multicollinearity concentrates the signal in 4–5 effective dimensions (§4.2)"
- Page 3: "variance inflation analysis reveals VIF>10 for 14–16 features, placing the effective independent dimensionality at 4–5"
- Page 4: "P90_PPL ranks top-2 by Gini importance in all 9 cells; VAR_SURPRISAL ranks in 8/9"
- Page 4: "top-2 features alone reach 91.1%" (of full-set performance)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d885fa45-f459-4037-afc0-1fe77a607e78",
  "isSidechain": true,
  "agentId": "a20d3ac2b2042555e",
  "requestId": "req_011Cb6oeukfBQK6ofyH7YKqC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da8b9793-b5f8-4382-9d0d-a728c2929c24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCKnvdtqY1ahgzpgvvpcMa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 16904,
      "output_tokens": 5420,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5420,
          "cache_read_input_tokens": 16904,
          "cache_creation_input_tokens": 2711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2711,
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
