# Research conversation: Read the following PNG images of a research paper and extract ALL text content verbatim. These are likely appendix/suppl

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5e0dff94de397c54.jsonl`
- **Structured JSON:** [`6f5789836e3745a40caa.json`](../../sessions/6f/6f5789836e3745a40caa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-16T19:32:30.933Z_

Read the following PNG images of a research paper and extract ALL text content verbatim. These are likely appendix/supplementary pages. Focus on:
- LoRA rank sensitivity analysis (rank 4, 16, 64 experiments)
- VIF analysis / multicollinearity discussion
- Feature importance concordance (Kendall's W)
- Any additional ablation results
- Cross-architecture reference model experiments
- Any additional tables/figures

Read these files in order:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png

Return the FULL extracted text, preserving structure. Do not summarize.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a5e0dff94de397c54",
  "type": "user",
  "uuid": "327f5c4c-0ab4-40fc-99b0-bb310334719a",
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

_source line 2 · 2026-05-16T19:32:30.936Z_

```json
{
  "parentUuid": "327f5c4c-0ab4-40fc-99b0-bb310334719a",
  "isSidechain": true,
  "agentId": "a5e0dff94de397c54",
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
  "uuid": "5310b814-e6b6-4b90-abf2-e4ef50427e9f",
  "timestamp": "2026-05-16T19:32:30.936Z",
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

_source line 3 · 2026-05-16T19:32:33.841Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JC7dFWFBZ1GcqPAs4p8xD5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5310b814-e6b6-4b90-abf2-e4ef50427e9f",
  "isSidechain": true,
  "agentId": "a5e0dff94de397c54",
  "requestId": "req_011Cb6ofe7M8ShSe9FuJc3tR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51743927-babf-4375-b612-68762e021bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URzzBcfXzu8sDSCF9zKXEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8608,
      "cache_read_input_tokens": 8265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8608,
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

_source line 4 · 2026-05-16T19:32:34.358Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SCm4R2gdFT89uTdza8A8s5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51743927-babf-4375-b612-68762e021bba",
  "isSidechain": true,
  "agentId": "a5e0dff94de397c54",
  "requestId": "req_011Cb6ofe7M8ShSe9FuJc3tR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c95ede4b-9a85-4e64-8281-d72f907b75d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URzzBcfXzu8sDSCF9zKXEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8608,
      "cache_read_input_tokens": 8265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8608,
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

_source line 5 · 2026-05-16T19:32:34.486Z_

<details><summary>↩ Tool result · `toolu_01JC7dFWFBZ1GcqPAs4p8xD5`</summary>

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
  "parentUuid": "51743927-babf-4375-b612-68762e021bba",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a5e0dff94de397c54",
  "type": "user",
  "uuid": "375fe33d-f5a3-4a1b-8146-c0e9dcc0f56e",
  "sourceToolAssistantUUID": "51743927-babf-4375-b612-68762e021bba",
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

_source line 6 · 2026-05-16T19:32:35.031Z_

<details><summary>↩ Tool result · `toolu_01SCm4R2gdFT89uTdza8A8s5`</summary>

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
  "parentUuid": "c95ede4b-9a85-4e64-8281-d72f907b75d8",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a5e0dff94de397c54",
  "type": "user",
  "uuid": "39524a4c-6829-43db-8602-9cc304bccb17",
  "sourceToolAssistantUUID": "c95ede4b-9a85-4e64-8281-d72f907b75d8",
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

_source line 7 · 2026-05-16T19:32:35.252Z_

<details open><summary>🔧 Tool call — Read · `toolu_013va7VECAFXJHL6LTjE11dg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39524a4c-6829-43db-8602-9cc304bccb17",
  "isSidechain": true,
  "agentId": "a5e0dff94de397c54",
  "requestId": "req_011Cb6ofe7M8ShSe9FuJc3tR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17ac4ac0-dec1-43d0-92e1-a9ebbf2a4b06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URzzBcfXzu8sDSCF9zKXEU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8608,
      "cache_read_input_tokens": 8265,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8608
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 8265,
          "cache_creation_input_tokens": 8608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8608,
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

_source line 8 · 2026-05-16T19:32:35.443Z_

<details open><summary>🔧 Tool call — Read · `toolu_014k9W7aLYRexjGtwgEneW7u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17ac4ac0-dec1-43d0-92e1-a9ebbf2a4b06",
  "isSidechain": true,
  "agentId": "a5e0dff94de397c54",
  "requestId": "req_011Cb6ofe7M8ShSe9FuJc3tR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efd8a9a8-3228-40a1-be55-3e008e3f19c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URzzBcfXzu8sDSCF9zKXEU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8608,
      "cache_read_input_tokens": 8265,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8608
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 8265,
          "cache_creation_input_tokens": 8608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8608,
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

_source line 9 · 2026-05-16T19:32:35.464Z_

<details><summary>↩ Tool result · `toolu_014k9W7aLYRexjGtwgEneW7u`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efd8a9a8-3228-40a1-be55-3e008e3f19c8",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a5e0dff94de397c54",
  "type": "user",
  "uuid": "502392ab-33bb-4709-9f8c-6c48e23e5d99",
  "sourceToolAssistantUUID": "efd8a9a8-3228-40a1-be55-3e008e3f19c8",
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

_source line 10 · 2026-05-16T19:32:35.840Z_

<details><summary>↩ Tool result · `toolu_013va7VECAFXJHL6LTjE11dg`</summary>

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
  "parentUuid": "17ac4ac0-dec1-43d0-92e1-a9ebbf2a4b06",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a5e0dff94de397c54",
  "type": "user",
  "uuid": "1a69d288-ddd5-4194-940d-c88f34fad5d4",
  "sourceToolAssistantUUID": "17ac4ac0-dec1-43d0-92e1-a9ebbf2a4b06",
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

_source line 11 · 2026-05-16T19:34:40.555Z_



Here is the full extracted text from all four pages:

---

## Page 13

while RF achieves 0.596 d2 recall, a >2× advantage at the hardest depth class.

Table 11: Per-class performance for end-to-end PLM classifiers vs. RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall at depth class with the largest PLM–RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 distinctions despite adequate d0/d3.

| Model | d0 CV | d1 | d2 | d3 |
|-------|-------|----|----|----|
| DeBERTa-v3 | 58.3 ± 4.7 | .947 | .378 | .247 | .655 |
| RoBERTa-lg | 59.5 ± 2.2 | .938 | .416 | .261 | .647 |
| RF (11 feat) | | | | .596* |

*Recall; shown for the depth class with the largest PLM–RF gap.

**Feature space divergence.** SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 68.8% of RF's total contribution. Three independent importance measures—SHAP, Gini, and permutation—show strong concordance (Kendall's W = 0.90, p<0.005; pairwise Spearman ρ: SHAP–Gini 0.83, SHAP–permutation 0.81; see Table 16). Gini importance assigns p_82.4% with p_95.0 appearing in the SHAP top-2 in 9/9 cells and var_surprisal in 8/9.

