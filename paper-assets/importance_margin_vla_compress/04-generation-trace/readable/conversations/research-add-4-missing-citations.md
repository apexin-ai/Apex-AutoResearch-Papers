# research add 4 missing citations

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_research_add_4_missing_citations_20260519T062752.jsonl`
- **Structured JSON:** [`40792b33441360ec0dde.json`](../../sessions/40/40792b33441360ec0dde.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-19T06:28:51.091337+00:00_

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
  "session": "worker_research_add_4_missing_citations_20260519T062752",
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

_source line 2 · 2026-05-19T06:28:51.091663+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T06:28:51.091853+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CogACT robot manipulation arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CogACT robot manipulation arxiv 2024"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T06:28:51.091984+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA-OFT fine-tuning arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA-OFT fine-tuning arxiv 2024"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T06:28:51.092106+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TokenPacker visual token compression VLM arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TokenPacker visual token compression VLM arxiv"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T06:28:51.092270+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TinyVLA small vision language action model arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TinyVLA small vision language action model arxiv"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T06:28:51.092426+00:00_

Web search results for query: "TokenPacker visual token compression VLM arxiv"

Links: [{"title":"A Survey on Visual Token Compression for Efficient Vision-Language Models","url":"https://www.researchgate.net/publication/398219411_A_Survey_on_Visual_Token_Compression_for_Efficient_Vision-Language_Models"},{"title":"Balancing Saliency and Coverage: Semantic Prominence-Aware Budgeting for Visual Token Compression in VLMs","url":"https://arxiv.org/pdf/2603.14892"},{"title":"Towards Lossless Ultimate Vision Token Compression for VLMs","url":"https://arxiv.org/pdf/2512.09010"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters","url":"https://arxiv.org/html/2411.03312"}]

Based on the search results, I found information about TokenPacker:

TokenPacker is an efficient visual projector for multimodal LLM. In multimodal large language models (MLLMs), the visual projector is a crucial component that connects the visual encoder with the large language model (LLM). Most current MLLMs adopt a simple multi-layer perceptron (MLP) to preserve visual contexts via direct transformation, however, this approach tends to generate redundant visual tokens, particularly when processing high-resolution images, ultimately reducing the efficiency of MLLMs.

TokenPacker was published in IJCV'25 (International Journal of Computer Vision 2025), and has been compared with other visual token compression methods for VLMs. TokenPacker is compared to other token compression methods including LLaVA-PruMerge, Matryoshka Multimodal Models, and Matry
…[truncated 160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T06:28:51.092600+00:00_

Web search results for query: "CogACT robot manipulation arxiv 2024"

Links: [{"title":"arXiv:2411.19650v1 [cs.RO] 29 Nov 2024","url":"https://cogact.github.io/CogACT_paper.pdf"},{"title":"[PDF] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CogACT:-A-Foundational-Vision-Language-Action-Model-Li-Liang/54caf5927a6d656bb84d2a16e16fa2b0c5d6f522"},{"title":"[2411.19650v1] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650v1"},{"title":"[2411.19650] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650"},{"title":"(PDF) CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://www.researchgate.net/publication/386335138_CogACT_A_Foundational_Vision-Language-Action_Model_for_Synergizing_Cognition_and_Action_in_Robotic_Manipulation"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/html/2411.19650v1"},{"title":"Dexbotic: Open-Source Vision-Language-Action Toolbox","url":"https://arxiv.org/html/2510.23511v1"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241119650L/abstract"},{"title":"GitHub - microsoft/CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://github.com/microsoft/CogACT"}]

I found comprehensive information about CogACT. Here are the key findings:

## CogACT Overview

CogACT is a new advanced Vision-Language-Action (VLA) architecture derived from VLM that prop
…[truncated 1298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T06:28:51.092783+00:00_

Web search results for query: "OpenVLA-OFT fine-tuning arxiv 2024"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/html/2603.16044v1"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"}]

Based on the search results, here's what I found about OpenVLA-OFT fine-tuning:

## Overview

OpenVLA-OFT is an Optimized Fine-Tuning recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to improve inference efficiency, policy performance, and flexibility in the model's input-output specifications.

## Performance Results

OpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×.

In real-world evaluations, the fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and out
…[truncated 618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T06:28:51.092956+00:00_

Web search results for query: "TinyVLA small vision language action model arxiv"

Links: [{"title":"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models","url":"https://openreview.net/pdf/9ac0b98a230a3ae07dbc5ece257b8f7484e528eb.pdf"},{"title":"(PDF) TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://www.researchgate.net/publication/384155059_TinyVLA_Towards_Fast_Data-Efficient_Vision-Language-Action_Models_for_Robotic_Manipulation"},{"title":"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2409.12514v5"},{"title":"(PDF) TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (2024) | Junjie Wen | 2 Citations","url":"https://scispace.com/papers/tinyvla-towards-fast-data-efficient-vision-language-action-6z5925cxwsnc"},{"title":"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/pdf/2409.12514"},{"title":"[2409.12514] TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/abs/2409.12514"},{"title":"[2409.12514v5] TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/abs/2409.12514v5"},{"title":"Rethinking the Practicality of Vision-language-action Model:","url":"https://arxiv.org/pdf/2602.22663"},{"title":"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tinyvla-towards-fast-data-efficient-vision-language"}]

Based on the search results, here's what I found about TinyVLA:

## Overview

TinyVLA is a compact vision-language-action model designed for fast inference. It addresses two key factors in existing VLA models that contribute to high inference latency: (1) they are built o
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T06:28:51.093123+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.19650",
  "prompt": "Extract the full title, all author names, and the arxiv submission date/year for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2411.19650",
    "prompt": "Extract the full title, all author names, and the arxiv submission date/year for this paper."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T06:28:51.093316+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.19645",
  "prompt": "Extract the full title, all author names, and the arxiv submission date/year for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2502.19645",
    "prompt": "Extract the full title, all author names, and the arxiv submission date/year for this paper."
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T06:28:51.093452+00:00_

# CogACT Paper Information

**Full Title:** "CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation"

**Authors:** Qixiu Li, Yaobo Liang, Zeyu Wang, Lin Luo, Xi Chen, Mozheng Liao, Fangyun Wei, Yu Deng, Sicheng Xu, Yizhong Zhang, Xiaofan Wang, Bei Liu, Jianlong Fu, Jianmin Bao, Dong Chen, Yuanchun Shi, Jiaolong Yang, and Baining Guo

**Submission Date:** November 29, 2024

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T06:28:51.093573+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2409.12514",
  "prompt": "Extract the full title, all author names, and the arxiv submission date/year for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2409.12514",
    "prompt": "Extract the full title, all author names, and the arxiv submission date/year for this paper."
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T06:28:51.093689+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TokenPacker efficient visual projector multimodal LLM arxiv paper ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TokenPacker efficient visual projector multimodal LLM arxiv paper ID"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T06:28:51.093810+00:00_

# Paper Information

**Full Title:** "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"

**Authors:** Moo Jin Kim, Chelsea Finn, Percy Liang

**ArXiv Submission Date:** February 27, 2025

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T06:28:51.093931+00:00_

# TinyVLA Paper Details

**Full Title:** "TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation"

**Authors:**
Junjie Wen, Yichen Zhu, Jinming Li, Minjie Zhu, Kun Wu, Zhiyuan Xu, Ning Liu, Ran Cheng, Chaomin Shen, Yaxin Peng, Feifei Feng, and Jian Tang

**Submission Date:** September 19, 2024

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T06:28:51.094081+00:00_

Web search results for query: "TokenPacker efficient visual projector multimodal LLM arxiv paper ID"

Links: [{"title":"GitHub - CircleRadon/TokenPacker: The code for \"TokenPacker: Efficient Visual Projector for Multimodal LLM\", IJCV2025 · GitHub","url":"https://github.com/CircleRadon/TokenPacker"},{"title":"Paper page - TokenPacker: Efficient Visual Projector for Multimodal LLM","url":"https://huggingface.co/papers/2407.02392"},{"title":"[2407.02392] TokenPacker: Efficient Visual Projector for Multimodal LLM","url":"https://arxiv.org/abs/2407.02392"},{"title":"TokenPacker: Efficient Visual Projector for Multimodal LLM | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tokenpacker-efficient-visual-projector-multimodal-llm"},{"title":"[2407.02392] TokenPacker: Efficient Visual Projector for Multimodal LLM","url":"https://ar5iv.labs.arxiv.org/html/2407.02392"},{"title":"TokenPacker: Efficient Visual Projector for Multimodal LLM","url":"https://arxiv.org/pdf/2407.02392"},{"title":"TokenPacker: Efficient Visual Projector for Multimodal LLM | International Journal of Computer Vision | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11263-025-02491-7"},{"title":"TokenPacker: Efficient Visual Projector for Multimodal LLM - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240702392L/abstract"},{"title":"TokenPacker: Efficient Visual Projector for Multimodal LLM","url":"https://arxiv.org/html/2407.02392v1"}]

Based on the search results, I found the information about the TokenPacker paper:

The arXiv paper ID for "TokenPacker: Efficient Visual Projector for Multimodal LLM" is 2407.02392.

TokenPacker is a novel visual projector which adopts a coarse-to-fine scheme to inject enriched characteristics to generate condensed visual tokens. Using TokenPacker, visual tokens can be compressed by 75%∼89%, while achieving comparable or even better performance across diverse benchmarks with significantly higher efficiency.


REMIND
…[truncated 94 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T06:28:51.094261+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.02392",
  "prompt": "Extract the full title, all author names, and the arxiv submission date/year for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2407.02392",
    "prompt": "Extract the full title, all author names, and the arxiv submission date/year for this paper."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T06:28:51.094383+00:00_

# TokenPacker Paper Details

**Full Title:** "TokenPacker: Efficient Visual Projector for Multimodal LLM"

**Authors:**
1. Wentong Li
2. Yuqian Yuan
3. Jian Liu
4. Dongqi Tang
5. Song Wang
6. Jie Qin
7. Jianke Zhu
8. Lei Zhang

**Submission Date:** July 2, 2024 (initial submission in 2024)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T06:28:51.094518+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T06:28:51.094648+00:00_

__pycache__
_lerobot_compat.py
_project
acis_overhead.json
action_divergence_closedloop.json
action_divergence_curve.pdf
action_divergence_curve.png
action_divergence_data.json
action_divergence_summary.pdf
analyze_action_divergence.py
analyze_action_divergence_v2.py
architecture_report.md
attention_analysis.json
attention_data.npz
attention_distribution.pdf
attention_distribution.png
attention_heatmap.pdf
attention_heatmap.png
attention_metadata.json
attention_per_task.pdf
attention_per_task.png
checkpoint_integrity_report.md
configs
corl_template
degradation_curve.pdf
diagnosis_fullft_batch64_v2_crash.md
dream_reports
eval_formal_bound.py
eval_imm_v7_final.json
eval_pi05_baseline.json
eval_random_prune_baseline
eval_results
eval_sim.py
eval_success_rate_libero.py
eval_token_importance.py
evaluate.py
experiment_summary.csv
experiment_summary.json
geometric_prior_pruning.py
grids_positioning_for_related_work.txt
imm
imm_two_stage_v9
inference_latency_comparison
inference_latency_comparison.json
manifest.yaml
mvp_imm_anchor_v8
mvp_imm_v8b_twostage
new_references_8papers.bib
openvla_attention_entropy_real.json
openvla_k03_partial_results.json
patch_eval_temp.py
patch_evaluate.py
patch_twostage.py
plan_009_token_importance
plan_011_acis_overhead
research_lora_mode_collapse_fix.md
review_issues.yaml
review_reports
run_mvp.sh
run_v8_1_final_eval.sh
run_v8b_final_eval.sh
smolvla_attention_entropy_perlayer_DEPRECATED_wrong_tasks.json
smolvla_entropy_perlayer
test_geometric_pruning.py
train.py
train_smart_compress_m128_resume
v8_checkpoint_trajectory
worker_output_baseline_control_crash.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T06:28:51.094777+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/missing_citations_4papers.bib",
  "content": "@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/missing_citations_4papers.bib",
    "content": "@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T06:28:51.094915+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/missing_citations_4papers.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_add_4_missing_citations_20260519T062752",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T06:28:51.095070+00:00_

4 篇论文的 BibTeX 条目已写入 `artifacts/missing_citations_4papers.bib`，所有 arXiv ID 均已通过页面验证：

| 论文 | arXiv ID | 年份 |
|------|----------|------|
| CogACT | 2411.19650 | 2024 |
| OpenVLA-OFT | 2502.19645 | 2025 |
| TokenPacker | 2407.02392 | 2024 |
| TinyVLA | 2409.12514 | 2024 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_add_4_missing_citations_20260519T062752"
}
```

</details>

---
