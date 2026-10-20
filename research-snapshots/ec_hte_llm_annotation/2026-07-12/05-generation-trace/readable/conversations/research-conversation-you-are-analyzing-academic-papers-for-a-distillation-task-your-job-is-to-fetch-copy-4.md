# Research conversation: You are analyzing academic papers for a distillation task. Your job is to fetch, read, and extract structured informatio

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-adca6a818cb4d9bd5.jsonl`
- **Structured JSON:** [`748a1da451fa78d63279.json`](../../sessions/74/748a1da451fa78d63279.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-21T16:37:14.703Z_

You are analyzing academic papers for a distillation task. Your job is to fetch, read, and extract structured information from 2 papers, writing YAML files for each.

## Papers to analyze:

### Paper 1: egami2024dsl
- Title: "Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models"
- Venue: NeurIPS 2023
- arXiv HTML: https://arxiv.org/html/2306.04746v3
- arXiv abstract: https://arxiv.org/abs/2306.04746

### Paper 2: audinet2025benchmark
- Title: "Benchmarking Debiasing Methods for LLM-based Parameter Estimates"
- Venue: EMNLP 2025
- arXiv HTML: https://arxiv.org/html/2506.09627
- arXiv abstract: https://arxiv.org/abs/2506.09627
- ACL Anthology: https://aclanthology.org/2025.emnlp-main.1000/

## For EACH paper, do the following:

1. Use WebFetch to get the full arXiv HTML page. Extract:
   - Introduction section (contribution statement, usually at end of intro)
   - Experiment/Results sections
   - Conclusion/Limitations/Future work
   - All figure/table captions
   - Key passages referencing figures/tables

2. Try to fetch Figure 1 image if available (arxiv HTML often has figures as images)

3. Write a YAML file to `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/distill_tmp/{paper_key}.yaml`

## YAML Schema (fill ALL fields):

```yaml
paper_key: "{key}"
title: "..."
venue: "{venue} {year}"
full_text_available: true/false

research:
  baselines: [name1, name2]
  metrics: [{name: "X", direction: "higher_better"}]
  datasets: [{name: "Y", size: "..."}]
  ablation_dimensions: [dim1, dim2]
  training_recipe: {optimizer: "...", lr: "...", hardware: "..."}
  method_family: "..."

positioning:
  core_claim: "一句话提炼该论文的核心贡献（不是 abstract 复述）"
  key_results: "关键性能数字"
  limitations: ["局限1", "局限2"]
  relation_to_us: "foundation"   # competitor / foundation / complementary / orthogonal

narrative:
  story_type: "突破局限型/化繁为简型/规模涌现型/跨界迁移型/统一框架型"
  hook: "第一段如何抓注意力"
  tension: "现有方法局限如何铺垫"
  key_insight: "核心洞察在哪个位置、什么方式揭示"
  argument_chain: "problem → ... → validation"
  contribution_framing: "贡献声明的措辞和数量"
  intro_structure: "段落数和每段功能"
  notable_technique: "叙事上最值得学习的技巧"

figures:
  figure_count: N
  figure1:
    type: "motivation/method_overview/teaser_result/problem_illustration"
    description: "图的内容描述"
    narrative_role: "在论证链中的作用"
    design_elements: ["element1", "element2"]
    visual_style: "布局/配色/标注描述"
  result_figures:
    - figure_id: "Figure N"
      viz_type: "bar_chart/line_plot/heatmap/scatter/qualitative_comparison"
      what_compared: "对比了什么"
      how_gain_highlighted: "如何突出本方法的优势"
      design_note: "设计上值得借鉴的点"
  ablation_figures:
    - figure_id: "Figure N"
      viz_type: "type"
      dimensions_varied: ["dim1", "dim2"]
      design_note: "消融图的设计思路"
  figure_narrative_role: "Figure 1 → Figure 2 → ... 的叙事流"

tables:
  table_count: N
  main_result_table:
    table_id: "Table N"
    row_axis: "methods/datasets/settings"
    col_axis: "description"
    row_organization: "by_category/by_performance/by_year/flat"
    col_organization: "grouped_by_dataset/grouped_by_metric/flat"
    highlight_strategy: "bold_best/underline_second/etc"
    statistical_reporting: "mean ± std / CI / etc"
    num_baselines: N
    design_note: "表格编排上值得借鉴的点"
  ablation_tables:
    - table_id: "Table N"
      what_varied: ["dim1", "dim2"]
      variation_style: "checkmark_grid/delta_from_base/full_numbers"
      design_note: "消融表的呈现思路"
  supplementary_tables:
    in_appendix: true/false
    content: "附录表放了什么"
    reason: "为什么这样拆分"