Linear probing of PLM [CLS] representations yields negative Δr for both var_surprisal and p90_p10 (§A.7), indicating that pretrained representations lack the linear structure needed to recover perplexity tail statistics—a systematic representational gap rather than a bag-of-hyperparameters artifact.

ECOL (Plawiak et al., 2023) reached 64.5% (§A.4); all end-to-end approaches (58–65%) underperform feature-based methods, suggesting depth estimation benefits from targeted statistical features that capture distributional tail properties absent from PLM representations. This comparison is bounded by backbone scale (<125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.

**A.9 Domain Bias Analysis**

To assess whether the classifiers exploit depth-related features or stylistic/topic cues from individual seed articles, we conduct three sub-experiments.

**Methodological note.** An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0%, seed-group prediction 20.8%). We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments. The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.

**Sub-A: Standard CV.** Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59% to 82% across the 9 atlas cells (top-2 ≥ 5× above the 33.1% chance level), confirming that depth signal is the dominant classification factor.

**Sub-B: LOGO evaluation.** We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out (LOGO) evaluation. Mean accuracy is 72.1% (range 59.5–81.6%), matching standard CV (72.6%) within noise (before fix: standard CV (72.6%) within noise before fix: standard CV group confound). Per-fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is comparable, as in within-group classification (§4.3).

