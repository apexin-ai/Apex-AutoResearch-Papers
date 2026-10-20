# research code survey

**redundancy compound sparsity 2** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_research_code-survey_20260512T075744.jsonl`
- **Structured JSON:** [`193632965d2bba5b41d6.json`](../../sessions/19/193632965d2bba5b41d6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-12T08:01:32.897551+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T08:01:32.897897+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T08:01:32.898089+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Token Filtering arXiv 2512.07090 GitHub code KV cache eviction EMA centroid"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Token Filtering arXiv 2512.07090 GitHub code KV cache eviction EMA centroid"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T08:01:32.898220+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TEAL training-free efficient activation-aware LLM pruning ICLR 2025 GitHub code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TEAL training-free efficient activation-aware LLM pruning ICLR 2025 GitHub code"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-12T08:01:32.898383+00:00_

Web search results for query: "TEAL training-free efficient activation-aware LLM pruning ICLR 2025 GitHub code"

Links: [{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"Training-Free Activation Sparsity in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=dGVZwyq5tV"},{"title":"training-free activation sparsity in large language models","url":"https://www.arxiv.org/pdf/2408.14690"},{"title":"GitHub - victor7246/prunenet: Official repository for the paper: \"You Only Prune Once: Designing Calibration-Free Model Compression With Policy Learning\" [ICLR 2025]. · GitHub","url":"https://github.com/victor7246/prunenet"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"TEAL: Training-Free Activation Sparsity in Large Language Models","url":"https://www.together.ai/blog/teal-training-free-activation-sparsity-in-large-language-models"},{"title":"GitHub - LumosJiang/Awesome-On-Device-LLMs: [ArXiv 2025] A curated list of papers on on-device large language models, focusing on model compression and system optimization techniques from the survey \"On-Device Large Language Models: A Survey of Model Compression and System Optimization\". · GitHub","url":"https://github.com/LumosJiang/Awesome-On-Device-LLMs"},{"title":"GitHub - F-JISOO/ICLR-2025-Submitted · GitHub","url":"https://github.com/F-JISOO/ICLR-2025-Submitted"},{"title":"GitHub - horseee/Awesome-Efficient-LLM: A curated list for Efficient Large Language Models · GitHub","url":"https://github.com/horseee/Awesome-Efficient-LLM"}]

Based
…[truncated 1408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T08:01:32.898644+00:00_

Web search results for query: "Token Filtering arXiv 2512.07090 GitHub code KV cache eviction EMA centroid"

Links: [{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/html/2512.07090"},{"title":"[2512.07090] Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/abs/2512.07090"},{"title":"CTkvr: Efficient KV Cache Retrieval for Long-Context LLMs via Centroid-then-Token Indexing","url":"https://arxiv.org/html/2512.15550"},{"title":"Learning What to Write: Write-Gated KV for Efficient Long-Context Inference","url":"https://arxiv.org/html/2512.17452v1"},{"title":"CAOTE: KV Cache Eviction for LLMs via Attention Output Error-Based Token Selection","url":"https://arxiv.org/html/2504.14051v4"},{"title":"CAOTE: KV Caching through Attention Output Error based Token Eviction","url":"https://arxiv.org/html/2504.14051v1"},{"title":"G-KV: Decoding-Time KV Cache Eviction with Global Attention | OpenReview","url":"https://openreview.net/forum?id=4Uxtzc5Jns"},{"title":"G-KV: Decoding-Time KV Cache Eviction with Global Attention","url":"https://arxiv.org/html/2512.00504v1"},{"title":"[2512.15550] CTkvr: KV Cache Retrieval for Long-Context LLMs via Centroid then Token Indexing","url":"https://arxiv.org/abs/2512.15550"},{"title":"HashEvict: A Pre-Attention KV Cache Eviction Strategy using Locality-Sensitive Hashing","url":"https://arxiv.org/html/2412.16187v3"}]

Based on the search results, I found relevant information about the arXiv paper 2512.07090:

## Token Filtering (arXiv 2512.07090)

Token Filtering is a lightweight online structured pruning technique that makes pruning decisions directly during inference without any calibration data. The key idea is to measure token redundancy via joint key-value similarity and skip redundant attention computations, thereby reducing inference cost while preserving critical information.

To further enhance stability, the method designs a variance-aware fusion st
…[truncated 907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T08:01:32.898831+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Leveraging KV Similarity\" \"Online Structured Pruning\" GitHub repository code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Leveraging KV Similarity\" \"Online Structured Pruning\" GitHub repository code"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-12T08:01:32.898957+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TEAL \"training-free activation sparsity\" GitHub repository code together.ai"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TEAL \"training-free activation sparsity\" GitHub repository code together.ai"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-12T08:01:32.899107+00:00_

Web search results for query: "TEAL "training-free activation sparsity" GitHub repository code together.ai"

Links: [{"title":"GitHub - FasterDecoding/TEAL","url":"https://github.com/FasterDecoding/TEAL"},{"title":"TEAL: Training-Free Activation Sparsity in Large Language Models","url":"https://www.together.ai/blog/teal-training-free-activation-sparsity-in-large-language-models"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2408.14690v1"},{"title":"training-free activation sparsity in large language models","url":"https://www.arxiv.org/pdf/2408.14690"},{"title":"[2408.14690] Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/abs/2408.14690"},{"title":"Together AI Present TEAL: A Groundbreaking Training-Free Activation Sparsity Method for Optimizing Large Language Models with Enhanced Efficiency and Minimal Degradation in Resource-Constrained Environments - MarkTechPost","url":"https://www.marktechpost.com/2024/09/08/together-ai-present-teal-a-groundbreaking-training-free-activation-sparsity-method-for-optimizing-large-language-models-with-enhanced-efficiency-and-minimal-degradation-in-resource-constrained-enviro/"},{"title":"Training-Free Activation Sparsity in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=dGVZwyq5tV"},{"title":"(PDF) Training-Free Activation Sparsity in Large Language Models","url":"https://www.researchgate.net/publication/383460804_Training-Free_Activation_Sparsity_in_Large_Language_Models"},{"title":"Preprint. Under Review. TRAINING-FREE ACTIVATION SPARSITY IN","url":"https://www.arxiv.org/pdf/2408.14690v1"},{"title":"Training-Free Activation Sparsity in Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240814690L/abstract"}]

I found the TEAL GitHub repository and related information. Here are the search results:

## TEAL: Training-Free Activation Sparsity in Large Language Models

**GitHub Repository
…[truncated 1187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T08:01:32.899286+00:00_

Web search results for query: ""Leveraging KV Similarity" "Online Structured Pruning" GitHub repository code"

Links: [{"title":"[2512.07090] Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/abs/2512.07090"},{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://www.arxiv.org/pdf/2512.07090"},{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/html/2512.07090"},{"title":"(PDF) Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://www.researchgate.net/publication/398476553_Leveraging_KV_Similarity_for_Online_Structured_Pruning_in_LLMs"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"Published in Transactions on Machine Learning Research (05/2025)","url":"https://openreview.net/pdf?id=z3JZzu9EA3"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://openreview.net/pdf?id=C69741fMFX"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"Similarity-Aware Token Pruning: Your VLM but Faster","url":"https://arxiv.org/html/2503.11549v1"}]

Based on my search results, I found information about the research paper "Leveraging KV Similarity for Online Structured Pruning in LLMs," but I did not find a specific GitHub repository link in the search results.

## About the Research

The paper introduces Token Filtering, a lightweight online structured pruning technique that makes pruning decisions directly during inference without any calibration data. The key idea is to measure token redundancy via joint key-value similarity and skip redundant attention computations,
…[truncated 1145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T08:01:32.899473+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.07090",
  "prompt": "Find the GitHub repository link or code link for this paper. Look for any URLs pointing to code, supplementary material, or author GitHub profiles."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2512.07090",
    "prompt": "Find the GitHub repository link or code link for this paper. Look for any URLs pointing to code, supplementary material, or author GitHub profiles."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T08:01:32.899606+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/FasterDecoding/TEAL",
  "prompt": "Extract the full README content. I need: 1) repository structure (key files/directories), 2) how magnitude-based pruning is implemented, 3) which layers are pruned, 4) default sparsity ratios, 5) supported model architectures, 6) how to integrate with HuggingFace transformers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/FasterDecoding/TEAL",
    "prompt": "Extract the full README content. I need: 1) repository structure (key files/directories), 2) how magnitude-based pruning is implemented, 3) which layers are pruned, 4) default sparsity ratios, 5) supported model architectures, 6) how to integrate with HuggingFace transformers."
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T08:01:32.899730+00:00_

# Code Repository Search Result

Based on the webpage content provided, **no GitHub repository link or code link is mentioned** for this paper (arXiv:2512.07090).

The page includes sections for "Code, Data, Media Associated with this Article" with tools like alphaXiv, CatalyzeX Code Finder, DagsHub, and Hugging Face, but none of these display actual links or indicate that code has been shared by the authors.

To find code for this paper, you would need to:
- Check the authors' GitHub profiles directly
- Visit the paper's full HTML or PDF version for supplementary materials
- Contact the authors listed: Jungmin Lee, Gwangeun Byeon, Yulhwa Kim, or Seokin Hong

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T08:01:32.899892+00:00_

# TEAL Repository Analysis

## 1) Repository Structure
Key directories include:
- **figures/**: visualizations and documentation images
- **gpt-fast/**: inference implementation framework
- **kernels/**: sparse computation kernels
- **models/**: pre-calibrated thresholds for Llama-2/3 and Mistral
- **teal/**: core sparsity implementation (histogram generation, perplexity testing, optimization)
- **utils/**: utility functions
- **notebooks/**: jupyter demonstrations

## 2) Magnitude-Based Pruning Implementation
The method applies "magnitude-based activation sparsity to hidden states throughout the entire model." Implementation involves:
- Constructing activation histograms via `grab_acts.py`
- Using calibrated thresholds stored in model folders
- Block-wise greedy optimization available through `greedyopt.py`

## 3) Which Layers Are Pruned
The documentation specifies pruning occurs in "hidden states throughout the entire model" but doesn't detail specific layer types. The approach targets activation tensors rather than weights.

## 4) Default Sparsity Ratios
The paper achieves "40-50% model-wide sparsity with minimal performance degradation." Example configurations use `--sparsity 0.5` (50%) in provided scripts.

## 5) Supported Model Architectures
Currently supports:
- Llama-2 (7B-70B)
- Llama-3 (7B-70B)
- Mistral family
- FP16 inference only for quantitative evaluation

## 6) HuggingFace Integration
The codebase references HuggingFace model IDs (e.g., `meta-llama/Llama-2-7b-hf`) and includes conversion scripts, but the README doesn't detail direct transformer library integration. Users download HF models and convert to gpt-fast format using provided conversion utilities.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T08:01:32.900053+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jungmin Lee \"token filtering\" KV similarity structured pruning GitHub code 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jungmin Lee \"token filtering\" KV similarity structured pruning GitHub code 2025"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-12T08:01:32.900170+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2512.07090",
  "prompt": "Extract the key algorithm details: 1) The EMA centroid update formula (Anchor_k, Anchor_v), 2) The similarity score formula with alpha and gamma parameters, 3) Default values of gamma (EMA decay), alpha (key/value weight), and threshold tau, 4) How the hook is attached to attention layers, 5) The token filtering decision process (which tokens are kept/pruned), 6) Any pseudocode or algorithm descriptions. Also look for any GitHub or code repository links."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2512.07090",
    "prompt": "Extract the key algorithm details: 1) The EMA centroid update formula (Anchor_k, Anchor_v), 2) The similarity score formula with alpha and gamma parameters, 3) Default values of gamma (EMA decay), alpha (key/value weight), and threshold tau, 4) How the hook is attached to attention layers, 5) The token filtering decision process (which tokens are kept/pruned), 6) Any pseudocode or algorithm descriptions. Also look for any GitHub or code repository links."
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T08:01:32.900288+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/FasterDecoding/TEAL/tree/main/teal",
  "prompt": "List all files in the teal/ directory with their descriptions. I need to understand the code structure for magnitude-based activation pruning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/FasterDecoding/TEAL/tree/main/teal",
    "prompt": "List all files in the teal/ directory with their descriptions. I need to understand the code structure for magnitude-based activation pruning."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T08:01:32.900454+00:00_

Web search results for query: "Jungmin Lee "token filtering" KV similarity structured pruning GitHub code 2025"

Links: [{"title":"[2512.07090] Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/abs/2512.07090"},{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://www.arxiv.org/pdf/2512.07090"},{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/html/2512.07090"},{"title":"(PDF) Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://www.researchgate.net/publication/398476553_Leveraging_KV_Similarity_for_Online_Structured_Pruning_in_LLMs"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"},{"title":"SlimGPT: Layer-wise Structured Pruning for Large Language Models","url":"https://www.researchgate.net/publication/397201574_SlimGPT_Layer-wise_Structured_Pruning_for_Large_Language_Models"},{"title":"Learned Token Pruning for Transformers | Request PDF","url":"https://www.researchgate.net/publication/362690076_Learned_Token_Pruning_for_Transformers"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"Similarity-Aware Token Pruning: Your VLM but Faster","url":"https://arxiv.org/html/2503.11549v1"},{"title":"GitHub - Theia-4869/CDPruner: [NeurIPS 2025] Official code for paper: Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs.","url":"https://github.com/Theia-4869/CDPruner"}]

Based on the search results, I found information about Jungmin Lee's work on token filtering with KV similarity and structured pruning:

## Key Finding

Jungmin Lee and 3 other authors published a paper titled "Leveraging KV Similarity for Online Structured Pruning in LLMs", which was posted on arXiv in December 2025.

## About Token 
…[truncated 1061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T08:01:32.900622+00:00_

# TEAL Directory Structure

Based on the GitHub page content provided, here are the files in the `teal/` directory:

1. **grab_acts.py** - Likely handles extraction or collection of activation data needed for pruning analysis

2. **greedyopt.py** - Implements greedy optimization algorithms, probably for selecting which activations to prune

3. **mlp.py** - Contains multi-layer perceptron implementations, possibly modified for pruning operations

4. **model.py** - Core model architecture definitions

5. **ppl_test.py** - Perplexity testing module for evaluating model performance after pruning

6. **self_attn.py** - Self-attention mechanism implementation, likely adapted for magnitude-based pruning

7. **__pycache__/** - Python cache directory (compiled bytecode)

The structure suggests TEAL implements magnitude-based activation pruning by: extracting activations, applying greedy optimization to identify pruning candidates, testing impact via perplexity metrics, and modifying core components (attention, MLP layers) accordingly.

Note: The page content itself doesn't provide detailed file descriptions—this analysis is inferred from filename conventions and the stated project focus on faster decoding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T08:01:32.900766+00:00_

# Token Filtering Algorithm Details

## Key Algorithm Components

### 1. **EMA Centroid Update Formula**
The anchor key/value uses exponential moving average with smoothing factor γ (gamma):

```
Anchor ← γ·Anchor + (1−γ)·k_current
```

Default value: **γ = 0.9** (mentioned as "close to one"). This "emphasizes more recent inputs and avoids the dominance of older tokens."

### 2. **Similarity Score Computation**

**Variance-aware weighting formula:**
```
α = σ_v^(-2) / (σ_k^(-2) + σ_v^(-2))
S_KV = α·s_k + (1−α)·s_v
```

Where:
- s_k, s_v = cosine similarity scores for keys/values across attention heads
- σ_k², σ_v² = running variances across heads
- α adapts dynamically, assigning "greater weight to the side with lower variance"

### 3. **Threshold Adaptation**

Layer-wise threshold updates via proportional feedback:
```
T_l ← T_l + η(P_current − P_tail)
```

Where η is a "small learning rate" (specific value not provided in document).

### 4. **Token Filtering Decision**

Tokens are pruned when: **S_KV > τ[i]**

For pruned tokens: "the attention output for that token is replaced with zero" while LayerNorm still executes.

### 5. **Tail-Focused Pruning Strategy**

Applies only to final Y fraction of layers (default **Y = 0.5**):
```
P_tail = P_global / Y
```

## Architecture Integration

Token Filtering inserts "an additional Token Filtering layer into each Transformer block, placing it before the attention layer" with a skip path for bypassed computations.

## Implementation Note

**No code repository link is provided in the document.** The paper notes that "official implementations released by the original authors" exist for baselines but does not indicate public availability of Token Filtering code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-12T08:01:32.900934+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/teal/mlp.py",
  "prompt": "Extract the complete source code. I need to understand: 1) How magnitude-based pruning is applied to MLP layers, 2) Which specific sublayers (gate, up, down projections) are pruned, 3) How the sparsity threshold/ratio is applied, 4) The actual masking/zeroing logic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/teal/mlp.py",
    "prompt": "Extract the complete source code. I need to understand: 1) How magnitude-based pruning is applied to MLP layers, 2) Which specific sublayers (gate, up, down projections) are pruned, 3) How the sparsity threshold/ratio is applied, 4) The actual masking/zeroing logic."
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-12T08:01:32.901059+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/teal/self_attn.py",
  "prompt": "Extract the complete source code. I need to understand: 1) How magnitude-based pruning is applied to attention layers, 2) What activations are pruned (Q, K, V, or output projections), 3) How sparsity thresholds are applied, 4) The masking logic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/teal/self_attn.py",
    "prompt": "Extract the complete source code. I need to understand: 1) How magnitude-based pruning is applied to attention layers, 2) What activations are pruned (Q, K, V, or output projections), 3) How sparsity thresholds are applied, 4) The masking logic."
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T08:01:32.901176+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/teal/model.py",
  "prompt": "Extract the complete source code. I need: 1) How the model is composed, 2) How sparsity is configured per layer, 3) How thresholds are loaded and applied, 4) Integration with transformer architecture."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/teal/model.py",
    "prompt": "Extract the complete source code. I need: 1) How the model is composed, 2) How sparsity is configured per layer, 3) How thresholds are loaded and applied, 4) Integration with transformer architecture."
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-12T08:01:32.901298+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com \"token filtering\" \"kv similarity\" OR \"structured pruning\" LLM EMA anchor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com \"token filtering\" \"kv similarity\" OR \"structured pruning\" LLM EMA anchor"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-12T08:01:32.901437+00:00_

# Analysis of MLP Layer Pruning Implementation

Based on the provided code, here's what I can determine:

## 1) Pruning Application Method

The code doesn't show magnitude-based pruning directly. Instead, it uses a `SparsifyFn` class (imported from utils) that appears to be the actual pruning mechanism. The monkeypatch function replaces the standard forward pass with a custom implementation.

## 2) Pruned Sublayers

Three specific sublayers are targeted:
- **'gate'**: Applied to gate projection inputs
- **'up'**: Applied to up projection inputs  
- **'down'**: Applied to intermediate states before down projection

As shown: `"'gate': SparsifyFn(mlp.distrs['h1']).to(get_module_device(mlp)),"` and similar patterns for 'up' and 'down'.

## 3) Sparsity Threshold Application

The threshold logic is **not visible** in this excerpt. The `SparsifyFn` and `Distribution` classes (defined elsewhere in utils) contain the actual threshold computation. These classes are instantiated with `Distribution` objects that reference a file path, suggesting thresholds may be loaded from stored data.

## 4) Masking/Zeroing Logic

The actual masking occurs within `SparsifyFn.__call__()`, which is invoked as `self.sparse_fns['gate'](x)`. The code shows the pruned tensors are then passed to projection layers, but the zeroing mechanism itself is encapsulated in the external utility classes.

**Key limitation**: The complete pruning logic requires examining the `utils` module implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T08:01:32.901582+00:00_

# Analysis of Attention Layer Pruning Implementation

## 1) Magnitude-Based Pruning Application

The code doesn't directly implement magnitude-based pruning. Instead, it uses a **Distribution-based sparsification approach**:

```python
self_attn.sparse_fns = nn.ModuleDict({
    'q': SparsifyFn(self_attn.distrs['h1']),
    'k': SparsifyFn(self_attn.distrs['h1']),
    'v': SparsifyFn(self_attn.distrs['h1']),
    'o': SparsifyFn(self_attn.distrs['h2'])
})
```

The `SparsifyFn` modules are instantiated with `Distribution` objects that learn activation patterns from stored data, rather than using fixed magnitude thresholds.

## 2) Activations Being Pruned

The implementation prunes **both input and output projections**:

- **Input projections**: Query (q), Key (k), and Value (v) - all use distribution `h1`
- **Output projection**: The attention output (`o`) uses distribution `h2`

Notably, the sparsification occurs **before** the projection operations:
```python
x_q = self.sparse_fns['q'](hidden_states)
query_states = self.q_proj(x_q)
```

## 3) Sparsity Thresholds

The code references `Distribution` and `SparsifyFn` utilities (imported from `utils.utils`), but their threshold logic is **not shown in this excerpt**. The thresholds are managed externally via the `file_path` parameter, suggesting learned or pre-computed sparsity patterns stored on disk.

## 4) Masking Logic

**No explicit masking is implemented here.** Instead, the approach uses:
- **Activation grabbing mode**: Records actual activations for learning sparsity patterns
- **Sparsification mode**: Applies learned sparse masks via `SparsifyFn` before projection layers

The actual masking/zeroing mechanism resides in the imported `SparsifyFn` class, not in this forward function.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T08:01:32.901720+00:00_

# Source Code Analysis: Sparse Model Architecture

## 1. Model Composition

The architecture uses a mixin-based design pattern. **`SparseModelMixin`** enhances transformer models by wrapping decoder layers with sparsity logic. Two model variants inherit this mixin:

- **`LlamaSparseForCausalLM`**: Extends `LlamaForCausalLM`
- **`MistralSparseForCausalLM`**: Extends `MistralForCausalLM`

Each model contains stacked decoder layers that are monkeypatched during initialization: `"for i, layer in enumerate(self.model.layers): layers.append(_monkeypatch_layer(layer, path=...))"` to inject sparse computation modules.

## 2. Per-Layer Sparsity Configuration

Sparsity is configured through multiple methods:

- **Uniform sparsity**: `set_uniform_sparsity()` applies identical thresholds across all layers
- **Component-specific**: `set_mlp_sparsity()` and `set_self_attn_sparsity()` target MLP and attention modules separately
- **Greedy allocation**: `load_greedy_sparsities()` loads layer-specific values from a configuration file
- **Custom per-layer**: `set_sparsities()` accepts a dictionary mapping projections to layer-wise threshold arrays

Each layer's MLP and self-attention contain `sparse_fns` dictionaries holding sparsity operators for gates, up/down projections, and Q/K/V/O matrices.

## 3. Threshold Loading and Application

Thresholds are set via `set_threshold()` calls on sparse function objects. The `from_pretrained()` classmethod orchestrates this:

```
if greedy_sparsity_path is not None:
    model.load_greedy_sparsities(greedy_sparsity_path, greedy_sparsity_level)
