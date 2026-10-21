# audit ref verify worker A — Part 2 of 2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-ref-verify-worker-a.md) · [Structured JSON](../../../sessions/72/72b475ba133bd74f70dd.json)

## Round 6

### Tool result

_source line 263 · 2026-05-29T06:32:24.864Z_

<details><summary>↩ Tool result · `toolu_01TBGF9jeN72NEB1Wom2RLqs`</summary>

```text
Web search results for query: "kim2025openoft "Fine-Tuning Vision-Language-Action" title "OpenOFT" or "OpenVLA-OFT""

Links: [{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"},{"title":"openvla-oft/README.md at main · moojink/openvla-oft","url":"https://github.com/moojink/openvla-oft/blob/main/README.md"},{"title":"moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"[Literature Review] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.themoonlight.io/en/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"}]

I found relevant results for your search about the Kim et al. 2025 paper on fine-tuning vision-language-action models. Here's what I found:

## Paper Details

The paper is titled "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" by Kim, Moo Jin, Finn, Chelsea, and Liang, Percy (arXiv preprint arXiv:2502.19645, 2025).

## Key Contributions

The work proposes an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to improve inference efficiency, policy performance, and flexibility in the model's input-output specifications.

## Results

The proposed OpenVLA-OFT achieves state-of-the-art results on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×.

In real-world evaluations on a bimanual ALOHA robot, OpenVLA-OFT outperforms other VLAs (π0 and RDT-1B) and strong imitation learning policies by up to 15% in average success rate.

## Resources

The authors released code and pretrained model checkpoints at https://openvla-oft.github.io.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "243e44cc-e16b-48ce-9a16-f7cabb18e900"
}
```

</details>

---


### System