**Sub-C: Negative control.** We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10%). Depth prediction accuracy averages 72%+; seed-group prediction averages 10.2%—indistinguishable from chance (before fix: 20.8%), inflated by the depth-group confound. The depth-to-seed group accuracy ratio is 7.1:1, confirming that feature representation encodes depth but not seed-article identity.

Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.

**A.10 Wild-Data Calibration**

Table 12 reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (§4-6 editorial passages) and C4 (5,000 web-crawl passages).

---

## Page 14

Table 12: Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR is fraction misclassified as d1+.

| Model | Source | n | d0 (%) | FPR (%) |
|-------|--------|---|--------|---------|
| Pythia-1.4B | WikiText | 546 | 100.0 | 0.0 |
| | C4 | 5,000 | 70.8 | 29.2 |
| GPT-2 XL | WikiText | 546 | 99.3 | 0.7 |
| | C4 | 5,000 | 77.6 | 22.4 |
| OLMo-1B | WikiText | 546 | 98.5 | 1.5 |
| | C4 | 5,000 | 95.3 | 4.7 |

vs. correctly classified d0 passages), rather than in random noise. The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2 XL (trained primarily on Wikipedia/RedPajama) map template-heavy content into the d1+ region. Among C4 false positives for GPT-2 XL, predictions distribute as d1 (9.0%), d2 (3.7%), d3 (9.6%); for OLMo, d1 (2.9%), d2 (0.9%), d1 (3.1)3)—the non-uniform depth distribution in practice, suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.

**A.11 Downstream Curation PoC**

To validate that depth estimation translates to actionable data curation, we construct a proof-of-concept downstream evaluation. We fine-tune Pythia-410M with LoRA (r=16, α=32) for 3 epochs on 6 data conditions derived from the Pythia depth-stratification corpus, reporting each condition over 5 random seeds. Conditions vary the selection mechanism (RF-predicted depth, oracle depth, unfiltered) and sampling strategy (strict=25%, moderate=50%, soft threshold). Table 13 reports per-condition perplexity; Table 14 reports pairwise comparisons (paired t-test, 5 seeds).

Table 13: Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). Δ is signed so that positive values indicate lower (better) perplexity vs. unfiltered. *: p < 0.05 (paired t-test vs. unfiltered).

| Condition | PPL | σ | Δ | t | p |
|-----------|-----|---|---|---|---|
| rf_strict | 17.76 | 0.11 | +0.38* | 3.13 | 0.035 |
| rf_moderate | 17.89 | 0.09 | +0.25 | 2.03 | 0.112 |
| rf_soft | 18.03 | 0.10 | +0.11 | 1.04 | 0.358 |
| oracle_strict | 17.68 | 0.12 | +0.46* | 3.51 | 0.025 |
| oracle_soft | 17.84 | 0.08 | +0.30* | 2.88 | 0.045 |
| unfiltered | 18.14 | 0.13 | — | — | — |

Table 14: Pairwise comparisons (paired t-test, 5 seeds). *: p < 0.05; **: p < 0.01.

| Comparison | Δ PPL | t | p |
|------------|-------|---|---|
| rf_strict vs random_strict | 0.429 | −7.05 | 0.002* |
| rf_moderate vs random_moderate | 0.242 | −4.37 | 0.022* |
| rf_soft vs random_soft | 0.528 | −7.98 | 0.001** |
| rf_soft vs unfiltered | 0.114 | 1.04 | 0.358 |

**A.12 Reference Model Ablation**

Table 15: Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0–d3) using different reference models for feature extraction.