elif uniform_sparsity is not None:
    model.set_uniform_sparsity(uniform_sparsity)
```

The `apply_prefill` parameter controls whether thresholds apply during prompt processing, configured via `"set_apply_prefill(apply_prefill)"` on individual sparse functions.

## 4. Transformer Integration

Sparsification hooks into the standard transformer pipeline through `_monkeypatch_layer()`, which decorates exist
…[truncated 223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T08:01:32.901889+00:00_

Web search results for query: "site:github.com "token filtering" "kv similarity" OR "structured pruning" LLM EMA anchor"

Links: [{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"GitHub - pprp/Awesome-LLM-Prune: Awesome list for LLM pruning. · GitHub","url":"https://github.com/pprp/Awesome-LLM-Prune"},{"title":"Awesome-Efficient-LLM/pruning.md at main · horseee/Awesome-Efficient-LLM","url":"https://github.com/horseee/Awesome-Efficient-LLM/blob/main/pruning.md"},{"title":"GitHub - amazon-science/llm-rank-pruning: LLM-Rank: A graph theoretical approach to structured pruning of large language models based on weighted Page Rank centrality as introduced by the related paper.","url":"https://github.com/amazon-science/llm-rank-pruning"},{"title":"GitHub - AmberLJC/LLMSys-PaperList: Large Language Model (LLM) Systems Paper List · GitHub","url":"https://github.com/AmberLJC/LLMSys-PaperList"},{"title":"GitHub - LumosJiang/Awesome-On-Device-LLMs: [ArXiv 2025] A curated list of papers on on-device large language models, focusing on model compression and system optimization techniques from the survey \"On-Device Large Language Models: A Survey of Model Compression and System Optimization\". · GitHub","url":"https://github.com/LumosJiang/Awesome-On-Device-LLMs"},{"title":"GitHub - ritchieng/the-incredible-pytorch: The Incredible PyTorch: a curated list of tutorials, papers, projects, communities and more relating to PyTorch. · GitHub","url":"https://github.com/ritchieng/the-incredible-pytorch"}]

The web search has returned several results from GitHub repositories that contain curated lists of papers and resources related to LLM compression, pruning, 
…[truncated 1343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T08:01:32.902054+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/teal/grab_acts.py",
  "prompt": "Extract the complete source code. I need to understand how activation histograms are built and how magnitude thresholds are computed from activations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/teal/grab_acts.py",
    "prompt": "Extract the complete source code. I need to understand how activation histograms are built and how magnitude thresholds are computed from activations."
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-12T08:01:32.902173+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/FasterDecoding/TEAL/tree/main/utils",
  "prompt": "List all files in the utils/ directory. I need to find where SparsifyFn and Distribution classes are defined."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/FasterDecoding/TEAL/tree/main/utils",
    "prompt": "List all files in the utils/ directory. I need to find where SparsifyFn and Distribution classes are defined."
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T08:01:32.902288+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gwangeun Byeon OR Yulhwa Kim OR Seokin Hong github \"token filtering\" OR \"kv similarity\" OR \"structured pruning\" code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gwangeun Byeon OR Yulhwa Kim OR Seokin Hong github \"token filtering\" OR \"kv similarity\" OR \"structured pruning\" code"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T08:01:32.902425+00:00_

# Files in the utils/ Directory

Based on the webpage content, the `utils/` directory contains:

1. `__init__.py`
2. `data.py`
3. `eval_ppl.py`
4. `utils.py`
5. `__pycache__/` (directory)

## Finding SparsifyFn and Distribution Classes

The webpage only displays the directory listing and doesn't show the actual code contents. To locate where these classes are defined, you would need to examine the source files directly—likely `utils.py` or `data.py` are the most probable locations. You can click on each file in the GitHub repository to view its contents and search for these class definitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-12T08:01:32.902569+00:00_

# Activation Histogram Building Process

Based on the provided code, here's how the system constructs activation histograms:

## Key Components

**Data Processing:**
The script loads text data from the Alpaca dataset (300 samples), tokenizes it with a maximum sequence length of 2048 tokens, and creates batches of 10.

**Layer-by-Layer Processing:**
The code iterates through each transformer layer sequentially. For each layer, it:

1. Saves hidden state activations to disk before processing
2. Passes activations through the layer's self-attention and MLP modules
3. Calls `find_histogram()` on activation modules to compute statistics
4. Persists histograms via `save_histogram()`
5. Clears activation data from memory

## Histogram Computation Method

The actual threshold calculation isn't shown in this excerpt. The code references `"layer.mlp.activation_module.find_histogram()"` and similar calls, indicating the histogram logic exists in the `activation_module` class definition (not provided here).

Based on context, the process likely:
- Collects neuron activation magnitudes during forward passes
- Computes statistical distributions (histograms)
- Derives magnitude thresholds for sparsity decisions

**Note:** Complete implementation details for threshold computation require examining the `activation_module` class definition in the TEAL model framework referenced but not shown in this code sample.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T08:01:32.902728+00:00_

Web search results for query: "Gwangeun Byeon OR Yulhwa Kim OR Seokin Hong github "token filtering" OR "kv similarity" OR "structured pruning" code"

Links: [{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/html/2512.07090"},{"title":"[2512.07090] Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://arxiv.org/abs/2512.07090"},{"title":"SlimGPT: Layer-wise Structured Pruning for Large Language Models","url":"https://www.researchgate.net/publication/397201574_SlimGPT_Layer-wise_Structured_Pruning_for_Large_Language_Models"},{"title":"Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://www.arxiv.org/pdf/2512.07090"},{"title":"Gyuwan Kim","url":"https://gyuwankim.github.io/"},{"title":"(PDF) Leveraging KV Similarity for Online Structured Pruning in LLMs","url":"https://www.researchgate.net/publication/398476553_Leveraging_KV_Similarity_for_Online_Structured_Pruning_in_LLMs"},{"title":"dblp: Yulhwa Kim","url":"https://dblp.org/pid/223/9434.html"},{"title":"Accuracy (%) on non-reasoning benchmarks. Model IFEval MMLU Pro GPQA... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Accuracy-on-non-reasoning-benchmarks-Model-IFEval-MMLU-Pro-GPQA-MUSR-BBH-Avg_tbl2_397663246"},{"title":"YulhwaKim (Yulhwa Kim) · GitHub","url":"https://github.com/YulhwaKim"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"}]

Based on my search results, I found relevant information about the work by these researchers:

Jungmin Lee, Gwangeun Byeon, Yulhwa Kim, and Seokin Hong from Sungkyunkwan University introduced Token Filtering, a lightweight online structured pruning technique that makes pruning decisions directly during inference without any calibration data. The key idea is to measure
…[truncated 1000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-12T08:01:32.902897+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/YulhwaKim",
  "prompt": "List all repositories. Look for any repository related to token filtering, KV similarity, structured pruning, or LLM inference optimization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/YulhwaKim",
    "prompt": "List all repositories. Look for any repository related to token filtering, KV similarity, structured pruning, or LLM inference optimization."
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-12T08:01:32.903018+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/utils/utils.py",
  "prompt": "Extract the COMPLETE source code. I specifically need the SparsifyFn class and Distribution class implementations - how magnitude thresholds work, how activations are zeroed/masked, and how sparsity ratios translate to thresholds."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/utils/utils.py",
    "prompt": "Extract the COMPLETE source code. I specifically need the SparsifyFn class and Distribution class implementations - how magnitude thresholds work, how activations are zeroed/masked, and how sparsity ratios translate to thresholds."
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-12T08:01:32.903143+00:00_

Based on the GitHub profile content provided, I can see the following repositories listed:

1. **cutlass_tilesparse** - "CUDA templates for tile-sparse matrix multiplication based on CUTLASS"
2. **RRAMScalable_BNN** - "Neural Network-Hardware Co-design for Scalable RRAM-based BNN Accelerators"
3. **SAGE_IMC** - "An open-source framework for the IMC architecture design"
4. **blocksparse** - "Efficient GPU kernels for block-sparse matrix multiplication and convolution"
5. **cutlass** - "CUDA Templates for Linear Algebra Subroutines"
6. **test** - (no description provided)

**Relevant to your search:** The **cutlass_tilesparse** repository appears most directly related to optimization topics you mentioned, focusing on sparse matrix operations. The **blocksparse** repository also addresses sparse computation efficiency. However, none of the repositories explicitly mention token filtering, KV similarity, structured pruning, or LLM inference optimization in their descriptions. The profile shows 13 total repositories, but the page only displays 6 due to a loading error, so additional repositories may exist that aren't visible in this content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T08:01:32.903279+00:00_

# Sparsification Mechanism Analysis

## SparsifyFn Class

The `SparsifyFn` class implements magnitude-based activation sparsification:

**Threshold Computation:**
The class accepts either `init_sparsity` or `init_threshold`. When sparsity is provided, it converts to a threshold via: `thresh = distr.icdf(0.5 + init_sparsity/2)`. This uses the inverse CDF to find the magnitude value that separates the target sparsity percentage.

**Sparsification Process:**
The `apply()` method performs element-wise masking: `x.abs().gt(self.threshold) * x`. This zeros all activations with absolute value below the threshold while preserving larger values.

**Prefill Optimization:**
When sequence length exceeds 1 and prefill is enabled, the forward pass sparsifies only the latter half of context tokens, leaving early tokens intact. This addresses the "prefill sparsification phenomenon."

## Distribution Class

The distribution derives empirical statistics from saved activation histograms:

**CDF/ICDF Mapping:**
The `icdf(q)` method converts quantiles to magnitude thresholds by binary searching cumulative counts. Given a target quantile (e.g., 0.75 for 50% sparsity), it interpolates between bin centers to find the corresponding activation magnitude threshold.

**Implementation Detail:**
`"icdf(0.5 + init_sparsity/2)"` converts sparsity ratios into symmetric quantiles around the median, enabling balanced pruning across positive/negative activation ranges.

The relationship: higher sparsity → higher threshold → more activations zeroed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-12T08:01:32.903468+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/teal/greedyopt.py",
  "prompt": "Extract the complete source code. I need to understand: 1) How greedy optimization allocates sparsity across layers, 2) What the optimization objective is, 3) How per-layer vs per-component sparsity is decided."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/FasterDecoding/TEAL/main/teal/greedyopt.py",
    "prompt": "Extract the complete source code. I need to understand: 1) How greedy optimization allocates sparsity across layers, 2) What the optimization objective is, 3) How per-layer vs per-component sparsity is decided."
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-12T08:01:32.903601+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/FasterDecoding/TEAL/tree/main/models",
  "prompt": "List all subdirectories and files. I need to see which model architectures have pre-calibrated thresholds."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/FasterDecoding/TEAL/tree/main/models",
    "prompt": "List all subdirectories and files. I need to see which model architectures have pre-calibrated thresholds."
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-12T08:01:32.903724+00:00_

# TEAL Models Directory Contents

Based on the GitHub page, the `/models` directory contains the following subdirectories:

- Llama-2-13B
- Llama-2-70B
- Llama-2-7B
- Llama-3-70B
- Llama-3-8B
- Mistral-7B

The page displays these model folders but does not provide details about which ones have "pre-calibrated thresholds." To determine that information, you would need to examine the contents within each model directory, as this view only shows the folder structure without revealing their internal configuration files or documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T08:01:32.903867+00:00_

# Sparsity Optimization Analysis

## 1) Greedy Allocation Mechanism

The script uses **per-layer greedy optimization**. For each layer, it iteratively selects which component (q, k, v, o, gate, up, down) gets the next sparsity increment:

```python
for proj in projs:
    # Try incrementing each projection's sparsity
    # Keep the one producing lowest activation error
    if error < best_error:
        best_proj = proj
