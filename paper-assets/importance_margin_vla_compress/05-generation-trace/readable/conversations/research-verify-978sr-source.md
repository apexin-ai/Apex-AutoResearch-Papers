# research verify 978sr source

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_research_verify_978sr_source_20260519T062742.jsonl`
- **Structured JSON:** [`ae4838cf3d2601120ad3.json`](../../sessions/ae/ae4838cf3d2601120ad3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-19T06:31:56.754057+00:00_

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
  "session": "worker_research_verify_978sr_source_20260519T062742",
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

_source line 2 · 2026-05-19T06:31:56.754472+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T06:31:56.754680+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CogACT 97.8% success rate pruning VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CogACT 97.8% success rate pruning VLA"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T06:31:56.754815+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA-IAP CogACT 97.8 pruning arXiv 2603.22991"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA-IAP CogACT 97.8 pruning arXiv 2603.22991"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T06:31:56.754937+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EfficientVLA CogACT 97.8 pruning arXiv 2506.10100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EfficientVLA CogACT 97.8 pruning arXiv 2506.10100"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T06:31:56.755056+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CogACT robot manipulation model paper arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CogACT robot manipulation model paper arXiv"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T06:31:56.755239+00:00_

Web search results for query: "CogACT 97.8% success rate pruning VLA"

Links: [{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22991"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/pdf/2510.08464"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://cogact.github.io/"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/html/2411.19650v1"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.10100"},{"title":"SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models","url":"https://arxiv.org/html/2509.09090"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing   Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/pdf/2411.19650"}]

Based on the search results, I found information related to your query:

The VLA-IAP (Vision-Language-Action Interaction-Aligned Pruning) method achieves a 97.8% success rate with a 1.25× speedup on the LIBERO benchmark. However, the search results show that VLA-IAP, not CogACT, is the model achieving this specific 97.8% success rate with pruning.

The search r
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T06:31:56.755415+00:00_

Web search results for query: "VLA-IAP CogACT 97.8 pruning arXiv 2603.22991"

Links: [{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22991"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"}]

Based on the search results, here's what I found about the arXiv paper 2603.22991:

VLA-IAP is a training-free visual token pruning method that introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.

The method addresses the fact that as model capacity and visual context length grow, the inference cost of VLA (Vision-Language-Action) systems becomes a major bottleneck for real-world deployment on resource-constrained platforms.

VLA-IAP achieves a 97.8% success rate with a 1.25× speedup on the LIBERO benchmark, and up to 1.54× speedup while maintaining comparable performance.

The paper was published on March 24, 2026, and represents work on making Vision-Language-Action models more efficient for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T06:31:56.755592+00:00_

Web search results for query: "CogACT robot manipulation model paper arXiv"

Links: [{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://cogact.github.io/"},{"title":"[2411.19650] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650"},{"title":"[2411.19650v1] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650v1"},{"title":"(PDF) CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://www.researchgate.net/publication/386335138_CogACT_A_Foundational_Vision-Language-Action_Model_for_Synergizing_Cognition_and_Action_in_Robotic_Manipulation"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/html/2411.19650v1"},{"title":"CogACT/CogACT-Large · Hugging Face","url":"https://huggingface.co/CogACT/CogACT-Large"},{"title":"GitHub - microsoft/CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://github.com/microsoft/CogACT"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing   Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/pdf/2411.19650"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241119650L/abstract"}]

I found the paper you're looking for! Here's the information about the CogACT robot manipulation model:

**Paper Details:**

CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation is available on arXiv (2411
…[truncated 926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T06:31:56.755758+00:00_

Web search results for query: "EfficientVLA CogACT 97.8 pruning arXiv 2506.10100"

Links: [{"title":"[2506.10100] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"Paper page - EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"}]

Based on the search results, I found information about the paper you're looking for:

EfficientVLA is a structured and training-free inference acceleration framework that systematically eliminates computational barriers by exploiting multifaceted redundancies.

The framework synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features.

When applied to th
…[truncated 465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T06:31:56.755945+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22991v1",
  "prompt": "Find the exact table or section that reports 97.8% success rate. What model is being pruned (is it CogACT)? What is the pruning ratio? What benchmark is used? List all relevant numbers from the table including the pruning ratio, token retention ratio, success rate, and speedup. Also check if \"78% pruning\" or \"22% token retention\" or similar numbers appear."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2603.22991v1",
    "prompt": "Find the exact table or section that reports 97.8% success rate. What model is being pruned (is it CogACT)? What is the pruning ratio? What benchmark is used? List all relevant numbers from the table including the pruning ratio, token retention ratio, success rate, and speedup. Also check if \"78% pruning\" or \"22% token retention\" or similar numbers appear."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T06:31:56.756078+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2506.10100v1",
  "prompt": "Find all tables and results related to CogACT. What success rates does CogACT achieve with and without pruning/compression? Is there any mention of 97.8% success rate? What pruning ratios are used? List all CogACT-related numbers from tables, including success rates, pruning ratios, speedups, and FLOPs reductions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2506.10100v1",
    "prompt": "Find all tables and results related to CogACT. What success rates does CogACT achieve with and without pruning/compression? Is there any mention of 97.8% success rate? What pruning ratios are used? List all CogACT-related numbers from tables, including success rates, pruning ratios, speedups, and FLOPs reductions."
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T06:31:56.756234+00:00_

# Analysis of 97.8% Success Rate Finding

The 97.8% success rate appears in **Table 2** (OpenVLA-OFT Results on LIBERO Benchmark), not involving CogACT.

## Key Details:

**Model being pruned:** OpenVLA-OFT (7B backbone)

**Specific configuration:**
- Token retention ratio: 70%
- Pruning ratio: 30%
- Success rate: 97.8%
- Speedup: 1.25×
- Benchmark: LIBERO (spatial variation)

The paper states: "VLA-IAP achieves a state-of-the-art 97.8% success rate with a 1.25×speedup" on LIBERO with 70% token retention.

**Important note:** The abstract also mentions "97.8% success rate" but this refers to the unpruned baseline performance level that VLA-IAP maintains under compression, not a standalone result.

Under more aggressive 30% token retention (70% pruning), VLA-IAP achieves 97.1% average success with 1.54× speedup on the same model and benchmark.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T06:31:56.756390+00:00_

# CogACT Performance Data from EfficientVLA Paper

## Baseline CogACT Results (Without Compression)

**Visual Matching Setting:**
- Pick Coke Can: 91.3%
- Move Near: 85.0%
- Drawer: 71.8%
- Drawer Apple: 50.9%
- Average: 74.8%
- FLOPs: 100.0% (4.19T)
- Speedup: 1.00×
- Inference time: 0.2342s

**Variant Aggregation Setting:**
- Pick Coke Can: 89.6%
- Move Near: 80.8%
- Drawer: 28.3%
- Drawer Apple: 46.6%
- Average: 61.3%

## EfficientVLA Results (With Pruning)

**Best configuration (L=22, T=56):**
- Visual Matching average: 74.2% (0.6 percentage point drop)
- FLOPs: 28.9% of baseline
- Speedup: 1.93×

**There is no mention of 97.8% success rate** in the document.

## Pruning Ratios Applied

The paper specifies: "pruning 36% of parameters" and reducing visual tokens from 256 to 56 (78% reduction). The language module was reduced from 28 to 22 layers (21% layer reduction), with 25% MLP sparsity applied to remaining layers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T06:31:56.756574+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CogACT LIBERO benchmark success rate results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CogACT LIBERO benchmark success rate results"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T06:31:56.756700+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CogACT\" \"97.8\" OR \"97.8%\" success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CogACT\" \"97.8\" OR \"97.8%\" success rate"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T06:31:56.756837+00:00_

Web search results for query: "CogACT LIBERO benchmark success rate results"

Links: [{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation ...","url":"https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.13626"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://vla-cache.github.io/"}]

Based on the search results, I found some information about CogACT and LIBERO benchmark performance:

CogACT was tested within the context of VLA-Cache acceleration methods in the SIMPLER environment. The search results mention CogACT as a baseline model in robotic manipulation research, but the specific success rate results for CogACT on the LIBERO benchmark are not explicitly detailed in these particular sources.

However, the search results do provide context about LIBERO benchmark performance more generally: Models achieving success rates above 90% on the standard LIBERO benc
…[truncated 554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T06:31:56.757025+00:00_

Web search results for query: ""CogACT" "97.8" OR "97.8%" success rate"

Links: [{"title":"(PDF) CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://www.researchgate.net/publication/386335138_CogACT_A_Foundational_Vision-Language-Action_Model_for_Synergizing_Cognition_and_Action_in_Robotic_Manipulation"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://cogact.github.io/"},{"title":"Success rates in simulation scenario with CogACT and Octo model for... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rates-in-simulation-scenario-with-CogACT-and-Octo-model-for-picking-the-spoons_fig3_394488738"},{"title":"Test‐retest reliability and feasibility of web‐based cognitive assessment cCOG","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12741035/"},{"title":"Long COVID Brain Fog Treatment: Findings from a Pilot Randomized Controlled Trial of Constraint-Induced Cognitive Therapy","url":"https://www.medrxiv.org/content/10.1101/2024.07.04.24309908.full.pdf"},{"title":"Performance of central venous catheterization by medical students: a retrospective study of students’ logbooks","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4142460/"},{"title":"Evidence of an optimal error rate for motor skill learning","url":"https://www.biorxiv.org/content/10.1101/2023.07.19.549705.full.pdf"}]

Based on the search results, I found information about CogACT, which is a foundational vision-language-action model for robotic manipulation. However, the search results do not contain any reference to a "97.8%" or "97.8" success rate for CogACT.

The search results show various success rates for CogACT in different contexts, such as DiT-Large achieving an average success rate of 64.8%, and average success rates of 74.8% in Visual Matching and 61.3% in Variant Aggregation. However, none of the re
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T06:31:56.757258+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find 97.8% claim in paper",
  "prompt": "Search the project directory /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress for any mention of \"97.8\" in any file (tex, md, txt, yaml, etc.). Also search for \"CogACT\" mentions. I need to find the exact wording of the claim about \"CogACT achieves 97.8% SR under 78% pruning\" and its context. Report the exact file path, line numbers, and surrounding text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find 97.8% claim in paper",
    "prompt": "Search the project directory /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress for any mention of \"97.8\" in any file (tex, md, txt, yaml, etc.). Also search for \"CogACT\" mentions. I need to find the exact wording of the claim about \"CogACT achieves 97.8% SR under 78% pruning\" and its context. Report the exact file path, line numbers, and surrounding text."
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T06:31:56.757431+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22991v1",
  "prompt": "List ALL models tested in this paper (VLA-IAP). Specifically, was CogACT tested? List every table and what models appear in each table. For Table 2, list ALL rows with their model name, pruning ratio, success rate, and speedup. I need to know if CogACT appears anywhere in this paper with a 97.8% success rate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2603.22991v1",
    "prompt": "List ALL models tested in this paper (VLA-IAP). Specifically, was CogACT tested? List every table and what models appear in each table. For Table 2, list ALL rows with their model name, pruning ratio, success rate, and speedup. I need to know if CogACT appears anywhere in this paper with a 97.8% success rate."
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T06:31:56.757567+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "97\\.8",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "output_mode": "content",
  "context": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Grep",
  "tool_args": {
    "pattern": "97\\.8",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
    "output_mode": "content",
    "context": "5"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T06:31:56.757699+00:00_

# VLA Models Tested in VLA-IAP Paper

## All Models Tested:
- OpenVLA-OFT
- DreamVLA
- π₀ (Pi-0)
- π₀.₅ (Pi-0.5)
- CogACT (appears in Table 2 only)

## Table-by-Table Model Breakdown:

**Table 1:** DreamVLA, π₀, π₀.₅

**Table 2 (OpenVLA-OFT Results):**
- Part I lists multiple models including CogACT
- Part II shows pruning methods applied to OFT (7B) backbone

**Table 3-4:** OpenVLA-OFT

**Table 5:** π₀.₅

**Table 6:** DreamVLA, π₀

## CogACT Clarification:

CogACT **does not appear as a pruning method** with the 97.8% result. In Table 2, Part I, "CogACT (CogVLM 7B)" shows a baseline 93.6% success rate without pruning applied.

The **97.8% success rate** mentioned in the abstract and main results specifically refers to "OpenVLA-OFT (OFT 7B)" with VLA-IAP pruning at 70% token retention ratio, not CogACT.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T06:31:56.757844+00:00_

&lt;persisted-output>
Output too large (44.5KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/7f0e13aa-6aba-4b51-96d1-db2429e8525f/tool-results/toolu_017AYsdHjhFDwABFeocKuiip.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-98-
paper_framing.md-99-### RC4: Smart compression — is re-encoding or compression the mechanism?
paper_framing.md-100-**Response**: M=128 passthrough control definitively answers this. M=128 (no compression) = 59.8% vs M=32 (75% compression) = 61.6%. The +15pp over baseline comes from re-encoding; compression is a free bonus. CI overlap between M=128 and M=32/64 confirms compression adds negligible benefit.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-101-
paper_framing.md-102-### RC5: Relationship to VLA-IAP
paper_framing.md:103:**Response**: VLA-IAP's 97.8% on OpenVLA is consistent with our finding: MLP projector preserves token independence. VLA-IAP untested on pixel_shuffle VLAs; our geometric prior experiments (0%) predict it would fail.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-104-
paper_framing.md-105-### RC6: Is this just "different models behave differently"?
paper_framing.md-106-**Response**: We identify the specific mechanism (pixel_shuffle spatial folding) and provide evidence for WHY. Concrete design implications: future VLAs wanting efficiency should avoid pixel_shuffle or include learned re-encoding modules.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-107-
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-108-## All Experimental Evidence (confirmed)
--
decisions.yaml-1129-- id: D066
decisions.yaml
…[truncated 295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T06:31:56.758016+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "CogACT",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "output_mode": "content",
  "context": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Grep",
  "tool_args": {
    "pattern": "CogACT",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
    "output_mode": "content",
    "context": "5"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T06:31:56.758170+00:00_

&lt;persisted-output>
Output too large (27.9KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/7f0e13aa-6aba-4b51-96d1-db2429e8525f/tool-results/toolu_01FbQCxfxLqfsJSGF9PGM67c.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-6-
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-7-## Title (working)
paper_framing.md-8-"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-9-
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-10-## Core Insight
paper_framing.md:11:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-12-
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-13-## Paper Identity (Round 2 Reframing, 2026-05-19)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-14-[Omitted long context line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-15-
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-16-## Core Claims (4, all confirmed)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md-17-
paper_framing.md-18-### Claim 1: Architecture-Dependent Compressibility
paper_framing.md-19-Token pruning robustness in VLAs is strongly linked to the vision connector architecture. Under identical 50% random token removal:
paper_framing.md-20-
…[truncated 234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T06:31:56.758344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md",
  "offset": "95",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md",
    "offset": "95",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T06:31:56.758518+00:00_

95	
96	### RC3: Why not test SmolVLA without pixel_shuffle?
97	**Response**: SmolVLA's connector is integral (LLM expects 128 tokens, not 1024). Removing it requires retraining from scratch. OpenVLA comparison isolates the connector's role.
98	
99	### RC4: Smart compression — is re-encoding or compression the mechanism?
100	**Response**: M=128 passthrough control definitively answers this. M=128 (no compression) = 59.8% vs M=32 (75% compression) = 61.6%. The +15pp over baseline comes from re-encoding; compression is a free bonus. CI overlap between M=128 and M=32/64 confirms compression adds negligible benefit.
101	
102	### RC5: Relationship to VLA-IAP
103	**Response**: VLA-IAP's 97.8% on OpenVLA is consistent with our finding: MLP projector preserves token independence. VLA-IAP untested on pixel_shuffle VLAs; our geometric prior experiments (0%) predict it would fail.
104	
105	### RC6: Is this just "different models behave differently"?
106	**Response**: We identify the specific mechanism (pixel_shuffle spatial folding) and provide evidence for WHY. Concrete design implications: future VLAs wanting efficiency should avoid pixel_shuffle or include learned re-encoding modules.
107	
108	## All Experimental Evidence (confirmed)
109	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T06:31:56.758674+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"CogACT\\|78%\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress --include=\"*.md\" --include=\"*.tex\" --include=\"*.txt\" --include=\"*.yaml\" 2>/dev/null | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"CogACT\\|78%\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress --include=\"*.md\" --include=\"*.tex\" --include=\"*.txt\" --include=\"*.yaml\" 2>/dev/null | head -50"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T06:31:56.758836+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex:\item \textbf{Architecture-dependent compressibility} (\S\ref{sec:results}): Pixel-shuffle connectors exhibit cliff-edge failure (59.2\% $\to$ 0\%); MLP projectors degrade gracefully (74.0\% $\to$ 37.4\%), consistent with independent findings on CogACT (EfficientVLA~\cite{yang2025efficientvla}).
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex:Vision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is strongly linked to connector architecture. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\% to 0\% on the official checkpoint, even at 5\% token removal. This failure is robust across seven pruning configurations and three mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully under the same conditions. The divergence co-occurs with differences in token information density: pixel-shuffle produces tokens with near-uniform attention, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: a cross-attention module raises success rate above the uncompressed baseline even at 75\% token reduction, and a passthrough control isolates re-encoding as the causal factor. These findings, consistent with independent results on CogACT, suggest that VLA token compressibility is architecture-depend
…[truncated 12819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T06:31:56.758992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex",
  "offset": "1",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex",
    "offset": "1",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T06:31:56.759172+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Disentangling Connector Design from Model Scale}
5	\label{sec:scale_confound}
6	
7	Our cross-architecture comparison confounds the vision connector design (pixel-shuffle vs.\ MLP projector) with model scale (0.5B vs.\ 7B parameters). A larger model has more capacity to absorb perturbations through its deeper and wider attention layers, raising the question of whether SmolVLA's cliff-edge reflects architectural fragility or simply insufficient model capacity.
8	
9	Four lines of evidence favor the connector-level explanation. First, the official SmolVLA checkpoint (59.2\% SR baseline) exhibits the same cliff-edge under 50\% random pruning (0/500, 0.0\% SR), ruling out the possibility that our fine-tuned model's lower baseline (44.8\%) reflects undertrained weights that are unusually fragile. Second, SmolVLA collapses at $k = 0.95$, where only 7 of 128 tokens (5.5\%) are removed. A capacity-limited model that can solve the task with all tokens should not fail catastrophically when 95\% of the input is preserved; the perturbation is too small relative to the model's demonstrated capability. Third, the attention entropy ratio difference (0.98 vs.\ 0.64) is an architectural measurement, not a capacity measurement. SmolVLA's near-uniform attention distribution reflects the pixel-shuffle connector's output structure: because each token encodes 16 patches via channel concatenation, the resulting tokens are uniformly information-dense, and the downstream LLM has no basis for developing selective attention. OpenVLA's sharply non-uniform attention in deep layers reflects the MLP projector's preservation of per-patch granularity, which allows the model to learn which spatial locations carry task-relevant information. Fourth, the pixel-shuffle operation itself provides a mechanistic explanation: $4 \times 4$ spatial folding creates tokens whose meaning depends on the complete $4 \times 4$ grid, and removing any toke
…[truncated 10761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T06:31:56.759340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_provenance.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_provenance.yaml"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T06:31:56.759620+00:00_

1	paper:
2	  title: ''
3	  version: 56
4	  generated_at: '2026-05-19T00:58:16.680820+00:00'
5	claims:
6	- id: C001
7	  location:
8	    section: experiments
9	    paragraph: 0
10	    sentence: 0
11	  text: All six pruning conditions produce 0% SR vs 44.8% baseline
12	  type: quantitative
13	  evidence:
14	  - exp_id: eval_stage1_only
15	    metric: overall_success_rate
16	  - exp_id: eval_stage1only_object_v2_fixed
17	    metric: overall_success_rate
18	  decisions: []
19	  deprecated: false
20	- id: C003
21	  location:
22	    section: experiments
23	    paragraph: 0
24	    sentence: 0
25	  text: 'Cross-suite cliff-edge: Object 0%, Spatial 0%, Goal 0%'
26	  type: quantitative
27	  evidence:
28	  - exp_id: eval_spatial_prune_k05
29	    metric: overall_sr
30	  - exp_id: eval_goal_prune_k05
31	    metric: overall_sr
32	  decisions: []
33	  deprecated: false
34	- id: C004
35	  location:
36	    section: analysis
37	    paragraph: 0
38	    sentence: 0
39	  text: Attention entropy ratio 0.98
40	  type: quantitative
41	  evidence:
42	  - exp_id: attention_entropy_analysis
43	    metric: entropy_ratio
44	  decisions: []
45	  deprecated: true
46	- id: C005
47	  location:
48	    section: analysis
49	    paragraph: 0
50	    sentence: 0
51	  text: Attention entropy ratio reaches 0.98 (6.86/7.0 bits), Gini coefficient 0.246
52	  type: quantitative
53	  evidence:
54	  - exp_id: attention_entropy_analysis
55	    metric: entropy_ratio
56	  decisions: []
57	  deprecated: true
58	- id: C007
59	  location:
60	    section: analysis
61	    paragraph: 0
62	    sentence: 0
63	  text: Single-step L2 increases from 0.414 to 1.391 (3.4x degradation), relative
64	    error 111.5%
65	  type: quantitative
66	  evidence:
67	  - exp_id: offline_singlestep_action_error
68	    metric: l2_distance
69	  decisions: []
70	  deprecated: true
71	- id: C010
72	  location:
73	    section: analysis
74	    paragraph: 0
75	    sentence: 0
76	  text: Gripper error 1.02 indicates complete inversion
77	  type: qua
…[truncated 43321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T06:31:56.759778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
  "offset": "1",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
    "offset": "1",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T06:31:56.759929+00:00_

1	\section{Analysis and Discussion}
2	\label{sec:analysis}
3	
4	\subsection{Connector Design and Compressibility}
5	\label{sec:pixel_shuffle}
6	
7	The divergence between SmolVLA and OpenVLA co-occurs with differences in their vision connectors. SmolVLA's pixel-shuffle applies $4 \times 4$ spatial folding, so each of its 128 tokens encodes 16 patches via channel concatenation. Removing any token eliminates an entire receptive field with no redundancy from neighbors (Figure~\ref{fig:pixel_shuffle}). Because the folding is fixed and non-learned, no downstream layer can recover discarded information. OpenVLA's MLP projector maps each patch independently: removing one of 256 tokens discards $\sim$1/256 of the visual field, a localized loss that self-attention layers can partially compensate. At $k{=}0.50$, OpenVLA retains 37.4\% SR against a 74.0\% baseline; SmolVLA collapses to 0\% even at $k{=}0.95$.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=0.85\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
12	\caption{Pixel-shuffle folding: each $4{\times}4$ block of SigLIP patches is channel-concatenated into one token. Removing any token eliminates its receptive field (gray) with no redundancy.}
13	\label{fig:pixel_shuffle}
14	\end{figure}
15	
16	The attention entropy ratio quantifies this structural difference. We measure normalized Shannon entropy of attention weights on vision tokens (1.0 = uniform, lower = selective). SmolVLA's ratio is 0.95, near-uniform across all 16 layers (range 0.93--0.98, total variation 0.05). OpenVLA's overall ratio is 0.64, with progressive sharpening from 0.98 in layer 0 to 0.48 in layer 29 (total variation 0.50, $10\times$ SmolVLA's; see Figure~\ref{fig:entropy_layers} and Appendix~\ref{app:entropy_details}). This reflects fundamentally different information structures: pixel-shuffle tokens are uniformly information-dense and resist selective attention at every processing depth, while MLP-projected tokens allow the model to lea
…[truncated 5942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T06:31:56.760115+00:00_

Perfect! Now I have all the information. Let me compile the findings for you.

## Summary of Findings

I found the exact claim about CogACT's 97.8% success rate in **three locations** across the project:

### Primary Claims

**1. File: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex`**
- **Lines 13** (Discussion section)
- **Exact wording:**
  > "External evidence provides additional support. EfficientVLA~\cite{yang2025efficientvla} reports that CogACT (which uses an MLP projector) retains 97.8\% of its success rate under 78% token pruning, consistent with the graded degradation pattern we observe on OpenVLA. Our experiments on SmolVLA and OpenVLA, together with these findings on CogACT, reveal a consistent pattern across three models spanning two connector families: MLP-projector architectures tolerate aggressive pruning, while pixel-shuffle architectures do not."