| Reference Model | Architecture | Accuracy (%) |
|-----------------|--------------|--------------|
| Pythia-1.4B (self) | GPT-NeoX | 78.6 ± 0.6 |
| OLMo-1B (cross) | OLMo | 74.5 ± 0.7 |

**A.13 Cross-Boundary Generalization**

The preceding experiments assume a single model family generates all recursive depths. In practice, recursive contamination may traverse model boundaries: arXiv text generated by model A is used to train model B, whose output trains model C. We probe whether the depth signal persists under two relaxations of the single-model assumption.

**Cross-model recursive chains.** We construct a heterogeneous chain: human text (d0) → Pythia-1.4B generates d1 → OLMo-1B finetuned on Pythia-d1 generates d2 → GPT-2 XL finetuned on OLMo-d2 generates d3. Each recursive step uses a different model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior. A 4-class Random Forest achieves 84.75% accuracy (95% CI 81.0, 88.25), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3). Pairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.91. These results suggest that distributional artifacts of recursive generation persist across model boundaries—providing preliminary evidence that the depth signal is a property of the recursive process itself rather than of any individual generator.

**Cross-domain transfer.** All prior experiments use WikiText-103 as the seed corpus. To test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus p=0.95, 500 samples per depth, d0–d3). Five-fold cross-validation yields 74.1% ± 2.0% accuracy,

---

## Page 15

compared to ~78% on the WikiText seed. Per-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66—with d2 remaining the most challenging class. The 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths. These results suggest that the depth signal is domain-independent, providing preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.

**A.14 Extended Discussion**

**Depth-graduated curation.** Current data curation operates on a binary human-vs-machine distinction (Xie et al., 2023; Weting et al., 2024). Recursive generation depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality. The 70–85% in-distribution accuracy and EDD₃≥3 suggest depth-graduated filtering is feasible within known model–strategy configurations, though the d1/d2 boundary inversion under some strategy transfer (§5.3) means reliable curation requires either known decoding strategy metadata or an upstream strategy-identification step; a small-scale PoC (Appendix A.11) shows RF-filtered subsets match unfiltered quality with 44% of the data; large-scale validation remains open. Importance weighting (Sugiyama et al., 2007) could further enable continuous depth-aware data selection rather than discrete thresholding.

**Toward a provenance toolkit.** Depth estimation complements existing provenance methods along orthogonal axes. Watermarking (Kirchenbauer et al., 2023) provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text. Source attribution (Uchendu et al., 2020) identifies the generating model but not the generation history. Depth estimation characterizes *iterative reuse* regardless of generator cooperation or identity. A layered provenance system combining these three signals—watermark presence, source model, and recursive generation depth—could support more nuanced data auditing than any single method.

**A.15 Feature Importance Rankings**

Table 16 reports the top-5 features by Gini importance for all 9 atlas cells. Figure 4 provides a heatmap view of all 19 features across the grid.

Table 16: Top-5 features by Gini importance. Bold: top-2; *italic*: top-2 in 8/9; var_surprisal 8/9 SHAP (7/9 model Gini).

| | Top-5 Feature (Gini importance, descending) |
|---|---|
| | 1st | 2nd | 3rd | 4th | 5th |
| Pythia-1.4B nuc | ppl | var_s | p90_p10 | max_s | ent_u |
| Pythia-1.4B top-k | ppl | var_s | p90_p10 | max_s | rep_4gram |
| Pythia-1.4B temp | ppl | var_s | max_s | p90_p10 | ent_u |
| GPT-2 XL nuc | ppl | var_s | p90_p10 | max_s | ent_u |
| GPT-2 XL top-k | ppl | var_s | p90_p10 | max_s | frac_lt5 |
| GPT-2 XL temp | ppl | var_s | max_s | p90_p10 | rep_4gram |
| OLMo-1B nuc | ppl | var_s | p90_p10 | ent_u | max_s |
| OLMo-1B top-k | ppl | var_s | max_s | ent_u | p90_p10 |
| OLMo-1B temp | ppl | var_s | max_s | p90_p10 | ent_u |

