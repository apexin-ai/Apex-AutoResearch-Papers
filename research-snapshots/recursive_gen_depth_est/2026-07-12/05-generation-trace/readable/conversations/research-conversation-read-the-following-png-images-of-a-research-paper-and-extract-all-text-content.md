# Research conversation: Read the following PNG images of a research paper and extract ALL text content verbatim (especially section titles, expe

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a2be278cc5ed603b4.jsonl`
- **Structured JSON:** [`b68be5002ee3baa9b707.json`](../../sessions/b6/b68be5002ee3baa9b707.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-16T19:32:20.436Z_

Read the following PNG images of a research paper and extract ALL text content verbatim (especially section titles, experimental details, tables, and figures). Focus on: experiments section, results, ablations, and any discussion of LoRA rank sensitivity, feature groups, zero-shot LLM baselines.

Read these files in order:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png

For each page, report:
- All section/subsection headings
- Experimental setup details (models used, datasets, metrics)
- Table content (reproduce tables as markdown if possible)
- Discussion of: LoRA rank experiments, zero-shot LLM as "surface-text ablation" vs baseline, wild data FPR results, cross-scale claims and qualifications
- Any Limitations or Discussion section content
- Figure captions and descriptions

Return the FULL extracted text, preserving structure. Do not summarize.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a2be278cc5ed603b4",
  "type": "user",
  "uuid": "180b12a9-6aa2-4eb3-9eb5-b721a46f72fe",
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

_source line 2 · 2026-05-16T19:32:20.438Z_

```json
{
  "parentUuid": "180b12a9-6aa2-4eb3-9eb5-b721a46f72fe",
  "isSidechain": true,
  "agentId": "a2be278cc5ed603b4",
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
  "uuid": "33799cea-5b0c-444b-aac1-8ab9f67ebb8f",
  "timestamp": "2026-05-16T19:32:20.438Z",
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

_source line 3 · 2026-05-16T19:32:23.101Z_

<details open><summary>🔧 Tool call — Read · `toolu_014y4VgUe29tXkhQTpL6BLLf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33799cea-5b0c-444b-aac1-8ab9f67ebb8f",
  "isSidechain": true,
  "agentId": "a2be278cc5ed603b4",
  "requestId": "req_011Cb6oesE7DvgUqfTimxWaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ec7b754-38b8-4d92-b7d5-b42a922f17d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cja3KqsHjopo4iUG5t3CQE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8673,
      "cache_read_input_tokens": 8265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8673,
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

_source line 4 · 2026-05-16T19:32:23.727Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TuxFQNfTxSixojyj4sWe2d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ec7b754-38b8-4d92-b7d5-b42a922f17d6",
  "isSidechain": true,
  "agentId": "a2be278cc5ed603b4",
  "requestId": "req_011Cb6oesE7DvgUqfTimxWaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "791d4ce8-b636-44cf-b94a-8186db60c2be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cja3KqsHjopo4iUG5t3CQE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8673,
      "cache_read_input_tokens": 8265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8673,
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

_source line 5 · 2026-05-16T19:32:24.730Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CtqYehY85qZDHzZEwvmfTo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "791d4ce8-b636-44cf-b94a-8186db60c2be",
  "isSidechain": true,
  "agentId": "a2be278cc5ed603b4",
  "requestId": "req_011Cb6oesE7DvgUqfTimxWaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "991530da-fa5d-4700-896d-1c53c06c1cab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cja3KqsHjopo4iUG5t3CQE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8673,
      "cache_read_input_tokens": 8265,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8673
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 8265,
          "cache_creation_input_tokens": 8673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8673,
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

_source line 6 · 2026-05-16T19:32:24.735Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WwYuJ8UpqUFtatMcTJhzSv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "991530da-fa5d-4700-896d-1c53c06c1cab",
  "isSidechain": true,
  "agentId": "a2be278cc5ed603b4",
  "requestId": "req_011Cb6oesE7DvgUqfTimxWaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c5c24c7-8554-49e9-b228-ebfb075652ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cja3KqsHjopo4iUG5t3CQE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8673,
      "cache_read_input_tokens": 8265,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8673
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 8265,
          "cache_creation_input_tokens": 8673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8673,
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

_source line 7 · 2026-05-16T19:32:25.659Z_

<details><summary>↩ Tool result · `toolu_014y4VgUe29tXkhQTpL6BLLf`</summary>

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
  "parentUuid": "0ec7b754-38b8-4d92-b7d5-b42a922f17d6",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a2be278cc5ed603b4",
  "type": "user",
  "uuid": "a5269527-26a5-4d32-8f19-12aa42b2da88",
  "sourceToolAssistantUUID": "0ec7b754-38b8-4d92-b7d5-b42a922f17d6",
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

_source line 8 · 2026-05-16T19:32:26.667Z_

<details><summary>↩ Tool result · `toolu_01TuxFQNfTxSixojyj4sWe2d`</summary>

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
  "parentUuid": "791d4ce8-b636-44cf-b94a-8186db60c2be",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a2be278cc5ed603b4",
  "type": "user",
  "uuid": "80c44735-d186-459f-801e-a1146a95072e",
  "sourceToolAssistantUUID": "791d4ce8-b636-44cf-b94a-8186db60c2be",
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

_source line 9 · 2026-05-16T19:32:27.456Z_

<details><summary>↩ Tool result · `toolu_01CtqYehY85qZDHzZEwvmfTo`</summary>

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
  "parentUuid": "991530da-fa5d-4700-896d-1c53c06c1cab",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a2be278cc5ed603b4",
  "type": "user",
  "uuid": "7696447c-c362-4723-a752-e5c4a86761a3",
  "sourceToolAssistantUUID": "991530da-fa5d-4700-896d-1c53c06c1cab",
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

_source line 10 · 2026-05-16T19:32:27.584Z_

<details><summary>↩ Tool result · `toolu_01WwYuJ8UpqUFtatMcTJhzSv`</summary>

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
  "parentUuid": "7c5c24c7-8554-49e9-b228-ebfb075652ea",
  "isSidechain": true,
  "promptId": "7a8010eb-b6a1-4d1b-aa4e-cd84d2a39d6d",
  "agentId": "a2be278cc5ed603b4",
  "type": "user",
  "uuid": "7db9ae44-265b-4d4e-9f4e-02c1d896211c",
  "sourceToolAssistantUUID": "7c5c24c7-8554-49e9-b228-ebfb075652ea",
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

_source line 11 · 2026-05-16T19:35:20.680Z_



Here is the full extracted text from all four pages:

---

## PAGE 5 (main_p5.png)

**[Figure 1]** (top of page, left side)

A line chart titled with axis labels "Perplexity AUC" (y-axis) and "Depth d" (x-axis, values d0 through d4). Three lines are plotted:
- Pythia 1.4B (blue circles)
- GPT-2 XL (orange triangles)
- OLMo 1B (green squares)

Horizontal dashed lines mark τ = {0.65, 0.70, 0.75, 0.80}. All three curves converge below 0.70 at d4–d5. Shaded bands: bootstrap 95% CIs.

**Caption:** Figure 1: Binary pairwise AUC decay curves for three models (nucleus sampling, depth 0–5). VIF and var\_surprise reveals 14 to 18 features with VIF≤10, placing effective dimensionality at 4–5; forward selection confirms the dominant pair (p90\_ppl first in 69 cells, var\_surprisal in 39). The bivariate shifts with depth—var\_surprisal dominates at shallow boundaries while tail perplexity statistics take over deeper, consistent with model-collapse dynamics (Shumailov et al., 2024) (§5) (temperature heatmap in Figure 4, Appendix A.5).

---

of full accuracy; top-5 achieve 97.6%. VIF analysis reveals 14 to 18 features with VIF≤10, placing effective dimensionality at 4–5; forward selection confirms the dominant pair (p90\_ppl first in 69 cells, var\_surprisal in 39). The bivariate shifts with depth—var\_surprisal dominates at shallow boundaries while tail perplexity statistics take over deeper, consistent with model-collapse dynamics (Shumailov et al., 2024) (§5) (temperature heatmap in Figure 4, Appendix A.5).

### 4.3 Monotonicity and EDD Analysis

Depth features exhibit strong monotonic trends: perplexity tail statistics decrease with depth (Spearman ρ = −1 across cell-level medians) while repetition features increase (trajectories in Figure 3, Appendix A.1). Inter-depth distances are monotonically uniform (d0-vs-d1 AUC exceeds 0.99 in all cells, whereas d2-vs-d3 ranges from 0.69 to 0.89.

We extend to depth d=5 for all three models under nucleus sampling, training dedicated binary RF classifiers (500 trees) for each adjacent pair (fig. 1). Figure 1 shows the AUC decay: Pythia-1.4B decays monotonically from 0.999 (d0|1) to 0.683 (d4|5), with the steepest drop between d0-2 and d2-3. The d3-vs-d4 AUC clusters near T=0.75 across all three models (0.750–0.784), while d4–d5 uniformly falls below 0.70, establishing a consistent depth-4 decay boundary. At T=0.75, 7/9 atlas cells maintain EDD ≥ 3 on the primary benchmark; at T=0.80, 3/9 (full threshold sensitivity in Table 17, Appendix A.16).

EDD uses binary-pair classifiers to avoid decision boundary dilution: in Pythia nucleus, d2-vs-d3 AUC degrades from 0.804 (4-class) to 0.689 (6-class) despite identical data.

### 4.4 Strategy-Dependent Trajectories

The three decoding strategies induce qualitatively distinct degradation trajectories. Nucleus (p=0.95) produces the most consistent accuracy (78.2–83.3%) and serves as the reference. Temperature (τ=0.9) yields the highest accuracy in 2/3 models because uniform logit scaling accelerates convergence to an attractor distribution (Shumailov et al., 2024), amplifying the fingerprint—but creating a boundary reversal risk where temperature depth 5 features approximate nucleus-only d-depth (N+1) features (§5). Top-1 (ε=50) produces the lowest accuracy (69.6–76.6%) because hard vocabulary truncation removes depth-discriminative low-probability tokens, though feature direction is preserved (cross-model ρ = 0.811). The strategy effect (8.4 pp range) exceeds the model effect (7.1 pp).

### 5 Generalization and Robustness

We evaluate generalization along seven axes: four below—classifier choice (§5.1), cross-model transfer (§5.2), cross-strategy transfer (§5.3), and cross-scale (§5.4)—and three in the Appendix (end-to-end learning, temperature robustness, cross-boundary transfer).

### 5.1 Baseline Comparison

Table 3 evaluates RF, XGBoost, and LightGBM on the same 19 features across three atlas cells. Per-cell spread is <0.4pp, establishing a feature-determined ceiling independent of the learning algorithm. CORAL ordinal regression (Cao et al., 2020) and DeBERTa (Bhasin and Chen, 2026) match RF within 0.1 pp (ρ > 0.05); all feature-based methods significantly outperform CE-MLP (74.9%) and logistic regression (75.0%). Single-feature regression on mean perplexity performs at chance (25.3 ± 1%); two zero-shot LLMs—DeepSeek-V3.2 (26.5%, 95% CI [22.0, 31.0]) and Qwen2.5-7B-Instruct (30.4%, [26.5, 34.6])—also fail, with an accuracy gap exceeding 42 pp vs. RF. Figure 2 shows all near-perfectly identified; errors concentrate at d2/d3.

### 5.2 Cross-Model Transfer

We perform leave-one-model-family-out evaluation: train on two families (nucleus only), test on the held-out third (Table 4).

---

## PAGE 6 (main_p6.png)

**Table 3:** Classifier convergence: 4-class accuracy (%) across three atlas cells. RF, XGBoost, LightGBM on the same 19 features; Δ_max: largest per-cell spread. Chance = 25%.

| Cell | RF | XGB | LGBM | Δ_max |
|------|-----|------|------|-------|
| Pythia_nuc | 78.8 | 79.0 | 78.8 | 0.2 |
| GPT-2 XL_t | 83.8 | 84.2 | 84.5 | 0.4 |  *(note: "t" likely refers to temperature)*
| Pythia_top-k | 60.9 | 60.5 | 60.7 | ... |  *(partially visible)*

**[Figure 2]** Confusion matrices for the best-in-setting (GPT-2 XL, temp τ=0.9, 85.4%) and the best cross-model leave-one-out transfer (OLMo holdout, 60.2%); d0 recall ≈99%; in both, errors concentrate in d1-d3 under transfer.

Caption text below Figure 2:

Mean transfer accuracy is 66.4% (2.7× chance); d0 recall (>98%) inflates the headline while d2 drops to 26.8% (Pythia holdout).

### 5.3 Cross-Strategy Transfer

We train on two decoding strategies and test on the held-out third (Table 5).

Mean cross-strategy accuracy (59.1%) falls 7pp below cross-model (66.4%). Training on nucleus + top-k and testing on temperature inverts the d1/d2 boundary (d1/2 AUC < 0.5); per-strategy z-score normalization partially recovers it but leaves a residual gap (4 limitations). A multi-temperature ablation (Appendix A.6) confirms within-τ robustness for τ ∈ [0.9 ±0.12] AUC < 0.00 but cross-τ transfer (mean 46.7%) is harder than cross-strategy transfer. End-to-end PLMs (DeBERTa-V3, RoBERTa) achieve only ~59%, lagging RF and >1pp, confirming depth signal resides in perplexity tail statistics inaccessible to standard PLM representations (Appendix A.8).

### 5.4 Cross-Scale Analysis

We extend to four 7–8B models—Qwen2.5-7B-Instruct (Team, 2025) and Llama-3.1-8B-Instruct (Grattafiori et al., 2024)—under 4-bit NF4 QLoRA, generating depths d ∈ {0,...,5} with nucleus sampling (500 samples/depth). Table 6 re-

**Table 4:** Cross-model transfer (leave-one-out, nucleus only). Chance = 25% / 33% (d1-d3), d1-d3 bal. acc: Pythia 49.9%, OLMo 39.2%. GPT-2 XL 57.2% (mean 55.4%).

| Holdout | Acc | d0 | d1 | d2 | d3 |
|---------|-----|----|----|----|-----|
| | (%) | Rec. | Rec. | Rec. | Rec. |
| Pythia | 62.4 | 100.0 | 49.3 | 24.8 | 73.6 |
| OLMo | 69.2 | 99.3 | 75.4 | 24.1 | 53.8 |
| GPT-2 XL | 67.6 | 98.5 | 74.7 | 52.6 | 44.5 |
| Mean | 66.4 | 99.1 | 66.5 | 40.9 | 59.0 |  *(Note: row labeled "Mean" visible)*

**Table 5:** Cross-strategy transfer (leave-one-out). Chance = 25%.

| Holdout | Pythia | OLMo | GPT-2 XL |
|---------|--------|------|----------|
| Acc (%) | Acc (%) | Acc (%) | Pct |  *(header partially visible)*
| nucleus | 69.4 | 65.4 | 59.9 |
| temp (τ=0.9) | 62.8 | 54.2 | 56.1 |  *(Note: uncertain on exact numbers)*
| top-k (ε=50) | 51.5 | 53.6 | 54.9 |  *(Note: partially visible)*

ports matched evaluation against the 1–1.5B models.

Both 7–8B models substantially exceed chance: Llama-3.1-8B at 70.2% and Qwen2.5-7B at 60.1%, with d0 separability preserved (AUC > 0.949). Llama-3.1-8B matches smaller models at EDD∈[3,4] with monotonic AUC decay; Qwen2.5-7B achieves EDD_0.70 = 5 via a non-monotonic (U-shaped) trajectory where AUC recovers after a d2-d3 minimum (consecutive AUC profiles in Table 18, Appendix A.17). Per-step signal strength decreases at larger scale (mean consecutive AUC 0.78 vs. 0.85 at 1–1.5B), and the divergent trajectories suggest instruction tuning may alter degradation dynamics, though further architectures are needed. Cross-model recursive chains (84.7%) and cross-domain transfer (arXiv 74.1%) further confirm signal universality (Appendix A.13).

### 6 Discussion and Conclusion

We formulated recursive generation depth estimation and showed that a compact feature set dominated by perplexity tail statistics achieves 70–85% four-class accuracy (EDD_0.75=4 across models), with five features sufficing for 97.6% of full performance and classifier-agnostic convergence within ≤0.4pp. The dominant pair (p90\_ppl, top-2 in 99 cells, var\_surprisal in 8/9 under SHAP) generalizes across the three studied model families without retraining, making depth estimation a candidate early-warning signal for model collapse (Shumailov et al., 2024). Recent work corrob-

---

## PAGE 7 (main_p7.png)

**Table 6:** Cross-scale comparison: 4-class RF accuracy (%), depths 0–3, nucleus. EDD_τ=0.75 (depths 0–5), and d0-vs-d1 AUC. CI: 95% bootstrap. Chance = 25%.

| Model | 4-class acc. | EDD_τ=0.75 | d0-d1 AUC |
|-------|-------------|------------|-----------|
| GPT-2 XL (1.5B) | 83.8 | 4 | 0.999 |
| OLMo-1B | 78.8 | 4 | 0.997 |
| Pythia-1.4B | 78.8 | 4 | 0.999 |
| Llama-3.1-8B | 70.2 [68.8, 72.4] | 4 | 0.949 |
| Qwen2.5-7B | 60.1 [58.0, 62.3] | 5 | ... |

*(last entry partially visible)*

(continuation of Section 6 — Discussion and Conclusion):

orates this connection, identifying entropy decline as a measurable signal of recursive degradation that parallels the tail erosion our features capture (Shi et al., 2025). Zero-shot LLM baselines (DeepSeek-V3.2, 26.5%; Qwen2.5-7B, 30.4%) perform near chance, confirming that depth discrimination requires computed statistical features rather than general language understanding.

Cross-strategy transfer remains the primary bottleneck (59.1% vs. 66.4% cross-model), with the temperature-induced d1/d2 AUC inversion making single-classifier deployment across unknown strategies infeasible; strategy-conditioned classifiers—preceded by automatic strategy identification exploiting distinguishable perplexity signatures—offer a practical path, particularly since single-platform deployment typically knows the decoding strategy a priori.

Depth estimation enables graduated data curation beyond the binary human/machine distinction (Xie et al., 2025; Wrtg et al., 2024): a proof-of-concept shows RF-filtered subsets match unfiltered quality with 44% of the data (Appendix A.11). As a provenance signal, it complements watermarking (Kirchenbauer et al., 2023) and source attribution (Chenela et al., 2020) by characterizing iterative reuse regardless of generator identity (Revirsdorff et al., 2025). Cross-scale experiments (§5.4) confirm signal persistence at 7–8B scale with divergent AUC trajectories across architectures, suggesting instruction tuning may alter degradation dynamics; extending to segment-level estimation introduces a granularity–statistical-power tradeoff.

**Limitations**

**Cross-strategy deployment constraint.** Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling. Per-strategy z-score normalization partially corrects the inver-

sion under logistic regression (GPT-2 XL, d1/v2 AUC 0.24→0.56, OLMo 0.19→0.71) but yields negligible improvement for the Random Forest classifier used throughout the main experiments (Δ < 0.02 pp), and even in the best case (logistic regression) leaves a residual gap relative to within-strategy performance (ε>0.50), indicating that a two-stage pipeline (strategy identification → strategy-conditioned classification) is needed for reliable cross-strategy deployment.

**d0 inflation of headline metrics.** Depth 0 (human-written text) is near-perfectly separable (recall >98%) across all nine model-strategy settings, inflating headline accuracy. Cross-model transfer accuracy of 66.4% is substantially driven by d0; d2 recall drops to 26.8% in the worst case (Pythia holdout).

**Controlled vs. ecological setting.** The primary benchmark uses Wikipedia seed text with controlled recursive generators (LoRA fine-tuned, 1–1.5B parameter models); cross-scale experiments extend to 7–8B instruction-tuned models (§5.4). This protocol isolates the recursive depth variable but diverges from wild recursive contamination, where models are pretrained on mixed corpora containing post-generation outputs as unknown proportions; the fingerprints we identify may attenuate or shift under such diffuse exposure. Depth signal is the dominant classification factor (5-fold CV 95-82%), up to 2.5× chance. LOGO accuracy (72.1%) matches standard CV (72.0%), and subgroup prediction is at chance (10.25 vs. 10%; Appendix A.9). The 7–8B experiments use instruction-tuned models: only; whether base models at this scale exhibit the same signal profile remains open. Real-world documents may also interleave segments at different recursive generation depths, extending to segment-level estimation introduces a granularity–statistical-power tradeoff.

**Domain-dependent false positive rate.** On editorial text (WikiText-103), all classifiers achieve >98.5% d0 accuracy, but on web-crawl data (C4, 5,000 passages), FPR ranges from 4.7% (OLMo) to 22.4% (GPT-2 XL). Mislassification concentrates in template/SEO content with elevated repetition features (rep\_3gram +37%, rep\_4gram +75% vs. correctly classified d0); the model gap likely reflects training data composition (OLMo's Dolma includes diverse web data vs. Pythia/ GPT-2 XL's Wikipedia/WebText). Deployment on

---

## PAGE 8 (main_p8.png)

(continuation of Limitations):

heterogeneous web corpora requires model- and domain-specific calibration.

**Adversarial robustness.** Adversarial paraphrasing (Sadasivan et al., 2023) could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.

**EDD monotonicity assumption.** Our EDD definition (Eq. 1) requires all pairwise AUCs up to depth d* to exceed T, which is well-behaved when AUC decays monotonically—as observed in all our configurations. However, Bakshi and Chakraborty (2026) show that early recursion can temporarily improve model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d3/d5). Our cross-strategy results provide an empirical example of non-monotonic: training on nucleus + top-k and testing on temperature yields d1-vs-d2 AUC as low as 0.129 (GPT-2 XL) and 0.253 (OLMo), violating the monotonicity assumption. In such cases EDD would conservatively report a lower value than the deepest discriminable pair, potentially underestimating the true discriminable range; extending EDD to handle non-contiguous discriminable regions is future work. The choice of threshold T is also application-dependent: at T=0.80, several cells lose one depth level relative to T=0.75.

**Reference model dependency.** Surprisal-based features are computed relative to Pythia-1.4B, which coincides with one of the three generators. For the Pythia pipeline this constitutes self-model feature extraction, while OLMo and GPT-2 XL measurements are cross-model. Empirically, the self-model configuration does not yield the highest accuracy (Pythia 78.2% vs. GPT-2 XL 85.4%), suggesting the overlap does not confer a systematic advantage. An ablation with OLMo-1B as reference model shows 2-4pp (±2.3), suggesting moderate robustness; however, both reference models share similar scale (~1B) and autoregressive architecture, so validation with architecturally distinct references (e.g., encoder-only or larger-scale models) remains open. The choice of reference model affects feature values; a different reference model may shift absolute feature magnitudes and potentially alter discriminability at depth boundaries.

**Additional caveats.** Detection features degrade under domain shift (Pudasaini et al., 2026); our depth features are likely susceptible. Falashi et al. (2026) show that curated synthetic data need not trigger collapse, attenuating the fingerprints we exploit.

### Ethics Statement

This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2 XL) and Wikipedia text as seed. No human subjects were involved, no private or sensitive data were collected, and no new models were released. Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research. Code and data will be released upon acceptance.

### References

Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk. 2024. Self-Consuming Generative Models Go MAD. In *Proceedings of ICLR*. arXiv:2307.01850.

Soham Bakshi and Sumit Chakraborty. 2026. From Collapse to Improvement: Statistical Perspectives on the Evolution Dynamics of Iterative Training on Contaminated Sources. arXiv:2602.10531.

Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyang Yan, and Yue Zhang. 2024. Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature. In *Proceedings of ICLR*. arXiv:2310.05130.

Advit Raj Basani and Pin-Yu Chen. 2026. 2026. Detection Bootstraps AI-Generated Text Detection: Classifier on Machine Learning Research (TMLR). arXiv:2509.18880.

Sourya Basu, Govardana Sachithanandam Ramachan-dran, Nitish Shirish Keskar, and Lav R. Varshney. 2021. Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity. In *Proceedings of ICLR*.

Janek Bevendorff, Matti Wiegmann, Emmelie Richter, Martin Potthast, and Benno Stein. 2025. The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification. In *Findings of the Association for Computational Linguistics: ACL, 2025, pages 3762–3787, Vienna, Austria.*

Wenxiu Cao, Vahid Mirjalili, and Sebastian Raschka. 2020. Rank Consistent Ordinal Regression for

---

That is the full verbatim extraction from all four pages. Key elements summarized by topic:

**Experimental setup:** Three 1–1.5B models (Pythia-1.4B, OLMo-1B, GPT-2 XL); three decoding strategies (nucleus p=0.95, temperature τ=0.9, top-k ε=50); 19 perplexity-based features; RF/XGBoost/LightGBM classifiers; 4-class depth classification (d0–d3); extended to d0–d5 for EDD analysis. Cross-scale uses Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct under 4-bit NF4 QLoRA.

**LoRA rank sensitivity:** Not directly discussed as a standalone ablation in these pages. QLoRA (4-bit NF4) is mentioned only in the cross-scale §5.4 for generating recursive data with 7–8B models.

**Zero-shot LLM baselines (surface-text ablation):** DeepSeek-V3.2 achieves 26.5% (95% CI [22.0, 31.0]) and Qwen2.5-7B-Instruct 30.4% ([26.5, 34.6]) — both near chance (25%), with accuracy gap exceeding 42pp vs. RF. Discussed in §5.1 and §6 as confirming depth discrimination "requires computed statistical features rather than general language understanding."

**Wild data FPR results:** On WikiText-103 (editorial), >98.5% d0 accuracy. On C4 web-crawl data (5,000 passages), FPR ranges 4.7% (OLMo) to 22.4% (GPT-2 XL). Misclassification concentrates in template/SEO content with elevated repetition features (rep_3gram +37%, rep_4gram +75%).

**Cross-scale claims:** 7–8B models exceed chance (Llama 70.2%, Qwen 60.1%) but per-step signal strength decreases (mean consecutive AUC 0.78 vs. 0.85 at 1–1.5B). Divergent trajectories (Qwen U-shaped, Llama monotonic) suggest instruction tuning may alter degradation dynamics. Qualified with "though further architectures are needed."

**Limitations section:** Six explicit limitations — cross-strategy deployment constraint, d0 inflation of headline metrics, controlled vs. ecological setting gap, domain-dependent FPR, adversarial robustness (untested), EDD monotonicity assumption, reference model dependency, and additional caveats about domain shift and curated synthetic data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7db9ae44-265b-4d4e-9f4e-02c1d896211c",
  "isSidechain": true,
  "agentId": "a2be278cc5ed603b4",
  "requestId": "req_011Cb6ofPktiaJoBPUDnuxUj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edb8a972-3fb5-4c92-8c4f-710e6f0d880d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335",
  "sessionId": "f5009a54-ac13-49a4-83d8-13bbafebaca9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JUUvPiagbhDabyGrh71Pvx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 16938,
      "output_tokens": 6541,
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
          "output_tokens": 6541,
          "cache_read_input_tokens": 16938,
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
