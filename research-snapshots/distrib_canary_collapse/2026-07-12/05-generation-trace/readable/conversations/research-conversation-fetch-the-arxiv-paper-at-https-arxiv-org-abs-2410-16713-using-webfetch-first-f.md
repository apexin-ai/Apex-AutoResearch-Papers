# Research conversation: Fetch the arXiv paper at https://arxiv.org/abs/2410.16713 using WebFetch. First fetch the HTML version at https://arxiv.

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5324dfd68a7026d4.jsonl`
- **Structured JSON:** [`440ad056fd88f881a6b3.json`](../../sessions/44/440ad056fd88f881a6b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-20T15:00:59.378Z_

Fetch the arXiv paper at https://arxiv.org/abs/2410.16713 using WebFetch.

First fetch the HTML version at https://arxiv.org/html/2410.16713v2 with the prompt:
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

If the HTML version fails, try https://arxiv.org/abs/2410.16713 with the same prompt.

Then report EVERYTHING you extracted - do not summarize, give me the full extracted content. This is "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World" (ICML 2025).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a5324dfd68a7026d4",
  "type": "user",
  "uuid": "08990e9b-71a6-43f4-b5f6-9d9ea1e78d96",
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

_source line 2 · 2026-05-20T15:00:59.396Z_

```json
{
  "parentUuid": "08990e9b-71a6-43f4-b5f6-9d9ea1e78d96",
  "isSidechain": true,
  "agentId": "a5324dfd68a7026d4",
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
  "uuid": "bdba2181-0f4a-4584-bf72-029a4a5c2888",
  "timestamp": "2026-05-20T15:00:59.396Z",
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

_source line 3 · 2026-05-20T15:01:01.950Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WveBkPQuCrFhbUXnZfosUk`</summary>

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
  "parentUuid": "bdba2181-0f4a-4584-bf72-029a4a5c2888",
  "isSidechain": true,
  "agentId": "a5324dfd68a7026d4",
  "requestId": "req_011CbE2CPQMA3uLb5cardLLe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85168232-ddb1-4925-b561-de9205876ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XMGLHjYaBtHwxapMhFUcAa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9049,
      "cache_read_input_tokens": 8155,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9049
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 8155,
          "cache_creation_input_tokens": 9049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9049,
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

_source line 4 · 2026-05-20T15:01:01.957Z_

<details><summary>↩ Tool result · `toolu_01WveBkPQuCrFhbUXnZfosUk`</summary>

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
  "parentUuid": "85168232-ddb1-4925-b561-de9205876ec4",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a5324dfd68a7026d4",
  "type": "user",
  "uuid": "c686f9c3-fc32-4d82-9596-50dfc64f95c3",
  "sourceToolAssistantUUID": "85168232-ddb1-4925-b561-de9205876ec4",
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

_source line 5 · 2026-05-20T15:01:04.849Z_

I'll fetch the HTML version first, then fall back to the abstract page if needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c686f9c3-fc32-4d82-9596-50dfc64f95c3",
  "isSidechain": true,
  "agentId": "a5324dfd68a7026d4",
  "requestId": "req_011CbE2CaEyBZt7DhKKgc9MU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee10cc57-4f6e-4443-84cb-31617488d79e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TShaZ71CcV4zp8bsoYP2sB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 17204,
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

_source line 6 · 2026-05-20T15:01:06.001Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011cqFhc1au6Q1t3ijpLtVp4`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.16713v2",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee10cc57-4f6e-4443-84cb-31617488d79e",
  "isSidechain": true,
  "agentId": "a5324dfd68a7026d4",
  "requestId": "req_011CbE2CaEyBZt7DhKKgc9MU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "853803b2-7921-4298-99b5-0cf9e6964bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TShaZ71CcV4zp8bsoYP2sB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 17204,
      "output_tokens": 222,
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
          "output_tokens": 222,
          "cache_read_input_tokens": 17204,
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

_source line 7 · 2026-05-20T15:01:25.584Z_

<details><summary>↩ Tool result · `toolu_011cqFhc1au6Q1t3ijpLtVp4`</summary>

```text
# Detailed Paper Summary: "Collapse or Thrive? Perils and Promises of Synthetic Data"

## Core Contributions

This paper investigates whether training generative models on synthetic data from predecessor models causes "model collapse" (performance degradation). The researchers distinguish between two scenarios:

1. **Replace**: Data deleted after each iteration; subsequent models trained only on synthetic data
2. **Accumulate**: Real and synthetic data accumulate over iterations

Key finding: "In all three settings, we empirically find and (when possible) mathematically prove the answer is yes" that accumulation prevents collapse while replacement causes it.

## Main Experiments & Settings

### Three Primary Generative Modeling Settings

**Multivariate Gaussian Modeling**
- Start with n samples from 𝒩(μ⁽⁰⁾, Σ⁽⁰⁾)
- Iteratively fit Gaussians and sample synthetic data
- Replace scenario: covariance collapses to 0, mean diverges
- Accumulate scenario: both stabilize quickly
- Mathematical proof provided (Theorem 1): variance converges to σ₀² · sin(π/√n)/(π/√n)

**Kernel Density Estimation (KDE)**
- Four datasets: Blobs, Circles, Moons, Swiss Roll from sklearn
- Metric: Negative log-likelihood (NLL) on real test data
- Replace: rapid NLL increase across iterations
- Accumulate: NLL remains stable
- Note: "asymptotically diverges in theory" but at glacial rates practically

**Supervised Language Model Finetuning**
- Model: Google Gemma2 2B
- Dataset: Nvidia HelpSteer2 (~12.5k samples)
- Replace: eval loss increases
- Accumulate: eval loss remains low
- Conclusion: "deleting data after each iteration leads to collapse whereas accumulating data avoids collapse"

### Secondary Setting: Fixed Compute Budget (Accumulate-Subsample)

Introduces practical middle-ground where accumulated data are subsampled for constant compute:

**Five Generative Settings Tested:**
1. Multivariate Gaussian modeling
2. Language model instruction finetuning
3. Kernel density estimation
4. Linear regression
5. Language model pretraining on TinyStories

**Key Finding**: Test loss plateaus (unlike Replace's divergence) but deteriorates faster than pure Accumulate.

## Real vs. Synthetic Data Analysis

**Experimental Setup** (Language Model Finetuning):
- Generated 100k+ completions from finetuned Gemma 2B
- Tested combinations of varying real/synthetic data quantities
- Statistical analysis: R² values of 0.59 (cardinality) vs 0.34 (proportion)

**Critical Insight**: "When real data are plentiful, synthetic data is harmful, but when real data are scarce, there exists an optimal amount of synthetic data that are helpful."

Specifically:
- With ≤1024 real samples: some synthetic data improves loss
- With abundant real data: synthetic data degrades performance
- Quote: "removing synthetic data from training sets can improve test loss more than gathering additional high-quality data"

## Mathematical Contributions

**Theorem 1** (Univariate Gaussian): Provides explicit convergence rates for mean and variance under accumulation:
- Expected variance: σ₀² · ∏(1 - 1/(k²n)) as t→∞
- Expected mean error: σ₀² · (1 - sin(π/√n)/(π/√n))

**Lemmas 2-3**: Supporting results characterizing recursive mean/variance expressions.

## Datasets & Metrics

| Setting | Dataset | Metric |
|---------|---------|--------|
| Gaussian | Synthetic (generated) | Wasserstein-2 distance |
| KDE | sklearn (4 datasets) | Negative log-likelihood |
| LM SFT | HelpSteer2 | Eval loss |
| Pretraining | TinyStories | Perplexity/eval loss |
| Linear Reg | Synthetic | MSE |

## Key Figures Summary

- **Figure 1**: Gaussian collapse visualization (means drift, covariances collapse in Replace; both stabilize in Accumulate)
- **Figure 2**: KDE NLL increases rapidly with Replace, stays stable with Accumulate
- **Figure 3**: LM finetuning shows identical Replace/Accumulate divergence pattern
- **Figure 4**: Fixed-compute results across 5 settings; loss curves between Replace and pure Accumulate
- **Figure 5**: Heatmaps showing non-trivial interaction between real/synthetic data quantities

## Technical Details

**Training Setup for LM Experiments:**
- Model: Google Gemma2 2B
- Real dataset: HelpSteer2 instruction-following data
- Synthetic generation: Greedy decoding from finetuned models
- No explicit optimizer/learning rate details provided in main text

**Key Methodological Choice**: All experiments use unfiltered synthetic data (pessimistic scenario), ignoring quality filtering that practitioners employ in reality.

## Limitations & Future Work

The authors acknowledge:
- No data quality filtering applied (contrasts with real practice)
- Results limited to relatively small models/datasets due to compute constraints
- Need to understand conditions where synthetic data improves performance

Future directions proposed:
- Combining synthetic generation with filtering techniques
- Identifying which conditions enable synthetic data to improve test loss
- Understanding why accumulation can outperform real-only training

## Philosophical Framing

The paper contextualizes findings within realistic internet dynamics. A quote illustrates this: deleting data "is not what is happening on the internet...the classics will continue to be part of the training data set." This motivates why Accumulate better reflects real-world pretraining practices.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "853803b2-7921-4298-99b5-0cf9e6964bb1",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a5324dfd68a7026d4",
  "type": "user",
  "uuid": "6012a6f4-5dd7-4f72-a20f-21c3d6b2c611",
  "sourceToolAssistantUUID": "853803b2-7921-4298-99b5-0cf9e6964bb1",
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

_source line 8 · 2026-05-20T15:01:30.169Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XAku9UGsaGs8JcpJRKvCwt`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.16713v2",
  "prompt": "Extract verbatim text from:\n1. The complete Introduction section - every paragraph word for word\n2. The contribution statement at the end of the intro\n3. The Related Work section\n4. All figure captions (Figure 1, Figure 2, Figure 3, etc.) verbatim\n5. All table captions verbatim\n6. The conclusion section verbatim\n7. Author names and affiliations\n8. Abstract verbatim\nDo not summarize. Quote the actual text from the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6012a6f4-5dd7-4f72-a20f-21c3d6b2c611",
  "isSidechain": true,
  "agentId": "a5324dfd68a7026d4",
  "requestId": "req_011CbE2EKD9L9BTjCbuRZriY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40934bfe-35b2-4018-86b6-a0beda981222",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014vvSRqN1LL2wWmTRKYzuxp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1605,
      "cache_read_input_tokens": 18636,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1605
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 18636,
          "cache_creation_input_tokens": 1605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1605,
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

_source line 9 · 2026-05-20T15:02:02.814Z_

<details><summary>↩ Tool result · `toolu_01XAku9UGsaGs8JcpJRKvCwt`</summary>

```text
# Extraction from "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"

## Authors and Affiliations

Joshua Kazdan (Statistics, Stanford University), Rylan Schaeffer (Computer Science, Stanford University), Apratim Dey (Statistics, Stanford University), Matthias Gerstgrasser (Harvard SEAS & Stanford Computer Science), Rafael Rafailov (Computer Science, Stanford University), David Donoho (Statistics, Stanford University), Sanmi Koyejo (Computer Science, Stanford University)

## Abstract

"The increasing presence of AI-generated content on the internet raises a critical question: What happens when generative machine learning models are pretrained on web-scale datasets containing data created by earlier models? Some authors prophesy model collapse under a 'replace' scenario: a sequence of models, the first trained with real data and each later one trained only on synthetic data from its preceding model."

The paper examines whether model performance degrades under different data accumulation scenarios across multiple generative modeling settings.

## Introduction Section

"With each passing day, the internet contains increasingly more AI-generated content (Altman, 2024). What is the impact of this for future of deep generative models pretrained on web-scale datasets containing data generated by their predecessors?"

"Previous work forewarned that such model-data feedback loops can exhibit model collapse, a phenomenon whereby model performance degrades with each model-fitting iteration such that newer models trend towards useless (Shumailov et al., 2023)."

"This prophecy is deeply concerning because society is increasingly relying on these deep generative models (Bommasani et al., 2022; Reuel et al., 2024; Perrault & Clark, 2024; Kapoor et al., 2024), and model collapse threatens that future models will be made useless as society's current data practices pollute the pretraining data supply."

"However, the model collapse literature is replete with different experimental methodologies and different mathematical assumptions of different generative models, with different papers reaching different conclusions."

"In this work, we extend the accumulate workflow studied in Gerstgrasser et al. (2024) to cover several settings previously not studied in the literature to exhibit its effectiveness over the replace workflow."

"We begin by testing the following hypothesis – that model collapse emerges in a scenario where models are trained on evolving datasets built by deleting past data en masse; and model collapse is avoided in a scenario where the training datasets instead accumulate all real and synthetic data."

"We consider whether these claims hold in three new generative model task settings pointed to by recent prominent work; we find the claims hold."

"We then compare three clear dataset evolution scenarios, focusing on a new middle ground where data accumulate over time but each model is trained under a fixed compute budget; in this middle ground, we find that losses on real test data climb faster than without a compute budget but plateau to lower values than if data are deleted en masse after each model-fitting iteration."

"These results are consistent across five different generative modeling settings. Lastly, we investigate, in a specific situation, whether the proportion or cardinality of initial real data matters more for preventing model collapse and discover a non-trivial interaction between real and synthetic data: when real data are scarce, an appropriate amount of synthetic data reduces the test loss on real data, whereas when real data are ample, synthetic data increases the test loss on real data."

"Altogether, our work provides valuable comprehensive insights for predicting likely futures of deep generative models pretrained on web-scale data."

## Related Work

"The limitations of using AI-generated images to train other image models have been well-documented since 2022 (Hataya et al. (2023))."

"Shumailov et al. (2023) initially sounded alarms about synthetic data for training language models by showing that a model trained repeatedly on its own outputs exhibits severely denigrated quality."

"This theory and empirical work was quickly extended to many new settings (Alemohammad et al. (2024); Bertrand et al. (2024); Dohmatob et al. (2024b; a); Marchi et al. (2024))."

"The phenomenon that Shumailov identified as 'model collapse' still does not have a universally agreed upon, rigorous definition."

"Shumailov classified model collapse as a 'degenerative process affecting generations of learned generative models, in which the data they generate end up polluting the training set of the next generation.'"

"Dohmatob et al. (2024b) examine model collapse as an alteration of scaling law curves when training on synthetic as opposed to real data."

"In their theory sections, Shumailov et al. (2024) and Gerstgrasser et al. (2024) explore model collapse by asking when certain models exhibit divergent test loss after multiple iterations of training."

"In this paper, we take model collapse by its literal meaning: that model performance deteriorates catastrophically when models are trained on synthetic data."

"Within the model collapse literature, a variety of data dynamics have been studied, which vary in how 'real' data is discarded or retained, how 'synthetic' data is generated, and how each is (or is not) incorporated into future training sets (Martínez et al. (2023); Mobahi et al. (2020); Dohmatob et al. (2024a))."

"A common feature of many of these is that at least some real data is discarded, often because total dataset size is kept constant across model-fitting iterations."

"However, Gerstgrasser et al. (2024) note that this may not be representative of real-world dynamics, and that model collapse is avoided when data accumulates."

"What is not clear, however, is whether this claim holds universally, including in the specific settings studied in other prior work. We help close this gap by extending Gerstgrasser's empirical and theoretical analysis to several of these settings."

"Where model collapse can be seen as studying a worst-case scenario, it has also been observed that some kinds of synthetic data have a positive effect."

"Dohmatob et al. (2024b) and Jain et al. (2024) find that certain amounts of synthetic data can improve model performance, and Ferbach et al. (2024b) suggest that with curation, self-consuming loops can improve alignment with human preferences."

"A growing literature on how to filter and harness synthetic data has achieved impressive results on a variety of benchmarks (Zelikman et al. (2024); Li et al. (2024a); Yang et al. (2024)), raising interesting questions about the limits of when unfiltered synthetic data can help."

"In this vein, we answer a question posed by Gerstgrasser et al. (2024): does the proportion or the raw amount of real data in a mixed training set have a greater impact on test loss?"

"In the process, we find that small amounts of synthetic data can improve test loss when real data is scarce."

## Figure Captions

**Figure 1:** "Model Collapse in Multivariate Gaussian Modeling. Top: Previous work (Shumailov et al., 2024) proves model collapse occurs if one iteratively fits means and covariances to data and then samples new data from a Gaussian with the fitted parameters (left). We demonstrate that if one doesn't delete all data after each model-fitting iteration - i.e., if data accumulate - then model collapse does not occur (right)."

**Figure 2:** "Model Collapse in Kernel Density Estimation. Left: We consider 4 standard datasets from sklearn: Blobs, Circles, Moons and Swiss Roll. Center: For all four datasets, deleting data en masse causes the negative log likelihoods (NLL) of real test data to increase with each model-fitting iteration. Right: For all four datasets, accumulating data avoids model collapse."

**Figure 3:** "Model Collapse in Supervised Finetuning of Language Models. Finetuning Google's Gemma2 models on Nvidia's HelpSteer 2 dataset demonstrates that model collapse occurs if previous data are replaced after each model-fitting iteration (left), whereas model collapse is avoided if new synthetic data instead accumulate with previous real and synthetic data (right)."

**Figure 4:** "Model Collapse Under a Fixed Compute Budget. We compare deleting data after each model-fitting iteration (Replace) and accumulating data after each iteration (Accumulate) with a new fixed-compute data paradigm Accumulate-Subsample."

**Figure 5:** "The Value of Synthetic Data in Supervised Finetuning of Language Models. Finetuning Google's Gemma 2 2B on Nvidia's HelpSteer 2 dataset on different combinations of real and synthetic data demonstrates that loss grows with the number of synthetic data."

## Discussion Section

"Our work sought extend understanding of model collapse in the replace and accumulate workflows. We demonstrated in three new generative modeling settings that accumulating data over time avoids model collapse, whereas replacing data over time induces model collapse."

"We then demonstrated in five generative modeling settings that even when each model is trained on a fixed compute budget with a mixture of real and synthetic data, model performance does deteriorate more, but still tends to plateau."

"The consistency of these results across different model types and datasets suggests that this distinction is a general phenomenon, and is not specific to any particular model, dataset, or learning algorithm."

"Lastly, we explored the value of synthetic data for reducing the test loss on real data and found two different regimes: when real data are plentiful, synthetic data is harmful, but when real data are scarce, there exists an optimal amount of synthetic data that are helpful."

"In our view, the data paradigm in which synthetic data accumulates from a host of models in conjunction with a constant influx of real-world data is more realistic."

"Under such dynamics, where new synthetic data are added to existing real and synthetic data, model collapse appears unlikely."

"Our experiments take a pessimistic viewpoint, in the sense that our experiments pay no attention to the quality of data, whereas in practice, engineers heavily filter data based on various indicators of data quality."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40934bfe-35b2-4018-86b6-a0beda981222",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a5324dfd68a7026d4",
  "type": "user",
  "uuid": "37c4c4cf-46e1-4e59-b842-df2b823eb0c5",
  "sourceToolAssistantUUID": "40934bfe-35b2-4018-86b6-a0beda981222",
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

_source line 10 · 2026-05-20T15:02:08.916Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WnbRgQh82T4SM9vUZdRpku`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.16713v2",
  "prompt": "Extract verbatim text from the Methods section and Experiments section. I need:\n1. The complete Methods/Approach section with all mathematical formulations, algorithms, and descriptions\n2. Complete details on the experimental setup: model architectures, dataset sizes, number of iterations, sample sizes\n3. All numerical results quoted in the text (exact numbers, percentages, metrics)\n4. The training recipe: optimizer name, learning rate, batch size, number of epochs, hardware used (GPU type)\n5. How synthetic data is generated in each setting\n6. How many iterations are run in each experiment\n7. Any hyperparameter details\n8. The fixed compute budget (Accumulate-Subsample) method details\nQuote all text verbatim without summarizing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37c4c4cf-46e1-4e59-b842-df2b823eb0c5",
  "isSidechain": true,
  "agentId": "a5324dfd68a7026d4",
  "requestId": "req_011CbE2H4auNKvJfCdoTHsBk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "403fba99-9478-4bfa-89ba-e715ccee9025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018xJokK8wsjxjkj4KkmYCv9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2527,
      "cache_read_input_tokens": 20241,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2527
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 20241,
          "cache_creation_input_tokens": 2527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2527,
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

_source line 11 · 2026-05-20T15:02:23.900Z_

<details><summary>↩ Tool result · `toolu_01WnbRgQh82T4SM9vUZdRpku`</summary>

```text
# Methods and Experiments Extraction

## Methods Section

The paper does not contain a dedicated "Methods" section. Instead, methodologies are integrated into Section 3 (Testing Model Collapse Claims) and Section 4 (Fixed Compute Budget).

### Multivariate Gaussian Modeling

**Setup:** "We begin with n real data drawn from a multivariate Gaussian with mean μ(0) and covariance Σ(0): X₁(0),…,Xₙ(0)∼i.i.d.𝒩(μ(0),Σ(0))."

**Replace Scenario:** Mean estimation: "μ̂ᴿᵉᵖˡᵃᶜᵉ⁽ᵗ⁺¹⁾ = 1/n ∑ⱼ₌₁ⁿ Xⱼ⁽ᵗ⁾" and covariance: "Σ̂ᴿᵉᵖˡᵃᶜᵉ⁽ᵗ⁺¹⁾ = 1/(n-1) ∑ⱼ₌₁ⁿ (Xⱼ⁽ᵗ⁾ − μ̂ᴿᵉᵖˡᵃᶜᵉ⁽ᵗ⁺¹⁾)(Xⱼ⁽ᵗ⁾ − μ̂ᴿᵉᵖˡᵃᶜᵉ⁽ᵗ⁺¹⁾)ᵀ"

**Accumulate Scenario:** "μ̂ᴬᶜᶜᵘᵐᵘˡᵃᵗᵉ⁽ᵗ⁺¹⁾ = 1/(n(t+1)) ∑ᵢ₌₀ᵗ ∑ⱼ₌₁ⁿ Xⱼ⁽ⁱ⁾"

**Data Generation:** "X₁⁽ᵗ⁾,…,Xₙ⁽ᵗ⁾|μ̂ᴿᵉᵖˡᵃᶜᵉ⁽ᵗ⁾,Σ̂ᴿᵉᵖˡᵃᶜᵉ⁽ᵗ⁾∼i.i.d.𝒩(μ̂ᴿᵉᵖˡᵃᶜᵉ⁽ᵗ⁾,Σ̂ᴿᵉᵖˡᵃᶜᵉ⁽ᵗ⁾)"

**Experimental Parameters:** "Number of Samples Per Iteration: 316"

### Kernel Density Estimation

**Replace KDE:** "p̂ᴿᵉᵖˡᵃᶜᵉ⁽ᵗ⁺¹⁾(x) = 1/(nh) ∑ⱼ₌₁ⁿ K((x−Xⱼ⁽ᵗ⁾)/h)"

**Accumulate KDE:** "p̂ᴬᶜᶜᵘᵐᵘˡᵃᵗᵉ⁽ᵗ⁺¹⁾(x) = 1/(nh(t+1)) ∑ᵢ₌₀ᵗ ∑ⱼ₌₁ⁿ K((x−Xⱼ⁽ⁱ⁾)/h)"

**Kernel and Evaluation:** "We consider a standard Gaussian kernel" and "We evaluate the performance using the negative log-likelihood (NLL) on real held-out test data"

**Datasets:** "Four standard synthetic datasets from sklearn: blobs, circles, moons, and swiss roll"

### Supervised Finetuning of Language Models

**Model and Data:** "We choose Google's Gemma2 2B model" with "Nvidia's HelpSteer2 dataset"

**Data Amounts:** Replace: "∼12.5k"; Accumulate: "∼12.5k*t"

### Linear Regression

**Setup:** "We begin with our real covariates X∈ℝⁿˣᵈ and true linear relationship w(0). Initializing ŵ(0)=w(0), we sample the regression targets as: y(t)=Xŵ(t)+E(t); E(t)∼𝒩(0,σ²Iₐ)"

**Fitting:** "ŵ(t+1) = (XᵀX)⁻¹Xᵀy(t)"

## Experiments Section

### Fixed Compute Budget (Accumulate-Subsample)

**Five Settings Tested:** "Multivariate Gaussian modeling, language model instruction finetuning, kernel density estimation, linear regression and language model pretraining"

**Language Model Details:** "GPT and Llama variants on TinyStories"

**Key Findings:** Test loss "lies between the test losses of Replace and Accumulate" and "typically plateaus for both Accumulate-Subsample and Accumulate, whereas test losses for Replace typically diverge"

### Cardinality vs. Proportion of Real Data

**Experiment Setup:** "We sample 100k completions from the finetuned model and filter for those that are fewer than 512 tokens in length. This leaves us with over 55,000 remaining completions."

**Statistical Results:** R² for transformed real data: "0.59"; for proportion: "0.34"

**P-values:** "6.9×10⁻²⁵ and 4.6×10⁻²⁵"

**Threshold Finding:** "When the number of real data is 1024 or lower, we find that there is a small but non-zero amount of synthetic data that improves the test loss"

**Key Observation:** "Datasets containing only real data prove to be more valuable than datasets that contain ten times more real data mixed with synthetic data"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "403fba99-9478-4bfa-89ba-e715ccee9025",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a5324dfd68a7026d4",
  "type": "user",
  "uuid": "6666b687-a39a-465a-a0f9-3960c6689a28",
  "sourceToolAssistantUUID": "403fba99-9478-4bfa-89ba-e715ccee9025",
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

_source line 12 · 2026-05-20T15:02:30.219Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0137LkvT32Lf7FTswLNbwWwJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.16713v2",
  "prompt": "Extract the following verbatim:\n1. ALL training hyperparameters for the language model experiments: optimizer, learning rate, batch size, number of epochs, sequence length, hardware (GPU type and count)\n2. The exact Theorem 1 statement with all mathematical notation\n3. Exact numbers from all tables (Table 1, Table 2, etc.) if any exist\n4. The exact abstract - all sentences\n5. The contribution/summary bullets at the end of the introduction\n6. Any appendix content visible on this page\n7. The paper's section structure (all section and subsection titles)\nDo NOT summarize. Return verbatim text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6666b687-a39a-465a-a0f9-3960c6689a28",
  "isSidechain": true,
  "agentId": "a5324dfd68a7026d4",
  "requestId": "req_011CbE2JcWZgPwRBCQJtBWsr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0a5c338-18be-4832-a3e1-efe5a4867765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EFQQ5z6uyenvy72ob4pGim",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1886,
      "cache_read_input_tokens": 22768,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 22768,
          "cache_creation_input_tokens": 1886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1886,
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

_source line 13 · 2026-05-20T15:02:45.071Z_

<details><summary>↩ Tool result · `toolu_0137LkvT32Lf7FTswLNbwWwJ`</summary>

```text
# Extraction from Research Paper

## 1. Training Hyperparameters for Language Model Experiments

The document does not provide explicit hyperparameter specifications for most language model experiments. For supervised finetuning on HelpSteer2 with Gemma 2 2B, the paper states: "We choose Google's Gemma2 2B model (Team et al., [2024](https://arxiv.org/html/2410.16713v2#bib.bib40)) because it is high performing and relatively small" but does not list optimizer, learning rate, batch size, epochs, sequence length, or hardware specifications in the visible content.

For TinyStories pretraining experiments, the document references "small variants of common large language models – GPT (Radford et al., [2019](https://arxiv.org/html/2410.16713v2#bib.bib33); Brown et al., [2020](https://arxiv.org/html/2410.16713v2#bib.bib9)) and Llama" but provides no hyperparameter details.

## 2. Theorem 1 (Complete Statement)

"For notational efficiency, for a univariate Gaussian, let μ^(t) and σ^(t) denote μ^Accumulate(t) and Σ^Accumulate(t). Suppose that the mean and covariance are updated as in Eqns. 5 and 6. Then: 𝔼(σt²)=σ0²·∏k=1t(1−1/k²n)→σ0²·(sin(π/√n)/(π/√n)) and 𝔼[(μt−μ0)²]=σ0²·(1−∏k=1t(1−1/k²n))→σ0²·(1−sin(π/√n)/(π/√n))."

## 3. Tables

No numerical tables (Table 1, Table 2, etc.) appear in the provided content.

## 4. Complete Abstract

"The increasing presence of AI-generated content on the internet raises a critical question: What happens when generative machine learning models are pretrained on web-scale datasets containing data created by earlier models? Some authors prophesy model collapse under a 'replace' scenario: a sequence of models, the first trained with real data and each later one trained only on synthetic data from its preceding model. In this scenario, models successively degrade. Others see collapse as avoidable; in an 'accumulate' scenario, a sequence of models is trained, but each training uses all real and synthetic data generated so far. In this work, we deepen and extend the study of these contrasting scenarios. First, collapse versus avoidance of collapse is studied by comparing the replace and accumulate scenarios on each of three prominent generative modeling settings; we find the same contrast emerges in all three settings. Second, we study a compromise scenario; the available data remains the same as in the accumulate scenario – but unlike accumulate and like replace, each model is trained using a fixed compute budget; we demonstrate that model test loss on real data is larger than in the accumulate scenario, but apparently plateaus, unlike the divergence seen with replace. Third, we study the relative importance of cardinality and proportion of real data for avoiding model collapse. Surprisingly, we find a non-trivial interaction between real and synthetic data, where the value of synthetic data for reducing test loss depends on the absolute quantity of real data. Our insights are particularly important when forecasting whether future frontier generative models will collapse or thrive, and our results open avenues for empirically and mathematically studying the context-dependent value of synthetic data."

## 5. Contribution Summary (from Introduction)

The paper does not present explicit bullet points of contributions. Instead, it poses and answers research questions throughout Section 1 and Section 3.

## 6. Visible Appendix Content

Appendix A (Iterative Gaussian Model Fitting) contains Lemma 2, Lemma 3, and related proofs. Appendix section headings visible are: A.1 Setup, and references to Appendices B, C, and D (though full content not shown).

## 7. Complete Section Structure

1. Introduction: Model Collapse & Why It Matters
2. Related Work
3. Testing Two Model Collapse Claims (3.1 Multivariate Gaussian; 3.2 KDE; 3.3 Language Models)
4. Model Collapse Under Fixed Compute Budget
5. Cardinality vs Proportion of Real Data
6. Discussion
7. Future Directions
8. Acknowledgements
9. Appendices A-D
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0a5c338-18be-4832-a3e1-efe5a4867765",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a5324dfd68a7026d4",
  "type": "user",
  "uuid": "6803a0b9-8aac-476d-91e1-7a4980ab99f4",
  "sourceToolAssistantUUID": "c0a5c338-18be-4832-a3e1-efe5a4867765",
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

_source line 14 · 2026-05-20T15:04:02.505Z_

Here is the full extracted content from the paper "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World" (arXiv 2410.16713v2, ICML 2025):

---

## Authors & Affiliations

Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David Donoho, Sanmi Koyejo — Stanford University (Statistics & CS) and Harvard SEAS.

---

## Abstract (verbatim)

"The increasing presence of AI-generated content on the internet raises a critical question: What happens when generative machine learning models are pretrained on web-scale datasets containing data created by earlier models? Some authors prophesy model collapse under a 'replace' scenario: a sequence of models, the first trained with real data and each later one trained only on synthetic data from its preceding model. In this scenario, models successively degrade. Others see collapse as avoidable; in an 'accumulate' scenario, a sequence of models is trained, but each training uses all real and synthetic data generated so far. In this work, we deepen and extend the study of these contrasting scenarios. First, collapse versus avoidance of collapse is studied by comparing the replace and accumulate scenarios on each of three prominent generative modeling settings; we find the same contrast emerges in all three settings. Second, we study a compromise scenario; the available data remains the same as in the accumulate scenario – but unlike accumulate and like replace, each model is trained using a fixed compute budget; we demonstrate that model test loss on real data is larger than in the accumulate scenario, but apparently plateaus, unlike the divergence seen with replace. Third, we study the relative importance of cardinality and proportion of real data for avoiding model collapse. Surprisingly, we find a non-trivial interaction between real and synthetic data, where the value of synthetic data for reducing test loss depends on the absolute quantity of real data. Our insights are particularly important when forecasting whether future frontier generative models will collapse or thrive, and our results open avenues for empirically and mathematically studying the context-dependent value of synthetic data."

---

## Introduction (verbatim excerpts)

"With each passing day, the internet contains increasingly more AI-generated content (Altman, 2024). What is the impact of this for future of deep generative models pretrained on web-scale datasets containing data generated by their predecessors?"

"Previous work forewarned that such model-data feedback loops can exhibit model collapse, a phenomenon whereby model performance degrades with each model-fitting iteration such that newer models trend towards useless (Shumailov et al., 2023)."

"This prophecy is deeply concerning because society is increasingly relying on these deep generative models (Bommasani et al., 2022; Reuel et al., 2024; Perrault & Clark, 2024; Kapoor et al., 2024), and model collapse threatens that future models will be made useless as society's current data practices pollute the pretraining data supply."

"However, the model collapse literature is replete with different experimental methodologies and different mathematical assumptions of different generative models, with different papers reaching different conclusions."

"In this work, we extend the accumulate workflow studied in Gerstgrasser et al. (2024) to cover several settings previously not studied in the literature to exhibit its effectiveness over the replace workflow."

"We begin by testing the following hypothesis – that model collapse emerges in a scenario where models are trained on evolving datasets built by deleting past data en masse; and model collapse is avoided in a scenario where the training datasets instead accumulate all real and synthetic data."

"We consider whether these claims hold in three new generative model task settings pointed to by recent prominent work; we find the claims hold."

"We then compare three clear dataset evolution scenarios, focusing on a new middle ground where data accumulate over time but each model is trained under a fixed compute budget; in this middle ground, we find that losses on real test data climb faster than without a compute budget but plateau to lower values than if data are deleted en masse after each model-fitting iteration."

"These results are consistent across five different generative modeling settings. Lastly, we investigate, in a specific situation, whether the proportion or cardinality of initial real data matters more for preventing model collapse and discover a non-trivial interaction between real and synthetic data: when real data are scarce, an appropriate amount of synthetic data reduces the test loss on real data, whereas when real data are ample, synthetic data increases the test loss on real data."

"Altogether, our work provides valuable comprehensive insights for predicting likely futures of deep generative models pretrained on web-scale data."

---

## Paper Section Structure

1. Introduction: Model Collapse & Why It Matters
2. Related Work
3. Testing Two Model Collapse Claims
   - 3.1 Multivariate Gaussian
   - 3.2 KDE
   - 3.3 Language Models
4. Model Collapse Under Fixed Compute Budget
5. Cardinality vs Proportion of Real Data
6. Discussion
7. Future Directions
8. Acknowledgements
9. Appendices A–D

---

## Related Work (verbatim excerpts)

"The limitations of using AI-generated images to train other image models have been well-documented since 2022 (Hataya et al. (2023))."

"Shumailov et al. (2023) initially sounded alarms about synthetic data for training language models by showing that a model trained repeatedly on its own outputs exhibits severely denigrated quality."

"The phenomenon that Shumailov identified as 'model collapse' still does not have a universally agreed upon, rigorous definition."

"Shumailov classified model collapse as a 'degenerative process affecting generations of learned generative models, in which the data they generate end up polluting the training set of the next generation.'"

"Dohmatob et al. (2024b) examine model collapse as an alteration of scaling law curves when training on synthetic as opposed to real data."

"In their theory sections, Shumailov et al. (2024) and Gerstgrasser et al. (2024) explore model collapse by asking when certain models exhibit divergent test loss after multiple iterations of training."

"In this paper, we take model collapse by its literal meaning: that model performance deteriorates catastrophically when models are trained on synthetic data."

"A common feature of many of these is that at least some real data is discarded, often because total dataset size is kept constant across model-fitting iterations."

"However, Gerstgrasser et al. (2024) note that this may not be representative of real-world dynamics, and that model collapse is avoided when data accumulates."

"Where model collapse can be seen as studying a worst-case scenario, it has also been observed that some kinds of synthetic data have a positive effect."

"Dohmatob et al. (2024b) and Jain et al. (2024) find that certain amounts of synthetic data can improve model performance, and Ferbach et al. (2024b) suggest that with curation, self-consuming loops can improve alignment with human preferences."

"A growing literature on how to filter and harness synthetic data has achieved impressive results on a variety of benchmarks (Zelikman et al. (2024); Li et al. (2024a); Yang et al. (2024)), raising interesting questions about the limits of when unfiltered synthetic data can help."

"In this vein, we answer a question posed by Gerstgrasser et al. (2024): does the proportion or the raw amount of real data in a mixed training set have a greater impact on test loss? In the process, we find that small amounts of synthetic data can improve test loss when real data is scarce."

---

## Methods

### Two Core Scenarios (Replace vs. Accumulate)

**Replace**: Data deleted after each iteration; each subsequent model trained only on n synthetic samples from the preceding model.

**Accumulate**: Real and all synthetic data accumulate; each model trained on all n·(t+1) samples up to iteration t.

**Accumulate-Subsample** (new middle ground): Data accumulates but each model is trained on a subsampled fixed-size dataset (fixed compute budget).

### Multivariate Gaussian

- Start: n real samples from N(μ⁽⁰⁾, Σ⁽⁰⁾)
- Replace: μ̂ = (1/n)Σⱼ Xⱼ⁽ᵗ⁾; Σ̂ = (1/(n-1))Σⱼ (Xⱼ⁽ᵗ⁾ - μ̂)(…)ᵀ
- Accumulate: μ̂ = (1/n(t+1)) Σᵢ₌₀ᵗ Σⱼ Xⱼ⁽ⁱ⁾
- n = 316 samples per iteration

**Theorem 1** (Univariate Gaussian, Accumulate):
- 𝔼(σₜ²) = σ₀² · ∏ₖ₌₁ᵗ (1 - 1/(k²n)) → σ₀² · sin(π/√n)/(π/√n)
- 𝔼[(μₜ - μ₀)²] = σ₀² · (1 - ∏ₖ₌₁ᵗ (1 - 1/(k²n))) → σ₀² · (1 - sin(π/√n)/(π/√n))

Under Replace: covariance collapses to 0, mean diverges.

### KDE

- Replace: p̂⁽ᵗ⁺¹⁾(x) = (1/nh) Σⱼ K((x - Xⱼ⁽ᵗ⁾)/h)
- Accumulate: p̂⁽ᵗ⁺¹⁾(x) = (1/nh(t+1)) Σᵢ₌₀ᵗ Σⱼ K((x - Xⱼ⁽ⁱ⁾)/h)
- Kernel: standard Gaussian kernel
- Metric: Negative log-likelihood (NLL) on real held-out test data
- Datasets: 4 from sklearn — Blobs, Circles, Moons, Swiss Roll

### Language Model SFT

- Model: Google Gemma2 2B ("high performing and relatively small")
- Dataset: Nvidia HelpSteer2 (~12,500 samples)
- Replace: always ~12.5k samples (only synthetic from previous model)
- Accumulate: ~12.5k × t samples
- Synthetic generation: greedy decoding from finetuned models
- 100k completions generated; filtered to <512 tokens → ~55,000 remaining

### Language Model Pretraining (Fixed Compute setting only)

- Dataset: TinyStories
- Models: small GPT and Llama variants

### Linear Regression

- Setup: X ∈ ℝⁿˣᵈ, true weight w⁽⁰⁾; y⁽ᵗ⁾ = Xŵ⁽ᵗ⁾ + ε⁽ᵗ⁾; ε⁽ᵗ⁾ ~ N(0, σ²Iₐ)
- Fitting: ŵ⁽ᵗ⁺¹⁾ = (XᵀX)⁻¹Xᵀy⁽ᵗ⁾

Note: explicit hyperparameters (optimizer, LR, batch size, GPU type) are not reported in the visible main text; they may be in an appendix not fully rendered.

---

## Key Quantitative Results

- R² (cardinality of real data vs. test loss): **0.59** (p = 6.9×10⁻²⁵)
- R² (proportion of real data vs. test loss): **0.34** (p = 4.6×10⁻²⁵)
- Cardinality matters more than proportion.
- When real data ≤ 1024 samples: a small non-zero amount of synthetic data reduces test loss.
- When real data is abundant: any synthetic data increases test loss.
- "Datasets containing only real data prove to be more valuable than datasets that contain ten times more real data mixed with synthetic data."

---

## Figure Captions (verbatim)

**Figure 1**: "Model Collapse in Multivariate Gaussian Modeling. Top: Previous work (Shumailov et al., 2024) proves model collapse occurs if one iteratively fits means and covariances to data and then samples new data from a Gaussian with the fitted parameters (left). We demonstrate that if one doesn't delete all data after each model-fitting iteration - i.e., if data accumulate - then model collapse does not occur (right)."

**Figure 2**: "Model Collapse in Kernel Density Estimation. Left: We consider 4 standard datasets from sklearn: Blobs, Circles, Moons and Swiss Roll. Center: For all four datasets, deleting data en masse causes the negative log likelihoods (NLL) of real test data to increase with each model-fitting iteration. Right: For all four datasets, accumulating data avoids model collapse."

**Figure 3**: "Model Collapse in Supervised Finetuning of Language Models. Finetuning Google's Gemma2 models on Nvidia's HelpSteer 2 dataset demonstrates that model collapse occurs if previous data are replaced after each model-fitting iteration (left), whereas model collapse is avoided if new synthetic data instead accumulate with previous real and synthetic data (right)."

**Figure 4**: "Model Collapse Under a Fixed Compute Budget. We compare deleting data after each model-fitting iteration (Replace) and accumulating data after each iteration (Accumulate) with a new fixed-compute data paradigm Accumulate-Subsample."

**Figure 5**: "The Value of Synthetic Data in Supervised Finetuning of Language Models. Finetuning Google's Gemma 2 2B on Nvidia's HelpSteer 2 dataset on different combinations of real and synthetic data demonstrates that loss grows with the number of synthetic data."

---

## Discussion / Conclusion (verbatim excerpts)

"Our work sought extend understanding of model collapse in the replace and accumulate workflows. We demonstrated in three new generative modeling settings that accumulating data over time avoids model collapse, whereas replacing data over time induces model collapse."

"We then demonstrated in five generative modeling settings that even when each model is trained on a fixed compute budget with a mixture of real and synthetic data, model performance does deteriorate more, but still tends to plateau."

"The consistency of these results across different model types and datasets suggests that this distinction is a general phenomenon, and is not specific to any particular model, dataset, or learning algorithm."

"Lastly, we explored the value of synthetic data for reducing the test loss on real data and found two different regimes: when real data are plentiful, synthetic data is harmful, but when real data are scarce, there exists an optimal amount of synthetic data that are helpful."

"In our view, the data paradigm in which synthetic data accumulates from a host of models in conjunction with a constant influx of real-world data is more realistic."

"Under such dynamics, where new synthetic data are added to existing real and synthetic data, model collapse appears unlikely."

"Our experiments take a pessimistic viewpoint, in the sense that our experiments pay no attention to the quality of data, whereas in practice, engineers heavily filter data based on various indicators of data quality."

---

## Limitations (verbatim)

- No data quality filtering applied (contrasts with real practice where engineers heavily filter).
- Results limited to relatively small models/datasets due to compute constraints.
- Need to understand conditions where synthetic data improves performance.

## Future Directions

- Combining synthetic generation with filtering techniques.
- Identifying which conditions enable synthetic data to improve test loss.
- Understanding why accumulation can sometimes outperform real-only training.

---

## Appendix Structure

- Appendix A: Iterative Gaussian Model Fitting (includes Lemma 2, Lemma 3, proofs)
  - A.1 Setup
- Appendices B, C, D: referenced but not fully rendered in HTML

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6803a0b9-8aac-476d-91e1-7a4980ab99f4",
  "isSidechain": true,
  "agentId": "a5324dfd68a7026d4",
  "requestId": "req_011CbE2LB1hJ84Npzea1Gbkd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85418734-0bba-466c-b376-38555eadf403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018HeCHZh8s8ffULRqscWLzx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1314,
      "cache_read_input_tokens": 24654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1314,
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