**2. File: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex`**
- **Line 33** (Section: "Disentangling Connector from Scale")
- **Exact wording:**
  > "Independent findings from EfficientVLA~\cite{yang2025efficientvla} (CogACT retains 97.8\% SR under 78\% MLP-projector pruning) are consistent with this pattern."

**3. File: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_provenance.yaml`**
- **Line with evidence tracking for claim C359:**
  ```yaml
  - id: C359
    location:
      section: analysis
      paragraph: 0
      sentence: 0
    text: CogACT retains 97.8% SR under 78% MLP-projector pruning
    type: quantitative
    evidence:
    - exp_id: external_efficientvla
      metric: success_rate_retention
  ```

### Context and Key Details

**Source:** The claim is **not from the authors' own experiments** but rather cites **EfficientVLA** (yang2025efficientvla), an external work that tested CogACT.

**Connector Type:**
…[truncated 769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Agent",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T06:31:56.760331+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2506.10100v1",
  "prompt": "I need ALL tables with CogACT results. For each configuration:\n1. What is the baseline success rate of CogACT (no pruning)?\n2. What is the success rate after pruning/compression?\n3. How many visual tokens are retained (out of 256)? What is the token reduction percentage?\n4. Calculate: what percentage of baseline SR is retained after compression?\n\nSpecifically I'm looking for: does any CogACT configuration show 97.8% SR retention (not absolute SR) under 78% token pruning (256→56 tokens)?\n\nAlso check: are there LIBERO benchmark results for CogACT in this paper, or only SIMPLER?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2506.10100v1",
    "prompt": "I need ALL tables with CogACT results. For each configuration:\n1. What is the baseline success rate of CogACT (no pruning)?\n2. What is the success rate after pruning/compression?\n3. How many visual tokens are retained (out of 256)? What is the token reduction percentage?\n4. Calculate: what percentage of baseline SR is retained after compression?\n\nSpecifically I'm looking for: does any CogACT configuration show 97.8% SR retention (not absolute SR) under 78% token pruning (256→56 tokens)?\n\nAlso check: are there LIBERO benchmark results for CogACT in this paper, or only SIMPLER?"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T06:31:56.760484+00:00_

# EfficientVLA: CogACT Results Analysis

## Baseline vs. Compressed Performance

Based on Table 2 (Visual Matching configuration):

**Baseline CogACT:** 74.8% success rate across four tasks

**EfficientVLA with 56 tokens (78% reduction):**
- Configuration: L=22 layers, T=56 tokens
- Success rate: 74.2%
- **Retention: 99.2% of baseline SR** (74.2/74.8)

This configuration achieves approximately **99.2% success rate retention**, which exceeds your specified 97.8% threshold, while maintaining 78% token pruning (256→56 tokens).

## Token Reduction Details

The paper reduces visual tokens from 256 to 56, representing a **78.1% reduction** in token count.

## Benchmark Scope

**No LIBERO results are present in this paper.** The research exclusively evaluates EfficientVLA on the **SIMPLER environment** benchmark, which tests four robotic manipulation tasks:
- Pick coke can
- Move near
- Open/close drawer  
- Open top drawer and place apple

The evaluation includes two SIMPLER configurations: "Visual Matching" and "Variant Aggregation," but no LIBERO benchmark data appears anywhere in the document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T06:31:56.760656+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2506.10100v1",
  "prompt": "Find the EXACT Variant Aggregation results for CogACT in the EfficientVLA paper. List:\n1. Baseline CogACT Variant Aggregation average SR\n2. EfficientVLA (L=22, T=56) Variant Aggregation average SR\n3. The retention ratio (compressed/baseline)\n\nAlso list ALL individual task success rates for both Visual Matching AND Variant Aggregation settings, for both baseline and the L=22/T=56 configuration. I need exact numbers from the tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2506.10100v1",
    "prompt": "Find the EXACT Variant Aggregation results for CogACT in the EfficientVLA paper. List:\n1. Baseline CogACT Variant Aggregation average SR\n2. EfficientVLA (L=22, T=56) Variant Aggregation average SR\n3. The retention ratio (compressed/baseline)\n\nAlso list ALL individual task success rates for both Visual Matching AND Variant Aggregation settings, for both baseline and the L=22/T=56 configuration. I need exact numbers from the tables."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T06:31:56.760802+00:00_

# EfficientVLA Variant Aggregation Results

Based on Table 2 in the paper:

## Summary Metrics
1. **Baseline CogACT Variant Aggregation average SR**: 61.3%
2. **EfficientVLA (L=22, T=56) Variant Aggregation average SR**: 61.2%
3. **Retention ratio**: 99.8% (minimal 0.1 percentage point degradation)

## Complete Individual Task Results

**Visual Matching Setting:**

| Task | Baseline CogACT | EfficientVLA (L=22, T=56) |
|------|-----------------|--------------------------|
| PickCan | 91.3% | 93.3% |
| MoveNear | 85.0% | 81.3% |
| Drawer | 71.8% | 68.2% |
| DrawerApple | 50.9% | 53.8% |

**Variant Aggregation Setting:**

| Task | Baseline CogACT | EfficientVLA (L=22, T=56) |
|------|-----------------|--------------------------|
| PickCan | 89.6% | 93.2% |
| MoveNear | 80.8% | 75.8% |
| Drawer | 28.3% | 26.9% |
| DrawerApple | 46.6% | 49.2% |

The method achieves "1.93×" speedup while maintaining performance through strategic layer and token pruning plus intermediate feature caching.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T06:31:56.760971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_provenance.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_provenance.yaml"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T06:31:56.761427+00:00_

1	paper:
2	  title: ''
3	  version: 56
4	  generated_at: '2026-05-19T00:58:16.680820+00:00'
5	claims:
6	- id: C001
7	  location:
8	    section: experiments
9	    paragraph: 0
10	    sentence: 0
11	  text: All six pruning conditions produce 0% SR vs 44.8% baseline
12	  type: quantitative
13	  evidence:
14	  - exp_id: eval_stage1_only
15	    metric: overall_success_rate
16	  - exp_id: eval_stage1only_object_v2_fixed
17	    metric: overall_success_rate
18	  decisions: []
19	  deprecated: false
20	- id: C003
21	  location:
22	    section: experiments
23	    paragraph: 0
24	    sentence: 0
25	  text: 'Cross-suite cliff-edge: Object 0%, Spatial 0%, Goal 0%'
26	  type: quantitative
27	  evidence:
28	  - exp_id: eval_spatial_prune_k05
29	    metric: overall_sr
30	  - exp_id: eval_goal_prune_k05
31	    metric: overall_sr
32	  decisions: []
33	  deprecated: false
34	- id: C004
35	  location:
36	    section: analysis
37	    paragraph: 0
38	    sentence: 0
39	  text: Attention entropy ratio 0.98
40	  type: quantitative
41	  evidence:
42	  - exp_id: attention_entropy_analysis
43	    metric: entropy_ratio
44	  decisions: []
45	  deprecated: true
46	- id: C005
47	  location:
48	    section: analysis
49	    paragraph: 0
50	    sentence: 0
51	  text: Attention entropy ratio reaches 0.98 (6.86/7.0 bits), Gini coefficient 0.246
52	  type: quantitative
53	  evidence:
54	  - exp_id: attention_entropy_analysis
55	    metric: entropy_ratio
56	  decisions: []
57	  deprecated: true
58	- id: C007
59	  location:
60	    section: analysis
61	    paragraph: 0
62	    sentence: 0
63	  text: Single-step L2 increases from 0.414 to 1.391 (3.4x degradation), relative
64	    error 111.5%
65	  type: quantitative
66	  evidence:
67	  - exp_id: offline_singlestep_action_error
68	    metric: l2_distance
69	  decisions: []
70	  deprecated: true
71	- id: C010
72	  location:
73	    section: analysis
74	    paragraph: 0
75	    sentence: 0
76	  text: Gripper error 1.02 indicates complete inversion
77	  type: qua
…[truncated 43321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T06:31:56.761647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex",
  "offset": "1",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex",
    "offset": "1",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T06:31:56.761809+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Disentangling Connector Design from Model Scale}
5	\label{sec:scale_confound}
6	
7	Our cross-architecture comparison confounds the vision connector design (pixel-shuffle vs.\ MLP projector) with model scale (0.5B vs.\ 7B parameters). A larger model has more capacity to absorb perturbations through its deeper and wider attention layers, raising the question of whether SmolVLA's cliff-edge reflects architectural fragility or simply insufficient model capacity.
8	
9	Four lines of evidence favor the connector-level explanation. First, the official SmolVLA checkpoint (59.2\% SR baseline) exhibits the same cliff-edge under 50\% random pruning (0/500, 0.0\% SR), ruling out the possibility that our fine-tuned model's lower baseline (44.8\%) reflects undertrained weights that are unusually fragile. Second, SmolVLA collapses at $k = 0.95$, where only 7 of 128 tokens (5.5\%) are removed. A capacity-limited model that can solve the task with all tokens should not fail catastrophically when 95\% of the input is preserved; the perturbation is too small relative to the model's demonstrated capability. Third, the attention entropy ratio difference (0.98 vs.\ 0.64) is an architectural measurement, not a capacity measurement. SmolVLA's near-uniform attention distribution reflects the pixel-shuffle connector's output structure: because each token encodes 16 patches via channel concatenation, the resulting tokens are uniformly information-dense, and the downstream LLM has no basis for developing selective attention. OpenVLA's sharply non-uniform attention in deep layers reflects the MLP projector's preservation of per-patch granularity, which allows the model to learn which spatial locations carry task-relevant information. Fourth, the pixel-shuffle operation itself provides a mechanistic explanation: $4 \times 4$ spatial folding creates tokens whose meaning depends on the complete $4 \times 4$ grid, and removing any toke
…[truncated 4748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T06:31:56.761958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
  "offset": "25",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
    "offset": "25",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T06:31:56.762111+00:00_

25	\subsection{Why Learned Compression Succeeds}
26	\label{sec:learned_compression}
27	
28	Hard pruning applies a binary mask: selected tokens are kept, the rest discarded. Cross-attention pooling operates differently: each of $M$ queries computes a weighted sum over all 128 source tokens. Even at $M = 32$ (75\% reduction), every original token contributes through its attention weight; no information is deleted, only re-encoded. The $M = 128$ passthrough control confirms that the $\sim$15-point gain over baseline originates from the re-encoding itself, and an extended training control (100K additional steps without the compressor, 45.0\% SR) rules out the possibility that additional optimization alone explains the gain. The 22.2M-parameter cross-attention module introduces learned, task-adapted capacity that breaks the rigid spatial entanglement of pixel-shuffle tokens. Two factors explain the benefit: the module can emphasize task-relevant spatial features during training, and each query attends across the original $4 \times 4$ receptive field boundaries to integrate information that the pixel-shuffle connector keeps separated.
29	
30	\subsection{Disentangling Connector from Scale}
31	\label{sec:scale_confound}
32	
33	Our comparison confounds the vision connector with model scale (0.5B vs.\ 7B). Four observations favor the connector-level explanation: (1) the official SmolVLA checkpoint (59.2\% baseline) shows the same cliff-edge, ruling out undertrained weights; (2) collapse occurs at $k = 0.95$ (removing only 7 of 128 tokens), a perturbation too small for a capacity explanation; (3) the entropy ratio difference (0.95 vs.\ 0.64) is an architectural measurement, not capacity-dependent; (4) pixel-shuffle's $4 \times 4$ folding provides a mechanistic account of why each token is indispensable. Independent findings from EfficientVLA~\cite{yang2025efficientvla} (CogACT retains 97.8\% SR under 78\% MLP-projector pruning) are consistent with this pattern. Although four l
…[truncated 1402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_verify_978sr_source_20260519T062742",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-19T06:31:56.762442+00:00_

## 核实结果

### C359 数据点："CogACT retains 97.8% SR under 78% MLP-projector pruning"

**结论：97.8% 这个数字是错误的，与 EfficientVLA 的实际数据不符。**

---

### 1. EfficientVLA 中 CogACT 的真实数据

EfficientVLA (arXiv:2506.10100) 对 CogACT 做了 256→56 的视觉 token 压缩（**78% reduction — 这部分正确**），在 SIMPLER benchmark 上的结果：

| 设置 | Baseline SR | 压缩后 SR | **实际保留率** |
|------|-----------|---------|------------|
| Visual Matching | 74.8% | 74.2% | **99.2%** |
| Variant Aggregation | 61.3% | 61.2% | **99.8%** |

**97.8% 这个数字在 EfficientVLA 论文中不存在。** 实际保留率是 99.2%–99.8%。

### 2. 97.8% 的真正来源

97.8% 来自 **VLA-IAP** (arXiv:2603.22991)，但它是：
- **OpenVLA-OFT** 的绝对 SR（不是 CogACT）
- 在 **LIBERO** benchmark 上（不是 SIMPLER）
- **30% pruning** / 70% token retention（不是 78%）
- 1.25x speedup

完全不同的模型、benchmark 和 pruning ratio。

### 3. CogACT 原始论文

- **Title**: CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation
- **arXiv**: [2411.19650](https://arxiv.org/abs/2411.19650)
- **来源**: Microsoft Research, 2024年11月
- 架构：CogVLM backbone + MLP projector + Diffusion Action Transformer
- [项目页](https://cogact.github.io/) | [GitHub](https://github.com/microsoft/CogACT)

### 4. 错误性质

论文中的 claim 混合了两篇论文的数据：
- **78% token pruning** → 来自 EfficientVLA 对 CogACT 的实验（正确）
- **97.8%** → 来自 VLA-IAP 对 OpenVLA-OFT 的实验（张冠李戴）

### 5. 修正建议

两个选择：

**选项 A**：用 EfficientVLA 的真实数据（更好，因为实际保留率更高）
> "CogACT retains **99.2%** of its success rate under 78% token pruning"

**选项 B**：引用 VLA-IAP 的数据，但修正模型名称
> "OpenVLA-OFT retains 97.8% SR under 30% token pruning"

选项 A 更有利，因为 99.2% > 97.8%，论证力度更强。需要同时修改 `discussion.tex:13` 和 `analysis.tex:33` 两处。

Sources:
- [EfficientVLA (arXiv:2506.10100)](https://arxiv.org/abs/2506.10100)
- [VLA-IAP (arXiv:2603.22991)](https://arxiv.org/abs/2603.22991)
- [CogACT (arXiv:2411.19650)](https://arxiv.org/abs/2411.19650)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_verify_978sr_source_20260519T062742"
}
```

</details>

---
