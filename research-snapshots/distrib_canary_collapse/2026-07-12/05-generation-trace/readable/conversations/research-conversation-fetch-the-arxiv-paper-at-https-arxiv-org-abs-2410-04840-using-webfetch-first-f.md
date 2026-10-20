# Research conversation: Fetch the arXiv paper at https://arxiv.org/abs/2410.04840 using WebFetch. First fetch the HTML version at https://arxiv.

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6a18d51af7e60f09.jsonl`
- **Structured JSON:** [`1f937df967d473d3ade3.json`](../../sessions/1f/1f937df967d473d3ade3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-20T15:00:46.292Z_

Fetch the arXiv paper at https://arxiv.org/abs/2410.04840 using WebFetch.

First fetch the HTML version at https://arxiv.org/html/2410.04840v3 with the prompt:
"Extract the full paper content in detail. I need:
1. Complete introduction section with all paragraphs
2. The contribution statement (usually end of intro)
3. Complete experiment/results section including all tables and figures descriptions
4. Limitations and future work section
5. All figure and table captions
6. All references to figures/tables in the main text
7. Method section key details
8. Baselines, metrics, datasets used
9. Training recipe details (optimizer, lr, hardware, etc.)
Return as much detail as possible."

If the HTML version fails, try https://arxiv.org/abs/2410.04840 with the same prompt.

Then report EVERYTHING you extracted - do not summarize, give me the full extracted content. This is "Strong Model Collapse" (ICLR 2025 Spotlight).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "217d91de-5e08-4964-9121-ae00bd1d3957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T15:00:46.294Z_

```json
{
  "parentUuid": "217d91de-5e08-4964-9121-ae00bd1d3957",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
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
  "uuid": "9e4c9deb-cbbb-434d-b765-3fb92bed78f4",
  "timestamp": "2026-05-20T15:00:46.294Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-20T15:00:48.481Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DzSfn8uWQTvLRTSruzkBLU`</summary>

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
  "parentUuid": "9e4c9deb-cbbb-434d-b765-3fb92bed78f4",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2BRBjLVmNasTu2FJCD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c791f70-a2f2-4cb2-94ef-9e72895fb253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012X3rz6PbRgGhog6oq2TdXA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9033,
      "cache_read_input_tokens": 8155,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9033
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 8155,
          "cache_creation_input_tokens": 9033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9033,
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

_source line 4 · 2026-05-20T15:00:48.488Z_

<details><summary>↩ Tool result · `toolu_01DzSfn8uWQTvLRTSruzkBLU`</summary>

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
  "parentUuid": "3c791f70-a2f2-4cb2-94ef-9e72895fb253",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "87adb19b-636e-48a1-af91-5f993a1e4d49",
  "sourceToolAssistantUUID": "3c791f70-a2f2-4cb2-94ef-9e72895fb253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T15:00:51.817Z_

I'll fetch the HTML version first, then fall back if needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87adb19b-636e-48a1-af91-5f993a1e4d49",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2BapQvgCzRLL745aW4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86617ffd-c68c-4f96-a1a3-01999600d34e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GKQ2YnsHd8wFyrWASCFYHs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 17188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

_source line 6 · 2026-05-20T15:00:53.330Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013UYYSyG4oRpPiscyw2MVg5`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.04840v3",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86617ffd-c68c-4f96-a1a3-01999600d34e",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2BapQvgCzRLL745aW4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee1bc7ec-4ba4-436c-9f4a-116ea9265f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GKQ2YnsHd8wFyrWASCFYHs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 17188,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 17188,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1432,
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

_source line 7 · 2026-05-20T15:00:53.337Z_

<details><summary>↩ Tool result · reported error · `toolu_013UYYSyG4oRpPiscyw2MVg5`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee1bc7ec-4ba4-436c-9f4a-116ea9265f06",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "088d612a-4c2d-4308-bc7f-b5e976ccbeb8",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "ee1bc7ec-4ba4-436c-9f4a-116ea9265f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T15:00:56.500Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RPvLz92ueQQuPWJZnTeyyc`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.04840v2",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "088d612a-4c2d-4308-bc7f-b5e976ccbeb8",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2BwLhFzpHb86ssxQTa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e31ac3e2-dae3-4f56-baab-8f02f678cdb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018MUxK2fZPCGpCVE5bYjrKP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 18620,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 247
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 18620,
          "cache_creation_input_tokens": 247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 247,
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

_source line 9 · 2026-05-20T15:01:13.249Z_

<details><summary>↩ Tool result · `toolu_01RPvLz92ueQQuPWJZnTeyyc`</summary>

```text
# Summary of "Strong Model Collapse" Paper

## Introduction & Core Contribution

The paper investigates **model collapse** — performance degradation when AI models train on synthetic data mixed with real data. The authors establish that even "as little as 1% of the total training dataset" of synthetic data can degrade performance, contradicting assumptions that simple data mixing strategies prevent collapse.

**Two main results:**

1. **Strong Model Collapse**: Models trained on any fixed proportion of synthetic data (where p₂ doesn't vanish) suffer persistent performance degradation unless synthetic data proportion approaches zero asymptotically.

2. **Model Size Effects**: Larger models amplify collapse before the interpolation threshold but may mitigate it afterward, predicting a "double-descent" curve in collapse severity.

## Methodology

The analysis employs **operator-valued free probability theory** to derive a new bias-variance decomposition:

E_test ≃ B + V + ζ

where the extra term ζ quantifies model collapse. The framework analyzes:
- **Classical linear regression** with ridge regularization
- **Random projections models** approximating neural networks with tunable width m

Work assumes Gaussian features, linear labeling functions with label noise, and studies the "proportionate scaling limit" where dimensions, samples, and model size all grow.

## Theoretical Setup Key Details

**Data distributions**: Two sources with potentially mismatched label functions (w₁* vs w₂*). Quality metric c² measures disparity via "tr(ΣΔ)/d" where Δ = cov(w₂* - w₁*).

**Asymptotic regime**: d, n → ∞ with fixed ratios d/n → φ and m/n → ψ for random projections.

## Main Experimental Results

### Toy Settings
- Random projections on Gaussian data
- Two-layer networks on MNIST
- Perfect agreement between theory and experiments (Figures 2, 5)

### Language Modeling (GPT-2 on BabiStories)
Results demonstrate:
- Synthetic data proportion impact: "Impact of Synthetic Data Proportion" shows test perplexity increases with p₂
- Model size impact: "Impact of Model Size" confirms larger models suffer worse collapse initially

### Key Finding from Corollary 1
In the underparametrized isotropic case with small φ:

E_test ≃ σ²d/n + p₂²c² + O(φ²)

This shows collapse error scales quadratically with synthetic proportion and doesn't vanish as dataset size grows.

## Strategic Data Mixing Analysis (Section 5)

The paper evaluates whether weighted mixing or multi-step approaches prevent collapse:

- **Single-step weighted mixing**: Fails unless weights asymptotically remove all synthetic data
- **Multi-step dynamic mixing**: No complete solution identified

Conclusion: "model collapse cannot generally be mitigated by simple adjustments such as data weighting" unless strategies "asymptotically remove all but a vanishing proportion of synthetic data."

## Figure Descriptions

**Figure 1** (Pareto diagram): Compares test error with mixed vs. real-only training for random projections. Shows Pareto frontiers for different synthetic data quality levels; higher frontiers indicate worse collapse.

**Figure 2**: Illustrates the B+V+ζ decomposition for random projections, showing double-descent in bias term and ζ's contribution to model collapse.

**Figure 3**: Empirical confirmation of Corollary 1 in classical linear models, showing test error deviates from ideal scaling law (p₂=0) even with small synthetic fractions.

**Figure 4**: Impact of model size m on collapse across different data quality levels and synthetic proportions.

**Figure 5**: Double-descent curve visualization matching theoretical predictions.

## Limitations & Open Questions

The work focuses on:
- Gaussian feature distributions and linear labeling
- Simplified neural network approximation (random projections)
- Supervised regression settings

Unresolved: Methods to effectively prevent collapse beyond data curation/filtering mentioned briefly.

## Datasets & Training Details

- **MNIST**: Two-layer fully-trained networks
- **BabiStories**: Reproduction of TinyStories using Mixtral-8x7B to generate synthetic data; GPT-2 models trained with varying synthetic proportions
- **Gaussian experiments**: Controlled d=600, identity covariance, n=500 total samples

Specific hyperparameters for language modeling (learning rates, batch sizes, hardware) relegated to Appendix A.3.

## Key Metrics

- Test error on true data distribution P₁
- Proportion of synthetic data (p₂ or n₂/n)
- Data quality parameter c²
- Model parametrization rate (ψ = m/n)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e31ac3e2-dae3-4f56-baab-8f02f678cdb8",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "6d81c6a7-7bd7-43e6-9eeb-182bacc20146",
  "sourceToolAssistantUUID": "e31ac3e2-dae3-4f56-baab-8f02f678cdb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T15:01:16.564Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Kf7x39D351QAvDDYaMnEtn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.04840",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d81c6a7-7bd7-43e6-9eeb-182bacc20146",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2DQR9nxERJDDHKWAYE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d03a1707-94e8-4d2b-acd5-939ee2f5bcc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NZFYXpnJipuTrsuz7JU6tZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1326,
      "cache_read_input_tokens": 18867,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1326
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 18867,
          "cache_creation_input_tokens": 1326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1326,
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

_source line 11 · 2026-05-20T15:01:21.492Z_

<details><summary>↩ Tool result · `toolu_01Kf7x39D351QAvDDYaMnEtn`</summary>

```text
# Analysis of "Strong Model Collapse" Paper

Based on the arXiv page provided, I can only access the abstract and metadata. The full paper content (introduction, experiments, methods, results, figures, tables, and references) is not included in the webpage excerpt you shared.

## What's Available:

**Title:** Strong Model Collapse

**Authors:** Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe

**Key Finding from Abstract:**
The research demonstrates that "even the smallest fraction of synthetic data (e.g., as little as 1% of the total training dataset) can still lead to model collapse."

**Research Domain:** Machine Learning (cs.LG/stat.ML)

**Submission Date:** October 7-8, 2024

## What's Not Available:

To extract the detailed sections you requested—full introduction, contribution statements, complete experiments, limitations, figure captions, training details, baselines, metrics, datasets, and references—you would need to:

1. **Access the PDF directly** via the "/pdf/2410.04840" link
2. **View the HTML version** (marked experimental)
3. **Download the TeX source** for complete technical details

The webpage excerpt contains only bibliographic metadata and abstract information, not the full paper content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d03a1707-94e8-4d2b-acd5-939ee2f5bcc5",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "c92d2024-82f1-4e61-8f5b-c424b6894d81",
  "sourceToolAssistantUUID": "d03a1707-94e8-4d2b-acd5-939ee2f5bcc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T15:01:24.847Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M4QsZ3B6HPzESK8bfeJtwd`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.04840v1",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c92d2024-82f1-4e61-8f5b-c424b6894d81",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2E1jvF5kdbjcuwsoDZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e732419-3eca-41d4-aad3-eee843b41ae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QoPoDns9m277vqiTKzWXcN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 507,
      "cache_read_input_tokens": 20193,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 507
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 20193,
          "cache_creation_input_tokens": 507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 507,
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

_source line 13 · 2026-05-20T15:01:40.408Z_

<details><summary>↩ Tool result · `toolu_01M4QsZ3B6HPzESK8bfeJtwd`</summary>

```text
# Summary of "Strong Model Collapse" Research Paper

## 1. Introduction & Core Contributions

The paper addresses "model collapse"—a critical performance degradation when training data includes synthetic content generated by other models. The authors establish that even minimal synthetic data (1% of training set) can severely degrade performance, breaking neural scaling laws.

**Main findings:**
- "Even the smallest fraction of synthetic data...can still lead to model collapse" where larger datasets don't improve performance
- Strategic data mixing alone cannot prevent collapse unless synthetic data proportion approaches zero
- Model size effects are non-monotonic: larger models amplify collapse in underfitting regimes but may mitigate it post-interpolation threshold

## 2. Theoretical Framework

**Setup:** The authors analyze supervised regression with mixed real (P₁) and synthetic (P₂) data distributions using:

- **Classical linear model:** Ridge regression in input space
- **Random projections model:** Simplified neural networks approximated via random feature maps (captures model size effects through m parameters)

**Key parameters:**
- p₂: proportion of synthetic data in training set
- c²: synthetic data quality metric measuring distribution mismatch
- ψ = m/n: parametrization rate (model size relative to sample size)

## 3. Novel Bias-Variance Decomposition

The central theoretical contribution is a decomposition: **E_test ≃ B + V + ζ**

Where B (bias) and V (variance) follow classical patterns, but ζ represents an additional error term directly attributable to synthetic data contamination. Critically, "unless p₂→0⁺, the performance of the model eventually plateaus" above baseline.

In the isotropic case with small proportions of data: "E_test ≃ σ²d/n + p₂²c² + O(ϕ²)"

This demonstrates strong collapse: test error includes irreducible p₂²c² term that vanishes only when synthetic data is completely eliminated.

## 4. Experimental Validation

**Datasets and models tested:**

1. **Gaussian toy setting:** Random projections with synthetic data from modified label distributions
2. **MNIST:** Two-layer neural networks with full training
3. **Language modeling:** GPT-2 models trained on BabiStories (synthetic generation using Mixtral-8x7B)

**Key experimental findings:**
- Theoretical predictions match empirical results with "perfect match" (Figure 3)
- Model size creates double-descent phenomenon in collapse behavior
- Small synthetic data fractions (5-20%) produce measurable performance degradation across settings

## 5. Mitigation Strategies Analysis

The paper examines whether strategic approaches can prevent collapse:

- **Weighted single-step mixing:** Fails unless approaching zero synthetic proportion
- **Dynamic multi-step mixing:** Discussed as potential but insufficient without asymptotic elimination of synthetic data

"Model collapse cannot generally be mitigated by simple adjustments such as data weighting...unless these strategies asymptotically remove all but a vanishing proportion of synthetic data"

## 6. Key Technical Details

**Mathematical tools:** Operator-valued free probability theory (OVFPT) for computing high-dimensional limits of random matrix traces

**Scaling regimes:**
- Classical model: d, n → ∞ with d/n → ϕ ∈ (0,∞)
- Random projections: Additionally m/d → γ and m/n → ψ

**Fixed-point equations:** Complex transcendental equations define parameters e, τ, u, ω characterizing model behavior

## 7. Limitations & Open Questions

The paper focuses on theoretical settings (linear models, Gaussian features). Real neural networks may exhibit different dynamics. Practical mitigation beyond synthetic data elimination remains an open challenge.

## 8. Figure/Table References

- **Figure 1:** Pareto frontier showing model size effects across synthetic data qualities
- **Figure 2:** Illustration of bias-variance decomposition with double-descent
- **Figure 3:** Empirical validation of Corollary 1 (isotropic case)
- **Figure 4:** Impact of model size on collapse across quality levels
- **Figure 5:** Double-descent curve empirical confirmation

All figures demonstrate close alignment between theoretical predictions and experimental observations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e732419-3eca-41d4-aad3-eee843b41ae9",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "56b99f06-686f-406f-95b0-fbddc475c91e",
  "sourceToolAssistantUUID": "4e732419-3eca-41d4-aad3-eee843b41ae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T15:01:45.167Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MMRRLmTQ7E8N9NRi9xrREL`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2410.04840",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs - extract verbatim\n2. The contribution statement (usually end of intro) - extract verbatim\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section - extract verbatim\n5. All figure and table captions - extract verbatim\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\n10. All section headings and subheadings\nReturn as much verbatim text as possible, especially intro and contribution sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56b99f06-686f-406f-95b0-fbddc475c91e",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2FQccSa5D5QPehHY5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3456f01d-53a9-4ea1-9419-a8a30bbb2e5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01K7zM4nz5YLPxLFZfbSKYsx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1191,
      "cache_read_input_tokens": 20700,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1191
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 20700,
          "cache_creation_input_tokens": 1191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1191,
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

_source line 15 · 2026-05-20T15:01:52.745Z_

<details><summary>↩ Tool result · `toolu_01MMRRLmTQ7E8N9NRi9xrREL`</summary>

```text
I appreciate the request, but I need to be transparent about what I'm encountering: the provided content appears to be a binary PDF file (containing compressed streams, object definitions, and encoded image data) rather than human-readable text.

The content shows PDF structure markers like:
- `%PDF-1.5` header
- Object definitions (`obj`, `endobj`)
- Compression filters (`/FlateDecode`)
- Stream data (binary/compressed content)

**I cannot extract the paper's actual content** because:

1. The text is encoded/compressed in PDF binary format, not plain text
2. Decompressing and rendering PDF content to extract text requires specialized PDF parsing
3. I don't have the capability to decompress `/FlateDecode` streams or interpret PDF objects

**What I recommend:**

- **If you have the PDF file**: Use a PDF extraction tool (pdftotext, PyPDF2, or your PDF reader's export function) to convert it to text first
- **Then share the extracted text**, and I can happily:
  - Pull the introduction verbatim (within 125-character quote limits)
  - Extract contribution statements
  - Summarize methods, experiments, results
  - List datasets, baselines, metrics
  - Capture training details and citations

Would you be able to provide the paper content in plain text format, or share the paper title/source so I can assist differently?

[Binary content (application/pdf, 1021.3KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-distiller-3275b75a/e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae/tool-results/webfetch-1779289305252-kvs15v.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3456f01d-53a9-4ea1-9419-a8a30bbb2e5a",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "fdc8d990-42ea-4dcc-b689-5bbf0a6436b0",
  "sourceToolAssistantUUID": "3456f01d-53a9-4ea1-9419-a8a30bbb2e5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-20T15:01:55.306Z_

The PDF was saved locally. Let me extract text from it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdc8d990-42ea-4dcc-b689-5bbf0a6436b0",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2GKGfxfbSf1b7tV2v6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94642591-d442-4bf8-a8a7-24215a482790",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BAiEBhXeAoF7xERa6bFJqg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 21891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 693,
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

_source line 17 · 2026-05-20T15:01:56.757Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Dvex1kNi9bKc1XB8tf4QEo`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-distiller-3275b75a/e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae/tool-results/webfetch-1779289305252-kvs15v.pdf /tmp/strong_model_collapse.txt && wc -l /tmp/strong_model_collapse.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94642591-d442-4bf8-a8a7-24215a482790",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2GKGfxfbSf1b7tV2v6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af314c96-0837-46e6-8674-0b9651004b3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BAiEBhXeAoF7xERa6bFJqg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 21891,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 693
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 21891,
          "cache_creation_input_tokens": 693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 693,
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

_source line 18 · 2026-05-20T15:01:57.230Z_

<details><summary>↩ Tool result · `toolu_01Dvex1kNi9bKc1XB8tf4QEo`</summary>

```text
3470 /tmp/strong_model_collapse.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af314c96-0837-46e6-8674-0b9651004b3b",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "4dc64509-9f46-4a8b-bfff-c1fec8c32254",
  "sourceToolAssistantUUID": "af314c96-0837-46e6-8674-0b9651004b3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T15:01:59.731Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X3QGdbRCFQazA9Xv91HeNC`</summary>

```json
{
  "file_path": "/tmp/strong_model_collapse.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dc64509-9f46-4a8b-bfff-c1fec8c32254",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2GeUaJWGjx3xwsDpcY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15c78df8-d62e-45b1-a4c0-cc360fa2941b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01J1TEtxj3yxtrV78nWi7eF9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 22584,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 223
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 22584,
          "cache_creation_input_tokens": 223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 223,
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

_source line 20 · 2026-05-20T15:01:59.739Z_

<details><summary>↩ Tool result · `toolu_01X3QGdbRCFQazA9Xv91HeNC`</summary>

```text
1	Strong Model Collapse
2	Elvis Dohmatob1
3	Yunzhen Feng1,2,∗
4	Arjun Subramonian1,4,∗
5	Julia Kempe1,2,3
6	
7	e.dohmatob@meta.com
8	yf2231@nyu.edu
9	arjunsub@cs.ucla.edu
10	kempe@meta.com
11	
12	arXiv:2410.04840v2 [cs.LG] 8 Oct 2024
13	
14	1 FAIR, Meta
15	2 NYU Center for Data Science
16	3 NYU Courant Institute
17	4 UCLA
18	∗ work done while interning at Meta
19	
20	Abstract
21	Within the scaling laws paradigm, which underpins the training of large neural
22	networks like ChatGPT and Llama, we consider a supervised regression setting
23	and establish the existance of a strong form of the model collapse phenomenon,
24	a critical performance degradation due to synthetic data in the training corpus.
25	Our results show that even the smallest fraction of synthetic data (e.g., as little
26	as 1% of the total training dataset) can still lead to model collapse: larger and
27	larger training sets do not enhance performance. We further investigate whether
28	increasing model size, an approach aligned with current trends in training large
29	language models, exacerbates or mitigates model collapse. In a simplified regime
30	where neural networks are approximated via random projections of tunable size,
31	we both theoretically and empirically show that larger models can amplify model
32	collapse. Interestingly, our theory also indicates that, beyond the interpolation
33	threshold (which can be extremely high for very large datasets), larger models
34	may mitigate the collapse, although they do not entirely prevent it. Our theoretical
35	findings are empirically verified through experiments on language models and
36	feed-forward neural networks for images.
37	
38	1
39	
40	Introduction
41	
42	The term Model Collapse refers to a critical degradation in the performance of AI models, particularly when a significant portion of their training data consists of synthetic data generated by other
43	models. As detailed in Shumailov et al. (2023), this phenomenon arises as the model gradually overfits to patterns found in synthetic data, which may not fully represent the richness or variability of
44	real-world data. Over successive training cycles, this feedback loop results in the model reinforcing
45	errors, biases, or oversimplifications from the synthetic data. Consequently, the model’s ability to
46	generalize to real-world data is compromised, as it increasingly relies on the distorted distribution
47	provided by prior AI generations rather than learning accurate representations of the real world.
48	This phenomenon was observed empirically (Hataya et al., 2023; Martı́nez et al., 2023a,b; Bohacek
49	& Farid, 2023; Briesch et al., 2023; Guo et al., 2023) and described theoretically (Alemohammad
50	et al., 2023; Bertrand et al., 2023; Dohmatob et al., 2024a,b). The connection to the breakdown
51	of neural scaling laws (Kaplan et al., 2020) has been pointed out and analyzed in Dohmatob et al.
52	(2024b): as data becomes more synthetic, larger training sets do not enhance performance.
53	The issue is especially concerning in large-scale AI systems like ChatGPT and Llama (Touvron
54	et al., 2023; Dubey & et al., 2024), which rely heavily on vast amounts of training data to maintain
55	their performance. If synthetic data is used in training these models, even in small quantities, the
56	model can start producing “gibberish” or nonsensical outputs, contains misinformation, or reflect
57	stereotypes. This is because the model effectively starts to amplify its own mistakes (Shumailov
58	et al., 2024). This feedback loop results in a gradual loss of model fidelity, reducing its ability to
59	generalize or adapt to new, unseen test environments.
60	1
61	
62	1.1
63	
64	Main Contributions
65	
66	In this work, we establish a series of results which shed more light on model collapse, bringing the
67	phenomenon closer to a solid theoretical foundation. We consider the following important questions:
68	(Q1) Is model collapse inevitable or can it be fixed by strategically mixing synthetic and real data?
69	(Q2) Are larger models more prone to model collapse than smaller ones?
70	Our theoretical analysis focuses on the solvable setting of linear regression with and without random
71	projections, with the latter serving as an approximation of neural networks by means of random
72	feature maps (Maloney et al., 2022; Bach, 2023). Also, in accordance with the current “neural
73	scaling laws” paradigm (Kaplan et al., 2020; Hoffmann et al., 2022) whichs underlies the training
74	of LLMs, where models and dataset sizes become larger over time, we focus on the setup where the
75	total amount of data (synthetic + real data) used for training grows arbitrarily.
76	Let us summarize our main findings.
77	
78	Test error (train on real + synth.)
79	
80	Result #1: Strong Model Collapse. First, we establish a robust negative result which shows that
81	model collapse generally persists even when mixing real and synthetic data, as long as the fraction
82	of training data which is synthetic does not vanish (cf. Section 3.1 and 3.2). By synthetic data, we
83	mean any training data from a distribution which deviates from the distribution of real data, i.e. data
84	on which the test performance is evaluated. Thus, model collapse cannot generally be mitigated by
85	simple adjustments such as data weighting (Jain et al., 2024; Ferbach et al., 2024) unless these strategies asymptotically remove all but a vanishing proportion of synthetic data from the training process
86	(Section 5). Our results show that the findings of Shumailov et al. (2024); Alemohammad et al.
87	(2023); Bertrand et al. (2023); Dohmatob et al. (2024a,c) are worse than anticipated, by considering
88	the more realistic scenario where a mixture of synthetic and real data is used for training.
89	synthetic dataset size n2 = 50
90	
91	synthetic dataset size n2 = 200
92	30
93	
94	synthetic dataset size n2 = 400 loge ( )
95	0.6
96	0.4
97	
98	30
99	
100	0.2
101	
102	31
103	31
104	
105	0.2 0.3 0.4 0.5 0.6
106	Test error (train on real data only)
107	
108	32
109	
110	0.0
111	
112	31
113	
114	0.2 0.3 0.4 0.5 0.6
115	Test error (train on real data only)
116	
117	32
118	
119	0.2
120	0.4
121	0.2 0.3 0.4 0.5 0.6
122	Test error (train on real data only)
123	
124	Figure 1: Pareto diagram: Understanding the role of model size in model collapse. We compare the test
125	error (on the real / true data distribution), for a random projections model (equation (5) of Section 2.2) when
126	training is done on a mix of synthetic and real data (y-axis), versus real data only (x-axis); in both cases, the
127	total amount of training data is fixed to n = 500. On the scatter plots, square points correspond to very highquality synthetic data (i.e from a distribution which is close to the true data distribution), diamonds correspond
128	to high-quality synthetic data, triangles correspond to low-quality, while stars correspond to very low-quality
129	synthetic data. The black lines correspond to the Pareto frontiers for each level of quality of the synthetic data;
130	the higher the frontier above the diagonal in the given setting, the more serious is the model collapse. The
131	colorbar is the log of parametrization rate ψ = m/n, where m captures is the size of the model.
132	– Result #2: Model Size and Model Collapse. In Section 3.2, we disentangle the effect of a model’s
133	size on its ability to cope with model collapse. We show that in general, bigger models will suffer
134	more from model collapse as soon as the deviation between the distribution of the synthetic data
135	and real data is significant. Crucially, our theory also predicts that past the interpolation threshold
136	point, this tendency can be reversed: large models become more robust to model collapse. Put
137	together, these results predict the existence of a double-descent curve regarding the model collapse
138	phenomenon. This is illustrated in Figures 1 and 2. Thus, the model collapse profile depends
139	critically on design choices like model size.
140	Experimental Validation.
141	
142	Our theoretical results are empirically confirmed with experiments in :
143	
144	• Toy settings, including random projections model on Gaussian data, and shallow networks fully
145	trained on the MNIST dataset (Deng, 2012). Refer to the end of Section 3.2 and Appendix ??.
146	2
147	
148	• Realistic setting of GPT-2 models trained on BabiStories (Zhang et al., 2024a), a reproduction
149	of TinyStories (Eldan & Li, 2023) using the Mixtral-8x7B open language model (Jiang et al.,
150	2024)). Refer to Section 4.
151	Approach. From a technical standpoint, our theoretical analysis focuses on regression problems
152	in the classical linear setting introduced in Dohmatob et al. (2024a) for studying model collapse,
153	and also the setting of neural networks in a simplified regime which can be approximated by random projections (Maloney et al., 2022; Bach, 2023). We employ the tools of operator-valued free
154	probability theory (OVFPT) (Mingo & Speicher, 2017) to obtain a new bias-variance decomposition
155	Etest ≃ B + V + ζ, of the test error evaluated on the real / true data distribution, of a model trained
156	on a mixture of real and synthetic data. The extra term ζ then induces model collapse.
157	1.0
158	0.8
159	0.5
160	0.2
161	0.0
162	
163	Bias B
164	c2
165	0.0
166	0.1
167	0.5
168	1.0
169	
170	0
171	
172	250 500 750 1000
173	
174	Network width m
175	
176	1.0
177	0.8
178	0.5
179	0.2
180	0.0
181	
182	Variance V
183	
184	0
185	
186	250 500 750 1000
187	
188	Extra term
189	
190	6.0
191	4.0
192	
193	4.0
194	
195	2.0
196	
197	2.0
198	
199	0.0
200	
201	Network width m
202	
203	0
204	
205	250 500 750 1000
206	
207	Network width m
208	
209	Test error Etest
210	
211	6.0
212	
213	0.0
214	
215	0
216	
217	250 500 750 1000
218	
219	Network width m
220	
221	Figure 2: Illustration of our new bias-variance decomposition Etest ≃ B + V + ζ for neural networks
222	in the simplified random projections regime (cf. Section 3.2), trained on a mixture of real and synthetic data.
223	The sum B + V corresponds to the classical bias variance decomposition in this setup when all the training
224	data is real. The extra term ζ is responsible for model collapse when training is done on a mixture of real and
225	synthetic data. The scalar c2 characterizes the quality of the synthetic data (cf. Definition 1), via its mismatch
226	with the real data distribution. The vertical line corresponds to the interpolation threshold m = n, where m is
227	the model size and n is the total sample size. Notice the well-known double-descent curve in the bias curve.
228	
229	1.2
230	
231	Related Work
232	
233	The theoretical study of model collapse in the setting of high-dimensional supervised-learning with
234	linear regression and kernel ridge regression was initiated in Dohmatob et al. (2024a). This work
235	derives analytical formulas that quantitatively describe iterative retraining on synthetic data in both
236	under-parameterized and over-parameterized regimes, considering both low- and high-dimensional
237	asymptotics. It places itself within an important body of works studying kernel ridge regression
238	(on “clean” data), which serves as an effective proxy for neural networks in various regimes, for
239	instance in the infinite-width limit (Neal, 1996; Williams, 1996; Jacot et al., 2018; Lee et al., 2018)
240	or in the lazy regime of training (Chizat et al., 2019) and are a testbed to study interesting phenomena
241	observed in deep learning. For instance, Rahimi & Recht (2008); Rudi & Rosasco (2017); Maloney
242	et al. (2022) study scaling laws for regression in the random feature model and Bach (2023) analyses
243	double descent in this setting. Scaling laws have been shown for kernel models under the Gaussian
244	design, e.g. in Caponnetto & de Vito (2007); Spigler et al. (2020); Cui et al. (2022) for regression
245	and Cui et al. (2023) for classification.
246	Very few theoretical works tackle the analysis of models trained on mixtures of original (real /
247	clean) and synthetic data. Bertrand et al. (2023) analyze the training process at the distribution level
248	and provide stability results under a locality assumption in parameter space. Seddik et al. (2024)
249	analyze the mixing of discrete original and synthetic data, and provide upper bounds on the amount
250	of synthetic data that can be included to avoid model collapse. Let us also mention the recent works
251	(Jain et al., 2024; Ferbach et al., 2024) which are potential methods for mitigating model collapse.
252	Jain et al. (2024) analyze linear regression on isotropic Gaussian data for mixtures of clean and
253	synthetic data by minizing a strategically weighted sum of losses (one term for each data source,
254	real and synthetic), while Ferbach et al. (2024) can be seen as a multi-step version thereof where at
255	each stage, the synthetic data generator is distilled by interpolating with real data. These methods
256	are analyzed in Section 5, where we outline their shortcomings regarding model collapse.
257	Finally, a few works go beyond the mixing scenario and analyze how to curate or filter synthetic
258	data to avoid model collapse (Feng et al., 2024; Zhang et al., 2024b; Alemohammad et al., 2024),
259	but a rigorous study of their effectiveness is still lacking.
260	3
261	
262	2
263	
264	Theoretical Setup
265	
266	2.1
267	
268	Data Distributions
269	
270	Consider an iid sample from D1 = {(xi , yi ) | 1 ≤ i ≤ n1 } of size n1 from the true data distribution
271	P1 and an independent iid sample D2 = {(xi , yi ) | n1 + 1 ≤ i ≤ n} of size n2 from another data
272	distribution P2 (which we shall hereafter call the synthetic data distribution), where n := n1 + n2
273	is the total amount of training data. Here, Pk = PΣk ,wk∗ ,σk2 is the distribution on Rd × R given by
274	(Features) x ∼ N (0, Σk ),
275	(Labels) y = x⊤ wk∗ + ϵ, with ϵ ∼ N (0, σk2 ) independent of x.
276	
277	(1)
278	
279	Each Σk is a d × d positive-definite covariance matrix which captures the intrinsic variations of the
280	input feature vector x. The σk ’s control the level of label noise in each distribution.
281	Structure of the Label Shift. For conciseness, we will assume the following priors on the wk∗ ’s
282	• True labelling function: w1∗ ∼ N (0, Γ),
283	• Mismatch between real and synthetic: δ := w2∗ − w1∗ ∼ N (0, ∆), independent of w1∗ ,
284	for some d × d positive-semidefinite matrices Γ and ∆.
285	Remark 1. To ease the presentation of our results, we shall assume that the matrices Σ1 , Σ2 , Γ, and
286	∆ are diagonal matrices, and therefore commute. Furthermore, except otherwise explicitly stated,
287	we shall assume equal covariance matrices, and take Σ1 = Σ2 = Σ as in Dohmatob et al. (2024a).
288	The matrix Γ captures the structure of the ground-truth labelling function in the real / test distribution
289	P1 . Together with the label-noise levels σ12 and σ22 , the matrix ∆ = cov(w2∗ − w1∗ ) captures the
290	covariance structure of the disparity between the true data distribution P1 and the synthetic data
291	distribution P2 regarding the conditional distribution p(y|x); the marginal distribution of x stays the
292	same under P1 and P2 due the assumption Σ1 = Σ2 = Σ. For example, the self-consuming-loops
293	setup of Dohmatob et al. (2024a) corresponds to taking ∆ proportional to the precision matrix of
294	the input features Σ−1 . Thus, the size of the fluctuations of each component δj of the difference
295	w2∗ − w1∗ is inversely proportional to the standard deviation of the corresponding feature. Another
296	important setup is the case where the fluctuations are isotropic, i.e taking ∆ ∝ Id .
297	Quality of Synthetic Data. Due to the a priori general structure of ∆, the label corresponding to
298	an input x will be different for both distributions, even in the absence of label-noise. On average, the
299	L2 -norm of this difference is Ew1∗ ,w2∗ Ex∼N (0,Σ) [(x⊤ w1∗ − x⊤ w2∗ )2 ] = tr Σ∆. We therefore define
300	Definition 1. The quality of synthetic data is defined as c2 (∆) = (1/d) tr Σ∆, which captures the
301	disparity between the synthetic data distribution P2 and the real data distribution P1 (small values
302	of c2 (∆) are better). For example, if ∆ = c2 Σ−1 as in Dohmatob et al. (2024a), then c2 (∆) = c2 .
303	2.2
304	
305	Models and Performance Measure
306	
307	Given this training data, the goal of a learner is to construct an estimator b
308	w. This can be seen as a
309	linear model from x 7→ x⊤ b
310	w. Evaluated on the real / true data distribution P1 (which coincides with
311	the distribution from which the real component D1 of the training dataset D is drawn), the test error
312	of a model fb : Rd → R is defined by
313	Etest (fb) = ED Ex∼N (0,Σ1 ) [(fb(x) − x⊤ w1∗ )2 ].
314	
315	(2)
316	
317	This will be our main object of study, for different models fb. The outermost expectation ED is to
318	quench the randomness in the training dataset D used to train the model.
319	We consider two families of analytically tractable models: (1) classical linear models obtained via
320	penalized regression in the input space, and (2) models obtained via penalized regression in a feature
321	space given by random projections. The latter allows us to study the role of model size in model
322	collapse, by varying the output dimension of the random projection mapping. This output dimension
323	m controls the size of a neural network in a simplified regime (Maloney et al., 2022; Bach, 2023).
324	4
325	
326	(1) Classical Linear Model. We start with a setup motivated by Dohmatob et al. (2024a). We are
327	interested in the penalized linear model (ridge) fbCL : x 7→ x⊤ w
328	b with parameter vector w
329	b given by
330	n
331	
332	1X ⊤
333	(xi w − yi )2 + λ∥w∥2 ,
334	d
335	w∈R n
336	i=1
337	
338	w
339	b = arg min
340	
341	(3)
342	
343	trained on the total dataset D = D1 ∪ D2 . Of course, the unregularized limit λ → 0+ corresponds to
344	ordinary least-squares (OLS). We shall work in the following so-called proportionate scaling limit
345	(Proportionate Scaling Limit for Classical Linear Model) For fixed ϕ ∈ (0, ∞), p2 ∈ (0, 1),
346	d, n, n1 , n2 → ∞,
347	
348	n2 /n → p2 ,
349	
350	n1 /n → p1 = 1 − p2 ,
351	
352	d/n → ϕ.
353	
354	(4)
355	
356	The extreme cases p1 → 0+ and p2 → 0+ correspond to training on only synthetic (resp. real) data.
357	In particular, p1 → 0+ corresponds to the setting considered in Dohmatob et al. (2024a). Note that
358	in the isotropic setting where Σ ∝ Id , ϕ controls the speed of learning on clean data. Indeed, for
359	small ϕ, the scaling law in this case is known (Hastie et al., 2022) to be Etest ≃ σ12 ϕ + O(ϕ2 ). As
360	we shall see (Corollary 1), this scaling law gets deformed in the presence of synthetic data in the
361	training dataset, leading to model collapse.
362	(2) Random Projections Model. We consider neural networks in a simplified regime which can
363	be approximated via random projections (Maloney et al., 2022; Bach, 2023), i.e f (x) = v ⊤ Sx.
364	Here, S is a d × m random matrix with iid entries from N (0, 1/d); it maps an input-vector x ∈ Rd
365	to a random feature vector z = Φ(x) := Sx ∈ Rm . Only the “read-out” weights v ∈ Rk are
366	learned, by fitting on the dataset D. Consider the model fbRP : x 7→ Φ(x)⊤ vb, where vb is given by
367	n
368	
369	vb = arg minm
370	v∈R
371	
372	1X
373	(Φ(xi )⊤ v − yi )2 + λ∥v∥22 .
374	n i=1
375	
376	(5)
377	
378	Note that such a simplified neural network model has been proposed in the literature as a theoretical
379	testbed for studying intriguing properties of neural networks, like scaling laws (Maloney et al.,
380	2022) and double-descent (Bach, 2023). Also see Section 1.2. It can be shown that the extreme case
381	m/n → ∞ reduces to the classical linear model.
382	We shall work in the following asymptotic regime:
383	(Proportionate Scaling Limit for Random Projections Model)
384	d, m, n, n1 , n2 → ∞,
385	
386	n1 /n → p1 , n2 /n → p2 ,
387	
388	d/n → ϕ, m/d → γ, m/n → ψ,
389	
390	(6)
391	
392	for some constants ϕ, γ, ψ ∈ (0, ∞) and p1 , p2 ∈ (0, 1), with p1 + p2 = 1 and ψ = ϕγ.
393	Note that the ratio ψ/ϕ ≃ md captures the size of the network, though the number of trainable
394	parameters (the read-out layer) is m ≃ γd.
395	
396	3 A New Bias-Variance Decomposition and
397	the Emergence of Strong Model Collapse
398	3.1
399	
400	Classical Linear Models
401	
402	We begin with an analysis of the test error Etest (fbCL ) for the classical linear model defined in
403	(3) trained on a mixture of synthetic and true / real data, but evaluated on test data from the true
404	data distribution only. We will establish a new bias-variance decomposition with an additional term
405	which quantitatively reveals the emergence of model collapse (Shumailov et al., 2023, 2024).
406	Let us first recall some standard notations. Denote by κ = κ(n, λ; Σ) the unique positive solution
407	to the fixed-point equation
408	κ − λ = κ df 1 (κ; Σ)/n, with df k (t; Σ) := tr Σk (Σ + tId )−k .
409	5
410	
411	(7)
412	
413	Also define u = u(n, λ; Σ) ≥ 0 as follows
414	u :=
415	
416	df 2 (κ; Σ)/n
417	.
418	1 − df 2 (κ; Σ)/n
419	
420	(8)
421	
422	The following result (proved in the appendix, alongside all other theoretical results in this work)
423	will be exploited in the sequel to show that the use of synthetic data in model training can lead to
424	catastrophic effects regarding test error.
425	Theorem 1. Define σ 2 := p1 σ12 + p2 σ22 and let κ, u ≥ 0 be as previously constructed. In the
426	proportionate scaling limit (4), the test error w.r.t the true data distribution P1 , of the classical
427	linear model fbCL defined in (3) is given by Etest (fbCL ) ≃ E + ζ, with
428	E = B + V,
429	
430	V = σ2
431	
432	df 2 (κ; Σ)/n
433	,
434	1 − df 2 (κ; Σ)/n
435	
436	B = κ2
437	
438	tr ΓΣ(Σ + κId )−2
439	,
440	1 − df 2 (κ; Σ)/n
441	
442	ζ = p22 · (1 + p1 u) tr ∆Σ3 (Σ + κId )−2 + p2 u tr ∆Σ(p1 Σ + κId )2 (Σ + κId )−2 .
443	
444	(9)
445	(10)
446	
447	Note that for ∆ = 0 (i.e w2∗ = w1∗ ), which corresponds to assuming that the real data and the
448	surrogate data have the same distribution, the above theorem gives Etest (fbCL ) ≃ E ≃ B +V which
449	is the classical bias-variance decomposition (Hastie et al., 2022; Richards et al., 2021) for ridge
450	regression on n samples from the distribution PΣ,w1∗ ,σ2 . The extra term ζ appearing in Theorem 1
451	is responsible for model collapse! In Appendix B.2, we show how Theorem 1 recovers the main
452	results of Dohmatob et al. (2024a) for special choices of the displacement matrix ∆.
453	Strong Model Collapse. In particular, in the “scaling laws” regime where ϕ → 0+ , it holds that
454	ζ ≃ p22 tr ∆. In this case, if tr ∆ remains bounded away from zero, then so is ζ unless p2 → 0+ ,
455	i.e we discard all synthetic data from the training dataset. This is strong model collapse. It hints
456	that model collapse as exposed by Shumailov et al. (2023, 2024); Hataya et al. (2023); Martı́nez
457	et al. (2023a,b); Bohacek & Farid (2023); Briesch et al. (2023); Guo et al. (2023) cannot be fixed by
458	naively mixing synthetic and real data during training. We show in Section 3.2 that this observation
459	continues to hold in the setting of random projections model fbRP defined in (5). Finally, in Section 5
460	we study what happens when the synthetic data and real data are strategically mixed during training.
461	Proving Theorem 1. It turns out that the analysis of the classical linear model’s test error
462	Etest (fbCL ) in Theorem 1 amounts to the analysis of the trace of rational functions of sums of
463	random matrices. Although the limiting spectral density of sums of random matrices is a classical computation using subordination techniques (Marčenko & Pastur, 1967; Kargin, 2015), this is
464	not enough for the full analysis; a more involved analysis is required. This difficulty will be even
465	greater in the setting of random projections fbRP . To the rescue, in Appendix D we shall employ
466	operator-valued free probability theory (OVFPT) to compute the exact high-dimensional limits of
467	such quantities. The tools of OVFPT have been used in the recent machine learning theory literature to obtain precise asymptotics for the test error of neural networks (trained on real data only) in
468	various linearized settings (Adlam & Pennington, 2020; Tripuraneni et al., 2021; Lee et al., 2023).
469	Example: The Isotropic Case. To help unpack Theorem 1, consider the following concrete setup
470	Σ = Id , Γ = (r2 /d)Id , ∆ = (c2 /d)Id ,
471	for some constants r, c > 0. The constant c2 captures how close the distribution of the synthetic
472	data P1 is to the distribution of the real data P1 ; thus it captures the quality of the synthetic data.
473	This gives u ≃ ϕ/((1 + κ)2 − ϕ), where κ > 0 uniquely satisfies the fixed-point equation κ − λ =
474	κϕ/(1 + κ); this is a quadratic equation that characterizes the well-known Marchenko-Pastur law
475	(Marčenko & Pastur, 1967). The quantities appearing in the formulae presented in Theorem 1 then
476	take the following simple forms: V = σ 2 ϕ/((1 + κ)2 − ϕ) and B = κ2 r2 /((1 + κ)2 − ϕ), and
477	
478	ζ = p2 (1 + p1 u) + (p1 + κ)2 u p2 c2 /(1 + κ)2 .
479	In particular, in the unregularized limit λ → 0+ corresponding to OLS, we get κ → (ϕ − 1)+ .
480	To further make things concrete, consider the under-parametrized case where ϕ ∈ (0, 1) in the
481	proportionate scaling regime (4). The over-parametrized case ϕ ∈ (1, ∞) is treated in Appendix
482	B.1. We deduce the following corollary to Theorem 1.
483	6
484	
485	Corollary 1. Suppose ϕ ∈ (0, 1). Then, in the limit (4) and λ → 0+ , the test error with respect to
486	the true data distribution P1 , of the classical linear model fbCL defined in (3) is given by
487	
488	Etest (fbCL ) ≃ σ 2 ϕ/(1 − ϕ) + p22 + p2 p1 ϕ/(1 − ϕ) c2 .
489	(11)
490	Moreover, for fixed c > 0 and small ϕ ∈ (0, 1), it holds that
491	Etest (fbCL ) ≃ σ 2 d/n + p22 c2 + O(ϕ2 ).
492	
493	(12)
494	
495	2
496	
497	In particular, if c = Ω(1), i.e bounded away from zero (corresponding to low-quality synthetic
498	data), then Etest (fbCL ) = Ω(p22 c2 ): the scaling law plateaus unless p2 → 0+ , i.e unless all but a
499	vanishing proportion of synthetic data is discarded from the training dataset.
500	The result is empirically illustrated in Figure 3, where we see that even a small amount of low-quality
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15c78df8-d62e-45b1-a4c0-cc360fa2941b",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "55ae51bb-572a-4ee0-8a39-bead5d30dd81",
  "sourceToolAssistantUUID": "15c78df8-d62e-45b1-a4c0-cc360fa2941b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T15:02:03.181Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PCtrhF73jwMQJr81MaBPXx`</summary>

