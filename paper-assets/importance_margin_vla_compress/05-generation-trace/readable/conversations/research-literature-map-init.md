# research literature map init

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_research_literature-map-init_20260515T115042.jsonl`
- **Structured JSON:** [`b768f56421a285f99143.json`](../../sessions/b7/b768f56421a285f99143.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-15T11:52:10.085583+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T11:52:10.085931+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T11:52:10.086210+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LightVLA arXiv 2509.12594 visual token compression VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LightVLA arXiv 2509.12594 visual token compression VLA"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T11:52:10.086410+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AutoSelect arXiv 2603.07135 automated token selection VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AutoSelect arXiv 2603.07135 automated token selection VLA"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T11:52:10.086542+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DiffRate ICCV 2023 differentiable token compression vision transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DiffRate ICCV 2023 differentiable token compression vision transformer"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T11:52:10.086675+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA paper small vision language action model robotics 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA paper small vision language action model robotics 2025"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T11:52:10.086904+00:00_

Web search results for query: "LightVLA arXiv 2509.12594 visual token compression VLA"

Links: [{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"LiteVLA-H: Dual-Rate Vision-Language-Action Inference for Onboard Aerial Guidance and Semantic Perception","url":"https://arxiv.org/html/2605.00884"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"}]

Based on the search results, here's what I found about LightVLA (arXiv 2509.12594):

## Overvi
…[truncated 1698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T11:52:10.087203+00:00_

Web search results for query: "AutoSelect arXiv 2603.07135 automated token selection VLA"

Links: [{"title":"[2603.07135] The Model Knows Which Tokens Matter: Automatic Token Selection via Noise Gating","url":"https://arxiv.org/abs/2603.07135"},{"title":"The Model Knows Which Tokens Matter: Automatic Token Selection via Noise Gating","url":"https://arxiv.org/html/2603.07135"},{"title":"[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.25766"},{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233"},{"title":"VLN-Cache: Enabling Token Caching for VLN Models with Visual/Semantic Dynamics Awareness","url":"https://arxiv.org/html/2603.07080"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"}]

Based on the search results, here's what I found about AutoSelect arXiv 2603.07135:

## AutoSelect: Automatic Token Selection via Noise Gating

AutoSelect attaches a lightweight Scorer and Denoiser to a frozen VLM and trains with only the standard next token prediction loss, without auxiliary objectives or extra annota
…[truncated 1137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T11:52:10.087507+00:00_

Web search results for query: "DiffRate ICCV 2023 differentiable token compression vision transformer"

Links: [{"title":"DiffRate : Differentiable Compression Rate for Efﬁcient Vision Transformers","url":"https://openaccess.thecvf.com/content/ICCV2023/papers/Chen_DiffRate__Differentiable_Compression_Rate_for_Efficient_Vision_Transformers_ICCV_2023_paper.pdf"},{"title":"GitHub - OpenGVLab/DiffRate: [ICCV 23]An approach to enhance the efficiency of Vision Transformer (ViT) by concurrently employing token pruning and token merging techniques, while incorporating a differentiable compression rate. · GitHub","url":"https://github.com/OpenGVLab/DiffRate"},{"title":"ICCV 2023 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2023/html/Chen_DiffRate__Differentiable_Compression_Rate_for_Efficient_Vision_Transformers_ICCV_2023_paper.html"},{"title":"[Quick Review] DiffRate : Differentiable Compression Rate for Efficient Vision Transformers","url":"https://liner.com/review/diffrate-differentiable-compression-rate-for-efficient-vision-transformers"},{"title":"[2305.17997] DiffRate : Differentiable Compression Rate for Efficient Vision Transformers","url":"https://arxiv.org/abs/2305.17997"},{"title":"A. Training Details Our training receipt follows most of the techniques used","url":"https://openaccess.thecvf.com/content/ICCV2023/supplemental/Chen_DiffRate__Differentiable_Compression_Rate_for_Efficient_Vision_Transformers_ICCV_2023_supplemental.pdf"},{"title":"DiffRate : Differentiable Compression Rate for Efficient Vision Transformers","url":"https://arxiv.org/pdf/2305.17997"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"DiffRate : Differentiable Compression Rate for Efficient Vision Transformers | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10376949/;j
…[truncated 1869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T11:52:10.087818+00:00_

Web search results for query: "SmolVLA paper small vision language action model robotics 2025"

Links: [{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]","url":"https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250601844S/abstract"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"}]

## Summary of SmolVLA Paper

I found detailed informat
…[truncated 1844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T11:52:10.088087+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Compressor-VLA arXiv 2511.18950 instruction-guided visual token compression robotic manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Compressor-VLA arXiv 2511.18950 instruction-guided visual token compression robotic manipulation"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T11:52:10.088411+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EfficientVLA training-free acceleration compression vision-language-action 2506.10100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EfficientVLA training-free acceleration compression vision-language-action 2506.10100"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T11:52:10.088581+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA-IAP training-free visual token pruning interaction alignment 2603.22991"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA-IAP training-free visual token pruning interaction alignment 2603.22991"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T11:52:10.088706+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "soft top-k differentiable sorting relaxation machine learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "soft top-k differentiable sorting relaxation machine learning 2025"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T11:52:10.088850+00:00_

Web search results for query: "Compressor-VLA arXiv 2511.18950 instruction-guided visual token compression robotic manipulation"

Links: [{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://www.pi.website/download/fast.pdf"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.09927"},{"title":"[2512.09927] Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2512.09927"}]

I found detailed information about the Compressor-VLA paper. Here's what the research presents:

## Overview

Vision-Language-Action (VLA) models have emerged as a powerful paradigm in Embodied AI, however the significant computational overhead of processing redundant visual tokens remains a 
…[truncated 1597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T11:52:10.089036+00:00_

Web search results for query: "VLA-IAP training-free visual token pruning interaction alignment 2603.22991"

Links: [{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"HiPrune: Training-Free Visual Token Pruning via Hierarchical Attention in Vision-Language Models | Request PDF","url":"https://www.researchgate.net/publication/394262421_HiPrune_Training-Free_Visual_Token_Pruning_via_Hierarchical_Attention_in_Vision-Language_Models"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"[2603.21105] ResPrune: Text-Conditioned Subspace Reconstruction for Visual Token Pruning in Large Vision-Language Models","url":"https://arxiv.org/abs/2603.21105"},{"title":"[2603.05950] Energy-Driven Adaptive Visual Token Pruning for Efficient Vision-Language Models","url":"https://arxiv.org/abs/2603.05950"}]

Based on the search results, here's what I found about VLA-IAP:

VLA-IAP addresses the computational efficiency challenges of Vision-Language-
…[truncated 1249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T11:52:10.089266+00:00_

Web search results for query: "EfficientVLA training-free acceleration compression vision-language-action 2506.10100"

Links: [{"title":"[2506.10100] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.10100"},{"title":"Paper page - EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"[Literature Review] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/efficientvla-training-free-acceleration-and-compression-for-vision-language-action-models"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"[PDF] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/310b6b4048e36d5948de19fd26e112cbf05fa754"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=SELYlDHZk2"},{"title":"NeurIPS Poster EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://neurips.cc/virtual/2025/poster/117949"},{"title":"Tiny-VLA:Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://tiny-vla.github.io/"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"}]

Based on the search results, here's what I found about EfficientVLA (arXiv:2506.10100):

## Overview

EfficientVLA is a structured and training-free inference acceleration framework that systematically eliminates barri
…[truncated 1310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T11:52:10.089475+00:00_

Web search results for query: "soft top-k differentiable sorting relaxation machine learning 2025"

Links: [{"title":"DIFFERENTIABLE TOP-k CLASSIFICATION LEARNING","url":"https://openreview.net/pdf?id=6PTUd_zPdHL"},{"title":"[2510.11472] Differentiable Fast Top-K Selection for Large-Scale Recommendation","url":"https://arxiv.org/abs/2510.11472"},{"title":"Differentiable Top-K Estimator","url":"https://www.emergentmind.com/topics/differentiable-top-k-estimator"},{"title":"Differentiable Top-k Classiﬁcation Learning","url":"https://arxiv.org/pdf/2206.07290"},{"title":"Differentiable Sorting & Ranking Operators","url":"https://www.emergentmind.com/topics/differentiable-sorting-and-ranking-operators"},{"title":"Differentiable Fast Top-K Selection for Large-Scale Recommendation Yanjie Zhu∗","url":"https://arxiv.org/pdf/2510.11472"},{"title":"[2206.07290] Differentiable Top-𝑘 Classification Learning","url":"https://ar5iv.labs.arxiv.org/html/2206.07290"},{"title":"Differentiable Fast Top-K Selection for Large-Scale Recommendation","url":"https://arxiv.org/html/2510.11472v2"},{"title":"[PDF] SoftSort: A Continuous Relaxation for the argsort Operator | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SoftSort:-A-Continuous-Relaxation-for-the-argsort-Prillo-Eisenschlos/1648e353100681dc5747fbb8aa887fde4b5c105e"},{"title":"Differentiable Top-k Classification Learning","url":"https://kops.uni-konstanz.de/bitstreams/3b9cbc79-0a96-4a27-a4ba-b343a7882913/download"}]

Based on the search results, here's an overview of recent research on soft top-k differentiable sorting relaxation in machine learning for 2025:

## Key Recent Developments

DFTopK is claimed to be the first to introduce differentiable Top-K operators into recommendation systems and the first to achieve theoretically optimal linear-time complexity for Top-K selection. DFTopK achieves optimal O(n) time complexity, representing a significant improvement over previous methods.

## Major Approaches

Several d
…[truncated 1307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T11:52:10.089647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "margin maximization machine learning SVM large margin theory neural networks 2020 2021 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "margin maximization machine learning SVM large margin theory neural networks 2020 2021 2022"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T11:52:10.089772+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "spectral normalization Lipschitz constraint neural networks Miyato 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "spectral normalization Lipschitz constraint neural networks Miyato 2018"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T11:52:10.089889+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA open-source vision language action model robotics arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA open-source vision language action model robotics arXiv 2024"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T11:52:10.090001+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO benchmark lifelong robot learning suite manipulation 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO benchmark lifelong robot learning suite manipulation 2023"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T11:52:10.090175+00:00_

Web search results for query: "margin maximization machine learning SVM large margin theory neural networks 2020 2021 2022"

Links: [{"title":"Margin maximization with feed-forward neural networks: a comparative study with SVM and AdaBoost - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231203005186"},{"title":"Margin maximization for robust classification using deep learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/7965869/"},{"title":"Pairwise Margin Maximization for Deep Neural Networks Berry Weinstein","url":"https://arxiv.org/pdf/2110.04519"},{"title":"Margin Maximization Dynamics","url":"https://www.emergentmind.com/topics/margin-maximization-dynamics"},{"title":"Support vector machine - Wikipedia","url":"https://en.wikipedia.org/wiki/Support_vector_machine"},{"title":"Margin maximization principle: the basic idea of Support Vector Machine. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Margin-maximization-principle-the-basic-idea-of-Support-Vector-Machine_fig3_226587707"},{"title":"[2110.04519] Pairwise Margin Maximization for Deep Neural Networks","url":"https://arxiv.org/abs/2110.04519"},{"title":"Novel maximum-margin training algorithms for supervised neural networks - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/20409990/"},{"title":"Nonparallel support vector machine with large margin distribution for pattern classification - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320320301771"},{"title":"1 An Idiot’s guide to Support vector machines (SVMs) R. Berwick, Village Idiot","url":"https://web.mit.edu/6.034/wwwbob/svm-notes-long-08.pdf"}]

I've completed the web search for your query on margin maximization in machine learning, SVM theory, and neural networks from 2020-2022. Here's a summary of the key findings:

## Key Research Areas Found

**Margin Maximization in Deep Neural Networks (2021)**

A 2021 paper pr
…[truncated 1408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T11:52:10.090357+00:00_

Web search results for query: "spectral normalization Lipschitz constraint neural networks Miyato 2018"

Links: [{"title":"Atmadeep Banerjee - Spectral Normalization","url":"https://atom-101.github.io/blog/posts/2022-03-18-spectral-norm.html"},{"title":"Lipschitz Continuity and Spectral Normalization | by Wanshun Wong | TDS Archive | Medium","url":"https://medium.com/data-science/lipschitz-continuity-and-spectral-normalization-b03b36066b0d"},{"title":"Spectral Normalization for Generative Adversarial Networks | Request PDF","url":"https://www.researchgate.net/publication/318572189_Spectral_Normalization_for_Generative_Adversarial_Networks"},{"title":"Lipschitz constrained GANs via boundedness and continuity | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-020-04954-z"},{"title":"Published as a conference paper at ICLR 2018 SPECTRAL NORMALIZATION","url":"https://openreview.net/pdf?id=B1QRgziT-"},{"title":"Learning Smooth Neural Functions via Lipschitz Regularization","url":"https://arxiv.org/pdf/2202.08345"},{"title":"Spectral Normalization for GANs","url":"https://www.emergentmind.com/papers/1802.05957"},{"title":"Improving Lipschitz-Constrained Neural Networks by Learning Activation Functions","url":"https://arxiv.org/html/2210.16222v2"},{"title":"Spectral Normalisation for Deep Reinforcement Learning:","url":"http://proceedings.mlr.press/v139/gogianu21a/gogianu21a.pdf"},{"title":"(PDF) Regularisation of Neural Networks by Enforcing Lipschitz Continuity","url":"https://www.researchgate.net/publication/324492300_Regularisation_of_Neural_Networks_by_Enforcing_Lipschitz_Continuity"}]

Based on the search results, I found comprehensive information about spectral normalization, Lipschitz constraints, and the Miyato 2018 paper:

## Overview

The 2018 paper "Spectral Normalization for Generative Adversarial Networks" was authored by T. Miyato, T. Kataoka, M. Koyama, and Y. Yoshida and published at ICLR 201
…[truncated 1347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T11:52:10.090536+00:00_

Web search results for query: "LIBERO benchmark lifelong robot learning suite manipulation 2023"

Links: [{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"NeurIPS Poster LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://neurips.cc/virtual/2023/poster/73415"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO Benchmark: Lifelong Robot Learning","url":"https://www.emergentmind.com/topics/libero-benchmark"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning – Sony AI","url":"https://ai.sony/publications/LIBERO-Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learning/"},{"title":"(PDF) LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.researchgate.net/publication/371347094_LIBERO_Benchmarking_Knowledge_Transfer_for_Lifelong_Robot_Learning"}]

Based on the search results, here's what I found about LIBERO:

## Overview

LIBERO is a novel benchmark of lifelong learning for robot manipulation. It was published in September 2023 as a NeurIPS 2023 Dat
…[truncated 1566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T11:52:10.090712+00:00_

Web search results for query: "OpenVLA open-source vision language action model robotics arXiv 2024"

Links: [{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"openvla/openvla-7b · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b"},{"title":"Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions","url":"https://arxiv.org/html/2505.11214v1"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"}]

Based on the search results, here's what I found about OpenVLA:

## Overview

OpenVLA is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.

## Performance

OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such 
…[truncated 1163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T11:52:10.090856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Octo generalist robot policy paper arXiv 2024 Berkeley"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Octo generalist robot policy paper arXiv 2024 Berkeley"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T11:52:10.090976+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "flow matching action prediction robotics pi0 Physical Intelligence 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "flow matching action prediction robotics pi0 Physical Intelligence 2024"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T11:52:10.091091+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ETA-VLA efficient token adaptation temporal fusion VLA 2603.25766"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ETA-VLA efficient token adaptation temporal fusion VLA 2603.25766"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T11:52:10.091244+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "token merging ToMe vision transformer Bolya 2023 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "token merging ToMe vision transformer Bolya 2023 ICLR"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T11:52:10.091394+00:00_

Web search results for query: "Octo generalist robot policy paper arXiv 2024 Berkeley"

Links: [{"title":"[2405.12213] Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/abs/2405.12213"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/html/2405.12213v1"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/"},{"title":"Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1","url":"https://arxiv.org/pdf/2405.12213"},{"title":"Octo: An Open-Source Generalist Robot Policy - Paper Detail","url":"https://deeplearn.org/arxiv/487297/octo:-an-open-source-generalist-robot-policy"},{"title":"An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/paper.pdf"},{"title":"Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1","url":"https://openreview.net/pdf/e2dabc0a3fd32239dcab07d7bcfa1fae085f49b0.pdf"},{"title":"An open-source generalist model for robot object manipulation","url":"https://techxplore.com/news/2024-06-source-generalist-robot.html"},{"title":"(PDF) Octo: An Open-Source Generalist Robot Policy","url":"https://www.researchgate.net/publication/380730391_Octo_An_Open-Source_Generalist_Robot_Policy"},{"title":"Octo: An Open-Source Generalist Robot Policy | Request PDF","url":"https://www.researchgate.net/publication/383897130_Octo_An_Open-Source_Generalist_Robot_Policy"}]

I found the paper you're looking for. Here's what I found about the Octo generalist robot policy paper:

## Overview

Octo is a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date. It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs.

## Key Features

The Octo model is a transformer-based diffusion policy, pretrained
…[truncated 1048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T11:52:10.091560+00:00_

Web search results for query: "ETA-VLA efficient token adaptation temporal fusion VLA 2603.25766"

Links: [{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766v1"},{"title":"[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.25766"},{"title":"[2508.19257] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.19257"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257v1"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/395033880_TTF-VLA_Temporal_Token_Fusion_via_Pixel-Attention_Integration_for_Vision-Language-Action_Models"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"[PDF] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TTF-VLA:-Temporal-Token-Fusion-via-Pixel-Attention-Liu-Zhang/02462f0f53d1b48867e35eae8901d75996e5a662"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for","url":"https://arxiv.org/pdf/2508.19257"}]

I found information about ETA-VLA (arxiv 26
…[truncated 959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T11:52:10.091742+00:00_

Web search results for query: "flow matching action prediction robotics pi0 Physical Intelligence 2024"

Links: [{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"},{"title":"Robotics Foundation Models by Physical Intelligence: OpenPi | by Siamak Yousefi | Medium","url":"https://medium.com/@siamak.yousefi.1984_58741/robotics-foundation-models-by-physical-intelligence-openpi-663dc55aa9d3"},{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"},{"title":"[2410.24164] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164"},{"title":"π0 robot policy model. π0[1] is a generalist robot policy… | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/%CF%800-robot-policy-model-50d50b739a40"},{"title":"Understanding pi0 by Physical Intelligence: A Vision-Language-Action Flow Model for General Robot Control","url":"https://blog.phospho.ai/understanding-p0-by-physical-intelligence-a-vision-language-action-flow-model-for-general-robot-control/"},{"title":"Notes on: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" | cloderic.com","url":"https://www.cloderic.com/content/2025-02-27-notes-on-pi0"},{"title":"π₀ (Pi0) · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi0"},{"title":"π0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://www.pi.website/download/pi0.pdf"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"}]

Based on the search results, here's what I found about π₀ (Pi0), flow matching, action prediction, and robotics from Physical Intelligence in 2024:

## Overview

π₀ is a Vision-Language-Action model for general
…[truncated 1616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T11:52:10.091918+00:00_

Web search results for query: "token merging ToMe vision transformer Bolya 2023 ICLR"

Links: [{"title":"Published as a conference paper at ICLR 2023 TOKEN MERGING: YOUR VIT BUT FASTER","url":"https://arxiv.org/pdf/2210.09461"},{"title":"GitHub - facebookresearch/ToMe: A method to increase the speed and lower the memory footprint of existing vision transformers. · GitHub","url":"https://github.com/facebookresearch/ToMe"},{"title":"[2210.09461] Token Merging: Your ViT But Faster","url":"https://arxiv.org/abs/2210.09461"},{"title":"Token Merging: Your ViT But Faster | OpenReview","url":"https://openreview.net/forum?id=JroZRaRw7Eu"},{"title":"Token Merging for Fast Stable Diffusion Daniel Bolya Judy Hoffman Georgia Tech","url":"https://openaccess.thecvf.com/content/CVPR2023W/ECV/papers/Bolya_Token_Merging_for_Fast_Stable_Diffusion_CVPRW_2023_paper.pdf"},{"title":"Track: Oral 1 Track 1: Deep Learning and representational learning I","url":"https://iclr.cc/virtual/2023/session/13335"},{"title":"Published as a conference paper at ICLR 2023 TOKEN MERGING: YOUR VIT BUT FASTER","url":"https://openreview.net/pdf?id=JroZRaRw7Eu"},{"title":"Multimodal Promptable Token Merging for Diffusion Models","url":"https://ojs.aaai.org/index.php/AAAI/article/download/33894/36049"},{"title":"[Quick Review] Token Merging: Your ViT But Faster","url":"https://liner.com/review/token-merging-your-vit-but-faster"},{"title":"KFF: K-feature fusion token merging for vision transformer - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425018263"}]

Based on the search results, I found comprehensive information about Token Merging (ToMe) from the Bolya et al. paper presented at ICLR 2023.

## Overview

Token Merging (ToMe) is a simple method to increase the throughput of existing ViT models without needing to train. The work was authored by Daniel Bolya, Cheng-Yang Fu, Xiaoliang Dai, Peizhao Zhang, Christoph Feichtenhofer, and Judy Hoffman, and was published at the
…[truncated 1182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T11:52:10.092068+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pairwise margin maximization deep neural networks arXiv 2110.04519 Weinstein 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pairwise margin maximization deep neural networks arXiv 2110.04519 Weinstein 2021"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T11:52:10.092210+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "differentiable top-k operator implicit differentiation NeurIPS 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "differentiable top-k operator implicit differentiation NeurIPS 2022 2023"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T11:52:10.092426+00:00_

Web search results for query: "differentiable top-k operator implicit differentiation NeurIPS 2022 2023"

Not logged in · Please run /login


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T11:52:10.092597+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA-Pruner temporal-aware dual-level visual token pruning 2511.16449"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA-Pruner temporal-aware dual-level visual token pruning 2511.16449"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T11:52:10.092722+00:00_

Web search results for query: "VLA-Pruner temporal-aware dual-level visual token pruning 2511.16449"

Not logged in · Please run /login


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T11:52:10.092842+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "vision transformer token pruning attention score importance 2022 2023 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "tool_args": {
    "query": "vision transformer token pruning attention score importance 2022 2023 survey"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T11:52:10.092958+00:00_

Web search results for query: "vision transformer token pruning attention score importance 2022 2023 survey"

Not logged in · Please run /login


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T11:52:10.093099+00:00_

Web search results for query: "pairwise margin maximization deep neural networks arXiv 2110.04519 Weinstein 2021"

Links: [{"title":"Pairwise Margin Maximization for Deep Neural Networks Berry Weinstein","url":"https://arxiv.org/pdf/2110.04519"},{"title":"[2110.04519] Pairwise Margin Maximization for Deep Neural Networks","url":"https://arxiv.org/abs/2110.04519"},{"title":"Pairwise Margin Maximization for Deep Neural Networks | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9680053/"},{"title":"[2110.13905] Gradient Descent on Two-layer Nets: Margin Maximization and Simplicity Bias","url":"https://arxiv.org/abs/2110.13905"},{"title":"Margin maximization for robust classification using deep learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/7965869/"},{"title":"[2110.02732] On Margin Maximization in Linear and ReLU Networks","url":"https://arxiv.org/abs/2110.02732"},{"title":"[2110.02732v4] On Margin Maximization in Linear and ReLU Networks","url":"https://arxiv.org/abs/2110.02732v4"},{"title":"Certified Robustness via Dynamic Margin Maximization ...","url":"https://arxiv.org/pdf/2310.00116"},{"title":"Improving generalization of deep neural networks by leveraging margin distribution - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608022000971"},{"title":"Predicting the Generalization Gap in Deep Networks with ...","url":"https://www.scilit.com/publications/b46b8797d5580c9933156f550720a6d1"}]

Based on the search results, I found detailed information about the paper you requested:

The paper "Pairwise Margin Maximization for Deep Neural Networks" was submitted by Berry Weinstein and co-authors on October 9, 2021 with arXiv identifier 2110.04519.

**Key aspects of the paper:**

The paper addresses that weight decay regularization, which was borrowed from the SVM maximum margin principle and extended to multi-class deep networks, is not optimal for 
…[truncated 785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-map-init_20260515T115042",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-15T11:52:10.093319+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_literature-map-init_20260515T115042"
}
```

</details>

---
