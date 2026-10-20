# research keydiff details

**redundancy compound sparsity 2** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_research_keydiff_details_20260512T172753.jsonl`
- **Structured JSON:** [`2a425841ac58d7f1f445.json`](../../sessions/2a/2a425841ac58d7f1f445.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-12T17:30:08.854212+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T17:30:08.854596+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T17:30:08.854774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KeyDiff KV cache eviction centroid arxiv 2504.15364"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KeyDiff KV cache eviction centroid arxiv 2504.15364"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T17:30:08.854906+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KeyDiff KV cache compression paper 2025 experiments models datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KeyDiff KV cache compression paper 2025 experiments models datasets"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-12T17:30:08.855063+00:00_

Web search results for query: "KeyDiff KV cache eviction centroid arxiv 2504.15364"

Links: [{"title":"[2504.15364] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/abs/2504.15364"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/html/2504.15364v1"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments | alphaXiv","url":"https://www.alphaxiv.org/abs/2504.15364"},{"title":"(PDF) KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://www.researchgate.net/publication/391020426_KeDiff_Key_Similarity-Based_KV_Cache_Eviction_for_Long-Context_LLM_Inference_in_Resource-Constrained_Environments"},{"title":"Paper page - KeDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://huggingface.co/papers/2504.15364"},{"title":"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://arxiv.org/html/2509.17396v1"},{"title":"AI Papers on X: \"KeDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments. https://t.co/PpPoCzf8LI\" / X","url":"https://x.com/SciFi/status/1915009674882998569"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250415364P/abstract"},{"title":"KeDiff: Key Similarity-Based KV Cache Eviction for Long- ...","url":"https://www.alphaxiv.org/hi/overview/2504.15364v1"}]

I found the paper! Here's information about KeyDiff (arXiv 2504.
…[truncated 1463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T17:30:08.855253+00:00_

Web search results for query: "KeyDiff KV cache compression paper 2025 experiments models datasets"

Links: [{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"RETHINKING KEY-VALUE CACHE COMPRESSION TECHNIQUES FOR LARGE","url":"https://arxiv.org/pdf/2503.24000"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/html/2504.15364v1"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"A Systematic Exploration of KV Cache Compression ...","url":"https://arxiv.org/pdf/2503.11816"},{"title":"[2503.11816] Key, Value, Compress: A Systematic Exploration of KV Cache Compression Techniques","url":"https://arxiv.org/abs/2503.11816"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://proceedings.neurips.cc/paper_files/paper/2025/hash/57e0358aed314784cad14a26e1eba642-Abstract-Conference.html"}]

Based on the search results, I found information about the KeyDiff paper on KV cache compression. Here's what I found:

## KeyDiff Paper Overview

KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments, authored by Junyoung Park, Dalton Jones, Matthew J Morse, Raghavv Goel, Mingu Lee, and Chris Lott, was published at NeurIPS 2025.

## Methodology

KeyDiff proposes an eviction method that evi
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T17:30:08.855481+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2504.15364v1",
  "prompt": "Extract ALL experimental details from this paper, specifically:\n\n1. MODELS: exact model names and sizes used in experiments\n2. DATASETS: all evaluation benchmarks/datasets used, list every single one\n3. KV CACHE BUDGETS: all budget sizes tested (e.g., 2K, 4K, 6K, 8K) and what percentage of full cache they represent\n4. The \"<0.04% loss\" claim: what metric is this? PPL, accuracy, or something else? On which specific model, dataset, and budget?\n5. CENTROID/ANCHOR computation: how exactly is the anchor key computed? Is it an exact mean of all keys? Running mean? What is the computational complexity?\n6. BASELINE COMPARISONS: extract all comparison tables with H2O, StreamingLLM, SnapKV, TOVA etc. Include exact numbers.\n7. Any ablation studies or additional analysis\n\nPlease be as detailed and precise as possible, including exact numbers from tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2504.15364v1",
    "prompt": "Extract ALL experimental details from this paper, specifically:\n\n1. MODELS: exact model names and sizes used in experiments\n2. DATASETS: all evaluation benchmarks/datasets used, list every single one\n3. KV CACHE BUDGETS: all budget sizes tested (e.g., 2K, 4K, 6K, 8K) and what percentage of full cache they represent\n4. The \"<0.04% loss\" claim: what metric is this? PPL, accuracy, or something else? On which specific model, dataset, and budget?\n5. CENTROID/ANCHOR computation: how exactly is the anchor key computed? Is it an exact mean of all keys? Running mean? What is the computational complexity?\n6. BASELINE COMPARISONS: extract all comparison tables with H2O, StreamingLLM, SnapKV, TOVA etc. Include exact numbers.\n7. Any ablation studies or additional analysis\n\nPlease be as detailed and precise as possible, including exact numbers from tables."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-12T17:30:08.855665+00:00_

# KeyDiff Experimental Details Extraction

## 1. MODELS TESTED

- Llama 3.1-8B-Instruct
- Llama 3.2-3B-Instruct
- Qwen 2.5-3B-Instruct
- Qwen 2.5-7B-Instruct

## 2. DATASETS/BENCHMARKS

**LongBench (English subset):**
Single Doc QA (NarrativeQA, Qasper), Multi Doc QA (MF-en, HotpotQA, 2WikiMQA, Musique), Summarization (GovReport, QMSum, MultiNews), Fewshot Learning (TREC, TriviaQA, SAMSum), Synthetic (PCount, PR-en), Code (Lcc, RB-P)

**Additional benchmark:**
Needle In a Haystack test

## 3. KV CACHE BUDGETS TESTED

- 2K tokens (2048)
- 4K tokens (4096)
- 6K tokens (6144) – represents ~33% compression
- 8K tokens (8192) – represents ~23% compression

## 4. THE "<0.04% LOSS" CLAIM

"KeyDiff shows significant a improvement...achieving near full-context model performance even with the smallest budget. We observed similar trends in the full LongBench task suite." Specifically: **0.04% accuracy drop on LongBench with 8K cache budget using Llama 3.1-8B-Instruct** (averaged across all tasks in Table 1).

## 5. ANCHOR/CENTROID COMPUTATION

The anchor vector is computed as:
μ(K̂) = (1/n)∑ᵢ₌₁ⁿ(kᵢ/‖kᵢ‖)

Where normalized keys are averaged. Ablation studies (Table 2) show using unnormalized mean μ(K) performs similarly. **Computational complexity: O(n) operations on average**, where n is cache size.

## 6. BASELINE COMPARISONS

**Table 1 (Llama 3.1-8B-Instruct, LongBench average, B=128):**

| Budget | H2O | TOVA | Sink | SnapKV | KeyDiff |
|--------|-----|------|------|--------|---------|
| 2K | 16.89 | 37.52 | 36.88 | 39.60 | 44.33 |
| 4K | 26.37 | 41.49 | 40.95 | 45.18 | 47.66 |
| 6K | 33.19 | 45.24 | 43.39 | 47.12 | 48.51 |
| 8K | 38.20 | 47.09 | 44.68 | 48.06 | 49.03 |

**Table 1 (Llama 3.2-3B-Instruct, same conditions):**

| Budget | H2O | TOVA | Sink | SnapKV | KeyDiff |
|--------|-----|------|------|--------|---------|
| 2K | 14.25 | 33.52 | 33.74 | 35.46 | 38.14 |
| 4K | 22.38 | 38.24 | 37.96 | 40.60 | 43.67 |
| 6K | 28.44 | 41.02 | 40.01 | 43.55 | 45.27 |
| 8K | 33.46
…[truncated 1172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T17:30:08.855887+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2504.15364v1",
  "prompt": "I need very specific details:\n\n1. What is the FULL CONTEXT (no eviction) baseline score on LongBench for Llama 3.1-8B-Instruct and Llama 3.2-3B-Instruct? I need the exact number so I can verify the \"0.04% loss\" claim against KeyDiff's 8K score.\n\n2. For the anchor computation: is it recomputed from scratch every step (exact mean), or is it maintained as a running/incremental mean? Does the paper discuss this?\n\n3. What is the context length of the input sequences in LongBench? What is the max sequence length the models support?\n\n4. The \"23% KV cache reduction\" for 8K budget - what is the full context size this is relative to? Is it relative to a specific input length?\n\n5. Are there per-task breakdown numbers in the tables? What are KeyDiff's scores on individual LongBench tasks vs full context?\n\n6. Math500 results for Deepseek-R1-Distill-Llama-8B - what are the exact numbers?\n\n7. Latency comparison numbers - what is the exact speedup vs each baseline?\n\nExtract exact numbers, not summaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2504.15364v1",
    "prompt": "I need very specific details:\n\n1. What is the FULL CONTEXT (no eviction) baseline score on LongBench for Llama 3.1-8B-Instruct and Llama 3.2-3B-Instruct? I need the exact number so I can verify the \"0.04% loss\" claim against KeyDiff's 8K score.\n\n2. For the anchor computation: is it recomputed from scratch every step (exact mean), or is it maintained as a running/incremental mean? Does the paper discuss this?\n\n3. What is the context length of the input sequences in LongBench? What is the max sequence length the models support?\n\n4. The \"23% KV cache reduction\" for 8K budget - what is the full context size this is relative to? Is it relative to a specific input length?\n\n5. Are there per-task breakdown numbers in the tables? What are KeyDiff's scores on individual LongBench tasks vs full context?\n\n6. Math500 results for Deepseek-R1-Distill-Llama-8B - what are the exact numbers?\n\n7. Latency comparison numbers - what is the exact speedup vs each baseline?\n\nExtract exact numbers, not summaries."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T17:30:08.856091+00:00_

# KeyDiff Paper: Specific Data Points

## 1. Full Context Baseline Scores

From **Table 1**, the non-evicting baseline scores are:
- **Llama 3.1-8B-Instruct**: 49.20 average
- **Llama 3.2-3B-Instruct**: 45.87 average

KeyDiff at 8K achieves:
- **Llama 3.1-8B**: 49.03 (gap: 0.17 points, ~0.35%)
- **Llama 3.2-3B**: 45.78 (gap: 0.09 points, ~0.20%)

**Note**: The paper's "≤0.04%" claim appears to reference a different metric or subset; the table shows larger gaps when calculated from raw scores.

## 2. Anchor Vector Computation

The paper does not explicitly specify whether the anchor `μ(K̂)` is recomputed from scratch at each eviction step or maintained incrementally. Section 3.2 states the anchor is computed as `1/n ∑ k̂ᵢ` where n is the current cache size, suggesting fresh computation per step, but no confirmation of incremental tracking exists.

## 3. LongBench Context Lengths

The paper states: "51% of prompts are longer than the largest KV cache size of 8K" but **does not provide specific maximum sequence lengths** for the benchmark or model context windows. Section B.3 references "Prompt lengths" statistics but these are truncated in the provided content.

## 4. "23% KV Cache Reduction" Basis

This figure represents the **average compression across LongBench tasks**: with an 8K budget versus uncompressed full prompts, approximately 23% of the original KV cache is eliminated. No single reference length is specified.

## 5. Per-Task Breakdowns

**Table 1 provides complete per-task results**. Examples for 8K budget (Llama 3.1-8B):
- NarrativeQA: 18.78 vs baseline 34.86
- Qasper: 11.35 vs baseline 25.32
- PassageRetrieval-en: 59.74 vs baseline 61.66

Full task-level data appears in **Table 11** (referenced as containing complete results but not reproduced in excerpt).

## 6. Math500 / Deepseek Results

**No Math500 or Deepseek-R1-Distill-Llama-8B results appear in the provided content.** The paper evaluates only: Llama 3.1-8B, Llama 3.2-3B, and Qwen 2.5-3B/7B.

## 7
…[truncated 146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T17:30:08.856281+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.15364",
  "prompt": "Extract the full abstract of this paper. I need to find the exact wording of the \"0.04% loss\" claim and any mention of Deepseek-R1, Math500, and latency speedup numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2504.15364",
    "prompt": "Extract the full abstract of this paper. I need to find the exact wording of the \"0.04% loss\" claim and any mention of Deepseek-R1, Math500, and latency speedup numbers."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T17:30:08.856433+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2504.15364v1",
  "prompt": "Find and extract:\n1. The Qwen 2.5-3B and Qwen 2.5-7B results tables with exact numbers for all budgets and all baselines\n2. Any mention of Deepseek-R1-Distill-Llama-8B or Math500 benchmark - search the entire document\n3. Any latency or throughput measurements - search for words like \"latency\", \"speedup\", \"throughput\", \"wall-clock\", \"time\", \"seconds\"\n4. The exact text surrounding the \"0.04%\" claim - I need the exact sentence\n5. Table 7 (appendix) results if available\n6. Algorithm pseudocode or detailed description of per-step eviction procedure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2504.15364v1",
    "prompt": "Find and extract:\n1. The Qwen 2.5-3B and Qwen 2.5-7B results tables with exact numbers for all budgets and all baselines\n2. Any mention of Deepseek-R1-Distill-Llama-8B or Math500 benchmark - search the entire document\n3. Any latency or throughput measurements - search for words like \"latency\", \"speedup\", \"throughput\", \"wall-clock\", \"time\", \"seconds\"\n4. The exact text surrounding the \"0.04%\" claim - I need the exact sentence\n5. Table 7 (appendix) results if available\n6. Algorithm pseudocode or detailed description of per-step eviction procedure"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T17:30:08.856571+00:00_

# KeyDiff Paper Abstract - Key Claims

Here is the full abstract with the specific claims you requested:

**Full Abstract:**
"We demonstrate that geometrically distinctive keys during LLM inference tend to have high attention scores. Based on the phenomenon we propose KeyDiff, a training-free KV cache eviction method based solely on key similarity. Unlike other KV cache eviction methods, KeyDiff can process arbitrarily long prompts within strict resource constraints and efficiently generate responses. We provide a theoretical basis for KeyDiff by relating key diversity with attention scores. These results imply KeyDiff can efficiently identify the most important tokens to retain. Notably KeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention. Under a strict memory allowance, we demonstrate the effectiveness of KeyDiff for the Llama and Qwen model families by observing a performance gap of less than 0.04% with 8K cache budget (~23% KV cache reduction) from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B. We also observe near baseline performance for Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark and decrease end-to-end inference latency by up to 30% compared to the other token-eviction methods."

**Key Specific Claims:**
- Performance gap: "less than 0.04%"
- Model tested: "Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark"
- Latency improvement: "up to 30% compared to the other token-eviction methods"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T17:30:08.856713+00:00_

Based on my review of the provided document, here are the findings:

## 1. Qwen 2.5 Results Tables

The main paper (Table 1) only shows Llama 3.1-8B and Llama 3.2-3B results. Qwen 2.5-3B/7B results are mentioned as being in Table 9 of the appendix, but **Table 9 is not included in the provided content**. The document references it: "those of Qwen 2.5-3B/7B-Instruct in [Table 9]" but the actual table data is not present.

## 2. Deepseek-R1-Distill or Math500

**No mention found** anywhere in the document of Deepseek-R1-Distill-Llama-8B or a Math500 benchmark.

## 3. Latency or Throughput Measurements

**No latency, speedup, throughput, wall-clock time, or seconds measurements** are provided in this paper. The work focuses exclusively on accuracy metrics.

## 4. The "0.04%" Claim - Exact Text

"KeyDiff outperforms other eviction strategies across most tasks, demonstrating a performance gap of less than 0.04% with 8K cache budget (∼23% KV cache reduction) from the non-evicting baseline on the LongBench benchmark for Llama 3.1-8B and Llama 3.2-3B."

## 5. Table 7 (Appendix Results)

Table 7 is referenced as containing "Results for Full Prompt Processing" but **the actual table data is not included** in the provided document excerpt.

## 6. Algorithm Pseudocode

The document provides equations and mathematical descriptions rather than traditional pseudocode. The eviction procedure is summarized in Equations 7-8, with Figure 3 illustrating the three-step process: compute anchor vector, calculate cosine similarities, retain lowest-similarity tokens.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_keydiff_details_20260512T172753",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T17:30:08.856943+00:00_

数据收集完毕。以下是 KeyDiff 论文精确实验条件的汇总。

---

## KeyDiff (arXiv:2504.15364) 实验条件汇总

### 1. 模型

| 模型 | 参数量 | 用途 |
|------|--------|------|
| Llama 3.1-8B-Instruct | 8B | 主实验 (LongBench) |
| Llama 3.2-3B-Instruct | 3B | 主实验 (LongBench) |
| Qwen 2.5-3B-Instruct | 3B | 附录 (Table 9, 未在 HTML 中完整展示) |
| Qwen 2.5-7B-Instruct | 7B | 附录 (Table 9) |
| Deepseek-R1-Distill-Llama-8B | 8B | Math500 (仅在 abstract 提及, 正文/附录未找到详细数据) |

### 2. 评测数据集

**LongBench (English subset, 16 tasks):**
- Single Doc QA: NarrativeQA, Qasper
- Multi Doc QA: MultifieldQA-en, HotpotQA, 2WikiMQA, Musique
- Summarization: GovReport, QMSum, MultiNews
- Few-shot: TREC, TriviaQA, SAMSum
- Synthetic: PassageCount, PassageRetrieval-en
- Code: LCC, RepoBench-P

**其他:** Needle In a Haystack, Math500 (仅 abstract 提及)

### 3. KV Cache Budget

| Budget | Token 数 | 近似压缩比 (基于 LongBench 平均) |
|--------|----------|--------------------------------|
| 2K | 2048 | ~80% reduction |
| 4K | 4096 | ~55% reduction |
| 6K | 6144 | ~33% reduction |
| 8K | 8192 | **~23% reduction** |

Block size: B=128 (prompt processing), B=1 (generation)。51% 的 LongBench prompt 长度超过 8K。

### 4. "<0.04% loss" 精确含义

**论文原文：** "a performance gap of less than 0.04% with 8K cache budget (~23% KV cache reduction) from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B"

**但实际表格数据存在不一致：**

| 模型 | Full Context | KeyDiff@8K | 绝对差 (pp) | 相对差 |
|------|-------------|------------|-------------|--------|
| Llama 3.1-8B | 49.20 | 49.03 | **0.17 pp** | **0.35%** |
| Llama 3.2-3B | 45.87 | 45.78 | **0.09 pp** | **0.20%** |

- **度量：** LongBench 各任务平均分 (各任务有自己的 metric，综合后取均值)
- **0.04% 与表格数据不匹配** — 可能指特定 subset、附录中的 full-prompt-processing (B=∞) 配置 (Table 7)，或者 abstract 的表述有误。HTML 版未完整展示附录表格，无法最终确认。

### 5. Centroid (Anchor) 计算方式

**公式：**
$$\mu(\hat{K}) = \frac{1}{n}\sum_{i=1}^{n} \frac{k_i}{\|k_i\|}$$

- **先对每个 key 做 L2 归一化，再取算术平均** — 即 exact mean of normalized keys
- 论文**未明确说明**是 per-step 重新计算还是 running mean (incremental)
- 由于是简单均值，理论上可用 running sum 增量维护：`sum += new_key/||new_key||; sum -= evicted_key/||evicted_key||; anchor = sum/n`
- **复杂度：O(n) per eviction step** (n = cache size)，计算所有 token 与 anchor 的 cosine similarity 以选出要驱逐的 token

**Ablation (Llama 3.2-3B, Table 2) — anchor 选择方式对比：**

| Budget | Pairwise | Median | KeyDiff (Mean) |
|--------|----------|--------|----------------|
| 2K | 35.24 | 35.43 | 35.09 |
| 4K | 40.61 | 40.67 | 40.28 |
| 6K | 41.87 | 41.89 | 41.88 |
| 8K | 42.45 | 42.26 | 42.40 |

差异很小，Mean 方案在大 budget 下接近其他方案，但计算最简单。

### 6. Baseline 对比 (主表)

**Llama 3.1-8B-Instruct, LongBench Average, B=128:**

| Budget | H2O | TOVA | StreamingLLM (Sink) | SnapKV | **KeyDiff** | Full Context |
|--------|-----|------|---------------------|--------|-------------|-------------|
| 2K | 16.89 | 37.52 | 36.88 | 39.60 | **44.33** | 49.20 |
| 4K | 26.37 | 41.49 | 40.95 | 45.18 | **47.66** | 49.20 |
| 6K | 33.19 | 45.24 | 43.39 | 47.12 | **48.51** | 49.20 |
| 8K | 38.20 | 47.09 | 44.68 | 48.06 | **49.03** | 49.20 |

**Llama 3.2-3B-Instruct, LongBench Average, B=128:**

| Budget | H2O | TOVA | StreamingLLM (Sink) | SnapKV | **KeyDiff** | Full Context |
|--------|-----|------|---------------------|--------|-------------|-------------|
| 2K | 14.25 | 33.52 | 33.74 | 35.46 | **38.14** | 45.87 |
| 4K | 22.38 | 38.24 | 37.96 | 40.60 | **43.67** | 45.87 |
| 6K | 28.44 | 41.02 | 40.01 | 43.55 | **45.27** | 45.87 |
| 8K | 33.46 | 43.21 | 41.97 | 44.96 | **45.78** | 45.87 |

**Similarity metric ablation (Table 3, Llama 3.2-3B):**

| Budget | Dot Product | Euclidean | **Cosine (KeyDiff)** |
|--------|------------|-----------|---------------------|
| 2K | 30.14 | 13.68 | **35.09** |
| 4K | 38.01 | 21.06 | **40.28** |
| 8K | 42.23 | 29.53 | **42.40** |

### 7. 缺失/不完整数据

| 信息 | 状态 |
|------|------|
| Deepseek-R1 + Math500 精确数字 | **仅 abstract 提及 "near baseline"，正文无详细表格** |
| 延迟 "up to 30% speedup" 具体数据 | **仅 abstract 提及，正文无 latency 表格** |
| Qwen 2.5-3B/7B 完整结果 | **在附录 Table 9，HTML 版未完整渲染** |
| Full prompt processing (B=∞) 结果 | **在附录 Table 7，HTML 版未完整渲染** |
| 0.04% claim 的精确来源 | **与主表数据不一致，可能来自未展示的附录表** |

---

**核心结论：** KeyDiff 在所有 budget 下均优于 H2O、TOVA、StreamingLLM、SnapKV。8K budget 下与 full context 的差距为 0.17pp (Llama-8B) / 0.09pp (Llama-3B)。Anchor 是 normalized keys 的 exact mean，O(n) 复杂度。Abstract 中的 "0.04%"、"30% latency"、"Math500" 三项 claim 在论文正文中均未找到支撑数据表格。

Sources:
- [KeyDiff Paper (arXiv abstract)](https://arxiv.org/abs/2504.15364)
- [KeyDiff Paper (HTML full text)](https://arxiv.org/html/2504.15364v1)
- [AlphaXiv page](https://www.alphaxiv.org/abs/2504.15364)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_keydiff_details_20260512T172753"
}
```

</details>

---