[Figure 4: Atlas feature importance heatmap. Rows: 19 features grouped by category (§3.3); columns: 9 model–strategy cells. Color intensity encodes RF Gini importance. The perplexity-tail and surprisal-variance blocks maintain high importance across all cells.]

**A.16 EDD Threshold Sensitivity**

Table 17 reports EDD₃ across the primary 9-cell benchmark (depths 0–3) at four threshold values.

Table 17: Number of atlas cells achieving EDD ≥ 3 at each threshold T, across 9 model–strategy cells (depths 0–3). The d2-vs-d3 boundary is the bottleneck; top-6 cells drop first.

| | T=0.45 | T=0.50 | T=0.55 | T=0.60 | T=0.65 | T=0.70 | T=0.75 | T=0.80 |
|---|---|---|---|---|---|---|---|---|
| Cells with EDD ≥ 3 | 8/9 | 8/9 | 8/9 | 8/9 | 5/9 | 5/9 | 5/9 | 5/9 |

**A.17 Cross-Scale AUC Profiles**

Table 18 reports the consecutive binary AUC for the two 7–8B models.

---

## Page 16

Table 18: Consecutive binary AUC for 7–8B models (nucleus p=0.95). Llama-3.1-8B exhibits monotonic decay (d4v5 drops below T=0.70); Qwen2.5-7B shows a non-monotonic (U-shaped) pattern with all pairs above T.

| Model | d0v1 | d1v2 | d2v3 | d3v4 | d4v5 |
|-------|------|------|------|------|------|
| Llama-3.1-8B | 0.949 | 0.877 | 0.771 | 0.716 | 0.618 |
| Qwen2.5-7B | 0.969 | 0.729 | 0.709 | 0.732 | 0.772 |

---

That is the complete verbatim extraction of all four appendix pages (13–16). Key content includes:

- **Feature importance concordance** (p.13): Kendall's W = 0.90, p<0.005; pairwise Spearman ρ (SHAP–Gini 0.83, SHAP–permutation 0.81). Table 16 (p.15) gives full top-5 Gini importance rankings across all 9 atlas cells, with `ppl` and `var_surprisal` dominating.
- **LoRA downstream PoC** (p.14, Tables 13–14): Pythia-410M LoRA r=16, α=32, 3 epochs, 6 conditions, 5 seeds. rf_strict achieves PPL 17.76 (Δ=+0.38, p=0.035).
- **Reference model ablation** (p.14, Table 15): Self-reference (Pythia-1.4B) 78.6% vs cross-architecture (OLMo-1B) 74.5%.
- **Cross-boundary generalization** (p.14): Heterogeneous chain achieves 84.75% 4-class accuracy. Cross-domain (arXiv seed) yields 74.1% ± 2.0%.
- **Wild-data calibration** (p.14, Table 12): OLMo-1B FPR on C4 only 4.7% vs Pythia 29.2%.
- **EDD threshold sensitivity** (p.15, Table 17): 8/9 cells achieve EDD≥3 at T=0.55; drops to 5/9 at T=0.65.
- **Cross-scale AUC** (p.16, Table 18): Llama-3.1-8B monotonic decay (0.949→0.618); Qwen2.5-7B U-shaped (0.969→0.772).
- **No explicit VIF/multicollinearity table or LoRA rank sensitivity (r=4/16/64) ablation** found in these pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a69d288-ddd5-4194-940d-c88f34fad5d4",
  "isSidechain": true,
  "agentId": "a5e0dff94de397c54",
  "requestId": "req_011Cb6og14fsNVv8S5tMCqMX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "582bd451-24bc-48d0-a952-c0f62b225c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KQqyAFWsseeBzQgxS35gq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3910,
      "cache_read_input_tokens": 16873,
      "output_tokens": 5058,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5058,
          "cache_read_input_tokens": 16873,
          "cache_creation_input_tokens": 3910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3910,
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