sparsities[best_proj] += step_sizes[best_proj]
```

The algorithm picks whichever projection contributes the **least activation error** when sparsified.

## 2) Optimization Objective

The primary goal is minimizing "activation error" — the L2 norm difference between original and sparsified layer outputs:

> "torch.norm(target_acts[:, start_idx:] - new_activations[:, start_idx:], dim=1).mean()"

This is calculated only on the **last 25% of the sequence** by default, focusing on outputs most relevant to predictions.

## 3) Per-Layer vs Per-Component Sparsity

**Per-component sparsity**: Each of 7 projections has independent thresholds adjustable via `set_layer_sparsities()`. Step sizes are **weighted inversely** by model architecture importance:

```python
step_sizes = {proj: base_step_size * (1 / weights[proj]) for proj in projs}
```

**Per-layer constraint**: Effective sparsity across all components is calculated as a weighted average:

> "weighted_sparsity_sum / total_weight"

The loop terminates when this effective metric reaches the target (default 0.9).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-12T08:01:32.904034+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/",
    "description": "Check artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-12T08:01:32.904152+00:00_

Exit code 2
ls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/': No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-12T08:01:32.904270+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/",
  "description": "Create artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/",
    "description": "Create artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-12T08:01:32.904383+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-12T08:01:32.904617+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/code_survey_report.md",
  "content": "# Code Survey: Token Filtering & TEAL\n\n## 1. 代码库信息\n\n| 方法 | 论文 | GitHub |\n|------|------|--------|\n| Token Filtering | [arXiv:2512.07090](https://arxiv.org/abs/2512.07090) \"Leveraging KV Similarity for Online Structured Pruning in LLMs\" | **无公开代码库**（截至2026-05-12，作者 Jungmin Lee / Yulhwa Kim / Seokin Hong，Sungkyunkwan University，未发布代码） |\n| TEAL | [arXiv:2408.14690](https://arxiv.org/abs/2408.14690) \"Training-Free Activation Sparsity in Large Language Models\" (ICLR 2025) | [FasterDecoding/TEAL](https://github.com/FasterDecoding/TEAL)（MIT/Together AI） |\n\n---\n\n## 2. Token Filtering — EMA Similarity 核心算法\n\n> 来源：论文 HTML 版本，无可运行代码。以下为从论文提取的伪代码。\n\n### 2.1 EMA Centroid 更新\n\n```python\n# 对每个 attention head h, 每层 l:\nAnchor_k[l,h] = gamma * Anchor_k[l,h] + (1 - gamma) * k_new[l,h]\nAnchor_v[l,h] = gamma * Anchor_v[l,h] + (1 - gamma) * v_new[l,h]\n```\n\n**默认超参数：γ (gamma) = 0.9**（论文称\"close to one\"，强调近期 token 的影响）\n\n### 2.2 Variance-Aware Similarity Fusion\n\n```python\n# 逐 head 计算 cosine similarity\ns_k = cos_sim(k_new, Anchor_k)  # per head\ns_v = cos_sim(v_new, Anchor_v)  # per head\n\n# 跨 head 计算 running variance\nsigma_k_sq = running_var(s_k, across_heads)\nsigma_v_sq = running_var(s_v, across_heads)\n\n# Variance-aware 权重（低方差侧权重更大）\nalpha = (1/sigma_v_sq) / (1/sigma_k_sq + 1/sigma_v_sq)\n\n# Joint similarity score\nS_KV = alpha * s_k + (1 - alpha) * s_v\n```\n\n**注意：α 不是固定值，而是根据 key/value 方差动态计算的。** 低方差信号更可靠，分配更高权重。\n\n### 2.3 Adaptive Threshold\n\n```python\n# 每层独立的阈值，通过比例反馈动态调整\nT_l = T_l + eta * (P_current - P_tail)\n\n# 其中：\n# P_tail = P_global / Y   (Y=0.5, 即 tail-focused，仅后 50% 的层参与 pruning)\n# eta = small learning rate (论文未给出具体值)\n# P_global = 目标全局 pruning rate\n```\n\n### 2.4 Token Filtering Decision\n\n```python\nif S_KV[token] > T_l:\n    # token 冗余，跳过 attention 计算\n    attention_output[token] = 0  # 直接置零\n    # LayerNorm 仍然执行（residual path 保留）\nelse:\n    # 正常走 attention\n    attention_output[token] = attention(q, k, v)[token]\n```\n\n### 2.5 默认超参数汇总\n\n| 参数 | 值 | 说明 |\n|------|-----|------|\n| γ (EMA decay) | 0.9 | 越接近1越强调历史 |\n| α (key/value权重) | 动态计算 | variance-aware，非固定 |\n| Y (tail ratio) | 0.5 | 仅后半层参与 pruning |\n| η (threshold lr) | 未公开 | 小学习率 |\n| τ (初始阈值) | 未公开 | 逐层自适应 |\n| 支持模型 | LLaMA-2 7B/13B, LLaMA-3 8B, Mistral 7B | 论文实验模型 |\n\n### 2.6 Hook 挂载位置\n\nToken Filtering 层**插入在每个 Transformer block 的 attention 之前**。判断 token 是否冗余后：\n- 冗余 token → 跳过 attention，输出置零，走 skip path\n- 非冗余 token → 正常执行 attention\n\n---\n\n## 3. TEAL — Magnitude-Based Activation Pruning 核心代码\n\n### 3.1 核心 Sparsify 逻辑\n\n```python\n# utils/utils.py — SparsifyFn.apply()\ndef apply(self, x):\n    return x.abs().gt(self.threshold) * x\n    # 绝对值低于 threshold 的激活直接置零\n    # 高于 threshold 的保留原值\n```\n\n### 3.2 Threshold 计算（从 Distribution）\n\n```python\n# threshold 通过 activation histogram 的 inverse CDF 计算\nthreshold = distribution.icdf(0.5 + sparsity / 2)\n\n# 例如 sparsity=0.5 → icdf(0.75)\n# 即找到 75th percentile 的绝对值作为阈值\n# 对称性：正负激活两侧各裁剪 25%\n```\n\n### 3.3 被 Prune 的层和组件\n\n```python\n# self_attn.py — Attention 层\nsparse_fns = {\n    'q': SparsifyFn(distrs['h1']),   # Query input\n    'k': SparsifyFn(distrs['h1']),   # Key input\n    'v': SparsifyFn(distrs['h1']),   # Value input\n    'o': SparsifyFn(distrs['h2'])    # Output projection input\n}\n\n# 应用时机：在 projection 之前\nx_q = sparse_fns['q'](hidden_states)  # 先 sparsify\nquery_states = q_proj(x_q)             # 再 project\n\n# mlp.py — MLP 层\nsparse_fns = {\n    'gate': SparsifyFn(distrs['h1']),  # Gate projection input\n    'up':   SparsifyFn(distrs['h1']),  # Up projection input\n    'down': SparsifyFn(...)            # Down projection input (intermediate)\n}\n```\n\n**关键点：TEAL 在 linear projection 之前 sparsify 输入激活，利用输入稀疏性加速矩阵乘。**\n\n### 3.4 Greedy 逐层优化\n\n```python\n# greedyopt.py — 贪心分配 per-component sparsity\nfor layer in model.layers:\n    while effective_sparsity < target:\n        best_proj, best_error = None, float('inf')\n        for proj in ['q','k','v','o','gate','up','down']:\n            # 尝试增加该 component 的 sparsity\n            error = L2_norm(original_output - sparsified_output)\n            if error < best_error:\n                best_proj, best_error = proj, error\n        sparsities[best_proj] += step_size\n\n# 优化目标：最小化 layer output 的 L2 error\n# 仅计算序列后 25% 的 token (与预测最相关)\n```\n\n### 3.5 默认超参数汇总\n\n| 参数 | 值 | 说明 |\n|------|-----|------|\n| 默认 sparsity | 0.4-0.5 (40-50%) | 模型级全局 sparsity |\n| Calibration 数据 | Alpaca, 300 samples, seq_len=2048 | 用于构建 histogram |\n| Greedy target | 0.9 per-layer effective | 贪心停止条件 |\n| Prefill 策略 | 仅 sparsify 后半段 context tokens | 避免影响 prompt 编码 |\n| 支持模型 | Llama-2 7B/13B/70B, Llama-3 8B/70B, Mistral-7B | 已有预校准 thresholds |\n\n### 3.6 Speedup 结果\n\n| Sparsity | Wall-clock Speedup |\n|----------|-------------------|\n| 40% | 1.53× |\n| 50% | 1.80× |\n\n---\n\n## 4. HuggingFace Transformers 集成方式的关键差异\n\n| 维度 | Token Filtering | TEAL |\n|------|----------------|------|\n| **集成方式** | 在 attention 前插入额外的 filtering 层 | Monkeypatch 替换 forward 方法 |\n| **修改粒度** | Token 级：整个 token 被跳过或保留 | Element 级：单个激活值被置零 |\n| **是否需要校准** | 否（online，推理时自适应） | 是（需要 300 样本 Alpaca 预校准 histogram） |\n| **需要自定义 kernel** | 否（仅跳过计算） | 是（需要 sparse matrix 乘法 kernel 获得 speedup） |\n| **影响的计算** | 仅 attention（MLP 不受影响） | Attention + MLP 的所有 7 个 projection |\n| **阈值来源** | 在线自适应（EMA + variance-aware feedback） | 离线预校准（activation histogram → CDF threshold） |\n| **模型架构改动** | 需要插入新层（Token Filtering layer） | 仅替换 forward 函数，无新层 |\n| **与 quantization 兼容** | 论文未讨论 | 明确兼容（weight quantization） |\n\n---\n\n## 5. Cross-Axis 验证脚本的实现建议\n\n### 5.1 总体架构\n\n两个方法作用在不同轴上：\n- **Token Filtering**：token 轴（哪些 token 参与 attention）\n- **TEAL**：activation element 轴（哪些激活值非零）\n\n组合策略：先做 Token Filtering 减少 token 数，再对剩余 token 的激活做 TEAL magnitude pruning。\n\n### 5.2 实现路径\n\n```python\n# 方案：两阶段 pipeline\nclass CrossAxisPruner:\n    def __init__(self, gamma=0.9, teal_sparsity=0.5, tail_ratio=0.5):\n        self.token_filter = TokenFilter(gamma, tail_ratio)\n        self.teal = TEALSparsifier(teal_sparsity)\n\n    def forward(self, hidden_states, layer_idx, num_layers):\n        # Stage 1: Token Filtering (仅后半层)\n        if layer_idx >= num_layers * (1 - self.token_filter.tail_ratio):\n            mask = self.token_filter.compute_mask(hidden_states)\n            # mask: [batch, seq_len] bool\n        else:\n            mask = torch.ones(batch, seq_len, dtype=torch.bool)\n\n        # Stage 2: TEAL element-wise sparsify (所有层)\n        sparse_hidden = self.teal.apply(hidden_states)\n        # sparse_hidden: same shape, small values zeroed\n\n        # Stage 3: Combine\n        # 被 Token Filter 过滤的 token 不参与 attention\n        # 保留的 token 使用 sparsified activations\n        return sparse_hidden, mask\n```\n\n### 5.3 关键实现注意事项\n\n1. **Token Filtering 需要从零实现**（无公开代码）：\n   - EMA anchor 的初始化：用第一个 token 的 K/V 作为初始 anchor\n   - Running variance 需要 Welford's online algorithm\n   - Threshold 的 η 需要调参（建议从 0.01 开始）\n\n2. **TEAL 可直接复用**：\n   - `pip install` TEAL repo 或 copy `utils/utils.py` 的 `SparsifyFn`\n   - 需要先在目标模型上 run `grab_acts.py` 生成 histogram\n   - 或使用 `models/` 下已有的 Llama/Mistral 预校准 thresholds\n\n3. **验证指标**：\n   - Perplexity（WikiText-2, C4）— 基础质量检查\n   - Commonsense reasoning（ARC, HellaSwag, MMLU）— 功能完整性\n   - Wall-clock latency — 实际 speedup\n   - 分别测 Token Filtering only / TEAL only / Combined，三组对比\n\n4. **风险点**：\n   - Token Filtering 和 TEAL 的 sparsity 可能**不正交**——被 filter 的 token 本身可能也是 TEAL 会 prune 掉的低 magnitude 激活\n   - 需要监控 combined pruning rate 是否超过有效阈值\n   - Prefill 阶段两者行为不同（Token Filtering 不适用 prefill，TEAL 对 prefill 后半段生效）\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/code_survey_report.md",
    "content": "# Code Survey: Token Filtering & TEAL\n\n## 1. 代码库信息\n\n| 方法 | 论文 | GitHub |\n|------|------|--------|\n| Token Filtering | [arXiv:2512.07090](https://arxiv.org/abs/2512.07090) \"Leveraging KV Similarity for Online Structured Pruning in LLMs\" | **无公开代码库**（截至2026-05-12，作者 Jungmin Lee / Yulhwa Kim / Seokin Hong，Sungkyunkwan University，未发布代码） |\n| TEAL | [arXiv:2408.14690](https://arxiv.org/abs/2408.14690) \"Training-Free Activation Sparsity in Large Language Models\" (ICLR 2025) | [FasterDecoding/TEAL](https://github.com/FasterDecoding/TEAL)（MIT/Together AI） |\n\n---\n\n## 2. Token Filtering — EMA Similarity 核心算法\n\n> 来源：论文 HTML 版本，无可运行代码。以下为从论文提取的伪代码。\n\n### 2.1 EMA Centroid 更新\n\n```python\n# 对每个 attention head h, 每层 l:\nAnchor_k[l,h] = gamma * Anchor_k[l,h] + (1 - gamma) * k_new[l,h]\nAnchor_v[l,h] = gamma * Anchor_v[l,h] + (1 - gamma) * v_new[l,h]\n```\n\n**默认超参数：γ (gamma) = 0.9**（论文称\"close to one\"，强调近期 token 的影响）\n\n### 2.2 Variance-Aware Similarity Fusion\n\n```python\n# 逐 head 计算 cosine similarity\ns_k = cos_sim(k_new, Anchor_k)  # per head\ns_v = cos_sim(v_new, Anchor_v)  # per head\n\n# 跨 head 计算 running variance\nsigma_k_sq = running_var(s_k, across_heads)\nsigma_v_sq = running_var(s_v, across_heads)\n\n# Variance-aware 权重（低方差侧权重更大）\nalpha = (1/sigma_v_sq) / (1/sigma_k_sq + 1/sigma_v_sq)\n\n# Joint similarity score\nS_KV = alpha * s_k + (1 - alpha) * s_v\n```\n\n**注意：α 不是固定值，而是根据 key/value 方差动态计算的。** 低方差信号更可靠，分配更高权重。\n\n### 2.3 Adaptive Threshold\n\n```python\n# 每层独立的阈值，通过比例反馈动态调整\nT_l = T_l + eta * (P_current - P_tail)\n\n# 其中：\n# P_tail = P_global / Y   (Y=0.5, 即 tail-focused，仅后 50% 的层参与 pruning)\n# eta = small learning rate (论文未给出具体值)\n# P_global = 目标全局 pruning rate\n```\n\n### 2.4 Token Filtering Decision\n\n```python\nif S_KV[token] > T_l:\n    # token 冗余，跳过 attention 计算\n    attention_output[token] = 0  # 直接置零\n    # LayerNorm 仍然执行（residual path 保留）\nelse:\n    # 正常走 attention\n    attention_output[token] = attention(q, k, v)[token]\n```\n\n### 2.5 默认超参数汇总\n\n| 参数 | 值 | 说明 |\n|------|-----|------|\n| γ (EMA decay) | 0.9 | 越接近1越强调历史 |\n| α (key/value权重) | 动态计算 | variance-aware，非固定 |\n| Y (tail ratio) | 0.5 | 仅后半层参与 pruning |\n| η (threshold lr) | 未公开 | 小学习率 |\n| τ (初始阈值) | 未公开 | 逐层自适应 |\n| 支持模型 | LLaMA-2 7B/13B, LLaMA-3 8B, Mistral 7B | 论文实验模型 |\n\n### 2.6 Hook 挂载位置\n\nToken Filtering 层**插入在每个 Transformer block 的 attention 之前**。判断 token 是否冗余后：\n- 冗余 token → 跳过 attention，输出置零，走 skip path\n- 非冗余 token → 正常执行 attention\n\n---\n\n## 3. TEAL — Magnitude-Based Activation Pruning 核心代码\n\n### 3.1 核心 Sparsify 逻辑\n\n```python\n# utils/utils.py — SparsifyFn.apply()\ndef apply(self, x):\n    return x.abs().gt(self.threshold) * x\n    # 绝对值低于 threshold 的激活直接置零\n    # 高于 threshold 的保留原值\n```\n\n### 3.2 Threshold 计算（从 Distribution）\n\n```python\n# threshold 通过 activation histogram 的 inverse CDF 计算\nthreshold = distribution.icdf(0.5 + sparsity / 2)\n\n# 例如 sparsity=0.5 → icdf(0.75)\n# 即找到 75th percentile 的绝对值作为阈值\n# 对称性：正负激活两侧各裁剪 25%\n```\n\n### 3.3 被 Prune 的层和组件\n\n```python\n# self_attn.py — Attention 层\nsparse_fns = {\n    'q': SparsifyFn(distrs['h1']),   # Query input\n    'k': SparsifyFn(distrs['h1']),   # Key input\n    'v': SparsifyFn(distrs['h1']),   # Value input\n    'o': SparsifyFn(distrs['h2'])    # Output projection input\n}\n\n# 应用时机：在 projection 之前\nx_q = sparse_fns['q'](hidden_states)  # 先 sparsify\nquery_states = q_proj(x_q)             # 再 project\n\n# mlp.py — MLP 层\nsparse_fns = {\n    'gate': SparsifyFn(distrs['h1']),  # Gate projection input\n    'up':   SparsifyFn(distrs['h1']),  # Up projection input\n    'down': SparsifyFn(...)            # Down projection input (intermediate)\n}\n```\n\n**关键点：TEAL 在 linear projection 之前 sparsify 输入激活，利用输入稀疏性加速矩阵乘。**\n\n### 3.4 Greedy 逐层优化\n\n```python\n# greedyopt.py — 贪心分配 per-component sparsity\nfor layer in model.layers:\n    while effective_sparsity < target:\n        best_proj, best_error = None, float('inf')\n        for proj in ['q','k','v','o','gate','up','down']:\n            # 尝试增加该 component 的 sparsity\n            error = L2_norm(original_output - sparsified_output)\n            if error < best_error:\n                best_proj, best_error = proj, error\n        sparsities[best_proj] += step_size\n\n# 优化目标：最小化 layer output 的 L2 error\n# 仅计算序列后 25% 的 token (与预测最相关)\n```\n\n### 3.5 默认超参数汇总\n\n| 参数 | 值 | 说明 |\n|------|-----|------|\n| 默认 sparsity | 0.4-0.5 (40-50%) | 模型级全局 sparsity |\n| Calibration 数据 | Alpaca, 300 samples, seq_len=2048 | 用于构建 histogram |\n| Greedy target | 0.9 per-layer effective | 贪心停止条件 |\n| Prefill 策略 | 仅 sparsify 后半段 context tokens | 避免影响 prompt 编码 |\n| 支持模型 | Llama-2 7B/13B/70B, Llama-3 8B/70B, Mistral-7B | 已有预校准 thresholds |\n\n### 3.6 Speedup 结果\n\n| Sparsity | Wall-clock Speedup |\n|----------|-------------------|\n| 40% | 1.53× |\n| 50% | 1.80× |\n\n---\n\n## 4. HuggingFace Transformers 集成方式的关键差异\n\n| 维度 | Token Filtering | TEAL |\n|------|----------------|------|\n| **集成方式** | 在 attention 前插入额外的 filtering 层 | Monkeypatch 替换 forward 方法 |\n| **修改粒度** | Token 级：整个 token 被跳过或保留 | Element 级：单个激活值被置零 |\n| **是否需要校准** | 否（online，推理时自适应） | 是（需要 300 样本 Alpaca 预校准 histogram） |\n| **需要自定义 kernel** | 否（仅跳过计算） | 是（需要 sparse matrix 乘法 kernel 获得 speedup） |\n| **影响的计算** | 仅 attention（MLP 不受影响） | Attention + MLP 的所有 7 个 projection |\n| **阈值来源** | 在线自适应（EMA + variance-aware feedback） | 离线预校准（activation histogram → CDF threshold） |\n| **模型架构改动** | 需要插入新层（Token Filtering layer） | 仅替换 forward 函数，无新层 |\n| **与 quantization 兼容** | 论文未讨论 | 明确兼容（weight quantization） |\n\n---\n\n## 5. Cross-Axis 验证脚本的实现建议\n\n### 5.1 总体架构\n\n两个方法作用在不同轴上：\n- **Token Filtering**：token 轴（哪些 token 参与 attention）\n- **TEAL**：activation element 轴（哪些激活值非零）\n\n组合策略：先做 Token Filtering 减少 token 数，再对剩余 token 的激活做 TEAL magnitude pruning。\n\n### 5.2 实现路径\n\n```python\n# 方案：两阶段 pipeline\nclass CrossAxisPruner:\n    def __init__(self, gamma=0.9, teal_sparsity=0.5, tail_ratio=0.5):\n        self.token_filter = TokenFilter(gamma, tail_ratio)\n        self.teal = TEALSparsifier(teal_sparsity)\n\n    def forward(self, hidden_states, layer_idx, num_layers):\n        # Stage 1: Token Filtering (仅后半层)\n        if layer_idx >= num_layers * (1 - self.token_filter.tail_ratio):\n            mask = self.token_filter.compute_mask(hidden_states)\n            # mask: [batch, seq_len] bool\n        else:\n            mask = torch.ones(batch, seq_len, dtype=torch.bool)\n\n        # Stage 2: TEAL element-wise sparsify (所有层)\n        sparse_hidden = self.teal.apply(hidden_states)\n        # sparse_hidden: same shape, small values zeroed\n\n        # Stage 3: Combine\n        # 被 Token Filter 过滤的 token 不参与 attention\n        # 保留的 token 使用 sparsified activations\n        return sparse_hidden, mask\n```\n\n### 5.3 关键实现注意事项\n\n1. **Token Filtering 需要从零实现**（无公开代码）：\n   - EMA anchor 的初始化：用第一个 token 的 K/V 作为初始 anchor\n   - Running variance 需要 Welford's online algorithm\n   - Threshold 的 η 需要调参（建议从 0.01 开始）\n\n2. **TEAL 可直接复用**：\n   - `pip install` TEAL repo 或 copy `utils/utils.py` 的 `SparsifyFn`\n   - 需要先在目标模型上 run `grab_acts.py` 生成 histogram\n   - 或使用 `models/` 下已有的 Llama/Mistral 预校准 thresholds\n\n3. **验证指标**：\n   - Perplexity（WikiText-2, C4）— 基础质量检查\n   - Commonsense reasoning（ARC, HellaSwag, MMLU）— 功能完整性\n   - Wall-clock latency — 实际 speedup\n   - 分别测 Token Filtering only / TEAL only / Combined，三组对比\n\n4. **风险点**：\n   - Token Filtering 和 TEAL 的 sparsity 可能**不正交**——被 filter 的 token 本身可能也是 TEAL 会 prune 掉的低 magnitude 激活\n   - 需要监控 combined pruning rate 是否超过有效阈值\n   - Prefill 阶段两者行为不同（Token Filtering 不适用 prefill，TEAL 对 prefill 后半段生效）\n"
  }
}
````

