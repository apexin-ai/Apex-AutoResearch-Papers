# research exp 009 wang differentiation

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_research_exp_009_wang_differentiation_20260519T131120.jsonl`
- **Structured JSON:** [`3e3d51981b4ced3aea85.json`](../../sessions/3e/3e3d51981b4ced3aea85.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-19T13:16:53.548059+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T13:16:53.548393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T13:16:53.548570+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.06457",
  "prompt": "Extract the full paper title, all authors, submission date, and the complete abstract. Return them verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2507.06457",
    "prompt": "Extract the full paper title, all authors, submission date, and the complete abstract. Return them verbatim."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T13:16:53.548818+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
  "prompt": "Extract the COMPLETE text of this paper, section by section. For every section and subsection, return the full text verbatim. I need every paragraph, every claim, every result. Do not summarize - return the actual text. Pay special attention to any mentions of: convergence, converge, converging, equalizer, equalize, equalizing, architecture-agnostic, architecture-independent, attention ratio, hybrid, mixing, per-example, sample-level, instance-level, scale, scaling, model size, cross-architecture, across architectures. Mark these passages clearly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
    "prompt": "Extract the COMPLETE text of this paper, section by section. For every section and subsection, return the full text verbatim. I need every paragraph, every claim, every result. Do not summarize - return the actual text. Pay special attention to any mentions of: convergence, converge, converging, equalizer, equalize, equalizing, architecture-agnostic, architecture-independent, attention ratio, hybrid, mixing, per-example, sample-level, instance-level, scale, scaling, model size, cross-architecture, across architectures. Mark these passages clearly."
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T13:16:53.548978+00:00_

# Paper Details

**Full Title:** "A Systematic Analysis of Hybrid Linear Attention"

**Authors:** Dustin Wang, Rui-Jie Zhu, Steven Abreu, Yong Shan, Taylor Kergan, Yuqi Pan, Yuhong Chou, Zheng Li, Ge Zhang, Wenhao Huang, Jason Eshraghian

**Submission Date:** July 8, 2025

**Abstract:**
The paper addresses how Transformers struggle with quadratic complexity on lengthy sequences. The researchers evaluated multiple linear attention mechanisms when used alone and in hybrid combinations with full attention. They trained 72 models across different parameter sizes and token budgets, testing six linear attention variants at various mixing ratios.

Their findings show that strong standalone linear models don't necessarily perform well in hybrid configurations. Language modeling performance remains consistent across different attention ratios, while recall capabilities improve significantly when full attention layers comprise a greater proportion—particularly when the linear-to-full ratio falls below 3:1. The study identifies selective gating, hierarchical recurrence, and managed forgetting as essential features. They recommend architectures like HGRN-2 or GatedDeltaNet with ratios between 3:1 and 6:1 for achieving competitive recall efficiency. The researchers have released their 72 trained models publicly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T13:16:53.549133+00:00_

# Analysis of "A Systematic Analysis of Hybrid Linear Attention"

I appreciate your request, but I need to clarify what I can appropriately provide. Rather than reproduce the entire paper verbatim (which would constitute substantial copyright infringement), I'll offer a structured extraction of key findings with marked passages addressing your specific interests.

## Key Passages on Your Areas of Interest

**On Hybrid Architecture and Mixing:**
- "Hybrid Linear Attention models have emerged... This approach interleaves full attention layers with linear attention layers."
- The paper tests "five configurations for each linear attention mechanism: linear-to-full attention ratios of 24:1, 12:1, 6:1, 3:1"

**On Architecture-Level Performance (marked):**
- "Superior standalone linear models do not necessarily excel in hybrids" — this directly contradicts architecture-independent assumptions
- Critical finding: "GatedDeltaNet achieves the highest standalone accuracy. However, when hybridized, HGRN2 at a 6:1 linear-to-full attention ratio outperforms it"

**On Scaling/Model Size Effects:**
- Models tested at "340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens)"
- Results suggest findings don't necessarily "persist at the 10B+ scale"

**On Convergence/Equalization:**
- Language modeling performance "remains largely flat across all ratio configurations" and "cluster around 0.55-0.57"
- Recall performance shows "clear upward trend as the proportion of full-attention layers increases" but "saturates around 3:1"

## Core Recommendation

The authors recommend "HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1" for achieving Transformer-level recall efficiently.

Would you like me to focus on specific sections in greater detail?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T13:16:53.549310+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
  "prompt": "Find and extract VERBATIM every sentence or paragraph that contains any of these words: convergence, converge, converging, equalize, equalizer, equalizing, flatten, flat, saturate, saturation, plateau, diminishing. Include the section name where each passage appears. I need the exact original wording, not paraphrases."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
    "prompt": "Find and extract VERBATIM every sentence or paragraph that contains any of these words: convergence, converge, converging, equalize, equalizer, equalizing, flatten, flat, saturate, saturation, plateau, diminishing. Include the section name where each passage appears. I need the exact original wording, not paraphrases."
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T13:16:53.549439+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
  "prompt": "Find and extract VERBATIM every sentence or paragraph that discusses: (1) per-example or sample-level or instance-level analysis, (2) cross-architecture comparison or architecture-agnostic findings, (3) scale-dependent or model-size-dependent results (340M vs 1.3B differences), (4) task-specific or task-dependent patterns. Include the section name for each passage. Return exact original text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
    "prompt": "Find and extract VERBATIM every sentence or paragraph that discusses: (1) per-example or sample-level or instance-level analysis, (2) cross-architecture comparison or architecture-agnostic findings, (3) scale-dependent or model-size-dependent results (340M vs 1.3B differences), (4) task-specific or task-dependent patterns. Include the section name for each passage. Return exact original text."
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T13:16:53.549569+00:00_

# Extracted Passages Containing Target Words

## Section: 4.2 Impact of the Linear-to-Full Attention Ratio

**Convergence/Saturate:**
"Performance rises from pure linear configurations (around 0.1-0.35 RULER score) towards the full-attention baseline (dashed line at approximately 0.42). Notably, most architectures **approach or exceed this baseline at the 3:1 ratio**, with some like DeltaNet and Gated-DeltaNet achieving their peak recall performance at this configuration."

**Plateau:**
"All architectures show a clear upward trend as the proportion of full-attention layers increases... Notably, most architectures approach or exceed this baseline at the 3:1 ratio, with some like DeltaNet and Gated-DeltaNet achieving their peak recall performance at this configuration. This trend demonstrates that recall capability benefits substantially from increased full-attention allocation, unlike language modeling performance."

## Section: 2 Related work

**Plateau:**
"Empirically, long-context quality rises steeply once a few full-attention blocks or heads are present, after which **perplexity plateaus**; thus the linear:full ratio primarily controls recall."

## Section: Introduction

**Diminishing Returns:**
"Finally, Ref. [14] has demonstrated that simply increasing the state size of linear attention models yields **diminishing returns**."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T13:16:53.549748+00:00_

# Analysis of Comparative Study Patterns

## (1) Per-Example/Sample-Level Analysis
**Not found.** The paper focuses on aggregate metrics across benchmarks rather than individual example analysis.

## (2) Cross-Architecture Comparison

**Abstract:**
"We systematically evaluate various linear attention models across generations—vector recurrences to advanced gating mechanisms—both standalone and hybridized."

**Section 3.3:**
"Our main objective is to understand the roles of state size and state management in hybrid stacks."

**Section 4.1:**
"We investigate whether linear-attention architectures that excel in standalone evaluation maintain their relative performance when combined with full attention in hybrid configurations."

**Section 4.5:**
"Hybrid quality cannot be inferred from standalone performance. GatedDeltaNet is strongest in purely linear form, yet HGRN-2 delivers the best results once full-attention layers are added."

## (3) Scale-Dependent Results

**Section 4.1:**
"At the 340M parameter scale, GatedDeltaNet achieves the highest standalone accuracy. However, when hybridized, HGRN2 at a 6:1 linear-to-full attention ratio outperforms it."

**Section 4.1:**
"The same pattern emerges at 1.3B parameters: GatedDeltaNet leads in standalone evaluation but becomes comparable with HGRN2 after hybridization."

## (4) Task-Specific Patterns

**Section 4.2:**
"Language modeling performance remains largely flat across all ratio configurations... All architectures show a clear upward trend as the proportion of full-attention layers increases" (for recall).

**Section 4.3:**
"Recall rises steadily as full-attention layers are added and saturates around 3:1."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T13:16:53.549924+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
  "prompt": "Extract the COMPLETE text of Section 4 (Findings/Results) and Section 5 (Discussion/Conclusion). Include ALL subsections (4.1, 4.2, 4.3, 4.4, 4.5, etc.) and their full text. I need every sentence verbatim - do not skip or summarize anything. Also extract any section about \"Key Takeaways\" or \"Recommendations\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
    "prompt": "Extract the COMPLETE text of Section 4 (Findings/Results) and Section 5 (Discussion/Conclusion). Include ALL subsections (4.1, 4.2, 4.3, 4.4, 4.5, etc.) and their full text. I need every sentence verbatim - do not skip or summarize anything. Also extract any section about \"Key Takeaways\" or \"Recommendations\"."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T13:16:53.550052+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
  "prompt": "Extract the COMPLETE text of Section 1 (Introduction) and Section 3 (Methodology/Experimental Setup). Include every paragraph verbatim. I need the exact text about what models they trained, what benchmarks they used, what metrics, and how they set up their experiments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
    "prompt": "Extract the COMPLETE text of Section 1 (Introduction) and Section 3 (Methodology/Experimental Setup). Include every paragraph verbatim. I need the exact text about what models they trained, what benchmarks they used, what metrics, and how they set up their experiments."
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T13:16:53.550187+00:00_

# Section 1: Introduction

The researchers investigated whether "superior standalone linear models do not necessarily excel in hybrids." They trained 72 models across two scales: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering "six linear attention variants across five hybridization ratios."

Their core research questions were: (1) Does better standalone performance guarantee superior hybrid architecture? (2) Which aspects are more influenced by full-to-linear ratios: language modeling or recall? (3) What architectural components optimize both metrics?

# Section 3: Methodology

**Models Evaluated:** The study examined linear attention spanning three generations—from vector recurrences (HGRN, Hawk) to matrix-valued states via outer products (RetNet, GLA, HGRN-2, Mamba-2, RWKV-6) to delta-rule mechanisms (DeltaNet, Gated DeltaNet).

**Hybridization Strategy:** They used "a repeating block of two conceptually different layers: Linear–attention layer" with constant-size state and "Full-attention layer" with standard softmax. They tested "five configurations for each linear attention mechanism: linear-to-full attention ratios of 24:1, 12:1, 6:1, 3:1, and a fully linear (pure) variant."

**Training Details:** Models used fineweb-edu dataset with AdamW optimizer and cosine scheduling. The 340M-parameter models trained on 20B tokens (batch size 50k); 1.3B-parameter models trained on 100B tokens (batch size 1M).

**Benchmarks:** Language modeling tasks included "ARC-Challenge, ARC-Easy, HellaSwag, LAMBADA, OpenBookQA, and PIQA," while recall evaluation used "RULER, a suite of benchmarks that assess a model's performance on retrieval, multi-hop tracing, aggregation, and question answering."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T13:16:53.550360+00:00_

# Section 4: Empirical Study

## 4.1 Standalone Performance versus Hybrid Performance

The research demonstrates that "linear-attention architectures that excel in standalone evaluation maintain their relative performance when combined with full attention in hybrid configurations" is false. At 340M parameters, GatedDeltaNet achieves highest standalone accuracy, yet HGRN2 at 6:1 ratio outperforms it when hybridized, "exceeding both the Transformer baseline and the standalone leader by 1.2 percentage points."

Similar patterns emerge at 1.3B scale: GatedDeltaNet leads standalone but becomes comparable to HGRN2 post-hybridization. The key finding: "The relative performance of different architectures changes substantially when linear and full attention mechanisms are combined."

## 4.2 Impact of the Linear-to-Full Attention Ratio

Language modeling performance "remains largely flat across all ratio configurations" with architectures clustering around 0.55-0.57 average scores. Conversely, recall demonstrates "a clear upward trend as the proportion of full-attention layers increases," rising from pure linear (0.1-0.35 RULER) toward full-attention baseline (~0.42).

"Most architectures approach or exceed this baseline at the 3:1 ratio." Critical insight: "recall capability benefits substantially from increased full-attention allocation, unlike language modeling performance."

Fine-grained RULER subtasks show Single-Key, Multi-Key, and QA are "noticeably affected by changing ratio," while Common Word Extraction and Frequent Word Extraction don't correlate with hybrid ratio.

## 4.3 Architectural Determinants of Hybrid Effectiveness

Three complementary properties emerge as critical:

**Selective gating:** "Architectures that expose their hidden state to a learned, token-wise gate—GatedDeltaNet and HGRN-2—consistently perform best in recall once hybridised, surpassing the Transformer baseline by 2–5 percentage points."

**Hierarchical recurrence:** HGRN-2's two-level pathway
…[truncated 2475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T13:16:53.550532+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
  "prompt": "I need specific details about: (1) Do they use any statistical tests (Spearman correlation, permutation test, t-test, significance test, p-value, confidence interval)? (2) Do they analyze individual examples or only aggregate/average metrics? (3) Do they compare how different architectures converge to similar performance as attention ratio changes? (4) Do they analyze which specific examples or samples benefit from which architecture? (5) What specific numerical scores do they report for 340M vs 1.3B models - are there tables with exact numbers? (6) Do they discuss \"equalizer\" or \"leveling\" effect where architectures become more similar? Extract all relevant passages verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
    "prompt": "I need specific details about: (1) Do they use any statistical tests (Spearman correlation, permutation test, t-test, significance test, p-value, confidence interval)? (2) Do they analyze individual examples or only aggregate/average metrics? (3) Do they compare how different architectures converge to similar performance as attention ratio changes? (4) Do they analyze which specific examples or samples benefit from which architecture? (5) What specific numerical scores do they report for 340M vs 1.3B models - are there tables with exact numbers? (6) Do they discuss \"equalizer\" or \"leveling\" effect where architectures become more similar? Extract all relevant passages verbatim."
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T13:16:53.550675+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
  "prompt": "Extract the content of ALL tables and figures in this paper. For each table, give me the caption and all numerical values. For each figure, give me the caption and describe what is shown. I need the exact numbers they report."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ar5iv.labs.arxiv.org/html/2507.06457",
    "prompt": "Extract the content of ALL tables and figures in this paper. For each table, give me the caption and all numerical values. For each figure, give me the caption and describe what is shown. I need the exact numbers they report."
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T13:16:53.550820+00:00_

# Analysis of Statistical Methods and Details in Hybrid Linear Attention Paper

## (1) Statistical Tests
**Finding:** No statistical significance testing is employed.

The paper reports numerical results without p-values, confidence intervals, or formal hypothesis tests. Tables 2-6 present point estimates only, with no error bars or significance markers.

## (2) Individual Examples vs. Aggregate Metrics
**Finding:** Only aggregate metrics are reported.

The paper states: "All evaluation benchmarks are conducted in a zero-shot manner without any task-specific fine-tuning." Results are reported as averaged scores across benchmarks (e.g., "Avg" columns in Tables 2-3). No per-example analysis or error analysis is provided.

## (3) Convergence Analysis Across Ratios
**Finding:** They describe convergence patterns but not formal convergence analysis.

The authors observe: "Language modeling performance remains largely flat across all ratio configurations. Most architectures cluster around 0.55-0.57 average LM score, with minimal variation." Figure 3 visualizes this convergence graphically without statistical quantification of the "flattening" effect.

## (4) Architecture-Specific Sample Benefits
**Finding:** No per-sample analysis conducted.

The paper does not identify which examples benefit from which architectures. Analysis remains at the benchmark level, not individual instances.

## (5) Exact Numerical Scores: 340M vs. 1.3B
**340M Results (Table 2):**
- HGRN2 6:1: average 0.456
- GatedDeltaNet pure: average 0.442
- Transformer: average 0.444

**1.3B Results (Table 3):**
- HGRN2 6:1: average 0.565
- GatedDeltaNet 24:1: average 0.565
- Transformer: average 0.548

## (6) "Equalizer" or Leveling Effects
**Finding:** Implicitly discussed but not formally named.

The authors note: "The relative performance of different architectures changes substantially when linear and full attention mechanisms are combined," indicating convergence toward similar hybrid performance despit
…[truncated 31 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T13:16:53.550997+00:00_

# Tables and Figures from "A Systematic Analysis of Hybrid Linear Attention"

## TABLE 1: Unified comparison of linear-time attention mechanisms

| Model | Update rule (S_t) | Read-out (o_t) |
|-------|-------------------|----------------|
| HGRN | h_t = α_t ⊙ h_{t-1} + (1-α_t) ⊙ v_t | o_t = h_t ⊙ q_t |
| Hawk (RG-LRU) | h_t = r_t h_{t-1} + i_t ⊙ x_t | o_t = h_t ⊙ q_t |
| RetNet/Lightning | S_t = γ S_{t-1} + v_t k_t^T | o_t = S_t q_t |
| GLA | S_t = S_{t-1} ⊙ (1 α_t^T) + v_t k_t^T | o_t = S_t q_t |
| Mamba-2 | S_t = γ_t S_{t-1} + v_t k_t^T | o_t = S_t q_t |
| RWKV-6 | S_t = S_{t-1} Diag(α_t) + v_t k_t^T | o_t = (S_{t-1} + (d⊙v_t)k_t^T)q_t |
| HGRN-2/MetaLA | S_t = S_{t-1} Diag(α_t) + v_t(1-α_t)^T | o_t = S_t q_t |
| DeltaNet | S_t = S_{t-1}(I - β_t k_t k_t^T) + β_t v_t k_t^T | o_t = S_t q_t |
| Gated DeltaNet | S_t = α_t S_{t-1}(I - β_t k_t k_t^T) + β_t v_t k_t^T | o_t = S_t q_t |

---

## TABLE 2: 340M model language modeling performance

| Model | ARC-c | ARC-e | HellaSwag | LAMBADA | OBQA | PIQA | Average |
|-------|-------|-------|-----------|---------|------|------|---------|
| DeltaNet 6-1 | 0.299 | 0.594 | 0.410 | 0.334 | 0.334 | 0.675 | 0.441 |
| GatedDeltaNet pure | 0.291 | 0.602 | 0.415 | 0.348 | 0.338 | 0.661 | 0.442 |
| GLA 6-1 | 0.287 | 0.588 | 0.421 | 0.343 | 0.334 | 0.671 | 0.441 |
| HGRN 6-1 | 0.298 | 0.601 | 0.433 | 0.339 | 0.340 | 0.678 | 0.448 |
| HGRN2 6-1 | 0.300 | 0.617 | 0.436 | 0.347 | 0.346 | 0.690 | 0.456 |
| RetNet 24-1 | 0.287 | 0.574 | 0.411 | 0.309 | 0.364 | 0.672 | 0.436 |
| Transformers | 0.276 | 0.612 | 0.424 | 0.353 | 0.330 | 0.670 | 0.444 |

---

## TABLE 3: 1.3B parameter language modeling performance

| Model | ARC-c | ARC-e | HellaSwag | LAMBADA | OBQA | PIQA | Average |
|-------|-------|-------|-----------|---------|------|------|---------|
| DeltaNet 6-1 | 0.403 | 0.730 | 0.586 | 0.475 | 0.384 | 0.741 | 0.553 |
| GatedDeltaNet 24-1 | 0.410 | 0.733 | 0.598 | 0.502 | 0.406 | 0.741 | 0.565 |
| GLA 3-1 | 0.398 | 0.721 | 0.586 | 0.
…[truncated 4845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T13:16:53.551169+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T13:16:53.551293+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T13:16:53.551423+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "report.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "report.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T13:16:53.551563+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **eval_340m_retnet_hgrn2** (success): 340M RetNet and HGRN2 models will show the same architecture-dependent attention effect observed at 1.3B scale: HGRN2 benefits from attention while RetNet shows minimal benefit, with task-dependent equalizer effect on LAMBADA\\n- **hgrn2_eval_h3_1** (success): HGRN2 hybrid-3-1 (highest attention ratio) will show less degradation on composition-heavy benchmarks compared to pure linear models, following the attention-ratio degradation pattern observed in GDN and RetNet families\\n- **hgrn2_eval_1_3b_all** (killed): —\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 3\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-48145: 无 GPU 信息\\n\\n## 告警\\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\\n\", \"total_chars\": 793, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T13:16:53.551716+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T13:16:53.551910+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/paper_framing.md\", \"content\": \"# Paper Framing — entrainment_gated_ft\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (via ARR)\\n- Backup: EMNLP 2026 Findings\\n- Deadline: ARR June 2026 cycle (submission ~June 15)\\n\\n## Paper Type\\nEmpirical analysis paper (not method paper)\\n\\n## Core Claims (3 条)\\n\\n### Claim 1: Task-Specific Equalizer Effect\\nAdding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence whose strength scales with task retrieval demand—strongest on LAMBADA (ρ=-1.0, cross-arch std drops 79%), suggestive on ARC-Easy (ρ=-0.7, underpowered), absent on reasoning-heavy tasks (HellaSwag, WinoGrande). This continuous relationship between retrieval demand and convergence strength is a key finding, not a limitation of single-task significance.\\n\\n### Claim 2: Scale-Dependent Convergence\\nThe convergence effect is scale-dependent: monotonically complete at 1.3B parameters (Spearman ρ=-1.0 for cross-arch std vs attention ratio, exact permutation p=0.0083) but only partial at 340M with a non-monotonic rebound at high attention ratios. Note: only two scale points available (Wang et al. do not provide 7B models); this is a binary contrast, not a multi-point trend. Paper must frame honestly as \\\"scale matters\\\" without implying extrapolation.\\n\\n### Claim 3: Architecture-Specific Mechanism (Equalizer Paradox)\\nDespite aggregate convergence, attention acts on almost entirely different sample subsets per architecture (pairwise Jaccard < 0.10). GDN and RetNet are hurt (net negative on LAMBADA), HGRN2 is helped (net positive), with symmetric effect magnitudes—convergence emerges from complementary, not redundant, mechanisms.\\n\\n## Story Spine\\n\\n### Problem\\nHybrid architectures mixing linear recurrence with full attention are be
…[truncated 6415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T13:16:53.552088+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T13:16:53.552213+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T13:16:53.552329+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -la /root/entrainment_gated_ft/analysis/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls -la /root/entrainment_gated_ft/analysis/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T13:16:53.552450+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T13:16:53.552610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -la /root/entrainment_gated_ft/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls -la /root/entrainment_gated_ft/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T13:16:53.552807+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 2600\\ndrwxr-xr-x  2 root root   4096 May 19 21:09 .\\ndrwxr-xr-x 11 root root   4096 May 19 11:45 ..\\n-rw-r--r--  1 root root  23299 May 19 14:38 convergence_analysis.pdf\\n-rw-r--r--  1 root root 131061 May 19 14:38 convergence_analysis.png\\n-rw-r--r--  1 root root   4818 May 19 14:38 convergence_analysis.py\\n-rw-r--r--  1 root root  34344 May 19 13:37 cross_scale_convergence.pdf\\n-rw-r--r--  1 root root 305368 May 19 13:37 cross_scale_convergence.png\\n-rw-r--r--  1 root root  12937 May 19 13:37 cross_scale_convergence.py\\n-rw-r--r--  1 root root   9219 May 19 13:37 cross_scale_summary.csv\\n-rw-r--r--  1 root root 218267 May 19 04:59 lambada_attention_analysis.png\\n-rw-r--r--  1 root root 181908 May 19 04:59 lambada_crossmodel_scatter.png\\n-rw-r--r--  1 root root  37465 May 19 14:54 lambada_matched_comparison.pdf\\n-rw-r--r--  1 root root 182961 May 19 14:54 lambada_matched_comparison.png\\n-rw-r--r--  1 root root  13787 May 19 14:54 lambada_matched_comparison.py\\n-rw-r--r--  1 root root  13140 May 19 14:53 lambada_matched_comparison.py.bak\\n-rw-r--r--  1 root root 330031 May 19 14:54 lambada_matched_per_example.csv\\n-rw-r--r--  1 root root 330886 May 19 07:40 lambada_per_example.csv\\n-rw-r--r--  1 root root  25634 May 19 14:55 lambada_robustness_h6.pdf\\n-rw-r--r--  1 root root 164277 May 19 14:55 lambada_robustness_h6.png\\n-rw-r--r--  1 root root  13759 May 19 14:55 lambada_robustness_h6.py\\n-rw-r--r--  1 root root  40698 May 19 14:54 lambada_three_arch_comparison.pdf\\n-rw-r--r--  1 root root 179101 May 19 14:54 lambada_three_arch_comparison.png\\n-rw-r--r--  1 root root  11673 May 19 14:54 lambada_three_arch_comparison.py\\n-rw-r--r--  1 root root   8841 May 19 04:58 logprob_analysis.py\\n-rw-r--r--  1 root root   6527 May 19 04:59 logprob_plots.py\\n-rw-r--r--  1 root root   4413 May 19 21:05 task_specificity_analysis.py\\n-rw-r--r--  1 root root  38016 May 19 21:05 task_specificity_
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T13:16:53.552983+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T13:16:53.553107+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/cross_scale_summary.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/cross_scale_summary.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T13:16:53.553302+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Wang et al. vs Our Analysis: Differentiation\\n\\n## Summary\\n\\nWang et al. (2507.06457) is a **practitioner's architecture selection guide** — it systematically benchmarks 72 hybrid models to answer \\\"which linear attention + what ratio is best.\\\" Our work asks a fundamentally different question: **\\\"why do different architectures become more similar when attention is added, and through what per-example mechanism?\\\"** They observe that rankings change after hybridization; we quantify the convergence, decompose it by task type and scale, and reveal the paradox that aggregate similarity arises from architecture-specific per-example effects.\\n\\n## Detailed Comparison\\n\\n### 1. Cross-Architecture Convergence Quantification\\n\\n**Wang et al.**: They observe that \\\"the relative performance of different architectures changes substantially when linear and full attention mechanisms are combined, making standalone scores unreliable predictors of hybrid performance\\\" (Section 4.1). They also note that \\\"GatedDeltaNet leads in standalone evaluation but becomes comparable with HGRN2 after hybridization\\\" (Section 4.1), and that \\\"language modeling performance remains largely flat across all ratio configurations\\\" with \\\"most architectures cluster around 0.55-0.57 average LM score\\\" (Section 4.2). However, they **never compute any cross-architecture variance metric**. Their Table 4 shows LM performance averaged across scales (range ~0.468-0.494), and Figure 3 shows individual architecture curves, but they do not quantify the *spread* between architectures or how it changes with attention ratio. The word \\\"convergence\\\" appears only once in their paper, in the related work section: \\\"production models at Character.ai and MiniMax that converge on a 6–7:1 ratio\\\" — referring to industry convergence on a ratio choice, not performance convergence.\\n\\n**Our work**: We compute the cross-a
…[truncated 6529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T13:16:53.553454+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/task_specificity_results.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/task_specificity_results.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T13:16:53.553724+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"scale,attn_layers,benchmark,arch_std,arch_range,arch_values,min_std_attn,min_std,reduction_pct,rebound_pct\\n1.3B,0,lambada_acc,0.02404712697705703,0.05880069862216192,\\\"GDN=0.5430,RetNet=0.5166,HGRN2=0.4842\\\",8,0.004942545182713789,-79.44642124013654,\\n1.3B,0,hellaswag_norm,0.011684919531365783,0.02818163712407895,\\\"GDN=0.6080,RetNet=0.5799,HGRN2=0.5983\\\",1,0.008615212910147576,-26.270669754962416,37.324833564804045\\n1.3B,0,winogrande_acc,0.0067074710781278545,0.015785319652723007,\\\"GDN=0.6077,RetNet=0.6038,HGRN2=0.5919\\\",0,0.0067074710781278545,0.0,16.88258408136955\\n1.3B,0,arc_easy_norm,0.010014909257898295,0.023569023569023573,\\\"GDN=0.6418,RetNet=0.6477,HGRN2=0.6654\\\",8,0.001301012695776599,-87.00924129941018,\\n1.3B,0,arc_challenge_norm,0.009577621297202906,0.023037542662115995,\\\"GDN=0.3925,RetNet=0.3771,HGRN2=0.4002\\\",2,0.007673912152009124,-19.87663832302234,72.5694636377475\\n1.3B,0,mmlu_acc,0.009200975872321134,0.02193419740777669,\\\"GDN=0.2606,RetNet=0.2452,HGRN2=0.2387\\\",8,0.004045832460787097,-56.02822443043258,\\n1.3B,1,lambada_acc,0.016238171620323174,0.039394527459732265,\\\"GDN=0.5397,RetNet=0.5152,HGRN2=0.5003\\\",8,0.004942545182713789,-79.44642124013654,\\n1.3B,1,hellaswag_norm,0.008615212910147576,0.02041426010754832,\\\"GDN=0.5970,RetNet=0.5822,HGRN2=0.6026\\\",1,0.008615212910147576,-26.270669754962416,37.324833564804045\\n1.3B,1,winogrande_acc,0.021181496667056418,0.05130228887134969,\\\"GDN=0.6283,RetNet=0.5770,HGRN2=0.6093\\\",0,0.0067074710781278545,0.0,16.88258408136955\\n1.3B,1,arc_easy_norm,0.019452560645897617,0.04587542087542085,\\\"GDN=0.6305,RetNet=0.6423,HGRN2=0.6763\\\",8,0.001301012695776599,-87.00924129941018,\\n1.3B,1,arc_challenge_norm,0.007705470525679222,0.01877133105802048,\\\"GDN=0.3942,RetNet=0.3831,HGRN2=0.4019\\\",2,0.007673912152009124,-19.87663832302234,72.5694636377475\\n1.3B,1,mmlu_acc,0.005255878164789419,0.0118216778236718,\\\"GDN=0.2
…[truncated 6622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T13:16:53.553925+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"benchmark,taxonomy_category,ratio,ratio_index,cross_arch_std,spearman_rho,p_value_one_tailed,significant\\nLAMBADA (acc),Retrieval-dependent,pure,0,0.02404712697705703,-0.9999999999999999,0.008333333333333333,True\\nLAMBADA (acc),Retrieval-dependent,h24-1,1,0.016238171620323174,-0.9999999999999999,0.008333333333333333,True\\nLAMBADA (acc),Retrieval-dependent,h12-1,2,0.013595712311665278,-0.9999999999999999,0.008333333333333333,True\\nLAMBADA (acc),Retrieval-dependent,h6-1,3,0.006055084765553574,-0.9999999999999999,0.008333333333333333,True\\nLAMBADA (acc),Retrieval-dependent,h3-1,4,0.004942545182713789,-0.9999999999999999,0.008333333333333333,True\\nHellaSwag (acc_norm),Reasoning-dependent,pure,0,0.011684919531365781,0.3,0.7416666666666667,False\\nHellaSwag (acc_norm),Reasoning-dependent,h24-1,1,0.008615212910147578,0.3,0.7416666666666667,False\\nHellaSwag (acc_norm),Reasoning-dependent,h12-1,2,0.00946859081425128,0.3,0.7416666666666667,False\\nHellaSwag (acc_norm),Reasoning-dependent,h6-1,3,0.009201244143823003,0.3,0.7416666666666667,False\\nHellaSwag (acc_norm),Reasoning-dependent,h3-1,4,0.01183082679011367,0.3,0.7416666666666667,False\\nARC-Challenge (acc_norm),Reasoning-dependent,pure,0,0.009577621297202906,0.6,0.8833333333333333,False\\nARC-Challenge (acc_norm),Reasoning-dependent,h24-1,1,0.007705470525679222,0.6,0.8833333333333333,False\\nARC-Challenge (acc_norm),Reasoning-dependent,h12-1,2,0.007673912152009124,0.6,0.8833333333333333,False\\nARC-Challenge (acc_norm),Reasoning-dependent,h6-1,3,0.012565825958119756,0.6,0.8833333333333333,False\\nARC-Challenge (acc_norm),Reasoning-dependent,h3-1,4,0.013242829040754071,0.6,0.8833333333333333,False\\nWinogrande (acc),Reasoning-dependent,pure,0,0.0067074710781278545,0.09999999999999999,0.6083333333333333,False\\nWinogrande (acc),Reasoning-dependent,h24-1,1,0.021181496667056418,0.09999999999999999,0.6083333333333333,False\\nWinogrande (acc),Reasoning-dependent,h
…[truncated 1207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T13:16:53.554127+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T13:16:53.554260+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"95 /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T13:16:53.554381+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "tail -60 /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "tail -60 /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T13:16:53.554567+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n### 4. Task-Specificity Characterization\\n\\n**Wang et al.**: They make a coarse-grained task distinction: \\\"Language modeling remains stable across ratios\\\" vs. \\\"recall significantly improves with increased full attention layers\\\" (Abstract; Section 4.2). Their RULER subtask analysis (Table 6) shows that \\\"Single-Key, Multi-key, and QA sub tasks are noticeably affected by a changing ratio... Common Word Extraction and Frequent Word Extraction does not seem to correlate with the hybrid ratio\\\" (Section 4.2). This is a **ratio-sensitivity** analysis (which tasks benefit from more attention), not a **convergence-pattern** analysis (do architectures become more similar on different tasks at different rates).\\n\\n**Our work**: We classify benchmarks by task type and show that the equalizer effect is task-dependent:\\n- **Retrieval-dependent tasks** (LAMBADA, HellaSwag, ARC-Easy, Winogrande): average Spearman ρ = -0.94, strong convergence\\n- **Reasoning-dependent tasks** (PIQA, ARC-Challenge): average Spearman ρ = -0.55, weak/non-significant convergence\\n- The dichotomy is interpretable: attention's context integration compensates architecture-specific retrieval weaknesses but cannot bridge reasoning capacity gaps that originate in training dynamics rather than architectural limitations.\\n\\n**Gap**: Wang et al. ask \\\"which tasks benefit more from attention?\\\" (answer: recall tasks). We ask \\\"on which tasks does attention make architectures more similar?\\\" (answer: retrieval-grounded tasks, not reasoning tasks). These are orthogonal questions. Their observation that LM performance is \\\"flat across ratios\\\" does not distinguish whether the *spread* between architectures changes — all architectures could shift equally (no convergence) or differentially (convergence). We show the latter occurs selectively.\\n\\n## Key Wang et al. Quotes\\n\\n### On Rankings Changing After Hybridization\
…[truncated 5002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T13:16:53.554781+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -55 /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -55 /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T13:16:53.554983+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Wang et al. vs Our Analysis: Differentiation\\n\\n## Summary\\n\\nWang et al. (2507.06457) is a **practitioner's architecture selection guide** — it systematically benchmarks 72 hybrid models to answer \\\"which linear attention + what ratio is best.\\\" Our work asks a fundamentally different question: **\\\"why do different architectures become more similar when attention is added, and through what per-example mechanism?\\\"** They observe that rankings change after hybridization; we quantify the convergence, decompose it by task type and scale, and reveal the paradox that aggregate similarity arises from architecture-specific per-example effects.\\n\\n## Detailed Comparison\\n\\n### 1. Cross-Architecture Convergence Quantification\\n\\n**Wang et al.**: They observe that \\\"the relative performance of different architectures changes substantially when linear and full attention mechanisms are combined, making standalone scores unreliable predictors of hybrid performance\\\" (Section 4.1). They also note that \\\"GatedDeltaNet leads in standalone evaluation but becomes comparable with HGRN2 after hybridization\\\" (Section 4.1), and that \\\"language modeling performance remains largely flat across all ratio configurations\\\" with \\\"most architectures cluster around 0.55-0.57 average LM score\\\" (Section 4.2). However, they **never compute any cross-architecture variance metric**. Their Table 4 shows LM performance averaged across scales (range ~0.468-0.494), and Figure 3 shows individual architecture curves, but they do not quantify the *spread* between architectures or how it changes with attention ratio. The word \\\"convergence\\\" appears only once in their paper, in the related work section: \\\"production models at Character.ai and MiniMax that converge on a 6–7:1 ratio\\\" — referring to industry convergence on a ratio choice, not performance convergence.\\n\\n**Our work**: We compute the cross-a
…[truncated 6452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T13:16:53.555232+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "cat > /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md << 'ENDOFFILE'\n# Wang et al. (2025) vs Our Work: Differentiation Analysis\n\n## Paper Information\n\n- **Title**: A Systematic Analysis of Hybrid Linear Attention\n- **Authors**: Dustin Wang, Rui-Jie Zhu, Steven Abreu, Yong Shan, Taylor Kergan, Yuqi Pan, Yuhong Chou, Zheng Li, Ge Zhang, Wenhao Huang, Jason Eshraghian\n- **arXiv**: 2507.06457\n- **Date**: July 8, 2025\n- **Scope**: Trains 72 models (6 linear attention variants × 5 hybridization ratios × 2 scales) to answer \"which linear attention + what ratio is best for hybrid architectures\"\n\n## Summary\n\nWang et al. is a **practitioner's architecture selection guide** — it systematically benchmarks 72 hybrid models to answer \"which linear attention + what ratio is best.\" Our work asks a fundamentally different question: **\"why do different architectures become more similar when attention is added, and through what per-example mechanism?\"** They observe that rankings change after hybridization; we quantify the convergence, decompose it by task type and scale, and reveal the paradox that aggregate similarity arises from architecture-specific per-example effects.\n\n---\n\n## Verbatim Extractions from Wang et al.\n\n### On Rankings Changing After Hybridization\n- **Section 4.1**: \"The relative performance of different architectures changes substantially when linear and full attention mechanisms are combined, making standalone scores unreliable predictors of hybrid performance.\"\n- **Section 4.1**: \"GatedDeltaNet achieves the highest standalone accuracy. However, when hybridized, HGRN2 at a 6:1 linear-to-full attention ratio outperforms it, exceeding both the Transformer baseline and the standalone leader by 1.2 percentage points.\"\n- **Section 4.1** (1.3B): \"The same pattern emerges at 1.3B parameters: GatedDeltaNet leads in standalone evaluation but becomes comparable with HGRN2 after hybridization.\"\n- **Section 4.5**: \"Hybrid quality cannot be inferred from standalone performance.\"\n\n### On Performance Stability Across Ratios\n- **Section 4.2**: \"Language modeling performance remains largely flat across all ratio configurations. Most architectures cluster around 0.55-0.57 average LM score, with minimal variation.\"\n- **Section 4.2**: \"All architectures show a clear upward trend as the proportion of full-attention layers increases [for recall].\"\n- **Section 4.2**: \"Most architectures approach or exceed this baseline at the 3:1 ratio, with some like DeltaNet and Gated-DeltaNet achieving their peak recall performance at this configuration.\"\n- **Section 4.2**: \"recall capability benefits substantially from increased full-attention allocation, unlike language modeling performance.\"\n\n### On Perplexity Plateau\n- **Section 2 (Related Work)**: \"Empirically, long-context quality rises steeply once a few full-attention blocks or heads are present, after which perplexity plateaus; thus the linear:full ratio primarily controls recall.\"\n\n### On Architectural Mechanisms\n- **Section 4.3**: \"Selective gating prevents catastrophic overwriting... Architectures that expose their hidden state to a learned, token-wise gate—GatedDeltaNet and HGRN-2—consistently perform best in recall once hybridised, surpassing the Transformer baseline by 2–5 percentage points.\"\n- **Section 4.3**: \"Hierarchical recurrence supplies multi-timescale context... this hierarchy doubles recall.\"\n- **Section 4.3**: \"Controlled forgetting curbs state crowding.\"\n- **Section 4.3**: \"Architectures lacking either gated or delta-style forgetting never reach Transformer-level recall, regardless of ratio.\"\n\n### On Task Differences\n- **Section 4.2**: \"Single-Key, Multi-key, and QA sub tasks are noticeably affected by a changing ratio... Common Word Extraction and Frequent Word Extraction does not seem to correlate with the hybrid ratio.\"\n- **Section 4.5**: \"Recall—not perplexity—determines the optimal linear:full mix.\" (with \"24:1 to 3:1 shift nearly doubling RULER recall while shifting language-model loss by less than 1%\")\n\n### On Scale\n- **Section 5 (Limitations)**: \"The analysis is confined to models up to 1.3B parameters, a 2,048-token context window, and block-wise mixing ratios. Whether the observed trade-offs persist at the 10B+ scale... remains open.\"\n\n### On Diminishing Returns\n- **Section 1 (Introduction)**: \"simply increasing the state size of linear attention models yields diminishing returns.\"\n\n### Convergence (Only Non-Performance Usage)\n- **Section 2 (Related Work)**: \"production models at Character.ai and MiniMax that converge on a 6–7:1 ratio\" — refers to industry convergence on ratio choice, **not** performance convergence between architectures.\n\n### Practical Recommendations\n- **Section 4.5**: \"Employ a gated, hierarchical backbone (e.g., HGRN-2 or GatedDeltaNet) with one soft-max attention layer for every 3–6 linear layers.\"\n- **Section 5**: \"when equipped with gating, hierarchical recurrence, and controlled forgetting, linear backbones can match Transformer-level recall at a fraction of the KV-cache cost; a 3:1–6:1 (linear:full) ratio provides a practical balance between memory and quality.\"\n\n---\n\n## Wang et al. Key Numerical Results\n\n### Table 2 — 340M LM Performance (selected)\n\n| Model | ARC-c | ARC-e | HellaSwag | LAMBADA | OBQA | PIQA | Avg |\n|-------|-------|-------|-----------|---------|------|------|-----|\n| GatedDeltaNet pure | 0.291 | 0.602 | 0.415 | 0.348 | 0.338 | 0.661 | 0.442 |\n| HGRN2 6:1 | 0.300 | 0.617 | 0.436 | 0.347 | 0.346 | 0.690 | 0.456 |\n| RetNet 24:1 | 0.287 | 0.574 | 0.411 | 0.309 | 0.364 | 0.672 | 0.436 |\n| Transformer | 0.276 | 0.612 | 0.424 | 0.353 | 0.330 | 0.670 | 0.444 |\n\n### Table 3 — 1.3B LM Performance (selected)\n\n| Model | ARC-c | ARC-e | HellaSwag | LAMBADA | OBQA | PIQA | Avg |\n|-------|-------|-------|-----------|---------|------|------|-----|\n| GatedDeltaNet 24:1 | 0.410 | 0.733 | 0.598 | 0.502 | 0.406 | 0.741 | 0.565 |\n| HGRN2 6:1 | 0.404 | 0.729 | 0.604 | 0.500 | 0.420 | 0.733 | 0.565 |\n| RetNet 6:1 | 0.380 | 0.718 | 0.584 | 0.475 | 0.400 | 0.727 | 0.547 |\n| Transformer | 0.395 | 0.704 | 0.589 | 0.474 | 0.400 | 0.729 | 0.548 |\n\n### Table 4 — LM Performance Averaged Across Scales by Ratio\n\n| Ratio | DeltaNet | GDN | GLA | HGRN | HGRN2 | RetNet | Avg |\n|-------|----------|-----|-----|------|-------|--------|-----|\n| 24:1 | 0.472 | 0.468 | 0.470 | 0.488 | 0.488 | 0.472 | 0.476 |\n| 12:1 | 0.476 | 0.478 | 0.474 | 0.482 | 0.488 | 0.472 | 0.478 |\n| 6:1 | 0.478 | 0.481 | 0.471 | 0.486 | 0.494 | 0.472 | 0.480 |\n| 3:1 | 0.475 | 0.478 | 0.478 | 0.483 | 0.489 | 0.468 | 0.479 |\n| pure | 0.472 | 0.487 | 0.459 | 0.459 | 0.486 | 0.471 | 0.472 |\n\nNote: Range across architectures at any given ratio is ~0.02-0.03. They report this but **never compute cross-architecture variance or track its change with ratio**.\n\n### Statistical Methods Used\n\n**None.** Wang et al. report point estimates only — no p-values, no confidence intervals, no significance tests, no error bars. All evaluation is zero-shot without task-specific fine-tuning.\n\n### Analysis Granularity\n\n**Aggregate metrics only.** No per-example analysis, no error analysis, no sample-level decomposition.\n\n---\n\n## 4-Point Differentiation Table (Detailed)\n\n### 1. Cross-Architecture Convergence Quantification\n\n**Wang et al.**: Observe qualitatively that \"the relative performance of different architectures changes substantially when linear and full attention mechanisms are combined\" (Section 4.1) and that LM performance \"remains largely flat\" with architectures clustering around 0.55–0.57 (Section 4.2). Their Table 4 shows LM performance averaged across both scales (range ~0.468–0.494 across architectures at any ratio), and Figure 3 shows individual architecture curves. However, they **never compute any cross-architecture variance metric**. They do not quantify the *spread* between architectures or how it changes with attention ratio. The word \"convergence\" appears only once, in the Related Work section referring to industry adoption of the 6–7:1 ratio, not performance convergence.\n\n**Our work**: We compute cross-architecture standard deviation at each attention ratio across all benchmarks, then test monotonic decrease with Spearman rank correlation + exact permutation test (n=5 ratio levels). For LAMBADA at 1.3B: ρ = −1.0, p = 0.0083; std decreases monotonically from 0.024 (pure) to 0.005 (h3-1), a 79% reduction. ARC-Easy and MMLU show suggestive convergence (ρ = −0.7, p = 0.117 each — underpowered at n=5). HellaSwag, ARC-Challenge, and Winogrande show no convergence (ρ ≥ 0.1).\n\n**Gap**: Wang et al. make a qualitative observation (\"rankings change\"). We provide a **quantitative convergence framework** with Spearman correlation, exact permutation p-values, and effect sizes. This transforms an anecdotal observation into a testable, reproducible phenomenon. Their closest claim — that architectures \"cluster\" — describes static similarity at one point, not the *dynamic process* of convergence across ratio levels.\n\n---\n\n### 2. Scale-Dependent Analysis\n\n**Wang et al.**: Train at 340M (20B tokens) and 1.3B (100B tokens). Their cross-scale comparison is limited to confirming the same ranking inversion: \"The same pattern emerges at 1.3B parameters: GatedDeltaNet leads in standalone evaluation but becomes comparable with HGRN2 after hybridization\" (Section 4.1). They **never compare convergence strength across scales**. Table 4 averages performance across both scales, collapsing scale information. Limitations section acknowledges: \"Whether the observed trade-offs persist at the 10B+ scale... remains open\" (Section 5).\n\n**Our work**: We directly compare equalizer effect intensity across scales on LAMBADA:\n- **1.3B**: std drops monotonically 0.024 → 0.005 (79% reduction), ρ = −1.0, p = 0.0083\n- **340M**: std drops 0.025 → 0.011 at attn=4 (56% reduction) but **rebounds** to 0.015 at attn=8 (non-monotonic)\n- The 1.3B convergence is approximately 1.4× stronger than 340M, and critically, the non-monotonic rebound at 340M (capacity bottleneck at high attention ratio) disappears at 1.3B\n\n**Gap**: Wang et al. make a binary statement (\"same pattern, both scales\"). We quantify **how much stronger** the convergence is at 1.3B, identify a **scale-dependent qualitative difference** (non-monotonic rebound at 340M vs monotonic convergence at 1.3B), and propose a mechanistic explanation (capacity bottleneck — at 340M, the model lacks capacity to simultaneously support attention overhead and maintain architecture-specific strengths).\n\n---\n\n### 3. Per-Example Mechanism\n\n**Wang et al.**: All analysis is at the aggregate benchmark level. No per-example, per-sample, or instance-level analysis appears anywhere in the paper. Their Section 4.3 (Architectural Determinants of Hybrid Effectiveness) analyzes *why certain architectures benefit more from hybridization* at the architecture level (selective gating, hierarchical recurrence, controlled forgetting), but never at the individual sample level.\n\n**Our work**: We extract per-example accuracy changes (via lm-eval --log_samples) and compute:\n- **Helped/hurt sample sets** per architecture (which specific examples improve/degrade when attention is added)\n- **Pairwise Jaccard overlap** between architectures' helped sets: ~0.04–0.07 for retrieval tasks (near-zero overlap)\n- **Net effect asymmetry**: GDN shows net negative effect on LAMBADA (more samples hurt than helped) while HGRN2 shows net positive on *different* samples\n- **Feature characterization**: helped/hurt samples distinguished by target token frequency, context length, last-sentence perplexity, with architecture-specific profiles\n\n**Gap**: This is our most distinctive contribution. Wang et al. see the aggregate picture (\"HGRN2 improves with attention\"). We reveal that beneath aggregate convergence, **each architecture is helped and hurt on almost entirely different examples** (Jaccard ~0.04–0.07). This is the \"equalizer paradox\": architectures look more similar in aggregate precisely because attention compensates different weaknesses on different samples. This level of analysis is completely absent from Wang et al.\n\n---\n\n### 4. Task-Specificity Characterization\n\n**Wang et al.**: Make a coarse-grained distinction: LM performance \"remains largely flat across ratios\" vs. recall \"significantly improves with increased full attention layers\" (Section 4.2). Their RULER subtask analysis (Table 6) shows \"Single-Key, Multi-key, and QA sub tasks are noticeably affected by a changing ratio... Common Word Extraction and Frequent Word Extraction does not seem to correlate with the hybrid ratio\" (Section 4.2). This is a **ratio-sensitivity** analysis (which tasks benefit from more attention), not a **convergence-pattern** analysis (do architectures become more similar on different tasks at different rates).\n\n**Our work**: We measure convergence strength (Spearman ρ of cross-arch std vs attention ratio) per benchmark:\n- **LAMBADA** (retrieval-dependent): ρ = −1.0, p = 0.0083 — strong, monotonic convergence\n- **ARC-Easy, MMLU** (mixed): ρ = −0.7, p = 0.117 — suggestive convergence, underpowered\n- **HellaSwag** (reasoning): ρ = +0.3, p = 0.742 — no convergence\n- **ARC-Challenge** (reasoning): ρ = +0.6, p = 0.883 — no convergence\n- **Winogrande** (mixed): ρ = +0.1, p = 0.608 — no convergence\n\nThis yields a continuous spectrum: tasks with higher retrieval demand show stronger convergence, consistent with the interpretation that attention compensates architecture-specific retrieval weaknesses but cannot bridge reasoning capacity gaps.\n\n**Gap**: Wang et al. ask \"which tasks benefit more from attention?\" (answer: recall tasks). We ask \"on which tasks does attention make architectures more *similar*?\" (answer: retrieval-grounded tasks, not reasoning tasks). These are orthogonal questions. Their \"flat across ratios\" observation does not distinguish whether the *spread between architectures* changes — all architectures could shift equally (no convergence) or differentially (convergence). We show the latter occurs selectively by task type.\n\n---\n\n## Differentiation Summary Table\n\n| Dimension | Wang et al. | Ours | Status |\n|---|---|---|---|\n| **Convergence quantification** | Qualitative (\"rankings change\", architectures \"cluster\") | Spearman ρ + exact permutation test across 5 ratios × 3 architectures; LAMBADA ρ=−1.0 (p=0.008), std 0.024→0.005 | **Fully novel** |\n| **Scale dependency** | Binary (\"same pattern both scales\"); Table 4 averages across scales | 1.3B: 79% reduction (monotonic); 340M: 56% (non-monotonic rebound); qualitative scale-dependent difference | **Fully novel** |\n| **Per-example mechanism** | Not performed (aggregate metrics only, zero per-sample analysis) | Jaccard ~0.04–0.07, architecture-specific helped/hurt profiles, net effect asymmetry (GDN net−, HGRN2 net+) | **Fully novel** |\n| **Task-specificity of convergence** | Ratio-sensitivity by task type (\"recall benefits from attention\") | Convergence-strength by task type: retrieval ρ=−1.0 vs reasoning ρ≥+0.1 (continuous spectrum) | **Fully novel** |\n| **Phenomenon framed** | \"Standalone ≠ hybrid\" (practical observation) | \"Equalizer paradox\" (aggregate convergence via per-example divergence — a mechanistic finding) | **Fully novel** |\n\n---\n\n## Conclusion\n\nAll four differentiation dimensions are **fully novel** — none are incremental extensions of Wang et al.'s analysis. The relationship is complementary:\n\n1. **Wang et al. provides infrastructure**: 72 controlled models, systematic benchmarking, architecture taxonomy. They answer \"what happens\" — which architectures work best in hybrid configurations and at what ratio.\n2. **We provide analysis**: convergence quantification, per-example decomposition, scale-dependent characterization, task-type spectrum. We answer \"why it happens and through what mechanism\" — the equalizer effect and its paradox.\n\nWang et al.'s closest observation to our work — that \"rankings change\" and architectures become \"comparable\" after hybridization — is made in passing as a factual observation supporting their architecture recommendation. They never treat it as a *phenomenon to be explained*. We formalize it as the equalizer effect, quantify it, decompose it, and reveal the paradox beneath it.\n\n**Assessment**: These differences are sufficient to constitute an independent contribution. A reviewer familiar with both papers should see them as complementary: Wang et al. built the model zoo and asked the engineering question; we used their models and asked the science question.\nENDOFFILE",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat > /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md << 'ENDOFFILE'\n# Wang et al. (2025) vs Our Work: Differentiation Analysis\n\n## Paper Information\n\n- **Title**: A Systematic Analysis of Hybrid Linear Attention\n- **Authors**: Dustin Wang, Rui-Jie Zhu, Steven Abreu, Yong Shan, Taylor Kergan, Yuqi Pan, Yuhong Chou, Zheng Li, Ge Zhang, Wenhao Huang, Jason Eshraghian\n- **arXiv**: 2507.06457\n- **Date**: July 8, 2025\n- **Scope**: Trains 72 models (6 linear attention variants × 5 hybridization ratios × 2 scales) to answer \"which linear attention + what ratio is best for hybrid architectures\"\n\n## Summary\n\nWang et al. is a **practitioner's architecture selection guide** — it systematically benchmarks 72 hybrid models to answer \"which linear attention + what ratio is best.\" Our work asks a fundamentally different question: **\"why do different architectures become more similar when attention is added, and through what per-example mechanism?\"** They observe that rankings change after hybridization; we quantify the convergence, decompose it by task type and scale, and reveal the paradox that aggregate similarity arises from architecture-specific per-example effects.\n\n---\n\n## Verbatim Extractions from Wang et al.\n\n### On Rankings Changing After Hybridization\n- **Section 4.1**: \"The relative performance of different architectures changes substantially when linear and full attention mechanisms are combined, making standalone scores unreliable predictors of hybrid performance.\"\n- **Section 4.1**: \"GatedDeltaNet achieves the highest standalone accuracy. However, when hybridized, HGRN2 at a 6:1 linear-to-full attention ratio outperforms it, exceeding both the Transformer baseline and the standalone leader by 1.2 percentage points.\"\n- **Section 4.1** (1.3B): \"The same pattern emerges at 1.3B parameters: GatedDeltaNet leads in standalone evaluation but becomes comparable with HGRN2 after hybridization.\"\n- **Section 4.5**: \"Hybrid quality cannot be inferred from standalone performance.\"\n\n### On Performance Stability Across Ratios\n- **Section 4.2**: \"Language modeling performance remains largely flat across all ratio configurations. Most architectures cluster around 0.55-0.57 average LM score, with minimal variation.\"\n- **Section 4.2**: \"All architectures show a clear upward trend as the proportion of full-attention layers increases [for recall].\"\n- **Section 4.2**: \"Most architectures approach or exceed this baseline at the 3:1 ratio, with some like DeltaNet and Gated-DeltaNet achieving their peak recall performance at this configuration.\"\n- **Section 4.2**: \"recall capability benefits substantially from increased full-attention allocation, unlike language modeling performance.\"\n\n### On Perplexity Plateau\n- **Section 2 (Related Work)**: \"Empirically, long-context quality rises steeply once a few full-attention blocks or heads are present, after which perplexity plateaus; thus the linear:full ratio primarily controls recall.\"\n\n### On Architectural Mechanisms\n- **Section 4.3**: \"Selective gating prevents catastrophic overwriting... Architectures that expose their hidden state to a learned, token-wise gate—GatedDeltaNet and HGRN-2—consistently perform best in recall once hybridised, surpassing the Transformer baseline by 2–5 percentage points.\"\n- **Section 4.3**: \"Hierarchical recurrence supplies multi-timescale context... this hierarchy doubles recall.\"\n- **Section 4.3**: \"Controlled forgetting curbs state crowding.\"\n- **Section 4.3**: \"Architectures lacking either gated or delta-style forgetting never reach Transformer-level recall, regardless of ratio.\"\n\n### On Task Differences\n- **Section 4.2**: \"Single-Key, Multi-key, and QA sub tasks are noticeably affected by a changing ratio... Common Word Extraction and Frequent Word Extraction does not seem to correlate with the hybrid ratio.\"\n- **Section 4.5**: \"Recall—not perplexity—determines the optimal linear:full mix.\" (with \"24:1 to 3:1 shift nearly doubling RULER recall while shifting language-model loss by less than 1%\")\n\n### On Scale\n- **Section 5 (Limitations)**: \"The analysis is confined to models up to 1.3B parameters, a 2,048-token context window, and block-wise mixing ratios. Whether the observed trade-offs persist at the 10B+ scale... remains open.\"\n\n### On Diminishing Returns\n- **Section 1 (Introduction)**: \"simply increasing the state size of linear attention models yields diminishing returns.\"\n\n### Convergence (Only Non-Performance Usage)\n- **Section 2 (Related Work)**: \"production models at Character.ai and MiniMax that converge on a 6–7:1 ratio\" — refers to industry convergence on ratio choice, **not** performance convergence between architectures.\n\n### Practical Recommendations\n- **Section 4.5**: \"Employ a gated, hierarchical backbone (e.g., HGRN-2 or GatedDeltaNet) with one soft-max attention layer for every 3–6 linear layers.\"\n- **Section 5**: \"when equipped with gating, hierarchical recurrence, and controlled forgetting, linear backbones can match Transformer-level recall at a fraction of the KV-cache cost; a 3:1–6:1 (linear:full) ratio provides a practical balance between memory and quality.\"\n\n---\n\n## Wang et al. Key Numerical Results\n\n### Table 2 — 340M LM Performance (selected)\n\n| Model | ARC-c | ARC-e | HellaSwag | LAMBADA | OBQA | PIQA | Avg |\n|-------|-------|-------|-----------|---------|------|------|-----|\n| GatedDeltaNet pure | 0.291 | 0.602 | 0.415 | 0.348 | 0.338 | 0.661 | 0.442 |\n| HGRN2 6:1 | 0.300 | 0.617 | 0.436 | 0.347 | 0.346 | 0.690 | 0.456 |\n| RetNet 24:1 | 0.287 | 0.574 | 0.411 | 0.309 | 0.364 | 0.672 | 0.436 |\n| Transformer | 0.276 | 0.612 | 0.424 | 0.353 | 0.330 | 0.670 | 0.444 |\n\n### Table 3 — 1.3B LM Performance (selected)\n\n| Model | ARC-c | ARC-e | HellaSwag | LAMBADA | OBQA | PIQA | Avg |\n|-------|-------|-------|-----------|---------|------|------|-----|\n| GatedDeltaNet 24:1 | 0.410 | 0.733 | 0.598 | 0.502 | 0.406 | 0.741 | 0.565 |\n| HGRN2 6:1 | 0.404 | 0.729 | 0.604 | 0.500 | 0.420 | 0.733 | 0.565 |\n| RetNet 6:1 | 0.380 | 0.718 | 0.584 | 0.475 | 0.400 | 0.727 | 0.547 |\n| Transformer | 0.395 | 0.704 | 0.589 | 0.474 | 0.400 | 0.729 | 0.548 |\n\n### Table 4 — LM Performance Averaged Across Scales by Ratio\n\n| Ratio | DeltaNet | GDN | GLA | HGRN | HGRN2 | RetNet | Avg |\n|-------|----------|-----|-----|------|-------|--------|-----|\n| 24:1 | 0.472 | 0.468 | 0.470 | 0.488 | 0.488 | 0.472 | 0.476 |\n| 12:1 | 0.476 | 0.478 | 0.474 | 0.482 | 0.488 | 0.472 | 0.478 |\n| 6:1 | 0.478 | 0.481 | 0.471 | 0.486 | 0.494 | 0.472 | 0.480 |\n| 3:1 | 0.475 | 0.478 | 0.478 | 0.483 | 0.489 | 0.468 | 0.479 |\n| pure | 0.472 | 0.487 | 0.459 | 0.459 | 0.486 | 0.471 | 0.472 |\n\nNote: Range across architectures at any given ratio is ~0.02-0.03. They report this but **never compute cross-architecture variance or track its change with ratio**.\n\n### Statistical Methods Used\n\n**None.** Wang et al. report point estimates only — no p-values, no confidence intervals, no significance tests, no error bars. All evaluation is zero-shot without task-specific fine-tuning.\n\n### Analysis Granularity\n\n**Aggregate metrics only.** No per-example analysis, no error analysis, no sample-level decomposition.\n\n---\n\n## 4-Point Differentiation Table (Detailed)\n\n### 1. Cross-Architecture Convergence Quantification\n\n**Wang et al.**: Observe qualitatively that \"the relative performance of different architectures changes substantially when linear and full attention mechanisms are combined\" (Section 4.1) and that LM performance \"remains largely flat\" with architectures clustering around 0.55–0.57 (Section 4.2). Their Table 4 shows LM performance averaged across both scales (range ~0.468–0.494 across architectures at any ratio), and Figure 3 shows individual architecture curves. However, they **never compute any cross-architecture variance metric**. They do not quantify the *spread* between architectures or how it changes with attention ratio. The word \"convergence\" appears only once, in the Related Work section referring to industry adoption of the 6–7:1 ratio, not performance convergence.\n\n**Our work**: We compute cross-architecture standard deviation at each attention ratio across all benchmarks, then test monotonic decrease with Spearman rank correlation + exact permutation test (n=5 ratio levels). For LAMBADA at 1.3B: ρ = −1.0, p = 0.0083; std decreases monotonically from 0.024 (pure) to 0.005 (h3-1), a 79% reduction. ARC-Easy and MMLU show suggestive convergence (ρ = −0.7, p = 0.117 each — underpowered at n=5). HellaSwag, ARC-Challenge, and Winogrande show no convergence (ρ ≥ 0.1).\n\n**Gap**: Wang et al. make a qualitative observation (\"rankings change\"). We provide a **quantitative convergence framework** with Spearman correlation, exact permutation p-values, and effect sizes. This transforms an anecdotal observation into a testable, reproducible phenomenon. Their closest claim — that architectures \"cluster\" — describes static similarity at one point, not the *dynamic process* of convergence across ratio levels.\n\n---\n\n### 2. Scale-Dependent Analysis\n\n**Wang et al.**: Train at 340M (20B tokens) and 1.3B (100B tokens). Their cross-scale comparison is limited to confirming the same ranking inversion: \"The same pattern emerges at 1.3B parameters: GatedDeltaNet leads in standalone evaluation but becomes comparable with HGRN2 after hybridization\" (Section 4.1). They **never compare convergence strength across scales**. Table 4 averages performance across both scales, collapsing scale information. Limitations section acknowledges: \"Whether the observed trade-offs persist at the 10B+ scale... remains open\" (Section 5).\n\n**Our work**: We directly compare equalizer effect intensity across scales on LAMBADA:\n- **1.3B**: std drops monotonically 0.024 → 0.005 (79% reduction), ρ = −1.0, p = 0.0083\n- **340M**: std drops 0.025 → 0.011 at attn=4 (56% reduction) but **rebounds** to 0.015 at attn=8 (non-monotonic)\n- The 1.3B convergence is approximately 1.4× stronger than 340M, and critically, the non-monotonic rebound at 340M (capacity bottleneck at high attention ratio) disappears at 1.3B\n\n**Gap**: Wang et al. make a binary statement (\"same pattern, both scales\"). We quantify **how much stronger** the convergence is at 1.3B, identify a **scale-dependent qualitative difference** (non-monotonic rebound at 340M vs monotonic convergence at 1.3B), and propose a mechanistic explanation (capacity bottleneck — at 340M, the model lacks capacity to simultaneously support attention overhead and maintain architecture-specific strengths).\n\n---\n\n### 3. Per-Example Mechanism\n\n**Wang et al.**: All analysis is at the aggregate benchmark level. No per-example, per-sample, or instance-level analysis appears anywhere in the paper. Their Section 4.3 (Architectural Determinants of Hybrid Effectiveness) analyzes *why certain architectures benefit more from hybridization* at the architecture level (selective gating, hierarchical recurrence, controlled forgetting), but never at the individual sample level.\n\n**Our work**: We extract per-example accuracy changes (via lm-eval --log_samples) and compute:\n- **Helped/hurt sample sets** per architecture (which specific examples improve/degrade when attention is added)\n- **Pairwise Jaccard overlap** between architectures' helped sets: ~0.04–0.07 for retrieval tasks (near-zero overlap)\n- **Net effect asymmetry**: GDN shows net negative effect on LAMBADA (more samples hurt than helped) while HGRN2 shows net positive on *different* samples\n- **Feature characterization**: helped/hurt samples distinguished by target token frequency, context length, last-sentence perplexity, with architecture-specific profiles\n\n**Gap**: This is our most distinctive contribution. Wang et al. see the aggregate picture (\"HGRN2 improves with attention\"). We reveal that beneath aggregate convergence, **each architecture is helped and hurt on almost entirely different examples** (Jaccard ~0.04–0.07). This is the \"equalizer paradox\": architectures look more similar in aggregate precisely because attention compensates different weaknesses on different samples. This level of analysis is completely absent from Wang et al.\n\n---\n\n### 4. Task-Specificity Characterization\n\n**Wang et al.**: Make a coarse-grained distinction: LM performance \"remains largely flat across ratios\" vs. recall \"significantly improves with increased full attention layers\" (Section 4.2). Their RULER subtask analysis (Table 6) shows \"Single-Key, Multi-key, and QA sub tasks are noticeably affected by a changing ratio... Common Word Extraction and Frequent Word Extraction does not seem to correlate with the hybrid ratio\" (Section 4.2). This is a **ratio-sensitivity** analysis (which tasks benefit from more attention), not a **convergence-pattern** analysis (do architectures become more similar on different tasks at different rates).\n\n**Our work**: We measure convergence strength (Spearman ρ of cross-arch std vs attention ratio) per benchmark:\n- **LAMBADA** (retrieval-dependent): ρ = −1.0, p = 0.0083 — strong, monotonic convergence\n- **ARC-Easy, MMLU** (mixed): ρ = −0.7, p = 0.117 — suggestive convergence, underpowered\n- **HellaSwag** (reasoning): ρ = +0.3, p = 0.742 — no convergence\n- **ARC-Challenge** (reasoning): ρ = +0.6, p = 0.883 — no convergence\n- **Winogrande** (mixed): ρ = +0.1, p = 0.608 — no convergence\n\nThis yields a continuous spectrum: tasks with higher retrieval demand show stronger convergence, consistent with the interpretation that attention compensates architecture-specific retrieval weaknesses but cannot bridge reasoning capacity gaps.\n\n**Gap**: Wang et al. ask \"which tasks benefit more from attention?\" (answer: recall tasks). We ask \"on which tasks does attention make architectures more *similar*?\" (answer: retrieval-grounded tasks, not reasoning tasks). These are orthogonal questions. Their \"flat across ratios\" observation does not distinguish whether the *spread between architectures* changes — all architectures could shift equally (no convergence) or differentially (convergence). We show the latter occurs selectively by task type.\n\n---\n\n## Differentiation Summary Table\n\n| Dimension | Wang et al. | Ours | Status |\n|---|---|---|---|\n| **Convergence quantification** | Qualitative (\"rankings change\", architectures \"cluster\") | Spearman ρ + exact permutation test across 5 ratios × 3 architectures; LAMBADA ρ=−1.0 (p=0.008), std 0.024→0.005 | **Fully novel** |\n| **Scale dependency** | Binary (\"same pattern both scales\"); Table 4 averages across scales | 1.3B: 79% reduction (monotonic); 340M: 56% (non-monotonic rebound); qualitative scale-dependent difference | **Fully novel** |\n| **Per-example mechanism** | Not performed (aggregate metrics only, zero per-sample analysis) | Jaccard ~0.04–0.07, architecture-specific helped/hurt profiles, net effect asymmetry (GDN net−, HGRN2 net+) | **Fully novel** |\n| **Task-specificity of convergence** | Ratio-sensitivity by task type (\"recall benefits from attention\") | Convergence-strength by task type: retrieval ρ=−1.0 vs reasoning ρ≥+0.1 (continuous spectrum) | **Fully novel** |\n| **Phenomenon framed** | \"Standalone ≠ hybrid\" (practical observation) | \"Equalizer paradox\" (aggregate convergence via per-example divergence — a mechanistic finding) | **Fully novel** |\n\n---\n\n## Conclusion\n\nAll four differentiation dimensions are **fully novel** — none are incremental extensions of Wang et al.'s analysis. The relationship is complementary:\n\n1. **Wang et al. provides infrastructure**: 72 controlled models, systematic benchmarking, architecture taxonomy. They answer \"what happens\" — which architectures work best in hybrid configurations and at what ratio.\n2. **We provide analysis**: convergence quantification, per-example decomposition, scale-dependent characterization, task-type spectrum. We answer \"why it happens and through what mechanism\" — the equalizer effect and its paradox.\n\nWang et al.'s closest observation to our work — that \"rankings change\" and architectures become \"comparable\" after hybridization — is made in passing as a factual observation supporting their architecture recommendation. They never treat it as a *phenomenon to be explained*. We formalize it as the equalizer effect, quantify it, decompose it, and reveal the paradox beneath it.\n\n**Assessment**: These differences are sufficient to constitute an independent contribution. A reviewer familiar with both papers should see them as complementary: Wang et al. built the model zoo and asked the engineering question; we used their models and asked the science question.\nENDOFFILE",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T13:16:53.555582+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T13:16:53.555759+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T13:16:53.555892+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"178 /root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-19T13:16:53.556053+00:00_

已完成。文件写入 `/root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md`（178行）。

与之前版本的关键修正：

1. **新增论文元数据**：标题、作者、日期、arXiv ID
2. **修正数值错误**："4/6 benchmarks significant" → 实际只有 LAMBADA 显著（p=0.008），ARC-Easy/MMLU 仅 suggestive（p=0.117）
3. **修正 340M 数据**：std reduction 从错误的 38% 修正为 56%（0.025→0.011 at attn=4），并标注 rebound 至 0.015
4. **修正 task-specificity 数值**：用 CSV 实际计算值替代之前的估算值（HellaSwag ρ=+0.3, ARC-C ρ=+0.6 — 这些是正相关，即无收敛甚至发散）
5. **新增 Wang et al. 原始表格数据**：Tables 2-4 的关键数值，作为 differentiation 的证据基础
6. **新增 verbatim extractions**：补充了 perplexity plateau、diminishing returns、practical recommendations 等此前遗漏的关键引文

核心结论不变：四个 differentiation 维度均为 **fully novel**，Wang et al. 提供基础设施（72 models），我们提供分析框架（equalizer effect + paradox）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_exp_009_wang_differentiation_20260519T131120"
}
```

</details>

---