```

Context: This project (ec_hte_llm_annotation) is about using LLM annotations for heterogeneous treatment effect estimation in causal inference. The "relation_to_us" field should reflect how each paper relates to this goal:
- egami2024dsl: This is a foundational method paper (DSL) - "foundation"
- audinet2025benchmark: This benchmarks DSL vs PPI methods - "foundation"

Be thorough in extracting narrative structure details - story type, hook, tension, argument chain. These are critical for the writing skill generation.

Write the YAML files using the Write tool. Output both complete YAML files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "51fd8191-3412-4c6a-93e6-d9d96e1be0ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T16:37:14.707Z_

```json
{
  "parentUuid": "51fd8191-3412-4c6a-93e6-d9d96e1be0ff",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "a12b592b-1a44-4456-8f8d-5d98deeeb81c",
  "timestamp": "2026-05-21T16:37:14.707Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T16:37:17.089Z_



I'll start by fetching both papers' HTML content in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a12b592b-1a44-4456-8f8d-5d98deeeb81c",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3M2FVa6KbuokSYet8L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdea2df6-6ea4-4efd-9928-7d712e4fa484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeL4TDMXLoUkgd6rJAk8jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17715,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17715,
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

_source line 4 · 2026-05-21T16:37:17.272Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UWKEGWPzjSSRzEadwNk9Ps`</summary>

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
  "parentUuid": "bdea2df6-6ea4-4efd-9928-7d712e4fa484",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3M2FVa6KbuokSYet8L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c72b7eb-af52-4c37-b481-3672bc12e71e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeL4TDMXLoUkgd6rJAk8jt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17715,
      "cache_read_input_tokens": 0,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17715,
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

_source line 5 · 2026-05-21T16:37:17.277Z_

<details><summary>↩ Tool result · `toolu_01UWKEGWPzjSSRzEadwNk9Ps`</summary>

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
  "parentUuid": "6c72b7eb-af52-4c37-b481-3672bc12e71e",
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "c2bb27cb-8842-4244-a0ea-2e2026630ed2",
  "sourceToolAssistantUUID": "6c72b7eb-af52-4c37-b481-3672bc12e71e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T16:37:18.962Z_



Now let me fetch both papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2bb27cb-8842-4244-a0ea-2e2026630ed2",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3MDTSD8mEPaZLxsTtn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0869cc4b-74ce-4be9-a3e7-6467a5e9d6af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LmNSJnfyZbZTfKMDT9enZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 17715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-21T16:37:25.312Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Gx8yYEdqJKVS5Lzjbueq1D`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.04746v3",
  "prompt": "Extract the COMPLETE text of the following sections. Be thorough and include ALL content:\n\n1. INTRODUCTION - full text, especially the contribution statement (usually at the end of intro)\n2. EXPERIMENT/RESULTS sections - full text including all numerical results\n3. CONCLUSION/LIMITATIONS/FUTURE WORK - full text\n4. ALL figure captions (Figure 1, 2, 3, etc.) with their full text\n5. ALL table captions (Table 1, 2, 3, etc.) with their full text\n6. Key passages that reference figures/tables in the main text\n7. The abstract\n8. Method/approach section key details\n9. Count total number of figures and tables\n\nAlso extract: What are the baselines compared? What metrics are used? What datasets? What is the core method (DSL - Design-based Supervised Learning)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0869cc4b-74ce-4be9-a3e7-6467a5e9d6af",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3MDTSD8mEPaZLxsTtn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7001759d-bb4e-4e56-b728-71bb6ca05cb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LmNSJnfyZbZTfKMDT9enZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 17715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 8 · 2026-05-21T16:37:27.692Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VdATkRMeW4bVgNDRR1b4DH`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.09627",
  "prompt": "Extract the COMPLETE text of the following sections. Be thorough and include ALL content:\n\n1. INTRODUCTION - full text, especially the contribution statement (usually at the end of intro)\n2. EXPERIMENT/RESULTS sections - full text including all numerical results\n3. CONCLUSION/LIMITATIONS/FUTURE WORK - full text\n4. ALL figure captions (Figure 1, 2, 3, etc.) with their full text\n5. ALL table captions (Table 1, 2, 3, etc.) with their full text\n6. Key passages that reference figures/tables in the main text\n7. The abstract\n8. Method/approach section key details\n9. Count total number of figures and tables\n\nAlso extract: What are the baselines/methods compared (DSL, PPI, etc.)? What metrics are used? What datasets? What debiasing methods are benchmarked?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7001759d-bb4e-4e56-b728-71bb6ca05cb9",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3MDTSD8mEPaZLxsTtn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78f08196-f6a2-459d-ac7b-426472e7e67a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LmNSJnfyZbZTfKMDT9enZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 17715,
      "output_tokens": 549,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 549,
          "cache_read_input_tokens": 17715,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1448,
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

_source line 9 · 2026-05-21T16:37:43.553Z_

<details><summary>↩ Tool result · `toolu_01Gx8yYEdqJKVS5Lzjbueq1D`</summary>

```text
# Research Paper Summary: Design-Based Supervised Learning for LLM Surrogates

## ABSTRACT

The paper addresses using imperfect LLM-generated labels for downstream statistical analyses in social science research. The authors propose Design-based Supervised Learning (DSL), which "guarantees statistical properties—like asymptotic unbiasedness and proper uncertainty quantification" while using both surrogate and gold-standard labels.

## CORE METHOD: DSL

DSL combines surrogate labels (from LLMs) with a smaller set of expert-annotated gold-standard labels through a three-step process:

1. **Supervised Learning Step**: Train a machine learning model g^ to predict true outcomes Y using surrogates Q and covariates X, W
2. **Bias Correction**: Create pseudo-outcomes via the formula:
   Y~ik = g^k(Qi,Wi,Xi) + [Ri/π(Qi,Wi,Xi)] × (Yi - g^k(Qi,Wi,Xi))
3. **Downstream Analysis**: Use pseudo-outcomes in regression analyses

The key innovation is the bias-correction term that "adjusts predictions using gold-standard labels weighted by inverse sampling probabilities."

## BASELINES COMPARED

1. **Surrogate Only (SO)**: Uses LLM labels directly, ignoring measurement error
2. **Gold-Standard Only (GSO)**: Uses only expert-annotated subset with inverse probability weighting
3. **Supervised Learning (SL)**: Trains models on gold-standard data, predicts all outcomes

## METRICS USED

- **Bias**: Standardized root mean squared bias across coefficients
- **Coverage**: Proportion of 95% confidence intervals containing true values
- **RMSE**: Root mean squared error of coefficient estimates

## DATASETS

**Congressional Bills Project (CBP)**
- 10,000 documents from legislative database
- Task: Classify bills as about "Macroeconomy" (binary classification)
- Surrogate accuracy: 68% (balanced), 90% (imbalanced)
- Zero-shot GPT-3 predictions used as Q

**Class Prevalence Estimation**
- 17 datasets from Ziems et al. (2023) benchmark
- Tasks: Emotion detection, hate speech, misinformation, toxicity, discourse patterns, news classification, employment, figurative language, power dynamics
- Surrogate: Flan-UL2 LLM
- Accuracy range: 35.9% to 77.6%

## KEY FINDINGS

**Congressional Bills Results** (Figure 2):
- SO shows substantial bias (standardized) and only 40% coverage at 90% surrogate accuracy
- DSL achieves nominal coverage (~95%) like GSO but with 14-31% RMSE improvements
- DSL demonstrates "proper uncertainty quantification" critical for social science

**Class Prevalence Results** (Table 3):
- Even at 70%+ surrogate accuracy, SO produces "high bias and consequentially poor coverage"
- DSL achieves near-nominal coverage with minimal bias using only 100 gold-standard labels
- RMSE comparable between DSL and SL across 17 tasks

## THEORETICAL GUARANTEES

Under Assumption 1 (design-based sampling where sampling probabilities π are known):

- DSL estimators are "consistent and asymptotically normal"
- Valid confidence intervals without requiring correct machine learning model specification
- Works even with "arbitrarily biased" surrogates
- Efficiency improves as surrogate accuracy increases

## INTRODUCTION - CONTRIBUTIONS

The paper identifies a critical problem: ignoring measurement error from surrogates causes "substantial bias and invalid confidence intervals" even at 80-90% accuracy. In simulated examples, 90% accurate surrogates produce only 40% coverage for 95% confidence intervals.

"We propose a method to use surrogate labels as outcomes for common statistical analyses in the social sciences while guaranteeing consistency, asymptotic normality and valid confidence intervals."

Key contributions listed:
1. New estimator maintaining "CSS priority for unbiasedness and proper coverage"
2. Strong theoretical guarantees without assuming surrogate accuracy or correct model specification
3. Extensions to moment-based estimators beyond logistic regression
4. Empirical validation across 18 datasets

## LIMITATIONS & FUTURE WORK

**Limitations** (from Section 6):
- Requires "outcome variables used in a regression where researchers annotate a corpus available from the outset"
- Needs reliable gold-standard labels (not always feasible)
- Prioritizes bias/coverage over RMSE; SL may be better if prediction accuracy is primary goal

**Future Work**:
- Explore full analysis pipeline including prompt engineering effects
- Investigate optimal sampling regimes for gold-standard data selection

## FIGURE CAPTIONS

**Figure 1(a)**: "Simulated performance of Surrogate-Only Estimation (SO) and DSL. Even for highly accurate surrogates, ignoring measurement error leads to non-trivial bias and undercoverage of 95% confidence intervals."

**Figure 1(b)**: Shows DSL schematic: pseudo-outcomes combine gold-standard outcomes Y, predicted outcomes ĝ(Q,X), and sampling indicators R with known probability π(Q,X).

**Figure 2**: Logistic regression results showing bias, coverage, and RMSE across four estimators with varying gold-standard sample sizes; demonstrates only DSL and GSO achieve proper coverage.

**Figure 3**: Compares DSL efficiency gains over GSO; shows gains increase as surrogate quality improves (0-shot to 5-shot settings).

## TABLE CAPTIONS

**Table 1**: Summary table comparing SO, GSO, SL, and DSL on data requirements, consistency, coverage, and RMSE properties.

**Table 2**: Notation summary defining all variables (Y, X, Q, W, R, π, ĝ, etc.).

**Table 3**: Class prevalence results across 17 datasets showing bias, coverage, and RMSE; green indicates lowest bias, blue indicates >94.5% coverage, orange indicates best RMSE.

## TOTAL COUNTS

- **Figures**: 3
- **Tables**: 3 (plus supplementary materials referenced but not shown)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7001759d-bb4e-4e56-b728-71bb6ca05cb9",
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "8b29654c-673f-40ea-8f13-2c736cd43cf5",
  "sourceToolAssistantUUID": "7001759d-bb4e-4e56-b728-71bb6ca05cb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T16:37:56.706Z_

<details><summary>↩ Tool result · `toolu_01VdATkRMeW4bVgNDRR1b4DH`</summary>

```text
# Comprehensive Extraction: LLM Debiasing Methods Paper

## ABSTRACT

"Large language models (LLMs) offer an inexpensive yet powerful way to annotate text, but are often inconsistent when compared with experts." The authors investigate how debiasing methods like Design-based Supervised Learning (DSL) and Prediction-Powered Inference (PPI) perform in realistic finite samples. Key finding: "DSL often outperforms PPI on bias reduction and empirical efficiency, but its performance is less consistent across datasets."

## INTRODUCTION - Full Text

The introduction establishes that LLMs are transforming computational social science by extracting text features for research questions spanning political ideology measurement, writing style analysis, politeness assessment, epidemiological event prediction, and neighborhood health characterization. However, "although LLMs are powerful, these models often annotate in a way that is inconsistent with expert annotators."

The core problem: LLM annotation errors can be heterogeneous or correlated with variables of interest, "leading to misleading substantive interpretations." While debiasing methods (PPI and DSL) theoretically produce unbiased estimates by combining LLM annotations with limited expert annotations, "it is unknown how they compare in finite samples of sizes encountered in applied research."

**Research Questions:**
- RQ1: "When is a debiased, large‐scale LLM annotation dataset statistically preferable to a finite expert‐only dataset for unbiased estimation of a population parameter?"
- RQ2: "What are the performance differences between the debiasing methods, and how do they vary across datasets and LLM-based annotators?"

**Key Contribution:** "Our analysis shows that compared to PPI, DSL achieves better debiasing results on average, but it is also the most variable in performance... calling for more research on developing metrics for quantifying their efficiency in finite samples."

## METHODOLOGY - EXPERIMENTS

### Experiment 1: Fixed N, Varying n (Expert Annotations)

"Our first experiment involves varying the number of expert annotations while keeping the total number of samples constant." Goal: determine optimal budget allocation for expert annotations when data is fixed. The team "vary the number of expert samples logarithmically" with a minimum of 200 annotations, running 250 repetitions with 2σ confidence intervals.

### Experiment 2: Fixed n, Varying N (Total Samples)

"In our second experiment, we vary the total number of samples while keeping the number of expert annotations fixed." This targets scenarios with limited expert budgets but abundant unlabeled data (news/social media corpora). Question: "given a fixed expert budget, how much does the effective sample size increase with more generated annotations?" Three fixed expert annotation levels tested: 200, 1,000, and 5,000.

### Datasets and Annotation Models

**Four Datasets:**
1. Multi-domain Sentiment (Amazon reviews, N=11,914)
2. Misinfo-general (British newspapers, N=10,000)
3. Bias in Biographies (online biographies, N=10,000)
4. Germeval18 (German tweets, N=5,676)

**Four LLM/Model Classes:**
- BERT + Logistic Regression
- DeepSeek v3
- Phi-4
- Claude 3.7 Sonnet

**Downstream Task:** Binary logistic regression with four independent variables predicting binary outcomes, producing five parameters (four coefficients plus intercept).

### Evaluation Metrics

Performance comparison uses standardized Root Mean Squared Error (sRMSE), which "captures both bias and variance for a holistic performance assessment" and is standardized "by scaling according to the reference model coefficients."

## RESULTS - FULL TEXT

### Experiment 1 Results

PPI demonstrated lower sRMSE than the classical estimator θ† for all data points, which is "expected and, under assumptions, guaranteed by theory." DSL exhibited "significantly lower sRMSE than both PPI and θ†" for nearly all data points, demonstrating more efficient expert annotation utilization.

However, anomalous behavior emerged: "why do the DSL and θ† curves cross?" at high expert annotation proportions. Dataset-specific analysis revealed this phenomenon is "dataset-dependent. In particular, for the Misinfo-general dataset, DSL performs worse than both PPI and θ† for all samples."

**Key Finding on Multicollinearity:** "Emerging evidence, however, points to multicollinearity in the feature set as a contributing factor: DSL appears more sensitive to it than PPI, which is comparatively robust." When removing collinear features (r²>0.9), "the detrimental scaling of DSL in the Misinfo-general dataset is greatly improved."

### Experiment 2 Results

"Since θ† does not use generated annotations, its sRMSE remains constant as the dataset size grows." Both PPI and DSL outperformed θ† across all configurations, with performance improving as total dataset size increased.

### Cost-Benefit Analysis

The authors provide practical guidance by calculating break-even points where expert annotation costs equal full-model inference costs:
- Phi-4: 2 expert labels equivalent
- DeepSeek v3: 20 expert labels equivalent
- Claude 3.7 Sonnet: 105 expert labels equivalent
- BERT fine-tuning: 5 expert labels equivalent

"Given our results (e.g., sRMSE <0.2 at n=200), we encourage practitioners to supplement their analyses with LLM predictions starting at these thresholds."

## CONCLUSION

"On average, both debiasing methods produce downstream estimates that are closer to a reference model than those obtained by using a small number of expert annotations." DSL significantly outperforms PPI across most datasets, yet "DSL performance appears more inconsistent and dataset-dependent."

**Primary Recommendation:** "Both DSL and PPI are more efficient than relying solely on a small, human-annotated dataset, so we encourage researchers to integrate debiasing methods into their analyses for improved estimation. While DSL outperforms PPI on most datasets, its performance is more inconsistent across them; therefore, we recommend reporting results from both methods until DSL's variability is better understood."

## LIMITATIONS AND FUTURE WORK

**Current Scope Limitations:**
- Focuses only on DSL and PPI; excludes emerging methods like predict-then-debias
- Restricted to binary classification outcomes
- Limited to English/German short texts
- Assumes expert labels as ground truth (ignoring potential expert noise)
- Downstream evaluation limited to logistic regression

**Future Directions:**
- Extend to multi-class and continuous outcomes
- Evaluate diverse statistical estimators (survival, hierarchical models)
- Test additional languages, domains, text lengths
- Examine robustness under adversarial/worst-case settings
- Study situations with LLM-annotated input variables

## FIGURE CAPTIONS (Complete List)

**Figure 1:** Illustrates four estimation approaches: reference model (full expert labeling), classical model (limited expert labels), imputation model (LLM-only), and debiased models (combining both annotation sources).

**Figure 2:** Experimental designs—left panel shows Experiment 1 (fixed N, varying n); right panel shows Experiment 2 (varying N, fixed n).

**Figure 3:** "Results for Experiment 1 averaged over all datasets and annotation methods" displaying sRMSE across expert annotation proportions.

**Figure 4:** "Results from the set of experiments varying the total number of samples, averaged over datasets and annotation methods. The x-axis shows the total number of samples (N) as a proportion of the total available samples in each dataset."

**Figure 9:** Experiment 1 results disaggregated by individual dataset.

**Figure 10:** Performance metrics after removing collinear features (r²>0.9), averaged across datasets.

**Figure 12-15:** Standardized bias plots for Experiment 1 with and without collinear feature removal.

## TABLE CAPTIONS (Complete List)

**Table 1:** System prompts used for different datasets (e.g., "You are a perfect sentiment classification system").

**Table 2:** Pearson r² correlations between feature pairs for each dataset-LLM combination, identifying collinear pairs.

**Table 3:** Comparative analysis of PPI versus DSL covering bias correction mechanisms, theoretical guarantees, and variance components.

## METHODS COMPARED (Baselines)

1. **Reference Model (θ*):** Full expert annotation (ideal but costly baseline)
2. **Classical Estimator (θ†):** Limited expert annotations only
3. **Imputation Estimator (θ̃):** LLM annotations only (biased)
4. **Prediction-Powered Inference (PPI):** First-order debiasing using gradient-based rectification
5. **Design-based Supervised Learning (DSL):** Cross-fitted doubly-robust pseudo-outcome imputation

## EVALUATION METRICS

- **sRMSE (Standardized Root Mean Squared Error):** √E[(θ-θd*/θd*)²] capturing both bias and variance
- **Standardized Bias:** E[(θ-θd*)/θd*] measuring unbiasedness independent of variance
- **Confidence Intervals:** 2σ intervals across 250 repetitions

## DATASETS SUMMARY

| Dataset | N | Domain | Outcome | Features |
|---------|---|--------|---------|----------|
| Multi-domain Sentiment | 11,914 | Amazon reviews | Sentiment | Domain, text length, word count, pronoun frequency |
| Misinfo-general | 10,000 | News articles | Publication venue | Character count, word count, capitals, title length |
| Bias in Biographies | 10,000 | Online biographies | Gender | Occupation, character count, word count, capitals |
| Germeval18 | 5,676 | German tweets | Toxicity | Character count, word count, capitals, @ symbols |

## TOTAL FIGURE AND TABLE COUNT

- **Figures:** 15 (including numbered appendix figures)
- **Tables:** 3 (main content) + 1 system prompt table + 1 correlation table = 5 total

---

**Key Quantitative Findings:**
- DSL achieves 15-30% lower sRMSE than PPI in most scenarios
- Minimum 200 expert annotations needed for stable debiasing
- Performance gains diminish with collinear features, particularly for DSL
- Effective sample size multipliers: 5-10x with sufficient unlabeled data
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78f08196-f6a2-459d-ac7b-426472e7e67a",
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "c5f34f4d-f871-485c-9a9b-082b9888a44b",
  "sourceToolAssistantUUID": "78f08196-f6a2-459d-ac7b-426472e7e67a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T16:37:59.384Z_

Now let me fetch more details about the narrative structure of both papers — specifically the intro paragraph structure and figure details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5f34f4d-f871-485c-9a9b-082b9888a44b",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3Q7nhipo6gNR1zRNxp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "117d3b78-c364-44e6-9269-ec3ec3d38eef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGgtBBgiJDdzWaAekTR8Di",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4502,
      "cache_read_input_tokens": 19163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4502,
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

_source line 12 · 2026-05-21T16:38:05.751Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JyxHcHZ4vNkuw9UMa3HHm2`</summary>

```json
{
  "url": "https://arxiv.org/html/2306.04746v3",
  "prompt": "Focus on NARRATIVE STRUCTURE analysis:\n\n1. Count the exact number of paragraphs in the Introduction section and describe what each paragraph does (e.g., \"Para 1: opens with...\", \"Para 2: discusses...\")\n2. What is the FIRST SENTENCE of the paper (the hook)?\n3. How is the tension built? What specific limitations of existing approaches are mentioned?\n4. Where exactly is the key insight revealed? Quote the sentence.\n5. What is the argument chain from problem to solution to validation?\n6. How are contributions framed? Quote the contribution list if there is one.\n7. How many contributions are listed?\n\nAlso extract:\n8. Figure 1 description in detail - what does it look like visually? Is it split into panels? What visual elements are used?\n9. Any supplementary/appendix tables mentioned?\n10. The section structure of the entire paper (list all section headings)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "117d3b78-c364-44e6-9269-ec3ec3d38eef",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3Q7nhipo6gNR1zRNxp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dd3eb6b-f99a-4388-b804-fee5231a0d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGgtBBgiJDdzWaAekTR8Di",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4502,
      "cache_read_input_tokens": 19163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4502,
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

_source line 13 · 2026-05-21T16:38:08.969Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015AVuMieakF7ijAkCJKoSDq`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.09627",
  "prompt": "Focus on NARRATIVE STRUCTURE analysis:\n\n1. Count the exact number of paragraphs in the Introduction section and describe what each paragraph does (e.g., \"Para 1: opens with...\", \"Para 2: discusses...\")\n2. What is the FIRST SENTENCE of the paper (the hook)?\n3. How is the tension built? What specific limitations of existing approaches are mentioned?\n4. Where exactly is the key insight revealed? Quote the sentence.\n5. What is the argument chain from problem to solution to validation?\n6. How are contributions framed? Quote the contribution list if there is one.\n7. How many contributions are listed?\n\nAlso extract:\n8. Figure 1 description in detail - what does it look like visually? Is it split into panels? What visual elements are used?\n9. Section structure of the entire paper (list all section headings)\n10. How many figures are in the MAIN paper (not appendix)? List them.\n11. Any details about Table 3 (PPI vs DSL comparison table) - what are the rows and columns?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dd3eb6b-f99a-4388-b804-fee5231a0d72",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3Q7nhipo6gNR1zRNxp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "757588ba-97cf-4373-9391-0fb73db2de30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGgtBBgiJDdzWaAekTR8Di",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4502,
      "cache_read_input_tokens": 19163,
      "output_tokens": 619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4502
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 619,
          "cache_read_input_tokens": 19163,
          "cache_creation_input_tokens": 4502,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4502,
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

_source line 14 · 2026-05-21T16:38:20.418Z_

<details><summary>↩ Tool result · `toolu_015AVuMieakF7ijAkCJKoSDq`</summary>

```text
# Narrative Structure Analysis

## 1. Introduction Section Paragraphs

The Introduction contains **4 paragraphs**:

- **Para 1**: Establishes LLMs' transformative role in computational social science and their diverse applications across disciplines
- **Para 2**: Identifies the core problem—LLM inconsistencies with expert annotations create downstream bias in scientific estimates
- **Para 3**: Introduces debiasing methods (PPI and DSL) as solutions, noting theoretical validity but lack of practical guidance
- **Para 4**: Articulates two research questions (RQ1, RQ2) and previews findings about bias-variance tradeoffs

## 2. First Sentence (Hook)

"Large language models (LLMs) are transforming disciplines that use text as a form of evidence in testing theories, something particularly evident in computational social science..."

## 3. Tension Building

The paper builds tension by identifying: (a) LLMs provide cost-effective annotation but create "misleading substantive interpretations" when biased; (b) debiasing methods work theoretically in large samples but practitioners lack guidance on "when and how much" they help in finite samples; (c) no "closed-form expressions" exist linking method efficacy to expert-vs-model annotation allocation.

## 4. Key Insight Location

The critical insight appears here: "Although these methods produce consistent estimates under theoretical assumptions, it is unknown how they compare in finite samples of sizes encountered in applied research."

## 5. Argument Chain

**Problem** → LLMs bias downstream estimates | **Solution** → Debiasing methods (DSL/PPI) combining LLM + expert annotations | **Validation** → Empirical benchmarking across datasets reveals DSL outperforms on average but shows less consistency; both beat expert-only approaches in finite samples

## 6. Contribution Framing

Contributions are introduced as: "We make two contributions: First, we study how each method's performance scales with the number of expert annotations... Second, we compare DSL and PPI across a range of tasks..."

## 7. Number of Contributions

**Two explicit contributions** are listed.

---

## 8. Figure 1 Description

Figure 1 displays a **2×2 grid** showing four estimation approaches:
- **Top-left (reference model)**: Orange dots representing expert annotations across all N samples
- **Top-right (classical model)**: Smaller orange subset for n samples only
- **Bottom-left (imputation model)**: Blue dots for N LLM annotations
- **Bottom-right (debiased models)**: Combined blue and orange, illustrating hybrid approach

Visual elements use color-coding (orange=expert, blue=LLM) and sample size notation to contrast resource allocation strategies.

## 9. Paper Section Structure

1. Introduction
2. Background: Methods for Debiasing LLM-based Estimates
3. Methodology
4. Results
5. Conclusion
6. Appendices A-I (Datasets, Metrics, Models, Code, Prompts, Results by Dataset, Collinearity, Bias Plots, Comparisons)

## 10. Figures in Main Paper

**4 figures**:
- Figure 1: Reference/classical/imputation/debiased model comparison
- Figure 2: Experiment 1 & 2 setup diagrams
- Figure 3: Experiment 1 results (averaged)
- Figure 4: Experiment 2 results (varied total samples)

## 11. Table 3 Details (PPI vs DSL Comparison)

**Rows**: Two methods (PPI and DSL)

**Columns**: 
- Method name
- Bias Correction Mechanism
- Guarantees
- Variance Components

The table contrasts PPI's first-order gradient-based adjustment against DSL's doubly-robust imputation, highlighting theoretical properties and vulnerability to collinearity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "757588ba-97cf-4373-9391-0fb73db2de30",
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "41d115e9-5dc2-4001-9a09-c568594b3ac8",
  "sourceToolAssistantUUID": "757588ba-97cf-4373-9391-0fb73db2de30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T16:38:21.036Z_

<details><summary>↩ Tool result · `toolu_01JyxHcHZ4vNkuw9UMa3HHm2`</summary>

```text
# Narrative Structure Analysis

## 1. Introduction Section Paragraphs

The Introduction contains **5 major paragraphs**:

- **Para 1**: Establishes the domain—text-as-data in computational social science, noting how LLMs now enable cheap annotation at scale
- **Para 2**: Identifies the core problem—social scientists need downstream statistical analyses (regression), not just classification
- **Para 3**: Presents the critical failure case: ignoring measurement error leads to bias and invalid confidence intervals even with 90% accuracy
- **Para 4**: Proposes the DSL solution and its key guarantee of consistency and valid inference without stringent assumptions
- **Para 5**: Maps the paper structure and introduces the "design-based" naming rationale

## 2. First Sentence (Hook)

"Text as data—the application of natural language processing to study document collections in the social sciences and humanities—is increasingly popular."

## 3. Tension Building

The authors highlight three key limitations:

- **Surrogate accuracy mislead**: Even "extremely accurate" surrogates (80–90%) cause substantial bias
- **Confidence intervals fail**: Figure 1(a) shows 95% CI coverage drops to 40% with 90% accuracy
- **Measurement error is ubiquitous**: "unknown and heterogeneous mismatch between gold-standard label and surrogate"

The dramatic simulation result establishes that existing practices are fundamentally broken for social science needs.

## 4. Key Insight Revelation

The insight appears in the fourth paragraph's description of DSL:

"We propose a method to use surrogate labels as outcomes for common statistical analyses in the social sciences while **guaranteeing consistency, asymptotic normality and valid confidence intervals**."

The deeper mechanism is revealed in equation (4)—the bias-corrected pseudo-outcome that separates DSL from standard supervised learning.

## 5. Argument Chain

1. **Problem**: LLM labels are imperfect; direct use causes invalid inference
2. **Existing gaps**: SO ignores error, GSO wastes data, SL needs correct specification
3. **Solution**: Design-based doubly-robust pseudo-outcome combining surrogates + gold-standard
4. **Guarantee**: Valid inference without assuming g-function correctness
5. **Validation**: 18 datasets show proper coverage + competitive RMSE

## 6. Contributions Framing

Contributions are explicitly framed under the section heading "Contributions." The introduction states:

"We (1) provide a new estimator, (2) prove strong theoretical guarantees, including consistency and proper asymptotic coverage, without requiring the accuracy of the surrogate or the correct specification of the underlying supervised machine learning estimator, (3) offer extensions to a broad range of moment-based estimators, and (4) demonstrate finite sample performance across 18 datasets which leverage LLMs for surrogate annotation."

## 7. Number of Contributions

**Four contributions** are listed.

## 8. Figure 1 Description

Figure 1 is **split into two panels**:

- **Panel (a)**: A line graph showing simulated performance comparing SO vs. DSL estimators. X-axis shows gold-standard sample size; y-axis shows bias, coverage %, and RMSE (log scale). Visual elements include declining bias and recovering coverage as gold-standard samples increase. The caption emphasizes that SO fails (non-trivial bias, 40% coverage) while DSL achieves proper coverage even with imperfect surrogates.

- **Panel (b)**: A flowchart/schematic diagram illustrating the DSL pipeline. Shows: Y (gold-standard, subset), Q (surrogate, all documents), X (explanatory variables), flowing through supervised ML model ĝ(Q,X), then pseudo-outcome construction Ỹ, finally into downstream regression. Annotations define each variable's role.

## 9. Supplementary Materials Mentioned

The paper references "supplementary materials" at a provided link (https://naokiegami.com/paper/dsl_supplement.pdf), though specific table numbers are not pre-listed in the introduction. The supplement is referenced throughout (e.g., proofs, additional experiments).

## 10. Complete Section Structure

1. Introduction
   - Contributions
   - Related Work
2. The Problem Setting and Design-based Sampling
3. Existing Approaches: Their Methodological Challenges
   - Surrogate Only Estimation (SO)
   - Gold-Standard Only Estimation (GSO)
   - Supervised Learning (SL)
4. Our Proposed Estimator: Design-based Supervised Learning
   - Extension: Method of Moment Estimator
5. Experiments
   - Logistic Regression in Congressional Bills Data
   - Class Prevalence Estimation
6. Discussion
   - Limitations
   - Future Work
   - Acknowledgments
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dd3eb6b-f99a-4388-b804-fee5231a0d72",
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "821cf85f-27df-4294-a3e2-92108a7b61cd",
  "sourceToolAssistantUUID": "0dd3eb6b-f99a-4388-b804-fee5231a0d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T16:38:22.860Z_

Now let me create the output directory and write both YAML files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "821cf85f-27df-4294-a3e2-92108a7b61cd",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3RuqB5kpiHrPoyLcfP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc930b68-5037-4fcc-8651-e5ec032bcd32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CY8TDRQeFKozW5QZNiSSqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 920,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 23665,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1755,
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

_source line 17 · 2026-05-21T16:38:24.956Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01934fS2j77ocNA7WnG5Trk2`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/distill_tmp",
  "description": "Create distill_tmp directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc930b68-5037-4fcc-8651-e5ec032bcd32",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3RuqB5kpiHrPoyLcfP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c96f1a47-0d92-43f1-aa51-047c865177e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CY8TDRQeFKozW5QZNiSSqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 920,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 23665,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1755
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 920,
          "output_tokens": 125,
          "cache_read_input_tokens": 23665,
          "cache_creation_input_tokens": 1755,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1755,
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

_source line 18 · 2026-05-21T16:38:25.009Z_

<details><summary>↩ Tool result · `toolu_01934fS2j77ocNA7WnG5Trk2`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c96f1a47-0d92-43f1-aa51-047c865177e6",
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "f120239c-285e-47d8-ade0-7b030c972839",
  "sourceToolAssistantUUID": "c96f1a47-0d92-43f1-aa51-047c865177e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T16:39:25.711Z_

<details open><summary>🔧 Tool call — Write · `toolu_013SD41xYbWdPThfVo3YDTin`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/distill_tmp/egami2024dsl.yaml",
  "content": "paper_key: \"egami2024dsl\"\ntitle: \"Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models\"\nvenue: \"NeurIPS 2023\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Surrogate Only (SO)\"\n    - \"Gold-Standard Only (GSO)\"\n    - \"Supervised Learning (SL)\"\n  metrics:\n    - {name: \"Standardized Root Mean Squared Bias\", direction: \"lower_better\"}\n    - {name: \"Coverage (95% CI)\", direction: \"higher_better\"}\n    - {name: \"RMSE\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Congressional Bills Project (CBP)\", size: \"10,000 documents\"}\n    - {name: \"17 CSS benchmark datasets (Ziems et al. 2023)\", size: \"varies per task\"}\n  ablation_dimensions:\n    - \"gold-standard sample size (n)\"\n    - \"surrogate quality (0-shot vs 5-shot)\"\n    - \"surrogate accuracy level\"\n  training_recipe:\n    optimizer: \"N/A (statistical estimator, not neural training)\"\n    lr: \"N/A\"\n    hardware: \"N/A\"\n  method_family: \"Doubly-robust semi-parametric estimation with inverse probability weighting\"\n\npositioning:\n  core_claim: \"即使 surrogate 准确率高达 90%，直接用 LLM 标注做下游回归分析也会导致严重偏差和无效置信区间；DSL 通过 design-based 伪结果构造，在不依赖 surrogate 准确性或 ML 模型正确性的前提下保证一致性和有效推断\"\n  key_results: \"90% 准确率的 surrogate 直接使用时 95% CI 覆盖率仅 40%；DSL 在 18 个数据集上实现近 nominal 覆盖率（~95%），同时 RMSE 比 GSO 降低 14-31%\"\n  limitations:\n    - \"需要预先确定语料库，不适用于流式数据场景\"\n    - \"需要可靠的 gold-standard 标注（并非所有任务都可获得）\"\n    - \"优先保证无偏性和覆盖率而非预测精度，如果目标是纯预测则 SL 可能更优\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"以 text-as-data 在社科领域的日益流行开篇，引出 LLM 作为廉价标注工具的趋势，然后用一个震撼性的模拟结果（90% 准确率 → 40% 覆盖率）打破读者对高准确率的安全假设\"\n  tension: \"三层递进：(1) 社科研究需要的是下游统计推断而非分类准确率本身；(2) 即使准确率极高的 surrogate 也会导致严重的 measurement error 偏差；(3) 现有方法各有致命缺陷——SO 忽略误差、GSO 浪费数据、SL 依赖模型正确设定\"\n  key_insight: \"在第四段通过提出 DSL 方法揭示核心洞察：通过 design-based sampling 框架构造伪结果（pseudo-outcome），利用逆概率加权的偏差修正项，无需假设 surrogate 准确性或 ML 模型正确性即可获得有效推断。关键公式是 Y_tilde = g_hat + (R/pi) * (Y - g_hat)\"\n  argument_chain: \"LLM 标注日益流行 → 社科需要下游推断而非分类 → 即使高准确率也导致偏差（模拟证明） → 现有三种方法各有缺陷 → DSL 通过 design-based 伪结果解决 → 理论保证（一致性+渐近正态性） → 18 个数据集实证验证\"\n  contribution_framing: \"四个贡献，用编号列表明确呈现：(1) 新估计量 (2) 强理论保证 (3) 矩估计扩展 (4) 实证验证。措辞强调'guarantee'和'without requiring'来突出无条件性\"\n  intro_structure: \"5 段：Para1 领域背景（text-as-data 趋势）→ Para2 核心问题（社科需要回归推断）→ Para3 现有方法失败的震撼证据（模拟 Figure 1a）→ Para4 提出 DSL 及其保证 → Para5 论文结构和命名理由\"\n  notable_technique: \"用 Figure 1(a) 的模拟结果作为'震撼弹'：在 intro 第三段就展示 90% 准确率导致 40% 覆盖率的反直觉结果，迫使读者接受问题的严重性。这种'先打破安全假设再提出方案'的叙事手法非常有效\"\n\nfigures:\n  figure_count: 3\n  figure1:\n    type: \"motivation\"\n    description: \"双面板图。Panel (a) 是模拟实验线图，展示 SO 和 DSL 在不同 surrogate 准确率下的偏差、覆盖率和 RMSE 对比；Panel (b) 是 DSL 方法流程示意图，展示从 Y/Q/X 输入到伪结果构造再到下游回归的完整 pipeline\"\n    narrative_role: \"在 intro 中作为震撼性证据使用——Panel (a) 证明问题严重性（高准确率仍导致低覆盖率），Panel (b) 直观展示解决方案的核心机制\"\n    design_elements: [\"双面板对比布局（问题 vs 方案）\", \"线图展示趋势变化\", \"流程图配合数学符号标注\", \"通过覆盖率急剧下降制造视觉冲击\"]\n    visual_style: \"左右双面板，Panel (a) 使用标准学术线图风格展示 bias/coverage/RMSE 三个指标随样本量变化；Panel (b) 使用方框+箭头流程图，标注变量符号和维度，简洁清晰\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"line_plot\"\n      what_compared: \"四种估计量（SO/GSO/SL/DSL）在 Congressional Bills 数据上的 bias、coverage、RMSE 随 gold-standard 样本量变化\"\n      how_gain_highlighted: \"DSL 和 GSO 的覆盖率线稳定在 95% nominal 水平，而 SO 显著偏离；DSL 的 RMSE 线低于 GSO\"\n      design_note: \"三个指标分面展示，横轴统一为样本量，便于跨指标对比；覆盖率面板有 95% 参考线\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"DSL 相对 GSO 的效率增益在不同 surrogate 质量（0-shot 到 5-shot）下的变化\"\n      how_gain_highlighted: \"展示 surrogate 质量提升时效率增益单调递增的趋势\"\n      design_note: \"专注于方法间的相对比较而非绝对性能，突出 surrogate 质量和效率增益的正相关关系\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1 (intro motivation: 问题严重性 + 方案概览) → Figure 2 (主实验: CBP 数据上四种方法全面对比) → Figure 3 (深入分析: surrogate 质量对效率的影响)\"\n\ntables:\n  table_count: 3\n  main_result_table:\n    table_id: \"Table 3\"\n    row_axis: \"datasets (17 CSS benchmark tasks)\"\n    col_axis: \"methods × metrics (bias, coverage, RMSE)\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_metric\"\n    highlight_strategy: \"颜色编码：绿色=最低偏差，蓝色=覆盖率>94.5%，橙色=最优 RMSE\"\n    statistical_reporting: \"点估计值（基于多次重复实验）\"\n    num_baselines: 3\n    design_note: \"用颜色而非加粗来区分不同指标的最优，避免视觉混乱；17 个数据集的大规模验证增强说服力；将任务按类别（emotion/hate speech/misinformation 等）分组展示\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"理论证明、额外实验细节、CBP 数据集详细结果\"\n    reason: \"主文聚焦方法和核心实证，将数学证明和细节数据放入在线补充材料以保持主文简洁\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f120239c-285e-47d8-ade0-7b030c972839",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3SCqsArDD4DcARMdwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4cd9b50-bed6-4776-9510-6c35f3c2eef7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToH2ikX3iECuyUQwpwnjRN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1166,
      "cache_read_input_tokens": 25420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1166,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 20 · 2026-05-21T16:39:25.724Z_

<details><summary>↩ Tool result · `toolu_013SD41xYbWdPThfVo3YDTin`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/distill_tmp/egami2024dsl.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4cd9b50-bed6-4776-9510-6c35f3c2eef7",
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "eceaa759-8ca2-4ffc-9dbc-a0175a60b34c",
  "sourceToolAssistantUUID": "d4cd9b50-bed6-4776-9510-6c35f3c2eef7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T16:40:22.523Z_

<details open><summary>🔧 Tool call — Write · `toolu_01X8nwndku6di4pNVYqinwGE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/distill_tmp/audinet2025benchmark.yaml",
  "content": "paper_key: \"audinet2025benchmark\"\ntitle: \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\"\nvenue: \"EMNLP 2025\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Reference Model (full expert annotation, θ*)\"\n    - \"Classical Estimator (limited expert only, θ†)\"\n    - \"Imputation Estimator (LLM only, θ̃)\"\n    - \"Prediction-Powered Inference (PPI)\"\n    - \"Design-based Supervised Learning (DSL)\"\n  metrics:\n    - {name: \"Standardized RMSE (sRMSE)\", direction: \"lower_better\"}\n    - {name: \"Standardized Bias\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Multi-domain Sentiment (Amazon reviews)\", size: \"11,914\"}\n    - {name: \"Misinfo-general (British newspapers)\", size: \"10,000\"}\n    - {name: \"Bias in Biographies (online biographies)\", size: \"10,000\"}\n    - {name: \"Germeval18 (German tweets)\", size: \"5,676\"}\n  ablation_dimensions:\n    - \"expert annotation count (n)\"\n    - \"total sample size (N)\"\n    - \"LLM/model type (BERT+LR, DeepSeek v3, Phi-4, Claude 3.7 Sonnet)\"\n    - \"collinearity in feature set\"\n  training_recipe:\n    optimizer: \"N/A (statistical estimation, not neural training)\"\n    lr: \"N/A\"\n    hardware: \"N/A (LLM inference via API for Claude/DeepSeek; local for BERT/Phi-4)\"\n  method_family: \"Benchmark comparison of semi-parametric debiasing estimators for LLM annotations\"\n\npositioning:\n  core_claim: \"DSL 和 PPI 两种去偏方法在有限样本中的首次系统性实证对比——DSL 平均表现更优但稳定性更差，且对特征共线性敏感；实践者应同时报告两种方法的结果\"\n  key_results: \"DSL 在大多数数据集上 sRMSE 比 PPI 低 15-30%；但在 Misinfo-general 数据集上 DSL 表现劣于 PPI 和 classical estimator；最少 200 个 expert 标注即可实现有效去偏（sRMSE < 0.2）\"\n  limitations:\n    - \"仅对比 DSL 和 PPI，未涵盖新兴方法如 predict-then-debias\"\n    - \"限于二分类任务\"\n    - \"仅覆盖英语和德语短文本\"\n    - \"假设 expert 标注为 ground truth，未考虑 expert 噪声\"\n    - \"下游评估仅限于 logistic regression\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"化繁为简型\"\n  hook: \"以 LLM 正在变革计算社会科学各学科为背景开篇，强调 LLM 标注的广泛应用（政治意识形态、写作风格、礼貌度、流行病预测等），然后指出标注不一致性会导致误导性结论\"\n  tension: \"去偏方法（PPI 和 DSL）理论上能保证无偏估计，但实践者缺乏有限样本下的性能指导——理论保证是渐近的，实际应用中样本有限，不存在闭式表达式来连接方法效力与标注预算分配\"\n  key_insight: \"在 intro 第四段通过两个研究问题揭示：(RQ1) 何时去偏后的大规模 LLM 标注优于小规模纯 expert 标注？(RQ2) 两种去偏方法在不同数据集和标注器上的性能差异如何？关键发现是 DSL 平均更优但不稳定，与特征共线性相关\"\n  argument_chain: \"LLM 标注广泛应用 → 标注偏差导致下游推断误导 → 去偏方法理论有效但缺乏有限样本指导 → 提出两个研究问题 → 系统性 benchmark 实验 → 发现 DSL 平均更优但不稳定 → 建议同时报告两种方法\"\n  contribution_framing: \"两个贡献，措辞为 'We make two contributions'：(1) 研究各方法性能如何随 expert 标注数量扩展 (2) 跨任务对比 DSL 和 PPI。强调实践导向——为应用研究者提供指导\"\n  intro_structure: \"4 段：Para1 LLM 变革 CSS 的大背景 → Para2 核心问题（标注偏差导致误导） → Para3 去偏方法存在但缺乏实践指导 → Para4 研究问题和主要发现预览\"\n  notable_technique: \"将论文定位为'bridge between theory and practice'——不提出新方法，而是为已有方法提供缺失的实证指导。这种 benchmark 论文的叙事策略是：承认理论的价值，但指出理论到实践的 gap，然后用系统实验填补。成本-收益分析（将 expert 标注成本换算为 LLM 调用等价数）是很有实践价值的分析角度\"\n\nfigures:\n  figure_count: 4\n  figure1:\n    type: \"method_overview\"\n    description: \"2×2 网格图，展示四种估计策略：(左上) reference model 用全部 N 个 expert 标注（橙色点）；(右上) classical model 仅用 n 个 expert 标注；(左下) imputation model 用 N 个 LLM 标注（蓝色点）；(右下) debiased models 结合两种标注来源\"\n    narrative_role: \"在方法背景部分提供直观的四种方案对比视图，帮助读者快速理解去偏方法的核心思想——结合小量 expert 和大量 LLM 标注\"\n    design_elements: [\"颜色编码（橙色=expert, 蓝色=LLM）\", \"2×2 对比布局\", \"样本量标注 (N vs n)\", \"简洁示意图风格\"]\n    visual_style: \"2×2 网格，每格用彩色圆点表示样本，橙蓝双色区分标注来源；白底简洁风格，无多余装饰；标题标注每种方案名称\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Experiment 1：DSL、PPI、classical estimator 的 sRMSE 随 expert 标注比例变化（跨数据集和标注方法平均）\"\n      how_gain_highlighted: \"DSL 曲线在大部分区间低于 PPI 和 classical，直观展示优势；但在高标注比例时出现交叉，暴露不稳定性\"\n      design_note: \"使用 2σ 置信区间带展示不确定性；曲线交叉点是论文核心发现之一，图表设计自然引导读者发现这一现象\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Experiment 2：三种方法的 sRMSE 随总样本量 N 变化（固定 expert 标注数）\"\n      how_gain_highlighted: \"classical estimator 保持水平线（不使用 LLM 标注），DSL 和 PPI 随 N 增加而下降，展示增加 LLM 标注的边际价值\"\n      design_note: \"水平参考线（classical）对比下降曲线（DSL/PPI）的视觉对比非常清晰；分面展示三个固定 n 水平（200/1000/5000）\"\n  ablation_figures:\n    - figure_id: \"Figure 10 (appendix)\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"collinearity removal threshold (r²>0.9)\", \"dataset\"]\n      design_note: \"展示去除共线性特征后 DSL 性能改善，支持'DSL 对共线性敏感'的核心发现\"\n  figure_narrative_role: \"Figure 1 (背景: 四种估计策略概览) → Figure 2 (方法: 两个实验设计示意) → Figure 3 (结果: Exp1 主结果) → Figure 4 (结果: Exp2 主结果) → Appendix Figures (深入: 分数据集、去共线性等细节)\"\n\ntables:\n  table_count: 3\n  main_result_table:\n    table_id: \"Table 3\"\n    row_axis: \"methods (PPI vs DSL)\"\n    col_axis: \"comparison dimensions (bias correction mechanism, guarantees, variance components)\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dimension\"\n    highlight_strategy: \"无数值加粗，而是以文本描述形式对比两种方法的理论性质\"\n    statistical_reporting: \"定性对比而非定量数值\"\n    num_baselines: 2\n    design_note: \"这是一个方法论对比表而非实验结果表——用结构化文本描述两种方法在偏差修正机制、理论保证、方差成分上的差异，帮助读者理解为何 DSL 对共线性敏感\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"dataset\", \"LLM/model type\"]\n      variation_style: \"full_numbers\"\n      design_note: \"展示各数据集-模型组合的特征间 Pearson r² 相关性，定量支持共线性分析\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"系统提示词（Table 1）、分数据集详细结果图（Figures 5-15）、标准化偏差图、去共线性后结果\"\n    reason: \"主文仅展示跨数据集平均结果以保持简洁，附录提供分数据集和分模型的完整分解，供需要细节的读者参考\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eceaa759-8ca2-4ffc-9dbc-a0175a60b34c",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3SCqsArDD4DcARMdwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4d9e4e2-376a-4005-9d67-94320d7dbdf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToH2ikX3iECuyUQwpwnjRN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1166,
      "cache_read_input_tokens": 25420,
      "output_tokens": 5667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5667,
          "cache_read_input_tokens": 25420,
          "cache_creation_input_tokens": 1166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1166,
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

_source line 22 · 2026-05-21T16:40:22.533Z_

<details><summary>↩ Tool result · `toolu_01X8nwndku6di4pNVYqinwGE`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/distill_tmp/audinet2025benchmark.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4d9e4e2-376a-4005-9d67-94320d7dbdf0",
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "fb3c902d-b738-44a2-bc99-934e974d291e",
  "sourceToolAssistantUUID": "c4d9e4e2-376a-4005-9d67-94320d7dbdf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T16:40:28.297Z_

Let me verify both files were written correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb3c902d-b738-44a2-bc99-934e974d291e",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3asH92dp53fZCv1gwQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94875206-d089-443b-a296-f10b55d24ccb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vc8bJaZj7mooL2w12UM2cy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5821,
      "cache_read_input_tokens": 26586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5821,
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

_source line 24 · 2026-05-21T16:40:29.268Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DR2o7yyK4pU1idthxTZwD9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/distill_tmp/egami2024dsl.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94875206-d089-443b-a296-f10b55d24ccb",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3asH92dp53fZCv1gwQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1a08fea-818c-4b32-8629-d3d0e4cd2019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vc8bJaZj7mooL2w12UM2cy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5821,
      "cache_read_input_tokens": 26586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5821,
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

### Tool result

_source line 25 · 2026-05-21T16:40:29.274Z_

<details><summary>↩ Tool result · `toolu_01DR2o7yyK4pU1idthxTZwD9`</summary>

```text
1	paper_key: "egami2024dsl"
2	title: "Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models"
3	venue: "NeurIPS 2023"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Surrogate Only (SO)"
9	    - "Gold-Standard Only (GSO)"
10	    - "Supervised Learning (SL)"
11	  metrics:
12	    - {name: "Standardized Root Mean Squared Bias", direction: "lower_better"}
13	    - {name: "Coverage (95% CI)", direction: "higher_better"}
14	    - {name: "RMSE", direction: "lower_better"}
15	  datasets:
16	    - {name: "Congressional Bills Project (CBP)", size: "10,000 documents"}
17	    - {name: "17 CSS benchmark datasets (Ziems et al. 2023)", size: "varies per task"}
18	  ablation_dimensions:
19	    - "gold-standard sample size (n)"
20	    - "surrogate quality (0-shot vs 5-shot)"
21	    - "surrogate accuracy level"
22	  training_recipe:
23	    optimizer: "N/A (statistical estimator, not neural training)"
24	    lr: "N/A"
25	    hardware: "N/A"
26	  method_family: "Doubly-robust semi-parametric estimation with inverse probability weighting"
27	
28	positioning:
29	  core_claim: "即使 surrogate 准确率高达 90%，直接用 LLM 标注做下游回归分析也会导致严重偏差和无效置信区间；DSL 通过 design-based 伪结果构造，在不依赖 surrogate 准确性或 ML 模型正确性的前提下保证一致性和有效推断"
30	  key_results: "90% 准确率的 surrogate 直接使用时 95% CI 覆盖率仅 40%；DSL 在 18 个数据集上实现近 nominal 覆盖率（~95%），同时 RMSE 比 GSO 降低 14-31%"
31	  limitations:
32	    - "需要预先确定语料库，不适用于流式数据场景"
33	    - "需要可靠的 gold-standard 标注（并非所有任务都可获得）"
34	    - "优先保证无偏性和覆盖率而非预测精度，如果目标是纯预测则 SL 可能更优"
35	  relation_to_us: "foundation"
36	
37	narrative:
38	  story_type: "突破局限型"
39	  hook: "以 text-as-data 在社科领域的日益流行开篇，引出 LLM 作为廉价标注工具的趋势，然后用一个震撼性的模拟结果（90% 准确率 → 40% 覆盖率）打破读者对高准确率的安全假设"
40	  tension: "三层递进：(1) 社科研究需要的是下游统计推断而非分类准确率本身；(2) 即使准确率极高的 surrogate 也会导致严重的 measurement error 偏差；(3) 现有方法各有致命缺陷——SO 忽略误差、GSO 浪费数据、SL 依赖模型正确设定"
41	  key_insight: "在第四段通过提出 DSL 方法揭示核心洞察：通过 design-based sampling 框架构造伪结果（pseudo-outcome），利用逆概率加权的偏差修正项，无需假设 surrogate 准确性或 ML 模型正确性即可获得有效推断。关键公式是 Y_tilde = g_hat + (R/pi) * (Y - g_hat)"
42	  argument_chain: "LLM 标注日益流行 → 社科需要下游推断而非分类 → 即使高准确率也导致偏差（模拟证明） → 现有三种方法各有缺陷 → DSL 通过 design-based 伪结果解决 → 理论保证（一致性+渐近正态性） → 18 个数据集实证验证"
43	  contribution_framing: "四个贡献，用编号列表明确呈现：(1) 新估计量 (2) 强理论保证 (3) 矩估计扩展 (4) 实证验证。措辞强调'guarantee'和'without requiring'来突出无条件性"
44	  intro_structure: "5 段：Para1 领域背景（text-as-data 趋势）→ Para2 核心问题（社科需要回归推断）→ Para3 现有方法失败的震撼证据（模拟 Figure 1a）→ Para4 提出 DSL 及其保证 → Para5 论文结构和命名理由"
45	  notable_technique: "用 Figure 1(a) 的模拟结果作为'震撼弹'：在 intro 第三段就展示 90% 准确率导致 40% 覆盖率的反直觉结果，迫使读者接受问题的严重性。这种'先打破安全假设再提出方案'的叙事手法非常有效"
46	
47	figures:
48	  figure_count: 3
49	  figure1:
50	    type: "motivation"
51	    description: "双面板图。Panel (a) 是模拟实验线图，展示 SO 和 DSL 在不同 surrogate 准确率下的偏差、覆盖率和 RMSE 对比；Panel (b) 是 DSL 方法流程示意图，展示从 Y/Q/X 输入到伪结果构造再到下游回归的完整 pipeline"
52	    narrative_role: "在 intro 中作为震撼性证据使用——Panel (a) 证明问题严重性（高准确率仍导致低覆盖率），Panel (b) 直观展示解决方案的核心机制"
53	    design_elements: ["双面板对比布局（问题 vs 方案）", "线图展示趋势变化", "流程图配合数学符号标注", "通过覆盖率急剧下降制造视觉冲击"]
54	    visual_style: "左右双面板，Panel (a) 使用标准学术线图风格展示 bias/coverage/RMSE 三个指标随样本量变化；Panel (b) 使用方框+箭头流程图，标注变量符号和维度，简洁清晰"
55	  result_figures:
56	    - figure_id: "Figure 2"
57	      viz_type: "line_plot"
58	      what_compared: "四种估计量（SO/GSO/SL/DSL）在 Congressional Bills 数据上的 bias、coverage、RMSE 随 gold-standard 样本量变化"
59	      how_gain_highlighted: "DSL 和 GSO 的覆盖率线稳定在 95% nominal 水平，而 SO 显著偏离；DSL 的 RMSE 线低于 GSO"
60	      design_note: "三个指标分面展示，横轴统一为样本量，便于跨指标对比；覆盖率面板有 95% 参考线"
61	    - figure_id: "Figure 3"
62	      viz_type: "line_plot"
63	      what_compared: "DSL 相对 GSO 的效率增益在不同 surrogate 质量（0-shot 到 5-shot）下的变化"
64	      how_gain_highlighted: "展示 surrogate 质量提升时效率增益单调递增的趋势"
65	      design_note: "专注于方法间的相对比较而非绝对性能，突出 surrogate 质量和效率增益的正相关关系"
66	  ablation_figures: []
67	  figure_narrative_role: "Figure 1 (intro motivation: 问题严重性 + 方案概览) → Figure 2 (主实验: CBP 数据上四种方法全面对比) → Figure 3 (深入分析: surrogate 质量对效率的影响)"
68	
69	tables:
70	  table_count: 3
71	  main_result_table:
72	    table_id: "Table 3"
73	    row_axis: "datasets (17 CSS benchmark tasks)"
74	    col_axis: "methods × metrics (bias, coverage, RMSE)"
75	    row_organization: "by_category"
76	    col_organization: "grouped_by_metric"
77	    highlight_strategy: "颜色编码：绿色=最低偏差，蓝色=覆盖率>94.5%，橙色=最优 RMSE"
78	    statistical_reporting: "点估计值（基于多次重复实验）"
79	    num_baselines: 3
80	    design_note: "用颜色而非加粗来区分不同指标的最优，避免视觉混乱；17 个数据集的大规模验证增强说服力；将任务按类别（emotion/hate speech/misinformation 等）分组展示"
81	  ablation_tables: []
82	  supplementary_tables:
83	    in_appendix: true
84	    content: "理论证明、额外实验细节、CBP 数据集详细结果"
85	    reason: "主文聚焦方法和核心实证，将数学证明和细节数据放入在线补充材料以保持主文简洁"
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1a08fea-818c-4b32-8629-d3d0e4cd2019",
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "88955fa3-4738-4eba-8a96-a49ecc1747d9",
  "sourceToolAssistantUUID": "f1a08fea-818c-4b32-8629-d3d0e4cd2019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T16:40:29.404Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xg1JZmgFeRcMHSkKFtriXu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/distill_tmp/audinet2025benchmark.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88955fa3-4738-4eba-8a96-a49ecc1747d9",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3asH92dp53fZCv1gwQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ff7b068-6f01-4fce-8c05-d437d05ca858",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vc8bJaZj7mooL2w12UM2cy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5821,
      "cache_read_input_tokens": 26586,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5821
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 26586,
          "cache_creation_input_tokens": 5821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5821,
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

_source line 27 · 2026-05-21T16:40:29.408Z_

<details><summary>↩ Tool result · `toolu_01Xg1JZmgFeRcMHSkKFtriXu`</summary>

```text
1	paper_key: "audinet2025benchmark"
2	title: "Benchmarking Debiasing Methods for LLM-based Parameter Estimates"
3	venue: "EMNLP 2025"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Reference Model (full expert annotation, θ*)"
9	    - "Classical Estimator (limited expert only, θ†)"
10	    - "Imputation Estimator (LLM only, θ̃)"
11	    - "Prediction-Powered Inference (PPI)"
12	    - "Design-based Supervised Learning (DSL)"
13	  metrics:
14	    - {name: "Standardized RMSE (sRMSE)", direction: "lower_better"}
15	    - {name: "Standardized Bias", direction: "lower_better"}
16	  datasets:
17	    - {name: "Multi-domain Sentiment (Amazon reviews)", size: "11,914"}
18	    - {name: "Misinfo-general (British newspapers)", size: "10,000"}
19	    - {name: "Bias in Biographies (online biographies)", size: "10,000"}
20	    - {name: "Germeval18 (German tweets)", size: "5,676"}
21	  ablation_dimensions:
22	    - "expert annotation count (n)"
23	    - "total sample size (N)"
24	    - "LLM/model type (BERT+LR, DeepSeek v3, Phi-4, Claude 3.7 Sonnet)"
25	    - "collinearity in feature set"
26	  training_recipe:
27	    optimizer: "N/A (statistical estimation, not neural training)"
28	    lr: "N/A"
29	    hardware: "N/A (LLM inference via API for Claude/DeepSeek; local for BERT/Phi-4)"
30	  method_family: "Benchmark comparison of semi-parametric debiasing estimators for LLM annotations"
31	
32	positioning:
33	  core_claim: "DSL 和 PPI 两种去偏方法在有限样本中的首次系统性实证对比——DSL 平均表现更优但稳定性更差，且对特征共线性敏感；实践者应同时报告两种方法的结果"
34	  key_results: "DSL 在大多数数据集上 sRMSE 比 PPI 低 15-30%；但在 Misinfo-general 数据集上 DSL 表现劣于 PPI 和 classical estimator；最少 200 个 expert 标注即可实现有效去偏（sRMSE < 0.2）"
35	  limitations:
36	    - "仅对比 DSL 和 PPI，未涵盖新兴方法如 predict-then-debias"
37	    - "限于二分类任务"
38	    - "仅覆盖英语和德语短文本"
39	    - "假设 expert 标注为 ground truth，未考虑 expert 噪声"
40	    - "下游评估仅限于 logistic regression"
41	  relation_to_us: "foundation"
42	
43	narrative:
44	  story_type: "化繁为简型"
45	  hook: "以 LLM 正在变革计算社会科学各学科为背景开篇，强调 LLM 标注的广泛应用（政治意识形态、写作风格、礼貌度、流行病预测等），然后指出标注不一致性会导致误导性结论"
46	  tension: "去偏方法（PPI 和 DSL）理论上能保证无偏估计，但实践者缺乏有限样本下的性能指导——理论保证是渐近的，实际应用中样本有限，不存在闭式表达式来连接方法效力与标注预算分配"
47	  key_insight: "在 intro 第四段通过两个研究问题揭示：(RQ1) 何时去偏后的大规模 LLM 标注优于小规模纯 expert 标注？(RQ2) 两种去偏方法在不同数据集和标注器上的性能差异如何？关键发现是 DSL 平均更优但不稳定，与特征共线性相关"
48	  argument_chain: "LLM 标注广泛应用 → 标注偏差导致下游推断误导 → 去偏方法理论有效但缺乏有限样本指导 → 提出两个研究问题 → 系统性 benchmark 实验 → 发现 DSL 平均更优但不稳定 → 建议同时报告两种方法"
49	  contribution_framing: "两个贡献，措辞为 'We make two contributions'：(1) 研究各方法性能如何随 expert 标注数量扩展 (2) 跨任务对比 DSL 和 PPI。强调实践导向——为应用研究者提供指导"
50	  intro_structure: "4 段：Para1 LLM 变革 CSS 的大背景 → Para2 核心问题（标注偏差导致误导） → Para3 去偏方法存在但缺乏实践指导 → Para4 研究问题和主要发现预览"
51	  notable_technique: "将论文定位为'bridge between theory and practice'——不提出新方法，而是为已有方法提供缺失的实证指导。这种 benchmark 论文的叙事策略是：承认理论的价值，但指出理论到实践的 gap，然后用系统实验填补。成本-收益分析（将 expert 标注成本换算为 LLM 调用等价数）是很有实践价值的分析角度"
52	
53	figures:
54	  figure_count: 4
55	  figure1:
56	    type: "method_overview"
57	    description: "2×2 网格图，展示四种估计策略：(左上) reference model 用全部 N 个 expert 标注（橙色点）；(右上) classical model 仅用 n 个 expert 标注；(左下) imputation model 用 N 个 LLM 标注（蓝色点）；(右下) debiased models 结合两种标注来源"
58	    narrative_role: "在方法背景部分提供直观的四种方案对比视图，帮助读者快速理解去偏方法的核心思想——结合小量 expert 和大量 LLM 标注"
59	    design_elements: ["颜色编码（橙色=expert, 蓝色=LLM）", "2×2 对比布局", "样本量标注 (N vs n)", "简洁示意图风格"]
60	    visual_style: "2×2 网格，每格用彩色圆点表示样本，橙蓝双色区分标注来源；白底简洁风格，无多余装饰；标题标注每种方案名称"
61	  result_figures:
62	    - figure_id: "Figure 3"
63	      viz_type: "line_plot"
64	      what_compared: "Experiment 1：DSL、PPI、classical estimator 的 sRMSE 随 expert 标注比例变化（跨数据集和标注方法平均）"
65	      how_gain_highlighted: "DSL 曲线在大部分区间低于 PPI 和 classical，直观展示优势；但在高标注比例时出现交叉，暴露不稳定性"
66	      design_note: "使用 2σ 置信区间带展示不确定性；曲线交叉点是论文核心发现之一，图表设计自然引导读者发现这一现象"
67	    - figure_id: "Figure 4"
68	      viz_type: "line_plot"
69	      what_compared: "Experiment 2：三种方法的 sRMSE 随总样本量 N 变化（固定 expert 标注数）"
70	      how_gain_highlighted: "classical estimator 保持水平线（不使用 LLM 标注），DSL 和 PPI 随 N 增加而下降，展示增加 LLM 标注的边际价值"
71	      design_note: "水平参考线（classical）对比下降曲线（DSL/PPI）的视觉对比非常清晰；分面展示三个固定 n 水平（200/1000/5000）"
72	  ablation_figures:
73	    - figure_id: "Figure 10 (appendix)"
74	      viz_type: "line_plot"
75	      dimensions_varied: ["collinearity removal threshold (r²>0.9)", "dataset"]
76	      design_note: "展示去除共线性特征后 DSL 性能改善，支持'DSL 对共线性敏感'的核心发现"
77	  figure_narrative_role: "Figure 1 (背景: 四种估计策略概览) → Figure 2 (方法: 两个实验设计示意) → Figure 3 (结果: Exp1 主结果) → Figure 4 (结果: Exp2 主结果) → Appendix Figures (深入: 分数据集、去共线性等细节)"
78	
79	tables:
80	  table_count: 3
81	  main_result_table:
82	    table_id: "Table 3"
83	    row_axis: "methods (PPI vs DSL)"
84	    col_axis: "comparison dimensions (bias correction mechanism, guarantees, variance components)"
85	    row_organization: "by_category"
86	    col_organization: "grouped_by_dimension"
87	    highlight_strategy: "无数值加粗，而是以文本描述形式对比两种方法的理论性质"
88	    statistical_reporting: "定性对比而非定量数值"
89	    num_baselines: 2
90	    design_note: "这是一个方法论对比表而非实验结果表——用结构化文本描述两种方法在偏差修正机制、理论保证、方差成分上的差异，帮助读者理解为何 DSL 对共线性敏感"
91	  ablation_tables:
92	    - table_id: "Table 2"
93	      what_varied: ["dataset", "LLM/model type"]
94	      variation_style: "full_numbers"
95	      design_note: "展示各数据集-模型组合的特征间 Pearson r² 相关性，定量支持共线性分析"
96	  supplementary_tables:
97	    in_appendix: true
98	    content: "系统提示词（Table 1）、分数据集详细结果图（Figures 5-15）、标准化偏差图、去共线性后结果"
99	    reason: "主文仅展示跨数据集平均结果以保持简洁，附录提供分数据集和分模型的完整分解，供需要细节的读者参考"
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ff7b068-6f01-4fce-8c05-d437d05ca858",
  "isSidechain": true,
  "promptId": "3f021609-9c10-4599-8531-4bfc2dd94b34",
  "agentId": "adca6a818cb4d9bd5",
  "type": "user",
  "uuid": "3a8e1da8-1a19-4a0d-b539-8a67725c63da",
  "sourceToolAssistantUUID": "9ff7b068-6f01-4fce-8c05-d437d05ca858",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T16:40:43.236Z_

Both YAML files are complete and verified. Here is the summary:

**Files written:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/distill_tmp/egami2024dsl.yaml`
- `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/distill_tmp/audinet2025benchmark.yaml`

**Key extraction highlights:**

**egami2024dsl (NeurIPS 2023)** -- DSL foundational method paper:
- Story type: "突破局限型" -- uses a shocking simulation (90% accuracy -> 40% CI coverage) as intro hook
- 5-paragraph intro structure with 4 explicit contributions
- 3 figures (Fig 1 is dual-panel motivation+method, Figs 2-3 are line plots), 3 tables (Table 3 is the 17-dataset main result with color-coded highlights)
- Baselines: SO/GSO/SL; Metrics: bias/coverage/RMSE; 18 datasets total
- Core positioning: design-based pseudo-outcome guarantees valid inference without requiring surrogate accuracy or ML model correctness

**audinet2025benchmark (EMNLP 2025)** -- DSL vs PPI benchmark paper:
- Story type: "化繁为简型" -- bridges theory-practice gap for debiasing methods
- 4-paragraph intro with 2 RQs and 2 contributions
- 4 main figures (Fig 1 is 2x2 method overview grid, Figs 3-4 are main result line plots), 3 tables (Table 3 is qualitative PPI vs DSL comparison)
- 4 datasets x 4 LLM/model types; Metrics: sRMSE, standardized bias
- Core finding: DSL outperforms PPI by 15-30% sRMSE on average but is less stable, particularly sensitive to feature collinearity; recommends reporting both methods

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a8e1da8-1a19-4a0d-b539-8a67725c63da",
  "isSidechain": true,
  "agentId": "adca6a818cb4d9bd5",
  "requestId": "req_011CbG3bNrdQqqw1hC3RemCr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dc706c2-f523-4256-9f9a-4f92e2d1492a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/distiller_bd7aa1a3",
  "sessionId": "5cfd0b44-a88d-47c7-a52d-960d82d8144a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8wAxmySZZhS41fKqDeVt4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6086,
      "cache_read_input_tokens": 32407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6086,
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