</details>

---

### Tool result

_source line 48 · 2026-05-12T08:01:32.904858+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/code_survey_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-12T08:01:32.904988+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "code_survey_report",
  "type": "report",
  "description": "Token Filtering (arXiv:2512.07090) 与 TEAL (ICLR 2025) 代码库调研报告：EMA similarity 算法、magnitude-based pruning 核心实现、默认超参数、HF 集成差异、cross-axis 验证建议",
  "project": "solver-verified-formalizer-rl",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/code_survey_report.md",
  "tags": "['token-filtering', 'teal', 'kv-cache', 'activation-pruning', 'code-survey']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "code_survey_report",
    "type": "report",
    "description": "Token Filtering (arXiv:2512.07090) 与 TEAL (ICLR 2025) 代码库调研报告：EMA similarity 算法、magnitude-based pruning 核心实现、默认超参数、HF 集成差异、cross-axis 验证建议",
    "project": "solver-verified-formalizer-rl",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/code_survey_report.md",
    "tags": "['token-filtering', 'teal', 'kv-cache', 'activation-pruning', 'code-survey']"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-12T08:01:32.905139+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_f360d5\", \"name\": \"code_survey_report\", \"type\": \"report\", \"description\": \"Token Filtering (arXiv:2512.07090) 与 TEAL (ICLR 2025) 代码库调研报告：EMA similarity 算法、magnitude-based pruning 核心实现、默认超参数、HF 集成差异、cross-axis 验证建议\", \"path\": \"projects/solver-verified-formalizer-rl/artifacts/_project/report/code_survey_report.md\", \"url\": null, \"project\": \"solver-verified-formalizer-rl\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T08:01:23.458920+00:00\", \"tags\": [\"token-filtering\", \"teal\", \"kv-cache\", \"activation-pruning\", \"code-survey\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_code-survey_20260512T075744",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-12T08:01:32.905307+00:00_

报告已完成并注册（`art_20260512_f360d5`）。

核心发现：

- **Token Filtering**：无公开代码库。算法从论文提取——EMA centroid（γ=0.9）+ variance-aware fusion（α动态计算）+ adaptive threshold，仅作用于后50%层的 attention token 轴。需从零实现。
- **TEAL**：[FasterDecoding/TEAL](https://github.com/FasterDecoding/TEAL) 代码完整。核心一行 `x.abs().gt(threshold) * x`，threshold 通过 activation histogram 的 inverse CDF 获得。Monkeypatch 方式集成 HF 模型，sparsify 所有 7 个 projection 的输入激活，默认 40-50% sparsity。
- **关键差异**：Token Filtering 是 token 粒度的在线过滤（无需校准），TEAL 是 element 粒度的离线校准 pruning。两者作用轴正交，可组合但需监控 combined pruning rate 防止过度稀疏。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_code-survey_20260512T075744"
}
```

</details>

---
