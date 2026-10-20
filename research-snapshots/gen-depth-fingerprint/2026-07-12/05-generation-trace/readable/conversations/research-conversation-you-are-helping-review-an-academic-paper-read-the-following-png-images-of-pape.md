# Research conversation: You are helping review an academic paper. Read the following PNG images of paper pages and provide a DETAILED transcript

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa6e5a24eaf133e5d.jsonl`
- **Structured JSON:** [`e4b654d2e0e9b858fbf6.json`](../../sessions/e4/e4b654d2e0e9b858fbf6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-17T11:03:37.446Z_

You are helping review an academic paper. Read the following PNG images of paper pages and provide a DETAILED transcription/summary of all content. Focus especially on:
- Experimental results: all tables with exact numbers, statistical tests, p-values
- Discussion, limitations, conclusion sections
- Any figures with descriptions
- Ethics statement, limitations section
- References section (list key references)

Read these image files:
1. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p5.png
2. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p6.png
3. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p7.png
4. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p8.png

Report EVERYTHING you see - all text, all numbers, all technical details. Do not summarize - give me the full content. This is for a peer review and I need every detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "aa6e5a24eaf133e5d",
  "type": "user",
  "uuid": "4803752f-3d34-4a5b-9208-47a67e1c71b8",
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

_source line 2 · 2026-05-17T11:03:37.448Z_

```json
{
  "parentUuid": "4803752f-3d34-4a5b-9208-47a67e1c71b8",
  "isSidechain": true,
  "agentId": "aa6e5a24eaf133e5d",
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
  "uuid": "7723bf31-2ec3-4cee-a77d-6415652932f7",
  "timestamp": "2026-05-17T11:03:37.448Z",
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

_source line 3 · 2026-05-17T11:03:40.158Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KjKtWsx85szRGhWfMiNPWW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7723bf31-2ec3-4cee-a77d-6415652932f7",
  "isSidechain": true,
  "agentId": "aa6e5a24eaf133e5d",
  "requestId": "req_011Cb82foadXpUjdDjQV2U7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "225b7716-8078-41af-a664-b4ae2be1dcf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqNgmZ5aLYmF1ZYpUvCzpx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9879,
      "cache_read_input_tokens": 9144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9879,
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

_source line 4 · 2026-05-17T11:03:40.937Z_

<details open><summary>🔧 Tool call — Read · `toolu_015zPjjzDJKn18bn5UUGFagi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "225b7716-8078-41af-a664-b4ae2be1dcf0",
  "isSidechain": true,
  "agentId": "aa6e5a24eaf133e5d",
  "requestId": "req_011Cb82foadXpUjdDjQV2U7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89bb667a-cb11-4fd3-8d34-df134a3e3c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqNgmZ5aLYmF1ZYpUvCzpx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9879,
      "cache_read_input_tokens": 9144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9879,
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

_source line 5 · 2026-05-17T11:03:41.613Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RMsPDs8pHtnYxFiktHPgsw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89bb667a-cb11-4fd3-8d34-df134a3e3c44",
  "isSidechain": true,
  "agentId": "aa6e5a24eaf133e5d",
  "requestId": "req_011Cb82foadXpUjdDjQV2U7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7227f784-98cd-42cf-a499-7ff2c3cc5e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqNgmZ5aLYmF1ZYpUvCzpx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9879,
      "cache_read_input_tokens": 9144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9879,
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

_source line 6 · 2026-05-17T11:03:42.637Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WjtW49cr8SRo8sftqZjG1Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7227f784-98cd-42cf-a499-7ff2c3cc5e43",
  "isSidechain": true,
  "agentId": "aa6e5a24eaf133e5d",
  "requestId": "req_011Cb82foadXpUjdDjQV2U7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2aadb6fe-2ddd-4e5b-b219-a46a1c2d720c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqNgmZ5aLYmF1ZYpUvCzpx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9879,
      "cache_read_input_tokens": 9144,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9879
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 9144,
          "cache_creation_input_tokens": 9879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9879,
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

_source line 7 · 2026-05-17T11:03:45.986Z_

<details><summary>↩ Tool result · `toolu_01KjKtWsx85szRGhWfMiNPWW`</summary>

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
  "parentUuid": "225b7716-8078-41af-a664-b4ae2be1dcf0",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "aa6e5a24eaf133e5d",
  "type": "user",
  "uuid": "991dcac6-26a7-41cd-b26f-d2dca26c894e",
  "sourceToolAssistantUUID": "225b7716-8078-41af-a664-b4ae2be1dcf0",
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

_source line 8 · 2026-05-17T11:03:46.645Z_

<details><summary>↩ Tool result · `toolu_015zPjjzDJKn18bn5UUGFagi`</summary>

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
  "parentUuid": "89bb667a-cb11-4fd3-8d34-df134a3e3c44",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "aa6e5a24eaf133e5d",
  "type": "user",
  "uuid": "0c8b605a-3896-4273-8b1a-ac6c84dd111e",
  "sourceToolAssistantUUID": "89bb667a-cb11-4fd3-8d34-df134a3e3c44",
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

_source line 9 · 2026-05-17T11:03:48.344Z_

<details><summary>↩ Tool result · `toolu_01RMsPDs8pHtnYxFiktHPgsw`</summary>

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
  "parentUuid": "7227f784-98cd-42cf-a499-7ff2c3cc5e43",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "aa6e5a24eaf133e5d",
  "type": "user",
  "uuid": "f76ba9d5-3ad5-41c4-9126-a0ffe7dc5169",
  "sourceToolAssistantUUID": "7227f784-98cd-42cf-a499-7ff2c3cc5e43",
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

_source line 10 · 2026-05-17T11:03:49.619Z_

<details><summary>↩ Tool result · `toolu_01WjtW49cr8SRo8sftqZjG1Y`</summary>

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
  "parentUuid": "2aadb6fe-2ddd-4e5b-b219-a46a1c2d720c",
  "isSidechain": true,
  "promptId": "288b1cfa-6daa-455f-ac86-c14bbcb627e5",
  "agentId": "aa6e5a24eaf133e5d",
  "type": "user",
  "uuid": "4646a0d0-b200-4980-a658-f393ccb3b165",
  "sourceToolAssistantUUID": "2aadb6fe-2ddd-4e5b-b219-a46a1c2d720c",
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

_source line 11 · 2026-05-17T11:06:17.713Z_



Here is the complete detailed transcription of all content from pages 5-8 of the paper:

---

## PAGE 5

### (Continuation from previous section, top of page)

four pairwise comparisons (ensemble vs. each individual baseline) in §4.3; applying Bonferroni correction (α_adj = 0.05/4 = 0.0125), all remain significant at p < 0.001. Feature-depth correlations (§4.2) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.

**Baselines.** We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT (Bao et al., 2024), Binoculars (Hans et al., 2024), and LLI-Score (Narayanaswamy et al., 2026). Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.

**Length confound control.** Since TTR and hapax_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation. We conduct three complementary analyses: (1) length-depth correlation to verify absence of systematic length variation, (2) length-feature correlation to identify features with moderate length dependence, and (3) classification on length-matched subsets that equalize length distributions across depth classes (§4.1).

## 4 Results

### 4.1 Depth Classification Performance

The 7-feature ensemble achieves 5-class LOGO F1 = 0.762 (95% CI [0.758, 0.766], N = 37,058) across eight generators from five families (Table 1). Because gen-0 seeds are shared across generators (§3.2), we also report a task-free binary metric (gen-1 vs. gen-2+) F1 = 0.694, CI [0.688, 0.700]. Per-generator binary F1 ranges from 0.653 (Mistral-7B) to 0.724 (Pythia-2.8B); the primary difficulty is distinguishing gen-1 from gen-2+ (Appendix G). Larger generators show moderate degradation (Qwen1.5-8B: 0.692, Mistral-7B: 0.653) relative to the 0.694 average.

**Cross-model generalization.** Cross-model chains (randomly selected generator per step) yield binary F1 = 0.764 under 5-fold CV,² confirming that depth signal persists when text passes

²Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen). Llama and Mistral were added later for single-generator evaluation.

through heterogeneous generators. Leave-one-family-out (LOFO) evaluation yields average binary F1 = 0.686 (Δ = -0.8 pp vs. LOGO), confirming transfer across architectural families under the strictest unseen-generator test. Appendix D further demonstrates that the signal generalizes across text domains (News, Academic, Code; binary F1 > 0.75).

**Length confound control.** Length-matched subsampling yields binary F1 = 0.724 (vs. 0.770 unmatched; Δ = 0.046); a random-subsample control at equal N (F1 = 0.767) confirms the drop reflects deconfounding, not sample-size reduction. Length accounts for ≈6% of discriminative performance (Appendix B).

**Table 1:** 5-generator LOGO bias-F1 for the 7-feature ensemble (bootstrap 95% CIs, n = 1000). Binary F1 (gen-1 vs. gen-2+) is the primary metric. 3-class includes the shared gen-0 class (§3.2).

| Model | Family | 3-class | 3-of-11 | Bin F1 | 95% CI |
|-------|--------|---------|---------|--------|--------|
| Pythia-2.8B | Pythia | 2.08 | 0.706 | 0.724 | [.700, .742] |
| Pythia-1.4B | Pythia | 1.76 | 0.673 | 0.705 | [.680, .726] |
| OLMo-1.7B | OLMo | 1.68 | 0.675 | 0.706 | [.680, .730] |
| Qwen1.5-0.5B | Qwen | 0.96 | 0.655 | 0.680 | [.654, .705] |
| OLMo-2-1B | OLMo | 0.84 | 0.679 | 0.693 | [.670, .715] |
| Qwen1.5-8B | Qwen | 0.76 | 0.641 | 0.692 | [.665, .719] |
| Llama-3.2-3B | Llama | 0.84 | 0.635 | 0.681 | [.656, .711] |
| Mistral-7B | Mistral | 7.08 | 0.632 | 0.653 | [.617, .686] |
| **Average (5-gen LOGO)** | | **0.762** | **0.694** | | [.681, .705] |

---

## PAGE 6

### (Figure 1 - left side of page)

**Figure 1:** Differential depth response. Spearman correlations between individual features and generation depth. Central-tendency and diversity features (hapax ratio, TTR, entropy mean) show strong monotonic drift, while shape features (entropy std, tail decay) remain near-stationarity.

[The figure shows scatter/strip plots with features on x-axis (Hapax TTR, ρ, H_max, H_sd, Tail Deci, γ_δ) and Spearman ρ values on y-axis. Different colored markers for Pythia-7B, Pythia-1.4B, OLMo-2-1B, Qwen1.5-0.5B, Qwen1.5-8B]

**Table 2:** Cross-family reference model validation (5-gen LOGO subset). Drift direction is consistent (negative) across all three references; magnitude varies with capacity. Spread in LOGO F1 is 0.013.

| Reference | Family | Params | LOGO F1 | Est. DvR |
|-----------|--------|--------|---------|----------|
| Pythia-410M | Pythia | 410M | 0.801 | -1.18, -1.44 |
| OLMo-2-1B | OLMo | 1B | 0.807 | ... [-.091] |
| Qwen1.5-0.5B | Qwen | 0.68 | 0.816 | -0.10, -1.39 |

ically outperforms surface-only (F1 = 0.688) and reference-only (F1 = 0.713; McNemar p ≤ 0; Table 3). Reference-only features yield higher binary F1 (0.833 vs. 0.695 for the full ensemble) because surface lexical features introduce noise at the gen-1/gen-2+ boundary. However, surface features are essential for 5-class classification, where they improve gen-0 discrimination by capturing vocabulary diversity patterns absent in reference-model entropy statistics (Full 5-class F1 = 0.773 vs. Reference-only: 0.713). Permutation importance: hapax ratio (0.35); entropy mean (0.23), TTR (0.18). Leave-one-feature-out confirms 6 of 7 features contribute positively (Appendix F).

**Cross-family reference models.** Alternative references (OLMo-2-1B, Qwen1.5-0.5B) achieve comparable LOGO F1 (spread 0.013; Table 2), with consistently negative entropy drift, confirming that DDR is a property of recursive generation.

### 4.3 Comparison with Detection Baselines

Can existing detection methods, designed for binary classification, also discriminate generation depth? We repurpose four detection scores as or-

**Table 3:** Feature ablation results

| Feature set | F1 | Top feature (imp.) |
|-------------|----|--------------------|
| Full (7 features) | 0.773 | hapax_ratio (0.35) |
| Surface only (2) | 0.688 | hapax_ratio (0.41) |
| Reference only (5) | 0.713 | entropy_mean (0.27) |

Table 3: Feature ablation (8-gen, 10-fold stratified CV, 3-class). Full > surface (+8.5pp) and Full > reference (+6.0pp) confirms complementarity.

### (Figure 2 - right side)

**Figure 2:** LOGO binary F1 with 95% bootstrap CIs. Per-generator variance is higher for single detectors than for the ensemble.

[Bar chart showing F1 scores for different methods: Avg LogProb, FastDetectGPT, Binoculars, LLI-Score across different models (Pythia-7B, Pythia-1.4B, OLMo-2-1B, Qwen1.5-0.5B, Qwen1.5-8B)]

dinal depth predictors using the same XGBoost framework and identical LOGO splits (Table 4, Figure 2).

The 7-feature ensemble (binary F1 = 0.701) outperforms all individual baselines (best: LD-Score 0.676; CIs non-overlapping). Multi-detector ensembles (4det-surface, 0.707) achieve the highest binary F1 by combining four GPT-detection scores; our single-reference approach (410M parameters) achieves statistically indistinguishable binary performance (±0.6pp) with overlapping CIs.

If depth fingerprinting reliably identifies recursive text, can it improve data curation? Fine-tuning OLMo-2-0425-1B on five data variants (3 seeds each) shows that data quality dominates depth composition: random subsampling (ppl = 2.367, 95% CI [2.367, 2.367]) outperforms depth-stratified selection (ppl = 2.387, 95% CI [2.387, 2.388]) at equal sample extent, Δ = 0.020, p = 0.25 by paired permutation test (n = 3 seeds; minimum achievable p for this sample size). Cross-seed variation is below 0.001 for all variants, so the ranking is stable but the text is underpowered (Appendix L). Depth composition per se does not determine training utility.

## 5 Discussion

**Why does shape remain stationary?** The softmax architecture and sampling hyperparameters

---

## PAGE 7

**Table 4:** Depth classification (8-gen pooled LOGO). Evaluated on N = 34,131 samples for which all detector scores are available; class-balanced downsampling is applied within each LOGO fold. The 7-feature ensemble uses a 7-class LOGO schema.

| Method | Feat. | 3-of F1 | Bin F1 |
|--------|-------|---------|--------|
| 4 det. + surface | 6 | **0.792** | **0.707** |
| 7-feature ensemble | 7 | 0.776 | 0.701 |
| 4-detector ens. | 4 | 0.754 | 0.698 |
| LLI-Score | 1 | 0.633 | 0.676 |
| Avg LogProb | 1 | 0.707 | 0.674 |
| FastDetectGPT | 1 | 0.604 | 0.576 |
| Binoculars | 1 | 0.411 | 0.534 |

The slight difference from Table 1 (5 = 37,058, full dataset) reflects the reduced sample

that determine distributional shape are fixed across depths. Recursive generation shifts context toward high-probability regions, reducing entropy mean, but does not alter the generation mechanism itself. This account predicts stationarity until the model reaches its fixed-point distribution, a regime not observed at chain length ≤4. Sampling ablation provides a natural-test: depth signal is robust when sampling noise is low (t ∈ {0.5, 0.7}, ≤0.3pp degradation) but degrades at t = 1.0 (−6pp; Appendix H), where sampling randomness overpowers the systematic location shift.

**Prompt-type dependence.** Continuation chains yield the strongest signal (F1 = 0.781 vs. 0.730 for elaboration), with cross-type transfer at 0.753 (Appendix C). Semantic-preserving constraints attenuate drift, consistent with Mohamed et al. (2025): the more a task anchors the output distribution to the input, the less room recursive drift has to accumulate.

**Practical applicability.** At the document level, gen-1 per-class F1 = 0.63 (37% misclassification) is insufficient for automated filtering but sufficient for corpus-level flagging, where error scales as O(1/√n) and aggregate depth composition estimates become reliable. Error analysis (Appendix K) confirms that misclassification concentrates in shallow gen-2+ samples where drift has not yet accumulated, consistent with DDR predictions.

**Relation to model collapse.** Model collapse (Shumailov et al., 2024; Dohmatob et al., 2025) describes degradation when models are retrained on their own outputs. Our inference-chain drift oc-

curs without parameter updates, potentially representing an early, reversible stage of the same distributional narrowing. Topic drift accounts for <9% of feature variance (R² = 0.082), confirming it mediates rather than confounds depth signal.

**Granularity and robustness.** Three classes represent the practical resolution ceiling: 5-class LOGO F1 drops to ≈0.50, with depths 2-4 mutually indistinguishable (Appendix D). That said, QLoRA fine-tuning recovers 3-class F1 = 0.905 (Appendix E), confirming that richer signal exists beyond the seven summary statistics. Under text perturbation, LLM-simulated sentence regeneration (50% edit distance) causes comparable degradation to 5% random word replacement (Appendix I), confirming that depth signal resides in generative structure rather than surface token statistics.

**Instruction tuning.** Instruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1 = 0.538 vs. 0.764 base). Length regulation and format constraints imposed by alignment compress the distributional variation that depth fingerprinting exploits, justifying our restriction to base models as the appropriate setting for isolating the phenomenon.

## 6 Conclusion

We introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (3-class F1 = 0.809 on cross-model chains, 0.762 under LOGO). The finding that generative data curation provides no downstream benefit despite structured distributional change suggests that the drift captured by depth fingerprinting is orthogonal to the text properties that determine training utility.

Two boundaries define the scope of these results. First, instruction tuning compresses the distributional variation that fingerprinting exploits; extending to aligned models requires disentangling format-induced and depth-induced drift. Second, while the signal generalizes across generators up to 8B parameters, frontier-scale models (70B+) with higher fluency may further compress

---

## PAGE 8

feature margins. All code, data, and trained models will be released upon publication.

## Limitations

All eight generators are base (pretrained) models. This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift. However, web text is predominantly produced by instruction-tuned and RLHF-aligned models. Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1 = 0.538 (vs. 0.764 base) and Qwen1.5-0.5B with chat template to 0.667 (vs. 0.838 under a 7-generator split). Length-matched analysis yields near-zero correlations (|ρ| < 0.02) and binary classification near chance (F1 ≈ 0.5) for Qwen models, leaving interpretation ambiguous. Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.

Our experiments include generators up to 8.2B parameters (Qwen1.5-8B). Depth signal persists at this scale (Qwen1.5-8B 3-class F1 = 0.714), but cross-scale transfer incurs a moderate gap vs. ≤2.8B generators (F1 = 0.773 (0.831)). Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.

Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1 = 0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrase chains (binary F1 = 0.617 vs. 0.749 for continuation). DDR is most reliably detected in continuation-style generation, near-paraphrastic settings approach the method's detection floor. Cross-prompt-type transfer (LOFO F1 = 0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator × cross-prompt interactions remain untested.

Our primary evaluation uses single-generator chains; cross-model chains (§4.1) confirm depth signal under generator heterogeneity (3-class F1 = 0.809, binary F1 = 0.764), though the eight generators represent a controlled laboratory setting rather than the full diversity of real-world contamination. Simulated human editing (§5) sug-

gests graceful degradation, but the gap between simulated token replacement and real-world post-processing remains untested.

The reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (§4.2) confirm the phenomenon is not reference-specific (spread 0.013 across three references). All seed texts in the main evaluation are English Wikipedia excerpts. Cross-domain evaluation (Appendix J) shows that depth signal persists across News, Academic, and Code domains (binary F1 = 0.73 under LOGO at t = 1.0), though a domain × temperature interaction exists: certain domain/temperature combinations at lower temperature approach chance level (e.g., Academic domain binary F1 = 0.628 at t = 0.7), suggesting that reference model calibration is critical for cross-domain deployment. Generalization to other languages remains untested.

Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus p = 0.9). A sampling ablation (Appendix H) shows robustness to moderate variation (t ∈ {0.5, 0.7}, <0.3pp) but substantial degradation at t = 1.0 (−6pp), indicating that depth fingerprinting has reduced accuracy in high-temperature decoding regimes.

We use 3-class granularity (gen-0/gen-1/gen-2+). A 5-class evaluation (Appendix D) yields LOGO F1 ≈ 0.50, with depths 2-4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.

## Ethics Statement

All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved. Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author. Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal. We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing). We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.

---

**Key quantitative findings summary across these pages:**

- **Main result:** 7-feature ensemble achieves 5-class LOGO F1 = 0.762 (95% CI [0.758, 0.766]), binary F1 = 0.694 [0.681, 0.705]
- **Cross-model chains:** binary F1 = 0.764 (5-fold CV)
- **LOFO evaluation:** binary F1 = 0.686 (Δ = -0.8pp vs LOGO)
- **Length confound:** matched F1 = 0.724 vs unmatched 0.770 (Δ = 0.046); length accounts for ~6% of discriminative performance
- **Feature ablation:** Full (7 feat) F1 = 0.773; Surface only F1 = 0.688; Reference only F1 = 0.713
- **Best baseline comparison:** 4-det + surface F1 = 0.707 (bin), 7-feature ensemble F1 = 0.701 (bin); LLI-Score best single = 0.676
- **Data curation experiment:** Random subsampling ppl = 2.367 outperforms depth-stratified ppl = 2.387, Δ = 0.020, p = 0.25 (underpowered)
- **QLoRA fine-tuning:** recovers 3-class F1 = 0.905
- **Instruct models:** OLMo-Instruct LOGO F1 = 0.538 vs 0.764 base
- **Sampling ablation:** robust at t ∈ {0.5, 0.7} (<0.3pp degradation), degrades at t = 1.0 (−6pp)
- **Cross-domain:** binary F1 = 0.73 under LOGO at t = 1.0; Academic domain F1 = 0.628 at t = 0.7
- **Prompt-type:** continuation F1 = 0.781, elaboration 0.730, rewriting 0.737, paraphrase binary F1 = 0.617 vs 0.749
- **Cross-prompt-type transfer LOFO F1 = 0.753**
- **Topic drift:** accounts for <9% of feature variance (R² = 0.082)
- **5-class granularity:** drops to F1 ≈ 0.50, depths 2-4 indistinguishable
- **Cross-family reference model spread:** 0.013 in LOGO F1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4646a0d0-b200-4980-a658-f393ccb3b165",
  "isSidechain": true,
  "agentId": "aa6e5a24eaf133e5d",
  "requestId": "req_011Cb82gj8m4KT996BLEtCHP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bceb5457-5dbe-4260-a980-7e9a6a271469",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "3828f685-a19b-490c-b390-5f05fad289be",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXC8GTNMQnpvVWRJVwdXQa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 19023,
      "output_tokens": 5725,
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
          "output_tokens": 5725,
          "cache_read_input_tokens": 19023,
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