```json
{
  "file_path": "/tmp/strong_model_collapse.txt",
  "limit": 500,
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55ae51bb-572a-4ee0-8a39-bead5d30dd81",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2GqFE1VFsPv1uHqCKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f29d59e8-796b-40bb-84c9-9f2c3a2a3a9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HvvJW9wtmB71rFTGRAdWxn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8910,
      "cache_read_input_tokens": 22807,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 22807,
          "cache_creation_input_tokens": 8910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8910,
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

_source line 22 · 2026-05-20T15:02:03.200Z_

<details><summary>↩ Tool result · `toolu_01PCtrhF73jwMQJr81MaBPXx`</summary>

```text
500	The result is empirically illustrated in Figure 3, where we see that even a small amount of low-quality
501	synthetic data is enough to cause model collapse, whereby the test error of the model deviates from
502	a perfect diagonal (ideal scaling law, corresponding to p2 = 0, i.e training on real data only).
503	
504	Figure 3: Strong model collapse in classical linear model (empirical confirmation of Corollary 1). The
505	training dataset comprises of n = n1 + n2 samples from a mixture of n2 = p2 n synthetic samples and n1 =
506	n − n2 real samples. The real samples are from the same distribution as the real / true samples of the training
507	dataset, while the synthetic samples are from a distribution with the same covariance structure and label noise
508	level σ = 1, but an incorrect labelling function (epistemic error). The quality of the synthetic data is controlled
509	by the scalar c, with c → 0 corresponding to synthetic data of perfect quality (higher values correspond to
510	lower quality synthetic data). Solid curves correspond to experiments, and broken curves correspond to our
511	theoretical predictions of Corollary 1; notice the perfect match. We see that even a small amount of low-quality
512	synthetic data is enough to cause model collapse, whereby the test error of the model deviates from a perfect
513	diagonal (ideal scaling law, corresponding to p2 = 0, i.e training on real data only).
514	Remark 2. Corollary 1 can be extended to the the non-isotropic case, but the statement is much
515	longer and is thus omitted here.
516	3.2
517	
518	Random Projections Model
519	
520	We now turn to the more challenging setting of the random projections model fbRP given in (5). As
521	mentioned before (cf. Section 2.2), such models are considered in our work as a simplification of
522	the high-dimensional dynamics of actual neural networks, which still allows us to capture the effect
523	of model size in the model collapse phenomenon.
524	We will need the following scalars which capture the high-dimensional statistics of the model fbRP .
525	Definition 2. Let (e, τ ) be the unique positive solution to the following fixed-point equations
526	¯ K0 K −1 , with K0 := eΣ, K := γτ K0 + λId ,
527	1/e = 1 + ψτ ¯
528	tr ΣK −1 , 1/τ = 1 + tr
529	¯ A := tr A/d is the normalized trace operator. Also define (u, ω) by the equations
530	where tr
531	
532	(13)
533	
534	¯ Σ1 (γτ 2 L′ + ωId )K −2 , ω = τ 2 tr
535	¯ (γωK02 + λ2 L′ )K −2 , with L′ := (1 + u)Σ. (14)
536	u = ψe2 tr
537	Finally, define the following auxiliary scalars θ := λ/(γτ e) > 0 and ω ′ := ω/(γτ 2 ) > 0.
538	As usual, we denote σ 2 := p1 σ12 + p2 σ22 . Also, for any p ∈ [0, 1] define a d × d positive definite
539	matrix T (θ; p) := pΣ + θId , and T (θ) := T (θ; p)|p=1 = Σ + θId .
540	The following result is a nontrivial extension of Theorem 1 to the case of random projections.
541	7
542	
543	Theorem 2. In the proportionate scaling limit (6), the test error w.r.t the true data distribution P1 ,
544	of the random projections model fbRP defined in (5) is given by Etest (fbRP ) ≃ E + ζ, with
545	E ≃ B + V, where B = (1 + u)θ2 tr ΓΣT (θ)−2 + ω ′ tr ΓΣ2 T (θ)−2 ,
546	
547	V = tr Σ2 T (θ)−2 + (ω ′ − θu) tr ΣT (θ)−2 σ 2 /e ,
548	
549	(15)
550	
551	ζ = p22 (1 + p1 u) tr ∆Σ3 T (θ)−2 + p2 ω ′ tr ∆Σ2 T (θ)−2 + p2 u tr ∆ΣT (θ; p1 )2 T (θ)−2 .
552	Special Cases of Theorem 2 In the limit p2 → 0+ (i.e., no synthetic data; all the training data is
553	real), ζ → 0 in Theorem 2, and we recover the main result of Bach (2023) as a special case, namely
554	Etest (fbRP ) ≃ B + V , with B and V as given in the theorem. Note that even in this special case, our
555	result is more general since it covers the entire regularization path while the formulae in Bach (2023)
556	are only for the unregularized case λ → 0+ . On the other hand, Theorem 2 is a generalization of
557	Theorem 1, as can be seen by taking ψ → ∞. Refer to Appendix F.3 for details.
558	3.3
559	
560	Some Consequences of Theorem 2
561	
562	We now explore a few important consequences of Theorem 2.
563	A Double-Descent Curve. The bias-variance decomposition presented in Theorem 2 is empirically illustrated in Figures 2 and 5 for the Gaussian setting (1) (see Appendix A.1 for details on
564	the experimental setup). Notice the perfect match with experiments. The shape of the bias curve
565	in Figure 2 (leftmost plot) is reminiscent of the well-known double-descent (Bach, 2023) in the unregularized setting λ → 0+ . The divergence at the interpolation threshold m = n (i.e. ψ = 1) is
566	because the bias term B, the variance term V , and the extra term ζ (responsible for model collapse)
567	all diverge to infinity at this point.
568	Strong Model Collapse. Observe that the first term in the expression for ζ given in Theorem 2 is
569	lower-bounded by p22 tr ∆Σ3 (Σ + θId )−2 , which scales linearly with the square of the proportion
570	p2 ≃ n2 /n of synthetic data in the training dataset D. However, unless p2 → 0+ , i.e unless
571	the proportion p2 of synthetic data in the training dataset vanishes, the performance of the model
572	eventually plateaus above the baseline E (corresponding to the setting where all training data is real,
573	i.e no synthetic data in training dataset). This is strong model collapse.
574	Since the factor tr ∆Σ3 (Σ + θId )−2 only depends on the design choices of the model (via the scalar
575	θ defined previously), we expect that different design choices (e.g., model size) will lead to different
576	model collapse profiles. Figure 4 shows results for different proportions of synthetic data and various
577	values of the quality parameters c2 (cf. Definition 1), and also different model sizes m, in the toy
578	setting of multivariate Gaussians with random projections (experimental details in Section A.1).
579	c2 = 0.0
580	
581	Test error
582	
583	2.0
584	
585	p2
586	0.02
587	0.1
588	0.2
589	0.4
590	0.6
591	0.8
592	
593	1.5
594	1.0
595	0.5
596	0.0
597	
598	0
599	
600	200 400 600 800 1000
601	
602	Network width m
603	
604	c2 = 0.1
605	
606	2.0
607	
608	c2 = 0.5
609	
610	5
611	4
612	
613	4
614	
615	3
616	
617	3
618	
619	2
620	
621	2
622	
623	0.5
624	
625	1
626	
627	1
628	
629	0.0
630	
631	0
632	
633	1.5
634	1.0
635	
636	0
637	
638	200 400 600 800 1000
639	
640	Network width m
641	
642	0
643	
644	200 400 600 800 1000
645	
646	Network width m
647	
648	c2 = 1.0
649	
650	5
651	
652	0
653	
654	0
655	
656	200 400 600 800 1000
657	
658	Network width m
659	
660	Figure 4: Impact of model size (network width m) on model collapse. For various levels of data quality
661	
662	c2 (cf. Definition 1) we show test error as a function of model size for various mixing ratios (darker curves
663	correspond to higher fractions p2 of synthetic data). Error bars correspond to 5 independent runs.
664	
665	Are Larger Models More Prone or Less Prone to Model Collapse? Figure 1 shows the results
666	of a small experiment to investigate this. The input dimension is d = 600, and the covariance matrix
667	is identity Id (isotropic features). The total number of training examples is fixed to n = 500. The
668	∆ matrix is taken to be of the form ∆ = (c2 /d)Σ−1 (similar results are observed for different
669	covariance matrices) for different values of c2 as follows: c2 = 0 (synthetic data of very high
670	quality), represented with square markers; c2 = 0.1 (high quality synthetic data), represented with
671	8
672	
673	In the middle plot of Figure 1, size of the synthetic
674	dataset is comparable to the size of the real dataset
675	(n2 = 200 versus n1 = 300). For high-quality synthetic data, larger models are still better than smaller
676	models. However, for this setting, the frontier shifts
677	upwards and from left to right, and the optimal
678	model size is intermediate. For the rightmost plot,
679	the size of the synthetic dataset is considerably larger
680	than the real dataset (n2 = 400 versus n1 = 100).
681	The results are similar to the case n2 = 200 except
682	that the Pareto frontiers are higher over the diagonal (indicating more serious model collapse). In all
683	cases, very small models are never optimal: they are
684	not good even in the classical sense when training is
685	done only on real data, and the presence of synthetic
686	data only makes this worse.
687	
688	4
689	
690	Test error Etest
691	
692	diamonds; c2 = 0.5 (low quality), represented by triangles; and c2 = 1 (very low-quality synthetic
693	data), represented by crosses. As indicated on the figure, the leftmost plot corresponds to the regime
694	where there is much fewer synthetic than real samples (n2 = 50 synthetic samples versus n1 = 450
695	real samples). Here, for both high-quality and low-quality synthetic data (squares), the optimal
696	tradeoff is struck by larger models (i.e, larger values of ψ). For lower-quality data, the frontier shifts
697	upwards and from left to right; larger models cease being optimal for coping with model collapse
698	and the optimal model size is intermediate.
699	
700	6
701	5
702	4
703	3
704	2
705	1
706	0
707	
708	c2
709	0.0
710	0.1
711	0.5
712	1.0
713	
714	0
715	
716	250
717	500
718	750
719	Network width m
720	
721	1000
722	
723	Figure 5: Impact of model size (network width
724	m) on model collapse. As usual, solid curves
725	correspond to experimental results (5 runs), while
726	broken curves correspond to predictions of our
727	theory (here, Corollary 4). Error bars correspond
728	to 5 independent runs. Also see Figures 2 and 4.
729	
730	Experimental Results
731	
732	Our theoretical framework is developed within the context of high-dimensional linear regression
733	and random projections models using Gaussian data. We now provide evidence that our theory is
734	applicable to large-scale problems beyond Gaussian data: (1) neural networks on MNIST (Deng,
735	2012) and (2) language modelling.
736	4.1
737	
738	Experiments on Neural Networks on MNIST
739	
740	Our first departure from the confines of our theory are experiments with two-layer neural networks
741	trained on the MNIST dataset (Deng, 2012) both in the random feature model (with ReLU activations) and with fully trained networks. These experiments complement the empirical validation we
742	already provided in Figures 1, 2, 5, 4, and discussed amply at the end of Section 3.2.
743	
744	Hidden Dimension
745	100
746	400
747	1000
748	2000
749	4000
750	10000
751	
752	10 1
753	
754	MSE Loss
755	
756	Setup. For two-layer neural networks, we consider
757	two scenarios: (1) learning with a random projection
758	model as in Section 3.2, where the first layer of the
759	network is fixed randomly, and only the second layer
760	is trained, and (2) learning with a fully trainable neural network. The first setting directly corresponds to
761	our theoretical results from Section 3.2, but with ReLU
762	activation functions. In the case of fully trained neural networks in the second setting, our theory does not
763	apply directly. However, we hypothesize that the general trends observed in our asymptotic theory will still
764	hold: (1) there will be a significant model collapse,
765	which only diminishes as the fraction of synthetic data
766	approaches 0; (2) larger models will exhibit a more severe model collapse.
767	
768	6 × 10 2
769	
770	103
771	
772	104
773	
774	Number of Samples
775	
776	Figure 6: Fully trained two-layer network
777	on MNIST data. Impact of model size (hidden dimension, aka network width) on model
778	collapse. Here, the model is trained solely on
779	synthetic data (i.e p2 → 1).
780	
781	To align with the theoretical setting, we employ a
782	(multivariate) regression approach where labels are converted to one-hot vectors and the model is
783	trained using mean squared error. The synthetic labels were generated by another two-layer network,
784	with Gaussian label noise (standard deviation of 0.1) added. A validation set is used to select the
785	9
786	
787	best checkpoint, and evaluation is conducted on the test set using the clean labels. Further details of
788	the training are provided in Appendix A.2.
789	Results. Figure 7 presents the results for both random feature models (left) and fully trained neural
790	networks (right). In these experiments, we mixed synthetic and original data in the training set with
791	varying coefficients, p1 . As the proportion of synthetic data, p2 , increases, the scaling laws slow
792	down and eventually plateau. We observe a strong model collapse: only when p2 approaches 0
793	does the collapse subside. The results are consistent across both cases, validating our theoretical
794	predictions and demonstrating the applicability of our insights to more complex scenarios.
795	We also investigated how model size, specifically the hidden dimension of fully trained neural networks, affects model collapse. As shown in Figure 6, models with varying hidden dimensions were
796	trained exclusively on the synthetic dataset with p2 = 1. For training sets ranging from 10,000 to
797	50,000 samples, our results indicate that larger models are more susceptible to model collapse under
798	the same validation and evaluation protocols. Notably, all these models remain in the interpolation
799	regime, aligning with our theoretical predictions.
800	In summary, we find that the general trends observed in our asymptotic theory still hold: (1) there
801	is significant model collapse, which only diminishes as the fraction of synthetic data approaches 0;
802	(2) larger models exhibit a more severe model collapse.
803	0
804	
805	0.001
806	
807	The proportion of synthetic data, p2
808	
809	0.001
810	
811	0.005
812	
813	0.01
814	
815	0.02
816	
817	0.05
818	
819	0.1
820	
821	0.2
822	
823	0.5
824	
825	0.9
826	
827	MSE Loss
828	
829	10 1
830	
831	10 2
832	102
833	
834	103
835	
836	Number of Samples
837	
838	104
839	
840	102
841	
842	103
843	
844	104
845	
846	Number of Samples
847	
848	Figure 7: Model collapse as a function of the proportion of synthetic data. We use the MNIST dataset with
849	regression loss. Error bars correspond to 5 runs. Left, Random feature model with hidden dimension 100,000.
850	Right, Two-layer neural network of width (i.e hidden dimennsion) m = 2000.
851	
852	4.2
853	
854	Language Modeling
855	
856	We then extend our focus to tasks beyond classification, specifically language modeling with GPT-2
857	models. The BabiStories dataset (Zhang et al., 2024a), a reproduction of TinyStories (Eldan & Li,
858	2023) using the Mixtral-8x7B open language model (Jiang et al., 2024) enables us to study language
859	modeling with relatively small models in a compute-efficient and environmentally friendly way. It
860	comprises stories generated by prompting large models to create narratives in simple language that
861	a three-year-old child could understand, effectively simplifying the underlying language model.
862	Setup. We train a GPT-2-small model with 124 million parameters on the BabiStories dataset
863	as the generator. Using the same story prompts, which include the story beginning and character names, the generator creates our synthetic dataset. We then mix this synthetic dataset with the
864	original BabiStories, train, and evaluate model perplexity on a validation set derived from the original BabiStories. Detailed information on optimization and model configurations is provided in
865	Appendix A.3.
866	Impact of Synthetic Data Proportion. We investigate the effect of varying the synthetic data
867	proportion (p2 ) on the model’s scaling in Figure 8 (left). Here, the x-axis represents the number of
868	tokens used to train the model. In this experiment, the synthetic data is of high quality, as evidenced
869	by the low training loss and coherent text generations, corresponding to the small c2 (cf. Definition
870	1) case in our illustrative Figure 1. Consequently, even moderate amounts of synthetic data delay
871	10
872	
873	the progression of the scaling laws, and we expect this to eventually lead to plateaus or at least very
874	bad bad (i.e small) exponents in the final scaling laws as predicted in Dohmatob et al. (2024b) in the
875	special case of training on synthetic data only.
876	p2
877	
878	1.9 × 100
879	
880	Loss
881	
882	1.8 × 100
883	1.7 × 100
884	
885	1.6 × 100
886	1.5 × 100
887	
888	6 × 108
889	
890	109
891	
892	2 × 109
893	
894	3 × 109 4 × 109
895	
896	Number of Tokens
897	
898	2 × 100
899	
900	0.0
901	0.001
902	0.005
903	0.01
904	0.02
905	0.05
906	0.1
907	0.2
908	0.5
909	0.9
910	1.0
911	
912	Number of Layers
913	
914	1.95 × 100
915	
916	12
917	18
918	24
919	
920	1.9 × 100
921	
922	Loss
923	
924	2 × 100
925	
926	1.85 × 100
927	1.8 × 100
928	1.75 × 100
929	1.7 × 100
930	
931	1.65 × 100
932	
933	109
934	
935	1010
936	
937	Number of Tokens
938	
939	1011
940	
941	Figure 8: Results on BabiStories with GPT-2 models. Synthetic BabiStories is generated with a trained GPT2-small with the same set of prompts. (Left) Impact of the proportion of synthetic data p2 on model collapse
942	in a language model with 12 layers. (Right) Impact of model size (number of layers) on model collapse. Here
943	the model is trained on synthetic data only (i.e p2 = 1). The loss is evaluated on the TinyStories test set.
944	
945	Impact of Model Size. We next examine the impact of model size on training with synthetic data.
946	In addition to the GPT-2-small model (12 layers), we introduce two larger models: one with 18
947	layers (166 million parameters) and another with 24 layers (204 million parameters). The embedding
948	dimension and number of attention heads remain constant across all models. We generate a synthetic
949	dataset 10 times larger than the original one to support the scaling of tokens. As shown in Figure
950	8 (right), larger (deeper) models maintain a lower test loss until the dataset size increases—likely
951	exceeding the interpolation threshold—at which point smaller models begin to exhibit lower loss
952	and reduced overfitting. This aligns with the predictions of Theorem 2 (also refer to Figure 1, 2,
953	and the discussion just after the theorem), which suggest that larger models tend to amplify model
954	collapse beyond the interpolation threshold. In Figure 8, we observe this amplification when the
955	number of tokens exceeds 3 × 1010 . Conversely, the theory predicts that over-parameterized models
956	help mitigate collapse, a trend we observe when the number of tokens is below 1 × 1010 , leading to
957	improved performance of larger models.
958	
959	5
960	
961	Can Strategic Data Mixing Schemes Prevent Model Collapse?
962	
963	Having established the occurrence of strong model collapse both theoretically and empirically, we
964	now explore strategies to mitigate it and leverage synthetic data under stronger assumptions. We
965	begin by assuming clear information about the data source and consider two data mixing methods:
966	1) weighted data mixing (Jain et al., 2024), 2) strategic iterative mixing, inspired by Ferbach et al.
967	(2024).
968	5.1
969	
970	Weighted Single-Step Data Mixing
971	
972	For the purposes of studying scaling laws for learning on mixtures of real and surrogate data (e.g
973	synthetic data), the setting considered in (Jain et al., 2024) consists in the following optimization
974	problem:
975	X
976	X
977	(1 − α)
978	α
979	2
980	2
981	2
982	w
983	b = arg minn
984	(x⊤
985	(x⊤
986	(16)
987	i w − yi ) +
988	i w − yi ) + λ∥w∥ .
989	w∈R
990	n1
991	n2
992	(xi ,yi )∈D1
993	
994	(xi ,yi )∈D2
995	
996	This is an instance of weighted empirical risk minimization (Shimodaira, 2000; Vogel et al., 2021)
997	where the weight the sample weight πi is constant across each group: πi = (1 − α)n/n1 ≃ (1 −
998	α)/p1 for real samples real samples vs πi = αn/n2 ≃ α/p2 for synthetic samples. Thus α ∈ (0, 1)
999	is a mixing coefficient for the two the two source of data; in particular α → 0 corresponds to only
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f29d59e8-796b-40bb-84c9-9f2c3a2a3a9a",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "e192e7bd-c449-4f59-a61a-f7318f0f76a9",
  "sourceToolAssistantUUID": "f29d59e8-796b-40bb-84c9-9f2c3a2a3a9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T15:02:06.556Z_