_source line 264_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae7c854fbb04eafdf",
  "tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "description": "Searching for arxiv 2511.16449 VLA-Pruner authors Liu Ziyan 2025",
  "usage": {
    "total_tokens": 24077,
    "tool_uses": 10,
    "duration_ms": 38563
  },
  "last_tool_name": "WebSearch",
  "uuid": "8144253c-8fbb-4c03-a7be-a17be1b291f9",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 265_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XYMzrAJUHEGYMczJeFtfdo`</summary>

```json
{
  "query": "arxiv 2511.16449 VLA-Pruner authors Liu Ziyan 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "bbcbc526-cd59-45a7-a0fc-4ba10b54aced",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKBu1Ek52QUYyvVEQQxphL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 792,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 19878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2925,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 266_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae7c854fbb04eafdf",
  "tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "description": "Searching for arXiv 2407.10671 Qwen2 first author \"An Yang\"",
  "usage": {
    "total_tokens": 24078,
    "tool_uses": 11,
    "duration_ms": 38667
  },
  "last_tool_name": "WebSearch",
  "uuid": "1aac0cf5-608e-4a0f-b3f7-5733fb5ccedf",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 267_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FfX4Ukx8RUtbuePbPanGYW`</summary>

```json
{
  "query": "arXiv 2407.10671 Qwen2 first author \"An Yang\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "01ad6981-4bfd-4875-9177-73562b4268d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKBu1Ek52QUYyvVEQQxphL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 792,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 19878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2925,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 268 · 2026-05-29T06:32:27.200Z_

<details><summary>↩ Tool result · `toolu_01Par7YyDVUZjC1hyJGBA4M9`</summary>

```text
Web search results for query: "arxiv 2410.04417 SparseVLM first author "Yuan Zhang" OR "Chun-Kai Fan""

Links: [{"title":"Paper page - SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://huggingface.co/papers/2410.04417"},{"title":"[Literature Review] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://www.themoonlight.io/en/review/sparsevlm-visual-token-sparsification-for-efficient-vision-language-model-inference"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference · Issue #38509 · huggingface/transformers","url":"https://github.com/huggingface/transformers/issues/38509"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004417Z/abstract"},{"title":"[2410.04417] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/abs/2410.04417"},{"title":"SparseVLM","url":"https://leofan90.github.io/SparseVLMs.github.io/"},{"title":"Panasonic HD develops “SparseVLM” technology that doubles the processing speed of Vision-Language Models | Innovations/Technologies | Company | Press Releases | Panasonic Newsroom Global","url":"https://news.panasonic.com/global/zh-CHS/press/en250704-2"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/html/2410.04417"},{"title":"GitHub - Theia-4869/SparseVLM","url":"https://github.com/Theia-4869/SparseVLM"}]

I found the paper! The arxiv paper 2410.04417 is titled "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference" and the first authors are Yuan Zhang and Chun-Kai Fan, confirming that both authors you mentioned are indeed the first authors listed.

SparseVLM optimizes vision-language models by pruning irrelevant visual tokens using text-relevant tokens and adaptive sparsification, improving efficiency with minimal accuracy loss. It prunes redundant image tokens layer-wise using self-attention weights and introduces token recycling to compress pruned information, reducing FLOPs and latency by up to 60% while preserving accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "229b398f-e9a6-43ee-bec8-aa7e4b91435d"
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-29T06:32:27.873Z_

<details><summary>↩ Tool result · `toolu_018s8i4rrsEFQbCNzZrPmH5n`</summary>

```text
Web search results for query: "SparseViT CVPR 2023 authors Xuanyao Chen full author list"

Links: [{"title":"CVPR 2023 Open Access Repository","url":"https://openaccess.thecvf.com/content/CVPR2023/html/Chen_SparseViT_Revisiting_Activation_Sparsity_for_Efficient_High-Resolution_Vision_Transformer_CVPR_2023_paper.html"},{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer | Request PDF","url":"https://www.researchgate.net/publication/373309740_SparseViT_Revisiting_Activation_Sparsity_for_Efficient_High-Resolution_Vision_Transformer"},{"title":"dblp: Xuanyao Chen","url":"https://dblp.org/pid/294/6120.html"},{"title":"CVPR Poster SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer","url":"https://cvpr.thecvf.com/virtual/2023/poster/21307"},{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High ...","url":"https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_SparseViT_Revisiting_Activation_Sparsity_for_Efficient_High-Resolution_Vision_Transformer_CVPR_2023_paper.pdf"},{"title":"[2303.17605] SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer","url":"https://arxiv.org/abs/2303.17605"},{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution   Vision Transformer","url":"https://arxiv.org/pdf/2303.17605"}]

The full author list for the SparseViT CVPR 2023 paper is: Xuanyao Chen, Zhijian Liu, Haotian Tang, Li Yi, Hang Zhao, and Song Han.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016gyvTeHUBKP9YcsvMWBLj5",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "1f683da9-90e9-4442-a331-5a9ed0723e2f"
}
```

</details>

---


### Tool result

_source line 270 · 2026-05-29T06:32:28.854Z_

<details><summary>↩ Tool result · `toolu_01CiDTArfcctJ8WCpp7Cbrp3`</summary>

```text
Web search results for query: "CrossGET Cross-Guided Ensemble of Tokens Accelerating Vision-Language Transformers Shi Dachuan ICML 2024 arXiv 2305.17455"

Links: [{"title":"Releases · sdc17/CrossGET","url":"https://github.com/sdc17/CrossGET/releases"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers | OpenReview","url":"https://openreview.net/forum?id=CSIfCpXhCF"},{"title":"GitHub - sdc17/CrossGET: [ICML 2024] CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers.","url":"https://github.com/sdc17/CrossGET"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating   Vision-Language Transformers","url":"https://arxiv.org/pdf/2305.17455"},{"title":"[2305.17455] CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers","url":"https://arxiv.org/abs/2305.17455"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers","url":"https://arxiv.org/html/2305.17455"},{"title":"Sparsity Meets Similarity: Leveraging Long-Tail Distribution for Dynamic Optimized Token Representation in Multimodal Large Language Models","url":"https://arxiv.org/html/2409.01162v2"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"}]

I found the paper you're looking for! Here's what I found about CrossGET:

CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers was presented at ICML 2024. The paper is authored by Shi Dachuan and colleagues, with the arXiv identifier 2305.17455.

The paper introduces CrossGET, a general acceleration framework for vision-language Transformers that adaptively combines tokens in real-time during inference, significantly reducing computational costs while maintaining high performance.

The framework features two main innovations:

1. Cross-modal guided token matching and ensemble to exploit cross-modal information effectively, introducing cross-modal tokens with negligible extra parameters

2. Complete-graph soft matching, which provides more reliable token-matching results while maintaining parallelizability and high efficiency

The paper conducts extensive experiments on various vision-language tasks including image-text retrieval, visual reasoning, image captioning, and visual question answering, demonstrating effectiveness on both classic multimodal architectures and emerging multimodal LLMs.

The code and paper are available on GitHub and arXiv respectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "baf5e077-9a9d-4049-b3ab-39327b85fd69"
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-29T06:32:28.955Z_

<details><summary>↩ Tool result · `toolu_018wuYKefwENc9tbhuC97aTo`</summary>

```text
Web search results for query: "arXiv 2112.07658 "A-ViT" title name change AdaViT"

Links: [{"title":"[2112.07658v3] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658v3"},{"title":"[2112.07658] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658"},{"title":"[2112.07658v1] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658v1"},{"title":"[2112.07658] A-ViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://ar5iv.labs.arxiv.org/html/2112.07658"},{"title":"AdaViT: Adaptive Tokens for Efficient Vision Transformer - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv211207658Y/abstract"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://a-vit.github.io/"},{"title":"[2111.15668] AdaViT: Adaptive Vision Transformers for Efficient Image Recognition","url":"https://arxiv.org/abs/2111.15668"},{"title":"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition","url":"https://arxiv.org/pdf/2111.15668"}]

Based on the search results, I can provide you with information about the arXiv paper 2112.07658:

The paper's title is "AdaViT: Adaptive Tokens for Efficient Vision Transformer", though the method itself is introduced as "A-ViT". 

The title naming shows an interesting pattern: the initial version (v1) submitted on December 14, 2021 used "AdaViT" in the abstract, while later versions (v3 from October 5, 2022) refer to the method as "A-ViT" in the abstract. However, the official project page and citations show both naming conventions being used: "A-ViT: Adaptive Tokens for Efficient Vision Transformer" for the conference paper and "AdaViT: Adaptive Tokens for Efficient Vision Transformer" for the arXiv version.

So to clarify: the paper's official title appears to be "AdaViT" or "A-ViT" (with both forms used interchangeably), while the method name in the abstract evolved between "AdaViT" in the original submission and "A-ViT" in later revisions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016gyvTeHUBKP9YcsvMWBLj5",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "b3e37efa-c1f6-4d05-937e-3d1482dd1141"
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-29T06:32:29.136Z_

<details><summary>↩ Tool result · `toolu_01RkKziLTtNvf48SWvWSgJwJ`</summary>

```text
Web search results for query: "DINOv2 Learning Robust Visual Features without Supervision Oquab TMLR arXiv 2304.07193"

Links: [{"title":"DINOv2: Learning Robust Visual Features without Supervision | alphaXiv","url":"https://www.alphaxiv.org/overview/2304.07193"},{"title":"[2304.07193] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193"},{"title":"[2304.07193v1] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193v1"},{"title":"[2304.07193v2] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193v2"},{"title":"Paper page - DINOv2: Learning Robust Visual Features without Supervision","url":"https://huggingface.co/papers/2304.07193"},{"title":"[PDF] DINOv2: Learning Robust Visual Features without Supervision | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DINOv2:-Learning-Robust-Visual-Features-without-Oquab-Darcet/5a9cb1b3dc4655218b3deeaf4a2417a9a8cd0891"},{"title":"GitHub - facebookresearch/dinov2: PyTorch code and models for the DINOv2 self-supervised learning method. · GitHub","url":"https://github.com/facebookresearch/dinov2"}]

I found the paper you're searching for. Here's what I found:

**DINOv2: Learning Robust Visual Features without Supervision** is authored by Maxime Oquab, Timothée Darcet, and others, with the arXiv identifier 2304.07193.

**Key Points:**

The paper presents a foundation model in computer vision that produces all-purpose visual features that work across image distributions and tasks without fine-tuning.

The work demonstrates that existing self-supervised pretraining methods can produce such features if trained on enough curated data from diverse sources.

The authors revisit existing approaches and combine different techniques to scale pretraining in terms of data and model size, with most technical contributions aimed at accelerating and stabilizing training at scale.

For data, they propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of using uncurated data as is typical in self-supervised learning.

The model uses the LVD-142M curated dataset, sourced from ImageNet, Google Landmarks, Mapillary SLS, Food-101, and other sources.

You can access the paper directly on arXiv at https://arxiv.org/abs/2304.07193 or view the code on GitHub at https://github.com/facebookresearch/dinov2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "c51c4a07-630a-4d57-b76d-141a14357e3a"
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-29T06:32:29.547Z_

<details><summary>↩ Tool result · `toolu_01UdgVHXTt478iUPx53LnLfk`</summary>

```text
Web search results for query: "arxiv 2403.06764 FastV authors "Liang Chen""

Links: [{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/html/2403.06764v1"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"http://export.arxiv.org/abs/2403.06764"},{"title":"GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/chenllliang/FastV"},{"title":"[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"},{"title":"GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/pkunlp-icler/FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference","url":"https://arxiv.org/html/2403.06764v3"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play ...","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10478.pdf"}]

Based on the search results, here's what I found about the paper arxiv 2403.06764 FastV:

**Paper Title:** An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models

**Authors:** Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, Baobao Chang

**Main Contribution:** FastV is a versatile plug-and-play method designed to optimize computational efficiency by learning adaptive attention patterns in early layers and pruning visual tokens in subsequent ones.

**Research Focus:** The study identifies inefficient attention phenomena in Large Vision-Language Models (LVLMs), notably within prominent models like LLaVA-1.5, QwenVL-Chat and Video-LLaVA, and finds that attention computation over visual tokens is of extreme inefficiency in the deep layers of popular LVLMs.

**Performance Results:** FastV demonstrates the ability to dramatically reduce computational costs (e.g., a 45% reduction in FLOPs for LLaVA-1.5-13B) without sacrificing performance in a wide range of image and video understanding tasks.

**Publication Venue:** The paper was published at the European Conference on Computer Vision in 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012SNg9wq7f6YSRDXZgo7Ry5",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "c1c46536-41f7-491e-8957-45a8c479361d"
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-29T06:32:29.556Z_

<details><summary>↩ Tool result · `toolu_01KGF8B3jcJptqY6M97AMZ5V`</summary>

```text
Web search results for query: "Vision-Language Foundation Models Effective Robot Imitators Li Xinghang ICLR 2024 arXiv 2311.01378"

Links: [{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"Paper page - Vision-Language Foundation Models as Effective Robot Imitators","url":"https://huggingface.co/papers/2311.01378"},{"title":"Vision-Language Foundation Models as Effective Robot Imitators | alphaXiv","url":"https://www.alphaxiv.org/hi/overview/2311.01378v3"},{"title":"Vision-Language Foundation Models as Effective Robot Imitators | OpenReview","url":"https://openreview.net/forum?id=lFYj0oibGR"},{"title":"RoboFlamingo | Vision-Language Foundation Models as Effective Robot Imitators","url":"https://roboflamingo.github.io/"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation","url":"https://arxiv.org/html/2406.04339v2"},{"title":"[PDF] Vision-Language Foundation Models as Effective Robot Imitators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Vision-Language-Foundation-Models-as-Effective-Li-Liu/857efca0d4cbece97da4b904de1d506c2af25f9c"},{"title":"GitHub - RoboFlamingo/RoboFlamingo: Code for RoboFlamingo · GitHub","url":"https://github.com/RoboFlamingo/RoboFlamingo"}]

I found the paper you're looking for. Here's what the search revealed:

The paper titled "Vision-Language Foundation Models as Effective Robot Imitators" was submitted on November 2, 2023 (arXiv:2311.01378) and last revised on February 5, 2024. The authors are Xinghang Li, Minghuan Liu, Hanbo Zhang, Cunjun Yu, Jie Xu, Hongtao Wu, Chilam Cheang, Ya Jing, Weinan Zhang, Huaping Liu, Hang Li, and Tao Kong.

The research seeks a straightforward way of making use of existing vision-language models (VLMs) with simple fine-tuning on robotics data, and introduces a simple and novel vision-language manipulation framework, dubbed RoboFlamingo, built upon the open-source VLMs, OpenFlamingo.

RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned manipulation datasets.

The paper appears to have been presented at ICLR 2024. You can access the full paper on arXiv at https://arxiv.org/abs/2311.01378, and the official RoboFlamingo project page at https://roboflamingo.github.io/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "03c1ff7b-946f-4467-b5da-0045738e2a11"
}
```

</details>

---


### System

_source line 275_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a09124f3977418cbc",
  "tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "description": "Searching for proceedings.mlr.press v305 black25a pi0.5",
  "usage": {
    "total_tokens": 27506,
    "tool_uses": 14,
    "duration_ms": 58695
  },
  "last_tool_name": "WebSearch",
  "uuid": "72f30b43-0613-4537-909c-555592065147",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 276_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Tt6QANNRWoaq7gZJmAuWb`</summary>

```json
{
  "query": "proceedings.mlr.press v305 black25a pi0.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "6eb73ee0-7583-4bda-8529-d1447a63ab7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016K8YddYXJ1NLEzdCxnEdhc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4237,
      "cache_read_input_tokens": 22789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4237,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-29T06:32:29.692Z_

<details><summary>↩ Tool result · `toolu_01CFQvGaacsKsJs6Se79woft`</summary>

```text
Web search results for query: "TokenLearner arXiv 2106.11297 title "What Can 8 Learned Tokens Do""

Links: [{"title":"[2106.11297] TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?","url":"https://arxiv.org/abs/2106.11297"},{"title":"GitHub - xiamenwcy/TokenLearner: A PyTorch implementation of \"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?\"","url":"https://github.com/xiamenwcy/TokenLearner"},{"title":"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210611297R/abstract"},{"title":"GitHub - ariG23498/TokenLearner: TensorFlow implementation of \"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?\"","url":"https://github.com/ariG23498/TokenLearner"},{"title":"Paper page - TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?","url":"https://huggingface.co/papers/2106.11297"},{"title":"[PDF] TokenLearner: What Can 8 Learned Tokens Do for Images and Videos? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TokenLearner%3A-What-Can-8-Learned-Tokens-Do-for-and-Ryoo-Piergiovanni/48bcfea07f343b29128c71bb2cce5f3ab62f6d85"},{"title":"1 TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?","url":"https://arxiv.org/pdf/2106.11297"},{"title":"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos? | Request PDF","url":"https://www.researchgate.net/publication/352642552_TokenLearner_What_Can_8_Learned_Tokens_Do_for_Images_and_Videos"},{"title":"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos? | alphaXiv","url":"https://www.alphaxiv.org/overview/2106.11297v4"}]

I found the paper you're looking for! Here's what I found:

**TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?** is a paper by Michael S. Ryoo, AJ Piergiovanni, Anurag Arnab, Mostafa Dehghani, and Anelia Angelova, with the arXiv identifier 2106.11297.

**Overview:**
The paper introduces a novel visual representation learning approach that relies on adaptively learned tokens and is applicable to both image and video understanding tasks. Instead of relying on hand-designed splitting strategies, the approach learns to mine important tokens in visual data. This enables efficient modeling of pairwise attention between tokens, over longer temporal horizons for videos or spatial content in images.

**Key Results:**
The method accomplishes competitive results at significantly reduced compute amount. The paper was extended from its conference version that appeared at NeurIPS 2021.

The paper is accessible at: https://arxiv.org/abs/2106.11297


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016gyvTeHUBKP9YcsvMWBLj5",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "596d4ba7-3a44-4de6-8213-cd624eda3dc3"
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-29T06:32:29.836Z_

<details><summary>↩ Tool result · `toolu_012LrJ2DDaTkrrC8FzLaZCkM`</summary>

```text
Web search results for query: "arxiv 2510.17777 exact title "Decoupled" OR "Decoupling" SparseVILA"

Links: [{"title":"[2510.17777] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/abs/2510.17777"},{"title":"2025-10-21 SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/html/2510.17777"},{"title":"Decoupled Action Expert: Confining Task Knowledge to the Conditioning Pathway","url":"https://arxiv.org/pdf/2511.12101"},{"title":"Decoupled Seg Tokens Make Stronger Reasoning Video Segmenter and Grounder","url":"https://arxiv.org/pdf/2506.22880"},{"title":"Decoupling Global and Local Representations via Invertible Generative   Flows","url":"https://arxiv.org/pdf/2004.11820"}]

I found the paper! The search results show that SparseVILA is a new paradigm for efficient VLM inference that decouples visual sparsity across the prefilling and decoding stages.

**Paper Details:**
- **ArXiv ID:** 2510.17777
- **Title:** "SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference"
- **Submitted:** October 20, 2025

**Key Points:**
SparseVILA distributes sparsity across stages by pruning redundant visual tokens during prefill and retrieving only query-relevant tokens during decoding. This decoupled design matches leading prefill pruning methods while preserving multi-turn fidelity by retaining most of the visual cache so that query-aware tokens can be retrieved at each conversation round.

Built on an AWQ-optimized inference pipeline, SparseVILA achieves up to 4.0 times faster prefilling, 2.5 times faster decoding, and an overall 2.6 times end-to-end speedup.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "9e9aa15a-2dea-4951-af46-e9175c7ceca2"
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-29T06:32:29.899Z_

<details><summary>↩ Tool result · `toolu_01XCQ2wwJT5DAYHPMNcRqp4d`</summary>

```text
Web search results for query: "VLA-Cache arxiv 2502.02175 authors "Siyu Xu""

Links: [{"title":"[2502.02175] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/abs/2502.02175"},{"title":"(PDF) VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://www.researchgate.net/publication/388685612_VLA-Cache_Towards_Efficient_Vision-Language-Action_Model_via_Adaptive_Token_Caching_in_Robotic_Manipulation"},{"title":"GitHub - siyuhsu/vla-cache: [NeurIPS 2025] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching · GitHub","url":"https://github.com/siyuhsu/vla-cache"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1554&show=1919"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"Paper page - VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://huggingface.co/papers/2502.02175"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

**arXiv ID:** 2502.02175

**Authors:** Siyu Xu, Yunke Wang, Chenghao Xia, Dihao Zhu, Tao Huang, and Chang Xu

**Overview:** The paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames. VLA-Cache exploits temporal continuity in robotic manipulation by identifying minimally changed tokens between adjacent frames and reusing their cached key-value representations, while selectively re-computing task-relevant tokens that are environmentally sensitive to maintain action precision.

**Acceptance:** The paper was accepted by NeurIPS 2025

You can access the full paper at: https://arxiv.org/abs/2502.02175


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_012SNg9wq7f6YSRDXZgo7Ry5",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "26a1fb1e-37f6-4fd2-ac63-dec748580bba"
}
```

</details>

---


### Tool result

_source line 280 · 2026-05-29T06:32:29.992Z_

<details><summary>↩ Tool result · `toolu_01PesQEdqtRDxGk5e5hB9qdk`</summary>

```text
Web search results for query: "Quantifying Attention Flow Transformers Abnar Zuidema ACL 2020"

Links: [{"title":"Quantifying Attention Flow in Transformers - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.385/"},{"title":"Quantifying Attention Flow in Transformers","url":"https://notes-vault.pages.dev/Scientific-Literature-References/literature-notes/@abnarQuantifyingAttentionFlow2020"},{"title":"UvA-DARE (Digital Academic Repository)","url":"https://pure.uva.nl/ws/files/178487922/2020.acl-main.385.pdf"},{"title":"Attention Flow - AmsterdamNLP","url":"https://amsterdamnlp.github.io/blog/attentionflow/"},{"title":"Quantifying Attention Flow in Transformers | MYRIAD","url":"https://creatis-myriad.github.io/2022/07/07/AttentionRollout.html"},{"title":"[PDF] Quantifying Attention Flow in Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Attention-Flow-in-Transformers-Abnar-Zuidema/76a9f336481b39515d6cea2920696f11fb686451"},{"title":"Quantifying Attention Flow in Transformers","url":"https://aclanthology.org/2020.acl-main.385.pdf"},{"title":"ACL2020: Quantifying Attention Flow in Transformers","url":"https://virtual.acl2020.org/paper_main.385.html"},{"title":"Quantifying Attention Flow in Transformers | Request PDF","url":"https://www.researchgate.net/publication/343298597_Quantifying_Attention_Flow_in_Transformers"},{"title":"Quantifying Attention Flow in Transformers","url":"https://arxiv.org/pdf/2005.00928"}]

I found the paper you're looking for. Here's what I found:

"Quantifying Attention Flow in Transformers" is a paper by Samira Abnar and Willem Zuidema, published in 2020 in the Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL), pages 4190–4197.

The paper addresses how "self-attention" in the Transformer model combines information from attended embeddings into the representation of the focal embedding in the next layer, causing information originating from different tokens to get increasingly mixed across layers of the Transformer. This makes attention weights unreliable as explanations probes.

The authors propose two methods for approximating the attention to input tokens given attention weights—attention rollout and attention flow—as post hoc methods when using attention weights as the relative relevance of the input tokens, showing that these methods give complementary views on the flow of information and yield higher correlations with importance scores obtained using ablation methods and input gradients compared to raw attention.

The paper has gathered more than 250 citations in 2 years and focuses on interpreting attention patterns in Transformers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "9c6ff7ac-fdcc-4994-9732-f56e936fb458"
}
```

</details>

---


### System

_source line 281_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a09124f3977418cbc",
  "tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "description": "Searching for RT-2 Brohan first author or Zitkovich CoRL 2023 a…",
  "usage": {
    "total_tokens": 27552,
    "tool_uses": 15,
    "duration_ms": 59802
  },
  "last_tool_name": "WebSearch",
  "uuid": "723c9b1b-ca66-4ad0-9922-4560fa74ec23",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 282_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011xV1UP64AVcMHvNu5qufLZ`</summary>

```json
{
  "query": "RT-2 Brohan first author or Zitkovich CoRL 2023 author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "2cf804df-e01c-4ac9-b4e4-b14fface6ca0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016K8YddYXJ1NLEzdCxnEdhc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4237,
      "cache_read_input_tokens": 22789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4237,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-29T06:32:30.766Z_

<details><summary>↩ Tool result · `toolu_01Hqjb7yJZwLBkPeQ4RqdkYH`</summary>

```text
Web search results for query: "RoFormer Enhanced Transformer Rotary Position Embedding Su Jianlin Neurocomputing 2024"

Links: [{"title":"dblp: RoFormer: Enhanced transformer with Rotary Position Embedding.","url":"https://dblp.org/rec/journals/ijon/SuALPBL24.html"},{"title":"RoFormer: Enhanced transformer with Rotary Position Embedding - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231223011864"},{"title":"[2104.09864] RoFormer: Enhanced Transformer with Rotary Position Embedding","url":"https://arxiv.org/abs/2104.09864"},{"title":"ROFORMER: ENHANCED TRANSFORMER WITH ROTARY POSITION EMBEDDING Jianlin Su","url":"https://arxiv.org/pdf/2104.09864"},{"title":"RoFormer: Enhanced transformer with Rotary Position Embedding | Request PDF","url":"https://www.researchgate.net/publication/375900997_RoFormer_Enhanced_transformer_with_Rotary_Position_Embedding"},{"title":"(PDF) RoFormer: Enhanced Transformer with Rotary Position Embedding","url":"https://www.researchgate.net/publication/351019664_RoFormer_Enhanced_Transformer_with_Rotary_Position_Embedding"},{"title":"RoFormer: : Enhanced transformer with Rotary Position Embedding: Neurocomputing: Vol 568, No C","url":"https://dl.acm.org/doi/10.1016/j.neucom.2023.127063"}]

Based on the search results, I found the paper you're looking for:

The paper "RoFormer: Enhanced transformer with Rotary Position Embedding" was authored by Jianlin Su, Murtadha H. M. Ahmed, Yu Lu, Shengfeng Pan, Wen Bo, and Yunfeng Liu, and was published in Neurocomputing volume 568 in 2024.

The paper proposes a novel method named Rotary Position Embedding (RoPE) to effectively leverage positional information, which encodes the absolute position with a rotation matrix and incorporates the explicit relative position dependency in the self-attention formulation. 

RoPE enables valuable properties including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping linear self-attention with relative position encoding. The paper evaluates RoFormer on various long text classification benchmark datasets, and the experiments show that it consistently overcomes its alternatives.

You can access the paper through multiple sources including ScienceDirect, arXiv, and the ACM Digital Library.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "0c461eaa-1542-4f3a-8417-71b480497ec1"
}
```

</details>

---


### System

_source line 284_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a09124f3977418cbc",
  "tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "description": "Searching for SmolVLA 2506.01844 submission date June 2025 year",
  "usage": {
    "total_tokens": 27598,
    "tool_uses": 16,
    "duration_ms": 60101
  },
  "last_tool_name": "WebSearch",
  "uuid": "c55629bb-efb7-4775-b02a-d3b59133387d",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 285_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VaCGL8TYbN7bb8EFaEnXkh`</summary>

```json
{
  "query": "SmolVLA 2506.01844 submission date June 2025 year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "780c4b6c-db1c-4df5-868d-7050064ece8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016K8YddYXJ1NLEzdCxnEdhc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4237,
      "cache_read_input_tokens": 22789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4237,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 286 · 2026-05-29T06:32:31.671Z_

<details><summary>↩ Tool result · `toolu_01XYMzrAJUHEGYMczJeFtfdo`</summary>

```text
Web search results for query: "arxiv 2511.16449 VLA-Pruner authors Liu Ziyan 2025"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://www.arxiv.org/list/cs.CV/2025?skip=24300&show=50"},{"title":"Computer Science Nov 2025","url":"https://arxiv.org/list/cs/2025-11?skip=7900"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449v2"}]

Based on the search results, here's the information about arxiv 2511.16449:

**Paper:** VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference

**Authors:** Ziyan Liu, Yeqiu Chen, Hongyi Cai, Tao Lin, Shuo Yang, Zheng Liu, Bo Zhao

**Submission Date:** Submitted on 20 Nov 2025 (v1), last revised 10 Feb 2026 (this version, v3)

**Affiliations:** School of AI, Shanghai Jiao Tong University; University of Science and Technology of China; Harbin Institute of Technology (Shenzhen); BAAI

**Overview:** VLA-Pruner is a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation.

The paper addresses the challenge of computational efficiency in Vision-Language-Action models for embodied AI applications, particularly focusing on token pruning strategies tailored to VLA systems rather than generic Vision-Language Models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "65f91d5d-7cbf-497b-802b-5cca87ee5d90"
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-29T06:32:32.792Z_

<details><summary>↩ Tool result · `toolu_01FfX4Ukx8RUtbuePbPanGYW`</summary>

```text
Web search results for query: "arXiv 2407.10671 Qwen2 first author "An Yang""

Links: [{"title":"[2407.10671] Qwen2 Technical Report","url":"https://arxiv.org/abs/2407.10671"},{"title":"[2407.10671v1] Qwen2 Technical Report","url":"https://arxiv.org/abs/2407.10671v1"},{"title":"[2407.10671v4] Qwen2 Technical Report","url":"https://arxiv.org/abs/2407.10671v4"},{"title":"Qwen2 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/382272036_Qwen2_Technical_Report"},{"title":"Paper page - Qwen2 Technical Report","url":"https://huggingface.co/papers/2407.10671"},{"title":"(PDF) Qwen2.5-Omni Technical Report","url":"https://www.researchgate.net/publication/390213734_Qwen25-Omni_Technical_Report"},{"title":"[PDF] Qwen2 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Qwen2-Technical-Report-Yang-Yang/54fb839f621e3fe787437ab8ca5f37e7e4726bfe"},{"title":"arXiv:2407.10671v4 [cs.CL] 10 Sep 2024","url":"https://arxiv.org/pdf/2407.10671"}]

Based on the search results, I can confirm that arXiv:2407.10671 is the Qwen2 Technical Report with An Yang listed as the first author. The paper was submitted on July 15, 2024, with the latest version (v4) revised on September 10, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "d7dd2f01-07f3-4619-aa08-8927959518eb"
}
```

</details>

---


### Tool result

_source line 288 · 2026-05-29T06:32:34.291Z_

<details><summary>↩ Tool result · `toolu_018Tt6QANNRWoaq7gZJmAuWb`</summary>

```text
Web search results for query: "proceedings.mlr.press v305 black25a pi0.5"

Links: [{"title":"$\\pi_0.5$: a Vision-Language-Action Model with Open-World Generalization","url":"https://proceedings.mlr.press/v305/black25a.html"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://proceedings.mlr.press/v305/haon25a.html"},{"title":"First Order Model-Based RL through Decoupled Backpropagation","url":"https://proceedings.mlr.press/v305/amigo25a.html"},{"title":"FlashBack: Consistency Model-Accelerated Shared Autonomy","url":"https://proceedings.mlr.press/v305/sun25a.html"},{"title":"Meta-Optimization and Program Search using Language Models for Task and Motion Planning","url":"https://proceedings.mlr.press/v305/shcherba25a.html"},{"title":"GitHub - mlresearch/v305: Proceedings of CoRL 2025 · GitHub","url":"https://github.com/mlresearch/v305"},{"title":"Diffusion-Guided Multi-Arm Motion Planning","url":"https://proceedings.mlr.press/v305/parimi25a.html"},{"title":"LocoFormer: Generalist Locomotion via Long-context Adaptation","url":"https://proceedings.mlr.press/v305/liu25a.html"},{"title":"Neural Robot Dynamics","url":"https://proceedings.mlr.press/v305/xu25g.html"}]

Based on the search results, I found the paper you're looking for:

**π₀.₅: a Vision-Language-Action Model with Open-World Generalization** is published in Proceedings of The 9th Conference on Robot Learning, in Proceedings of Machine Learning Research volume 305, pages 17-40.

The paper has multiple authors including K. Black, N. Brown, J. Darpinian, and many others, and was published in 2025. The paper appears to be available at https://proceedings.mlr.press/v305/black25a.html.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "8fb6db58-2abe-4073-b75e-a714fbf1206d"
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-29T06:32:34.443Z_

<details><summary>↩ Tool result · `toolu_01VaCGL8TYbN7bb8EFaEnXkh`</summary>

```text
Web search results for query: "SmolVLA 2506.01844 submission date June 2025 year"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"[2506.01844v1] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844v1"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://www.researchgate.net/publication/392370918_SmolVLA_A_Vision-Language-Action_Model_for_Affordable_and_Efficient_Robotics"}]

Based on the search results, the SmolVLA paper (arXiv:2506.01844) was submitted on June 2, 2025. This confirms the submission date is in June 2025 as you mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "68453317-ff1a-40ff-93a3-f5a8cd62de82"
}
```

</details>

---


### System

_source line 290_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5bfe667164930f6d",
  "tool_use_id": "toolu_016gyvTeHUBKP9YcsvMWBLj5",
  "description": "Searching for CogACT arXiv 2411.19650 authors \"Qixiu Li\"",
  "usage": {
    "total_tokens": 26888,
    "tool_uses": 13,
    "duration_ms": 39597
  },
  "last_tool_name": "WebSearch",
  "uuid": "a6753bb0-04c4-4d17-b222-3f1eb37bc8c9",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 291_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E7qfJGdAK3772NRvw4W93Y`</summary>

```json
{
  "query": "CogACT arXiv 2411.19650 authors \"Qixiu Li\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016gyvTeHUBKP9YcsvMWBLj5",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "e5628e44-0ba7-43cf-8655-171e7d2163a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSmXCCeFEsovd9xSzLDv3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 584,
      "cache_creation_input_tokens": 1802,
      "cache_read_input_tokens": 23964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1802,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 292_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5bfe667164930f6d",
  "tool_use_id": "toolu_016gyvTeHUBKP9YcsvMWBLj5",
  "description": "Searching for X-VLA arXiv 2510.10274 authors \"Jinliang Zheng\" y…",
  "usage": {
    "total_tokens": 26889,
    "tool_uses": 14,
    "duration_ms": 40131
  },
  "last_tool_name": "WebSearch",
  "uuid": "25524b5f-555c-468f-baae-10456dcea89c",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 293_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MD1iyW89XH8oavNWSF1Q6o`</summary>

```json
{
  "query": "X-VLA arXiv 2510.10274 authors \"Jinliang Zheng\" year 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016gyvTeHUBKP9YcsvMWBLj5",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "11d26010-afca-4625-a3c4-269fbc94a345",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSmXCCeFEsovd9xSzLDv3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 584,
      "cache_creation_input_tokens": 1802,
      "cache_read_input_tokens": 23964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1802,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 294_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for Flamingo Visual Language Model Few-Shot Learning …",
  "usage": {
    "total_tokens": 21352,
    "tool_uses": 7,
    "duration_ms": 24744
  },
  "last_tool_name": "WebSearch",
  "uuid": "72e80b4d-d991-49e6-af4f-814907ffbc3b",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 295_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W5r8XzAptNNS8wWFdn3MMd`</summary>

```json
{
  "query": "Flamingo Visual Language Model Few-Shot Learning Alayrac Jean-Baptiste NeurIPS 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "7b9b88c1-85fe-4cf4-be64-a5158b6237b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QXpNqudrHH8iyUVL7aeP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1644,
      "cache_creation_input_tokens": 2563,
      "cache_read_input_tokens": 16750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 296_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for Perceiver General Perception Iterative Attention …",
  "usage": {
    "total_tokens": 21391,
    "tool_uses": 8,
    "duration_ms": 25273
  },
  "last_tool_name": "WebSearch",
  "uuid": "2343c0e7-9709-47c8-a288-f4725921c4cf",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 297_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011ugpik6gndeDetW3U6FUT8`</summary>

```json
{
  "query": "Perceiver General Perception Iterative Attention Jaegle Andrew ICML 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "411a5247-4115-4fcc-b184-0f08241fcf1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QXpNqudrHH8iyUVL7aeP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1644,
      "cache_creation_input_tokens": 2563,
      "cache_read_input_tokens": 16750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 298_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for RT-2 Vision-Language-Action Models Transfer Web K…",
  "usage": {
    "total_tokens": 21430,
    "tool_uses": 9,
    "duration_ms": 26670
  },
  "last_tool_name": "WebSearch",
  "uuid": "05d2ec9b-3a06-499d-8220-570239bff150",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 299_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RsF9CNVysX67eJZHPTkQ9W`</summary>

```json
{
  "query": "RT-2 Vision-Language-Action Models Transfer Web Knowledge Robotic Control arXiv 2307.15818 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "a4f2d933-a684-4593-830d-9a9ce3dd6d0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QXpNqudrHH8iyUVL7aeP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1644,
      "cache_creation_input_tokens": 2563,
      "cache_read_input_tokens": 16750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 300 · 2026-05-29T06:32:37.387Z_

<details><summary>↩ Tool result · `toolu_011xV1UP64AVcMHvNu5qufLZ`</summary>

```text
Web search results for query: "RT-2 Brohan first author or Zitkovich CoRL 2023 author list"

Links: [{"title":"[2307.15818v1] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818v1"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"Training Strategies for Efficient Embodied Reasoning","url":"https://arxiv.org/html/2505.08243v1"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"RT-2: Vision-Language-Action Models","url":"https://robotics-transformer2.github.io/"},{"title":"Real-time open-vocabulary perception for mobile robots on edge devices: a systematic analysis of the accuracy-latency trade-off - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12583037/"},{"title":"RT-2: Vision-Language-Action Models Transfer Web ...","url":"https://arxiv.org/pdf/2307.15818"}]

Based on the search results, I can answer your query:

The first author of the RT-2 paper is Anthony Brohan, and Brianna Zitkovich is the first-listed author in the CoRL 2023 version of the paper. 

It's worth noting that the authors are listed in alphabetical order, with a contribution statement provided in the paper appendix, which explains why the author order differs between the arXiv version (which lists Brohan first) and the official CoRL proceedings version (which lists Zitkovich first).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "691750dc-19e5-4556-969d-e44d60efc471"
}
```

</details>

---


### System

_source line 301_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for Open X-Embodiment Robotic Learning Datasets RT-X …",
  "usage": {
    "total_tokens": 21469,
    "tool_uses": 10,
    "duration_ms": 27669
  },
  "last_tool_name": "WebSearch",
  "uuid": "94e22951-e107-4e10-8045-0764f6c6839d",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 302_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NPp5s7KZLTfv12P9y9JScW`</summary>

```json
{
  "query": "Open X-Embodiment Robotic Learning Datasets RT-X Models ICRA 2024 arXiv 2310.08864"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "f70bce62-fb4e-46e6-9b9f-c71ddbbabd4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QXpNqudrHH8iyUVL7aeP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1644,
      "cache_creation_input_tokens": 2563,
      "cache_read_input_tokens": 16750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 303_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for H2O Heavy-Hitter Oracle Efficient Generative Infe…",
  "usage": {
    "total_tokens": 21508,
    "tool_uses": 11,
    "duration_ms": 29059
  },
  "last_tool_name": "WebSearch",
  "uuid": "d9e896af-6274-49af-912e-3d8805d3f1a4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 304_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AJ6LKHymAxSY6SKZrD4QZU`</summary>

```json
{
  "query": "H2O Heavy-Hitter Oracle Efficient Generative Inference Large Language Models Zhang Zhenyu NeurIPS 2023 arXiv 2306.14048"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "2466a30f-caa5-4b9b-b24d-790fa0790501",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QXpNqudrHH8iyUVL7aeP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1644,
      "cache_creation_input_tokens": 2563,
      "cache_read_input_tokens": 16750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-29T06:32:40.939Z_

<details><summary>↩ Tool result · `toolu_01E7qfJGdAK3772NRvw4W93Y`</summary>

```text
Web search results for query: "CogACT arXiv 2411.19650 authors "Qixiu Li""

Links: [{"title":"[2411.19650v1] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650v1"},{"title":"[2411.19650] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650"},{"title":"[PDF] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CogACT:-A-Foundational-Vision-Language-Action-Model-Li-Liang/54caf5927a6d656bb84d2a16e16fa2b0c5d6f522"},{"title":"(PDF) CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://www.researchgate.net/publication/386335138_CogACT_A_Foundational_Vision-Language-Action_Model_for_Synergizing_Cognition_and_Action_in_Robotic_Manipulation"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://cogact.github.io/"},{"title":"Scalable Vision-Language-Action Model Pretraining for ​Robotic Manipulation with Real-Life Human Activity Videos","url":"https://arxiv.org/html/2510.21571v1"},{"title":"README.md · CogACT/CogACT-Small at 8afbf8b0b3ab13fe6bb08d17c6f5956218d45e8d","url":"https://huggingface.co/CogACT/CogACT-Small/blob/8afbf8b0b3ab13fe6bb08d17c6f5956218d45e8d/README.md"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/html/2411.19650v1"},{"title":"GitHub - microsoft/CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://github.com/microsoft/CogACT"},{"title":"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models","url":"https://arxiv.org/html/2508.09071v2"}]

Based on the search results, I found information about the CogACT paper (arXiv 2411.19650):

## Paper Details

CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation was authored by Qixiu Li and 17 other authors.

## Complete Author List

The authors are: Qixiu Li, Yaobo Liang, Zeyu Wang, Lin Luo, Xi Chen, Mozheng Liao, Fangyun Wei, Yu Deng, Sicheng Xu, Yizhong Zhang, Xiaofan Wang, Bei Liu, Jianlong Fu, Jianmin Bao, Dong Chen, Yuanchun Shi, Jiaolong Yang, and Baining Guo.

## Affiliations

The authors are affiliated with Tsinghua University, Microsoft Research Asia, USTC, and the Institute of Microelectronics, CAS.

## Paper Summary

The advancement of large Vision-Language-Action (VLA) models has significantly improved robotic manipulation in terms of language-guided task execution and generalization to unseen scenarios, though existing VLAs still show unsatisfactory task performance. The paper proposes a componentized VLA architecture with a specialized action module conditioned on VLM output and demonstrates strong performance enhancement with diffusion action transformers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016gyvTeHUBKP9YcsvMWBLj5",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "a8bc04b2-2e1d-4c8d-b012-23938bc4c870"
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-29T06:32:41.131Z_

<details><summary>↩ Tool result · `toolu_01W5r8XzAptNNS8wWFdn3MMd`</summary>

```text
Web search results for query: "Flamingo Visual Language Model Few-Shot Learning Alayrac Jean-Baptiste NeurIPS 2022"

Links: [{"title":"Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/960a172bc7fbf0177ccccbb411a7d800-Abstract-Conference.html"},{"title":"[PDF] Flamingo: a Visual Language Model for Few-Shot Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Flamingo:-a-Visual-Language-Model-for-Few-Shot-Alayrac-Donahue/26218bdcc3945c7edae7aa2adbfba4cd820a2df3"},{"title":"[2204.14198] Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://arxiv.org/abs/2204.14198"},{"title":"Flamingo: a visual language model for few-shot learning - ORA - Oxford University Research Archive","url":"https://ora.ox.ac.uk/objects/uuid:72fd0848-5ee3-43fa-bdab-d777270d7a58"},{"title":"Flamingo: a Visual - Language Model for Few-Shot Learning","url":"https://faculty.cc.gatech.edu/~zk15/teaching/AY2024_cs8803vlm_fall/slides/L10_Flamingo.pdf"},{"title":"Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://arxiv.org/pdf/2204.14198"},{"title":"Flamingo: a Visual Language Model for Few-Shot Learning - Samuel Albanie","url":"https://samuelalbanie.com/digests/2022-05-flamingo/"},{"title":"🦩 Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://papers.neurips.cc/paper_files/paper/2022/file/960a172bc7fbf0177ccccbb411a7d800-Paper-Conference.pdf"}]

I've successfully found information about the Flamingo Visual Language Model paper. Here are the search results:

## Overview

The paper introduces Flamingo, a family of Visual Language Models (VLM) designed to address the challenge of building models that can be rapidly adapted to novel tasks using only a handful of annotated examples.

## Key Details

- **Authors**: The paper was authored by Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, and 24 other co-authors
- **Publication**: Published at NeurIPS 2022 (Advances in Neural Information Processing Systems 35)
- **Preprint**: The paper was posted on arXiv in April 2022

## Key Contributions

The paper proposes key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest images or videos as inputs.

Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow them with in-context few-shot learning capabilities.

The official NeurIPS proceedings and full paper are available at the links found in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "5999de8c-f2fd-49ba-9756-0e1a6b788434"
}
```

</details>

---


### System

_source line 307_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae7c854fbb04eafdf",
  "tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "description": "Searching for \"Visual Instruction Tuning\" LLaVA authors \"Qingya…",
  "usage": {
    "total_tokens": 25342,
    "tool_uses": 12,
    "duration_ms": 54590
  },
  "last_tool_name": "WebSearch",
  "uuid": "8e6c12a0-f958-4212-b6e1-f926162d8fa0",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 308_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DQ7JDZ7GoiMQpgeJX7PShg`</summary>

```json
{
  "query": "\"Visual Instruction Tuning\" LLaVA authors \"Qingyang Wu\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "5792f0ac-9551-4c21-aaf6-0bce87c0ebf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wZr3THN1bEXTad1VvNQVd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 22803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2053,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-29T06:32:42.261Z_

<details><summary>↩ Tool result · `toolu_01MPsS7mHSQEtv87FmRCXFvf`</summary>

```text
Web search results for query: ""See What Matters" ICML 2026 Feng Yixu authors list"

Links: [{"title":"Downloads 2026","url":"https://icml.cc/Downloads/2026"},{"title":"Maximum Value Matters: Finding Hot Topics in Scholarly Fields","url":"https://arxiv.org/pdf/1710.06637"},{"title":"Knowledge Graph and Accurate Portrait Construction of Scientific and   Technological Academic Conferences","url":"https://arxiv.org/pdf/2204.04888"},{"title":"AI Can Learn Scientific Taste","url":"https://arxiv.org/pdf/2603.14473"},{"title":"Paper Digest: ICML 2026 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/"},{"title":"Paper Digest: ICML 2026 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2026/05/icml-2026-papers-highlights/"},{"title":"ICLR 2026 Thursday 04/23","url":"https://iclr.cc/virtual/2026/day/4/23"}]

Let me search more specifically for the paper with that exact title:

Links: [{"title":"Maximum Value Matters: Finding Hot Topics in Scholarly Fields","url":"https://arxiv.org/pdf/1710.06637"},{"title":"ICML 2022 Reviewers","url":"https://icml.cc/Conferences/2022/Reviewers"},{"title":"Model stability of COVID-19 mortality prediction with biomarkers","url":"https://www.medrxiv.org/content/10.1101/2020.07.29.20161323.full.pdf"},{"title":"The ICML 2023 Ranking Experiment: Examining Author Self-Assessment in ML/AI Peer Review","url":"https://arxiv.org/pdf/2408.13430"},{"title":"ICML 2022 Authorship - Paper Copilot","url":"https://papercopilot.com/icml-authorship/icml-2022-authorship/"}]

Let me try a more direct search on arXiv for this paper:

Links: [{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"Recommending Best Paper Awards for ML/AI Conferences via the Isotonic Mechanism","url":"https://arxiv.org/html/2601.15249v2"},{"title":"Stop Automating Peer Review Without Rigorous Evaluation","url":"https://arxiv.org/html/2605.03202v1"},{"title":"Maximum Value Matters: Finding Hot Topics in Scholarly Fields","url":"https://arxiv.org/pdf/1710.06637"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"ICML 2026 Papers","url":"https://icml.cc/virtual/2026/papers.html"}]

Let me try searching for the paper title more directly:

Links: [{"title":"Why Thoughtful Attention Matters More Than Ever in 2026","url":"https://www.featherandfernpr.co.uk/post/why-thoughtful-attention-matters-more-than-ever-in-2026"},{"title":"Marketing in 2026: Defining Attention - The Metrics That Matter - Brillity Digital","url":"https://brillitydigital.com/blog/marketing-in-2026-defining-attention-the-metrics-that-matter/"},{"title":"Attention Is All You Need: The Paper That Changed AI Forever - Kanoonpedia","url":"https://kanoonpedia.com/attention-is-all-you-need-transformer-explained/"},{"title":"How Media Professionals Can Test the Waters with Attention in 2026","url":"https://www.amplified.co/insight/blog-test-the-waters-with-attention-in-2026"},{"title":"Attention Is All You Need, explained like you’re smart and busy | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/attention-is-all-you-need-explained-like-youre-smart-and-busy-2a3d7436144f"},{"title":"New ADHD Research Challenges Former Assumptions. Why It Matters","url":"https://www.edweek.org/teaching-learning/new-adhd-research-challenges-former-assumptions-why-it-matters/2026/02"},{"title":"[2409.19001] Pay Attention to What Matters","url":"https://arxiv.org/abs/2409.19001"},{"title":"Year-End Reflection: 10 Deep Questions for 2025 and 2026 | Activities Matter","url":"https://activitiesmatter.app/blog/ten-reflection-prompts-to-bridge-2025-and-2026/"}]

I found a related paper called "Pay Attention to What Matters," but not the exact "See What Matters" paper you're looking for. Let me try one more specific search:

Links: [{"title":"Auditor Models to Suppress Poor AI Predictions Can Improve Human-AI Collaborative Performance","url":"https://www.medrxiv.org/content/10.1101/2025.06.24.25330212.full.pdf"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"Deep learning models for COVID-19 chest x-ray classification: Preventing shortcut learning using feature disentanglement","url":"https://www.medrxiv.org/content/10.1101/2021.02.11.20196766.full.pdf"},{"title":"AI Can Learn Scientific Taste","url":"https://arxiv.org/pdf/2603.14473"},{"title":"ICML 2026 Papers","url":"https://icml.cc/virtual/2026/papers.html"},{"title":"Weakly Supervised Active Learning for Abstract Screening Leveraging LLM-Based Pseudo-Labeling","url":"https://www.medrxiv.org/content/10.1101/2025.08.24.25334314.full.pdf"},{"title":"Reasoning Models for Text Mining in Oncology – a Comparison Between o1 Preview and GPT-4o","url":"https://www.medrxiv.org/content/10.1101/2024.12.06.24318592.full.pdf"},{"title":"Model stability of COVID-19 mortality prediction with biomarkers","url":"https://www.medrxiv.org/content/10.1101/2020.07.29.20161323.full.pdf"}]

I apologize, but I was unable to find the specific paper titled "See What Matters" by Feng Yixu at ICML 2026 with its complete author list through my web searches. The search results did not return this particular paper despite multiple search attempts using different query variations.

To locate this paper and its authors, I would recommend:

1. Visiting the official ICML 2026 papers page directly at icml.cc
2. Searching the ICML 2026 proceedings or program schedule
3. Checking the arXiv preprint server with the exact paper title
4. Looking at the Paper Digest ICML 2026 database, which has comprehensive listings of all accepted papers

If you have a direct link to the paper or additional details about it, that would help me provide you with the author list.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "27288bfa-bda1-4d09-ae1d-cf1c9b7e69f7"
}
```

</details>

---


### System

_source line 310_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a09124f3977418cbc",
  "tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "description": "Searching for OpenVLA CoRL 2024 PMLR volume 270 publication yea…",
  "usage": {
    "total_tokens": 29612,
    "tool_uses": 17,
    "duration_ms": 71497
  },
  "last_tool_name": "WebSearch",
  "uuid": "0b561a2f-d924-41c1-854e-580d84a77fe3",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 311_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011G6xcHYSbEwZhJ55F4zJRg`</summary>

```json
{
  "query": "OpenVLA CoRL 2024 PMLR volume 270 publication year 2025 kim25c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "691a01be-9516-4c4d-959c-0bbd5ea491e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNkWcGhvdrW6Rykd3VvHwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 609,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 27026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 312_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a09124f3977418cbc",
  "tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "description": "Searching for Octo RSS 2024 PMLR proceedings Ghosh authors full…",
  "usage": {
    "total_tokens": 29613,
    "tool_uses": 18,
    "duration_ms": 71678
  },
  "last_tool_name": "WebSearch",
  "uuid": "dea2bd44-48e8-4e4c-872f-3da2b023ed5f",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 313_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QB7eqm2PJFEmzeEyCdqGjj`</summary>

```json
{
  "query": "Octo RSS 2024 PMLR proceedings Ghosh authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "83b8c2c1-ce31-455d-87de-7b8fe7f17755",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNkWcGhvdrW6Rykd3VvHwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 609,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 27026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 314 · 2026-05-29T06:32:42.727Z_

<details><summary>↩ Tool result · `toolu_01RsF9CNVysX67eJZHPTkQ9W`</summary>

```text
Web search results for query: "RT-2 Vision-Language-Action Models Transfer Web Knowledge Robotic Control arXiv 2307.15818 authors"

Links: [{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://stevengong.co/research-papers/RT2-VisionLanguageAction-Models-Transfer-Web-Knowledge-to-Robotic-Control"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"RT-2: Vision-Language-Action Models Transfer Web ...","url":"https://arxiv.org/pdf/2307.15818"},{"title":"[2307.15818v1] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818v1"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://huggingface.co/papers/2307.15818"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"dblp: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.","url":"https://dblp.org/rec/journals/corr/abs-2307-15818.html"}]

Based on the search results, here's the information about the RT-2 paper (arXiv 2307.15818):

**Paper Title:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

**Authors:** Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, Pete Florence, Chuyuan Fu, Montse Gonzalez Arenas, Keerthana Gopalakrishnan, Kehang Han, Karol Hausman, Alexander Herzog, Jasmine Hsu, Brian Ichter, Alex Irpan, Nikhil J. Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Isabel Leal, Lisa Lee, Tsang-Wei Edward Lee, Sergey Levine, Yao Lu, Henryk Michalewski, Igor Mordatch, Karl Pertsch, Kanishka Rao, Krista Reymann, Michael S. Ryoo, Grecia Salazar, Pannag Sanketi, Pierre Sermanet, Jaspiar Singh, Anikait Singh, Radu Soricut, Huong T. Tran, Vincent Vanhoucke, Quan Vuong, Ayzaan Wahid, Stefan Welker, Paul Wohlhart, Jialin Wu, Fei Xia, Ted Xiao, Peng Xu, Sichun Xu, Tianhe Yu, Brianna Zitkovich

**Overview:** The paper studies how vision-language models trained on Internet-scale data can be incorporated directly into end-to-end robotic control to boost generalization and enable emergent semantic reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "ad83ad3b-d491-47f2-980d-6a8498c096e6"
}
```

</details>

---


### System

_source line 315_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae7c854fbb04eafdf",
  "tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "description": "Searching for LLaVA-PruMerge arXiv 2403.15388 authors Shang Yuz…",
  "usage": {
    "total_tokens": 25343,
    "tool_uses": 13,
    "duration_ms": 55890
  },
  "last_tool_name": "WebSearch",
  "uuid": "efe35689-cfac-4427-933c-d9f9b48c0cc5",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 316_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PHzP2S8AuqPJi9FuknavqS`</summary>

```json
{
  "query": "LLaVA-PruMerge arXiv 2403.15388 authors Shang Yuzhang year venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "5eae429f-11bf-402e-903e-1e1a0af605c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wZr3THN1bEXTad1VvNQVd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 22803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2053,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-29T06:32:43.537Z_

<details><summary>↩ Tool result · `toolu_01MD1iyW89XH8oavNWSF1Q6o`</summary>

```text
Web search results for query: "X-VLA arXiv 2510.10274 authors "Jinliang Zheng" year 2025"

Links: [{"title":"[2510.10274] X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/abs/2510.10274"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2510.10274"},{"title":"(PDF) X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://www.researchgate.net/publication/396462440_X-VLA_Soft-Prompted_Transformer_as_Scalable_Cross-Embodiment_Vision-Language-Action_Model"},{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"},{"title":"2025-10-14 X-VLA: Soft-Prompted Transformer as Scalable","url":"https://arxiv.org/pdf/2510.10274"},{"title":"dblp: X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model.","url":"https://dblp.org/rec/journals/corr/abs-2510-10274.html"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.10274"},{"title":"Paper page - X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://huggingface.co/papers/2510.10274"}]

I found the paper you were looking for. Here are the details:

**Paper:** X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model

**arXiv ID:** 2510.10274

**Submission Date:** October 11, 2025

**Authors:** Jinliang Zheng, Jianxiong Li, Zhihao Wang, Dongxiu Liu, Xirui Kang, Yuchun Feng, Yinan Zheng, Jiayin Zou, Yilun Chen, Jia Zeng, Ya-Qin Zhang, Jiangmiao Pang, Jingjing Liu, Tai Wang, and Xianyuan Zhan

**Affiliations:** Institute for AI Industry Research (AIR) at Tsinghua University, Shanghai AI Lab, and Peking University

**Summary:** The paper addresses successful generalist Vision-Language-Action (VLA) models that rely on effective training across diverse robotic platforms with large-scale, cross-embodiment, heterogeneous datasets. The authors propose a novel Soft Prompt approach with minimally added parameters, by infusing prompt learning concepts into cross-embodiment robot learning and introducing separate sets of learnable embeddings for each distinct data source. The new X-VLA is a flow-matching-based VLA architecture that relies exclusively on soft-prompted standard Transformer encoders, and X-VLA won 1st Place (Champion) at the AgiBot World Challenge, held at IROS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016gyvTeHUBKP9YcsvMWBLj5",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "27e0d404-9f3a-4f37-b99c-676c390cb1fb"
}
```

</details>

---


### Tool result

_source line 318 · 2026-05-29T06:32:44.703Z_

<details><summary>↩ Tool result · `toolu_01NPp5s7KZLTfv12P9y9JScW`</summary>

```text
Web search results for query: "Open X-Embodiment Robotic Learning Datasets RT-X Models ICRA 2024 arXiv 2310.08864"

Links: [{"title":"Open X-Embodiment: Robotic learning datasets and RT-X models - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/open-x-embodiment-robotic-learning-datasets-and-rt-x-models/"},{"title":"Open x-embodiment: Robotic learning datasets and rt-x models - UCSD ARCLAB","url":"https://ucsdarclab.com/autopublication/open-x-embodiment-robotic-learning-datasets-and-rt-x-models/"},{"title":"Open X-Embodiment: Robotic learning datasets and RT-X models | Centre for AI in Assistive Autonomy","url":"https://assistive-autonomy.ed.ac.uk/project/feature-publication-oxe/"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models – UT Austin Robot Perception and Learning Lab","url":"https://rpl.cs.utexas.edu/publications/2024/05/13/rtx-icra24-rtx/"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models : Open X-Embodiment Collaboration>0> - Arizona State University","url":"https://asu.elsevierpure.com/en/publications/open-x-embodiment-robotic-learning-datasets-and-rt-x-models-open-/"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models","url":"https://robotics-transformer-x.github.io/"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models","url":"https://arxiv.org/pdf/2310.08864"},{"title":"[2310.08864] Open X-Embodiment: Robotic Learning Datasets and RT-X Models","url":"https://arxiv.org/abs/2310.08864"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models : Open X-Embodiment Collaboration0 | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10611477"}]

Based on the search results, here's information about the Open X-Embodiment project:

## Overview

Open X-Embodiment: Robotic learning datasets and RT-X models was published at the 2024 IEEE International Conference on Robotics and Automation (ICRA). The paper won the ICRA 2024 Best Paper Award.

## The Dataset

The Open X-Embodiment Dataset is the largest open-source real robot dataset to date, containing 1M+ real robot trajectories spanning 22 robot embodiments, from single robot arms to bi-manual robots and quadrupeds. The dataset was constructed by pooling 60 existing robot datasets from 34 robotic research labs around the world.

## The RT-X Models

The team assembled a dataset from 22 different robots collected through a collaboration between 21 institutions, demonstrating 527 skills (160266 tasks), and developed a high-capacity model called RT-X that exhibits positive transfer and improves the capabilities of multiple robots by leveraging experience from other platforms.

## Key Research Question

The paper addresses whether large, high-capacity models trained on diverse datasets can lead to consolidation of pretrained models in robotics, similar to what has happened in NLP and computer vision, exploring whether generalist X-robot policies can be adapted efficiently to new robots, tasks, and environments.

**arXiv Reference:** https://doi.org/10.48550/arXiv.2310.08864


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "e030d7bd-4d79-4af8-970e-a5ce7d71bdf5"
}
```

</details>

---


### System

_source line 319_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adda7656f92cca819",
  "tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "description": "Searching for arxiv 2605.11817 \"See What Matters\" authors Feng …",
  "usage": {
    "total_tokens": 29818,
    "tool_uses": 17,
    "duration_ms": 83052
  },
  "last_tool_name": "WebSearch",
  "uuid": "e8bbcf32-4f93-44e7-bf48-c2eee58943b6",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 320_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CoqHs7EQ9KPM96KW6ezcLs`</summary>

```json
{
  "query": "arxiv 2605.11817 \"See What Matters\" authors Feng Yixu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "b2f55f4e-c148-48df-9212-a91613fe88a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HU2h1wnfsDZ41qJwykwRGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4183,
      "cache_read_input_tokens": 25198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4183,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 321_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adda7656f92cca819",
  "tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "description": "Searching for Compressor-VLA arxiv 2511.18950 year submitted 20…",
  "usage": {
    "total_tokens": 29869,
    "tool_uses": 18,
    "duration_ms": 84057
  },
  "last_tool_name": "WebSearch",
  "uuid": "2f4d5a72-8f71-4ffe-b2b9-0747935567f9",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 322_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VZrfv1Db2YEaYyfzeotzPs`</summary>

```json
{
  "query": "Compressor-VLA arxiv 2511.18950 year submitted 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "8eb04509-de08-4dbd-a381-28f2640c9864",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HU2h1wnfsDZ41qJwykwRGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4183,
      "cache_read_input_tokens": 25198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4183,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-29T06:32:47.014Z_

<details><summary>↩ Tool result · `toolu_011ugpik6gndeDetW3U6FUT8`</summary>

```text
Web search results for query: "Perceiver General Perception Iterative Attention Jaegle Andrew ICML 2021"

Links: [{"title":"Perceiver: General Perception with Iterative Attention - researchr publication","url":"https://researchr.org/publication/JaegleGBVZC21"},{"title":"[Quick Review] Perceiver: General Perception with Iterative Attention","url":"https://liner.com/review/perceiver-general-perception-with-iterative-attention"},{"title":"Perceiver: General Perception with Iterative Attention — Paper summary | by Gowthami Somepalli | ML Summaries | Medium","url":"https://medium.com/ml-summaries/perceiver-paper-s-summary-3c589ec74238"},{"title":"[2103.03206] Perceiver: General Perception with Iterative Attention","url":"https://arxiv.org/abs/2103.03206"},{"title":"[2103.03206v2] Perceiver: General Perception with Iterative Attention","url":"https://arxiv.org/abs/2103.03206v2"},{"title":"Perceiver: General Perception with Iterative Attention","url":"https://proceedings.mlr.press/v139/jaegle21a/jaegle21a.pdf"},{"title":"ICML Poster Perceiver: General Perception with Iterative Attention","url":"https://icml.cc/virtual/2021/poster/10291"},{"title":"Perceiver: General Perception with Iterative Attention - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210303206J/abstract"},{"title":"ICML 2021 Perceiver: General Perception with Iterative Attention Spotlight","url":"https://icml.cc/virtual/2021/spotlight/10292"},{"title":"Perceiver: General Perception with Iterative Attention","url":"https://arxiv.org/pdf/2103.03206"}]

I found comprehensive information about this paper. Here are the key details:

## Paper Information

The paper "Perceiver: General Perception with Iterative Attention" was authored by Andrew Jaegle, Felix Gimeno, Andy Brock, Oriol Vinyals, Andrew Zisserman, and João Carreira, and was published in the Proceedings of the 38th International Conference on Machine Learning (ICML 2021) held July 18-24, 2021.

## Core Concept

The Perceiver is a model that builds upon Transformers and makes few architectural assumptions about the relationship between its inputs, but scales to hundreds of thousands of inputs, like ConvNets.

## Technical Approach

The model leverages an asymmetric attention mechanism to iteratively distill inputs into a tight latent bottleneck, allowing it to scale to handle very large inputs. The Perceiver iteratively attends to the input byte array by alternating cross-attention and latent self-attention blocks.

## Performance

The architecture is competitive with or outperforms strong, specialized models on classification tasks across various modalities: images, point clouds, audio, video, and video+audio. The Perceiver obtains performance comparable to ResNet-50 and ViT on ImageNet without 2D convolutions by directly attending to 50,000 pixels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "362c581f-9d56-4e05-be14-f5245693219e"
}
```

</details>

---


### Tool result

_source line 324 · 2026-05-29T06:32:47.026Z_

<details><summary>↩ Tool result · `toolu_01PHzP2S8AuqPJi9FuknavqS`</summary>

```text
Web search results for query: "LLaVA-PruMerge arXiv 2403.15388 authors Shang Yuzhang year venue"

Links: [{"title":"[2403.15388v5] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v5"},{"title":"[2403.15388v4] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v4"},{"title":"[Paper Review] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://velog.io/@euisuk-chung/LLaVA-PruMerge-Adaptive-Token-Reduction-for-Efficient-Large-Multimodal-Models"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/pdf/2403.15388"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/llava-prumerge-adaptive-token-reduction-efficient-large"},{"title":"[2403.15388] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://www.emergentmind.com/papers/2403.15388"},{"title":"dblp: LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models.","url":"https://dblp.org/rec/journals/corr/abs-2403-15388.html"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient ...","url":"https://arxiv.org/pdf/2403.15388v3/"}]

Based on the search results, here is the information for the LLaVA-PruMerge paper (arXiv 2403.15388):

**Authors:** Yuzhang Shang, Mu Cai, Bingxin Xu, Yong Jae Lee, Yan Yan

**Year:** Submitted on 22 Mar 2024

**Venue:** ICCV 2025

**Title:** LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "716d77d4-dbca-4f42-ac98-61d4860ad3e8"
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-29T06:32:47.473Z_

<details><summary>↩ Tool result · `toolu_01DQ7JDZ7GoiMQpgeJX7PShg`</summary>

```text
Web search results for query: ""Visual Instruction Tuning" LLaVA authors "Qingyang Wu" NeurIPS 2023"

Links: [{"title":"Visual Instruction Tuning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf"},{"title":"Visual Instruction Tuning: LLaVA Model Insights and Benchmarks (2023) - Studocu","url":"https://www.studocu.com/en-us/document/mitchell-technical-college/microbiology/visual-instruction-tuning-llava-model-insights-and-benchmarks-2023/143249240"},{"title":"NeurIPS Poster Visual Instruction Tuning","url":"https://neurips.cc/virtual/2023/poster/70080"},{"title":"Visual Instruction Tuning | OpenReview","url":"https://openreview.net/forum?id=w0H2xGHlkw"},{"title":"LLaVA","url":"https://llava-vl.github.io/"},{"title":"GitHub - haotian-liu/LLaVA: [NeurIPS'23 Oral] Visual Instruction Tuning (LLaVA) built towards GPT-4V level capabilities and beyond. · GitHub","url":"https://github.com/haotian-liu/llava"},{"title":"Visual Instruction Tuning","url":"https://arxiv.org/pdf/2304.08485"},{"title":"[PDF] Visual Instruction Tuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Visual-Instruction-Tuning-Liu-Li/a5036f31f0e629dc661f120b8c3b1f374d479ab8"}]

Based on the search results, I found comprehensive information about the "Visual Instruction Tuning" paper:

The paper was authored by Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee from the University of Wisconsin–Madison, Microsoft Research, and Columbia University. The paper was presented at NeurIPS 2023 as an Oral presentation.

The paper presents the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data, and introduces LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an LLM for general-purpose visual and language understanding.

To facilitate future research on visual instruction following, the authors construct two evaluation benchmarks with diverse and challenging application-oriented tasks. The paper also includes several resources: the GPT-4 generated visual instruction tuning data, model and code base are publicly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "d21d5d4b-453c-4bd2-b88a-ca82a0428b9f"
}
```

</details>

---


### System

_source line 326_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adda7656f92cca819",
  "tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "description": "Searching for \"Don't Run with Scissors\" Jabbour arxiv 2510.0846…",
  "usage": {
    "total_tokens": 29920,
    "tool_uses": 19,
    "duration_ms": 84851
  },
  "last_tool_name": "WebSearch",
  "uuid": "4d9aed7f-1180-4c23-b07a-b146c9e3c66b",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 327_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E3ZYfko3jCGERQRXGnUnSj`</summary>

```json
{
  "query": "\"Don't Run with Scissors\" Jabbour arxiv 2510.08464 venue conference accepted 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "2a0cb8b2-1f1e-4756-877d-27ed1b9d5fac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HU2h1wnfsDZ41qJwykwRGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4183,
      "cache_read_input_tokens": 25198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4183,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 328 · 2026-05-29T06:32:47.688Z_

<details><summary>↩ Tool result · `toolu_01AJ6LKHymAxSY6SKZrD4QZU`</summary>

```text
Web search results for query: "H2O Heavy-Hitter Oracle Efficient Generative Inference Large Language Models Zhang Zhenyu NeurIPS 2023 arXiv 2306.14048"

Links: [{"title":"[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/abs/2306.14048"},{"title":"AI-Powered Paper Summarization about the arXiv paper 2306.14048v1","url":"https://www.summarizepaper.com/en/arxiv-id/2306.14048v1/"},{"title":"H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large   Language Models","url":"https://arxiv.org/pdf/2306.14048"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html"},{"title":"Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://huggingface.co/papers/2306.14048"},{"title":"dblp: H&lt;sub>2&lt;/sub>O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2306-14048.html"},{"title":"H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/371871295_H_2O_Heavy-Hitter_Oracle_for_Efficient_Generative_Inference_of_Large_Language_Models"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6ceefa7b15572587b78ecfcebb2827f8-Paper-Conference.pdf"}]

I've successfully found the research paper. Here are the key findings:

## Paper Overview

The paper "H₂O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models" was authored by Zhenyu Zhang, Ying Sheng, Tianyi Zhou, Tianlong Chen, Lianmin Zheng, Ruisi Cai, Zhao Song, Yuandong Tian, Christopher Ré, Clark Barrett, Zhangyang Wang, and Beidi Chen.

## Publication Details

The paper was published in Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Main Conference Track. It was first submitted on June 24, 2023, and is available on arXiv as paper 2306.14048.

## Problem and Solution

Large Language Models are notably cost-prohibitive to deploy, particularly for applications involving long-content generation, such as dialogue systems and story writing. A large amount of transient state information, referred to as the KV cache, is stored in GPU memory in addition to model parameters, scaling linearly with the sequence length and batch size.

The authors propose Heavy Hitter Oracle (H₂O), a KV cache eviction policy that dynamically retains a balance of recent and H₂ tokens.

## Results

The implementation of H₂O with 20% heavy hitters improves throughput over DeepSpeed Zero-Inference, Hugging Face Accelerate, and FlexGen by up to 29×, 29×, and 3× on OPT-6.7B and OPT-30B. With the same batch size, H2O can reduce latency by up to 1.9×.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "e8e9d15a-f399-4d1e-a49f-41ff0532b31d"
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-29T06:32:48.004Z_

<details><summary>↩ Tool result · `toolu_01QB7eqm2PJFEmzeEyCdqGjj`</summary>

```text
Web search results for query: "Octo RSS 2024 PMLR proceedings Ghosh authors full list"

Links: [{"title":"A Closer Look at the Limitations of Instruction Tuning","url":"https://proceedings.mlr.press/v235/ghosh24a.html"},{"title":"LoRA+: Efficient Low Rank Adaptation of Large Models","url":"https://proceedings.mlr.press/v235/hayou24a.html"},{"title":"What matters in building vision–language–action models for generalist robots | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01168-7"},{"title":"Towards Achieving Sub-linear Regret and Hard Constraint Violation in Model-free RL","url":"https://proceedings.mlr.press/v238/ghosh24a.html"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 27th International Conference on Artificial Intelligence and Statistics Held in Palau de Congressos, Valencia, Spain on 02-04 May 2024 Published as Volume 238 by the Proceedings of Machine Learning Research on 18 April 2024. Volume Edited by: Sanjoy Dasgupta Stephan Mandt Yingzhen Li Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v238/"},{"title":"Author Correction: Exploring online public survey lifestyle datasets with statistical analysis, machine learning and semantic ontology","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11810986/"},{"title":"Author Information · Robotics: Science and Systems","url":"https://roboticsconference.org/2024/information/authorinfo/"}]

Based on the search results, I found a reference to the Octo paper from RSS 2024. The paper "Octo: an open-source generalist robot policy" was presented at Robotics: Science and Systems (RSS) 2024 with authors including Ghosh, D. et al.

However, the search results don't provide the complete full list of all authors for the Octo RSS 2024 paper in PMLR proceedings format. The reference found appears in a Nature Machine Intelligence article citing the work, but it doesn't include the full author list. The Octo paper may not be formally published in PMLR proceedings yet, or the complete author information may require accessing the RSS 2024 proceedings directly or the paper itself.

If you need the complete author list, I recommend visiting the RSS 2024 conference proceedings directly or accessing the paper through the Robotics: Science and Systems conference website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "25abeb86-9151-4583-bfd4-b74d5d980342"
}
```

</details>

---


### Tool result

_source line 330 · 2026-05-29T06:32:48.190Z_

<details><summary>↩ Tool result · `toolu_011G6xcHYSbEwZhJ55F4zJRg`</summary>

```text
Web search results for query: "OpenVLA CoRL 2024 PMLR volume 270 publication year 2025 kim25c"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://proceedings.mlr.press/v270/kim25c.html"},{"title":"GitHub - mlresearch/v270: Proceedings of CoRL 2024","url":"https://github.com/mlresearch/v270"},{"title":"CoRL.2024 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/CoRL.2024"},{"title":"[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"}]

Based on the search results, I found the paper you're looking for:

**OpenVLA: An Open-Source Vision-Language-Action Model** was published in Proceedings of The 8th Conference on Robot Learning (CoRL 2024), PMLR Volume 270, pages 2679-2713, in 2025. The paper citation is kim25c.

OpenVLA is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.

The paper is authored by Kim, Moo Jin and multiple co-authors including Pertsch, Karamcheti, Xiao, and others, with the proceedings published on January 12, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "aa2ac90c-1829-4b4b-8599-a493a301a8b6"
}
```

</details>

---


### System

_source line 331_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for Efficient Streaming Language Models Attention Sin…",
  "usage": {
    "total_tokens": 26528,
    "tool_uses": 12,
    "duration_ms": 40776
  },
  "last_tool_name": "WebSearch",
  "uuid": "561af12e-0c67-4b6e-87c1-742bf7e8d12a",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 332_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G4zh7CNK6NtMTvMsuRL3Ta`</summary>

```json
{
  "query": "Efficient Streaming Language Models Attention Sinks Xiao Guangxuan ICLR 2024 arXiv 2309.17453"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "4d33a38b-7311-4e2d-8889-0a90dc8f928f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCmABxwyVL7d6UsUGbR64C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6621,
      "cache_read_input_tokens": 19313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6621,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-29T06:32:52.308Z_

<details><summary>↩ Tool result · `toolu_01CoqHs7EQ9KPM96KW6ezcLs`</summary>

```text
Web search results for query: "arxiv 2605.11817 "See What Matters" authors Feng Yixu"

Links: [{"title":"[2605.11817] See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/abs/2605.11817"},{"title":"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/html/2605.11817"},{"title":"Sample-Efficient Deep Learning for COVID-19 Diagnosis Based on CT Scans","url":"https://www.medrxiv.org/content/10.1101/2020.04.13.20063941.full.pdf"},{"title":"Advancing a Vision Foundation Model for Ming-Style Furniture Image Segmentation: A New Dataset and Method","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11722721/"},{"title":"Maximum Value Matters: Finding Hot Topics in Scholarly Fields","url":"https://arxiv.org/pdf/1710.06637"}]

Based on the search results, I found the paper you're looking for:

**Title:** "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

**Authors:** &lt;cite index="1-6">Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, and Chang Xu

**ArXiv ID:** 2605.11817

**Overview:** The paper addresses Vision-Language-Action (VLA) models and their high computational cost that hinders real-time deployment in robotics manipulation. The authors propose the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA.

The paper was submitted on May 12, 2026, with a revised version (v2) on May 17, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "cce38dbb-9f88-4cfc-98b6-10882871d0d9"
}
```

</details>

---


### Tool result

_source line 334 · 2026-05-29T06:32:52.391Z_

<details><summary>↩ Tool result · `toolu_01VZrfv1Db2YEaYyfzeotzPs`</summary>

```text
Web search results for query: "Compressor-VLA arxiv 2511.18950 year submitted 2025"

Links: [{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.10100"}]

Based on the search results, Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation is a paper with arxiv ID 2511.18950.

Regarding the submission year: The paper proposes a framework consisting of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. Based on the arxiv ID format (2511.18950), this indicates the paper was submitted in November 2025 (the "25" refers to 2025, and "11" refers to November).

The paper addresses the significant computational overhead of processing redundant visual tokens in Vision-Language-Action (VLA) models, proposing a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "2a4fa922-d0f6-41cd-b2dd-2e2f8a127c6f"
}
```

</details>

---


### System

_source line 335_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for CALVIN Benchmark Language-Conditioned Policy Lear…",
  "usage": {
    "total_tokens": 26570,
    "tool_uses": 13,
    "duration_ms": 42287
  },
  "last_tool_name": "WebSearch",
  "uuid": "b83ae6b3-afa6-44f0-bd76-59dbb35de518",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 336_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YZQcuwypSyDtbHuaAFZwFN`</summary>

```json
{
  "query": "CALVIN Benchmark Language-Conditioned Policy Learning Long-Horizon Robot Manipulation Mees Oier IEEE RA-L 2022 arXiv 2112.03227"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "aa1e761c-d715-40a1-92a3-42e7da21c889",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCmABxwyVL7d6UsUGbR64C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6621,
      "cache_read_input_tokens": 19313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6621,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 337_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for Diffusion Policy Visuomotor Policy Learning Actio…",
  "usage": {
    "total_tokens": 26612,
    "tool_uses": 14,
    "duration_ms": 43229
  },
  "last_tool_name": "WebSearch",
  "uuid": "a29445b1-89c5-4052-b975-2d581a7825dd",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 338_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PM4E2LPfuCgkdUHSQndxsr`</summary>

```json
{
  "query": "Diffusion Policy Visuomotor Policy Learning Action Diffusion Chi Cheng RSS 2023 arXiv 2303.04137"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "57793138-256e-43fa-98b0-b7575fe4eeea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCmABxwyVL7d6UsUGbR64C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6621,
      "cache_read_input_tokens": 19313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6621,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 339_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aa3d59cc440129695",
  "tool_use_id": "toolu_012SNg9wq7f6YSRDXZgo7Ry5",
  "status": "completed",
  "output_file": "",
  "summary": "Verify bib entries group 3",
  "usage": {
    "total_tokens": 25970,
    "tool_uses": 11,
    "duration_ms": 75060
  },
  "uuid": "608bbe05-f366-47b0-aeb8-8b6801708a8f",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool result

_source line 340 · 2026-05-29T06:32:54.214Z_

<details><summary>↩ Tool result · `toolu_012SNg9wq7f6YSRDXZgo7Ry5`</summary>

```text
Now I have all the information needed. Let me also confirm the ICLR 2022 paper's exact title formatting — it says "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" (plural "Reorganizations"), while the bib entry says "Token Reorganizations" — let me check if the cited title matches exactly.

The bib entry states the title as: "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" — this matches the actual title found on arXiv and OpenReview.

Here is the structured verification checklist:

---

## Reference Verification Checklist

### 1. chen2024fastv
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Liang Chen (note: surname is Chen, given name is Liang) |
| Title | MATCH | "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models" |
| Year | MATCH | 2024 |
| Venue | MATCH | ECCV 2024 (Oral) |
| arXiv ID | MATCH | 2403.06764 |
| Issues | None | |

---

### 2. xu2025vlacache
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Siyu Xu (GitHub username: siyuhsu) |
| Title | MATCH | "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching" |
| Year | MATCH | 2025 (arXiv Feb 2025, accepted NeurIPS 2025) |
| Venue | MATCH | NeurIPS 2025 |
| arXiv ID | 2502.02175 (not listed in bib entry, but correct if needed) |
| Issues | None | |

---

### 3. cheng2026vlaiap
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Jintao Cheng |
| Title | MATCH | "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models" |
| Year | MATCH | 2026 (submitted March 24, 2026) |
| Venue | N/A | arXiv preprint only (no conference acceptance found) |
| arXiv ID | MATCH | 2603.22991 |
| Issues | None | |

---

### 4. rao2021dynamicvit
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Yongming Rao |
| Title | MATCH | "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification" |
| Year | MATCH | 2021 |
| Venue | MATCH | NeurIPS 2021 |
| arXiv ID | 2106.02034 (not listed in bib entry) |
| Issues | None | |

---

### 5. bolya2023tome
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Daniel Bolya |
| Title | MATCH | "Token Merging: Your ViT But Faster" |
| Year | MATCH | 2023 |
| Venue | MATCH | ICLR 2023 |
| arXiv ID | 2210.09461 (not listed in bib entry) |
| Issues | None | |

---

### 6. liang2022evit
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Youwei Liang |
| Title | MATCH | "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" |
| Year | MATCH | 2022 |
| Venue | MATCH | ICLR 2022 (Spotlight) |
| arXiv ID | 2202.07800 (not listed in bib entry) |
| Issues | None | |

---

### 7. liu2023libero
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Bo Liu |
| Title | MATCH | "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" |
| Year | MATCH | 2023 |
| Venue | MATCH | NeurIPS 2023 (Datasets and Benchmarks Track) |
| arXiv ID | 2306.03310 (not listed in bib entry) |
| Issues | None | |

---

### 8. yang2025efficientvla
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Yantai Yang |
| Title | MATCH | "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models" |
| Year | MATCH | 2025 (June 11, 2025) |
| Venue | arXiv preprint; also appears on OpenReview (possibly under review) |
| arXiv ID | MATCH | 2506.10100 |
| Issues | None | |

---

## Summary

All 8 references verified successfully. No fabricated citations, no author mismatches, no title errors, no year or venue discrepancies. All entries are real, correctly attributed papers.

agentId: aa3d59cc440129695 (use SendMessage with to: 'aa3d59cc440129695' to continue this agent)
&lt;usage>total_tokens: 26969
tool_uses: 11
duration_ms: 75063&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "1f16403b-dd86-400f-a350-29669f4e4107",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. chen2024fastv: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\" by Chen, Liang and others. ECCV 2024, arXiv 2403.06764.\n\n2. xu2025vlacache: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" by Xu, Siyu and others. NeurIPS 2025.\n\n3. cheng2026vlaiap: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\" by Cheng, Jintao and others. arXiv 2603.22991, year 2026.\n\n4. rao2021dynamicvit: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\" by Rao, Yongming and others. NeurIPS 2021.\n\n5. bolya2023tome: \"Token Merging: Your ViT But Faster\" by Bolya, Daniel and others. ICLR 2023.\n\n6. liang2022evit: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" by Liang, Youwei and others. ICLR 2022.\n\n7. liu2023libero: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\" by Liu, Bo and others. NeurIPS 2023.\n\n8. yang2025efficientvla: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\" by Yang, Yantai and others. arXiv 2506.10100, year 2025.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found.",
    "agentId": "aa3d59cc440129695",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Let me also confirm the ICLR 2022 paper's exact title formatting — it says \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" (plural \"Reorganizations\"), while the bib entry says \"Token Reorganizations\" — let me check if the cited title matches exactly.\n\nThe bib entry states the title as: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" — this matches the actual title found on arXiv and OpenReview.\n\nHere is the structured verification checklist:\n\n---\n\n## Reference Verification Checklist\n\n### 1. chen2024fastv\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Authors | MATCH | First author is Liang Chen (note: surname is Chen, given name is Liang) |\n| Title | MATCH | \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\" |\n| Year | MATCH | 2024 |\n| Venue | MATCH | ECCV 2024 (Oral) |\n| arXiv ID | MATCH | 2403.06764 |\n| Issues | None | |\n\n---\n\n### 2. xu2025vlacache\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Authors | MATCH | First author is Siyu Xu (GitHub username: siyuhsu) |\n| Title | MATCH | \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" |\n| Year | MATCH | 2025 (arXiv Feb 2025, accepted NeurIPS 2025) |\n| Venue | MATCH | NeurIPS 2025 |\n| arXiv ID | 2502.02175 (not listed in bib entry, but correct if needed) |\n| Issues | None | |\n\n---\n\n### 3. cheng2026vlaiap\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Authors | MATCH | First author is Jintao Cheng |\n| Title | MATCH | \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\" |\n| Year | MATCH | 2026 (submitted March 24, 2026) |\n| Venue | N/A | arXiv preprint only (no conference acceptance found) |\n| arXiv ID | MATCH | 2603.22991 |\n| Issues | None | |\n\n---\n\n### 4. rao2021dynamicvit\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Authors | MATCH | First author is Yongming Rao |\n| Title | MATCH | \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\" |\n| Year | MATCH | 2021 |\n| Venue | MATCH | NeurIPS 2021 |\n| arXiv ID | 2106.02034 (not listed in bib entry) |\n| Issues | None | |\n\n---\n\n### 5. bolya2023tome\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Authors | MATCH | First author is Daniel Bolya |\n| Title | MATCH | \"Token Merging: Your ViT But Faster\" |\n| Year | MATCH | 2023 |\n| Venue | MATCH | ICLR 2023 |\n| arXiv ID | 2210.09461 (not listed in bib entry) |\n| Issues | None | |\n\n---\n\n### 6. liang2022evit\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Authors | MATCH | First author is Youwei Liang |\n| Title | MATCH | \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" |\n| Year | MATCH | 2022 |\n| Venue | MATCH | ICLR 2022 (Spotlight) |\n| arXiv ID | 2202.07800 (not listed in bib entry) |\n| Issues | None | |\n\n---\n\n### 7. liu2023libero\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Authors | MATCH | First author is Bo Liu |\n| Title | MATCH | \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\" |\n| Year | MATCH | 2023 |\n| Venue | MATCH | NeurIPS 2023 (Datasets and Benchmarks Track) |\n| arXiv ID | 2306.03310 (not listed in bib entry) |\n| Issues | None | |\n\n---\n\n### 8. yang2025efficientvla\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Authors | MATCH | First author is Yantai Yang |\n| Title | MATCH | \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\" |\n| Year | MATCH | 2025 (June 11, 2025) |\n| Venue | arXiv preprint; also appears on OpenReview (possibly under review) |\n| arXiv ID | MATCH | 2506.10100 |\n| Issues | None | |\n\n---\n\n## Summary\n\nAll 8 references verified successfully. No fabricated citations, no author mismatches, no title errors, no year or venue discrepancies. All entries are real, correctly attributed papers."
      }
    ],
    "totalDurationMs": 75063,
    "totalTokens": 26969,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1793,
      "cache_read_input_tokens": 23756,
      "output_tokens": 1419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1793
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1419,
          "cache_read_input_tokens": 23756,
          "cache_creation_input_tokens": 1793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1793,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 11
    }
  }
}
```

</details>

---


### System

_source line 341_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for \"Are Transformers Effective for Time Series Forec…",
  "usage": {
    "total_tokens": 26654,
    "tool_uses": 15,
    "duration_ms": 44716
  },
  "last_tool_name": "WebSearch",
  "uuid": "67a99eff-74f9-42e5-b12f-f05a16c797d2",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 342_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MAu21mQzyTLcVKCbm65RD3`</summary>

```json
{
  "query": "\"Are Transformers Effective for Time Series Forecasting\" Zeng Ailing AAAI 2023 arXiv 2205.13504"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "d46ef292-865e-44e2-995b-3d240957a9b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCmABxwyVL7d6UsUGbR64C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6621,
      "cache_read_input_tokens": 19313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6621,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-29T06:32:55.323Z_

<details><summary>↩ Tool result · `toolu_01E3ZYfko3jCGERQRXGnUnSj`</summary>

```text
Web search results for query: ""Don't Run with Scissors" Jabbour arxiv 2510.08464 venue conference accepted 2025 2026"

Links: [{"title":"[2510.08464] Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/abs/2510.08464"},{"title":"Running With Scissors - Therapy by Dr. Nathan Miller","url":"https://www.nathanmillertherapy.com/give-this-some-thought/running-with-scissors"},{"title":"Don’t Run With Scissors | Theo Heartist","url":"https://theoheartist.com/2021/06/14/dont-run-with-scissors/"},{"title":"Don't run with scissors: young children's knowledge of home safety rules | Request PDF","url":"https://www.researchgate.net/publication/12148912_Don't_run_with_scissors_young_children's_knowledge_of_home_safety_rules"},{"title":"Don't run with scissors: young children's knowledge of home safety rules - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/11181886/"},{"title":"Workshop Safety, a.k.a. Don't Run With Scissors","url":"https://www.kitplanes.com/running-with-scissors-shop-safety/"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered | OpenReview","url":"https://openreview.net/forum?id=c8g57pKdXD"},{"title":"Modeling and predicting single-cell multi-gene perturbation responses with scLAMBDA","url":"https://www.biorxiv.org/content/10.1101/2024.12.04.626878.full.pdf"},{"title":"Prompt injection attacks on vision-language models for surgical decision support","url":"https://www.medrxiv.org/content/10.1101/2025.07.16.25331645.full.pdf"},{"title":"Large Language Models for Detecting CONSORT Guideline Compliance in Published Randomized Clinical Trials: A Cross-Sectional Evaluation Study","url":"https://www.medrxiv.org/content/10.1101/2025.10.03.25337291.full.pdf"}]

Based on the search results, I found information about the paper "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" (arxiv 2510.08464):

The paper addresses Vision-Language-Action (VLA) models and shows that pruning VLA models leads to drastic degradation and increased safety violations. The authors introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits.

The method performs a one-time interpolation between dense and pruned models in weight-space to compute a corrective term, which is used during inference to recover lost capabilities with minimal overhead. GLUESTICK requires no additional training, is agnostic to the pruning algorithm, and introduces a single hyperparameter that controls the tradeoff between efficiency and accuracy.

The paper was submitted to arXiv on October 9, 2025 with authors Jason Jabbour, Dong-Ki Kim, Max Smith, Jay Patrikar, Radhika Ghosal, Youhui Wang, Ali Agha, Vijay Janapa Reddi, and Shayegan Omidshafiei.

Regarding venue and conference acceptance information: The search results show the paper on arXiv and OpenReview, but do not contain information about acceptance to a specific conference venue for 2025 or 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "f7bbf4f5-cb34-4f2c-91e6-9ed3a4f48218"
}
```

</details>

---


### System

_source line 344_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for \"Embracing Negative Results in Machine Learning\" …",
  "usage": {
    "total_tokens": 26696,
    "tool_uses": 16,
    "duration_ms": 45333
  },
  "last_tool_name": "WebSearch",
  "uuid": "171f23e6-4d98-455f-93f3-e6c975102831",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 345_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JEagJvf4CSSV395YMEhkBJ`</summary>

```json
{
  "query": "\"Embracing Negative Results in Machine Learning\" Bouthillier Xavier ICML 2024 arXiv 2406.03980"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "8ff2eb90-317f-4f84-9c5a-849e434df756",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCmABxwyVL7d6UsUGbR64C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6621,
      "cache_read_input_tokens": 19313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6621,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 346 · 2026-05-29T06:32:58.594Z_

<details><summary>↩ Tool result · `toolu_01G4zh7CNK6NtMTvMsuRL3Ta`</summary>

```text
Web search results for query: "Efficient Streaming Language Models Attention Sinks Xiao Guangxuan ICLR 2024 arXiv 2309.17453"

Links: [{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/5e5fd18f863cbe6d8ae392a93fd271c9-Abstract-Conference.html"},{"title":"GitHub - mit-han-lab/streaming-llm: [ICLR 2024] Efficient Streaming Language Models with Attention Sinks · GitHub","url":"https://github.com/mit-han-lab/streaming-llm"},{"title":"Efficient Streaming Language Models with Attention Sinks | OpenReview","url":"https://openreview.net/forum?id=NG7sS51zVF"},{"title":"[PDF] Efficient Streaming Language Models with Attention Sinks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Streaming-Language-Models-with-Attention-Xiao-Tian/fdc53c2c10742464087c0525f77e32604827a21d"},{"title":"[2309.17453] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453"},{"title":"efficient streaming language models","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/5e5fd18f863cbe6d8ae392a93fd271c9-Paper-Conference.pdf"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://hanlab.mit.edu/projects/streamingllm"},{"title":"Efficient streaming language models with at","url":"https://arxiv.org/pdf/2309.17453"},{"title":"Efficient Streaming Language Models with Attention Sinks Paper written by:","url":"https://minjiazhang.github.io/courses/sp24-resource/streaming-attention-sink-pre.pdf"}]

I found the paper you're looking for! Here's a summary of the search results:

"Efficient Streaming Language Models with Attention Sinks" is a paper by Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis, published at ICLR 2024. The paper is also available on arXiv as arXiv 2309.17453.

**Key Problem and Solution:**

The paper addresses challenges in deploying LLMs for streaming applications like multi-round dialogue, including memory consumption from caching Key and Value states during decoding and the inability of LLMs to generalize beyond training sequence length.

The authors observe an interesting phenomenon called "attention sink," where keeping the KV of initial tokens largely recovers the performance of window attention. StreamingLLM is an efficient framework that enables LLMs trained with finite length attention windows to generalize to infinite sequence lengths without fine-tuning, allowing models like Llama-2, MPT, Falcon, and Pythia to perform stable language modeling with up to 4 million tokens and more.

**Real-World Implementation:**

Attention Sink is integrated by HuggingFace Transformers' main branch, and StreamingLLM is integrated into NVIDIA TensorRT-LLM.

You can access the paper through the ICLR proceedings, arXiv (2309.17453), or the GitHub repository at https://github.com/mit-han-lab/streaming-llm.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "88f49985-de45-44e3-92ed-ae7aa3c5e6d7"
}
```

</details>

---


### System

_source line 347_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adda7656f92cca819",
  "tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "description": "Searching for SparseVILA Khaki \"Decoupled\" OR \"Decoupling\" exac…",
  "usage": {
    "total_tokens": 32143,
    "tool_uses": 20,
    "duration_ms": 95996
  },
  "last_tool_name": "WebSearch",
  "uuid": "1a8fcf2c-19ef-44c1-bd86-0cb5a46a5f47",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 348_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A4v72TMUuMjgkAjZPfsYnD`</summary>

```json
{
  "query": "SparseVILA Khaki \"Decoupled\" OR \"Decoupling\" exact title ICCV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "3b3b5862-f1e7-4538-8e3c-289c07521a7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BvQGYUa2DN8WmGjgFMtWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2185,
      "cache_read_input_tokens": 29381,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2185,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 349_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adda7656f92cca819",
  "tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "description": "Searching for arxiv 2605.11817 \"See What Matters\" ICML 2026 pos…",
  "usage": {
    "total_tokens": 32181,
    "tool_uses": 21,
    "duration_ms": 96175
  },
  "last_tool_name": "WebSearch",
  "uuid": "37a26ab6-a6ff-4b2f-b71c-ab3f49dadaeb",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 350_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YUB7vJ2CrwXVLYDkUq3KBn`</summary>

```json
{
  "query": "arxiv 2605.11817 \"See What Matters\" ICML 2026 poster accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "aa8c0343-9f2f-4614-957c-99dba9bf2dbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BvQGYUa2DN8WmGjgFMtWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2185,
      "cache_read_input_tokens": 29381,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2185,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-29T06:32:59.051Z_

<details><summary>↩ Tool result · `toolu_01YZQcuwypSyDtbHuaAFZwFN`</summary>

```text
Web search results for query: "CALVIN Benchmark Language-Conditioned Policy Learning Long-Horizon Robot Manipulation Mees Oier IEEE RA-L 2022 arXiv 2112.03227"

Links: [{"title":"[2112.03227] CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks","url":"https://arxiv.org/abs/2112.03227"},{"title":"[2112.03227v2] CALVIN: A Benchmark for Language-conditioned Policy Learning for Long-horizon Robot Manipulation Tasks","url":"https://arxiv.org/abs/2112.03227v2"},{"title":"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv211203227M/abstract"},{"title":"CALVIN: A Benchmark for Language-Conditioned Policy Learning for   Long-Horizon Robot Manipulation Tasks","url":"https://arxiv.org/pdf/2112.03227"},{"title":"CALVIN: Benchmark for Language-Driven Robot Tasks","url":"https://www.emergentmind.com/papers/2112.03227"},{"title":"Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks","url":"http://ais.informatik.uni-freiburg.de/publications/papers/mees22rsspi.pdf"},{"title":"(PDF) CALVIN: A Benchmark for Language-conditioned Policy Learning for Long-horizon Robot Manipulation Tasks","url":"https://www.researchgate.net/publication/356817042_CALVIN_A_Benchmark_for_Language-conditioned_Policy_Learning_for_Long-horizon_Robot_Manipulation_Tasks"}]

I found the paper you're searching for. Here's the information about it:

**CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks**

The paper is authored by Oier Mees, Lukas Hermann, Erick Rosete-Beas, and Wolfram Burgard.

**Overview:**
CALVIN (Composing Actions from Language and Vision) is an open-source simulated benchmark to learn long-horizon language-conditioned tasks. The aim is to develop agents that can solve many robotic manipulation tasks over a long horizon, from onboard sensors, and specified only via human language.

**Key Features:**
- CALVIN tasks are more complex in terms of sequence length, action space, and language than existing vision-and-language task datasets and support flexible specification of sensor suites
- CALVIN includes approximately 24 hours of teleoperated unstructured play data together with 20K language directives
- The simulation platform supports RGB-D images from both a static and a gripper camera, proprioceptive information, and vision-based tactile sensing

**Publication:**
The paper was accepted for publication at IEEE Robotics and Automation Letters (RAL), with arXiv identifier 2112.03227.

The paper and associated resources are available at http://calvin.cs.uni-freiburg.de.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "f6f208bf-77b5-46f4-bf57-2b462cf34e0c"
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-29T06:32:59.464Z_

<details><summary>↩ Tool result · `toolu_01PM4E2LPfuCgkdUHSQndxsr`</summary>

```text
Web search results for query: "Diffusion Policy Visuomotor Policy Learning Action Diffusion Chi Cheng RSS 2023 arXiv 2303.04137"

Links: [{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"},{"title":"[2303.04137v1] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137v1"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"[2303.04137v3] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137v3"},{"title":"[2303.04137v5] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137v5"},{"title":"[2303.04137v4] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137v4"},{"title":"Paper page - Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://huggingface.co/papers/2303.04137"},{"title":"[2303.04137] Diffusion Policy - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2303.04137"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"}]

I found the paper you're searching for! Here's the information:

## Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process.

**Authors:** Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, and Shuran Song (with later versions adding Russ Tedrake)

**Publication:** Robotics: Science and Systems (RSS) 2023

**arXiv Identifier:** 2303.04137 (first submitted March 7, 2023)

**Key Contributions:** The diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability. The paper presents key technical contributions including the incorporation of receding horizon control, visual conditioning, and the time-series diffusion transformer.

**Results:** The paper benchmarked Diffusion Policy across 12 different tasks from 4 different robot manipulation benchmarks and found that it consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9%.

The paper also has an official project website at https://diffusion-policy.cs.columbia.edu/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "ced0c802-326c-4c4d-9398-464921db3342"
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-29T06:33:00.080Z_

<details><summary>↩ Tool result · `toolu_01MAu21mQzyTLcVKCbm65RD3`</summary>

```text
Web search results for query: ""Are Transformers Effective for Time Series Forecasting" Zeng Ailing AAAI 2023 arXiv 2205.13504"

Links: [{"title":"Yes, Transformers are Effective for Time Series Forecasting (+ Autoformer)","url":"https://huggingface.co/blog/autoformer"},{"title":"Are Transformers Effective for Time Series Forecasting? - R Discovery","url":"https://discovery.researcher.life/article/are-transformers-effective-for-time-series-forecasting/55dd0976743c3dbea291291e7d41dc3f"},{"title":"Aaai","url":"https://ojs.aaai.org/index.php/AAAI/citationstylelanguage/get/apa?submissionId=26317&publicationId=24597"},{"title":"Are Transformers Effective for Time Series Forecasting? | Request PDF","url":"https://www.researchgate.net/publication/371915865_Are_Transformers_Effective_for_Time_Series_Forecasting"},{"title":"GitHub - cure-lab/LTSF-Linear: [AAAI-23 Oral] Official implementation of the paper \"Are Transformers Effective for Time Series Forecasting?\" · GitHub","url":"https://github.com/cure-lab/LTSF-Linear"},{"title":"Are transformers effective for time series forecasting? | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i9.26317"},{"title":"Are Transformers Effective for Time Series Forecasting?","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26317/26089"},{"title":"[PDF] Are Transformers Effective for Time Series Forecasting? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Are-Transformers-Effective-for-Time-Series-Zeng-Chen/5f404dbba07619cc7f28d75d03f124a52290046e"},{"title":"Are Transformers Effective for Time Series Forecasting? | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26317"}]

I've found the paper you're looking for. Here's what I found:

"Are Transformers Effective for Time Series Forecasting?" by Zeng, A., Chen, M., Zhang, L., and Xu, Q. was published in 2023 in the Proceedings of the AAAI Conference on Artificial Intelligence, volume 37, issue 9, pages 11121-11128.

In the paper, the authors claim that Transformers are not effective for time series forecasting. Experimental results on nine real-life datasets show that LTSF-Linear surprisingly outperforms existing sophisticated Transformer-based LTSF models in all cases, and often by a large margin.

While positional encoding and token embeddings help preserve ordering information, the permutation-invariant nature of self-attention mechanisms inevitably results in temporal information loss.

The paper received recognition, with acceptance to AAAI 2023 with three strong accept ratings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "8a2af10b-723c-48f5-8b73-f03cbf3cfaf5"
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-29T06:33:02.316Z_

<details><summary>↩ Tool result · `toolu_01JEagJvf4CSSV395YMEhkBJ`</summary>

```text
Web search results for query: ""Embracing Negative Results in Machine Learning" Bouthillier Xavier ICML 2024 arXiv 2406.03980"

Links: [{"title":"Position: Embracing Negative Results in Machine Learning | OpenReview","url":"https://openreview.net/forum?id=3RXAiU7sss"},{"title":"ICML Poster Position: Embracing Negative Results in Machine Learning","url":"https://icml.cc/virtual/2024/poster/35063"},{"title":"[ICML 2024] Position: Embracing Negative Results in Machine Learning - YouTube","url":"https://www.youtube.com/watch?v=JDP6cXWmChI"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://proceedings.mlr.press/v235/karl24a.html"},{"title":"[2406.03980] Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/abs/2406.03980"},{"title":"ICML 2024 Schedule","url":"https://icml.cc/virtual/2024/calendar"},{"title":"(PDF) Position: Embracing Negative Results in Machine Learning","url":"https://www.researchgate.net/publication/381226301_Position_Embracing_Negative_Results_in_Machine_Learning"},{"title":"dblp: Position: Embracing Negative Results in Machine Learning.","url":"https://dblp.org/rec/journals/corr/abs-2406-03980.html"},{"title":"Negative chemical data boosts language models in reaction outcome prediction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12164950/"}]

I found the paper! Here are the search results for "Embracing Negative Results in Machine Learning" with arXiv ID 2406.03980 from ICML 2024:

**Paper Details:**
- Authors: Florian Karl, Lukas Malte Kemeter, Gabriel Dax, and Paulina Sierak
- arXiv: 2406.03980v1, submitted June 6, 2024
- Published in Proceedings of the 41st International Conference on Machine Learning, PMLR 235:23256-23265, 2024

**Main Argument:**
The position paper argues that predictive performance alone is not a good indicator for the worth of a publication, and using it as such fosters problems like inefficiencies of the machine learning research community as a whole and sets wrong incentives for researchers.

**Call to Action:**
The authors put out a call for the publication of "negative" results, which can help alleviate some of these problems and improve the scientific output of the machine learning research community, presenting advantages of publishing negative results and providing concrete measures for the community to move towards a paradigm where their publication is normalized.

The paper is available on multiple platforms including arXiv (arxiv.org/abs/2406.03980), OpenReview, and the ICML proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "4c886dc2-72c7-4a01-a396-5494c2941a40"
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-29T06:33:04.680Z_

<details><summary>↩ Tool result · `toolu_01A4v72TMUuMjgkAjZPfsYnD`</summary>

```text
Web search results for query: "SparseVILA Khaki "Decoupled" OR "Decoupling" exact title ICCV 2025"

Links: [{"title":"[2510.17777] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/abs/2510.17777"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"ICCV Poster SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://iccv.thecvf.com/virtual/2025/poster/1739"},{"title":"Training-Free Sparse Attention for Fast Video Generation via Offline Layer-Wise Sparsity Profiling and Online Bidirectional Co-Clustering","url":"https://arxiv.org/pdf/2603.18636"},{"title":"ICCV Poster DecAD: Decoupling Anomalies in Latent Space for Multi-Class Unsupervised Anomaly Detection","url":"https://iccv.thecvf.com/virtual/2025/poster/362"}]

I found the paper you're looking for! 

SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference is authored by Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Konstantinos Plataniotis, Yao Lu, Song Han, and Zhijian Liu. 

SparseVILA presents a new paradigm for efficient VLM inference that decouples visual sparsity across the prefilling and decoding stages. The method achieves up to 4.0 times faster prefilling, 2.5 times faster decoding, and an overall 2.6 times end-to-end speedup on long-context video tasks while improving accuracy on document-understanding and reasoning tasks.

The paper has been published at ICCV 2025 and is available on arXiv (paper ID: 2510.17777).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "782f5555-c983-45ea-b31d-489ff57c66fb"
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-29T06:33:06.821Z_

<details><summary>↩ Tool result · `toolu_01YUB7vJ2CrwXVLYDkUq3KBn`</summary>

```text
Web search results for query: "arxiv 2605.11817 "See What Matters" ICML 2026 poster accepted"

Links: [{"title":"[2605.11817] See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/abs/2605.11817"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"Stop Automating Peer Review Without Rigorous Evaluation","url":"https://arxiv.org/html/2605.03202v1"},{"title":"MLLMs Know Where to Look: Training-free Perception of Small Visual   Details with Multimodal LLMs","url":"https://arxiv.org/pdf/2502.17422"},{"title":"A Two-Stage Approach to Important Area Detection in Gathering Place Using a Novel Multi-Input Attention Network","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8749720/"},{"title":"OpenNovelty: An LLM-powered Agentic System for Verifiable Scholarly Novelty Assessment","url":"https://arxiv.org/pdf/2601.01576"}]

Based on the search results, I found information about the paper arxiv 2605.11817:

The paper titled "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" is by Yixu Feng and 6 other authors. The paper addresses Vision-Language-Action (VLA) models in robotics manipulation, which have shown promise but have high computational costs that hinder real-time deployment.

The paper proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA. By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression.

The paper was submitted to arXiv on May 12, 2026 with the latest revision on May 17, 2026.

However, I was unable to find specific information in the search results confirming whether this paper was accepted as a poster at ICML 2026. The search results show the arXiv paper but do not contain details about ICML 2026 acceptance decisions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "0644591b-21b6-4e89-bad1-9f20101c89fa"
}
```

</details>

---


### System

_source line 357_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for DINOv2 Oquab 2024 TMLR Transactions Machine Learn…",
  "usage": {
    "total_tokens": 31326,
    "tool_uses": 17,
    "duration_ms": 57551
  },
  "last_tool_name": "WebSearch",
  "uuid": "93da7eb1-0623-4447-8175-454af0650d64",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 358_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WBT2Mz6X4x6VtCTubWgg6S`</summary>

```json
{
  "query": "DINOv2 Oquab 2024 TMLR Transactions Machine Learning Research published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "27121362-6924-4a6b-bd28-245b5ace443f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAfzVRZ9tZdJa5Xdbr783X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4628,
      "cache_read_input_tokens": 25934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4628,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 359_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for RT-2 CoRL 2023 proceedings first author Zitkovich…",
  "usage": {
    "total_tokens": 31327,
    "tool_uses": 18,
    "duration_ms": 57939
  },
  "last_tool_name": "WebSearch",
  "uuid": "d43c5754-810d-4b78-afba-090c6254b531",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 360_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HmKZCiNFD98Nie9TGH58oB`</summary>

```json
{
  "query": "RT-2 CoRL 2023 proceedings first author Zitkovich Brohan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "2bb22671-f52a-4804-b27f-cae5bd24e63e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAfzVRZ9tZdJa5Xdbr783X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4628,
      "cache_read_input_tokens": 25934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4628,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 361_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for \"Position: Embracing Negative Results\" Bouthillie…",
  "usage": {
    "total_tokens": 31328,
    "tool_uses": 19,
    "duration_ms": 59085
  },
  "last_tool_name": "WebSearch",
  "uuid": "6a9da066-9dd4-49ba-9f78-4e8f56504031",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 362_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SsZy4Hih8G2S899A9mCbAP`</summary>

```json
{
  "query": "\"Position: Embracing Negative Results\" Bouthillier Xavier author ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "ba039e86-9752-484b-bece-e3c099b68fe6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAfzVRZ9tZdJa5Xdbr783X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4628,
      "cache_read_input_tokens": 25934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4628,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 363_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for CALVIN Mees 2022 IEEE RA-L Robotics Automation Le…",
  "usage": {
    "total_tokens": 31329,
    "tool_uses": 20,
    "duration_ms": 59409
  },
  "last_tool_name": "WebSearch",
  "uuid": "9b611ca6-0ada-4f64-84e1-ee3d43b5d21d",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 364_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KeS8J6fwhn7gwNErUEL99U`</summary>

```json
{
  "query": "CALVIN Mees 2022 IEEE RA-L Robotics Automation Letters publication year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "aa291647-ca06-4e5d-8b10-1b8e85bcac2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAfzVRZ9tZdJa5Xdbr783X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4628,
      "cache_read_input_tokens": 25934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4628,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 365_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for arXiv 2305.17455 CrossGET authors Shi Dachuan fir…",
  "usage": {
    "total_tokens": 31330,
    "tool_uses": 21,
    "duration_ms": 60316
  },
  "last_tool_name": "WebSearch",
  "uuid": "a2c3f523-0dbb-4d8c-ac3e-1ca936878726",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 366_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W4ivSkrdKtmdC92urAHRTe`</summary>

```json
{
  "query": "arXiv 2305.17455 CrossGET authors Shi Dachuan first author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "5b7c4d1d-e4f5-4c7d-b749-8ed21b792577",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAfzVRZ9tZdJa5Xdbr783X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4628,
      "cache_read_input_tokens": 25934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4628,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-29T06:33:12.793Z_

<details><summary>↩ Tool result · `toolu_01HmKZCiNFD98Nie9TGH58oB`</summary>

```text
Web search results for query: "RT-2 CoRL 2023 proceedings first author Zitkovich Brohan"

Links: [{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"Papers — CoRL 2023","url":"https://www.corl2023.org/papers"},{"title":"Real-time open-vocabulary perception for mobile robots on edge devices: a systematic analysis of the accuracy-latency trade-off - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12583037/"},{"title":"Advancing general robotic manipulation with multimodal foundation models: An embodied AI paradigm | Science China Technological Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11431-024-2910-3"},{"title":"RT-2: Vision-Language-Action Models Transfer Web ...","url":"https://arxiv.org/pdf/2307.15818"}]

Based on the search results, I found the information about the RT-2 paper from the CoRL 2023 proceedings. 

Brianna Zitkovich is listed as the first author of the RT-2 paper in the CoRL 2023 proceedings, with Anthony Brohan among the co-authors. 

The full title is "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" and it was published in the Proceedings of The 7th Conference on Robot Learning, in Proceedings of Machine Learning Research 229:2165-2183.

The authors are listed in alphabetical order, with contributions listed in Appendix A.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "15eae128-5107-4904-a126-0d531c1f2b34"
}
```

</details>

---


### Tool result

_source line 368 · 2026-05-29T06:33:15.553Z_

<details><summary>↩ Tool result · `toolu_01WBT2Mz6X4x6VtCTubWgg6S`</summary>

```text
Web search results for query: "DINOv2 Oquab 2024 TMLR Transactions Machine Learning Research published venue"

Links: [{"title":"DINOv2: Learning Robust Visual Features Without Supervision | ML Anthology","url":"https://mlanthology.org/tmlr/2024/oquab2024tmlr-dinov2/"},{"title":"Published in Transactions on Machine Learning Research (05/2024)","url":"https://openreview.net/pdf/129f9aa6abb956d6b52bcae0458ab67f1ebad847.pdf"},{"title":"Transactions on Machine Learning Research on X: \"Outstanding Finalist 2: “DINOv2: Learning Robust Visual Features without Supervision,\" by Maxime Oquab, Timothée Darcet (@TimDarcet), Théo Moutakanni (@TheoMoutakanni) et al. 5/n https://t.co/XBQJk03R8R\" / X","url":"https://x.com/TmlrOrg/status/1869867717953483138"},{"title":"A generalised vision transformer-based self-supervised model for diagnosing and grading prostate cancer using histological images | Prostate Cancer and Prostatic Diseases","url":"https://www.nature.com/articles/s41391-025-00957-w"},{"title":"dblp: Transactions on Machine Learning Research, Volume 2024","url":"https://dblp.org/db/journals/tmlr/tmlr2024.html"},{"title":"DINOv2: Learning Robust Visual Features without Supervision | by Jim Canary | Medium","url":"https://medium.com/@jimcanary/dinov2-learning-robust-visual-features-without-supervision-bfd1cd94cbdd"},{"title":"[2304.07193] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193"},{"title":"DINOv2: Learning Robust Visual Features without Supervision | OpenReview","url":"https://openreview.net/forum?id=a68SUt6zFt"},{"title":"Published in Transactions on Machine Learning Research (01/2024)","url":"https://arxiv.org/pdf/2304.07193"}]

Based on the search results, I found information about the DINOv2 paper by Oquab et al. and its publication venue:

DINOv2: Learning Robust Visual Features Without Supervision was published in Transactions on Machine Learning Research in 2024. The paper was authored by Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy V. Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, Mido Assran, Nicolas Ballas, Wojciech Galuba, Russell Howes, Po-Yao Huang, Shang-Wen Li, Ishan Misra, Michael Rabbat, Vasu Sharma, Gabriel Synnaeve, Hu Xu, Hervé Jégou, Julien Mairal, Patrick Labatut, Armand Joulin, and Piotr Bojanowski.

The paper demonstrates that existing pretraining methods, especially self-supervised methods, can produce all-purpose visual features that work across image distributions and tasks without finetuning if trained on enough curated data from diverse sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "10c8334e-46f2-4f28-8aab-e565eb3bdedd"
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-29T06:33:15.822Z_

<details><summary>↩ Tool result · `toolu_01W4ivSkrdKtmdC92urAHRTe`</summary>

```text
Web search results for query: "arXiv 2305.17455 CrossGET authors Shi Dachuan first author list"

Links: [{"title":"[2305.17455] CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers","url":"https://arxiv.org/abs/2305.17455"},{"title":"GitHub - sdc17/CrossGET: [ICML 2024] CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers · GitHub","url":"https://github.com/sdc17/crossget"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers | Request PDF","url":"https://www.researchgate.net/publication/371136150_CrossGET_Cross-Guided_Ensemble_of_Tokens_for_Accelerating_Vision-Language_Transformers"},{"title":"dblp: Dachuan Shi","url":"https://dblp.org/pid/283/0549.html"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers","url":"https://arxiv.org/html/2305.17455"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers | OpenReview","url":"https://openreview.net/forum?id=CSIfCpXhCF"}]

Based on the search results, here are the authors of the CrossGET paper (arXiv 2305.17455) in order:

1. Dachuan Shi
2. Chaofan Tao
3. Anyi Rao
4. Zhendong Yang
5. Chun Yuan
6. Jiaqi Wang

Dachuan Shi is the first author, and the paper presents Cross-Guided Ensemble of Tokens (CrossGET), a general acceleration framework for vision-language Transformers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "b363ce39-5101-48b4-af8e-17d1e474d100"
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-29T06:33:17.145Z_

<details><summary>↩ Tool result · `toolu_01SsZy4Hih8G2S899A9mCbAP`</summary>

```text
Web search results for query: ""Position: Embracing Negative Results" Bouthillier Xavier author ICML 2024"

Links: [{"title":"Position: Embracing Negative Results in Machine Learning | OpenReview","url":"https://openreview.net/forum?id=3RXAiU7sss"},{"title":"ICML Poster Position: Embracing Negative Results in Machine Learning","url":"https://icml.cc/virtual/2024/poster/35063"},{"title":"[ICML 2024] Position: Embracing Negative Results in Machine Learning - YouTube","url":"https://www.youtube.com/watch?v=JDP6cXWmChI"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://proceedings.mlr.press/v235/karl24a.html"},{"title":"ICML 2024 Schedule","url":"https://icml.cc/virtual/2024/calendar"},{"title":"[2406.03980] Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/abs/2406.03980"},{"title":"(PDF) Position: Embracing Negative Results in Machine Learning","url":"https://www.researchgate.net/publication/381226301_Position_Embracing_Negative_Results_in_Machine_Learning"},{"title":"Negativity towards negative results: a discussion of the disconnect between scientific worth and scientific culture","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3917235/"}]

I found information about the paper "Position: Embracing Negative Results in Machine Learning" presented at ICML 2024. However, I should note that the authors listed in the search results are **Florian Karl, Malte Kemeter, Gabriel Dax, and Paulina Sierak**, not Xavier Bouthillier as mentioned in your query.

Here's what the paper is about:

The paper was published at ICML 2024, and it argues that predictive performance alone is not a good indicator for the worth of a publication, and that using it as such fosters problems like inefficiencies of the machine learning research community and wrong incentives for researchers.

The authors call for the publication of "negative" results, which can help alleviate some of these problems and improve scientific output of the machine learning research community, and they present advantages of publishing negative results along with concrete measures for normalizing their publication.

The paper is available on multiple platforms including OpenReview, arXiv (2406.03980), and the ICML proceedings (PMLR 235:23256-23265).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "89a106d7-986d-4fff-b2fe-45be0c625086"
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-29T06:33:18.906Z_

<details><summary>↩ Tool result · `toolu_01KeS8J6fwhn7gwNErUEL99U`</summary>

```text
Web search results for query: "CALVIN Mees 2022 IEEE RA-L Robotics Automation Letters publication year"

Links: [{"title":"GitHub - mees/calvin: CALVIN - A benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks","url":"https://github.com/mees/calvin?tab=readme-ov-file"},{"title":"GitHub - mees/calvin: CALVIN - A benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks · GitHub","url":"https://github.com/mees/calvin"},{"title":"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022IRAL....7.7327M/abstract"},{"title":"IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED JULY, 2022 1","url":"https://arxiv.org/pdf/2204.06252"},{"title":"RA-L Paper Awards - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/publications/ra-l/ra-l-paper-awards/"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Calvin:+a+benchmark+for+language-conditioned+policy+learning+for+long-horizon+robot+manipulation+tasks&amp=&author=O+Mees&amp=&author=L+Hermann&amp=&author=E+Rosete-Beas&amp=&publication_year=2022&amp=&journal=IEEE+Robotics+and+Automation+Letters&amp=&pages=7327-7334&amp=&doi=10.1109/LRA.2022.3180108"},{"title":"Oier Mees","url":"https://www.oiermees.com/"},{"title":"IEEE Robotics and Automation Letters (RA-L)","url":"https://www.myhuiban.com/journal/1037?lang=en_us"}]

Based on the search results, the CALVIN paper by Mees et al. was published in IEEE Robotics and Automation Letters (RA-L) in 2022, specifically in volume 7, number 3, pages 7327-7334. More specifically, the publication was in July 2022.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "99c54220-fdbd-4e4b-a4ee-c1f87810b3d6"
}
```

</details>

---


### System

_source line 372_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ae7c854fbb04eafdf",
  "tool_use_id": "toolu_01AiUWsBMHdDKydMCo1apoX4",
  "status": "completed",
  "output_file": "",
  "summary": "Verify bib entries group 4",
  "usage": {
    "total_tokens": 27018,
    "tool_uses": 13,
    "duration_ms": 94812
  },
  "uuid": "fa8ad673-8f8e-49a1-80ae-965f911ab137",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool result

_source line 373 · 2026-05-29T06:33:21.750Z_

<details><summary>↩ Tool result · `toolu_01AiUWsBMHdDKydMCo1apoX4`</summary>

```text
Here is the structured verification checklist for all 8 references:

---

## Reference Verification Checklist

### 1. liu2025vlapruner — VLA-Pruner
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | YES | "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference" — exact match |
| Authors match | YES | First author is Liu, Ziyan — confirmed |
| Year match | **ISSUE** | arXiv submission date is **Nov 2025**, but the arXiv ID prefix `2511` means Nov 2025. The bib key says 2025, which is technically correct for the submission year. However, the latest revision is Feb 2026. The year 2025 is acceptable as the original submission year. |
| Venue match | N/A | No venue claimed (arXiv preprint) |
| arXiv ID match | YES | 2511.16449 confirmed |

**Verdict: OK.** No issues.

---

### 2. shang2024prumerge — LLaVA-PruMerge
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | YES | "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models" — exact match |
| Authors match | YES | Shang, Yuzhang is first author. Co-authors: Mu Cai, Bingxin Xu, Yong Jae Lee, Yan Yan |
| Year match | **ISSUE** | Bib key says `2024`, venue listed as ICCV 2025. The arXiv submission is Mar 2024, but the published venue is **ICCV 2025**. The year in the bibliography entry should be **2025** to match the publication venue. |
| Venue match | YES | ICCV 2025 confirmed via CVF Open Access |
| arXiv ID | Not given in entry | arXiv: 2403.15388 |

**Verdict: Year inconsistency.** The bib key `shang2024prumerge` implies year 2024, but the venue is ICCV 2025. The bibliography year should be **2025**.

---

### 3. liu2023llava — Visual Instruction Tuning
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | YES | "Visual Instruction Tuning" — exact match |
| Authors match | YES | Liu, Haotian; Li, Chunyuan; Wu, Qingyang; Lee, Yong Jae — all confirmed |
| Year match | YES | NeurIPS 2023 — confirmed |
| Venue match | YES | NeurIPS 2023 (Oral) — confirmed |
| arXiv ID | Not given | arXiv: 2304.08485 |

**Verdict: OK.** No issues.

---

### 4. shi2016subpixel — Sub-Pixel CNN
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | YES | "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network" — exact match |
| Authors match | YES | Shi, Wenzhe is first author — confirmed |
| Year match | YES | CVPR 2016 — confirmed |
| Venue match | YES | CVPR 2016 — confirmed |
| arXiv ID | Not given | arXiv: 1609.05158 |

**Verdict: OK.** No issues.

---

### 5. li2023blip2 — BLIP-2
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | **MINOR ISSUE** | Bib entry has "Pre-Training" but the official ICML title uses "Pre-training" (lowercase 't'). This is cosmetic and venue-dependent. |
| Authors match | YES | Li, Junnan is first author. Co-authors: Dongxu Li, Silvio Savarese, Steven Hoi — confirmed |
| Year match | YES | ICML 2023 — confirmed |
| Venue match | YES | ICML 2023 — confirmed |
| arXiv ID | Not given | arXiv: 2301.12597 |

**Verdict: OK.** Minor capitalization variant in title only.

---

### 6. zhai2023siglip — SigLIP
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | YES | "Sigmoid Loss for Language Image Pre-Training" — exact match |
| Authors match | YES | Zhai, Xiaohua is first author — confirmed |
| Year match | YES | ICCV 2023 — confirmed |
| Venue match | YES | ICCV 2023 — confirmed |
| arXiv ID | Not given | arXiv: 2303.15343 |

**Verdict: OK.** No issues.

---

### 7. yang2024qwen2 — Qwen2 Technical Report
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | YES | "Qwen2 Technical Report" — exact match |
| Authors match | YES | Yang, An is first author — confirmed |
| Year match | YES | 2024 (arXiv submission Jul 2024) — confirmed |
| Venue match | N/A | arXiv preprint, no formal venue |
| arXiv ID match | YES | 2407.10671 — confirmed |

**Verdict: OK.** No issues.

---

### 8. lipman2023flow — Flow Matching
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | YES | "Flow Matching for Generative Modeling" — exact match |
| Authors match | YES | Lipman, Yaron is first author — confirmed |
| Year match | YES | ICLR 2023 — confirmed |
| Venue match | YES | ICLR 2023 — confirmed |
| arXiv ID | Not given | arXiv: 2210.02747 |

**Verdict: OK.** No issues.

---

## Summary

| # | Bib Key | Status | Action Required |
|---|---------|--------|-----------------|
| 1 | liu2025vlapruner | OK | None |
| 2 | shang2024prumerge | **FIX NEEDED** | Change year from 2024 to **2025** to match ICCV 2025 publication venue |
| 3 | liu2023llava | OK | None |
| 4 | shi2016subpixel | OK | None |
| 5 | li2023blip2 | OK | None (minor capitalization variant is acceptable) |
| 6 | zhai2023siglip | OK | None |
| 7 | yang2024qwen2 | OK | None |
| 8 | lipman2023flow | OK | None |

**One actionable issue found:** Entry #2 (`shang2024prumerge`) has a year mismatch — the bib key and year field say 2024, but the paper was published at ICCV 2025. The year should be updated to 2025, and ideally the bib key renamed to `shang2025prumerge`.

Sources:
- [VLA-Pruner on arXiv](https://arxiv.org/abs/2511.16449)
- [LLaVA-PruMerge on arXiv](https://arxiv.org/abs/2403.15388)
- [LLaVA-PruMerge at ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Shang_LLaVA-PruMerge_Adaptive_Token_Reduction_for_Efficient_Large_Multimodal_Models_ICCV_2025_paper.html)
- [Visual Instruction Tuning at NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf)
- [Sub-Pixel CNN at CVPR 2016](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Shi_Real-Time_Single_Image_CVPR_2016_paper.html)
- [BLIP-2 at ICML 2023](https://proceedings.mlr.press/v202/li23q.html)
- [SigLIP at ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/html/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.html)
- [Qwen2 Technical Report on arXiv](https://arxiv.org/abs/2407.10671)
- [Flow Matching at ICLR 2023](https://iclr.cc/virtual/2023/poster/11309)

agentId: ae7c854fbb04eafdf (use SendMessage with to: 'ae7c854fbb04eafdf' to continue this agent)
&lt;usage>total_tokens: 28871
tool_uses: 13
duration_ms: 94816&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "6359a36c-08b4-482a-8a8a-1c1c23cdfba3",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. liu2025vlapruner: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\" by Liu, Ziyan and others. arXiv 2511.16449, year 2025.\n\n2. shang2024prumerge: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\" by Shang, Yuzhang and others. Listed as ICCV 2025, but bib key says 2024.\n\n3. liu2023llava: \"Visual Instruction Tuning\" by Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae. NeurIPS 2023.\n\n4. shi2016subpixel: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" by Shi, Wenzhe and others. CVPR 2016.\n\n5. li2023blip2: \"BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models\" by Li, Junnan and others. ICML 2023.\n\n6. zhai2023siglip: \"Sigmoid Loss for Language Image Pre-Training\" by Zhai, Xiaohua and others. ICCV 2023.\n\n7. yang2024qwen2: \"Qwen2 Technical Report\" by Yang, An and others. arXiv 2407.10671, year 2024.\n\n8. lipman2023flow: \"Flow Matching for Generative Modeling\" by Lipman, Yaron and others. ICLR 2023.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found.",
    "agentId": "ae7c854fbb04eafdf",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the structured verification checklist for all 8 references:\n\n---\n\n## Reference Verification Checklist\n\n### 1. liu2025vlapruner — VLA-Pruner\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Title match | YES | \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\" — exact match |\n| Authors match | YES | First author is Liu, Ziyan — confirmed |\n| Year match | **ISSUE** | arXiv submission date is **Nov 2025**, but the arXiv ID prefix `2511` means Nov 2025. The bib key says 2025, which is technically correct for the submission year. However, the latest revision is Feb 2026. The year 2025 is acceptable as the original submission year. |\n| Venue match | N/A | No venue claimed (arXiv preprint) |\n| arXiv ID match | YES | 2511.16449 confirmed |\n\n**Verdict: OK.** No issues.\n\n---\n\n### 2. shang2024prumerge — LLaVA-PruMerge\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Title match | YES | \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\" — exact match |\n| Authors match | YES | Shang, Yuzhang is first author. Co-authors: Mu Cai, Bingxin Xu, Yong Jae Lee, Yan Yan |\n| Year match | **ISSUE** | Bib key says `2024`, venue listed as ICCV 2025. The arXiv submission is Mar 2024, but the published venue is **ICCV 2025**. The year in the bibliography entry should be **2025** to match the publication venue. |\n| Venue match | YES | ICCV 2025 confirmed via CVF Open Access |\n| arXiv ID | Not given in entry | arXiv: 2403.15388 |\n\n**Verdict: Year inconsistency.** The bib key `shang2024prumerge` implies year 2024, but the venue is ICCV 2025. The bibliography year should be **2025**.\n\n---\n\n### 3. liu2023llava — Visual Instruction Tuning\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Title match | YES | \"Visual Instruction Tuning\" — exact match |\n| Authors match | YES | Liu, Haotian; Li, Chunyuan; Wu, Qingyang; Lee, Yong Jae — all confirmed |\n| Year match | YES | NeurIPS 2023 — confirmed |\n| Venue match | YES | NeurIPS 2023 (Oral) — confirmed |\n| arXiv ID | Not given | arXiv: 2304.08485 |\n\n**Verdict: OK.** No issues.\n\n---\n\n### 4. shi2016subpixel — Sub-Pixel CNN\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Title match | YES | \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" — exact match |\n| Authors match | YES | Shi, Wenzhe is first author — confirmed |\n| Year match | YES | CVPR 2016 — confirmed |\n| Venue match | YES | CVPR 2016 — confirmed |\n| arXiv ID | Not given | arXiv: 1609.05158 |\n\n**Verdict: OK.** No issues.\n\n---\n\n### 5. li2023blip2 — BLIP-2\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Title match | **MINOR ISSUE** | Bib entry has \"Pre-Training\" but the official ICML title uses \"Pre-training\" (lowercase 't'). This is cosmetic and venue-dependent. |\n| Authors match | YES | Li, Junnan is first author. Co-authors: Dongxu Li, Silvio Savarese, Steven Hoi — confirmed |\n| Year match | YES | ICML 2023 — confirmed |\n| Venue match | YES | ICML 2023 — confirmed |\n| arXiv ID | Not given | arXiv: 2301.12597 |\n\n**Verdict: OK.** Minor capitalization variant in title only.\n\n---\n\n### 6. zhai2023siglip — SigLIP\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Title match | YES | \"Sigmoid Loss for Language Image Pre-Training\" — exact match |\n| Authors match | YES | Zhai, Xiaohua is first author — confirmed |\n| Year match | YES | ICCV 2023 — confirmed |\n| Venue match | YES | ICCV 2023 — confirmed |\n| arXiv ID | Not given | arXiv: 2303.15343 |\n\n**Verdict: OK.** No issues.\n\n---\n\n### 7. yang2024qwen2 — Qwen2 Technical Report\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Title match | YES | \"Qwen2 Technical Report\" — exact match |\n| Authors match | YES | Yang, An is first author — confirmed |\n| Year match | YES | 2024 (arXiv submission Jul 2024) — confirmed |\n| Venue match | N/A | arXiv preprint, no formal venue |\n| arXiv ID match | YES | 2407.10671 — confirmed |\n\n**Verdict: OK.** No issues.\n\n---\n\n### 8. lipman2023flow — Flow Matching\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | YES | |\n| Title match | YES | \"Flow Matching for Generative Modeling\" — exact match |\n| Authors match | YES | Lipman, Yaron is first author — confirmed |\n| Year match | YES | ICLR 2023 — confirmed |\n| Venue match | YES | ICLR 2023 — confirmed |\n| arXiv ID | Not given | arXiv: 2210.02747 |\n\n**Verdict: OK.** No issues.\n\n---\n\n## Summary\n\n| # | Bib Key | Status | Action Required |\n|---|---------|--------|-----------------|\n| 1 | liu2025vlapruner | OK | None |\n| 2 | shang2024prumerge | **FIX NEEDED** | Change year from 2024 to **2025** to match ICCV 2025 publication venue |\n| 3 | liu2023llava | OK | None |\n| 4 | shi2016subpixel | OK | None |\n| 5 | li2023blip2 | OK | None (minor capitalization variant is acceptable) |\n| 6 | zhai2023siglip | OK | None |\n| 7 | yang2024qwen2 | OK | None |\n| 8 | lipman2023flow | OK | None |\n\n**One actionable issue found:** Entry #2 (`shang2024prumerge`) has a year mismatch — the bib key and year field say 2024, but the paper was published at ICCV 2025. The year should be updated to 2025, and ideally the bib key renamed to `shang2025prumerge`.\n\nSources:\n- [VLA-Pruner on arXiv](https://arxiv.org/abs/2511.16449)\n- [LLaVA-PruMerge on arXiv](https://arxiv.org/abs/2403.15388)\n- [LLaVA-PruMerge at ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Shang_LLaVA-PruMerge_Adaptive_Token_Reduction_for_Efficient_Large_Multimodal_Models_ICCV_2025_paper.html)\n- [Visual Instruction Tuning at NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf)\n- [Sub-Pixel CNN at CVPR 2016](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Shi_Real-Time_Single_Image_CVPR_2016_paper.html)\n- [BLIP-2 at ICML 2023](https://proceedings.mlr.press/v202/li23q.html)\n- [SigLIP at ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/html/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.html)\n- [Qwen2 Technical Report on arXiv](https://arxiv.org/abs/2407.10671)\n- [Flow Matching at ICLR 2023](https://iclr.cc/virtual/2023/poster/11309)"
      }
    ],
    "totalDurationMs": 94816,
    "totalTokens": 28871,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 755,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 24856,
      "output_tokens": 2340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 920
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 755,
          "output_tokens": 2340,
          "cache_read_input_tokens": 24856,
          "cache_creation_input_tokens": 920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 920,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 13
    }
  }
}
```

</details>

---


### System

_source line 374_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for arXiv 2307.15818 RT-2 author list order Brohan fi…",
  "usage": {
    "total_tokens": 35052,
    "tool_uses": 22,
    "duration_ms": 72624
  },
  "last_tool_name": "WebSearch",
  "uuid": "1191b8de-4033-42b3-bdba-8f038be1ab43",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 375_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L4a2Q1agXFumGVj99vjdsi`</summary>

```json
{
  "query": "arXiv 2307.15818 RT-2 author list order Brohan first Zitkovich"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "fca280ce-47ce-4930-99d7-a18c1055bd66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZ764Q1mv9FW1idRKdPbBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 535,
      "cache_creation_input_tokens": 3176,
      "cache_read_input_tokens": 30562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3176,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 376_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for DINOv2 TMLR 2024 publication date month year open…",
  "usage": {
    "total_tokens": 35058,
    "tool_uses": 23,
    "duration_ms": 73597
  },
  "last_tool_name": "WebSearch",
  "uuid": "39f23fd7-34f1-4751-be22-40b266b98637",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 377_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eo47oENxDm9QhdPqpsCUuM`</summary>

```json
{
  "query": "DINOv2 TMLR 2024 publication date month year openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "9ab7098b-e685-4b32-8c5b-5f4440302778",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZ764Q1mv9FW1idRKdPbBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 535,
      "cache_creation_input_tokens": 3176,
      "cache_read_input_tokens": 30562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3176,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 378_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for Diffusion Policy Chi Cheng RSS 2023 or IJRR venue…",
  "usage": {
    "total_tokens": 35064,
    "tool_uses": 24,
    "duration_ms": 74104
  },
  "last_tool_name": "WebSearch",
  "uuid": "0708fa77-3a00-49f3-b52b-7cd6d7700939",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 379_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VCmRcQwgbopme5dfyS33Bb`</summary>

```json
{
  "query": "Diffusion Policy Chi Cheng RSS 2023 or IJRR venue proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "7704cb9f-bab5-40a5-931b-1d0d9065d13d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZ764Q1mv9FW1idRKdPbBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 535,
      "cache_creation_input_tokens": 3176,
      "cache_read_input_tokens": 30562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3176,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-29T06:33:26.700Z_

<details><summary>↩ Tool result · `toolu_01L4a2Q1agXFumGVj99vjdsi`</summary>

```text
Web search results for query: "arXiv 2307.15818 RT-2 author list order Brohan first Zitkovich"

Links: [{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"[2307.15818v1] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818v1"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"dblp: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.","url":"https://dblp.org/rec/journals/corr/abs-2307-15818.html"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://huggingface.co/papers/2307.15818"},{"title":"RT-2: Vision-Language-Action Models","url":"https://robotics-transformer2.github.io/"}]

Based on the search results, the author list for arXiv paper 2307.15818 (RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control) begins with Anthony Brohan as the first author and ends with Brianna Zitkovich as the last author.

Additionally, the authors are listed in alphabetical order, with a contribution statement in the paper appendix.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "c8304ac8-0583-484a-9a3b-a3020fe1a552"
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-29T06:33:27.954Z_

<details><summary>↩ Tool result · `toolu_01Eo47oENxDm9QhdPqpsCUuM`</summary>

```text
Web search results for query: "DINOv2 TMLR 2024 publication date month year openreview"

Links: [{"title":"DINOv2: Learning Robust Visual Features without Supervision | OpenReview","url":"https://openreview.net/forum?id=a68SUt6zFt"},{"title":"DINOv2: Learning Robust Visual Features Without Supervision | ML Anthology","url":"https://mlanthology.org/tmlr/2024/oquab2024tmlr-dinov2/"},{"title":"Published in Transactions on Machine Learning Research (01/2024)","url":"https://arxiv.org/pdf/2304.07193"},{"title":"HAL Id: hal-04376640 https://hal.science/hal-04376640v2 Submitted on 2 Feb 2024","url":"https://hal.science/hal-04376640v2/file/CVPR_2023_dinov2%20(4).pdf"},{"title":"Accepted papers at TMLR on X: \"DINOv2: Learning Robust Visual Features without Supervision Maxime Oquab, Timothée Darcet, Théo Moutakanni et al.. Action editor: Abhishek Kumar. https://t.co/M0YHJp3SuI #supervised #visual #features\" / X","url":"https://x.com/TmlrPub/status/1749446940125757691"},{"title":"A generalised vision transformer-based self-supervised model for diagnosing and grading prostate cancer using histological images | Prostate Cancer and Prostatic Diseases","url":"https://www.nature.com/articles/s41391-025-00957-w"},{"title":"[2304.07193] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193"},{"title":"DINOv2: Learning Robust Visual Features without Supervision | by Jim Canary | Medium","url":"https://medium.com/@jimcanary/dinov2-learning-robust-visual-features-without-supervision-bfd1cd94cbdd"},{"title":"Explainable self-supervised learning for medical image diagnosis based on DINO V2 model and semantic search","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12402508/"}]

The DINOv2 paper was published in TMLR on January 11, 2024. The OpenReview page is available at openreview.net/forum?id=a68SUt6zFt.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "a3480079-0caa-414f-8cf7-2bff8c16bf5a"
}
```

</details>

---


### System

_source line 382_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a5bfe667164930f6d",
  "tool_use_id": "toolu_016gyvTeHUBKP9YcsvMWBLj5",
  "status": "completed",
  "output_file": "",
  "summary": "Verify bib entries group 5",
  "usage": {
    "total_tokens": 29092,
    "tool_uses": 14,
    "duration_ms": 94214
  },
  "uuid": "a26d0260-023c-428a-8851-480dbb97cadb",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool result

_source line 383 · 2026-05-29T06:33:29.241Z_

<details><summary>↩ Tool result · `toolu_016gyvTeHUBKP9YcsvMWBLj5`</summary>

```text
Here is the structured verification checklist for all 8 entries:

---

## Reference Verification Checklist

### 1. li2024cogact — CogACT
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author is Qixiu Li (Li, Qixiu). Confirmed. |
| Title | MATCH | "CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation" |
| Year | MATCH | Submitted 2024-11-29 |
| Venue | N/A | No venue claimed in the bib entry (arXiv preprint) |
| arXiv ID | MATCH | 2411.19650 |
| Issues | None | |

### 2. zheng2025xvla — X-VLA
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author is Jinliang Zheng (Zheng, Jinliang). Confirmed. |
| Title | MATCH | "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model" |
| Year | **ISSUE** | arXiv submission date is **2025-10-11** (arXiv ID 2510.xxxxx = October 2025). The bib key says "2025" which is correct for the arXiv posting. However, ICLR 2026 proceedings would formally be year 2026. If the bib entry lists year=2025, it should be updated to **2026** to match the ICLR publication year. |
| Venue | MATCH | GitHub repo and metadata confirm "[ICLR 2026]" acceptance. |
| arXiv ID | MATCH | 2510.10274 |
| Issues | **Year ambiguity**: arXiv posted 2025, but venue is ICLR 2026. Bib entry should use year=2026 if citing the conference version, or year=2025 if citing the preprint. Verify which year is used in the bib. |

### 3. lewis2020bart — BART
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author Mike Lewis, with Yinhan Liu, Naman Goyal, et al. Confirmed. |
| Title | MATCH | "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension" |
| Year | MATCH | 2020 |
| Venue | MATCH | ACL 2020 (ACL Anthology: 2020.acl-main.703) |
| arXiv ID | N/A | No arXiv ID claimed |
| Issues | None | |

### 4. ryoo2021tokenlearner — TokenLearner
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author Michael S. Ryoo. Confirmed. |
| Title | **MISMATCH** | The bib entry uses "TokenLearner: Adaptive Space-Time Tokenization for Videos" — this is the **NeurIPS 2021 proceedings title**. The arXiv version (2106.11297) is titled **"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?"** (an extended version). Both titles are legitimate, but they refer to different versions. |
| Year | MATCH | NeurIPS 2021 |
| Venue | MATCH | NeurIPS 2021. Confirmed via proceedings.neurips.cc. |
| arXiv ID | **CAUTION** | 2106.11297 is the arXiv ID for the *extended* paper ("What Can 8 Learned Tokens Do..."). The NeurIPS proceedings title is "Adaptive Space-Time Tokenization for Videos." If citing the NeurIPS version with the NeurIPS title, the arXiv ID is slightly mismatched (arXiv has the extended title). This is acceptable practice but worth noting for consistency. |
| Issues | Title/arXiv mismatch: the NeurIPS proceedings title differs from the arXiv title at arXiv:2106.11297. Choose one consistently — either cite the NeurIPS proceedings (with proceedings title, no arXiv ID) or cite the arXiv version (with arXiv title). |

### 5. yin2022avit — A-ViT
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author Hongxu Yin. Confirmed. |
| Title | **MISMATCH** | The bib uses "A-ViT: Adaptive Tokens for Efficient Vision Transformer". On arXiv (2112.07658), the title is **"AdaViT: Adaptive Tokens for Efficient Vision Transformer"** (all versions v1-v3). The CVPR 2022 accepted version and official project page use "A-ViT". This is a known name change between arXiv and CVPR. |
| Year | MATCH | CVPR 2022 |
| Venue | MATCH | CVPR 2022 (Oral). Confirmed. |
| arXiv ID | MATCH | 2112.07658 |
| Issues | **Title discrepancy**: arXiv title is "AdaViT" but the CVPR published version is "A-ViT" (renamed to avoid confusion with entry #6, Meng et al.'s "AdaViT"). If the bib cites the CVPR version, "A-ViT" is correct. If citing arXiv, "AdaViT" is the title there. Recommend using "A-ViT" (the CVPR title) and noting the arXiv lists it as "AdaViT". |

### 6. meng2022adavit — AdaViT (Meng et al.)
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author Lingchen Meng. Confirmed. |
| Title | MATCH | "AdaViT: Adaptive Vision Transformers for Efficient Image Recognition" |
| Year | MATCH | 2022 |
| Venue | MATCH | CVPR 2022. Confirmed via openaccess.thecvf.com. |
| arXiv ID | MATCH | 2111.15668 |
| Issues | None. Note this is a different paper from entry #5 (Yin et al.), despite both originally using "AdaViT" on arXiv. |

### 7. chen2023sparsevit — SparseViT
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author Xuanyao Chen. Full list: Xuanyao Chen, Zhijian Liu, Haotian Tang, Li Yi, Hang Zhao, Song Han. Confirmed. |
| Title | MATCH | "SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer" |
| Year | MATCH | 2023 |
| Venue | MATCH | CVPR 2023. Confirmed via CVPR Open Access and IEEE Xplore. |
| arXiv ID | MATCH | 2303.17605 |
| Issues | None | |

### 8. ye2025fitprune — Fit and Prune
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author Weihao Ye. Full list: Weihao Ye, Qiangqiang Wu, Wentao Lin, Yijiang Zhou. Confirmed. |
| Title | MATCH | "Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models" |
| Year | MATCH | AAAI 2025 (Proceedings of the AAAI Conference on Artificial Intelligence, 39(21), 22128-22136) |
| Venue | MATCH | AAAI 2025. Confirmed via ojs.aaai.org. |
| arXiv ID | MATCH | 2409.10197 |
| Issues | None | |

---

## Summary of Issues Found

| Entry | Severity | Issue |
|-------|----------|-------|
| #2 zheng2025xvla | Minor | Year should be **2026** if citing ICLR proceedings (not 2025). |
| #4 ryoo2021tokenlearner | Minor | arXiv title ("What Can 8 Learned Tokens Do for Images and Videos?") differs from NeurIPS title ("Adaptive Space-Time Tokenization for Videos"). Pick one consistently. |
| #5 yin2022avit | Minor | arXiv title is "AdaViT" but CVPR version is "A-ViT". Current bib uses "A-ViT" which matches CVPR — acceptable, but note the arXiv discrepancy. |

All 8 papers exist and are real. No fabricated references detected. 6 of 8 entries are fully clean; 2 have minor title/ID consistency issues and 1 has a year ambiguity.

Sources:
- [CogACT on arXiv](https://arxiv.org/abs/2411.19650)
- [X-VLA on arXiv](https://arxiv.org/abs/2510.10274)
- [X-VLA GitHub (ICLR 2026)](https://github.com/2toinf/X-VLA)
- [BART on ACL Anthology](https://aclanthology.org/2020.acl-main.703/)
- [TokenLearner on arXiv](https://arxiv.org/abs/2106.11297)
- [TokenLearner NeurIPS proceedings](https://proceedings.neurips.cc/paper/2021/hash/6a30e32e56fce5cf381895dfe6ca7b6f-Abstract.html)
- [A-ViT on arXiv](https://arxiv.org/abs/2112.07658)
- [A-ViT project page](https://a-vit.github.io/)
- [AdaViT (Meng) CVPR Open Access](https://openaccess.thecvf.com/content/CVPR2022/html/Meng_AdaViT_Adaptive_Vision_Transformers_for_Efficient_Image_Recognition_CVPR_2022_paper.html)
- [SparseViT CVPR Open Access](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_SparseViT_Revisiting_Activation_Sparsity_for_Efficient_High-Resolution_Vision_Transformer_CVPR_2023_paper.html)
- [Fit and Prune AAAI proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/34366)
- [Fit and Prune on arXiv](https://arxiv.org/abs/2409.10197)

agentId: a5bfe667164930f6d (use SendMessage with to: 'a5bfe667164930f6d' to continue this agent)
&lt;usage>total_tokens: 31355
tool_uses: 14
duration_ms: 94216&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "cf433f55-9051-4cba-9ec8-61b029e316e6",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. li2024cogact: \"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation\" by Li, Qixiu and others. arXiv 2411.19650, year 2024.\n\n2. zheng2025xvla: \"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" by Zheng, Jinliang and others. ICLR 2026, arXiv 2510.10274.\n\n3. lewis2020bart: \"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension\" by Lewis, Mike and others. ACL 2020.\n\n4. ryoo2021tokenlearner: \"TokenLearner: Adaptive Space-Time Tokenization for Videos\" by Ryoo, Michael S. and others. NeurIPS 2021, arXiv 2106.11297.\n\n5. yin2022avit: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\" by Yin, Hongxu and others. CVPR 2022, arXiv 2112.07658.\n\n6. meng2022adavit: \"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition\" by Meng, Lingchen and others. CVPR 2022, arXiv 2111.15668.\n\n7. chen2023sparsevit: \"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer\" by Chen, Xuanyao and others. CVPR 2023, arXiv 2303.17605.\n\n8. ye2025fitprune: \"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models\" by Ye, Weihao and others. AAAI 2025, arXiv 2409.10197.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found.",
    "agentId": "a5bfe667164930f6d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the structured verification checklist for all 8 entries:\n\n---\n\n## Reference Verification Checklist\n\n### 1. li2024cogact — CogACT\n| Check | Status | Detail |\n|-------|--------|--------|\n| Exists | YES | |\n| Authors | MATCH | First author is Qixiu Li (Li, Qixiu). Confirmed. |\n| Title | MATCH | \"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation\" |\n| Year | MATCH | Submitted 2024-11-29 |\n| Venue | N/A | No venue claimed in the bib entry (arXiv preprint) |\n| arXiv ID | MATCH | 2411.19650 |\n| Issues | None | |\n\n### 2. zheng2025xvla — X-VLA\n| Check | Status | Detail |\n|-------|--------|--------|\n| Exists | YES | |\n| Authors | MATCH | First author is Jinliang Zheng (Zheng, Jinliang). Confirmed. |\n| Title | MATCH | \"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" |\n| Year | **ISSUE** | arXiv submission date is **2025-10-11** (arXiv ID 2510.xxxxx = October 2025). The bib key says \"2025\" which is correct for the arXiv posting. However, ICLR 2026 proceedings would formally be year 2026. If the bib entry lists year=2025, it should be updated to **2026** to match the ICLR publication year. |\n| Venue | MATCH | GitHub repo and metadata confirm \"[ICLR 2026]\" acceptance. |\n| arXiv ID | MATCH | 2510.10274 |\n| Issues | **Year ambiguity**: arXiv posted 2025, but venue is ICLR 2026. Bib entry should use year=2026 if citing the conference version, or year=2025 if citing the preprint. Verify which year is used in the bib. |\n\n### 3. lewis2020bart — BART\n| Check | Status | Detail |\n|-------|--------|--------|\n| Exists | YES | |\n| Authors | MATCH | First author Mike Lewis, with Yinhan Liu, Naman Goyal, et al. Confirmed. |\n| Title | MATCH | \"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension\" |\n| Year | MATCH | 2020 |\n| Venue | MATCH | ACL 2020 (ACL Anthology: 2020.acl-main.703) |\n| arXiv ID | N/A | No arXiv ID claimed |\n| Issues | None | |\n\n### 4. ryoo2021tokenlearner — TokenLearner\n| Check | Status | Detail |\n|-------|--------|--------|\n| Exists | YES | |\n| Authors | MATCH | First author Michael S. Ryoo. Confirmed. |\n| Title | **MISMATCH** | The bib entry uses \"TokenLearner: Adaptive Space-Time Tokenization for Videos\" — this is the **NeurIPS 2021 proceedings title**. The arXiv version (2106.11297) is titled **\"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?\"** (an extended version). Both titles are legitimate, but they refer to different versions. |\n| Year | MATCH | NeurIPS 2021 |\n| Venue | MATCH | NeurIPS 2021. Confirmed via proceedings.neurips.cc. |\n| arXiv ID | **CAUTION** | 2106.11297 is the arXiv ID for the *extended* paper (\"What Can 8 Learned Tokens Do...\"). The NeurIPS proceedings title is \"Adaptive Space-Time Tokenization for Videos.\" If citing the NeurIPS version with the NeurIPS title, the arXiv ID is slightly mismatched (arXiv has the extended title). This is acceptable practice but worth noting for consistency. |\n| Issues | Title/arXiv mismatch: the NeurIPS proceedings title differs from the arXiv title at arXiv:2106.11297. Choose one consistently — either cite the NeurIPS proceedings (with proceedings title, no arXiv ID) or cite the arXiv version (with arXiv title). |\n\n### 5. yin2022avit — A-ViT\n| Check | Status | Detail |\n|-------|--------|--------|\n| Exists | YES | |\n| Authors | MATCH | First author Hongxu Yin. Confirmed. |\n| Title | **MISMATCH** | The bib uses \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\". On arXiv (2112.07658), the title is **\"AdaViT: Adaptive Tokens for Efficient Vision Transformer\"** (all versions v1-v3). The CVPR 2022 accepted version and official project page use \"A-ViT\". This is a known name change between arXiv and CVPR. |\n| Year | MATCH | CVPR 2022 |\n| Venue | MATCH | CVPR 2022 (Oral). Confirmed. |\n| arXiv ID | MATCH | 2112.07658 |\n| Issues | **Title discrepancy**: arXiv title is \"AdaViT\" but the CVPR published version is \"A-ViT\" (renamed to avoid confusion with entry #6, Meng et al.'s \"AdaViT\"). If the bib cites the CVPR version, \"A-ViT\" is correct. If citing arXiv, \"AdaViT\" is the title there. Recommend using \"A-ViT\" (the CVPR title) and noting the arXiv lists it as \"AdaViT\". |\n\n### 6. meng2022adavit — AdaViT (Meng et al.)\n| Check | Status | Detail |\n|-------|--------|--------|\n| Exists | YES | |\n| Authors | MATCH | First author Lingchen Meng. Confirmed. |\n| Title | MATCH | \"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition\" |\n| Year | MATCH | 2022 |\n| Venue | MATCH | CVPR 2022. Confirmed via openaccess.thecvf.com. |\n| arXiv ID | MATCH | 2111.15668 |\n| Issues | None. Note this is a different paper from entry #5 (Yin et al.), despite both originally using \"AdaViT\" on arXiv. |\n\n### 7. chen2023sparsevit — SparseViT\n| Check | Status | Detail |\n|-------|--------|--------|\n| Exists | YES | |\n| Authors | MATCH | First author Xuanyao Chen. Full list: Xuanyao Chen, Zhijian Liu, Haotian Tang, Li Yi, Hang Zhao, Song Han. Confirmed. |\n| Title | MATCH | \"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer\" |\n| Year | MATCH | 2023 |\n| Venue | MATCH | CVPR 2023. Confirmed via CVPR Open Access and IEEE Xplore. |\n| arXiv ID | MATCH | 2303.17605 |\n| Issues | None | |\n\n### 8. ye2025fitprune — Fit and Prune\n| Check | Status | Detail |\n|-------|--------|--------|\n| Exists | YES | |\n| Authors | MATCH | First author Weihao Ye. Full list: Weihao Ye, Qiangqiang Wu, Wentao Lin, Yijiang Zhou. Confirmed. |\n| Title | MATCH | \"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models\" |\n| Year | MATCH | AAAI 2025 (Proceedings of the AAAI Conference on Artificial Intelligence, 39(21), 22128-22136) |\n| Venue | MATCH | AAAI 2025. Confirmed via ojs.aaai.org. |\n| arXiv ID | MATCH | 2409.10197 |\n| Issues | None | |\n\n---\n\n## Summary of Issues Found\n\n| Entry | Severity | Issue |\n|-------|----------|-------|\n| #2 zheng2025xvla | Minor | Year should be **2026** if citing ICLR proceedings (not 2025). |\n| #4 ryoo2021tokenlearner | Minor | arXiv title (\"What Can 8 Learned Tokens Do for Images and Videos?\") differs from NeurIPS title (\"Adaptive Space-Time Tokenization for Videos\"). Pick one consistently. |\n| #5 yin2022avit | Minor | arXiv title is \"AdaViT\" but CVPR version is \"A-ViT\". Current bib uses \"A-ViT\" which matches CVPR — acceptable, but note the arXiv discrepancy. |\n\nAll 8 papers exist and are real. No fabricated references detected. 6 of 8 entries are fully clean; 2 have minor title/ID consistency issues and 1 has a year ambiguity.\n\nSources:\n- [CogACT on arXiv](https://arxiv.org/abs/2411.19650)\n- [X-VLA on arXiv](https://arxiv.org/abs/2510.10274)\n- [X-VLA GitHub (ICLR 2026)](https://github.com/2toinf/X-VLA)\n- [BART on ACL Anthology](https://aclanthology.org/2020.acl-main.703/)\n- [TokenLearner on arXiv](https://arxiv.org/abs/2106.11297)\n- [TokenLearner NeurIPS proceedings](https://proceedings.neurips.cc/paper/2021/hash/6a30e32e56fce5cf381895dfe6ca7b6f-Abstract.html)\n- [A-ViT on arXiv](https://arxiv.org/abs/2112.07658)\n- [A-ViT project page](https://a-vit.github.io/)\n- [AdaViT (Meng) CVPR Open Access](https://openaccess.thecvf.com/content/CVPR2022/html/Meng_AdaViT_Adaptive_Vision_Transformers_for_Efficient_Image_Recognition_CVPR_2022_paper.html)\n- [SparseViT CVPR Open Access](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_SparseViT_Revisiting_Activation_Sparsity_for_Efficient_High-Resolution_Vision_Transformer_CVPR_2023_paper.html)\n- [Fit and Prune AAAI proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/34366)\n- [Fit and Prune on arXiv](https://arxiv.org/abs/2409.10197)"
      }
    ],
    "totalDurationMs": 94216,
    "totalTokens": 31355,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2785,
      "cache_read_input_tokens": 25766,
      "output_tokens": 2803,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2803,
          "cache_read_input_tokens": 25766,
          "cache_creation_input_tokens": 2785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2785,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 14
    }
  }
}
```

</details>

---


### System

_source line 384_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a09124f3977418cbc",
  "tool_use_id": "toolu_018c5zBnBeNaQok2WqUVgLj2",
  "status": "completed",
  "output_file": "",
  "summary": "Verify bib entries group 2",
  "usage": {
    "total_tokens": 31028,
    "tool_uses": 18,
    "duration_ms": 120094
  },
  "uuid": "46cbcbd6-f7e0-4692-be4b-28b016104f84",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool result

_source line 385 · 2026-05-29T06:33:31.018Z_

<details><summary>↩ Tool result · `toolu_018c5zBnBeNaQok2WqUVgLj2`</summary>

```text
Now I have enough information to compile the full structured checklist. Here is the verification report:

---

## Reference Verification Checklist

### 1. shukor2025smolvla

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv, Semantic Scholar, HuggingFace |
| Authors | **MATCH** | First author is Mustafa Shukor; confirmed |
| Title | **MATCH** | "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics" -- exact |
| Year | **ISSUE** | The arXiv submission date is **June 2, 2025**. The arXiv ID prefix `2506` confirms June 2025. Listing year as 2025 is correct, but note the paper appeared mid-2025, not earlier |
| Venue | **N/A** | Listed as arXiv preprint only; no formal venue claimed. OK |
| arXiv ID | **MATCH** | 2506.01844 confirmed |

**Verdict: PASS**

---

### 2. kim2024openvla

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv (2406.09246), PMLR, OpenReview |
| Authors | **MATCH** | First author Moo Jin Kim; confirmed |
| Title | **MATCH** | "OpenVLA: An Open-Source Vision-Language-Action Model" -- exact |
| Year | **ISSUE** | The conference was CoRL 2024 (held Nov 2024), but the PMLR proceedings (volume 270) were published **January 12, 2025**. The bib key `kim2024` is acceptable if citing the conference year. However, the PMLR entry uses `kim25c`. Either 2024 or 2025 is defensible; using 2024 (conference year) is the common convention |
| Venue | **MATCH** | CoRL 2024, 8th Conference on Robot Learning -- confirmed |
| arXiv ID | **Not provided in entry** | arXiv:2406.09246 exists if needed |

**Verdict: PASS (minor: year ambiguity 2024 vs 2025 for PMLR publication date)**

---

### 3. brohan2023rt2

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv (2307.15818), PMLR, Semantic Scholar |
| Authors | **ISSUE** | On arXiv, Anthony Brohan is listed first. In the official CoRL 2023 PMLR proceedings (v229), the paper is listed as `zitkovich23a` with **Brianna Zitkovich** as first author. This is a large multi-author Google DeepMind paper; the author ordering differs between arXiv and proceedings. Citing "Brohan, Anthony and others" matches the arXiv version but **not** the official proceedings version |
| Title | **MATCH** | "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" -- exact |
| Year | **MATCH** | CoRL 2023, PMLR v229 -- confirmed |
| Venue | **MATCH** | CoRL 2023 (7th Conference on Robot Learning) -- confirmed |
| arXiv ID | **Not provided in entry** | arXiv:2307.15818 exists if needed |

**Verdict: PASS with caveat -- the official proceedings list Zitkovich as first author, not Brohan. If citing the proceedings, first author should be Zitkovich. If citing the arXiv preprint, Brohan is first. Recommend aligning the bib entry with whichever source is being cited.**

---

### 4. black2024pi0

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv (2410.24164), Semantic Scholar |
| Authors | **MATCH** | First author Kevin Black; confirmed (Physical Intelligence team) |
| Title | **MATCH** | "pi0: A Vision-Language-Action Flow Model for General Robot Control" -- exact (rendered as pi_0 in LaTeX) |
| Year | **MATCH** | Submitted October 31, 2024 |
| Venue | **N/A** | Listed as arXiv preprint; no formal venue claimed. OK |
| arXiv ID | **MATCH** | 2410.24164 confirmed |

**Verdict: PASS**

---

### 5. black2025pi05

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv (2504.16054) and PMLR v305 |
| Authors | **MATCH** | Kevin Black is listed as first author; confirmed |
| Title | **MATCH** | "pi0.5: a Vision-Language-Action Model with Open-World Generalization" -- exact (lowercase "a") |
| Year | **MATCH** | CoRL 2025 proceedings published 2025 |
| Venue | **MATCH** | CoRL 2025, PMLR volume 305 -- confirmed |
| Pages | **MATCH** | Pages 17-40 confirmed at `proceedings.mlr.press/v305/black25a.html` |
| arXiv ID | **MATCH** | 2504.16054 confirmed |

**Verdict: PASS**

---

### 6. ghosh2024octo

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv (2405.12213), Semantic Scholar, project website |
| Authors | **MATCH** | "Octo Model Team" with Dibya Ghosh as lead; confirmed |
| Title | **MATCH** | "Octo: An Open-Source Generalist Robot Policy" -- exact |
| Year | **MATCH** | RSS 2024 (held May 2024); arXiv May 2024 |
| Venue | **MATCH** | Robotics: Science and Systems (RSS) 2024 -- confirmed |
| arXiv ID | **Not provided in entry** | arXiv:2405.12213 exists if needed |

**Verdict: PASS**

---

### 7. brohan2023rt1

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv (2212.06817), RSS proceedings, DBLP |
| Authors | **MATCH** | Anthony Brohan is first author; confirmed via DBLP entry `BrohanBCCDFGHHH23` |
| Title | **MATCH** | "RT-1: Robotics Transformer for Real-World Control at Scale" -- exact |
| Year | **MATCH** | RSS 2023 -- confirmed |
| Venue | **MATCH** | Robotics: Science and Systems (RSS) 2023 -- confirmed |
| arXiv ID | **Not provided in entry** | arXiv:2212.06817 exists if needed |

**Verdict: PASS**

---

### 8. kim2025openoft

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv (2502.19645), project website, GitHub |
| Authors | **MATCH** | Moo Jin Kim, Chelsea Finn, Percy Liang -- confirmed (3 authors total) |
| Title | **MATCH** | "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" -- exact |
| Year | **MATCH** | Submitted February 27, 2025 |
| Venue | **N/A** | Listed as arXiv preprint; no formal venue claimed. OK |
| arXiv ID | **MATCH** | 2502.19645 confirmed |

**Verdict: PASS -- but note the bib key uses "openoft" which isn't in the title. The method name is OpenVLA-OFT. This is a naming convention choice, not an error.**

---

## Summary

| # | Key | Verdict | Issues |
|---|-----|---------|--------|
| 1 | shukor2025smolvla | PASS | None |
| 2 | kim2024openvla | PASS | PMLR publication date is 2025; conference year 2024 is the common citation convention, acceptable |
| 3 | brohan2023rt2 | **CAUTION** | Official PMLR proceedings list Zitkovich as first author, not Brohan. If citing the proceedings, this should be corrected |
| 4 | black2024pi0 | PASS | None |
| 5 | black2025pi05 | PASS | All details (volume, pages, arXiv ID) confirmed |
| 6 | ghosh2024octo | PASS | None |
| 7 | brohan2023rt1 | PASS | None |
| 8 | kim2025openoft | PASS | None |

**One actionable issue found:** Entry #3 (`brohan2023rt2`) -- if citing the official CoRL 2023 proceedings, the first author should be Zitkovich, not Brohan (the proceedings entry is `zitkovich23a`). If citing the arXiv preprint, Brohan as first author is correct. Recommend deciding which source to cite and aligning accordingly.

Sources:
- [SmolVLA arXiv](https://arxiv.org/abs/2506.01844)
- [OpenVLA PMLR](https://proceedings.mlr.press/v270/kim25c.html)
- [OpenVLA arXiv](https://arxiv.org/abs/2406.09246)
- [RT-2 PMLR (Zitkovich)](https://proceedings.mlr.press/v229/zitkovich23a.html)
- [RT-2 arXiv (Brohan)](https://arxiv.org/abs/2307.15818)
- [pi0 arXiv](https://arxiv.org/abs/2410.24164)
- [pi0.5 PMLR](https://proceedings.mlr.press/v305/black25a.html)
- [pi0.5 arXiv](https://arxiv.org/abs/2504.16054)
- [Octo arXiv](https://arxiv.org/abs/2405.12213)
- [RT-1 arXiv](https://arxiv.org/abs/2212.06817)
- [RT-1 RSS proceedings](https://www.roboticsproceedings.org/rss19/p025.pdf)
- [OpenVLA-OFT arXiv](https://arxiv.org/abs/2502.19645)
- [OpenVLA-OFT project page](https://openvla-oft.github.io/)

agentId: a09124f3977418cbc (use SendMessage with to: 'a09124f3977418cbc' to continue this agent)
&lt;usage>total_tokens: 33142
tool_uses: 18
duration_ms: 120095&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "baf58fff-59a5-423c-a7d8-c5cf3e4cb053",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. shukor2025smolvla: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\" by Shukor, Mustafa and others. arXiv 2506.01844, year 2025.\n\n2. kim2024openvla: \"OpenVLA: An Open-Source Vision-Language-Action Model\" by Kim, Moo Jin and others. CoRL 2024 (8th Conference on Robot Learning).\n\n3. brohan2023rt2: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Brohan, Anthony and others. CoRL 2023.\n\n4. black2024pi0: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" by Black, Kevin and others. arXiv 2410.24164, year 2024.\n\n5. black2025pi05: \"π0.5: a Vision-Language-Action Model with Open-World Generalization\" by Black, Kevin and others. CoRL 2025, PMLR volume 305, pages 17-40, arXiv 2504.16054.\n\n6. ghosh2024octo: \"Octo: An Open-Source Generalist Robot Policy\" by Octo Model Team, Ghosh, Dibya and others. RSS 2024.\n\n7. brohan2023rt1: \"RT-1: Robotics Transformer for Real-World Control at Scale\" by Brohan, Anthony and others. RSS 2023.\n\n8. kim2025openoft: \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" by Kim, Moo Jin and Finn, Chelsea and Liang, Percy. arXiv 2502.19645, year 2025.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found.",
    "agentId": "a09124f3977418cbc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to compile the full structured checklist. Here is the verification report:\n\n---\n\n## Reference Verification Checklist\n\n### 1. shukor2025smolvla\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | **YES** | Found on arXiv, Semantic Scholar, HuggingFace |\n| Authors | **MATCH** | First author is Mustafa Shukor; confirmed |\n| Title | **MATCH** | \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\" -- exact |\n| Year | **ISSUE** | The arXiv submission date is **June 2, 2025**. The arXiv ID prefix `2506` confirms June 2025. Listing year as 2025 is correct, but note the paper appeared mid-2025, not earlier |\n| Venue | **N/A** | Listed as arXiv preprint only; no formal venue claimed. OK |\n| arXiv ID | **MATCH** | 2506.01844 confirmed |\n\n**Verdict: PASS**\n\n---\n\n### 2. kim2024openvla\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | **YES** | Found on arXiv (2406.09246), PMLR, OpenReview |\n| Authors | **MATCH** | First author Moo Jin Kim; confirmed |\n| Title | **MATCH** | \"OpenVLA: An Open-Source Vision-Language-Action Model\" -- exact |\n| Year | **ISSUE** | The conference was CoRL 2024 (held Nov 2024), but the PMLR proceedings (volume 270) were published **January 12, 2025**. The bib key `kim2024` is acceptable if citing the conference year. However, the PMLR entry uses `kim25c`. Either 2024 or 2025 is defensible; using 2024 (conference year) is the common convention |\n| Venue | **MATCH** | CoRL 2024, 8th Conference on Robot Learning -- confirmed |\n| arXiv ID | **Not provided in entry** | arXiv:2406.09246 exists if needed |\n\n**Verdict: PASS (minor: year ambiguity 2024 vs 2025 for PMLR publication date)**\n\n---\n\n### 3. brohan2023rt2\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | **YES** | Found on arXiv (2307.15818), PMLR, Semantic Scholar |\n| Authors | **ISSUE** | On arXiv, Anthony Brohan is listed first. In the official CoRL 2023 PMLR proceedings (v229), the paper is listed as `zitkovich23a` with **Brianna Zitkovich** as first author. This is a large multi-author Google DeepMind paper; the author ordering differs between arXiv and proceedings. Citing \"Brohan, Anthony and others\" matches the arXiv version but **not** the official proceedings version |\n| Title | **MATCH** | \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" -- exact |\n| Year | **MATCH** | CoRL 2023, PMLR v229 -- confirmed |\n| Venue | **MATCH** | CoRL 2023 (7th Conference on Robot Learning) -- confirmed |\n| arXiv ID | **Not provided in entry** | arXiv:2307.15818 exists if needed |\n\n**Verdict: PASS with caveat -- the official proceedings list Zitkovich as first author, not Brohan. If citing the proceedings, first author should be Zitkovich. If citing the arXiv preprint, Brohan is first. Recommend aligning the bib entry with whichever source is being cited.**\n\n---\n\n### 4. black2024pi0\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | **YES** | Found on arXiv (2410.24164), Semantic Scholar |\n| Authors | **MATCH** | First author Kevin Black; confirmed (Physical Intelligence team) |\n| Title | **MATCH** | \"pi0: A Vision-Language-Action Flow Model for General Robot Control\" -- exact (rendered as pi_0 in LaTeX) |\n| Year | **MATCH** | Submitted October 31, 2024 |\n| Venue | **N/A** | Listed as arXiv preprint; no formal venue claimed. OK |\n| arXiv ID | **MATCH** | 2410.24164 confirmed |\n\n**Verdict: PASS**\n\n---\n\n### 5. black2025pi05\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | **YES** | Found on arXiv (2504.16054) and PMLR v305 |\n| Authors | **MATCH** | Kevin Black is listed as first author; confirmed |\n| Title | **MATCH** | \"pi0.5: a Vision-Language-Action Model with Open-World Generalization\" -- exact (lowercase \"a\") |\n| Year | **MATCH** | CoRL 2025 proceedings published 2025 |\n| Venue | **MATCH** | CoRL 2025, PMLR volume 305 -- confirmed |\n| Pages | **MATCH** | Pages 17-40 confirmed at `proceedings.mlr.press/v305/black25a.html` |\n| arXiv ID | **MATCH** | 2504.16054 confirmed |\n\n**Verdict: PASS**\n\n---\n\n### 6. ghosh2024octo\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | **YES** | Found on arXiv (2405.12213), Semantic Scholar, project website |\n| Authors | **MATCH** | \"Octo Model Team\" with Dibya Ghosh as lead; confirmed |\n| Title | **MATCH** | \"Octo: An Open-Source Generalist Robot Policy\" -- exact |\n| Year | **MATCH** | RSS 2024 (held May 2024); arXiv May 2024 |\n| Venue | **MATCH** | Robotics: Science and Systems (RSS) 2024 -- confirmed |\n| arXiv ID | **Not provided in entry** | arXiv:2405.12213 exists if needed |\n\n**Verdict: PASS**\n\n---\n\n### 7. brohan2023rt1\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | **YES** | Found on arXiv (2212.06817), RSS proceedings, DBLP |\n| Authors | **MATCH** | Anthony Brohan is first author; confirmed via DBLP entry `BrohanBCCDFGHHH23` |\n| Title | **MATCH** | \"RT-1: Robotics Transformer for Real-World Control at Scale\" -- exact |\n| Year | **MATCH** | RSS 2023 -- confirmed |\n| Venue | **MATCH** | Robotics: Science and Systems (RSS) 2023 -- confirmed |\n| arXiv ID | **Not provided in entry** | arXiv:2212.06817 exists if needed |\n\n**Verdict: PASS**\n\n---\n\n### 8. kim2025openoft\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Exists | **YES** | Found on arXiv (2502.19645), project website, GitHub |\n| Authors | **MATCH** | Moo Jin Kim, Chelsea Finn, Percy Liang -- confirmed (3 authors total) |\n| Title | **MATCH** | \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" -- exact |\n| Year | **MATCH** | Submitted February 27, 2025 |\n| Venue | **N/A** | Listed as arXiv preprint; no formal venue claimed. OK |\n| arXiv ID | **MATCH** | 2502.19645 confirmed |\n\n**Verdict: PASS -- but note the bib key uses \"openoft\" which isn't in the title. The method name is OpenVLA-OFT. This is a naming convention choice, not an error.**\n\n---\n\n## Summary\n\n| # | Key | Verdict | Issues |\n|---|-----|---------|--------|\n| 1 | shukor2025smolvla | PASS | None |\n| 2 | kim2024openvla | PASS | PMLR publication date is 2025; conference year 2024 is the common citation convention, acceptable |\n| 3 | brohan2023rt2 | **CAUTION** | Official PMLR proceedings list Zitkovich as first author, not Brohan. If citing the proceedings, this should be corrected |\n| 4 | black2024pi0 | PASS | None |\n| 5 | black2025pi05 | PASS | All details (volume, pages, arXiv ID) confirmed |\n| 6 | ghosh2024octo | PASS | None |\n| 7 | brohan2023rt1 | PASS | None |\n| 8 | kim2025openoft | PASS | None |\n\n**One actionable issue found:** Entry #3 (`brohan2023rt2`) -- if citing the official CoRL 2023 proceedings, the first author should be Zitkovich, not Brohan (the proceedings entry is `zitkovich23a`). If citing the arXiv preprint, Brohan as first author is correct. Recommend deciding which source to cite and aligning accordingly.\n\nSources:\n- [SmolVLA arXiv](https://arxiv.org/abs/2506.01844)\n- [OpenVLA PMLR](https://proceedings.mlr.press/v270/kim25c.html)\n- [OpenVLA arXiv](https://arxiv.org/abs/2406.09246)\n- [RT-2 PMLR (Zitkovich)](https://proceedings.mlr.press/v229/zitkovich23a.html)\n- [RT-2 arXiv (Brohan)](https://arxiv.org/abs/2307.15818)\n- [pi0 arXiv](https://arxiv.org/abs/2410.24164)\n- [pi0.5 PMLR](https://proceedings.mlr.press/v305/black25a.html)\n- [pi0.5 arXiv](https://arxiv.org/abs/2504.16054)\n- [Octo arXiv](https://arxiv.org/abs/2405.12213)\n- [RT-1 arXiv](https://arxiv.org/abs/2212.06817)\n- [RT-1 RSS proceedings](https://www.roboticsproceedings.org/rss19/p025.pdf)\n- [OpenVLA-OFT arXiv](https://arxiv.org/abs/2502.19645)\n- [OpenVLA-OFT project page](https://openvla-oft.github.io/)"
      }
    ],
    "totalDurationMs": 120095,
    "totalTokens": 33142,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 668,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 28430,
      "output_tokens": 2689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1355
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 668,
          "output_tokens": 2689,
          "cache_read_input_tokens": 28430,
          "cache_creation_input_tokens": 1355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1355,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 18
    }
  }
}
```

</details>

---


### Tool result

_source line 386 · 2026-05-29T06:33:31.212Z_

<details><summary>↩ Tool result · `toolu_01VCmRcQwgbopme5dfyS33Bb`</summary>

```text
Web search results for query: "Diffusion Policy Chi Cheng RSS 2023 or IJRR venue proceedings"

Links: [{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion Policy","url":"https://arxiv.org/html/2502.12371v2"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub","url":"https://github.com/real-stanford/diffusion_policy"},{"title":"Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11","url":"https://dl.acm.org/doi/10.1177/02783649241273668"},{"title":"[PDF] Diffusion policy: Visuomotor policy learning via action diffusion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diffusion-policy:-Visuomotor-policy-learning-via-Chi-Feng/bdba3bd30a49ea4c5b20b43dbd8f0eb59e9d80e2"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion","url":"https://www.researchgate.net/publication/384857010_Diffusion_policy_Visuomotor_policy_learning_via_action_diffusion"},{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion · Robotics: Science and Systems","url":"https://roboticsconference.org/2023/program/papers/026/"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/pdf/2303.04137"}]

Based on the search results, here's what I found about Diffusion Policy by Chi Cheng:

The paper "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion" by Cheng Chi and colleagues was published at Robotics: Science and Systems (RSS) 2023, and later appeared in The International Journal of Robotics Research (IJRR) 2024.

The RSS 2023 proceedings were held in Daegu, Republic of Korea, from July 10-14, 2023.

The paper's key contribution is that it introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process.

The authors include Cheng Chi from Columbia University, Siyuan Feng and Eric Cousineau and Benjamin Burchfiel from Toyota Research Institute, and Yilun Du from MIT, along with Shuran Song.

You can find the paper at the official project website (https://diffusion-policy.cs.columbia.edu/), on arXiv (arXiv:2303.04137), and in the IJRR journal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "00407d2e-2bda-4b54-9265-667a78354faf"
}
```

</details>

---


### System

_source line 387_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for arxiv.org abs 2307.15818 RT-2 \"Anthony Brohan\" fi…",
  "usage": {
    "total_tokens": 37492,
    "tool_uses": 25,
    "duration_ms": 84375
  },
  "last_tool_name": "WebSearch",
  "uuid": "123e589c-157c-442f-a075-8235fe27531d",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 388_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015NumkhjMv6gUjya9bnm86Y`</summary>

```json
{
  "query": "arxiv.org abs 2307.15818 RT-2 \"Anthony Brohan\" first author alphabetical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "f40fbe7b-9421-4096-b540-77d343ca4a0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GaEMFFfF5n7tRefD2SStR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2960,
      "cache_read_input_tokens": 33738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2960,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 389_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for RoboFlamingo ICLR 2024 accepted Li Xinghang title…",
  "usage": {
    "total_tokens": 37493,
    "tool_uses": 26,
    "duration_ms": 84843
  },
  "last_tool_name": "WebSearch",
  "uuid": "c1d1401e-aca6-4696-a315-818edd080412",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 390_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TTyMxE8JpCLWjjsnnA5ux3`</summary>

```json
{
  "query": "RoboFlamingo ICLR 2024 accepted Li Xinghang title exact"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "2715325f-6480-4476-9876-14dbe90c6d79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GaEMFFfF5n7tRefD2SStR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2960,
      "cache_read_input_tokens": 33738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2960,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-29T06:33:40.800Z_

<details><summary>↩ Tool result · `toolu_015NumkhjMv6gUjya9bnm86Y`</summary>

```text
Web search results for query: "arxiv.org abs 2307.15818 RT-2 "Anthony Brohan" first author alphabetical"

Links: [{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://huggingface.co/papers/2307.15818"},{"title":"RT-2: Vision-Language-Action Models Transfer Web ...","url":"https://arxiv.org/pdf/2307.15818"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"dblp: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.","url":"https://dblp.org/rec/journals/corr/abs-2307-15818.html"},{"title":"RT-2: Vision-Language-Action Models","url":"https://robotics-transformer2.github.io/"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"}]

Based on the search results, I can confirm the following about arxiv paper 2307.15818:

**Paper Details:**
- Title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
- First author: Anthony Brohan (with 53 other authors)

**Regarding author alphabetization:** The complete author list in alphabetical order is: Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, Pete Florence, Chuyuan Fu, Montse Gonzalez Arenas, Keerthana Gopalakrishnan, Kehang Han, Karol Hausman, Alexander Herzog, Jasmine Hsu, Brian Ichter, Alex Irpan, Nikhil J. Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Isabel Leal, Lisa Lee, Tsang-Wei Edward Lee, Sergey Levine, Yao Lu, Henryk Michalewski, Igor Mordatch, Karl Pertsch, Kanishka Rao, Krista Reymann, Michael S. Ryoo, Grecia Salazar, Pannag Sanketi, Pierre Sermanet, Jaspiar Singh, Anikait Singh, Radu Soricut, Huong T. Tran, Vincent Vanhoucke, Quan Vuong, Ayzaan Wahid, Stefan Welker, Paul Wohlhart, Jialin Wu, Fei Xia, Ted Xiao, Peng Xu, Sichun Xu, Tianhe Yu, and Brianna Zitkovich. 

Anthony Brohan is indeed listed as the first author alphabetically (his surname "Brohan" comes before "Brown," "Carbajal," etc.).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "03c24989-956e-4e03-aab1-7ff3d6ecb8e5"
}
```

</details>

---


### Tool result

_source line 392 · 2026-05-29T06:33:42.350Z_

<details><summary>↩ Tool result · `toolu_01TTyMxE8JpCLWjjsnnA5ux3`</summary>

```text
Web search results for query: "RoboFlamingo ICLR 2024 accepted Li Xinghang title exact"

Links: [{"title":"Vision-Language Foundation Models as Effective Robot Imitators | OpenReview","url":"https://openreview.net/forum?id=lFYj0oibGR"},{"title":"[Quick Review] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://liner.com/review/visionlanguage-foundation-models-as-effective-robot-imitators"},{"title":"RoboFlamingo | Vision-Language Foundation Models as Effective Robot Imitators","url":"https://roboflamingo.github.io/"},{"title":"RoboFlamingo Review | gracefullight.dev","url":"https://gracefullight.dev/en/2025/08/31/roboflamingo-review/"},{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"RoboFlamingo-Plus: Fusion of Depth and RGB Perception with   Vision-Language Models for Enhanced Robotic Manipulation","url":"https://arxiv.org/pdf/2503.19510"},{"title":"RoboFlamingo - Overview","url":"https://github.com/roboflamingo"},{"title":"GitHub - RoboFlamingo/RoboFlamingo: Code for RoboFlamingo · GitHub","url":"https://github.com/RoboFlamingo/RoboFlamingo"}]

Based on the search results, I found information about RoboFlamingo by Li Xinghang. However, the paper appears to have been published as a preprint on arXiv in 2023, not accepted to ICLR 2024.

The exact title is "Vision-Language Foundation Models as Effective Robot Imitators", authored by Xinghang Li and colleagues from ByteDance Research, Tsinghua University, Shanghai Jiao Tong University, and National University of Singapore.

The search results show this as an ICLR 2023 paper rather than ICLR 2024. The paper was first submitted to arXiv on November 2, 2023, according to the search results. If you're looking for information about an ICLR 2024 acceptance of this work, I would need to search for more recent publication information to verify that specific claim.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "585cfe85-016a-4b6a-b6e0-e24ed0260476"
}
```

</details>

---


### System

_source line 393_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for openreview.net \"Vision-Language Foundation Models…",
  "usage": {
    "total_tokens": 39328,
    "tool_uses": 27,
    "duration_ms": 96158
  },
  "last_tool_name": "WebSearch",
  "uuid": "b300f76c-a850-4f9a-9d4c-3c6035064b5b",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 394_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YPsbAsUmdiCUvzWB63BKfs`</summary>

```json
{
  "query": "openreview.net \"Vision-Language Foundation Models as Effective Robot Imitators\" ICLR 2024 accepted decision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "d484f7bc-807a-48a4-8667-af3d498ef833",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UciaZu8LQczgbBGt5kHoem",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1777,
      "cache_read_input_tokens": 36698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1777,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 395_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "adda7656f92cca819",
  "tool_use_id": "toolu_01C92XVpJdWF8gv5ndt6qErS",
  "status": "completed",
  "output_file": "",
  "summary": "Verify bib entries group 1",
  "usage": {
    "total_tokens": 33547,
    "tool_uses": 21,
    "duration_ms": 146987
  },
  "uuid": "b73880ab-59ff-47b5-933c-96d7440058ac",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool result

_source line 396 · 2026-05-29T06:33:49.810Z_

<details><summary>↩ Tool result · `toolu_01C92XVpJdWF8gv5ndt6qErS`</summary>

```text
Earlier search results did find an ICML 2026 poster page for this paper. Let me confirm the year for the Compressor-VLA entry — the arXiv ID 2511.* indicates November 2025, which matches the claimed year 2025.

Here is the structured verification checklist:

---

## Reference Verification Checklist

### 1. abnar2020quantifying
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title | "Quantifying Attention Flow in Transformers" | "Quantifying Attention Flow in Transformers" | OK |
| Authors | Abnar, Samira and Zuidema, Willem | Samira Abnar, Willem Zuidema | OK |
| Year | 2020 | 2020 | OK |
| Venue | ACL 2020 | ACL 2020 (Proceedings of the 58th Annual Meeting of the ACL) | OK |
| Pages | 4190-4197 | 4190-4197 (ACL Anthology confirms) | OK |
| **Verdict** | **PASS -- no issues** |

---

### 2. gao2025compressorvla
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title | "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation" | Exact match on arXiv | OK |
| Authors | Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing | Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian | OK |
| Year | 2025 | arXiv ID 2511.18950 = November 2025 | OK |
| Venue | arXiv preprint | arXiv preprint | OK |
| arXiv ID | 2511.18950 | 2511.18950 | OK |
| **Verdict** | **PASS -- no issues** |

---

### 3. wang2025specprunevla
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title | "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning" | Exact match on arXiv | OK |
| Authors | Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao | Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai | OK |
| Year | 2025 | arXiv submitted September 2025 | OK |
| Venue | arXiv preprint | arXiv preprint | OK |
| arXiv ID | 2509.05614 | 2509.05614 | OK |
| **Verdict** | **PASS -- no issues** |

---

### 4. jiang2026lightvla
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title | "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning" | Exact match on arXiv (note: arXiv uses lowercase "language-action" in subtitle) | OK |
| Authors | Jiang, Titong and others | First author Titong Jiang confirmed; full list: Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang | OK |
| Year | 2026 (ICRA) | GitHub repo states "ICRA 2026" | OK |
| Venue | ICRA 2026 | Confirmed ICRA 2026 via GitHub and ICRA author index | OK |
| arXiv ID | 2509.12594 | 2509.12594 | OK |
| **Verdict** | **PASS -- no issues. Note: arXiv preprint is from Sep 2025; bib year 2026 is correct as it refers to the ICRA 2026 publication year.** |

---

### 5. feng2026seewhatmatters
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title | "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" | Exact match on arXiv | OK |
| Authors | Feng, Yixu and others | First author Yixu Feng confirmed; full list: Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu | OK |
| Year | 2026 | arXiv submitted May 2026 | OK |
| Venue | ICML 2026 | Confirmed via ICML 2026 virtual poster page (icml.cc/virtual/2026/poster/65010) | OK |
| arXiv ID | 2605.11817 | 2605.11817 | OK |
| **Verdict** | **PASS -- no issues** |

---

### 6. zhang2025sparsevlm
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title | "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference" | Exact match | OK |
| Authors | Zhang, Yuan and others | First author Yuan Zhang confirmed; full list: Yuan Zhang, Chun-Kai Fan, Junpeng Ma, Wenzhao Zheng, Tao Huang, Kuan Cheng, Denis Gudovskiy, Tomoyuki Okuno, Yohei Nakata, Kurt Keutzer, Shanghang Zhang | OK |
| Year | 2025 | ICML 2025 | OK |
| Venue | ICML 2025 | Confirmed via ICML 2025 poster page and GitHub [ICML'25] tag | OK |
| arXiv ID | 2410.04417 | 2410.04417 | OK |
| **Verdict** | **PASS -- no issues. Note: arXiv preprint is from Oct 2024; bib year 2025 correctly refers to the ICML 2025 venue year.** |

---

### 7. khaki2025sparsevila
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title (bib) | "SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference" | — | **MISMATCH** |
| Title (actual) | — | "SparseVILA: **Decoupling** Visual Sparsity for Efficient VLM Inference" | — |
| Authors | Khaki, Samir and others | First author Samir Khaki confirmed; full list: Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Konstantinos N. Plataniotis, Yao Lu, Song Han, Zhijian Liu | OK |
| Year | 2025 | ICCV 2025 | OK |
| Venue | ICCV 2025 | Confirmed via ICCV 2025 poster page (iccv.thecvf.com) | OK |
| arXiv ID | 2510.17777 | 2510.17777 | OK |
| **Verdict** | **FAIL -- Title error: "Decoupled" should be "Decoupling". The actual title uses the gerund form "Decoupling", not the past participle "Decoupled".** |

---

### 8. jabbour2025dontrun
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title | "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" | Exact match on arXiv | OK |
| Authors | Jabbour, Jason and others | First author Jason Jabbour confirmed; full list: Jason Jabbour, Dong-Ki Kim, Max Smith, Jay Patrikar, Radhika Ghosal, Youhui Wang, Ali Agha, Vijay Janapa Reddi, Shayegan Omidshafiei | OK |
| Year | 2025 | arXiv submitted October 2025 | OK |
| Venue | arXiv preprint | arXiv preprint (also on OpenReview but no confirmed conference acceptance found) | OK |
| arXiv ID | 2510.08464 | 2510.08464 | OK |
| **Verdict** | **PASS -- no issues** |

---

## Summary

| # | Key | Status | Issue |
|---|---|---|---|
| 1 | abnar2020quantifying | PASS | None |
| 2 | gao2025compressorvla | PASS | None |
| 3 | wang2025specprunevla | PASS | None |
| 4 | jiang2026lightvla | PASS | None |
| 5 | feng2026seewhatmatters | PASS | None |
| 6 | zhang2025sparsevlm | PASS | None |
| 7 | khaki2025sparsevila | **FAIL** | Title says "Decoupled" but actual title is "Decoupling" |
| 8 | jabbour2025dontrun | PASS | None |

**Action required:** Fix entry #7 -- change "Decoupled" to "Decoupling" in the title.

Sources:
- [ACL Anthology - Quantifying Attention Flow](https://aclanthology.org/2020.acl-main.385/)
- [arXiv 2511.18950 - Compressor-VLA](https://arxiv.org/abs/2511.18950)
- [arXiv 2509.05614 - SpecPrune-VLA](https://arxiv.org/abs/2509.05614)
- [arXiv 2509.12594 - LightVLA](https://arxiv.org/abs/2509.12594)
- [GitHub LightVLA (ICRA 2026)](https://github.com/LiAutoAD/LightVLA)
- [arXiv 2605.11817 - See What Matters](https://arxiv.org/abs/2605.11817)
- [ICML 2026 Poster - See What Matters](https://icml.cc/virtual/2026/poster/65010)
- [arXiv 2410.04417 - SparseVLM](https://arxiv.org/abs/2410.04417)
- [ICML 2025 Poster - SparseVLM](https://icml.cc/virtual/2025/poster/46297)
- [GitHub SparseVLMs [ICML'25]](https://github.com/Gumpest/SparseVLMs)
- [arXiv 2510.17777 - SparseVILA](https://arxiv.org/abs/2510.17777)
- [ICCV 2025 Poster - SparseVILA](https://iccv.thecvf.com/virtual/2025/poster/1739)
- [arXiv 2510.08464 - Don't Run with Scissors](https://arxiv.org/abs/2510.08464)
- [OpenReview - Don't Run with Scissors](https://openreview.net/forum?id=c8g57pKdXD)

agentId: adda7656f92cca819 (use SendMessage with to: 'adda7656f92cca819' to continue this agent)
&lt;usage>total_tokens: 36014
tool_uses: 21
duration_ms: 146993&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "60cd2ae0-d3ad-4a07-81a7-7c25179bbfe2",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. abnar2020quantifying: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. ACL 2020, pages 4190-4197.\n\n2. gao2025compressorvla: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\" by Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing. arXiv 2511.18950, year 2025.\n\n3. wang2025specprunevla: \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\" by Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao. arXiv 2509.05614, year 2025.\n\n4. jiang2026lightvla: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\" by Jiang, Titong and others. ICRA 2026, arXiv 2509.12594.\n\n5. feng2026seewhatmatters: \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" by Feng, Yixu and others. ICML 2026, arXiv 2605.11817.\n\n6. zhang2025sparsevlm: \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" by Zhang, Yuan and others. ICML 2025, arXiv 2410.04417.\n\n7. khaki2025sparsevila: \"SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference\" by Khaki, Samir and others. ICCV 2025, arXiv 2510.17777.\n\n8. jabbour2025dontrun: \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" by Jabbour, Jason and others. arXiv 2510.08464, year 2025.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found.",
    "agentId": "adda7656f92cca819",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Earlier search results did find an ICML 2026 poster page for this paper. Let me confirm the year for the Compressor-VLA entry — the arXiv ID 2511.* indicates November 2025, which matches the claimed year 2025.\n\nHere is the structured verification checklist:\n\n---\n\n## Reference Verification Checklist\n\n### 1. abnar2020quantifying\n| Field | Bib Entry | Verified | Match? |\n|---|---|---|---|\n| Exists | — | Yes | OK |\n| Title | \"Quantifying Attention Flow in Transformers\" | \"Quantifying Attention Flow in Transformers\" | OK |\n| Authors | Abnar, Samira and Zuidema, Willem | Samira Abnar, Willem Zuidema | OK |\n| Year | 2020 | 2020 | OK |\n| Venue | ACL 2020 | ACL 2020 (Proceedings of the 58th Annual Meeting of the ACL) | OK |\n| Pages | 4190-4197 | 4190-4197 (ACL Anthology confirms) | OK |\n| **Verdict** | **PASS -- no issues** |\n\n---\n\n### 2. gao2025compressorvla\n| Field | Bib Entry | Verified | Match? |\n|---|---|---|---|\n| Exists | — | Yes | OK |\n| Title | \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\" | Exact match on arXiv | OK |\n| Authors | Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing | Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian | OK |\n| Year | 2025 | arXiv ID 2511.18950 = November 2025 | OK |\n| Venue | arXiv preprint | arXiv preprint | OK |\n| arXiv ID | 2511.18950 | 2511.18950 | OK |\n| **Verdict** | **PASS -- no issues** |\n\n---\n\n### 3. wang2025specprunevla\n| Field | Bib Entry | Verified | Match? |\n|---|---|---|---|\n| Exists | — | Yes | OK |\n| Title | \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\" | Exact match on arXiv | OK |\n| Authors | Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao | Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai | OK |\n| Year | 2025 | arXiv submitted September 2025 | OK |\n| Venue | arXiv preprint | arXiv preprint | OK |\n| arXiv ID | 2509.05614 | 2509.05614 | OK |\n| **Verdict** | **PASS -- no issues** |\n\n---\n\n### 4. jiang2026lightvla\n| Field | Bib Entry | Verified | Match? |\n|---|---|---|---|\n| Exists | — | Yes | OK |\n| Title | \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\" | Exact match on arXiv (note: arXiv uses lowercase \"language-action\" in subtitle) | OK |\n| Authors | Jiang, Titong and others | First author Titong Jiang confirmed; full list: Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang | OK |\n| Year | 2026 (ICRA) | GitHub repo states \"ICRA 2026\" | OK |\n| Venue | ICRA 2026 | Confirmed ICRA 2026 via GitHub and ICRA author index | OK |\n| arXiv ID | 2509.12594 | 2509.12594 | OK |\n| **Verdict** | **PASS -- no issues. Note: arXiv preprint is from Sep 2025; bib year 2026 is correct as it refers to the ICRA 2026 publication year.** |\n\n---\n\n### 5. feng2026seewhatmatters\n| Field | Bib Entry | Verified | Match? |\n|---|---|---|---|\n| Exists | — | Yes | OK |\n| Title | \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" | Exact match on arXiv | OK |\n| Authors | Feng, Yixu and others | First author Yixu Feng confirmed; full list: Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu | OK |\n| Year | 2026 | arXiv submitted May 2026 | OK |\n| Venue | ICML 2026 | Confirmed via ICML 2026 virtual poster page (icml.cc/virtual/2026/poster/65010) | OK |\n| arXiv ID | 2605.11817 | 2605.11817 | OK |\n| **Verdict** | **PASS -- no issues** |\n\n---\n\n### 6. zhang2025sparsevlm\n| Field | Bib Entry | Verified | Match? |\n|---|---|---|---|\n| Exists | — | Yes | OK |\n| Title | \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" | Exact match | OK |\n| Authors | Zhang, Yuan and others | First author Yuan Zhang confirmed; full list: Yuan Zhang, Chun-Kai Fan, Junpeng Ma, Wenzhao Zheng, Tao Huang, Kuan Cheng, Denis Gudovskiy, Tomoyuki Okuno, Yohei Nakata, Kurt Keutzer, Shanghang Zhang | OK |\n| Year | 2025 | ICML 2025 | OK |\n| Venue | ICML 2025 | Confirmed via ICML 2025 poster page and GitHub [ICML'25] tag | OK |\n| arXiv ID | 2410.04417 | 2410.04417 | OK |\n| **Verdict** | **PASS -- no issues. Note: arXiv preprint is from Oct 2024; bib year 2025 correctly refers to the ICML 2025 venue year.** |\n\n---\n\n### 7. khaki2025sparsevila\n| Field | Bib Entry | Verified | Match? |\n|---|---|---|---|\n| Exists | — | Yes | OK |\n| Title (bib) | \"SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference\" | — | **MISMATCH** |\n| Title (actual) | — | \"SparseVILA: **Decoupling** Visual Sparsity for Efficient VLM Inference\" | — |\n| Authors | Khaki, Samir and others | First author Samir Khaki confirmed; full list: Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Konstantinos N. Plataniotis, Yao Lu, Song Han, Zhijian Liu | OK |\n| Year | 2025 | ICCV 2025 | OK |\n| Venue | ICCV 2025 | Confirmed via ICCV 2025 poster page (iccv.thecvf.com) | OK |\n| arXiv ID | 2510.17777 | 2510.17777 | OK |\n| **Verdict** | **FAIL -- Title error: \"Decoupled\" should be \"Decoupling\". The actual title uses the gerund form \"Decoupling\", not the past participle \"Decoupled\".** |\n\n---\n\n### 8. jabbour2025dontrun\n| Field | Bib Entry | Verified | Match? |\n|---|---|---|---|\n| Exists | — | Yes | OK |\n| Title | \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" | Exact match on arXiv | OK |\n| Authors | Jabbour, Jason and others | First author Jason Jabbour confirmed; full list: Jason Jabbour, Dong-Ki Kim, Max Smith, Jay Patrikar, Radhika Ghosal, Youhui Wang, Ali Agha, Vijay Janapa Reddi, Shayegan Omidshafiei | OK |\n| Year | 2025 | arXiv submitted October 2025 | OK |\n| Venue | arXiv preprint | arXiv preprint (also on OpenReview but no confirmed conference acceptance found) | OK |\n| arXiv ID | 2510.08464 | 2510.08464 | OK |\n| **Verdict** | **PASS -- no issues** |\n\n---\n\n## Summary\n\n| # | Key | Status | Issue |\n|---|---|---|---|\n| 1 | abnar2020quantifying | PASS | None |\n| 2 | gao2025compressorvla | PASS | None |\n| 3 | wang2025specprunevla | PASS | None |\n| 4 | jiang2026lightvla | PASS | None |\n| 5 | feng2026seewhatmatters | PASS | None |\n| 6 | zhang2025sparsevlm | PASS | None |\n| 7 | khaki2025sparsevila | **FAIL** | Title says \"Decoupled\" but actual title is \"Decoupling\" |\n| 8 | jabbour2025dontrun | PASS | None |\n\n**Action required:** Fix entry #7 -- change \"Decoupled\" to \"Decoupling\" in the title.\n\nSources:\n- [ACL Anthology - Quantifying Attention Flow](https://aclanthology.org/2020.acl-main.385/)\n- [arXiv 2511.18950 - Compressor-VLA](https://arxiv.org/abs/2511.18950)\n- [arXiv 2509.05614 - SpecPrune-VLA](https://arxiv.org/abs/2509.05614)\n- [arXiv 2509.12594 - LightVLA](https://arxiv.org/abs/2509.12594)\n- [GitHub LightVLA (ICRA 2026)](https://github.com/LiAutoAD/LightVLA)\n- [arXiv 2605.11817 - See What Matters](https://arxiv.org/abs/2605.11817)\n- [ICML 2026 Poster - See What Matters](https://icml.cc/virtual/2026/poster/65010)\n- [arXiv 2410.04417 - SparseVLM](https://arxiv.org/abs/2410.04417)\n- [ICML 2025 Poster - SparseVLM](https://icml.cc/virtual/2025/poster/46297)\n- [GitHub SparseVLMs [ICML'25]](https://github.com/Gumpest/SparseVLMs)\n- [arXiv 2510.17777 - SparseVILA](https://arxiv.org/abs/2510.17777)\n- [ICCV 2025 Poster - SparseVILA](https://iccv.thecvf.com/virtual/2025/poster/1739)\n- [arXiv 2510.08464 - Don't Run with Scissors](https://arxiv.org/abs/2510.08464)\n- [OpenReview - Don't Run with Scissors](https://openreview.net/forum?id=c8g57pKdXD)"
      }
    ],
    "totalDurationMs": 146993,
    "totalTokens": 36014,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1365,
      "cache_read_input_tokens": 31566,
      "output_tokens": 3082,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1365
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3082,
          "cache_read_input_tokens": 31566,
          "cache_creation_input_tokens": 1365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1365,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-29T06:33:53.068Z_

<details><summary>↩ Tool result · `toolu_01YPsbAsUmdiCUvzWB63BKfs`</summary>

```text
Web search results for query: "openreview.net "Vision-Language Foundation Models as Effective Robot Imitators" ICLR 2024 accepted decision"

Links: [{"title":"Vision-Language Foundation Models as Effective Robot Imitators | OpenReview","url":"https://openreview.net/forum?id=lFYj0oibGR"},{"title":"[Quick Review] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://liner.com/review/visionlanguage-foundation-models-as-effective-robot-imitators"},{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions","url":"https://arxiv.org/html/2505.11214v1"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/html/2411.19650v1"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"Can Pretrained Vision-Language Embeddings Alone Guide Robot Navigation?","url":"https://arxiv.org/pdf/2506.14507"},{"title":"RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation","url":"https://arxiv.org/html/2406.04339v2"}]

Based on the search results, I found the paper "Vision-Language Foundation Models as Effective Robot Imitators" on OpenReview. The paper presents RoboFlamingo, a vision-language manipulation framework built upon OpenFlamingo that utilizes pre-trained vision-language models for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is fine-tuned by imitation learning on language-conditioned manipulation datasets.

However, I should note that the search results indicate this paper was presented at The Twelfth International Conference on Learning Representations in October 2023, not ICLR 2024. The paper appears to have been submitted to ICLR 2023 and is available on OpenReview at https://openreview.net/forum?id=lFYj0oibGR.

Unfortunately, the search results do not explicitly show the specific acceptance decision status from OpenReview. To find the exact decision information, you would need to visit the OpenReview page directly, where the decision status should be displayed at the top of the forum page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "d89f60ae-e9d9-40b9-937c-f4686c5b2ca4"
}
```

</details>

---


### System

_source line 398_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "description": "Searching for site:openreview.net \"Vision-Language Foundation M…",
  "usage": {
    "total_tokens": 40145,
    "tool_uses": 28,
    "duration_ms": 105247
  },
  "last_tool_name": "WebSearch",
  "uuid": "3ab471ba-0986-4d2d-a661-2ad613f2fe88",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool call

_source line 399_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018PdGkTuWG3NAd7YX74jjnS`</summary>

```json
{
  "query": "site:openreview.net \"Vision-Language Foundation Models as Effective Robot Imitators\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "9868bfd8-38fe-47cc-b205-1876640d3e6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155mUiGTRJXFhG9nMUyeVUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 38475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 400 · 2026-05-29T06:34:02.384Z_

<details><summary>↩ Tool result · `toolu_018PdGkTuWG3NAd7YX74jjnS`</summary>

```text
Web search results for query: "site:openreview.net "Vision-Language Foundation Models as Effective Robot Imitators" ICLR 2024"

Links: [{"title":"Vision-Language Foundation Models as Effective Robot Imitators | OpenReview","url":"https://openreview.net/forum?id=lFYj0oibGR"},{"title":"ICLR Poster Vision-Language Foundation Models as Effective Robot Imitators","url":"https://iclr.cc/virtual/2024/poster/17943"},{"title":"[Quick Review] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://liner.com/review/visionlanguage-foundation-models-as-effective-robot-imitators"},{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents | OpenReview","url":"https://openreview.net/forum?id=xVlcbh0poD"},{"title":"Can Pretrained Vision-Language Embeddings Alone Guide Robot Navigation?","url":"https://arxiv.org/pdf/2506.14507"},{"title":"RoboFlamingo | Vision-Language Foundation Models as Effective Robot Imitators","url":"https://roboflamingo.github.io/"},{"title":"Foundation Model Driven Robotics: A Comprehensive Review","url":"https://arxiv.org/pdf/2507.10087"}]

I found the paper you're looking for! Here are the search results:

"Vision-Language Foundation Models as Effective Robot Imitators" presents RoboFlamingo, a framework built upon OpenFlamingo that leverages vision-language models for robotics manipulation.

**Key Details:**

- **Paper Title:** Vision-Language Foundation Models as Effective Robot Imitators
- **Venue:** ICLR 2024 (presented as a poster on May 7, 2024)
- **OpenReview Link:** https://openreview.net/forum?id=lFYj0oibGR

**Main Contributions:**

RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned manipulation datasets.

**Performance:**

RoboFlamingo significantly outperforms existing methods in imitation learning performance on language-conditioned robotic manipulation tasks, achieving a 2x improvement over the previous state-of-the-art method (HULC) on the CALVIN benchmark.

The paper is also available on arXiv as paper 2311.01378 and has an official project website at roboflamingo.github.io.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "3234cf61-5004-4d8c-9957-de9923c8bbcc"
}
```

</details>

---


### System

_source line 401_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aa47d6ba91b6bb196",
  "tool_use_id": "toolu_015a21kJux6TDH1RMLQES3F4",
  "status": "completed",
  "output_file": "",
  "summary": "Verify bib entries group 6",
  "usage": {
    "total_tokens": 40938,
    "tool_uses": 28,
    "duration_ms": 171272
  },
  "uuid": "3b6abf99-ce85-415c-9331-3b306333cb1d",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe"
}
```

---


### Tool result

_source line 402 · 2026-05-29T06:35:01.822Z_

<details><summary>↩ Tool result · `toolu_015a21kJux6TDH1RMLQES3F4`</summary>

```text
Good, ICLR 2024 is confirmed. Now I have all the information I need. Let me compile the structured verification checklist.

Here is the structured verification checklist for all 15 entries:

---

## Reference Verification Checklist

### 1. shi2024crossget — CrossGET
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers" | Same | YES |
| Authors | Shi, Dachuan and others | Dachuan Shi, Chaofan Tao, Anyi Rao, Zhendong Yang, Chun Yuan, Jiaqi Wang | YES |
| Year | 2024 | 2024 | YES |
| Venue | ICML 2024 | ICML 2024 | YES |
| arXiv ID | 2305.17455 | 2305.17455 | YES |
| **Issues** | None | | |

---

### 2. oquab2023dinov2 / oquab2024dinov2 — DINOv2
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "DINOv2: Learning Robust Visual Features without Supervision" | Same | YES |
| Authors | Oquab, Maxime and others | Maxime Oquab, Timothee Darcet, et al. | YES |
| Year | 2024 (both entries) | 2024 (TMLR publication: January 2024) | YES |
| Venue | TMLR | Transactions on Machine Learning Research (TMLR) | YES |
| arXiv ID | 2304.07193 | 2304.07193 | YES |
| **Issues** | **Duplicate bib keys**: `oquab2023dinov2` and `oquab2024dinov2` both exist with year=2024. The key `oquab2023dinov2` is misleading — the "2023" in the key suggests year 2023, but the year field says 2024. The arXiv preprint was April 2023, the TMLR publication was January 2024. Recommend keeping only one entry (e.g., `oquab2024dinov2`) with year=2024 and removing the duplicate. | | |

---

### 3. su2024roformer — RoFormer
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "RoFormer: Enhanced Transformer with Rotary Position Embedding" | Same | YES |
| Authors | Su, Jianlin and others | Jianlin Su, Murtadha H.M. Ahmed, Yu Lu, Shengfeng Pan, Wen Bo, Yunfeng Liu | YES |
| Year | 2024 | 2024 | YES |
| Venue | Neurocomputing | Neurocomputing | YES |
| Volume/Pages | volume 568, pages 127063 | Volume 568, article 127063 | YES |
| **Issues** | None | | |

---

### 4. abnar2020quantifying — Quantifying Attention Flow
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "Quantifying Attention Flow in Transformers" | Same | YES |
| Authors | Abnar, Samira and Zuidema, Willem | Same | YES |
| Year | 2020 | 2020 | YES |
| Venue | ACL 2020 | ACL 2020 (Proceedings of the 58th Annual Meeting of the ACL) | YES |
| Pages | 4190-4197 | 4190-4197 | YES |
| **Issues** | None | | |

---

### 5. li2024roboflamingo — RoboFlamingo
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "Vision-Language Foundation Models as Effective Robot Imitators" | Same | YES |
| Authors | Li, Xinghang and others | Xinghang Li, Minghuan Liu, Hanbo Zhang, et al. | YES |
| Year | 2024 | 2024 | YES |
| Venue | ICLR 2024 | ICLR 2024 (poster) | YES |
| arXiv ID | 2311.01378 | 2311.01378 | YES |
| **Issues** | None | | |

---

### 6. alayrac2022flamingo — Flamingo
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "Flamingo: a Visual Language Model for Few-Shot Learning" | Same | YES |
| Authors | Alayrac, Jean-Baptiste and others | Jean-Baptiste Alayrac, Jeff Donahue, et al. | YES |
| Year | 2022 | 2022 | YES |
| Venue | NeurIPS 2022 | NeurIPS 2022 | YES |
| **Issues** | None | | |

---

### 7. jaegle2021perceiver — Perceiver
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "Perceiver: General Perception with Iterative Attention" | Same | YES |
| Authors | Jaegle, Andrew and others | Andrew Jaegle, Felix Gimeno, Andy Brock, Oriol Vinyals, Andrew Zisserman, Joao Carreira | YES |
| Year | 2021 | 2021 | YES |
| Venue | ICML 2021 | ICML 2021 | YES |
| **Issues** | None | | |

---

### 8. zitkovich2023rt2 / brohan2023rt2 — RT-2
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" | Same | YES |
| Year | 2023 | 2023 | YES |
| Venue | CoRL 2023 | CoRL 2023 (PMLR 229) | YES |
| arXiv ID | 2307.15818 | 2307.15818 | YES |
| **Issues** | **Author ordering discrepancy between arXiv and CoRL proceedings.** On arXiv, the authors are listed alphabetically starting with Anthony Brohan. In the CoRL proceedings (PMLR), the entry is filed as `zitkovich23a`, with Brianna Zitkovich listed first. The bib entry `zitkovich2023rt2` with "Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun..." matches the CoRL proceedings ordering. The `brohan2023rt2` entry with "Brohan, Anthony" as first author matches the arXiv ordering. **Both are technically correct for their respective sources.** For consistency, use whichever matches the source you cite (CoRL proceedings = Zitkovich first; arXiv = Brohan first, alphabetical). Remove the duplicate entry. | | |

---

### 9. openxembodiment2024 — Open X-Embodiment
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "Open X-Embodiment: Robotic Learning Datasets and RT-X Models" | Same | YES |
| Authors | Open X-Embodiment Collaboration | Same | YES |
| Year | 2024 | 2024 | YES |
| Venue | ICRA 2024 | IEEE ICRA 2024 (Best Paper Award) | YES |
| arXiv ID | 2310.08864 | 2310.08864 | YES |
| **Issues** | None | | |

---

### 10. zhang2023h2o — H2O
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models" | Same | YES |
| Authors | Zhang, Zhenyu and others | Zhenyu Zhang, Ying Sheng, Tianyi Zhou, et al. | YES |
| Year | 2023 | 2023 | YES |
| Venue | NeurIPS 2023 | NeurIPS 2023 | YES |
| arXiv ID | 2306.14048 | 2306.14048 | YES |
| **Issues** | None | | |

---

### 11. xiao2024streamingllm — StreamingLLM
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "Efficient Streaming Language Models with Attention Sinks" | Same | YES |
| Authors | Xiao, Guangxuan and others | Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, Mike Lewis | YES |
| Year | 2024 | 2024 | YES |
| Venue | ICLR 2024 | ICLR 2024 | YES |
| arXiv ID | 2309.17453 | 2309.17453 | YES |
| **Issues** | None | | |

---

### 12. mees2022calvin — CALVIN
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks" | Same | YES |
| Authors | Mees, Oier and others | Oier Mees, Lukas Hermann, Erick Rosete-Beas, Wolfram Burgard | YES |
| Year | 2022 | 2022 | YES |
| Venue | IEEE Robotics and Automation Letters (RA-L) | IEEE RA-L, vol. 7, no. 3, pp. 7327-7334 | YES |
| arXiv ID | 2112.03227 | 2112.03227 | YES |
| **Issues** | None | | |

---

### 13. chi2023diffusionpolicy — Diffusion Policy
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion" | Same | YES |
| Authors | Chi, Cheng and others | Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, Shuran Song | YES |
| Year | 2023 | 2023 | YES |
| Venue | RSS 2023 | RSS 2023 (Robotics: Science and Systems) | YES |
| arXiv ID | 2303.04137 | 2303.04137 | YES |
| **Issues** | None | | |

---

### 14. zeng2023transformers_tsf — Are Transformers Effective for TSF?
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "Are Transformers Effective for Time Series Forecasting?" | Same | YES |
| Authors | Zeng, Ailing and others | Ailing Zeng, Muxi Chen, Lei Zhang, Qiang Xu | YES |
| Year | 2023 | 2023 | YES |
| Venue | AAAI 2023 | AAAI 2023 (vol. 37, no. 9, pp. 11121-11128) | YES |
| arXiv ID | 2205.13504 | 2205.13504 | YES |
| **Issues** | None | | |

---

### 15. bouthillier2024negative — Embracing Negative Results
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "Position: Embracing Negative Results in Machine Learning" | Same | YES |
| Authors | Bouthillier, Xavier and others | **Florian Karl, Lukas Malte Kemeter, Gabriel Dax, Paulina Sierak** | **NO** |
| Year | 2024 | 2024 | YES |
| Venue | ICML 2024 | ICML 2024 (PMLR 235:23256-23265) | YES |
| arXiv ID | 2406.03980 | 2406.03980 | YES |
| **Issues** | **WRONG FIRST AUTHOR.** The bib key `bouthillier2024negative` and author field listing "Bouthillier, Xavier" is incorrect. The actual first author is **Florian Karl**. Xavier Bouthillier does not appear in the author list of this paper. The correct authors are Karl, Kemeter, Dax, and Sierak. The bib key should be something like `karl2024negative` or `karl2024position`. This must be corrected. | | |

---

## Summary of Issues Found

| # | Entry | Severity | Issue |
|---|-------|----------|-------|
| 2 | oquab2023dinov2 / oquab2024dinov2 | Minor | Duplicate bib entries. Key `oquab2023dinov2` is misleading (implies year 2023 but field says 2024). Remove one. |
| 8 | zitkovich2023rt2 / brohan2023rt2 | Minor | Two bib entries for the same paper with different first-author orderings. Both are valid depending on source (CoRL proceedings vs arXiv). Remove duplicate; pick one consistently. |
| **15** | **bouthillier2024negative** | **CRITICAL** | **Wrong author. First author is Florian Karl, not Xavier Bouthillier. Bib key and author field must be corrected.** |

All other 12 entries verified clean with correct titles, authors, years, venues, and arXiv IDs.

agentId: aa47d6ba91b6bb196 (use SendMessage with to: 'aa47d6ba91b6bb196' to continue this agent)
&lt;usage>total_tokens: 43778
tool_uses: 28
duration_ms: 171276&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "5c20cd79-1cc1-4e29-9ff7-ff3d412d9cde",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. shi2024crossget: \"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers\" by Shi, Dachuan and others. ICML 2024, arXiv 2305.17455.\n\n2. oquab2023dinov2 / oquab2024dinov2: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime and others. Listed as Transactions on Machine Learning Research (TMLR). Bib has two entries: one with key oquab2023dinov2 (year=2024) and one oquab2024dinov2 (year=2024, arXiv 2304.07193). Check which year is correct and if TMLR is the correct venue.\n\n3. su2024roformer: \"RoFormer: Enhanced Transformer with Rotary Position Embedding\" by Su, Jianlin and others. Neurocomputing, volume 568, pages 127063, year 2024.\n\n4. abnar2020quantifying: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. ACL 2020, pages 4190-4197.\n\n5. li2024roboflamingo: \"Vision-Language Foundation Models as Effective Robot Imitators\" by Li, Xinghang and others. ICLR 2024, arXiv 2311.01378.\n\n6. alayrac2022flamingo: \"Flamingo: a Visual Language Model for Few-Shot Learning\" by Alayrac, Jean-Baptiste and others. NeurIPS 2022.\n\n7. jaegle2021perceiver: \"Perceiver: General Perception with Iterative Attention\" by Jaegle, Andrew and others. ICML 2021.\n\n8. zitkovich2023rt2: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others. CoRL 2023, arXiv 2307.15818. NOTE: There's also a brohan2023rt2 entry with Brohan, Anthony as first author. Check which author list is correct for RT-2.\n\n9. openxembodiment2024: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\" by Open X-Embodiment Collaboration. ICRA 2024, arXiv 2310.08864.\n\n10. zhang2023h2o: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\" by Zhang, Zhenyu and others. NeurIPS 2023, arXiv 2306.14048.\n\n11. xiao2024streamingllm: \"Efficient Streaming Language Models with Attention Sinks\" by Xiao, Guangxuan and others. ICLR 2024, arXiv 2309.17453.\n\n12. mees2022calvin: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\" by Mees, Oier and others. IEEE Robotics and Automation Letters, year 2022, arXiv 2112.03227.\n\n13. chi2023diffusionpolicy: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\" by Chi, Cheng and others. RSS 2023, arXiv 2303.04137.\n\n14. zeng2023transformers_tsf: \"Are Transformers Effective for Time Series Forecasting?\" by Zeng, Ailing and others. AAAI 2023, arXiv 2205.13504.\n\n15. bouthillier2024negative: \"Position: Embracing Negative Results in Machine Learning\" by Bouthillier, Xavier and others. ICML 2024, arXiv 2406.03980.\n\nFor each, search on Google Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found.",
    "agentId": "aa47d6ba91b6bb196",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Good, ICLR 2024 is confirmed. Now I have all the information I need. Let me compile the structured verification checklist.\n\nHere is the structured verification checklist for all 15 entries:\n\n---\n\n## Reference Verification Checklist\n\n### 1. shi2024crossget — CrossGET\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers\" | Same | YES |\n| Authors | Shi, Dachuan and others | Dachuan Shi, Chaofan Tao, Anyi Rao, Zhendong Yang, Chun Yuan, Jiaqi Wang | YES |\n| Year | 2024 | 2024 | YES |\n| Venue | ICML 2024 | ICML 2024 | YES |\n| arXiv ID | 2305.17455 | 2305.17455 | YES |\n| **Issues** | None | | |\n\n---\n\n### 2. oquab2023dinov2 / oquab2024dinov2 — DINOv2\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"DINOv2: Learning Robust Visual Features without Supervision\" | Same | YES |\n| Authors | Oquab, Maxime and others | Maxime Oquab, Timothee Darcet, et al. | YES |\n| Year | 2024 (both entries) | 2024 (TMLR publication: January 2024) | YES |\n| Venue | TMLR | Transactions on Machine Learning Research (TMLR) | YES |\n| arXiv ID | 2304.07193 | 2304.07193 | YES |\n| **Issues** | **Duplicate bib keys**: `oquab2023dinov2` and `oquab2024dinov2` both exist with year=2024. The key `oquab2023dinov2` is misleading — the \"2023\" in the key suggests year 2023, but the year field says 2024. The arXiv preprint was April 2023, the TMLR publication was January 2024. Recommend keeping only one entry (e.g., `oquab2024dinov2`) with year=2024 and removing the duplicate. | | |\n\n---\n\n### 3. su2024roformer — RoFormer\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"RoFormer: Enhanced Transformer with Rotary Position Embedding\" | Same | YES |\n| Authors | Su, Jianlin and others | Jianlin Su, Murtadha H.M. Ahmed, Yu Lu, Shengfeng Pan, Wen Bo, Yunfeng Liu | YES |\n| Year | 2024 | 2024 | YES |\n| Venue | Neurocomputing | Neurocomputing | YES |\n| Volume/Pages | volume 568, pages 127063 | Volume 568, article 127063 | YES |\n| **Issues** | None | | |\n\n---\n\n### 4. abnar2020quantifying — Quantifying Attention Flow\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"Quantifying Attention Flow in Transformers\" | Same | YES |\n| Authors | Abnar, Samira and Zuidema, Willem | Same | YES |\n| Year | 2020 | 2020 | YES |\n| Venue | ACL 2020 | ACL 2020 (Proceedings of the 58th Annual Meeting of the ACL) | YES |\n| Pages | 4190-4197 | 4190-4197 | YES |\n| **Issues** | None | | |\n\n---\n\n### 5. li2024roboflamingo — RoboFlamingo\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"Vision-Language Foundation Models as Effective Robot Imitators\" | Same | YES |\n| Authors | Li, Xinghang and others | Xinghang Li, Minghuan Liu, Hanbo Zhang, et al. | YES |\n| Year | 2024 | 2024 | YES |\n| Venue | ICLR 2024 | ICLR 2024 (poster) | YES |\n| arXiv ID | 2311.01378 | 2311.01378 | YES |\n| **Issues** | None | | |\n\n---\n\n### 6. alayrac2022flamingo — Flamingo\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"Flamingo: a Visual Language Model for Few-Shot Learning\" | Same | YES |\n| Authors | Alayrac, Jean-Baptiste and others | Jean-Baptiste Alayrac, Jeff Donahue, et al. | YES |\n| Year | 2022 | 2022 | YES |\n| Venue | NeurIPS 2022 | NeurIPS 2022 | YES |\n| **Issues** | None | | |\n\n---\n\n### 7. jaegle2021perceiver — Perceiver\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"Perceiver: General Perception with Iterative Attention\" | Same | YES |\n| Authors | Jaegle, Andrew and others | Andrew Jaegle, Felix Gimeno, Andy Brock, Oriol Vinyals, Andrew Zisserman, Joao Carreira | YES |\n| Year | 2021 | 2021 | YES |\n| Venue | ICML 2021 | ICML 2021 | YES |\n| **Issues** | None | | |\n\n---\n\n### 8. zitkovich2023rt2 / brohan2023rt2 — RT-2\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" | Same | YES |\n| Year | 2023 | 2023 | YES |\n| Venue | CoRL 2023 | CoRL 2023 (PMLR 229) | YES |\n| arXiv ID | 2307.15818 | 2307.15818 | YES |\n| **Issues** | **Author ordering discrepancy between arXiv and CoRL proceedings.** On arXiv, the authors are listed alphabetically starting with Anthony Brohan. In the CoRL proceedings (PMLR), the entry is filed as `zitkovich23a`, with Brianna Zitkovich listed first. The bib entry `zitkovich2023rt2` with \"Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun...\" matches the CoRL proceedings ordering. The `brohan2023rt2` entry with \"Brohan, Anthony\" as first author matches the arXiv ordering. **Both are technically correct for their respective sources.** For consistency, use whichever matches the source you cite (CoRL proceedings = Zitkovich first; arXiv = Brohan first, alphabetical). Remove the duplicate entry. | | |\n\n---\n\n### 9. openxembodiment2024 — Open X-Embodiment\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\" | Same | YES |\n| Authors | Open X-Embodiment Collaboration | Same | YES |\n| Year | 2024 | 2024 | YES |\n| Venue | ICRA 2024 | IEEE ICRA 2024 (Best Paper Award) | YES |\n| arXiv ID | 2310.08864 | 2310.08864 | YES |\n| **Issues** | None | | |\n\n---\n\n### 10. zhang2023h2o — H2O\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\" | Same | YES |\n| Authors | Zhang, Zhenyu and others | Zhenyu Zhang, Ying Sheng, Tianyi Zhou, et al. | YES |\n| Year | 2023 | 2023 | YES |\n| Venue | NeurIPS 2023 | NeurIPS 2023 | YES |\n| arXiv ID | 2306.14048 | 2306.14048 | YES |\n| **Issues** | None | | |\n\n---\n\n### 11. xiao2024streamingllm — StreamingLLM\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"Efficient Streaming Language Models with Attention Sinks\" | Same | YES |\n| Authors | Xiao, Guangxuan and others | Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, Mike Lewis | YES |\n| Year | 2024 | 2024 | YES |\n| Venue | ICLR 2024 | ICLR 2024 | YES |\n| arXiv ID | 2309.17453 | 2309.17453 | YES |\n| **Issues** | None | | |\n\n---\n\n### 12. mees2022calvin — CALVIN\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\" | Same | YES |\n| Authors | Mees, Oier and others | Oier Mees, Lukas Hermann, Erick Rosete-Beas, Wolfram Burgard | YES |\n| Year | 2022 | 2022 | YES |\n| Venue | IEEE Robotics and Automation Letters (RA-L) | IEEE RA-L, vol. 7, no. 3, pp. 7327-7334 | YES |\n| arXiv ID | 2112.03227 | 2112.03227 | YES |\n| **Issues** | None | | |\n\n---\n\n### 13. chi2023diffusionpolicy — Diffusion Policy\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\" | Same | YES |\n| Authors | Chi, Cheng and others | Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, Shuran Song | YES |\n| Year | 2023 | 2023 | YES |\n| Venue | RSS 2023 | RSS 2023 (Robotics: Science and Systems) | YES |\n| arXiv ID | 2303.04137 | 2303.04137 | YES |\n| **Issues** | None | | |\n\n---\n\n### 14. zeng2023transformers_tsf — Are Transformers Effective for TSF?\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"Are Transformers Effective for Time Series Forecasting?\" | Same | YES |\n| Authors | Zeng, Ailing and others | Ailing Zeng, Muxi Chen, Lei Zhang, Qiang Xu | YES |\n| Year | 2023 | 2023 | YES |\n| Venue | AAAI 2023 | AAAI 2023 (vol. 37, no. 9, pp. 11121-11128) | YES |\n| arXiv ID | 2205.13504 | 2205.13504 | YES |\n| **Issues** | None | | |\n\n---\n\n### 15. bouthillier2024negative — Embracing Negative Results\n| Field | Bib Value | Verified Value | Match? |\n|-------|-----------|----------------|--------|\n| Exists | — | Yes | YES |\n| Title | \"Position: Embracing Negative Results in Machine Learning\" | Same | YES |\n| Authors | Bouthillier, Xavier and others | **Florian Karl, Lukas Malte Kemeter, Gabriel Dax, Paulina Sierak** | **NO** |\n| Year | 2024 | 2024 | YES |\n| Venue | ICML 2024 | ICML 2024 (PMLR 235:23256-23265) | YES |\n| arXiv ID | 2406.03980 | 2406.03980 | YES |\n| **Issues** | **WRONG FIRST AUTHOR.** The bib key `bouthillier2024negative` and author field listing \"Bouthillier, Xavier\" is incorrect. The actual first author is **Florian Karl**. Xavier Bouthillier does not appear in the author list of this paper. The correct authors are Karl, Kemeter, Dax, and Sierak. The bib key should be something like `karl2024negative` or `karl2024position`. This must be corrected. | | |\n\n---\n\n## Summary of Issues Found\n\n| # | Entry | Severity | Issue |\n|---|-------|----------|-------|\n| 2 | oquab2023dinov2 / oquab2024dinov2 | Minor | Duplicate bib entries. Key `oquab2023dinov2` is misleading (implies year 2023 but field says 2024). Remove one. |\n| 8 | zitkovich2023rt2 / brohan2023rt2 | Minor | Two bib entries for the same paper with different first-author orderings. Both are valid depending on source (CoRL proceedings vs arXiv). Remove duplicate; pick one consistently. |\n| **15** | **bouthillier2024negative** | **CRITICAL** | **Wrong author. First author is Florian Karl, not Xavier Bouthillier. Bib key and author field must be corrected.** |\n\nAll other 12 entries verified clean with correct titles, authors, years, venues, and arXiv IDs."
      }
    ],
    "totalDurationMs": 171276,
    "totalTokens": 43778,
    "totalToolUseCount": 28,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 39234,
      "output_tokens": 3751,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 792
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3751,
          "cache_read_input_tokens": 39234,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 792,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 28
    }
  }
}
```

</details>

---


### Assistant

_source line 403_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile all results and also check for some additional items:

1. Unused bib entries (entries in bib but not cited in main paper)
2. Missing bib entries (cited in tex but not in bib)
3. The `karl2024negative` reference in sections/introduction.tex - is it cited in the main paper?

Let me also check for the remaining entries that weren't covered by the agents:
- li2024tokenpacker
- wen2024tinyvla
- zhang2024fastervlm
- liu2024llava15
- chen2024internvl


- chen2024internvl25
- gao2024miniinternvl

These last two appear in the bib but aren't cited anywhere in the main paper files, though they might be referenced in draft sections not included in the build. Since they're not actually used, I don't need to verify them deeply. I should also double-check the `brohan2023rt2` versus `zitkovich2023rt2` situation - I need to confirm which one is actually cited in the introduction.

Looking at the main introduction.tex more carefully, I can see citations to black2024pi0, kim2024openvla, shukor2025smolvla, and zheng2025xvla in the vision connectors discussion, but neither brohan2023rt2 nor zitkovich2023rt2 appear to be cited in the main paper files at all - they're only in the bibliography.

Now I need to verify the other entries that weren't covered by the agents: li2024tokenpacker, wen2024tinyvla, zhang2024fastervlm, liu2024llava15, chen2024internvl, chen2024internvl25, and gao2024miniinternvl all appear to be unused as well. Let me systematically go through the main text to check citation accuracy for each reference that is actually cited.

I'm finding a critical issue with bouthillier2024negative - the first author should be Florian Karl, not Xavier Bouthillier, though this entry isn't cited in the main paper anyway.

There are several other problems: khaki2025sparsevila has a title error ("Decoupling" not "Decoupled"), shang2024prumerge is dated 2024 when it should be 2025, brohan2023rt2 has author ordering issues and duplicates zitkovich2023rt2, oquab2023dinov2 and oquab2024dinov2 are duplicates with a misleading key, ryoo2021tokenlearner has minor title variations between arXiv and NeurIPS versions, and yin2022avit shows "AdaViT" on arXiv versus the CVPR version.

For zheng2025xvla, the bib key says 2025 but the year field correctly shows 2026 for ICLR 2026, which is fine since the key is just cosmetic. Now I need to verify the citation contexts in the main paper to check if they're accurate.

Going through the introduction, the token pruning citations for vision transformers are correct, as are the VLA efficiency papers. The connector type citations also check out—π0 uses linear projections, OpenVLA uses MLP projectors, and SmolVLA uses pixel-shuffle folding. For zheng2025xvla, I need to verify the claim about learned encoders.

Now I'm verifying the related work section, checking that each citation correctly corresponds to its method name and that the descriptions of token pruning and pruning/merging approaches in vision transformers and VLMs are accurate. Continuing through the citation list, verifying the remaining papers on VLA optimization techniques like LightVLA, Compressor-VLA, and SpecPrune-VLA, along with related work on pruning effects and vision-language model architectures. Continuing to verify the citations for the method section, checking that flow matching, DINOv2, and the various vision-language architecture projectors are correctly attributed. Continuing to verify the remaining citations in the appendix section, checking that CogACT's pruning results are properly attributed to EfficientVLA's evaluation, and confirming the technical details for ToMe, BART, RoPE, and other supporting methods are accurately cited.

I'm also noticing there are quite a few bibliography entries that aren't actually referenced anywhere in the main paper—entries like RoboFlamingo, RT-1, RT-2, Octo, Flamingo, InternVL, and several others appear in the bibliography but don't have corresponding citations in the text.

Now I need to organize everything into a final checklist, separating the entries that are actually cited from those that are unused, and verify the citation contexts for the ones that are being used.

Looking at the verification results, π0 is correctly listed as an arXiv preprint, and SmolVLA is also properly marked as arXiv. I notice the DINOv2 entry has a year mismatch—the key says 2023 but the bib entry has 2024, though the citation in background.tex uses the 2023 key, so that's consistent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "2f0a2411-f3a1-41ab-aa14-2247bd51a6af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4xfR1M7FoXfsDGEMG4F6q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21172,
      "cache_read_input_tokens": 104396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21172
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 404_

All verification complete. Let me now compile the full checklist, including citation context checks.

---

## 引用核对清单

### A. 主论文中引用的条目（37条被引用，按出现顺序）

```
[✓] rao2021dynamicvit | Rao, Yongming et al. | "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification" | 2021 | NeurIPS 2021
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5, appendix — ViT token pruning代表工作 ✓

[✓] bolya2023tome | Bolya, Daniel et al. | "Token Merging: Your ViT But Faster" | 2023 | ICLR 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5, appendix — token merging方法 ✓

[✓] liang2022evit | Liang, Youwei et al. | "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" | 2022 | ICLR 2022
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5 — ViT token pruning ✓

[✓] cheng2026vlaiap | Cheng, Jintao et al. | "VLA-IAP: Training-Free Visual Token Pruning..." | 2026 | arXiv 2603.22991
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token pruning方法 ✓

[✓] xu2025vlacache | Xu, Siyu et al. | "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching" | 2025 | NeurIPS 2025
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token caching ✓

[✓] yang2025efficientvla | Yang, Yantai et al. | "EfficientVLA: Training-Free Acceleration and Compression for VLA Models" | 2025 | arXiv 2506.10100
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8, results — CogACT pruning结果来源 ✓

[✓] liu2025vlapruner | Liu, Ziyan et al. | "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning..." | 2025 | arXiv 2511.16449
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token pruning ✓

[✓] black2024pi0 | Black, Kevin et al. | "π0: A Vision-Language-Action Flow Model for General Robot Control" | 2024 | arXiv 2410.24164
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L16, method.tex, results — linear projection connector ✓

[✓] kim2024openvla | Kim, Moo Jin et al. | "OpenVLA: An Open-Source Vision-Language-Action Model" | 2024 | CoRL 2024
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L16, background, method, results — MLP projector connector ✓

[✓] shukor2025smolvla | Shukor, Mustafa et al. | "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics" | 2025 | arXiv 2506.01844
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction, background, method, results — pixel-shuffle connector ✓

[✓] zheng2025xvla | Zheng, Jinliang et al. | "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment VLA Model" | 2026 | ICLR 2026, arXiv 2510.10274
- 验证结果: 真实存在/作者正确/标题正确/年份正确(field=2026)/venue正确/arXiv ID正确
- 正文用法: introduction.tex L16, method, experiments, results — BART encoder connector ✓

[✓] chen2024fastv | Chen, Liang et al. | "An Image is Worth 1/2 Tokens After Layer 2..." | 2024 | ECCV 2024, arXiv 2403.06764
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token pruning ✓

[✗] shang2024prumerge | Shang, Yuzhang et al. | "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models" | 2024→2025 | ICCV 2025
- 验证结果: 真实存在/作者正确/标题正确/venue正确
- 问题: **年份错误**。Bib year=2025 正确匹配 ICCV 2025，但 bib key 暗示 2024。实际 booktitle 写的是 "IEEE/CVF International Conference on Computer Vision (ICCV)" year=2025，这是正确的。（复查：bib 文件中 year=2025，OK。bib key 中的 2024 仅是标识符不影响输出。）
- **修正**: 复查后 bib year field = 2025，venue = ICCV 2025，均正确。bib key "2024" 不影响输出。**改判为 ✓**。

[✓] zhang2025sparsevlm | Zhang, Yuan et al. | "SparseVLM: Visual Token Sparsification..." | 2025 | ICML 2025, arXiv 2410.04417
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token sparsification ✓

[✗] khaki2025sparsevila | Khaki, Samir et al. | "SparseVILA: Decoupled Visual Sparsity..." | 2025 | ICCV 2025, arXiv 2510.17777
- 验证结果: 真实存在/作者正确/年份正确/venue正确/arXiv ID正确
- 问题: **标题错误**。Bib 写 "Decoupled"，实际标题为 "Decoupling"（动名词形式）
- 正文用法: related_work.tex L8 — VLM token sparsification ✓

[✓] ye2025fitprune | Ye, Weihao et al. | "Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal LLMs" | 2025 | AAAI 2025, arXiv 2409.10197
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token pruning ✓

[✓] jiang2026lightvla | Jiang, Titong et al. | "The Better You Learn, The Smarter You Prune..." | 2026 | ICRA 2026, arXiv 2509.12594
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA differentiable token pruning ✓

[✓] gao2025compressorvla | Gao, Juntao et al. | "Compressor-VLA: Instruction-Guided Visual Token Compression..." | 2025 | arXiv 2511.18950
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA token compression ✓

[✓] wang2025specprunevla | Wang, Hanzhen et al. | "SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning" | 2025 | arXiv 2509.05614
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA pruning ✓

[✓] feng2026seewhatmatters | Feng, Yixu et al. | "See What Matters: Differentiable Grid Sample Pruning..." | 2026 | ICML 2026, arXiv 2605.11817
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA token pruning ✓

[✓] jabbour2025dontrun | Jabbour, Jason et al. | "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" | 2025 | arXiv 2510.08464
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L11 — concurrent work on VLA pruning failure ✓

[✓] liu2023llava | Liu, Haotian et al. | "Visual Instruction Tuning" | 2023 | NeurIPS 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — LLaVA MLP projector ✓

[✓] li2023blip2 | Li, Junnan et al. | "BLIP-2: Bootstrapping Language-Image Pre-Training..." | 2023 | ICML 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — cross-attention queries ✓

[✓] shi2016subpixel | Shi, Wenzhe et al. | "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel CNN" | 2016 | CVPR 2016
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — pixel shuffle origin ✓

[✓] zhai2023siglip | Zhai, Xiaohua et al. | "Sigmoid Loss for Language Image Pre-Training" | 2023 | ICCV 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background.tex — SmolVLA vision encoder ✓

[✓] yang2024qwen2 | Yang, An et al. | "Qwen2 Technical Report" | 2024 | arXiv 2407.10671
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: background.tex — Qwen2-0.5B LLM backbone ✓

[✓] lipman2023flow | Lipman, Yaron et al. | "Flow Matching for Generative Modeling" | 2023 | ICLR 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background.tex — flow matching action head ✓

[✓] oquab2023dinov2 | Oquab, Maxime et al. | "DINOv2: Learning Robust Visual Features without Supervision" | 2024 | TMLR
- 验证结果: 真实存在/作者正确/标题正确/year field=2024正确(TMLR 2024)/venue正确
- 问题（次要）: bib key 含 "2023" 但 year field = 2024。arXiv 发布于 2023.04，TMLR 发表于 2024.01。Key 不影响输出。
- 正文用法: background.tex — OpenVLA dual encoder ✓

[✓] black2025pi05 | Black, Kevin et al. | "π0.5: a Vision-Language-Action Model with Open-World Generalization" | 2025 | CoRL 2025, PMLR v305, pp.17-40, arXiv 2504.16054
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/volume正确/pages正确/arXiv ID正确
- 正文用法: method.tex, experiments.tex, results — linear connector model ✓

[✓] kim2025openoft | Kim, Moo Jin et al. | "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" | 2025 | arXiv 2502.19645
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: method.tex, results — OFT variant of OpenVLA ✓

[✓] lewis2020bart | Lewis, Mike et al. | "BART: Denoising Sequence-to-Sequence Pre-training..." | 2020 | ACL 2020
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: method.tex — X-VLA uses BART encoder ✓

[✓] liu2023libero | Liu, Bo et al. | "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" | 2023 | NeurIPS 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background, method, experiments, results — evaluation benchmark ✓

[✓] li2024cogact | Li, Qixiu et al. | "CogACT: A Foundational Vision-Language-Action Model..." | 2024 | arXiv 2411.19650
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: results — MLP projector corroboration from EfficientVLA ✓

[✓] shi2024crossget | Shi, Dachuan et al. | "CrossGET: Cross-Guided Ensemble of Tokens..." | 2024 | ICML 2024, arXiv 2305.17455
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L5 — ViT token pruning ✓

[✓] yin2022avit | Yin, Hongxu et al. | "A-ViT: Adaptive Tokens for Efficient Vision Transformer" | 2022 | CVPR 2022, arXiv 2112.07658
- 验证结果: 真实存在/作者正确/年份正确/venue正确/arXiv ID正确
- 问题（次要）: arXiv 标题为 "AdaViT"，CVPR 发表版改名 "A-ViT"。Bib 使用 CVPR 标题，正确。
- 正文用法: related_work.tex L5 — ViT adaptive tokens ✓

[✓] abnar2020quantifying | Abnar, Samira & Zuidema, Willem | "Quantifying Attention Flow in Transformers" | 2020 | ACL 2020, pp.4190-4197
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/pages正确
- 正文用法: appendix — attention rollout method ✓

[✓] su2024roformer | Su, Jianlin et al. | "RoFormer: Enhanced Transformer with Rotary Position Embedding" | 2024 | Neurocomputing v568 p127063
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/volume正确
- 正文用法: appendix — RoPE position encoding ✓
```

---

### B. 问题条目汇总

| # | 状态 | cite_key | 问题 | 严重度 |
|---|------|----------|------|--------|
| 1 | **✗** | `khaki2025sparsevila` | 标题 "Decoupled" 应为 "**Decoupling**" | **需修复** |

其余 36 条引用条目均验证通过。

---

### C. 未被主论文引用的 bib 条目（25条）

以下条目存在于 `references.bib` 但未在 main.tex 编译链中被 `\cite` 引用（可能来自早期草稿）：

| cite_key | 备注 |
|----------|------|
| `li2024roboflamingo` | 未引用 |
| `brohan2023rt2` | 未引用；与 `zitkovich2023rt2` 重复（同一论文，arXiv vs proceedings 作者顺序不同） |
| `brohan2023rt1` | 未引用 |
| `ghosh2024octo` | 未引用 |
| `alayrac2022flamingo` | 未引用 |
| `chen2024internvl` | 未引用 |
| `jaegle2021perceiver` | 未引用 |
| `li2024tokenpacker` | 未引用 |
| `wen2024tinyvla` | 未引用 |
| `ryoo2021tokenlearner` | 未引用 |
| `meng2022adavit` | 未引用 |
| `chen2023sparsevit` | 未引用 |
| `zhang2024fastervlm` | 未引用 |
| `liu2024llava15` | 未引用 |
| `chen2024internvl25` | 未引用 |
| `gao2024miniinternvl` | 未引用 |
| `zitkovich2023rt2` | 未引用；与 `brohan2023rt2` 重复 |
| `openxembodiment2024` | 未引用 |
| `zhang2023h2o` | 未引用 |
| `xiao2024streamingllm` | 未引用 |
| `mees2022calvin` | 未引用 |
| `chi2023diffusionpolicy` | 未引用 |
| `zeng2023transformers_tsf` | 未引用（仅在 sections/ 草稿中出现） |
| `bouthillier2024negative` | 未引用；**且作者错误**（实际第一作者为 Florian Karl，非 Xavier Bouthillier） |
| `oquab2024dinov2` | 未引用；与 `oquab2023dinov2` 重复 |

---

### D. 总结

**需修复（1条）：**
- `khaki2025sparsevila`：标题 "Decoupled" → "**Decoupling**"

**建议清理（不影响编译输出，但建议处理）：**
- 25 条未引用条目可从 bib 中移除以保持整洁
- `oquab2023dinov2` 和 `oquab2024dinov2` 是同一论文的重复条目
- `brohan2023rt2` 和 `zitkovich2023rt2` 是同一论文的重复条目（arXiv vs proceedings 作者顺序不同）
- `bouthillier2024negative` 的作者字段有误（但未被引用，不影响论文）

**全部 37 条被引用条目中**：36 条完全正确，1 条有标题拼写错误。所有引用在正文中的使用语境均准确，无张冠李戴的情况。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "uuid": "36daeda2-4e12-4548-bf8f-5033fc527fa3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4xfR1M7FoXfsDGEMG4F6q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21172,
      "cache_read_input_tokens": 104396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21172
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 405_

All verification complete. Let me now compile the full checklist, including citation context checks.

---

## 引用核对清单

### A. 主论文中引用的条目（37条被引用，按出现顺序）

```
[✓] rao2021dynamicvit | Rao, Yongming et al. | "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification" | 2021 | NeurIPS 2021
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5, appendix — ViT token pruning代表工作 ✓

[✓] bolya2023tome | Bolya, Daniel et al. | "Token Merging: Your ViT But Faster" | 2023 | ICLR 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5, appendix — token merging方法 ✓

[✓] liang2022evit | Liang, Youwei et al. | "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" | 2022 | ICLR 2022
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5 — ViT token pruning ✓

[✓] cheng2026vlaiap | Cheng, Jintao et al. | "VLA-IAP: Training-Free Visual Token Pruning..." | 2026 | arXiv 2603.22991
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token pruning方法 ✓

[✓] xu2025vlacache | Xu, Siyu et al. | "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching" | 2025 | NeurIPS 2025
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token caching ✓

[✓] yang2025efficientvla | Yang, Yantai et al. | "EfficientVLA: Training-Free Acceleration and Compression for VLA Models" | 2025 | arXiv 2506.10100
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8, results — CogACT pruning结果来源 ✓

[✓] liu2025vlapruner | Liu, Ziyan et al. | "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning..." | 2025 | arXiv 2511.16449
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token pruning ✓

[✓] black2024pi0 | Black, Kevin et al. | "π0: A Vision-Language-Action Flow Model for General Robot Control" | 2024 | arXiv 2410.24164
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L16, method.tex, results — linear projection connector ✓

[✓] kim2024openvla | Kim, Moo Jin et al. | "OpenVLA: An Open-Source Vision-Language-Action Model" | 2024 | CoRL 2024
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L16, background, method, results — MLP projector connector ✓

[✓] shukor2025smolvla | Shukor, Mustafa et al. | "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics" | 2025 | arXiv 2506.01844
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction, background, method, results — pixel-shuffle connector ✓

[✓] zheng2025xvla | Zheng, Jinliang et al. | "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment VLA Model" | 2026 | ICLR 2026, arXiv 2510.10274
- 验证结果: 真实存在/作者正确/标题正确/年份正确(field=2026)/venue正确/arXiv ID正确
- 正文用法: introduction.tex L16, method, experiments, results — BART encoder connector ✓

[✓] chen2024fastv | Chen, Liang et al. | "An Image is Worth 1/2 Tokens After Layer 2..." | 2024 | ECCV 2024, arXiv 2403.06764
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token pruning ✓

[✗] shang2024prumerge | Shang, Yuzhang et al. | "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models" | 2024→2025 | ICCV 2025
- 验证结果: 真实存在/作者正确/标题正确/venue正确
- 问题: **年份错误**。Bib year=2025 正确匹配 ICCV 2025，但 bib key 暗示 2024。实际 booktitle 写的是 "IEEE/CVF International Conference on Computer Vision (ICCV)" year=2025，这是正确的。（复查：bib 文件中 year=2025，OK。bib key 中的 2024 仅是标识符不影响输出。）
- **修正**: 复查后 bib year field = 2025，venue = ICCV 2025，均正确。bib key "2024" 不影响输出。**改判为 ✓**。

[✓] zhang2025sparsevlm | Zhang, Yuan et al. | "SparseVLM: Visual Token Sparsification..." | 2025 | ICML 2025, arXiv 2410.04417
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token sparsification ✓

[✗] khaki2025sparsevila | Khaki, Samir et al. | "SparseVILA: Decoupled Visual Sparsity..." | 2025 | ICCV 2025, arXiv 2510.17777
- 验证结果: 真实存在/作者正确/年份正确/venue正确/arXiv ID正确
- 问题: **标题错误**。Bib 写 "Decoupled"，实际标题为 "Decoupling"（动名词形式）
- 正文用法: related_work.tex L8 — VLM token sparsification ✓

[✓] ye2025fitprune | Ye, Weihao et al. | "Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal LLMs" | 2025 | AAAI 2025, arXiv 2409.10197
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token pruning ✓

[✓] jiang2026lightvla | Jiang, Titong et al. | "The Better You Learn, The Smarter You Prune..." | 2026 | ICRA 2026, arXiv 2509.12594
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA differentiable token pruning ✓

[✓] gao2025compressorvla | Gao, Juntao et al. | "Compressor-VLA: Instruction-Guided Visual Token Compression..." | 2025 | arXiv 2511.18950
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA token compression ✓

[✓] wang2025specprunevla | Wang, Hanzhen et al. | "SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning" | 2025 | arXiv 2509.05614
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA pruning ✓

[✓] feng2026seewhatmatters | Feng, Yixu et al. | "See What Matters: Differentiable Grid Sample Pruning..." | 2026 | ICML 2026, arXiv 2605.11817
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA token pruning ✓

[✓] jabbour2025dontrun | Jabbour, Jason et al. | "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" | 2025 | arXiv 2510.08464
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L11 — concurrent work on VLA pruning failure ✓

[✓] liu2023llava | Liu, Haotian et al. | "Visual Instruction Tuning" | 2023 | NeurIPS 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — LLaVA MLP projector ✓

[✓] li2023blip2 | Li, Junnan et al. | "BLIP-2: Bootstrapping Language-Image Pre-Training..." | 2023 | ICML 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — cross-attention queries ✓

[✓] shi2016subpixel | Shi, Wenzhe et al. | "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel CNN" | 2016 | CVPR 2016
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — pixel shuffle origin ✓

[✓] zhai2023siglip | Zhai, Xiaohua et al. | "Sigmoid Loss for Language Image Pre-Training" | 2023 | ICCV 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background.tex — SmolVLA vision encoder ✓

[✓] yang2024qwen2 | Yang, An et al. | "Qwen2 Technical Report" | 2024 | arXiv 2407.10671
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: background.tex — Qwen2-0.5B LLM backbone ✓

[✓] lipman2023flow | Lipman, Yaron et al. | "Flow Matching for Generative Modeling" | 2023 | ICLR 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background.tex — flow matching action head ✓

[✓] oquab2023dinov2 | Oquab, Maxime et al. | "DINOv2: Learning Robust Visual Features without Supervision" | 2024 | TMLR
- 验证结果: 真实存在/作者正确/标题正确/year field=2024正确(TMLR 2024)/venue正确
- 问题（次要）: bib key 含 "2023" 但 year field = 2024。arXiv 发布于 2023.04，TMLR 发表于 2024.01。Key 不影响输出。
- 正文用法: background.tex — OpenVLA dual encoder ✓

[✓] black2025pi05 | Black, Kevin et al. | "π0.5: a Vision-Language-Action Model with Open-World Generalization" | 2025 | CoRL 2025, PMLR v305, pp.17-40, arXiv 2504.16054
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/volume正确/pages正确/arXiv ID正确
- 正文用法: method.tex, experiments.tex, results — linear connector model ✓

[✓] kim2025openoft | Kim, Moo Jin et al. | "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" | 2025 | arXiv 2502.19645
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: method.tex, results — OFT variant of OpenVLA ✓

[✓] lewis2020bart | Lewis, Mike et al. | "BART: Denoising Sequence-to-Sequence Pre-training..." | 2020 | ACL 2020
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: method.tex — X-VLA uses BART encoder ✓

[✓] liu2023libero | Liu, Bo et al. | "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" | 2023 | NeurIPS 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background, method, experiments, results — evaluation benchmark ✓

[✓] li2024cogact | Li, Qixiu et al. | "CogACT: A Foundational Vision-Language-Action Model..." | 2024 | arXiv 2411.19650
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: results — MLP projector corroboration from EfficientVLA ✓

[✓] shi2024crossget | Shi, Dachuan et al. | "CrossGET: Cross-Guided Ensemble of Tokens..." | 2024 | ICML 2024, arXiv 2305.17455
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L5 — ViT token pruning ✓

[✓] yin2022avit | Yin, Hongxu et al. | "A-ViT: Adaptive Tokens for Efficient Vision Transformer" | 2022 | CVPR 2022, arXiv 2112.07658
- 验证结果: 真实存在/作者正确/年份正确/venue正确/arXiv ID正确
- 问题（次要）: arXiv 标题为 "AdaViT"，CVPR 发表版改名 "A-ViT"。Bib 使用 CVPR 标题，正确。
- 正文用法: related_work.tex L5 — ViT adaptive tokens ✓

[✓] abnar2020quantifying | Abnar, Samira & Zuidema, Willem | "Quantifying Attention Flow in Transformers" | 2020 | ACL 2020, pp.4190-4197
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/pages正确
- 正文用法: appendix — attention rollout method ✓

[✓] su2024roformer | Su, Jianlin et al. | "RoFormer: Enhanced Transformer with Rotary Position Embedding" | 2024 | Neurocomputing v568 p127063
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/volume正确
- 正文用法: appendix — RoPE position encoding ✓
```

---

### B. 问题条目汇总

| # | 状态 | cite_key | 问题 | 严重度 |
|---|------|----------|------|--------|
| 1 | **✗** | `khaki2025sparsevila` | 标题 "Decoupled" 应为 "**Decoupling**" | **需修复** |

其余 36 条引用条目均验证通过。

---

### C. 未被主论文引用的 bib 条目（25条）

以下条目存在于 `references.bib` 但未在 main.tex 编译链中被 `\cite` 引用（可能来自早期草稿）：

| cite_key | 备注 |
|----------|------|
| `li2024roboflamingo` | 未引用 |
| `brohan2023rt2` | 未引用；与 `zitkovich2023rt2` 重复（同一论文，arXiv vs proceedings 作者顺序不同） |
| `brohan2023rt1` | 未引用 |
| `ghosh2024octo` | 未引用 |
| `alayrac2022flamingo` | 未引用 |
| `chen2024internvl` | 未引用 |
| `jaegle2021perceiver` | 未引用 |
| `li2024tokenpacker` | 未引用 |
| `wen2024tinyvla` | 未引用 |
| `ryoo2021tokenlearner` | 未引用 |
| `meng2022adavit` | 未引用 |
| `chen2023sparsevit` | 未引用 |
| `zhang2024fastervlm` | 未引用 |
| `liu2024llava15` | 未引用 |
| `chen2024internvl25` | 未引用 |
| `gao2024miniinternvl` | 未引用 |
| `zitkovich2023rt2` | 未引用；与 `brohan2023rt2` 重复 |
| `openxembodiment2024` | 未引用 |
| `zhang2023h2o` | 未引用 |
| `xiao2024streamingllm` | 未引用 |
| `mees2022calvin` | 未引用 |
| `chi2023diffusionpolicy` | 未引用 |
| `zeng2023transformers_tsf` | 未引用（仅在 sections/ 草稿中出现） |
| `bouthillier2024negative` | 未引用；**且作者错误**（实际第一作者为 Florian Karl，非 Xavier Bouthillier） |
| `oquab2024dinov2` | 未引用；与 `oquab2023dinov2` 重复 |

---

### D. 总结

**需修复（1条）：**
- `khaki2025sparsevila`：标题 "Decoupled" → "**Decoupling**"

**建议清理（不影响编译输出，但建议处理）：**
- 25 条未引用条目可从 bib 中移除以保持整洁
- `oquab2023dinov2` 和 `oquab2024dinov2` 是同一论文的重复条目
- `brohan2023rt2` 和 `zitkovich2023rt2` 是同一论文的重复条目（arXiv vs proceedings 作者顺序不同）
- `bouthillier2024negative` 的作者字段有误（但未被引用，不影响论文）

**全部 37 条被引用条目中**：36 条完全正确，1 条有标题拼写错误。所有引用在正文中的使用语境均准确，无张冠李戴的情况。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 490579,
  "duration_api_ms": 1449655,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "d1c43d49-176c-4cc5-b7a0-739614d052fe",
  "total_cost_usd": 5.799549999999997,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 136582,
    "cache_read_input_tokens": 394665,
    "output_tokens": 19498,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 136582,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 9440,
        "cache_read_input_tokens": 104396,
        "cache_creation_input_tokens": 21172,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 21172
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1093983,
      "outputTokens": 39819,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 103,
      "costUSD": 2.3230779999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8849,
      "outputTokens": 43129,
      "cacheReadInputTokens": 1234129,
      "cacheCreationInputTokens": 277910,
      "webSearchRequests": 0,
      "costUSD": 3.4764720000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "11e76517-56a7-4626-b254-0f2a5b6495b4"
}
```

</details>

---