<details open><summary>🔧 Tool call — Read · `toolu_017nY2YLM9MF3zM3CKNm99D7`</summary>

```json
{
  "file_path": "/tmp/strong_model_collapse.txt",
  "limit": 500,
  "offset": 1000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e192e7bd-c449-4f59-a61a-f7318f0f76a9",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2H63Dcyuc2EyVtyU6Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abcb64af-7823-4bb4-bd64-9e56735629f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UbCW9WzZkGJgEYR2s8Bt61",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6488,
      "cache_read_input_tokens": 31717,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6488
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 31717,
          "cache_creation_input_tokens": 6488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6488,
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

_source line 24 · 2026-05-20T15:02:06.833Z_

<details><summary>↩ Tool result · `toolu_017nY2YLM9MF3zM3CKNm99D7`</summary>

```text
1000	using real data for training, while α → 1 corresponds to only using surrogate data. Formula (16)
1001	replaces the formula for the weights vector w
1002	b of the classical linear model fbCL (3).
1003	For conciseness, as in Section 5 we focus on the isotropic case considered in Section 3.1 where the
1004	feature covariance matrices are Σ1 = Σ2 = Σ = Id and the shift matrix ∆ := cov(w1∗ − w2∗ ) has
1005	11
1006	
1007	the form (c2 /d)Id for some scalar c > 0. Further, let us consider the regime where d/n → 0 . In
1008	the language of our paper, one should think of this as corresponding to the proportionate scaling
1009	regime given in (4), and then letting ϕ → 0+ (extremely under-parametrized regime). We have the
1010	following result.
1011	
1012	(a) n1 = 1000, d = 500.
1013	
1014	(b) n1 = 10000, d = 100, so that ϕ = d/n ≤ 100/10200 < 0.01 (small). Corollary 2 correctly
1015	predicts that the optimal strategy mixing coefficient is α∗ ≈ 0, i.e to discard surrogate data altogether.
1016	
1017	Figure 9: Failure of naive real+surrogate data mixing to solve model collapse. For this experiment, we
1018	use different several different values for the size of the real data n1 and the synthetic data n2 . Solid curves
1019	correspond to experiments while broken curves correspond to our theoretical prediction give in Corollary 2.
1020	Error-bars correspond to independent runs.
1021	Corollary 2. Consider the proportionate scaling limit (4). For small ϕ = d/n, it holds that
1022	Etest (fbCL ) ≃ p22 α2 c2 + ((1 − α)p1 σ12 + αp2 σ22 )ϕ + O(ϕ2 ).
1023	
1024	(17)
1025	
1026	The formula given in (17) represents a U-shaped function of α, minimized when α = α∗ , with
1027	
1028	
1029	p1 σ12 − p2 σ22
1030	α∗ = clip[0,1] 1 −
1031	ϕ .
1032	(18)
1033	2c2
1034	Single-Step Mixing Does Not Avoid Model Collapse. It should be clear that if tr ∆ = Ω(1) and
1035	σ1 , σ2 = O(1), then α∗ → 0; this corresponds to only using real data for training! In contrast any
1036	fixed value α ∈ (0, 1], leads a positive lower-bound on test error Etest (fbCL ) ≥ p22 α2 c2 ≳ c2 ; this is
1037	effectively model collapse. The situation is empirically confirmed in Figure 9.
1038	5.2
1039	
1040	Dynamic / Multi-Step Data Mixing
1041	
1042	As in the case of single-step mixing discussed in Section 5.1, take for concreteness, take Σ1 = Σ2 =
1043	Σ = Id for the covariance matrices, and ∆ = (c2 /d)Σ−1 = (c2 /d)Id . In this setup, the proposal of
1044	Ferbach et al. (2024) then becomes
1045	• The quality parameter (cf. Def 1) of the synthetic data at the beginning (i.e at t = 0) is c2 = c20 .
1046	• At iteration t + 1, we mix n2 = p2 n samples of synthetic data from a source having quality
1047	parameter c2 = c2t , with n1 = n − n2 samples of real data to construct a penalized linear model
1048	w
1049	b(t+1) according to (3). This trained model generates the synthetic data with c2 = c2t+1 .
1050	Thus, the idea is to iteratively enhance the quality of the synthetic data through bootstrapping.
1051	Corollary 3. For large t, it holds in the limit (4) and then ϕ, λ → 0+ that
1052	(t)
1053	2
1054	Etest (fbCL ) ≃ E/(1 − p22 ) + Θ(p2t
1055	2 ), where E ≃ σ d/n,
1056	
1057	12
1058	
1059	σ 2 := p1 σ12 + p2 σ22 .
1060	
1061	(19)
1062	
1063	c02 = 100
1064	
1065	c02 = 10 1
1066	
1067	c02 = 10 2
1068	
1069	Test error
1070	
1071	100
1072	10 1
1073	10 2
1074	
1075	Mixing
1076	Iterative
1077	Clean
1078	Single
1079	103
1080	Total dataset size n
1081	
1082	104
1083	
1084	103
1085	Total dataset size n
1086	
1087	104
1088	
1089	103
1090	Total dataset size n
1091	
1092	104
1093	
1094	Figure 10: Iterative vs Single-Step Mixing. Solid lines represent the experimental results (5 runs), while
1095	dashed lines correspond to the theoretical predictions of Corollary 3. The iterative mixing is repeated 5 times,
1096	with p1 = p2 = 0.5. “Clean” refers to the scaling when using solely the n1 = p1 n real data in the dataset.
1097	
1098	We now explore some important consequences of Corollary 3.
1099	Iterative Mixing Recovers Scaling Laws but Might Not be Feasible in Practice. If the practitioner can curate a sufficient amount of data from the original distribution, the training dataset will
1100	include a non-vanishing proportion of real data, ensuring that p1 remains bounded away from zero.
1101	By comparing E with p2t
1102	2 , we observe that iterative mixing over t iterations, where t is of the order
1103	of log(n/d), results in a scaling law proportional to E, as empirically confirmed in Figure 10. However, this comes at the cost of significant bootstrapping, a large volume of real data, and the need
1104	to clearly distinguish between real and synthetic data across iterations—conditions that are all too
1105	computationally expensive and challenging to implement in practice.
1106	Iterative Mixing Relies Mostly on Real Data. In Figure 10, we compare the scaling of iterative
1107	mixing with the scaling obtained using only the p1 n real data portion from the same training set
1108	(”Clean”). While the scaling rate remains consistent, iterative mixing consistently underperforms
1109	compared to using real data alone. This suggests that iterative mixing may primarily neutralize
1110	the synthetic data and heavily rely on the real data to recover the scaling. Even when the original
1111	synthetic data is of high quality (i.e., when c0 is small, rightmost plot of FIgure 10), the iterative
1112	method fails to effectively leverage the synthetic data, resulting in worse performance than single
1113	mixing. Thus, although iterative mixing recovers the same scaling rate, the model still collapses to
1114	some degree, and no significant performance improvement is observed.
1115	Iterative Mixing with Little Real Data is Bad. If we consider the setting where we only have
1116	limited real data or where there is faster accumulation of synthetic data, which corresponds to p2 →
1117	1 (the real data in the training set is diminishing), then it holds that for any t ≥ 1, Etest (w
1118	b(t) ) ≃
1119	c20 + tE. This is an increasing function of t, meaning that there is still catastrophic model collapse.
1120	
1121	6
1122	
1123	Discussion
1124	
1125	Our work systematically characterizes the effects of training models on mixtures of real and synthetic data, showing that model collapse is a robust phenomenon that persists even with small fractions of synthetic data, in the asymptotic regime. By introducing new mathematical tools, we extend
1126	prior work to analyze more complex mixing settings and models (random projections), broadening
1127	the scope of theoretically tractable problems. Experiments confirm our theoretical predictions across
1128	large language models (LLMs) and also fully-trained feed-forward neural networks.
1129	Going beyond the prevalent “neural scaling laws” paradigm (Kaplan et al., 2020; Hoffmann et al.,
1130	2022) which is at the basis of the current trend in training LLMs, this study emphasizes the importance of preserving and labeling real data, either by curating it or avoiding unintended synthetic data
1131	in training, reflecting a shift as AI-generated data becomes prevalent. Our work also delineates the
1132	impact of model size on the model collapse profile. Future work will explore the effect of other
1133	model design choices like activation functions, depth, and optimization hyper-parameters like learning rate and momentum. To this end, we can leverage “Gaussian equivalents” (Goldt et al., 2022) to
1134	extend our theory to wide, fully-trained networks in the neural tangent kernel (Jacot et al., 2018) and
1135	lazy (Chizat et al., 2019) regimes, using operator-valued free probability theory (Mingo & Speicher,
1136	2017), like we have done in our analysis.
1137	13
1138	
1139	7
1140	
1141	Acknowledgements
1142	
1143	YF and JK acknowledge support through the NSF under award 1922658. Part of this work was
1144	done while YF and JK where visiting the Centre Sciences de Donnees (CSD) at the Ecole Normale
1145	Superieure in Paris, France, and YF and JK wish to thank the CSD for their hospitality.
1146	
1147	References
1148	Ben Adlam and Jeffrey Pennington. The neural tangent kernel in high dimensions: Triple descent
1149	and a multi-scale theory of generalization. In International Conference on Machine Learning, pp.
1150	74–84. PMLR, 2020.
1151	Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein
1152	Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk. Self-consuming generative
1153	models go mad. arXiv preprint arxiv:2307.01850, 2023.
1154	Sina Alemohammad, Ahmed Imtiaz Humayun, Shruti Agarwal, John Collomosse, and Richard
1155	Baraniuk. Self-improving diffusion models with synthetic data, 2024. URL https://arxiv.
1156	org/abs/2408.16333.
1157	Francis Bach. High-dimensional analysis of double descent for linear regression with random projections. 2023.
1158	Quentin Bertrand, Avishek Joey Bose, Alexandre Duplessis, Marco Jiralerspong, and Gauthier
1159	Gidel. On the stability of iterative retraining of generative models on their own data. arXiv
1160	preprint arxiv:2310.00429, 2023.
1161	Matyas Bohacek and Hany Farid. Nepotistically trained generative-ai models collapse, 2023.
1162	Martin Briesch, Dominik Sobania, and Franz Rothlauf. Large language models suffer from their
1163	own output: An analysis of the self-consuming training loop, 2023.
1164	Andrea Caponnetto and Ernesto de Vito. Optimal rates for the regularized least-squares algorithm.
1165	Foundations of Computational Mathematics, 7:331–368, 2007.
1166	Lenaic Chizat, Edouard Oyallon, and Francis Bach. On lazy training in differentiable programming.
1167	Advances in neural information processing systems, 32, 2019.
1168	Hugo Cui, Bruno Loureiro, Florent Krzakala, and Lenka Zdeborová. Generalization error rates
1169	in kernel regression: the crossover from the noiseless to noisy regime. Journal of Statistical
1170	Mechanics: Theory and Experiment, 2022(11):114004, nov 2022.
1171	Hugo Cui, Bruno Loureiro, Florent Krzakala, and Lenka Zdeborová. Error scaling laws for kernel
1172	classification under source and capacity conditions. Machine Learning: Science and Technology,
1173	4(3):035033, August 2023. ISSN 2632-2153. doi: 10.1088/2632-2153/acf041.
1174	Li Deng. The mnist database of handwritten digit images for machine learning research [best of the
1175	web]. IEEE signal processing magazine, 29(6):141–142, 2012.
1176	Elvis Dohmatob, Yunzhen Feng, and Julia Kempe. Model collapse demystified: The case of regression. arXiv preprint arXiv:2402.07712, 2024a.
1177	Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, and Julia Kempe. A tale of tails:
1178	Model collapse as a change of scaling laws. In Forty-first International Conference on Machine
1179	Learning, 2024b.
1180	Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, and Julia Kempe. A tale of tails:
1181	Model collapse as a change of scaling laws. arXiv preprint arXiv:2402.07043, 2024c. URL
1182	https://openreview.net/forum?id=KVvku47shW.
1183	Abhimanyu Dubey and et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783, 2024.
1184	Ronen Eldan and Yuanzhi Li. Tinystories: How small can language models be and still speak
1185	coherent english? arXiv preprint arXiv:2305.07759, 2023.
1186	Yunzhen Feng, Elvis Dohmatob, Pu Yang, Francois Charton, and Julia Kempe. Beyond model
1187	collapse: Scaling up with synthesized data requires reinforcement, 2024. URL https://arxiv.
1188	org/abs/2406.07515.
1189	14
1190	
1191	Damien Ferbach, Quentin Bertrand, Avishek Joey Bose, and Gauthier Gidel. Self-consuming generative models with curated data provably optimize human preferences, 2024. URL https:
1192	//arxiv.org/abs/2407.09499.
1193	Sebastian Goldt, Bruno Loureiro, Galen Reeves, Florent Krzakala, Marc Mézard, and Lenka Zdeborová. The gaussian equivalence of generative models for learning with shallow neural networks.
1194	In Mathematical and Scientific Machine Learning, pp. 426–471. PMLR, 2022.
1195	Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, and Chloé Clavel. The curious decline of
1196	linguistic diversity: Training language models on synthetic text, 2023.
1197	Trevor Hastie, Andrea Montanari, Saharon Rosset, and Ryan J. Tibshirani. Surprises in highdimensional ridgeless least squares interpolation. The Annals of Statistics, 50(2), 2022.
1198	Ryuichiro Hataya, Han Bao, and Hiromi Arai. Will large-scale generative models corrupt future
1199	datasets? In Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV),
1200	pp. 20555–20565, October 2023.
1201	Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza
1202	Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy,
1203	Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, and Laurent Sifre.
1204	Training compute-optimal large language models, 2022.
1205	Arthur Jacot, Franck Gabriel, and Clement Hongler. Neural tangent kernel: Convergence and generalization in neural networks. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. CesaBianchi, and R. Garnett (eds.), Advances in Neural Information Processing Systems, volume 31.
1206	Curran Associates, Inc., 2018.
1207	Ayush Jain, Andrea Montanari, and Eren Sasoglu. Scaling laws for learning with real and surrogate
1208	data, 2024. URL https://arxiv.org/abs/2402.04376.
1209	Albert Q Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, et al.
1210	Mixtral of experts. arXiv preprint arXiv:2401.04088, 2024.
1211	Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child,
1212	Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language
1213	models. arXiv preprint arXiv:2001.08361, 2020.
1214	V. Kargin. Subordination for the sum of two random matrices. The Annals of Probability, 43(4):
1215	2119 – 2150, 2015.
1216	Donghwan Lee, Behrad Moniri, Xinmeng Huang, Edgar Dobriban, and Hamed Hassani. Demystifying disagreement-on-the-line in high dimensions. In International Conference on Machine
1217	Learning, pp. 19053–19093. PMLR, 2023.
1218	Jaehoon Lee, Yasaman Bahri, Roman Novak, Samuel S. Schoenholz, Jeffrey Pennington, and Jascha
1219	Sohl-Dickstein. Deep neural networks as gaussian processes. In 6th International Conference on
1220	Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings. OpenReview.net, 2018.
1221	Alexander Maloney, Daniel A. Roberts, and James Sully. A solvable model of neural scaling laws,
1222	2022.
1223	Gonzalo Martı́nez, Lauren Watson, Pedro Reviriego, José Alberto Hernández, Marc Juarez, and
1224	Rik Sarkar. Combining generative artificial intelligence (ai) and the internet: Heading towards
1225	evolution or degradation? arXiv preprint arxiv: 2303.01255, 2023a.
1226	Gonzalo Martı́nez, Lauren Watson, Pedro Reviriego, José Alberto Hernández, Marc Juarez, and Rik
1227	Sarkar. Towards understanding the interplay of generative artificial intelligence and the internet.
1228	arXiv preprint arxiv: 2306.06130, 2023b.
1229	V.A. Marčenko and Leonid Pastur. Distribution of eigenvalues for some sets of random matrices.
1230	Math USSR Sb, 1:457–483, 01 1967.
1231	James A. Mingo and Roland Speicher. Free Probability and Random Matrices, volume 35 of Fields
1232	Institute Monographs. Springer, 2017.
1233	Radford M. Neal. Priors for infinite networks. In Bayesian Learning for Neural Networks, pp.
1234	29–53. Springer, New York, 1996.
1235	15
1236	
1237	Ali Rahimi and Benjamin Recht. Weighted sums of random kitchen sinks: Replacing minimization
1238	with randomization in learning. In Advances in Neural Information Processing Systems. Curran
1239	Associates, Inc., 2008.
1240	Dominic Richards, Jaouad Mourtada, and Lorenzo Rosasco. Asymptotics of ridge(less) regression
1241	under general source condition. In Proceedings of The 24th International Conference on Artificial
1242	Intelligence and Statistics, volume 130 of Proceedings of Machine Learning Research. PMLR,
1243	2021.
1244	Alessandro Rudi and Lorenzo Rosasco. Generalization properties of learning with random features.
1245	In Advances in Neural Information Processing Systems. Curran Associates Inc., 2017. ISBN
1246	9781510860964.
1247	Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah. How bad is training on synthetic data? a statistical analysis of language model collapse.
1248	arXiv preprint arXiv:2404.05090, 2024.
1249	H. Shimodaira. Improving predictive inference under covariate shift by weighting the loglikelihood
1250	function. Journal of Statistical Planning and Inference, 90(2):227–244, 2000.
1251	Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, and Ross Anderson. The curse of recursion: Training on generated data makes models forget. arXiv preprint
1252	arxiv:2305.17493, 2023.
1253	Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, and Ross Anderson.
1254	Ai models collapse when trained on recursively generated data. Nature, 631, 2024.
1255	Stefano Spigler, Mario Geiger, and Matthieu Wyart. Asymptotic learning curves of kernel methods:
1256	empirical data versus teacher–student paradigm. Journal of Statistical Mechanics: Theory and
1257	Experiment, 2020(12):124001, December 2020. ISSN 1742-5468. doi: 10.1088/1742-5468/
1258	abc61d.
1259	Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.
1260	Nilesh Tripuraneni, Ben Adlam, and Jeffrey Pennington. Covariate shift in high-dimensional random
1261	feature regression. arXiv preprint arXiv:2111.08234, 2021.
1262	Robin Vogel, Mastane Achab, Stéphan Clémençon, and Charles Tillier. Weighted empirical risk
1263	minimization: Sample selection bias correction based on importance sampling. ArXiv, 2021.
1264	Christopher Williams. Computing with infinite networks. In M.C. Mozer, M. Jordan, and T. Petsche
1265	(eds.), Advances in Neural Information Processing Systems, volume 9. MIT Press, 1996.
1266	Jianyu Zhang, Niklas Nolte, Ranajoy Sadhukhan, Beidi Chen, and Léon Bottou. Memory mosaics.
1267	arXiv preprint arXiv:2405.06394, 2024a.
1268	Jinghui Zhang, Dandan Qiao, Mochen Yang, and Qiang Wei. Regurgitative training: The value of
1269	real data in training large language models. arXiv preprint arXiv:2407.12835, 2024b.
1270	
1271	16
1272	
1273	Appendix
1274	Table of Contents
1275	A Experimental Details
1276	A.1 Toy Setting: Random Projections Model . . . . . . . . . . . . . . . . . . . . .
1277	A.2 Two-layer neural networks . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1278	A.3 Language Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1279	
1280	18
1281	18
1282	18
1283	18
1284	
1285	B Some Omitted Theoretical Results and Comments
1286	B.1 Classical Linear Model in Over-Parametrized Isotropic Setting . . . . . . . . . .
1287	B.2 Connections to Classical Model Collapse in Regression . . . . . . . . . . . . .
1288	
1289	18
1290	18
1291	19
1292	
1293	C Raw Bias-Variance Decomposition
1294	C.1 Classical Linear Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1295	C.2 Random Projections Model . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1296	
1297	19
1298	19
1299	20
1300	
1301	D Deterministic Equivalents
1302	D.1 Classical Linear Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1303	D.2 Random Projections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1304	D.3 Proof of Proposition 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1305	
1306	22
1307	22
1308	23
1309	23
1310	
1311	(1)
1312	
1313	Computing rj . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1314	
1315	23
1316	
1317	Computing r(4) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1318	Computing r(3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1319	Computing r(2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1320	D.4 Proof of Proposition 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1321	
1322	24
1323	26
1324	27
1325	27
1326	
1327	E Proof of Theorem 1 and Corollaries
1328	E.1 Proof of Theorem 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1329	E.2 Proof of Corollary 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1330	E.3 Proof of Corollary 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1331	E.4 Proof of Corollary 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1332	E.5 Proof of Corollary 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1333	
1334	27
1335	27
1336	28
1337	28
1338	29
1339	30
1340	
1341	F Proof of Proposition 3 and Theorem 2
1342	F.1 Proof of Proposition 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1343	F.2 Proof of Theorem 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1344	F.3 Recovering Theorem 1 from Theorem 2 . . . . . . . . . . . . . . . . . . . . . .
1345	
1346	30
1347	30
1348	32
1349	32
1350	
1351	G Phase-Diagram for Random Projections Model
1352	G.1 The General Regularized Case . . . . . . . . . . . . . . . . . . . . . . . . . . .
1353	G.2 Unregularized Limit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1354	
1355	32
1356	32
1357	33
1358	
1359	17
1360	
1361	A
1362	
1363	Experimental Details
1364	
1365	A.1
1366	
1367	Toy Setting: Random Projections Model
1368	
1369	Setup. As a sanity check to empirical confirm our analytical predictions from Theorem 2, we consider a setting with multivariate Gaussian data (1). The feature covariance matrix Σ is constructed
1370	to have power-law eigenvalues λj = C/j, where C is such that tr Σ = λ1 + . . . + λd = 1. The
1371	ground-truth labelling weights w1∗ of the real data distribution P1 sampled from N (0, (1/d)Id ),
1372	while the ground-truth weights w2∗ for the synthtic data distribution are sampled from N (w1∗ , ∆)
1373	with ∆ = (c2 /d)Σ−1 for different values of c2 ranging from {0, 0.1, 0.5, 1} which controls for the
1374	quality of the synthetic data. We run a small experiment with label noise levels σ1 = σ2 = 0.1,
1375	input-dimension d = 600, number of real samples n1 = 300, and synthetic samples n2 = 200, for
1376	a total of n = n1 + n2 = 500 samples. We fit a random projection model fbRP according to (5) and
1377	for different values of the width parameter m (to control the size the of the model), and report the
1378	results in Figures 5 and 4. The regularization parameter λ is set to a very small value (10−8 ). We
1379	also consider a variation of this experiment with different values of the synthetic dataset size n2 and
1380	report the results in Figure 1.
1381	A.2
1382	
1383	Two-layer neural networks
1384	
1385	The two-layer neural networks are trained using stochastic gradient descent (SGD) with a batch size
1386	of 128 and a learning rate of 0.1. The models are trained for 400 epochs to fully converge. We
1387	employ a held-out validation set from the training set to select the best checkpoint to evaluate.
1388	A.3
1389	
1390	Language Modeling
1391	
1392	The generation process for the BabiStories dataset is detailed in the GitHub repository of Zhang
1393	et al. (2024a). The dataset comprises a training set of 2,200,000 stories and a validation set of
1394	22,000 stories, created by prompting the Mistral-8x7B model. Each prompt includes a description
1395	of the generation task, character names, specific words to be used, and the beginning of a story. The
1396	dataset stores the beginnings of these stories along with their generated continuations.
1397	In our experiments, we trained a GPT-2-small model on this dataset to generate synthetic data. The
1398	model was trained using next-token prediction, utilizing the beginnings and continuations of stories
1399	to have good story generation quality. To maintain consistency with the original prompt distribution,
1400	we used all the prompts that were initially employed to generate BabiStories. During story generation, we applied a temperature setting of 1 with top-p decoding where p = 1. After generation, we
1401	filtered out stories of poor quality, such as those containing unwanted symbols, following the same
1402	procedure as in Zhang et al. (2024a). The filtered beginnings and synthetic continuations were then
1403	collected to form the synthetic dataset.
1404	We used a GPT-2 model with an embedding dimension of d = 768, 12 attention heads, and a context
1405	length of 512 tokens, which typically encompasses one to three stories. During training, we applied
1406	a learning rate of 5 × 10−3 , a dropout rate of 0.05, L2 weight decay of 0.1, and a warm-up phase of
1407	2,000 iterations.
1408	
1409	B
1410	
1411	Some Omitted Theoretical Results and Comments
1412	
1413	B.1
1414	
1415	Classical Linear Model in Over-Parametrized Isotropic Setting
1416	
1417	We now complement the analysis presented at the end of Section 3.1 with an analysis for the case
1418	ϕ ∈ (1, ∞). Plugging into Theorem 1 gives κ → ϕ − 1 and u → 1/(1 − ϕ/ϕ2 ) = ϕ/(ϕ − 1) in the
1419	limit λ → 0+ . We obtain the following corollary.
1420	Corollary 4. For ϕ ∈ (1, ∞), in the limit (4) and λ → 0+ , it holds that Etest ≃ E + ζ, with
1421	
1422	
1423	1
1424	σ2
1425	p2 c2
1426	ϕ − p2
1427	2
1428	2
1429	E = V + B, B = r (1 − ), V =
1430	, ζ= 2
1431	p2
1432	+ (ϕ − p2 ) ,
1433	(20)
1434	ϕ
1435	ϕ−1
1436	ϕ
1437	ϕ−1
1438	Moreover, for large ϕ ∈ (1, ∞), it holds that Etest (fbCL ) − E ≃ (1 − 2/ϕ) p2 c2 + O(1/ϕ2 ).
1439	18
1440	
1441	Thus, for any fixed c > 0, strong model collapse occurs: the RHS vanishes only if p2 → 0+ , i.e
1442	only if we discard all but a vanishing proportion of synthetic data from the training dataset. This
1443	is strong model collapse. Combining with Corollary 1, we conclude that (at least in the isotropic
1444	setting, strong model collapse occurs both the under-parametrized and over-parametrized settings.
1445	B.2
1446	
1447	Connections to Classical Model Collapse in Regression
1448	
1449	In the setting of classical model collapse (Shumailov et al., 2023, 2024; Alemohammad et al., 2023;
1450	PN
1451	Dohmatob et al., 2024b,a), we have w2∗ = w1∗ + ℓ=1 Xℓ† Eℓ ,where N is the number of iterations (i.e
1452	self-loops) in the synthetic data-generation process. Let nℓ be the number of samples available for
1453	training at stage ℓ with training data (Xℓ , Xℓ w2∗ + Eℓ ) ∈ Rn×d × Rn , where the noise vectors Eℓ are
1454	independent with iid components from N (0, σℓ2 ). In the proportionate scaling regime n1 , . . . , nN →
1455	∞ with d/nℓ → ϕℓ ∈ (0, ∞) for all ℓ, the situation is equivalent to taking
1456	∆=
1457	
1458	X
1459	
1460	σℓ2 · E (Xℓ† )⊤ Xℓ† ≃
1461	
1462	ℓ
1463	
1464	X
1465	ℓ
1466	
1467	σℓ2
1468	Σ(Σ + κℓ Id )−2 , with κℓ = κ(nℓ , 0; Σ).
1469	nℓ − df 2 (κℓ ; Σ)
1470	
1471	In particular, if maxℓ ϕℓ ≤ 1 (so that there is enough samples to perfectly fit the training data at each
1472	stage of the iterative process),
1473	we set σℓ = σ0 for all ℓ, then the above expression
1474	P 2 and for simplicity
1475	−1
1476	simplifies to ∆ ≃
1477	. More generally, consider the generic setting where
1478	ℓ σℓ /(nℓ − d) Σ
1479	P
1480	∆ ≃ (c2 /d)Σ−1 , for any c > 0, so that the previous setting corresponds to c2 = ℓ σℓ2 ϕℓ /(1 − ϕℓ ).
1481	In the particular case where p1 → 0+ , i.e only synthetic data is available for training. Theorem 1
1482	then gives
1483	
1484	
1485	
1486	df 2
1487	c2
1488	· df 2 +uκ2 tr(Σ + κId )−2 = η 2 df 2 · 1 + κ2
1489	ζ≃
1490	tr(Σ + κId )−2 .
1491	d
1492	n − df 2
1493	P
1494	In particular, taking c2 = ℓ σℓ2 ϕℓ /(1 − ϕℓ ) gives
1495	
1496	
1497	df 2 X σℓ2 ϕℓ
1498	df 2
1499	tr(Σ + κId )−2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abcb64af-7823-4bb4-bd64-9e56735629f5",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "b663afc9-7b21-472f-a342-bc94a9a07e9d",
  "sourceToolAssistantUUID": "abcb64af-7823-4bb4-bd64-9e56735629f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T15:02:09.761Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KVAK4e3XzAXSPHNTF59nNP`</summary>

```json
{
  "file_path": "/tmp/strong_model_collapse.txt",
  "limit": 200,
  "offset": 1500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b663afc9-7b21-472f-a342-bc94a9a07e9d",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2HMacBv6hyxvWTyXpB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb06f6ac-b41e-43bb-a273-e1b322360e93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C6FgqhwcRGq8yWK37k8iD3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10536,
      "cache_read_input_tokens": 38205,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10536
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 38205,
          "cache_creation_input_tokens": 10536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10536,
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

_source line 26 · 2026-05-20T15:02:09.772Z_

<details><summary>↩ Tool result · `toolu_01KVAK4e3XzAXSPHNTF59nNP`</summary>

```text
1500	.
1501	(21)
1502	ζ ≃ 1 + κ2
1503	n − df 2
1504	d
1505	1 − ϕℓ
1506	ℓ
1507	
1508	This is recovers the main result of (Dohmatob et al., 2024a).
1509	
1510	C
1511	
1512	Raw Bias-Variance Decomposition
1513	
1514	Let Xj (resp. Yj ) be the design matrix (resp. response vector) corresponding to dataset Dj . Thus, the
1515	design matrix X1 ∈ Rn1 ×d for the real dataset has rows given by xi for i ∈ [n1 ] and Y1 ∈ Rn1 with
1516	components yi for i ∈ [n1 ], with X2 ∈ Rn2 ×d and Y2 ∈ Rn2 defined analogously for the synthetic
1517	dataset. Let X ∈ Rn×d (resp. Y ∈ Rn ) be the design matrix (resp. response vector) corresponding
1518	to the total dataset. We temporarily drop the condition Σ1 = Σ2 = Σ, and instead consider generally
1519	different covariance matrices Σ1 and Σ2 for the marginal distribution of the features x under the real
1520	data distribution P1 and the synthetic data distribution P2 .
1521	C.1
1522	
1523	Classical Linear Model
1524	
1525	Proposition 1. Evaluated on the distribution Pk = PΣk ,σk2 ,wk∗ , the test error of model fbCL defined
1526	in (3) is given by
1527	Etest (fbCL ) = Bk + Vk ,
1528	
1529	(22)
1530	
1531	2
1532	X
1533	
1534	σj2 (4)
1535	r (Id , Σk ),
1536	n j
1537	j=1
1538	(
1539	(3)
1540	r2 (∆, Σ1 ) + λ2 r(2) (Γ, Σ1 ),
1541	Bk =
1542	(3)
1543	(4)
1544	r1 (∆, Σ2 ) + λ2 r(2) (Γ + ∆, Σ2 ) + 2λr1 (∆, Σ2 ),
1545	
1546	where Vk =
1547	
1548	19
1549	
1550	(23)
1551	if k = 1,
1552	if k = 2.
1553	
1554	(24)
1555	
1556	Proof. Indeed, one computes
1557	ED ∥w
1558	b − wk∗ ∥2Σk = EX1 ,Y1 ,X2 ,Y2 Ex∼N (0,Σk ) [(x⊤ w
1559	b − x⊤ wk∗ )2 ]
1560	= EX1 ,Y1 ,X2 ,Y2 ∥w
1561	b − wk∗ ∥2Σk
1562	= EX1 ,Y1 ,X2 ,Y2 ∥(M + λId )−1 X ⊤ Y /n − wk∗ ∥2Σk
1563	= EX1 ,Y1 ,X2 ,Y2 ∥(M + λId )−1 X ⊤ (X1 w1∗ + E1 , X2 w2∗ + E2 )/n − wk∗ ∥2Σk
1564	= EX1 ,Y1 ,X2 ,Y2 ∥(M + λId )−1 (M1 w1∗ + M2 w2∗ ) − wk∗ ∥2Σk + V1 + V2
1565	= Bk + Vk,1 + Vk,2 .
1566	where
1567	∗
1568	Bk := E ∥(M + λId )−1 (Mk wk∗ + M−k w−k
1569	) − wk∗ ∥2Σk ,
1570	
1571	Vk,j :=
1572	
1573	σj2
1574	n
1575	
1576	σj2 (4)
1577	E tr Mj (M + λId )−1 Σk (M + λId )−1 =
1578	rj (Id , Σk ).
1579	n
1580	
1581	(25)
1582	(26)
1583	
1584	It remains to analyze the bias term Bk . To this end, observe that
1585	(M + λId )−1 Mk = Id − (M + λId )−1 (M−k + λId ) = Id − (M + λM )−1 M−k − λ(M + λId )−1 .
1586	∗
1587	∗
1588	Denoting M−1 = M2 , M−2 = M1 , w−1
1589	= w2∗ , w−2
1590	= w1∗ , and δk = (−1)k δ, where δ := w2∗ −w1∗ ,
1591	we deduce that
1592	∗
1593	(M + λId )−1 Mk wk∗ + (M + λId )−1 M−k w−k
1594	− wk∗
1595	∗
1596	= (M + λId )−1 M−k w−k
1597	− (M + λId )−1 M−k wk∗ − λ(M + λId )−1 wk∗
1598	
1599	= −(M + λId )−1 M−k δk − λ(M + λId )−1 wk⋆ .
1600	Since w1∗ and δ1 = δ := w2∗ − w1∗ are independent with distributions N (0, Γ) and N (0, ∆) respectively, we deduce that
1601	B1 = ∥(M + λId )−1 M2 δ − λ(M + λId )−1 w1⋆ ∥2Σ1
1602	= tr ∆M2 (M + λId )−1 Σ1 (M + λId )−1 M2 + λ2 tr Γ1 (M + λId )−1 Σ1 (M + λId )−1
1603	(3)
1604	
1605	= r2 (∆, Σ1 ) + λ2 r(2) (Γ, Σ1 ).
1606	On the other hand, we have B2 = B2,1 + B2,2 , where
1607	B2 = ∥ − (M + λId )−1 M1 δ − λ(M + λId )−1 w2⋆ ∥2Σ2
1608	= ∥ − (M + λId )−1 M1 δ − λ(M + λId )−1 (w1⋆ + δ)∥2Σ2
1609	= ∥ − (M + λId )−1 (M1 + λId ) δ − λ(M + λId )−1 w1⋆ ∥2Σ2
1610	= tr ∆(M1 + λId )(M + λId )−1 Σ2 (M + λId )−1 (M1 + λId ) + λ2 tr Γ(M + λId )−1 Σ2 (M + λId )−1
1611	= tr ∆M1 (M + λId )−1 Σ2 (M + λId )−1 M1 + λ2 tr ∆(M + λId )−1 Σ2 (M + λId )−1
1612	+ 2λ tr ∆M1 (M + λId )−1 Σ2 (M + λId )−1 + λ2 tr Γ(M + λId )−1 Σ2 (M + λId )−1
1613	(3)
1614	
1615	(4)
1616	
1617	= r1 (∆, Σ2 ) + λ2 r(2) (Γ + ∆, Σ2 ) + 2λr1 (∆, Σ2 ).
1618	This completes the proof.
1619	C.2
1620	
1621	Random Projections Model
1622	
1623	We now expand the test error Etest (fbRP ) of the random projections model fbRP defined in (5). For
1624	convenience, we recall the definition of the model here. Let S be a d × m random matrix with iid
1625	entries from N (0, 1/d). The model fbRP is defined by fbRP (x) := Φ(x)⊤ vb, where Φ(x) := S ⊤ x ∈
1626	Rm defines a random feature map, and vb ∈ Rm is given by
1627	X ∥Φ(Xk )v − Yk ∥2
1628	2
1629	arg minm L(w) =
1630	+ λ∥v∥22 .
1631	(27)
1632	v∈R
1633	n
1634	k
1635	
1636	20
1637	
1638	Note that the gradient ∇L(v) of the regularized loss L is given by
1639	X
1640	X
1641	X
1642	∇L(v)/2 =
1643	S ⊤ Xk⊤ (Xk Sv − Yk )/n + λv =
1644	S ⊤ Mk Sv −
1645	S ⊤ Xk⊤ Yk /n + η
1646	k
1647	
1648	= Hv −
1649	
1650	k
1651	
1652	X
1653	
1654	S
1655	
1656	⊤
1657	
1658	k
1659	
1660	Xk⊤ Yk /n,
1661	
1662	k
1663	
1664	where H := S ⊤ M S + λIm ∈ Rm×m , with M := M1 + M2 and Mk := Xk⊤ Xk /n. Thus, setting
1665	R := H −1 , we may write
1666	vb = RS ⊤ (X1⊤ Y1 + X2⊤ Y2 )/n = RS ⊤ (M1 w1 + M2 w2 ) + RS ⊤ X1⊤ E1 /n + RS ⊤ X2⊤ E2 /n.
1667	Now, one deduces the bias-variance decomposition
1668	Etest (fbRP ) = ED Ex∼N (0,Σk ) [(fbRP (x) − x⊤ w1∗ )2 ] = EX1 ,E1 ,X2 ,E2 ∥Sb
1669	v − wk ∥2Σk = Bk + Vk ,
1670	σj2
1671	EX1 ,X2 tr S ⊤ Mj SRS ⊤ Σk SRS ⊤ ,
1672	n
1673	Bk := EX1 ,X2 ∥SRS ⊤ (M1 w1 + M2 w2 ) − wk ∥2Σk .
1674	
1675	where Vk := Vk,1 + Vk,2 , with Vk,j :=
1676	
1677	The variance terms Vk,j can be directly handled via FPT computations. We now look at the bias
1678	term Bk . We first treat the case k = 1. One has
1679	E∥SRS ⊤ (M1 w1 + M2 w2 ) − w1 ∥2Σ
1680	= E∥(SRS ⊤ (M1 + M2 ) − Id )w1 + SRS ⊤ M2 δ∥2Σ
1681	= E∥(SRS ⊤ M − Id )w1 ∥2Σ + E∥SRS ⊤ M2 δ∥2Σ
1682	= E tr Γ(SRS ⊤ M − Id )Σ(M SRS ⊤ − Id ) + E tr ∆M2 SRS ⊤ ΣSRS ⊤ M2
1683	= tr ΓΣ + tr ΓSRS ⊤ M ΣM SRS ⊤ − 2E tr ΓΣSRS ⊤ M + E tr ∆M2 SRS ⊤ ΣSRS ⊤ M2
1684	= tr ΓΣ + E tr ΣM SRS ⊤ ΓSRS ⊤ M − 2E tr ΓΣSRS ⊤ M + E tr ∆M2 SRS ⊤ ΣSRS ⊤ M2 ,
1685	{z
1686	} |
1687	|
1688	{z
1689	}
1690	classical term (B)
1691	⊤
1692	
1693	extra term (ζ)
1694	
1695	where we recall that R := (S M S + λIm )
1696	
1697	−1
1698	
1699	and M := M1 + M2 with Mk = Xk⊤ Xk .
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb06f6ac-b41e-43bb-a273-e1b322360e93",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "a6d7e70f-fcb7-45f8-8d4f-0ef3de04d7fe",
  "sourceToolAssistantUUID": "eb06f6ac-b41e-43bb-a273-e1b322360e93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-20T15:02:12.778Z_

I now have all the key content. Let me read the appendix details on language modeling training setup for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6d7e70f-fcb7-45f8-8d4f-0ef3de04d7fe",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2Ha8uf8gwUF4Lb1GDg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ccea81cb-c060-491d-96bd-5aa9b6647dc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LBUeKYfRRy6hbSNX2UnHVh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 48741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3920,
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

_source line 28 · 2026-05-20T15:02:13.356Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KdTitNb2s2sh3bSZKC9qgz`</summary>

```json
{
  "file_path": "/tmp/strong_model_collapse.txt",
  "limit": 100,
  "offset": 1390
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccea81cb-c060-491d-96bd-5aa9b6647dc7",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2Ha8uf8gwUF4Lb1GDg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3baf6d88-5692-4940-a49f-58a4095f2f0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LBUeKYfRRy6hbSNX2UnHVh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 48741,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3920
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 48741,
          "cache_creation_input_tokens": 3920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3920,
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

_source line 29 · 2026-05-20T15:02:13.360Z_

<details><summary>↩ Tool result · `toolu_01KdTitNb2s2sh3bSZKC9qgz`</summary>

```text
1390	Language Modeling
1391	
1392	The generation process for the BabiStories dataset is detailed in the GitHub repository of Zhang
1393	et al. (2024a). The dataset comprises a training set of 2,200,000 stories and a validation set of
1394	22,000 stories, created by prompting the Mistral-8x7B model. Each prompt includes a description
1395	of the generation task, character names, specific words to be used, and the beginning of a story. The
1396	dataset stores the beginnings of these stories along with their generated continuations.
1397	In our experiments, we trained a GPT-2-small model on this dataset to generate synthetic data. The
1398	model was trained using next-token prediction, utilizing the beginnings and continuations of stories
1399	to have good story generation quality. To maintain consistency with the original prompt distribution,
1400	we used all the prompts that were initially employed to generate BabiStories. During story generation, we applied a temperature setting of 1 with top-p decoding where p = 1. After generation, we
1401	filtered out stories of poor quality, such as those containing unwanted symbols, following the same
1402	procedure as in Zhang et al. (2024a). The filtered beginnings and synthetic continuations were then
1403	collected to form the synthetic dataset.
1404	We used a GPT-2 model with an embedding dimension of d = 768, 12 attention heads, and a context
1405	length of 512 tokens, which typically encompasses one to three stories. During training, we applied
1406	a learning rate of 5 × 10−3 , a dropout rate of 0.05, L2 weight decay of 0.1, and a warm-up phase of
1407	2,000 iterations.
1408	
1409	B
1410	
1411	Some Omitted Theoretical Results and Comments
1412	
1413	B.1
1414	
1415	Classical Linear Model in Over-Parametrized Isotropic Setting
1416	
1417	We now complement the analysis presented at the end of Section 3.1 with an analysis for the case
1418	ϕ ∈ (1, ∞). Plugging into Theorem 1 gives κ → ϕ − 1 and u → 1/(1 − ϕ/ϕ2 ) = ϕ/(ϕ − 1) in the
1419	limit λ → 0+ . We obtain the following corollary.
1420	Corollary 4. For ϕ ∈ (1, ∞), in the limit (4) and λ → 0+ , it holds that Etest ≃ E + ζ, with
1421	
1422	
1423	1
1424	σ2
1425	p2 c2
1426	ϕ − p2
1427	2
1428	2
1429	E = V + B, B = r (1 − ), V =
1430	, ζ= 2
1431	p2
1432	+ (ϕ − p2 ) ,
1433	(20)
1434	ϕ
1435	ϕ−1
1436	ϕ
1437	ϕ−1
1438	Moreover, for large ϕ ∈ (1, ∞), it holds that Etest (fbCL ) − E ≃ (1 − 2/ϕ) p2 c2 + O(1/ϕ2 ).
1439	18
1440	
1441	Thus, for any fixed c > 0, strong model collapse occurs: the RHS vanishes only if p2 → 0+ , i.e
1442	only if we discard all but a vanishing proportion of synthetic data from the training dataset. This
1443	is strong model collapse. Combining with Corollary 1, we conclude that (at least in the isotropic
1444	setting, strong model collapse occurs both the under-parametrized and over-parametrized settings.
1445	B.2
1446	
1447	Connections to Classical Model Collapse in Regression
1448	
1449	In the setting of classical model collapse (Shumailov et al., 2023, 2024; Alemohammad et al., 2023;
1450	PN
1451	Dohmatob et al., 2024b,a), we have w2∗ = w1∗ + ℓ=1 Xℓ† Eℓ ,where N is the number of iterations (i.e
1452	self-loops) in the synthetic data-generation process. Let nℓ be the number of samples available for
1453	training at stage ℓ with training data (Xℓ , Xℓ w2∗ + Eℓ ) ∈ Rn×d × Rn , where the noise vectors Eℓ are
1454	independent with iid components from N (0, σℓ2 ). In the proportionate scaling regime n1 , . . . , nN →
1455	∞ with d/nℓ → ϕℓ ∈ (0, ∞) for all ℓ, the situation is equivalent to taking
1456	∆=
1457	
1458	X
1459	
1460	σℓ2 · E (Xℓ† )⊤ Xℓ† ≃
1461	
1462	ℓ
1463	
1464	X
1465	ℓ
1466	
1467	σℓ2
1468	Σ(Σ + κℓ Id )−2 , with κℓ = κ(nℓ , 0; Σ).
1469	nℓ − df 2 (κℓ ; Σ)
1470	
1471	In particular, if maxℓ ϕℓ ≤ 1 (so that there is enough samples to perfectly fit the training data at each
1472	stage of the iterative process),
1473	we set σℓ = σ0 for all ℓ, then the above expression
1474	P 2 and for simplicity
1475	−1
1476	simplifies to ∆ ≃
1477	. More generally, consider the generic setting where
1478	ℓ σℓ /(nℓ − d) Σ
1479	P
1480	∆ ≃ (c2 /d)Σ−1 , for any c > 0, so that the previous setting corresponds to c2 = ℓ σℓ2 ϕℓ /(1 − ϕℓ ).
1481	In the particular case where p1 → 0+ , i.e only synthetic data is available for training. Theorem 1
1482	then gives
1483	
1484	
1485	
1486	df 2
1487	c2
1488	· df 2 +uκ2 tr(Σ + κId )−2 = η 2 df 2 · 1 + κ2
1489	ζ≃
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3baf6d88-5692-4940-a49f-58a4095f2f0b",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a6a18d51af7e60f09",
  "type": "user",
  "uuid": "222a36e5-5d4f-4fa7-84da-43d080fa12d6",
  "sourceToolAssistantUUID": "3baf6d88-5692-4940-a49f-58a4095f2f0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-20T15:04:48.200Z_

I have comprehensively extracted all the key content from the paper. Here is the full extracted content:

---

## Full Extracted Content: "Strong Model Collapse" (arXiv:2410.04840, ICLR 2025 Spotlight)

**Authors:** Elvis Dohmatob (FAIR, Meta), Yunzhen Feng (NYU / Meta intern), Arjun Subramonian (UCLA / Meta intern), Julia Kempe (FAIR, Meta / NYU)

---

### Abstract (verbatim)

> Within the scaling laws paradigm, which underpins the training of large neural networks like ChatGPT and Llama, we consider a supervised regression setting and establish the existance of a strong form of the model collapse phenomenon, a critical performance degradation due to synthetic data in the training corpus. Our results show that even the smallest fraction of synthetic data (e.g., as little as 1% of the total training dataset) can still lead to model collapse: larger and larger training sets do not enhance performance. We further investigate whether increasing model size, an approach aligned with current trends in training large language models, exacerbates or mitigates model collapse. In a simplified regime where neural networks are approximated via random projections of tunable size, we both theoretically and empirically show that larger models can amplify model collapse. Interestingly, our theory also indicates that, beyond the interpolation threshold (which can be extremely high for very large datasets), larger models may mitigate the collapse, although they do not entirely prevent it. Our theoretical findings are empirically verified through experiments on language models and feed-forward neural networks for images.

---

### Section 1: Introduction (verbatim paragraphs)

**Para 1:** "The term Model Collapse refers to a critical degradation in the performance of AI models, particularly when a significant portion of their training data consists of synthetic data generated by other models. As detailed in Shumailov et al. (2023), this phenomenon arises as the model gradually overfits to patterns found in synthetic data, which may not fully represent the richness or variability of real-world data. Over successive training cycles, this feedback loop results in the model reinforcing errors, biases, or oversimplifications from the synthetic data. Consequently, the model's ability to generalize to real-world data is compromised, as it increasingly relies on the distorted distribution provided by prior AI generations rather than learning accurate representations of the real world. This phenomenon was observed empirically (Hataya et al., 2023; Martínez et al., 2023a,b; Bohacek & Farid, 2023; Briesch et al., 2023; Guo et al., 2023) and described theoretically (Alemohammad et al., 2023; Bertrand et al., 2023; Dohmatob et al., 2024a,b). The connection to the breakdown of neural scaling laws (Kaplan et al., 2020) has been pointed out and analyzed in Dohmatob et al. (2024b): as data becomes more synthetic, larger training sets do not enhance performance."

**Para 2:** "The issue is especially concerning in large-scale AI systems like ChatGPT and Llama (Touvron et al., 2023; Dubey & et al., 2024), which rely heavily on vast amounts of training data to maintain their performance. If synthetic data is used in training these models, even in small quantities, the model can start producing 'gibberish' or nonsensical outputs, contains misinformation, or reflect stereotypes. This is because the model effectively starts to amplify its own mistakes (Shumailov et al., 2024). This feedback loop results in a gradual loss of model fidelity, reducing its ability to generalize or adapt to new, unseen test environments."

---

### Section 1.1: Main Contributions (verbatim)

The paper poses two research questions:
- **(Q1)** Is model collapse inevitable or can it be fixed by strategically mixing synthetic and real data?
- **(Q2)** Are larger models more prone to model collapse than smaller ones?

**Result #1: Strong Model Collapse.** "First, we establish a robust negative result which shows that model collapse generally persists even when mixing real and synthetic data, as long as the fraction of training data which is synthetic does not vanish (cf. Section 3.1 and 3.2). By synthetic data, we mean any training data from a distribution which deviates from the distribution of real data, i.e. data on which the test performance is evaluated. Thus, model collapse cannot generally be mitigated by simple adjustments such as data weighting (Jain et al., 2024; Ferbach et al., 2024) unless these strategies asymptotically remove all but a vanishing proportion of synthetic data from the training process (Section 5). Our results show that the findings of Shumailov et al. (2024); Alemohammad et al. (2023); Bertrand et al. (2023); Dohmatob et al. (2024a,c) are worse than anticipated, by considering the more realistic scenario where a mixture of synthetic and real data is used for training."

**Result #2: Model Size and Model Collapse.** "In Section 3.2, we disentangle the effect of a model's size on its ability to cope with model collapse. We show that in general, bigger models will suffer more from model collapse as soon as the deviation between the distribution of the synthetic data and real data is significant. Crucially, our theory also predicts that past the interpolation threshold point, this tendency can be reversed: large models become more robust to model collapse. Put together, these results predict the existence of a double-descent curve regarding the model collapse phenomenon. This is illustrated in Figures 1 and 2. Thus, the model collapse profile depends critically on design choices like model size."

**Experimental Validation:**
- "Toy settings, including random projections model on Gaussian data, and shallow networks fully trained on the MNIST dataset (Deng, 2012)."
- "Realistic setting of GPT-2 models trained on BabiStories (Zhang et al., 2024a), a reproduction of TinyStories (Eldan & Li, 2023) using the Mixtral-8x7B open language model (Jiang et al., 2024)."

**Approach:** "From a technical standpoint, our theoretical analysis focuses on regression problems in the classical linear setting introduced in Dohmatob et al. (2024a) for studying model collapse, and also the setting of neural networks in a simplified regime which can be approximated by random projections (Maloney et al., 2022; Bach, 2023). We employ the tools of operator-valued free probability theory (OVFPT) (Mingo & Speicher, 2017) to obtain a new bias-variance decomposition Etest ≃ B + V + ζ, of the test error evaluated on the real / true data distribution, of a model trained on a mixture of real and synthetic data. The extra term ζ then induces model collapse."

---

### Section 2: Theoretical Setup

**Data Distributions:** Two data sources:
- D1: n1 samples from real distribution P1 = P_{Σ1, w1*, σ1²}
- D2: n2 samples from synthetic distribution P2 = P_{Σ2, w2*, σ2²}
- Features: x ~ N(0, Σk); Labels: y = x⊤wk* + ε, ε ~ N(0, σk²)

**Label shift structure:**
- w1* ~ N(0, Γ)
- δ := w2* − w1* ~ N(0, Δ), independent of w1*

**Data quality metric (Definition 1):** c²(Δ) = (1/d) tr ΣΔ — captures disparity between P2 and P1; smaller = better quality synthetic data.

**Two model families:**

1. **Classical Linear Model (ridge regression):** ŵ = argmin (1/n) Σ(xi⊤w − yi)² + λ‖w‖²

   Proportionate scaling limit: d, n → ∞ with d/n → φ, n2/n → p2.

2. **Random Projections Model:** f(x) = v⊤Sx, where S is d×m random matrix with iid N(0,1/d) entries (only read-out weights v ∈ Rm are learned).

   Proportionate scaling limit: d, m, n → ∞ with d/n → φ, m/d → γ, m/n → ψ. Parameter ψ = m/n controls model size (ψ < 1 = underparameterized, ψ > 1 = overparameterized/interpolation threshold at ψ = 1).

---

### Section 3: Theorems

**Theorem 1 (Classical Linear Model):** In the proportionate scaling limit, Etest(f̂CL) ≃ B + V + ζ, where:
- V = σ² · df₂(κ;Σ)/n / (1 − df₂(κ;Σ)/n)
- B = κ² · tr ΓΣ(Σ + κId)⁻² / (1 − df₂(κ;Σ)/n)
- ζ = p2² · (1 + p1u) tr ΔΣ³(Σ + κId)⁻² + p2u tr ΔΣ(p1Σ + κId)²(Σ + κId)⁻²

The extra term ζ is responsible for model collapse. For Δ=0 (no distribution mismatch), ζ=0 and we recover the classical bias-variance decomposition.

**Strong Model Collapse:** In the scaling laws regime φ → 0+, ζ ≃ p2² tr Δ. Unless p2 → 0+ (i.e., all synthetic data discarded), the test error plateaus above baseline. This is strong model collapse.

**Corollary 1 (isotropic case, Σ = Id, under-parametrized φ ∈ (0,1), λ → 0+):**
- Etest(f̂CL) ≃ σ²φ/(1−φ) + [p2² + p2p1φ/(1−φ)] c²
- For small φ: Etest(f̂CL) ≃ σ²d/n + p2²c² + O(φ²)

Implication: test error contains irreducible term p2²c² that does not vanish as n→∞ unless p2→0.

**Theorem 2 (Random Projections Model):** Analogous decomposition Etest(f̂RP) ≃ B + V + ζ with more complex formulas involving fixed-point equations for (e, τ, u, ω). Key: ζ ≥ p2² tr ΔΣ³(Σ + θId)⁻², which scales with p2² and plateaus unless p2 → 0+.

Special case p2 → 0+ recovers Bach (2023)'s double-descent result for random projections on clean data.

---

### Section 4: Experimental Results

#### 4.1 MNIST Experiments

**Setup:** Two-layer neural networks on MNIST. Two variants:
1. Random feature model (first layer fixed randomly, only second layer trained — directly matches theory)
2. Fully trained two-layer network (theory doesn't apply directly, but trends should hold)

Labels converted to one-hot vectors; MSE loss; synthetic labels from another two-layer network with Gaussian label noise (std = 0.1); validation set for checkpoint selection.

**Training details (Appendix A.2):** SGD, batch size 128, learning rate 0.1, 400 epochs to full convergence.

**Results (Figure 7):** As p2 increases, scaling laws slow down and eventually plateau. Strong model collapse: collapse only subsides when p2 → 0. Results consistent across both random feature and fully-trained networks.

**Model size effect (Figure 6):** Models with varying hidden dimensions (100, 400, 1000, 2000, 4000, 10000) trained exclusively on synthetic data (p2=1), training sets 10,000–50,000 samples. Larger models are more susceptible to model collapse (all remain in interpolation regime).

#### 4.2 Language Modeling

**Dataset:** BabiStories (Zhang et al., 2024a) — reproduction of TinyStories using Mixtral-8x7B. Training set: 2,200,000 stories; validation set: 22,000 stories.

**Generator:** GPT-2-small (124M parameters) trained on BabiStories, then used to generate synthetic dataset using same story prompts (story beginnings + character names). Temperature=1, top-p=1. Poor quality stories (containing unwanted symbols) filtered out.

**Training recipe (Appendix A.3):**
- Architecture: GPT-2, embedding dimension d=768, 12 attention heads, context length 512 tokens
- Learning rate: 5×10⁻³
- Dropout: 0.05
- L2 weight decay: 0.1
- Warm-up: 2,000 iterations
- Objective: next-token prediction

**Impact of Synthetic Data Proportion (Figure 8, left):** GPT-2 12-layer model, p2 ∈ {0, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 0.9, 1.0}. x-axis = number of tokens (up to ~4×10⁹). Even moderate synthetic data delays scaling law progression. High-quality synthetic data (small c²) so delays are smaller but still present.

**Impact of Model Size (Figure 8, right):** Three model sizes: 12 layers (GPT-2-small, 124M), 18 layers (166M), 24 layers (204M). Embedding dimension and attention heads held constant. Synthetic dataset 10× larger than original to support scaling. Larger models maintain lower test loss at smaller token counts (benefit in overparameterized regime). After ~3×10¹⁰ tokens, smaller models outperform larger models (amplification of collapse in underparameterized regime). Below ~10¹⁰ tokens, larger models perform better (consistent with theory's prediction for overparameterized regime mitigating collapse).

**Evaluation:** Test loss on TinyStories test set.

---

### Section 5: Strategic Data Mixing

#### 5.1 Weighted Single-Step Mixing (Jain et al., 2024)

Optimization: ŵ = argmin [(1−α)/n1 Σ(xi⊤w−yi)² + α/n2 Σ(xi⊤w−yi)²] + λ‖w‖²

**Corollary 2 (small φ):** Etest(f̂CL) ≃ p2²α²c² + [(1−α)p1σ1² + αp2σ2²]φ + O(φ²)

Optimal mixing coefficient: α* = clip[0,1](1 − [(p1σ1² − p2σ2²)/(2c²)] φ)

**Key conclusion:** For fixed c > 0 and σ1, σ2 = O(1), α* → 0 as φ → 0 (i.e., must discard all synthetic data). Any fixed α ∈ (0,1] leads to Etest ≥ p2²α²c² ≳ c²: effective model collapse. Empirically confirmed in Figure 9.

#### 5.2 Dynamic / Multi-Step Mixing (Ferbach et al., 2024)

Iterative scheme: at each iteration t+1, mix n2 synthetic samples from model trained at step t with n1 real samples.

**Corollary 3:** For large t, Etest(t)(f̂CL) ≃ E/(1−p2²) + Θ(p2t²), where E ≃ σ²d/n.

**Key findings:**
- Iterative mixing recovers scaling law rate (when t ~ log(n/d)), but at cost of significant bootstrapping and large volume of real data.
- Iterative mixing underperforms vs. using only real data ("Clean") consistently — it primarily neutralizes synthetic data and relies on real data.
- With limited real data (p2 → 1): Etest(ŵ(t)) ≃ c0² + tE — increasing in t, still catastrophic collapse.

---

### Section 6: Discussion / Limitations / Future Work (verbatim)

"Our work systematically characterizes the effects of training models on mixtures of real and synthetic data, showing that model collapse is a robust phenomenon that persists even with small fractions of synthetic data, in the asymptotic regime. By introducing new mathematical tools, we extend prior work to analyze more complex mixing settings and models (random projections), broadening the scope of theoretically tractable problems. Experiments confirm our theoretical predictions across large language models (LLMs) and also fully-trained feed-forward neural networks."

"Going beyond the prevalent 'neural scaling laws' paradigm (Kaplan et al., 2020; Hoffmann et al., 2022) which is at the basis of the current trend in training LLMs, this study emphasizes the importance of preserving and labeling real data, either by curating it or avoiding unintended synthetic data in training, reflecting a shift as AI-generated data becomes prevalent. Our work also delineates the impact of model size on the model collapse profile. **Future work** will explore the effect of other model design choices like activation functions, depth, and optimization hyper-parameters like learning rate and momentum. To this end, we can leverage 'Gaussian equivalents' (Goldt et al., 2022) to extend our theory to wide, fully-trained networks in the neural tangent kernel (Jacot et al., 2018) and lazy (Chizat et al., 2019) regimes, using operator-valued free probability theory (Mingo & Speicher, 2017), like we have done in our analysis."

**Limitations (implicit):** Theory focuses on (1) Gaussian feature distributions, (2) linear labeling functions, (3) supervised regression, (4) random projections as neural network proxy. Full neural networks (with activation functions, depth, backprop) not directly covered. Practical mitigation beyond discarding synthetic data remains open.

---

### All Figure Captions

**Figure 1:** "Pareto diagram: Understanding the role of model size in model collapse. We compare the test error (on the real / true data distribution), for a random projections model (equation (5) of Section 2.2) when training is done on a mix of synthetic and real data (y-axis), versus real data only (x-axis); in both cases, the total amount of training data is fixed to n = 500. On the scatter plots, square points correspond to very high-quality synthetic data (i.e from a distribution which is close to the true data distribution), diamonds correspond to high-quality synthetic data, triangles correspond to low-quality, while stars correspond to very low-quality synthetic data. The black lines correspond to the Pareto frontiers for each level of quality of the synthetic data; the higher the frontier above the diagonal in the given setting, the more serious is the model collapse. The colorbar is the log of parametrization rate ψ = m/n, where m captures is the size of the model."
- Three panels: n2=50 (left), n2=200 (middle), n2=400 (right); n1 = 450, 300, 100 respectively; d=600, isotropic Σ=Id; c² ∈ {0, 0.1, 0.5, 1.0}.

**Figure 2:** "Illustration of our new bias-variance decomposition Etest ≃ B + V + ζ for neural networks in the simplified random projections regime (cf. Section 3.2), trained on a mixture of real and synthetic data. The sum B + V corresponds to the classical bias variance decomposition in this setup when all the training data is real. The extra term ζ is responsible for model collapse when training is done on a mixture of real and synthetic data. The scalar c² characterizes the quality of the synthetic data (cf. Definition 1), via its mismatch with the real data distribution. The vertical line corresponds to the interpolation threshold m = n, where m is the model size and n is the total sample size. Notice the well-known double-descent curve in the bias curve."
- 4-panel figure: Bias B, Variance V, Extra term ζ, Test error Etest, all as function of network width m (0–1000). Lines for c² ∈ {0.0, 0.1, 0.5, 1.0}.

**Figure 3:** "Strong model collapse in classical linear model (empirical confirmation of Corollary 1). The training dataset comprises of n = n1 + n2 samples from a mixture of n2 = p2n synthetic samples and n1 = n − n2 real samples. The real samples are from the same distribution as the real / true samples of the training dataset, while the synthetic samples are from a distribution with the same covariance structure and label noise level σ = 1, but an incorrect labelling function (epistemic error). The quality of the synthetic data is controlled by the scalar c, with c → 0 corresponding to synthetic data of perfect quality (higher values correspond to lower quality synthetic data). Solid curves correspond to experiments, and broken curves correspond to our theoretical predictions of Corollary 1; notice the perfect match. We see that even a small amount of low-quality synthetic data is enough to cause model collapse, whereby the test error of the model deviates from a perfect diagonal (ideal scaling law, corresponding to p2 = 0, i.e training on real data only)."

**Figure 4:** "Impact of model size (network width m) on model collapse. For various levels of data quality c² (cf. Definition 1) we show test error as a function of model size for various mixing ratios (darker curves correspond to higher fractions p2 of synthetic data). Error bars correspond to 5 independent runs."
- 4-panel: c²=0.0, 0.1, 0.5, 1.0; x-axis = network width m (0–1000); p2 ∈ {0.02, 0.1, 0.2, 0.4, 0.6, 0.8}.

**Figure 5:** "Impact of model size (network width m) on model collapse. As usual, solid curves correspond to experimental results (5 runs), while broken curves correspond to predictions of our theory (here, Corollary 4). Error bars correspond to 5 independent runs. Also see Figures 2 and 4."
- x-axis: network width m (0–1000); c² ∈ {0.0, 0.1, 0.5, 1.0}.

**Figure 6:** "Fully trained two-layer network on MNIST data. Impact of model size (hidden dimension, aka network width) on model collapse. Here, the model is trained solely on synthetic data (i.e p2 → 1)."
- x-axis: Number of Samples (10³–10⁴); y-axis: MSE Loss; lines for hidden dimensions {100, 400, 1000, 2000, 4000, 10000}.

**Figure 7:** "Model collapse as a function of the proportion of synthetic data. We use the MNIST dataset with regression loss. Error bars correspond to 5 runs. Left, Random feature model with hidden dimension 100,000. Right, Two-layer neural network of width (i.e hidden dimension) m = 2000."
- x-axis: Number of Samples (10²–10⁴); y-axis: MSE Loss; p2 ∈ {0, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 0.9}.

**Figure 8:** "Results on BabiStories with GPT-2 models. Synthetic BabiStories is generated with a trained GPT-2-small with the same set of prompts. (Left) Impact of the proportion of synthetic data p2 on model collapse in a language model with 12 layers. (Right) Impact of model size (number of layers) on model collapse. Here the model is trained on synthetic data only (i.e p2 = 1). The loss is evaluated on the TinyStories test set."
- Left: x-axis tokens (6×10⁸–4×10⁹); p2 ∈ {0.0, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 0.9, 1.0}; y-axis loss ~1.5–1.9.
- Right: x-axis tokens (10⁹–10¹¹); layers ∈ {12, 18, 24}; y-axis loss ~1.65–2.0.

**Figure 9:** "Failure of naive real+surrogate data mixing to solve model collapse."
- (a) n1=1000, d=500; (b) n1=10000, d=100 (φ ≤ 0.01). Solid=experiment, broken=theory (Corollary 2).

**Figure 10:** "Iterative vs Single-Step Mixing. Solid lines represent the experimental results (5 runs), while dashed lines correspond to the theoretical predictions of Corollary 3. The iterative mixing is repeated 5 times, with p1 = p2 = 0.5. 'Clean' refers to the scaling when using solely the n1 = p1n real data in the dataset."
- 3-panel: c0² = 100, 10⁻¹, 10⁻²; x-axis: Total dataset size n (10³–10⁴); log-scale y-axis; lines: Mixing (iterative), Clean, Single.

---

### Baselines / Comparisons

No competing methods benchmarked in the traditional sense. The paper compares:
- Training on real data only (p2=0) — the "ideal scaling law" / "clean" baseline
- Weighted single-step mixing (Jain et al., 2024) — shown to fail
- Iterative/dynamic mixing (Ferbach et al., 2024) — shown to underperform
- Varying synthetic proportions p2 ∈ {0, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 0.9, 1.0}

---

### Metrics

- Test error on true distribution P1 (MSE for regression/MNIST)
- Test/validation perplexity / cross-entropy loss for language modeling (evaluated on TinyStories test set)
- Scaling law exponents (implicit, via log-log plots)

---

### Datasets

1. Gaussian synthetic data (toy): d=600, Σ = power-law eigenvalues λj=C/j, n=500 (n1=300, n2=200), λ=10⁻⁸
2. MNIST (Deng, 2012): classification as regression, synthetic labels from another two-layer network with Gaussian noise (std=0.1)
3. BabiStories (Zhang et al., 2024a): 2,200,000 training + 22,000 validation stories generated by Mixtral-8x7B; evaluated on TinyStories test set

---

### Training Recipe Summary

**Toy (random projections):** No gradient descent — closed-form ridge regression.

**MNIST two-layer networks:**
- Optimizer: SGD
- Batch size: 128
- Learning rate: 0.1
- Epochs: 400 (until convergence)
- Model sizes: hidden dim ∈ {100, 400, 1000, 2000, 4000, 10000}

**Language modeling (GPT-2):**
- Architecture: GPT-2 with d=768, 12/18/24 layers, 12 attention heads, context length 512 tokens
- Parameters: 124M (12L), 166M (18L), 204M (24L)
- Learning rate: 5×10⁻³
- Dropout: 0.05
- L2 weight decay: 0.1
- Warmup: 2,000 iterations
- Generation: temperature=1, top-p=1 (nucleus sampling with p=1)
- Generator: GPT-2-small trained on BabiStories
- Synthetic dataset for model-size experiment: 10× larger than original

---

### Related Work (key citations)

- Shumailov et al. (2023, 2024 Nature): original model collapse empirical/theory
- Alemohammad et al. (2023): self-consuming generative models
- Bertrand et al. (2023): stability of iterative retraining
- Dohmatob et al. (2024a): model collapse in regression (predecessor)
- Dohmatob et al. (2024b): model collapse as change of scaling laws (predecessor, ICML 2024)
- Jain et al. (2024): weighted mixing / scaling laws for real+surrogate data
- Ferbach et al. (2024): self-consuming models with curated data / iterative mixing
- Seddik et al. (2024): statistical analysis of LM collapse
- Maloney et al. (2022): solvable model of neural scaling laws (random projections)
- Bach (2023): double descent in random feature regression
- Feng et al. (2024): beyond model collapse — synthesis with reinforcement

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "222a36e5-5d4f-4fa7-84da-43d080fa12d6",
  "isSidechain": true,
  "agentId": "a6a18d51af7e60f09",
  "requestId": "req_011CbE2HqgJKpbSSvyWar5u7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b61c9f4-3722-45b2-b220-d008879fda0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UJgX1t8E4b92CSoF28wtF3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 52661,
      "output_tokens": 7293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1963
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7293,
          "cache_read_input_tokens": 52661,
          "cache_creation_input_tokens": 1963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1963,
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
