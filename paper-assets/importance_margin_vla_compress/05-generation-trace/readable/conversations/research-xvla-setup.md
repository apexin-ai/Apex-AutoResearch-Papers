# research xvla setup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 32
- **Original source:** `logs/chats/worker_research_xvla-setup_20260520T033718.jsonl`
- **Structured JSON:** [`150247072a60ff71b5a1.json`](../../sessions/15/150247072a60ff71b5a1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

65 recorded events

### Tool call

_source line 1 · 2026-05-20T03:46:12.567969+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T03:46:12.568370+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T03:46:12.568544+00:00_

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
  "session": "worker_research_xvla-setup_20260520T033718",
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

_source line 4 · 2026-05-20T03:46:12.568673+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T03:46:12.568794+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T03:46:12.569198+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"content\": \"# VLA 模型全面调研报告\\n\\n**调研日期**: 2026-05-20\\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\\n\\n---\\n\\n## 已有实验数据\\n\\n| 模型 | Connector | 压缩行为 |\\n|------|-----------|----------|\\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\\n| RoboFlamingo | Perceiver Resampler | 尝试失败（gripper loss 无法训练） |\\n\\n---\\n\\n## 完整模型调研表\\n\\n### 1. Octo (UC Berkeley, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | 27M (Small) / 93M (Base) |\\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\\n\\n### 2. CogACT (Microsoft/Tsinghua, 2024)\\n\\n| 字段 | 信息 |\\n|------|------|\\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\\n| 论文 LIBERO 结果 | 无 |\\n| 备
…[truncated 13825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T03:46:12.569428+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "ideas.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "ideas.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T03:46:12.569578+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'importance_margin_vla_compress'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T03:46:12.569705+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "decisions.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "decisions.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T03:46:12.570013+00:00_

Error: result (74,170 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/20d662e5-5088-44bd-947c-e359a0e484fb/tool-results/mcp-agent-ml-research-read_project_file-1779248259897.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/20d662e5-5088-44bd-947c-e359a0e484fb/tool-results/mcp-agent-ml-research-read_project_file-1779248259897.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/20d662e5-5088-44bd-947c-e359a0e484fb/tool-results/mcp-agent-ml-research-read_project_file-1779248259897.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T03:46:12.570196+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "X-VLA robot vision language action model 0.9B linear projection LIBERO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "X-VLA robot vision language action model 0.9B linear projection LIBERO"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T03:46:12.570328+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"X-VLA\" VLA model GitHub 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"X-VLA\" VLA model GitHub 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T03:46:12.570488+00:00_

Web search results for query: ""X-VLA" VLA model GitHub 2025 2026"

Links: [{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"},{"title":"AutoVLA","url":"https://autovla.github.io/"},{"title":"X-VLA","url":"https://thu-air-dream.github.io/X-VLA/"},{"title":"GitHub - yueen-ma/Awesome-VLA · GitHub","url":"https://github.com/yueen-ma/awesome-vla"}]

Based on the search results, here's what I found about X-VLA:

## X-VLA Overview

X-VLA has been accepted to ICLR 2026, and won 1st Place (Champion) at the AgiBot World Challenge, held at IROS 2025.

## What is X-VLA?

X-VLA is a Vision-Language-Action (VLA) model that introduces a s
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T03:46:12.570668+00:00_

Web search results for query: "X-VLA robot vision language action model 0.9B linear projection LIBERO"

Links: [{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model [Quick Review]","url":"https://liner.com/review/xvla-softprompted-transformer-as-scalable-crossembodiment-visionlanguageaction-model"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/html/2510.10274v1"},{"title":"(PDF) X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://www.researchgate.net/publication/396462440_X-VLA_Soft-Prompted_Transformer_as_Scalable_Cross-Embodiment_Vision-Language-Action_Model"},{"title":"X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task · Hugging Face","url":"https://huggingface.co/docs/lerobot/xvla"},{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.19233"},{"title":"dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought","url":"https://arxiv.org/pdf/2509.25681"}]

Based on the search results, here's what I found about the X-VLA robot vision language action model:

## Overview
X-VLA-0.9B achieves state-of-the-art generalization across six simulation platforms and three real-world robots, surpassing prior VLA approaches in dexterity, adaptability, and efficiency.

## Architecture and Training
The X-VLA 0.9B parameter model was trained with a carefully designed data processing and learning recipe, with the training pipeline pretrained on 290K episodes from Droid, Robomind, and Agibot, spanning seven platforms across five types of robotic arms. By leveraging so
…[truncated 795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T03:46:12.570859+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "X-VLA architecture Florence vision encoder linear projection vision tokens number 2toinf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "X-VLA architecture Florence vision encoder linear projection vision tokens number 2toinf"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T03:46:12.570993+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "X-VLA 2toinf GitHub code structure model architecture Florence encoder connector",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "X-VLA 2toinf GitHub code structure model architecture Florence encoder connector",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T03:46:12.571249+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "X-VLA huggingface model weights 2toINF checkpoint download",
  "allowed_domains": "['huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "X-VLA huggingface model weights 2toINF checkpoint download",
    "allowed_domains": "['huggingface.co']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T03:46:12.571485+00:00_

Web search results for query: "X-VLA architecture Florence vision encoder linear projection vision tokens number 2toinf"

Links: [{"title":"Florence-VL: Enhancing Vision-Language Models with Generative Vision Encoder and Depth-Breadth Fusion","url":"https://arxiv.org/html/2412.04424v1"},{"title":"(PDF) Florence-VL: Enhancing Vision-Language Models with Generative Vision Encoder and Depth-Breadth Fusion","url":"https://www.researchgate.net/publication/386502844_Florence-VL_Enhancing_Vision-Language_Models_with_Generative_Vision_Encoder_and_Depth-Breadth_Fusion"},{"title":"Efficient VLA Executor","url":"https://www.emergentmind.com/topics/vision-language-action-vla-executor"},{"title":"[Literature Review] Florence-VL: Enhancing Vision-Language Models with Generative Vision Encoder and Depth-Breadth Fusion","url":"https://www.themoonlight.io/en/review/florence-vl-enhancing-vision-language-models-with-generative-vision-encoder-and-depth-breadth-fusion"},{"title":"Florence-VL: Enhancing Vision-Language Models with Generative Vision","url":"https://arxiv.org/pdf/2412.04424"},{"title":"Papers Explained 214: Florence-2. While existing large vision models… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-214-florence-2-c4e17246d14b"},{"title":"Florence-VL: Enhancing Vision-Language Models with Generative Vision Encoder and Depth-Breadth Fusion","url":"https://jiuhaichen.github.io/florence-vl.github.io/"}]

I found search results related to Florence vision models and vision-language architectures, but the results primarily cover Florence-VL rather than "X-VLA" specifically. The search results discuss:

- Vision token embeddings produced by applying a linear projection and LayerNorm layer to visual embedding from DaViT
- Vision embeddings obtained by applying a linear projection and LayerNorm layer for dimensionality alignment

However, the search results don't contain specific information about "X-VLA architecture" or the "2toinf" parameter yo
…[truncated 441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T03:46:12.571662+00:00_

Web search results for query: "X-VLA huggingface model weights 2toINF checkpoint download"

Links: [{"title":"X-VLA - a 2toINF Collection","url":"https://huggingface.co/collections/2toINF/x-vla"},{"title":"2toINF/X-VLA-Pt · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-Pt"},{"title":"2toINF/X-VLA-SoftFold · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-SoftFold"},{"title":"Loading models · Hugging Face","url":"https://huggingface.co/docs/transformers/en/models"},{"title":"lerobot/xvla-base · Hugging Face","url":"https://huggingface.co/lerobot/xvla-base"},{"title":"Models · Hugging Face","url":"https://huggingface.co/docs/transformers/main_classes/model"},{"title":"2toINF/X-VLA-WidowX · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-WidowX"},{"title":"X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task","url":"https://huggingface.co/docs/lerobot/en/xvla"},{"title":"2toINF/X-VLA-RoboTwin2 · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-RoboTwin2"},{"title":"Model formats · Hugging Face","url":"https://huggingface.co/docs/diffusers/en/using-diffusers/other-formats"}]

Based on the search results, I found information about X-VLA models from the 2toINF organization on Hugging Face:

## X-VLA Model Checkpoints from 2toINF

The 2toINF collection on Hugging Face contains X-VLA models, which are robotics models with 0.9B parameters.

### Available Checkpoints

Several X-VLA model checkpoints are available for download:

1. **X-VLA-WidowX** - Can be loaded using `AutoModel.from_pretrained("2toINF/X-VLA-WidowX", trust_remote_code=True)`

2. **X-VLA-Pt** - Available at `https://huggingface.co/2toINF/X-VLA-Pt`

3. **X-VLA-SoftFold** - Available at `https://huggingface.co/2toINF/X-VLA-SoftFold`

4. **X-VLA-RoboTwin2** - Available at `https://huggingface.co/2toINF/X-VLA-RoboTwin2`

### Model Description

X-VLA is described as a "Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model" 
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T03:46:12.571842+00:00_

Web search results for query: "X-VLA 2toinf GitHub code structure model architecture Florence encoder connector"

Links: [{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"},{"title":"X-VLA/models/modeling_xvla.py at main · 2toinf/X-VLA","url":"https://github.com/2toinf/X-VLA/blob/main/models/modeling_xvla.py"},{"title":"GitHub - anyantudre/Florence-2-Vision-Language-Model: Florence-2 is a novel vision foundation model with a unified, prompt-based representation for a variety of computer vision and vision-language tasks. · GitHub","url":"https://github.com/anyantudre/Florence-2-Vision-Language-Model"},{"title":"Florence-VL: Enhancing Vision-Language Models with Generative Vision   Encoder and Depth-Breadth Fusion","url":"https://arxiv.org/pdf/2412.04424"},{"title":"GitHub - Rm1n90/Florence2Onnx: ONNX deploys for Florence 2 visual multimodal · GitHub","url":"https://github.com/Rm1n90/Florence2Onnx"},{"title":"X-VLA/evaluation/calvin/README.md at main · 2toinf/X-VLA","url":"https://github.com/2toinf/X-VLA/blob/main/evaluation/calvin/README.md"},{"title":"GitHub - intuitive-robots/flower_vla_calvin: [CoRL 25] Code for FLOWER VLA for finetuning FLOWER on CALVIN and all LIBERO environments · GitHub","url":"https://github.com/intuitive-robots/flower_vla_calvin"}]

Based on the search results, here's information about the X-VLA GitHub project by 2toinf:

## Code Structure and Model Architecture

All models share a consistent architecture: configuration_xvla.py, modeling_xvla.py, and unified tokenizer (tokenizer.json). X-VLA adopts a Server–Client architecture to separate the model environment from simulation or robot-specific dependencies.

## Core Model Design

X-VLA introduces a soft prompt mechanism — embodiment-specific learnable embeddings that guide a unified Transformer backbone toward effective multi-domai
…[truncated 920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T03:46:12.572018+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com/2toinf/X-VLA modeling_xvla.py Florence2 linear projection vision tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com/2toinf/X-VLA modeling_xvla.py Florence2 linear projection vision tokens"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T03:46:12.572159+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com/2toinf/X-VLA LIBERO evaluation fine-tune soft prompt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com/2toinf/X-VLA LIBERO evaluation fine-tune soft prompt"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T03:46:12.572282+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "X-VLA arxiv 2510.10274 architecture Florence-Large DaViT vision tokens 577"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "X-VLA arxiv 2510.10274 architecture Florence-Large DaViT vision tokens 577"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T03:46:12.572432+00:00_

Web search results for query: "site:github.com/2toinf/X-VLA modeling_xvla.py Florence2 linear projection vision tokens"

Links: [{"title":"X-VLA/models/modeling_xvla.py at main · 2toinf/X-VLA","url":"https://github.com/2toinf/X-VLA/blob/main/models/modeling_xvla.py"},{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"},{"title":"transformers/src/transformers/models/florence2/modeling_florence2.py at main · huggingface/transformers","url":"https://github.com/huggingface/transformers/blob/main/src/transformers/models/florence2/modeling_florence2.py"},{"title":"Florence-2: Open Source Vision Foundation Model — OpenVINO™ documentation","url":"https://docs.openvino.ai/2024/notebooks/florence2-with-output.html"},{"title":"XVLA Model | 2toinf/X-VLA | DeepWiki","url":"https://deepwiki.com/2toinf/X-VLA/2.1-xvla-model"},{"title":"Florence-VL: Enhancing Vision-Language Models with Generative Vision   Encoder and Depth-Breadth Fusion","url":"https://arxiv.org/pdf/2412.04424"},{"title":"2toINF/X-VLA-Pt · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-Pt"},{"title":"lerobot/xvla-google-robot · Hugging Face","url":"https://huggingface.co/lerobot/xvla-google-robot"},{"title":"2toINF/X-VLA-WidowX · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-WidowX"}]

I found the search results for your query. The search successfully located the X-VLA repository on GitHub, specifically the `modeling_xvla.py` file.

The file is part of the official implementation of "Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model". The code includes a validation that checks that "Florence2 config must provide `projection_dim` for multimodal fusion."

All X-VLA models share the same architecture defined in configuration_xvla.py and modeling_xvla.py. The repository demonstrates how Florence2's linear 
…[truncated 322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T03:46:12.572602+00:00_

Web search results for query: "site:github.com/2toinf/X-VLA LIBERO evaluation fine-tune soft prompt"

Links: [{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"GitHub - THU-AIR-DREAM/X-VLA.: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://github.com/THU-AIR-DREAM/X-VLA."},{"title":"X-VLA","url":"https://thu-air-dream.github.io/X-VLA/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Systems and methods for ensembling soft prompts in few-shot fine-tuning of language models","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12524613"},{"title":"X-VLA/evaluation/calvin/README.md at main · 2toinf/X-VLA","url":"https://github.com/2toinf/X-VLA/blob/main/evaluation/calvin/README.md"}]

Based on the search results, I found information about the X-VLA project on GitHub:

X-VLA-Libero is a model fine-tuned on the LIBERO benchmark running on a Franka robot, achieving 98.1% on LIBERO Eval.

The X-VLA repository contains several key components: all models share a consistent architecture including configuration_xvla.py, modeling_xvla.py, and unified tokenizer (tokenizer.json).

Regarding the soft prompt approach, X-VLA is a flow-matching-based VLA architecture that relies exclusively on soft-prompted standard Transformer encoders, enjoying both scalability and simplicity. Additionally, the model supports Parameter efficient finetuning (PEFT) techniques for fast adaptation.

The repository includes evaluation guidance for multiple benchmarks, and to evaluate across different simulations, users need to set up the
…[truncated 187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T03:46:12.572774+00:00_

Web search results for query: "X-VLA arxiv 2510.10274 architecture Florence-Large DaViT vision tokens 577"

Links: [{"title":"[2510.10274] X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/abs/2510.10274"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/html/2510.10274v1"},{"title":"X-VLA","url":"https://thu-air-dream.github.io/X-VLA/"},{"title":"Paper page - X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://huggingface.co/papers/2510.10274"},{"title":"2025-10-14 X-VLA: Soft-Prompted Transformer as Scalable","url":"https://arxiv.org/pdf/2510.10274"},{"title":"[2311.06242] Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks","url":"https://ar5iv.labs.arxiv.org/html/2311.06242"},{"title":"2toINF/X-VLA-Pt · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-Pt"},{"title":"2toINF/X-VLA-SoftFold · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-SoftFold"},{"title":"[2204.03645] DaViT: Dual Attention Vision Transformers","url":"https://arxiv.org/abs/2204.03645"}]

Based on the search results, here's what I found about the X-VLA architecture (arxiv 2510.10274):

## X-VLA Architecture Overview

X-VLA is a flow-matching-based VLA architecture that relies exclusively on soft-prompted standard Transformer encoders.

## Vision Encoder Components

The architecture adopts Florence-Large as the vision-language encoder and employs a standard Transformer backbone with 24 layers and a hidden size of 1024 for action generation.

A pretrained VLM encoder (Florence-Large) is used for the main vision-language stream (fixed-view and instruction), while auxiliary views such as wrist-views are processed with a shared vision backbone.

## Core Approach

The model proposes a novel Soft Prompt approach with minimally added parameters, by infusing prompt l
…[truncated 590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T03:46:12.572949+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T03:46:12.573070+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T03:46:12.573226+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2510.10274v1",
  "prompt": "Extract the detailed architecture of X-VLA:\n1. Vision encoder: what model exactly? (Florence-Large / DaViT / SigLIP?) How many vision tokens does it produce? What resolution?\n2. Connector/projection: Is it a single linear layer? What are the input and output dimensions? Is there LayerNorm?\n3. LLM backbone: What transformer? How many layers, hidden dim?\n4. Soft prompts: How are they injected? Before or after vision tokens?\n5. Action head: Flow matching details - how many action tokens? Chunking?\n6. Total parameter count breakdown (vision encoder, connector, LLM, action head)\n7. LIBERO training details: which checkpoint to use, how to fine-tune, what data format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2510.10274v1",
    "prompt": "Extract the detailed architecture of X-VLA:\n1. Vision encoder: what model exactly? (Florence-Large / DaViT / SigLIP?) How many vision tokens does it produce? What resolution?\n2. Connector/projection: Is it a single linear layer? What are the input and output dimensions? Is there LayerNorm?\n3. LLM backbone: What transformer? How many layers, hidden dim?\n4. Soft prompts: How are they injected? Before or after vision tokens?\n5. Action head: Flow matching details - how many action tokens? Chunking?\n6. Total parameter count breakdown (vision encoder, connector, LLM, action head)\n7. LIBERO training details: which checkpoint to use, how to fine-tune, what data format"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T03:46:12.573392+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://deepwiki.com/2toinf/X-VLA/2.1-xvla-model",
  "prompt": "Extract the complete architecture details of X-VLA model:\n1. How does the vision encoder (Florence) produce vision tokens? How many tokens?\n2. How is the linear projection implemented? Input dim, output dim?\n3. Where are soft prompts injected in the sequence?\n4. How does the action generation work (flow matching)?\n5. What is the full forward pass: image → vision tokens → projection → soft prompts → transformer → action?\n6. Any code snippets showing the projection layer or vision token processing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://deepwiki.com/2toinf/X-VLA/2.1-xvla-model",
    "prompt": "Extract the complete architecture details of X-VLA model:\n1. How does the vision encoder (Florence) produce vision tokens? How many tokens?\n2. How is the linear projection implemented? Input dim, output dim?\n3. Where are soft prompts injected in the sequence?\n4. How does the action generation work (flow matching)?\n5. What is the full forward pass: image → vision tokens → projection → soft prompts → transformer → action?\n6. Any code snippets showing the projection layer or vision token processing"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T03:46:12.573524+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/2toinf/X-VLA",
  "prompt": "Extract:\n1. Repository structure - what are the main directories and files?\n2. How to install and set up the environment (requirements, dependencies)\n3. LIBERO evaluation instructions - how to run, what checkpoint to use\n4. Model loading code examples\n5. Any mentions of vision token count, projection layer, or connector\n6. Server-Client architecture details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/2toinf/X-VLA",
    "prompt": "Extract:\n1. Repository structure - what are the main directories and files?\n2. How to install and set up the environment (requirements, dependencies)\n3. LIBERO evaluation instructions - how to run, what checkpoint to use\n4. Model loading code examples\n5. Any mentions of vision token count, projection layer, or connector\n6. Server-Client architecture details"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T03:46:12.573656+00:00_

# X-VLA Architecture Details

## 1. Vision Encoder
**Model:** Florence-Large (Xiao et al., 2024)
- Processes main fixed-view images and language instructions together
- Auxiliary views (wrist-camera) use a "shared vision backbone" separately
- Exact token count and resolution not specified in the document

## 2. Connector/Projection
The document states the architecture includes "dedicated encoding strategies to align" modalities, but specific connector dimensions are not disclosed. Only that there are "domain-specific output projections" for actions.

## 3. LLM Backbone
**Transformer configuration:**
- 24 transformer layers
- Hidden size: 1024
- "Standard Transformer encoders" for multimodal feature fusion
- "Simple stacking" of self-attention blocks

## 4. Soft Prompts
- Learnable embeddings denoted as P^H = {p_i} for each data source
- "Injected into the model at the early stage of action generation"
- Dimension k not explicitly stated
- Account for only 0.04% of total parameters

## 5. Action Head
**Flow-matching approach:**
- Generates 30 anchor points over 4-second horizon (through temporal downsampling)
- EEF representation: xyz position + Rotate6D rotation + binary gripper state
- Loss functions: MSE for position/rotation, BCE for gripper

## 6. Parameter Breakdown
- **Total:** 0.9B parameters (X-VLA-0.9B instantiation)
- Soft prompts + action projections: "small fraction (0.04%)"
- Vision-language modules: frozen or reduced learning rate
- No detailed per-component breakdown provided

## 7. LIBERO Fine-tuning
Specific checkpoint selection and data format details are not provided in the excerpt. The paper references Appendix H for finetuning details but those specifics aren't included in the supplied content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T03:46:12.573803+00:00_

# X-VLA Architecture Analysis

Based on the provided documentation, here's what can be determined about the X-VLA model architecture:

## 1. Vision Encoder Token Generation
The documentation states the model uses a **Vision-Language Model (VLM)** component but **does not specify**:
- The vision encoder type (Florence is mentioned nowhere in the content)
- The number of vision tokens produced
- Token generation mechanism details

Only this is confirmed: "Extracts spatial features from `image0`, `image1`, `image2`" with inputs resized to **224×224 pixels**.

## 2. Linear Projection Layer
**Not documented.** The content provides no specifications for:
- Input dimensionality
- Output dimensionality
- Projection layer implementation details

## 3. Soft Prompt Injection Location
The documentation confirms soft prompts exist but **lacks specifics** on injection point. It only states: "The **Soft Prompt Hub** is the key innovation enabling cross-embodiment generalization" via an `nn.Embedding` layer indexed by `domain_id`, but the exact sequence position is unspecified.

## 4. Action Generation (Flow Matching)
The mechanism is described as: "**flow-matching-based trajectory generation**. Unlike standard autoregressive or direct regression, the decoder uses a diffusion-inspired process controlled by the `steps` parameter" with defaults of 10 steps and 30-timestep horizons.

## 5. Complete Forward Pass Flow
The documented pipeline is:
Images (224×224) → **VLM encoding** → Transformer core → Action decoder → **Output: (batch, 30, 20) trajectory tensor**

Actual intermediate token handling is **not detailed**.

## 6. Code Snippets
**None provided.** The documentation references `models/modeling_xvla.py` and `configuration_xvla.py` but includes no actual code excerpts showing projection layers or token processing.

**Conclusion:** The provided documentation is architectural overview-level and omits crucial implementation details needed for your technical questions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T03:46:12.573966+00:00_

# X-VLA Repository Summary

## 1. Repository Structure

Main directories include:
- **datasets/** — data handling and domain configurations
- **evaluation/** — benchmark-specific evaluation scripts (LIBERO, Calvin, Google Robot, etc.)
- **models/** — core model architecture files

Key files: `train.py`, `peft_train.py`, `deploy.py`, `requirements.txt`, `environment.yml`

## 2. Installation & Environment Setup

The repository provides two installation methods:

```
conda create -n XVLA python=3.10 -y
pip install -r requirements.txt
```

Or using Conda environment file:
```
conda env create -f environment.yml
conda activate xvla-stable
```

## 3. LIBERO Evaluation

For LIBERO benchmarking, use the fine-tuned checkpoint `2toINF/X-VLA-Libero`. The documentation states: "For questions about converting relative actions to absolute actions..." refer to GitHub issues #2 and #15, with "full preprocessing guidance" available in `evaluation/libero/preprocess.md`. Performance achieves **98.1%** success rate.

LoRA adapter variants are also available (`X-VLA-libero-spatial-peft`, `X-VLA-libero-object-peft`, etc.).

## 4. Model Loading Code

```python
from transformers import AutoModel, AutoProcessor
model = AutoModel.from_pretrained("2toINF/X-VLA-WidowX", 
                                   trust_remote_code=True)
processor = AutoProcessor.from_pretrained("2toINF/X-VLA-WidowX", 
                                          trust_remote_code=True)
```

## 5. Vision Tokens, Projection, Connector

The documentation does **not** contain explicit mentions of vision token counts, projection layers, or connector specifications.

## 6. Server-Client Architecture

The system employs a "Server–Client architecture to separate the model environment from simulation or robot-specific dependencies." The server launches via:

```python
model.run(processor, host="0.0.0.0", port=8000)
```

Clients send POST requests to `http://&lt;server_ip>:8000/act` with JSON payloads containing proprioceptive state,
…[truncated 159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T03:46:12.574243+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/2toinf/X-VLA/blob/main/models/modeling_xvla.py",
  "prompt": "Extract ALL code related to:\n1. Vision encoder initialization and forward pass - how are vision tokens produced? How many?\n2. The projection/connector layer - is it nn.Linear? What dimensions? Any LayerNorm?\n3. How vision tokens, soft prompts, language tokens, and action tokens are concatenated in the sequence\n4. The full forward() method signature and flow\n5. Any mentions of \"projection\", \"embed\", \"visual\", \"image\", \"token\" in class definitions\n6. The XVLAModel or similar main class definition\n7. Florence2 integration - how is Florence used?\nGive me as much code as possible, especially class definitions and forward methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/2toinf/X-VLA/blob/main/models/modeling_xvla.py",
    "prompt": "Extract ALL code related to:\n1. Vision encoder initialization and forward pass - how are vision tokens produced? How many?\n2. The projection/connector layer - is it nn.Linear? What dimensions? Any LayerNorm?\n3. How vision tokens, soft prompts, language tokens, and action tokens are concatenated in the sequence\n4. The full forward() method signature and flow\n5. Any mentions of \"projection\", \"embed\", \"visual\", \"image\", \"token\" in class definitions\n6. The XVLAModel or similar main class definition\n7. Florence2 integration - how is Florence used?\nGive me as much code as possible, especially class definitions and forward methods."
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T03:46:12.574468+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/2toinf/X-VLA/blob/main/models/configuration_xvla.py",
  "prompt": "Extract the full configuration class for X-VLA. I need:\n1. All default hyperparameters (hidden_size, num_layers, num_heads, etc.)\n2. Vision encoder config (image_size, patch_size, vision_hidden_size)\n3. Projection dimensions (projection_dim or similar)\n4. Any Florence2-related config\n5. Action-related config (action_dim, chunk_size, etc.)\nGive me the complete class definition with all default values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/2toinf/X-VLA/blob/main/models/configuration_xvla.py",
    "prompt": "Extract the full configuration class for X-VLA. I need:\n1. All default hyperparameters (hidden_size, num_layers, num_heads, etc.)\n2. Vision encoder config (image_size, patch_size, vision_hidden_size)\n3. Projection dimensions (projection_dim or similar)\n4. Any Florence2-related config\n5. Action-related config (action_dim, chunk_size, etc.)\nGive me the complete class definition with all default values."
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T03:46:12.574632+00:00_

# X-VLA Configuration Class Extract

Based on the provided file, here's the complete `XVLAConfig` class definition with all parameters:

## Core Configuration Parameters

**Transformer Head:**
- `hidden_size`: 1024
- `depth`: 24
- `num_heads`: 16
- `mlp_ratio`: 4.0
- `num_domains`: 30
- `len_soft_prompts`: 32
- `dim_time`: 32
- `max_len_seq`: 512
- `use_hetero_proj`: False
- `soft_prompt_length`: 32

**Action & Proprioception:**
- `max_action_dim`: 20
- `real_action_dim`: 20
- `num_actions`: 30
- `action_mode`: "ee6d"
- `use_proprio`: True

**Vision Encoder:**
- `florence_config`: Florence2Config (nested configuration object)

## Key Notes

The file shows X-VLA uses a "Florence2" visual-language backbone as its encoder. The configuration is structured hierarchically, with Florence2 settings nested within the main XVLAConfig class. Vision-specific parameters like image_size and patch_size are not directly exposed in this configuration file—they're contained within the Florence2Config object instantiated separately.

The `to_dict()` method enables serialization of both the main config and its nested Florence2 subconfig for HuggingFace model saving/loading.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T03:46:12.574790+00:00_

# Code Analysis: X-VLA Vision-Language-Action Model

## 1. Vision Encoder Initialization

The model uses **Florence2** as the vision backbone:

```python
self.vlm = Florence2ForConditionalGeneration(config.florence_config).to(torch.float32)
```

The encoder processes multi-view images through `self.vlm._encode_image(valid_images)`, returning shape `[#valid, N, D]` where N is the number of image tokens and D is the projection dimension.

## 2. Projection/Connector Layer

The projection dimension is extracted from Florence2's config:

```python
projection_dim = getattr(self.vlm.config, "projection_dim", None)
if projection_dim is None:
    raise ValueError("Florence2 config must provide `projection_dim`...")
```

No explicit nn.Linear projection layer is shown in this file. The `projection_dim` parameter is passed to the transformer as `multi_modal_input_size`.

## 3. Vision-Action Token Sequencing

The code shows:
- **Primary view** (image 0): merged with language embeddings via `_merge_input_ids_with_image_features()`
- **Auxiliary views** (remaining images): flattened separately as `aux_visual_inputs`

```python
merged_embeds, attention_mask = self.vlm._merge_input_ids_with_image_features(
    image_features[:, 0], # first view
    inputs_embeds, # language
)
```

Soft prompts and action tokens are handled by `SoftPromptedTransformer`.

## 4. Forward Method Signature (Training)

```python
def forward(self, input_ids: torch.LongTensor, image_input: torch.FloatTensor,
            image_mask: torch.Tensor, domain_id: torch.LongTensor, 
            proprio: torch.Tensor, action: torch.Tensor) -> Dict[str, torch.Tensor]:
```

**Flow**: 
1. Encode multimodal inputs via `forward_vlm()`
2. Apply diffusion-style noising to actions
3. Preprocess via action_space
4. Transformer prediction
5. Compute loss

## 5. Vision-Related Keywords in Class

- `forward_vlm()` - multimodal encoder
- `image_features`, `image_mask`, `pixel_values`
- `valid_feats`, `aux_visual_inputs`
- `proje
…[truncated 773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T03:46:12.574952+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Florence-2 vision encoder DaViT number of visual tokens 224x224 image projection_dim"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Florence-2 vision encoder DaViT number of visual tokens 224x224 image projection_dim"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T03:46:12.575089+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/2toinf/X-VLA/blob/main/requirements.txt",
  "prompt": "List all dependencies and their versions in the requirements.txt file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/2toinf/X-VLA/blob/main/requirements.txt",
    "prompt": "List all dependencies and their versions in the requirements.txt file"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T03:46:12.575236+00:00_

# X-VLA Project Dependencies

The requirements.txt file contains 17 dependencies with specified versions:

| Package | Version |
|---------|---------|
| av | 15.0.0 |
| transformers | <=4.51.3 |
| fastapi | (latest) |
| tensorboard | (latest) |
| peft | 0.17.1 |
| uvicorn | 0.34.3 |
| json_numpy | 2.1.0 |
| safetensors | 0.4.5 |
| numpy | 1.26.3 |
| scipy | 1.15.0 |
| einops | 0.8.1 |
| timm | 1.0.12 |
| mmengine | 0.10.5 |
| pyarrow | 20.0.0 |
| h5py | 3.12.1 |
| accelerate | 1.2.1 |
| mediapy | 1.2.4 |

Most packages have pinned versions, while fastapi and tensorboard use flexible versioning (allowing updates to newer releases). The dependencies span machine learning frameworks, data processing tools, and web service utilities.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T03:46:12.575393+00:00_

Web search results for query: "Florence-2 vision encoder DaViT number of visual tokens 224x224 image projection_dim"

Links: [{"title":"Florence-2: How it works and how to use it","url":"https://www.assemblyai.com/blog/florence-2-how-it-works-how-to-use"},{"title":"Florence-2: Microsoft's Vision-Language Model vs YOLO","url":"https://www.ultralytics.com/blog/florence-2-microsofts-latest-vision-language-model"},{"title":"[2311.06242] Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks","url":"https://ar5iv.labs.arxiv.org/html/2311.06242"},{"title":"Florence-VL: Enhancing Vision-Language Models with Generative Vision Encoder and Depth-Breadth Fusion","url":"https://arxiv.org/html/2412.04424v1"},{"title":"Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks","url":"https://openaccess.thecvf.com/content/CVPR2024/papers/Xiao_Florence-2_Advancing_a_Unified_Representation_for_a_Variety_of_Vision_CVPR_2024_paper.pdf"},{"title":"Papers Explained 214: Florence-2. While existing large vision models… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-214-florence-2-c4e17246d14b"},{"title":"Florence-2: Vision-language Model","url":"https://blog.roboflow.com/florence-2/"},{"title":"GitHub - anyantudre/Florence-2-Vision-Language-Model: Florence-2 is a novel vision foundation model with a unified, prompt-based representation for a variety of computer vision and vision-language tasks. · GitHub","url":"https://github.com/anyantudre/Florence-2-Vision-Language-Model"},{"title":"Florence-2: Open Source Vision Foundation Model — OpenVINO™ documentation","url":"https://docs.openvino.ai/2024/notebooks/florence2-with-output.html"},{"title":"Introducing Florence-2: Microsoft’s Latest Multi-Modal, Compact Visual Language Model | Datature Blog","url":"https://datature.io/blog/introducing-florence-2-microsofts-latest-multi-modal-compact-visual-language-model"}]

Based on the search results, here's what I found about
…[truncated 1126 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T03:46:12.575853+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/microsoft/Florence-2-large/blob/main/config.json",
  "prompt": "Extract all config values, especially:\n1. projection_dim\n2. image_size or input_resolution\n3. vision_config details (patch_size, hidden_size, num_layers, etc.)\n4. Any values related to number of vision tokens\n5. The full config JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/microsoft/Florence-2-large/blob/main/config.json",
    "prompt": "Extract all config values, especially:\n1. projection_dim\n2. image_size or input_resolution\n3. vision_config details (patch_size, hidden_size, num_layers, etc.)\n4. Any values related to number of vision tokens\n5. The full config JSON"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T03:46:12.576025+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/2toINF/X-VLA-Libero",
  "prompt": "Extract:\n1. Model card details - how was this fine-tuned on LIBERO?\n2. Model size / parameter count\n3. Any config details visible\n4. How to load and use this checkpoint\n5. Training details if available\n6. What LIBERO suites does it cover?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/2toINF/X-VLA-Libero",
    "prompt": "Extract:\n1. Model card details - how was this fine-tuned on LIBERO?\n2. Model size / parameter count\n3. Any config details visible\n4. How to load and use this checkpoint\n5. Training details if available\n6. What LIBERO suites does it cover?"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T03:46:12.576180+00:00_

# Florence-2-Large Config Extraction

## Key Configuration Values

### 1. **Projection Dimension**
- `projection_dim`: **1024**

### 2. **Image Size / Input Resolution**
- **Not specified** in this config.json
- The vision config uses `patch_size`, `patch_stride`, and `patch_padding` instead of fixed image dimensions
- `image_pos_embed.max_pos_embeddings`: **50** (maximum positional embeddings for spatial dimensions)

### 3. **Vision Config Details**

| Parameter | Value |
|-----------|-------|
| **model_type** | davit |
| **patch_size** | [7, 3, 3, 3] (per stage) |
| **patch_stride** | [4, 2, 2, 2] |
| **patch_padding** | [3, 1, 1, 1] |
| **dim_embed** | [256, 512, 1024, 2048] |
| **num_heads** | [8, 16, 32, 64] |
| **depths** | [1, 1, 9, 1] |
| **window_size** | 12 |
| **drop_path_rate** | 0.1 |

### 4. **Vision Token Related Values**
- `image_pos_embed.max_pos_embeddings`: **50**
- `visual_temporal_embedding.max_temporal_embeddings`: **100**
- `image_feature_source`: ["spatial_avg_pool", "temporal_avg_pool"]

### 5. **Text Config (Decoder)**
- `d_model`: 1024
- `decoder_layers`: 12
- `decoder_attention_heads`: 16
- `decoder_ffn_dim`: 4096
- `max_position_embeddings`: 4096
- `vocab_size`: 51289

## Full Config JSON Structure
The complete configuration is shown in the source content above - it's a Florence-2 model (conditional generation architecture) with a DaViT vision encoder and a transformer text decoder, optimized for image-text-to-text tasks with 4k context length support.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T03:46:12.576330+00:00_

# X-VLA-Libero Model Details

## 1. Model Card & Fine-tuning Details
The page doesn't explicitly detail how this model was fine-tuned on LIBERO. However, it indicates:
- **Base Model:** Microsoft Florence-2-large (vision-language encoder)
- **Training Data:** Bridge Data V2
- **Approach:** Soft-prompted Transformer with embodiment-specific learnable embeddings
- **Paper:** "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model" (arXiv:2510.10274)

The model was "evaluated across **six simulations** and **three real-world robots**" but LIBERO-specific training details aren't provided on this page.

## 2. Model Size / Parameter Count
- **Parameters:** ~0.9B (0.9 billion)
- **Precision:** BF16
- **Framework:** PyTorch + Transformers

## 3. Configuration Details
| Component | Details |
|-----------|---------|
| **Vision Backbone** | Florence 2 Encoder (encoder-only) |
| **Action Module** | SoftPromptedTransformer (flow-matching denoiser) |
| **Action Mode** | `ee6d` (end-effector 6D) |
| **Key Innovation** | Separate learnable soft prompts per embodiment |

## 4. Loading & Usage

```python
# Load the model
from transformers import AutoModel

model = AutoModel.from_pretrained(
    "2toINF/X-VLA-Libero",  # or WidowX variant
    trust_remote_code=True
)

# Start FastAPI server
from transformers import AutoProcessor
processor = AutoProcessor.from_pretrained("2toINF/X-VLA-Libero", trust_remote_code=True)
model.run(processor, host="0.0.0.0", port=8000)
```

## 5. Training Summary
- **Training Data:** Bridge Data V2
- **Model Size:** 0.9B parameters
- **Action Mode:** `ee6d` (6D end-effector actions)
- **Precision:** BF16

## 6. LIBERO Coverage
**Not specified on this page.** The model card mentions evaluation on "six simulations" and "three real-world robots," but doesn't explicitly list which LIBERO suites are covered. Check the [GitHub repository](https://github.com/2toINF/X-VLA) or [paper (arXiv:2510.10274)](https://arxiv.org/abs/2510.
…[truncated 45 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T03:46:12.576521+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/2toinf/X-VLA/tree/main/evaluation/libero",
  "prompt": "Extract:\n1. Full directory listing - all files and subdirectories\n2. How to run LIBERO evaluation\n3. Client code structure\n4. Any preprocessing instructions\n5. Action space details (absolute vs relative actions)\n6. Which LIBERO suites are evaluated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/2toinf/X-VLA/tree/main/evaluation/libero",
    "prompt": "Extract:\n1. Full directory listing - all files and subdirectories\n2. How to run LIBERO evaluation\n3. Client code structure\n4. Any preprocessing instructions\n5. Action space details (absolute vs relative actions)\n6. Which LIBERO suites are evaluated"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T03:46:12.576652+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/2toINF/X-VLA-Pt",
  "prompt": "Extract:\n1. What is this checkpoint? Pre-trained or fine-tuned?\n2. Model size in bytes/GB\n3. Files included (safetensors, config, etc.)\n4. How to load\n5. Any training details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/2toINF/X-VLA-Pt",
    "prompt": "Extract:\n1. What is this checkpoint? Pre-trained or fine-tuned?\n2. Model size in bytes/GB\n3. Files included (safetensors, config, etc.)\n4. How to load\n5. Any training details"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T03:46:12.576780+00:00_

# X-VLA LIBERO Evaluation Summary

## 1. Directory Listing
The `/evaluation/libero` directory contains:
- `README.md` - Documentation
- `libero_client.py` - Client code for evaluation
- `preprocess.md` - Preprocessing instructions
- `rel2abs.py` - Script for coordinate conversion

## 2. Running LIBERO Evaluation

The evaluation process involves three steps:

**Environment Setup:** Install LIBERO with Python 3.8.13 and specified PyTorch versions (1.11.0+cu113).

**Server Launch:** Run the X-VLA model as an inference server using the command:
```
python -m deploy --model_path 2toINF/X-VLA-Libero --port 8000
```

**Client Execution:** Launch evaluation via:
```
python libero_client.py --task_suites libero_spatial libero_goal libero_object libero_10
```

## 3. Client Code Structure
The `libero_client.py` file serves as the evaluation client that connects to the X-VLA server for benchmark testing.

## 4. Preprocessing Instructions
A `preprocess.md` file contains relevant preprocessing details, though specific contents aren't detailed in the provided page.

## 5. Action Space Details
The `rel2abs.py` script indicates conversion between relative and absolute coordinates, suggesting the system handles action space transformations.

## 6. Evaluated LIBERO Suites
The evaluation covers four benchmark subtasks: **Spatial**, **Goal**, **Object**, and **10** (Long tasks).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T03:46:12.576922+00:00_

# X-VLA-Pt Checkpoint Summary

## 1. Checkpoint Type
**Pre-trained Foundation Model** – This is the base X-VLA 0.9B model, serving as the foundation edition. It has been fine-tuned from Microsoft's Florence-2-large encoder and can be further adapted for specific embodiments (36 fine-tuned variants exist).

## 2. Model Size
- **Parameters:** ~0.9B (900 million)
- **Format:** Safetensors with F32 (32-bit float) precision
- **Exact file size in bytes/GB:** Not explicitly stated in the content, but based on 0.9B params at F32, approximately **3.6 GB**

## 3. Files Included
- **Safetensors** format (default)
- Model weights
- Config files
- Processor files (AutoProcessor compatible)
- Custom code support enabled (`custom_code` tag present)

## 4. How to Load

```python
from transformers import AutoModel

model = AutoModel.from_pretrained(
    "2toINF/X-VLA-Pt",
    trust_remote_code=True
)
```

**Or with processor:**
```python
from transformers import AutoProcessor

processor = AutoProcessor.from_pretrained(
    "2toINF/X-VLA-Pt", 
    trust_remote_code=True
)
```

## 5. Training Details

| Aspect | Details |
|--------|---------|
| **Training Data** | Heterogeneous cross-embodiment robotic datasets (Bridge Data) |
| **Architecture** | Soft-prompted Transformer (Florence-2 encoder + SoftPromptedTransformer denoiser) |
| **Action Mode** | `ee6d` (end-effector 6D) |
| **Precision** | BF16 (during training) |
| **Framework** | PyTorch + Transformers |
| **Approach** | Embodiment-specific soft prompts with minimal added parameters |

**Paper:** arXiv:2510.10274 (Oct 2025) | **License:** Apache 2.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T03:46:12.577228+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/train_openvla_smart_compress*.py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/train_openvla_smart_compress*.py",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T03:46:12.577390+00:00_

artifacts/train_openvla_smart_compress.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T03:46:12.577514+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/VisionTokenCompressor*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/VisionTokenCompressor*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T03:46:12.577630+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T03:46:12.577742+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "VisionTokenCompressor",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Grep",
  "tool_args": {
    "pattern": "VisionTokenCompressor",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T03:46:12.577933+00:00_

Found 239 files
logs/workers/worker_research_xvla-setup_20260520T033718.log
logs/chats/feishu_group_oc_6ea0e93e255655758819bea2ab1f224d_director.jsonl
logs/workers/worker_ops_submit-msweep-m64-m96_20260520T033510.log
logs/chats/feishu_group_oc_abc8a64bdb1365da5cc53dca7c67507d_reviewer.jsonl
registry.yaml
logs/chats/feishu_group_oc_abc8a64bdb1365da5cc53dca7c67507d.jsonl
logs/chats/worker_ops_westd41074-disk-emergency_20260520T031058.jsonl
logs/workers/worker_ops_westd41074-disk-emergency_20260520T031058.log
logs/workers/worker_ops_launch_m64_westd41074_20260520T024658.log
logs/chats/worker_ops_launch_m96_westd41074_20260520T024652.jsonl
logs/workers/worker_ops_launch_m96_westd41074_20260520T024652.log
logs/workers/worker_ops_20k_gate_prep_20260520T024314.log
checkpoints/train_smart_compress_m16_seed44_v3_ANALYZING_20260520T020631.json
checkpoints/train_smart_compress_m16_seed43_ANALYZING_20260520T014641.json
checkpoints/train_smart_compress_m128_seed43_ANALYZING_20260520T014640.json
logs/workers/worker_ops_verify_c4ext_and_cleanup_41074_20260520T011513_result.json
logs/workers/worker_ops_verify_c4ext_and_cleanup_41074_20260520T011513.log
checkpoints/eval_smart_compress_m16_seed44_RUNNING_20260520T011342.json
checkpoints/train_smart_compress_m16_seed44_v3_ANALYZING_20260520T005719.json
checkpoints/train_smart_compress_m16_seed43_ANALYZING_20260520T005718.json
checkpoints/train_smart_compress_m128_seed43_ANALYZING_20260520T005717.json
logs/chats/worker_ops_westd27271_disk_emergency_20260520T003134.jsonl
logs/workers/worker_ops_westd27271_disk_emergency_20260520T003134.log
logs/chats/worker_ops_westd_status_and_utilization_20260520T001155.jsonl
logs/workers/worker_ops_westd_status_and_utilization_20260520T001155.log
logs/chats/feishu_group_oc_abc8a64bdb1365da5cc53dca7c67507d_paper_agent.jsonl
artifacts/manifest.yaml
logs/chats/worker_ops_cqa1_eval_submit_20260519T225647.jsonl
logs/workers/worker_ops_cqa1_eval_submit_20260519T225647.log
mistakes.yaml
checkpoints/eval_sma
…[truncated 14980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T03:46:12.578102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/train_openvla_smart_compress.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/train_openvla_smart_compress.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T03:46:12.578312+00:00_

1	"""Smart Compress Training: VisionTokenCompressor + OpenVLA on LIBERO.
2	
3	Usage:
4	    python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml
5	    python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml --dry-run
6	    python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml --resume checkpoints/openvla_sc_m32/latest
7	
8	Trainable: VisionTokenCompressor only.
9	Frozen: DINOv2 + SigLIP + projector + Llama-2 7B.
10	
11	OpenVLA uses autoregressive action prediction: continuous actions are discretized
12	to 256-bin tokens, and the LLM generates them via cross-entropy loss.
13	"""
14	
15	from __future__ import annotations
16	
17	import faulthandler
18	faulthandler.enable()
19	import argparse
20	import copy
21	import json
22	import logging
23	import os
24	import signal
25	import sys
26	import time as time_module
27	from pathlib import Path
28	from typing import Any, Dict, List, Optional
29	
30	import numpy as np
31	import torch
32	import torch.nn.functional as F
33	import yaml
34	
35	logging.basicConfig(
36	    level=logging.INFO,
37	    format="%(asctime)s [%(levelname)s] %(message)s",
38	    datefmt="%Y-%m-%d %H:%M:%S",
39	)
40	log = logging.getLogger(__name__)
41	
42	ARTIFACTS_DIR = Path(__file__).resolve().parent
43	sys.path.insert(0, str(ARTIFACTS_DIR))
44	
45	from openvla_vtc_adapter import (
46	    OpenVLAActionTokenizer,
47	    OpenVLASmartCompressWrapper,
48	    VisionTokenCompressor,
49	)
50	
51	
52	# ---- config loading ----
53	
54	def load_config(config_path: str) -> Dict[str, Any]:
55	    config_path = Path(config_path)
56	    with open(config_path) as f:
57	        config = yaml.safe_load(f)
58	    if "_base_" in config:
59	        base_path = config_path.parent / config.pop("_base_")
60	        base_config = load_config(str(base_path))
61	        base_config = deep_merge(base_config, config)
62	        return base_config
63	    return config
64	
65	
66	def 
…[truncated 3244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T03:46:12.578501+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/openvla_vtc_adapter.py",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/openvla_vtc_adapter.py",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T03:46:12.578686+00:00_

1	"""OpenVLA VTC Adapter: Vision Token Compressor for OpenVLA (Prismatic + Llama-2 7B).
2	
3	Compresses N projected vision tokens to M tokens using learnable cross-attention,
4	then runs standard autoregressive generation through the frozen LLM.
5	
6	Architecture:
7	  DINOv2+SigLIP (frozen) -> MLP projector (frozen) -> N tokens x 4096
8	  -> VisionTokenCompressor (trainable) -> M tokens x 4096
9	  -> Llama-2 7B (frozen) -> action token logits -> cross-entropy loss
10	
11	Differences from SmolVLA VTC (smart_compress_module.py):
12	  - hidden_dim: 960 -> 4096 (Llama-2 7B)
13	  - Vision tokens per camera: 128 -> 256 (DINOv2+SigLIP fused per-patch)
14	  - Action paradigm: flow matching -> autoregressive (256-bin discretized tokens)
15	  - No separate action expert; standard LM head generates action tokens
16	
17	Dependencies: torch, transformers (OpenVLA loaded via trust_remote_code=True)
18	"""
19	
20	from __future__ import annotations
21	
22	import math
23	from typing import Any, Dict, List, Optional, Tuple, Union
24	
25	import torch
26	import torch.nn as nn
27	import torch.nn.functional as F
28	from torch import Tensor
29	
30	
31	# ---------------------------------------------------------------------------
32	# VisionTokenCompressor (self-contained, same architecture as SmolVLA version)
33	# ---------------------------------------------------------------------------
34	
35	
36	class CrossAttentionBlock(nn.Module):
37	    """Pre-norm cross-attention + FFN block."""
38	
39	    def __init__(self, hidden_dim: int, num_heads: int, dropout: float = 0.1):
40	        super().__init__()
41	        self.norm_q = nn.LayerNorm(hidden_dim)
42	        self.norm_kv = nn.LayerNorm(hidden_dim)
43	        self.cross_attn = nn.MultiheadAttention(
44	            embed_dim=hidden_dim,
45	            num_heads=num_heads,
46	            dropout=dropout,
47	            batch_first=True,
48	        )
49	        self.norm_ffn = nn.LayerNorm(hidden_dim)
50	        self.ffn = nn.Sequential(
51	
…[truncated 6010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T03:46:12.578833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/openvla_vtc_adapter.py",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/openvla_vtc_adapter.py",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T03:46:12.579035+00:00_

200	# ---------------------------------------------------------------------------
201	# OpenVLA Smart Compress Wrapper
202	# ---------------------------------------------------------------------------
203	
204	
205	class OpenVLASmartCompressWrapper(nn.Module):
206	    """Wraps an OpenVLA model with VisionTokenCompressor.
207	
208	    Intercepts projected vision features, compresses N -> M tokens via
209	    cross-attention, and feeds compressed tokens through the frozen LLM
210	    for autoregressive action token prediction.
211	
212	    Args:
213	        model: OpenVLA model (AutoModelForVision2Seq with trust_remote_code).
214	        processor: OpenVLA processor (AutoProcessor).
215	        compress_config: dict with keys:
216	            hidden_dim (int): LLM hidden size (default 4096).
217	            num_queries (int): M compressed tokens (default 32).
218	            num_heads (int): attention heads (default 16).
219	            num_layers (int): cross-attention blocks (default 2).
220	            dropout (float): dropout rate (default 0.1).
221	    """
222	
223	    def __init__(
224	        self,
225	        model: nn.Module,
226	        processor,
227	        compress_config: Optional[Dict[str, Any]] = None,
228	    ):
229	        super().__init__()
230	        self.model = model
231	        self.processor = processor
232	
233	        cfg = compress_config or {}
234	        hidden_dim = cfg.get("hidden_dim", 4096)
235	
236	        # Auto-detect hidden_dim from model config
237	        if hidden_dim == 4096 and hasattr(model, "config"):
238	            if hasattr(model.config, "text_config"):
239	                hidden_dim = model.config.text_config.hidden_size
240	
241	        self.compressor = VisionTokenCompressor(
242	            hidden_dim=hidden_dim,
243	            num_queries=cfg.get("num_queries", 32),
244	            num_heads=cfg.get("num_heads", 16),
245	            num_layers=cfg.get("num_layers", 2),
246	            dropout=cfg.get("dropout", 0.
…[truncated 6823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T03:46:12.579382+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "importance_margin_vla_compress",
  "file": "memory.md",
  "content": "# VLA 模型全面调研报告\n\n**调研日期**: 2026-05-20\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\n\n---\n\n## 已有实验数据\n\n| 模型 | Connector | 压缩行为 |\n|------|-----------|----------|\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\n| RoboFlamingo | Perceiver Resampler | 尝试失败（gripper loss 无法训练） |\n\n---\n\n## 完整模型调研表\n\n### 1. Octo (UC Berkeley, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 27M (Small) / 93M (Base) |\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\n\n### 2. CogACT (Microsoft/Tsinghua, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 核心创新在 DiT action module（将 VLM 认知特征作为 condition 输入扩散 transformer 生成动作）。Connector 与 OpenVLA 相同（都基于 Prismatic） |\n\n### 3. HPT (MIT, NeurIPS 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 3.1M (S) / 12.6M (B) / 50.5M (L) / 226.8M (XL) / 1.1B (Huge) |\n| Vision encoder | 预训练冻结 ResNet18 |\n| **Connector 类型** | **Cross-attention tokenizer**（learnable tokens 通过 cross-attention 聚合 vision features → 固定 16 tokens，每个 camera view 有独立 MLP projector） |\n| LLM backbone | 无（纯 decoder-only transformer，从头训练） |\n| 开源状态 | ✅ weights + code, GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |\n| LIBERO 支持 | 未确认（paper 评测 6 个 benchmark） |\n| 改造成本 | 中（非标准 VLM 架构，需改 stem + action head） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 非 VLM→LLM 架构。Cross-attention tokenizer 类似 Perceiver 但更轻量（8 heads, 64 dim/head）。跨 embodiment 预训练。 |\n\n### 4. RT-2-X (Google DeepMind, 2023)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 55B |\n| Vision encoder | ViT (PaLI-X 的视觉编码器) |\n| **Connector 类型** | 未公开（闭源） |\n| LLM backbone | PaLI-X / PaLM-E |\n| 开源状态 | ❌ **闭源**，权重不公开 |\n| LIBERO 支持 | 不可行 |\n| 改造成本 | 不可行 |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 闭源模型，无法使用 |\n\n### 5. GR-1 (ByteDance, 2023)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确公布 |\n| Vision encoder | MAE ViT-Base (预训练) |\n| **Connector 类型** | **Perceiver Resampler**（将 MAE ViT 视觉 token 数量压缩）+ linear layers 对齐维度 |\n| LLM backbone | GPT-style causal transformer（非预训练 LLM） |\n| 开源状态 | ✅ weights + code, GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\n| 改造成本 | 高（需改 data pipeline、action space、视频生成部分可能要适配） |\n| 论文 LIBERO 结果 | 无（CALVIN: 94.9%） |\n| 备注 | 既做动作预测又做视频生成（future image prediction）。语言用 CLIP text encoder。使用 Perceiver Resampler 这一点很有价值——与 RoboFlamingo 类似但架构不同。 |\n\n### 6. GR-2 (ByteDance, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未公布 |\n| Vision encoder | 未公布 |\n| **Connector 类型** | 未公布 |\n| LLM backbone | 未公布 |\n| 开源状态 | ❌ **未开源**，代码/权重未释放 |\n| LIBERO 支持 | 不可行 |\n| 改造成本 | 不可行 |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | GR-1 的后续，但未开源 |\n\n### 7. LLARVA (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B |\n| Vision encoder | CLIP ViT-L/14 |\n| **Connector 类型** | **MLP projector**（LLaVA-style，2-layer MLP with GELU） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ code + LoRA weights, GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |\n| LIBERO 支持 | 需改造 |\n| 改造成本 | 中（需接 action head + LIBERO data pipeline） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 预测 visual traces (2D 轨迹) 作为中间表示。Connector 与 OpenVLA 类似（都是 MLP projector），但用 CLIP 而非 Prismatic 双 encoder |\n\n### 8. RoboVLMs (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 不定（框架） |\n| Vision encoder | 支持多种 VLM backbone |\n| **Connector 类型** | 取决于所选 VLM（框架支持多种） |\n| LLM backbone | 取决于所选 VLM |\n| 开源状态 | ✅ code + models, GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |\n| LIBERO 支持 | 需确认 |\n| 改造成本 | 低-中（框架设计灵活） |\n| 论文 LIBERO 结果 | 未确认 |\n| 备注 | 这是一个**框架**而非单一模型。实验了 8+ VLM backbone × 4 policy 架构。最佳模型用 Kosmos backbone。对我们的 connector 对比研究有参考价值但不直接使用。 |\n\n### 9. 3D-VLA (UMass, ICML 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确 |\n| Vision encoder | 3D feature extraction（point cloud based） |\n| **Connector 类型** | **Interaction tokens**（3D-LLM 架构，用交互 token 嵌入 embodied 环境） |\n| LLM backbone | 基于 3D-LLM |\n| 开源状态 | ✅ code + diffusion models, GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA), HF: anyezhy |\n| LIBERO 支持 | 需大量改造（paper 用 RLBench） |\n| 改造成本 | 高（3D 点云输入，与 LIBERO 2D 图像差异大） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 基于 3D 点云的 VLA，与我们研究的 2D 图像 → connector → LLM 管道差异太大，不推荐 |\n\n### 10. π0 / pi-zero (Physical Intelligence, 2024-2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |\n| Vision encoder | SigLIP-So400m (400M params) |\n| **Connector 类型** | **Linear projection**（单层线性层，将 SigLIP token 投影到 Gemma embedding space） |\n| LLM backbone | Gemma 2B (via PaliGemma) |\n| 开源状态 | ✅ weights + code, GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |\n| LIBERO 支持 | ✅ 有评测（LIBERO-PRO 中被评测） |\n| 改造成本 | 低（已有 LIBERO 评测代码） |\n| 论文 LIBERO 结果 | 有（LIBERO-PRO 中有结果） |\n| 备注 | **强力推荐**。Linear projection 是最简单的 connector，与 OpenVLA 的 2-layer MLP 形成鲜明对比。Action expert 通过 MoE 架构耦合。Flow matching 生成动作。 |\n\n### 11. OpenVLA-OFT (Stanford, 2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B |\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同的 Prismatic connector） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ weights + code, GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\n| LIBERO 支持 | ✅ 原生支持，SOTA 97.1% |\n| 改造成本 | 极低（已有完整 LIBERO fine-tune + eval） |\n| 论文 LIBERO 结果 | 有: 97.1% SR (4 suite avg) |\n| 备注 | Connector 与 OpenVLA 完全相同。改进在 fine-tuning recipe（continuous actions, action chunking, bidirectional attention）。对压缩实验来说，connector 级别的差异与 OpenVLA 相同，但 action generation 方式不同，可能影响压缩行为。 |\n\n### 12. RoboMM (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确公布 |\n| Vision encoder | CLIP (via OpenFlamingo) |\n| **Connector 类型** | **3D Perception Adapter (UVFormer)** + **Cross-attention**（OpenFlamingo 风格：text queries attend to visual features through cross-attention layers） |\n| LLM backbone | OpenFlamingo (cross-attention decoder) |\n| 开源状态 | ✅ code, GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |\n| LIBERO 支持 | ✅ 有评测 |\n| 改造成本 | 低-中 |\n| 论文 LIBERO 结果 | 有: 90.7% SR |\n| 备注 | Cross-attention connector 是独特的融合方式（与 MLP/linear 的 \"先投射再拼接\" 不同）。还有 occupancy supervision 的 3D adapter。多模态解码器增强感知。 |\n\n### 13. SpatialVLA (2025, RSS)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~4B |\n| Vision encoder | SigLIP |\n| **Connector 类型** | **Linear projection + Ego3D Position Encoding**（PaliGemma2 的 linear connector + MLP(sinusoidal(3D positions)) 叠加到 visual tokens 上） |\n| LLM backbone | Gemma (via PaliGemma2) |\n| 开源状态 | ✅ weights + code, GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |\n| LIBERO 支持 | 未确认 |\n| 改造成本 | 中（需接 LIBERO data pipeline） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 基于 PaliGemma2，connector 本质上是 linear projection（与 π0 相同），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token（其他模型 7 个）。 |\n\n### 14. DeeR-VLA (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 3B / 9B (OpenFlamingo 变体) |\n| Vision encoder | CLIP ViT-L/14 (428M params) |\n| **Connector 类型** | **Perceiver Resampler + Cross-attention**（OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间） |\n| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |\n| 开源状态 | ✅ code + checkpoints, GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\n| 改造成本 | 中-高（需接 LIBERO pipeline，且多 exit 架构增加复杂度） |\n| 论文 LIBERO 结果 | 无（CALVIN benchmark） |\n| 备注 | **Perceiver Resampler** 与 RoboFlamingo 相同架构基础。动态 early exit 是额外功能。可作为 Perceiver Resampler 实验的替代方案。 |\n\n### 15. TraceVLA (UMD, ICLR 2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision-based) |\n| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) / CLIP ViT (Phi-3 版) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\n| LLM backbone | Llama-2 7B (OpenVLA 版) / Phi-3 4B |\n| 开源状态 | ✅ code + weights, GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT license |\n| LIBERO 支持 | 未确认（SimplerEnv + 真机） |\n| 改造成本 | 低（基于 OpenVLA 改造） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | Connector 与 OpenVLA 相同，改进在于 visual trace prompting（在图像上叠加动作历史轨迹）。压缩行为预期与 OpenVLA 相似。 |\n\n### 16. X-VLA (ICLR 2026)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 0.9B |\n| Vision encoder | Florence-Large (DaViT) |\n| **Connector 类型** | **Linear projection + Soft Prompts**（vision features 通过 lightweight linear layer 投影到高维空间 + 每个 embodiment 有独立 learnable prompt embeddings 注入 transformer） |\n| LLM backbone | Standard transformer 24 layers (非预训练 LLM，但使用 Florence 预训练 VLM 初始化) |\n| 开源状态 | ✅ weights + code, GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |\n| LIBERO 支持 | ✅ 原生支持，98% SR |\n| 改造成本 | 极低（已有 LIBERO 训练权重） |\n| 论文 LIBERO 结果 | 有: 98% SR |\n| 备注 | **强力推荐**。Linear projection connector + flow matching action generation。LIBERO SOTA 之一。小模型(0.9B)便于实验。 |\n\n### 17. ECoT / Embodied Chain-of-Thought (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B (基于 OpenVLA) |\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ code + weights, GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b-bridge/oxe |\n| LIBERO 支持 | 需改造 |\n| 改造成本 | 低（基于 OpenVLA） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | Connector 与 OpenVLA 完全相同，增加了 chain-of-thought reasoning。对 connector 压缩研究无新增价值。 |\n\n### 18. LingBot-VLA (Ant Group/Robbyant, 2026)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 4B |\n| Vision encoder | Qwen2.5-VL 的 ViT（2D-RoPE + window attention） |\n| **Connector 类型** | **MLP merger**（2-layer MLP with ReLU，2×2 spatial grouping 后投影 + LLM decoder 中有 cross-attention 层融合 visual features） |\n| LLM backbone | Qwen2.5-VL-3B |\n| 开源状态 | ✅ weights + code, GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |\n| LIBERO 支持 | 未确认 |\n| 改造成本 | 中 |\n| 论文 LIBERO 结果 | 未确认 |\n| 备注 | Qwen2.5-VL 的 MLP merger 是一种混合 connector：先做 spatial grouping（类似 pixel-shuffle 的空间压缩）再 MLP 投射。Mixture of Transformers 架构。 |\n\n---\n\n## Connector 类型覆盖分析\n\n### 已有数据的 Connector 类型\n| Connector 类型 | 代表模型 | 压缩行为 |\n|---------------|----------|----------|\n| Pixel-shuffle | SmolVLA | Cliff-edge collapse |\n| 2-layer MLP projector | OpenVLA (Prismatic) | Graded degradation |\n| Perceiver Resampler | RoboFlamingo | 训练失败 |\n\n### 可新增的 Connector 类型\n| Connector 类型 | 候选模型 | 特点 | 可行性 |\n|---------------|----------|------|--------|\n| **Linear projection** | **π0**, X-VLA, SpatialVLA | 最简单的 connector，单层线性变换 | ⭐⭐⭐ 高 |\n| **Cross-attention (Flamingo-style)** | **RoboMM** | 不在 encoder 端压缩，而是 decoder 端通过 cross-attention 选择性融合 | ⭐⭐ 中 |\n| **CNN patch → direct concat** | Octo | 无独立 connector，图像 patches 直接拼入 transformer | ⭐ 低（架构差异太大） |\n| **MLP merger + spatial grouping** | LingBot-VLA | 先空间合并再 MLP 投射 + cross-attention | ⭐⭐ 中 |\n| **Cross-attention tokenizer** | HPT | learnable tokens 通过 cross-attention 聚合 vision features | ⭐ 低（非 VLM 架构） |\n\n### 关键发现\n1. **Linear projection** 是最有价值的新增类型——π0 和 X-VLA 都用这种最简单的 connector，与 OpenVLA 的 2-layer MLP 形成对比\n2. **Cross-attention** (RoboMM 的 OpenFlamingo 架构) 从根本上不同：不投射拼接，而是 decoder 层间交叉注意力\n3. 大量模型共享 connector：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 **2-layer MLP**（Prismatic 或 LLaVA 架构）\n\n---\n\n## Top 推荐：最适合扩展实验的 5 个模型\n\n### 🥇 1. π0 (Physical Intelligence)\n- **Connector**: Linear projection (单层线性)\n- **推荐理由**: \n  - 与 OpenVLA 的 2-layer MLP 形成直接对比（linear vs MLP）\n  - 开源权重 + 代码，社区活跃\n  - 已有 LIBERO 评测代码\n  - PaliGemma 架构广为人知\n  - 3B 参数可在单卡运行\n- **预期价值**: Linear projection 不增加非线性变换，token 可能保留更多原始 visual feature 结构 → 压缩行为可能与 MLP 不同\n\n### 🥈 2. X-VLA\n- **Connector**: Linear projection + soft prompts\n- **推荐理由**:\n  - 同样是 linear projection，与 π0 对比看 soft prompt 的影响\n  - LIBERO 98% SR，已有训练好的 LIBERO 权重直接可用\n  - 0.9B 参数，实验成本最低\n  - ICLR 2026，最新模型\n  - Apache-2.0 开源\n- **预期价值**: 验证 linear projection 的压缩行为是否 consistent across models\n\n### 🥉 3. DeeR-VLA\n- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)\n- **推荐理由**:\n  - Perceiver Resampler 与 RoboFlamingo 相同架构，但 DeeR-VLA 已验证可训练（CALVIN benchmark 正常工作）\n  - 给 Perceiver Resampler 第二次机会\n  - 可对比 RoboFlamingo 的训练失败是架构问题还是实现问题\n  - Open source with checkpoints\n- **预期价值**: Perceiver Resampler 本身就做了 attention-based compression → 压缩行为可能与 MLP/linear 截然不同\n- **风险**: LIBERO 需要自己改造\n\n### 4. RoboMM\n- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter\n- **推荐理由**:\n  - Cross-attention 融合方式从根本上不同于 projection-based connectors\n  - 已有 LIBERO 结果 (90.7%)\n  - Open source\n- **预期价值**: Cross-attention 在 decoder 端动态选择 visual features → 可能展现出与 projection-based 完全不同的压缩模式\n- **风险**: 架构较复杂，3D adapter 增加变量\n\n### 5. OpenVLA-OFT\n- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)\n- **推荐理由**:\n  - Connector 与 OpenVLA 相同，但 action generation 完全不同（continuous + chunking）\n  - LIBERO 97.1% SOTA\n  - 可验证 \"相同 connector + 不同 action head\" 是否影响压缩行为\n  - 已有完整 LIBERO 代码\n- **预期价值**: 作为 OpenVLA 的对照组，隔离 connector vs action head 对压缩的影响\n\n---\n\n## 不推荐的模型及原因\n\n| 模型 | 排除原因 |\n|------|----------|\n| RT-2-X | 闭源，权重不可用 |\n| GR-2 | 未开源 |\n| 3D-VLA | 3D 点云输入，与 2D VLA 差异太大 |\n| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP），不新增类型 |\n| LLARVA | Connector 与 OpenVLA 类似（MLP projector），不新增类型 |\n| TraceVLA | Connector 与 OpenVLA 相同，不新增类型 |\n| ECoT | Connector 与 OpenVLA 相同，不新增类型 |\n| HPT | 非 VLM 架构，不适合 connector 压缩叙事 |\n| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO 支持 + 视频生成架构改造成本高 |\n| Octo | 无独立 connector（CNN patch 直接拼入），架构与标准 VLM 差异太大 |\n\n---\n\n## 总结：Connector 类型 × 模型矩阵\n\n| Connector 类型 | 已有 | 推荐新增 |\n|---------------|------|----------|\n| Pixel-shuffle | SmolVLA ✅ | — |\n| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT（同 connector 不同 action head） |\n| Perceiver Resampler | RoboFlamingo ❌(失败) | **DeeR-VLA** |\n| **Linear projection** | — | **π0, X-VLA** |\n| **Cross-attention** | — | **RoboMM** |\n\n实现后可达 **5 种 connector 类型 × 6+ 模型**的全面对比。\n\n---\n\n## X-VLA 详细架构调研（2026-05-20 新增）\n\n### 模型身份确认\n- **名称**: X-VLA (Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model)\n- **论文**: arXiv:2510.10274, ICLR 2026\n- **GitHub**: [2toinf/X-VLA](https://github.com/2toinf/X-VLA)\n- **HuggingFace**: [2toINF/X-VLA](https://huggingface.co/collections/2toINF/x-vla)\n- **参数量**: 0.9B\n- **许可**: Apache-2.0\n- **LIBERO SR**: 98.1%\n\n### 架构详解\n\n```\nImage (224×224) → Florence-Large (DaViT) → Vision Tokens [B, N, 2048]\n    → Linear Projection + LayerNorm → [B, N, 1024]\n    → Merge with Text Token Embeddings → Florence2 Encoder (self-attention)\n    → Context Features → SoftPromptedTransformer (24 layers, hidden=1024)\n        + Soft Prompts (32 learnable embeddings per embodiment)\n        + Noised Action Tokens (flow matching)\n    → Denoised Action Trajectory [B, 30, 20]\n```\n\n**各组件详情**:\n\n| 组件 | 规格 |\n|------|------|\n| Vision Encoder | Florence-Large (DaViT): patch_stride=[4,2,2,2] → total stride 32 |\n| Vision Token 数量 | ~49 tokens (7×7 at 224×224) 或 ~576 tokens (24×24 at 768×768) — **需实际加载模型验证** |\n| Projection | Linear + LayerNorm, dim 2048 → 1024 (projection_dim=1024) |\n| Soft Prompts | 32 tokens/embodiment, 0.04% of total params |\n| Transformer | 24 layers, hidden=1024, 16 heads, mlp_ratio=4.0 |\n| Action Head | Flow matching, 30 anchor points × 20 dims (EE6D), 10 denoising steps |\n| Max Sequence | 512 tokens |\n\n### HuggingFace 权重\n| Checkpoint | 用途 | 地址 |\n|------------|------|------|\n| X-VLA-Pt | 预训练基座 (cross-embodiment) | 2toINF/X-VLA-Pt |\n| X-VLA-Libero | LIBERO 全参数微调 (98.1% SR) | 2toINF/X-VLA-Libero |\n| X-VLA-libero-*-peft | LIBERO LoRA 微调 (各 suite) | 2toINF/X-VLA-libero-spatial-peft 等 |\n\n### 环境依赖\n```\ntransformers<=4.51.3, torch, einops==0.8.1, timm==1.0.12, \naccelerate==1.2.1, peft==0.17.1, safetensors==0.4.5,\nnumpy==1.26.3, scipy==1.15.0, mmengine==0.10.5,\nfastapi, uvicorn==0.34.3, h5py==3.12.1, pyarrow==20.0.0,\nav==15.0.0, mediapy==1.2.4\n```\nLIBERO 评估另需 Python 3.8 环境。\n\n### VTC 集成方案\n**插入点**: Florence2 `_encode_image()` 输出 → **VTC** → `_merge_input_ids_with_image_features()`\n\n**改造清单**:\n1. 创建 `xvla_vtc_adapter.py`（复用 VisionTokenCompressor，hidden_dim 改 1024）\n2. 创建 XVLASmartCompressWrapper，hook Florence2 vision 输出\n3. 修改 merge 逻辑以适应压缩后的 token 数量\n4. 创建 `train_xvla_smart_compress.py`（参考 X-VLA 的 train.py + peft_train.py）\n5. 适配 flow matching loss（不同于 OpenVLA 的 cross-entropy）\n\n**与 OpenVLA VTC 的关键差异**:\n| 维度 | OpenVLA | X-VLA |\n|------|---------|-------|\n| hidden_dim | 4096 | 1024 |\n| 原始 vision tokens | 256 | ~49-576 (待验证) |\n| Action 范式 | Autoregressive (256-bin CE) | Flow matching (MSE+BCE) |\n| Connector | 2-layer MLP | Linear + LayerNorm |\n| 模型大小 | 7B | 0.9B |\n\n**预计工作量**: 8-12 小时\n- 代码改造: 4-6h（adapter + training script）\n- 环境搭建 + 模型下载: 2-3h\n- 验证 + 调试: 2-3h\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "memory.md",
    "content": "# VLA 模型全面调研报告\n\n**调研日期**: 2026-05-20\n**目的**: 寻找不同 connector 架构的开源 VLA 模型，扩展 vision connector 对 token 可压缩性影响的实验\n\n---\n\n## 已有实验数据\n\n| 模型 | Connector | 压缩行为 |\n|------|-----------|----------|\n| SmolVLA | Pixel-shuffle | Cliff-edge collapse (k=0.95 → 0% SR) |\n| OpenVLA | 2-layer MLP projector | Graded degradation (线性下降) |\n| RoboFlamingo | Perceiver Resampler | 尝试失败（gripper loss 无法训练） |\n\n---\n\n## 完整模型调研表\n\n### 1. Octo (UC Berkeley, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 27M (Small) / 93M (Base) |\n| Vision encoder | Shallow CNN (从头训练，非预训练 ViT) |\n| **Connector 类型** | **CNN patch encoder → 直接拼接进 transformer（无独立 connector）** |\n| LLM backbone | 纯 transformer（非预训练 LLM），decoder-only |\n| 开源状态 | ✅ weights + code, GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |\n| LIBERO 支持 | ✅ 原生支持，fine-tune 后 ~72% SR |\n| 改造成本 | 低（已有 LIBERO fine-tune 代码） |\n| 论文 LIBERO 结果 | 有: ~72% (fine-tuned) |\n| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。图像通过浅层 CNN 编码为 16×16 patches 后直接拼入 transformer 序列。语言用 T5 tokenizer/encoder。Action head 是 diffusion policy。 |\n\n### 2. CogACT (Microsoft/Tsinghua, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~7.1B (7B Prismatic VLM + 89M-300M DiT action module) |\n| Vision encoder | DINOv2 + SigLIP (双 encoder，channel 拼接) |\n| **Connector 类型** | **2-layer MLP projector**（Prismatic 架构：DINOv2+SigLIP feature → channel concat → 2-layer MLP → Llama-2 embedding space） |\n| LLM backbone | Llama-2 7B (via Prismatic-7B) |\n| 开源状态 | ✅ weights + code, GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base, CogACT/CogACT-Small |\n| LIBERO 支持 | 需改造（paper 用 SimplerEnv + 真机） |\n| 改造成本 | 中（需接 LIBERO data pipeline + action space） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 核心创新在 DiT action module（将 VLM 认知特征作为 condition 输入扩散 transformer 生成动作）。Connector 与 OpenVLA 相同（都基于 Prismatic） |\n\n### 3. HPT (MIT, NeurIPS 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 3.1M (S) / 12.6M (B) / 50.5M (L) / 226.8M (XL) / 1.1B (Huge) |\n| Vision encoder | 预训练冻结 ResNet18 |\n| **Connector 类型** | **Cross-attention tokenizer**（learnable tokens 通过 cross-attention 聚合 vision features → 固定 16 tokens，每个 camera view 有独立 MLP projector） |\n| LLM backbone | 无（纯 decoder-only transformer，从头训练） |\n| 开源状态 | ✅ weights + code, GitHub: [liruiw/HPT](https://github.com/liruiw/HPT), HF: liruiw/hpt |\n| LIBERO 支持 | 未确认（paper 评测 6 个 benchmark） |\n| 改造成本 | 中（非标准 VLM 架构，需改 stem + action head） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 非 VLM→LLM 架构。Cross-attention tokenizer 类似 Perceiver 但更轻量（8 heads, 64 dim/head）。跨 embodiment 预训练。 |\n\n### 4. RT-2-X (Google DeepMind, 2023)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 55B |\n| Vision encoder | ViT (PaLI-X 的视觉编码器) |\n| **Connector 类型** | 未公开（闭源） |\n| LLM backbone | PaLI-X / PaLM-E |\n| 开源状态 | ❌ **闭源**，权重不公开 |\n| LIBERO 支持 | 不可行 |\n| 改造成本 | 不可行 |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 闭源模型，无法使用 |\n\n### 5. GR-1 (ByteDance, 2023)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确公布 |\n| Vision encoder | MAE ViT-Base (预训练) |\n| **Connector 类型** | **Perceiver Resampler**（将 MAE ViT 视觉 token 数量压缩）+ linear layers 对齐维度 |\n| LLM backbone | GPT-style causal transformer（非预训练 LLM） |\n| 开源状态 | ✅ weights + code, GitHub: [bytedance/GR-1](https://github.com/bytedance/GR-1), Apache-2.0 |\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\n| 改造成本 | 高（需改 data pipeline、action space、视频生成部分可能要适配） |\n| 论文 LIBERO 结果 | 无（CALVIN: 94.9%） |\n| 备注 | 既做动作预测又做视频生成（future image prediction）。语言用 CLIP text encoder。使用 Perceiver Resampler 这一点很有价值——与 RoboFlamingo 类似但架构不同。 |\n\n### 6. GR-2 (ByteDance, 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未公布 |\n| Vision encoder | 未公布 |\n| **Connector 类型** | 未公布 |\n| LLM backbone | 未公布 |\n| 开源状态 | ❌ **未开源**，代码/权重未释放 |\n| LIBERO 支持 | 不可行 |\n| 改造成本 | 不可行 |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | GR-1 的后续，但未开源 |\n\n### 7. LLARVA (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B |\n| Vision encoder | CLIP ViT-L/14 |\n| **Connector 类型** | **MLP projector**（LLaVA-style，2-layer MLP with GELU） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ code + LoRA weights, GitHub: [Dantong88/LLARVA](https://github.com/Dantong88/LLARVA), Apache-2.0 |\n| LIBERO 支持 | 需改造 |\n| 改造成本 | 中（需接 action head + LIBERO data pipeline） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 预测 visual traces (2D 轨迹) 作为中间表示。Connector 与 OpenVLA 类似（都是 MLP projector），但用 CLIP 而非 Prismatic 双 encoder |\n\n### 8. RoboVLMs (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 不定（框架） |\n| Vision encoder | 支持多种 VLM backbone |\n| **Connector 类型** | 取决于所选 VLM（框架支持多种） |\n| LLM backbone | 取决于所选 VLM |\n| 开源状态 | ✅ code + models, GitHub: [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) |\n| LIBERO 支持 | 需确认 |\n| 改造成本 | 低-中（框架设计灵活） |\n| 论文 LIBERO 结果 | 未确认 |\n| 备注 | 这是一个**框架**而非单一模型。实验了 8+ VLM backbone × 4 policy 架构。最佳模型用 Kosmos backbone。对我们的 connector 对比研究有参考价值但不直接使用。 |\n\n### 9. 3D-VLA (UMass, ICML 2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确 |\n| Vision encoder | 3D feature extraction（point cloud based） |\n| **Connector 类型** | **Interaction tokens**（3D-LLM 架构，用交互 token 嵌入 embodied 环境） |\n| LLM backbone | 基于 3D-LLM |\n| 开源状态 | ✅ code + diffusion models, GitHub: [UMass-Embodied-AGI/3D-VLA](https://github.com/UMass-Embodied-AGI/3D-VLA), HF: anyezhy |\n| LIBERO 支持 | 需大量改造（paper 用 RLBench） |\n| 改造成本 | 高（3D 点云输入，与 LIBERO 2D 图像差异大） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 基于 3D 点云的 VLA，与我们研究的 2D 图像 → connector → LLM 管道差异太大，不推荐 |\n\n### 10. π0 / pi-zero (Physical Intelligence, 2024-2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~3.3B (400M SigLIP + 2.6B Gemma + ~300M action expert) |\n| Vision encoder | SigLIP-So400m (400M params) |\n| **Connector 类型** | **Linear projection**（单层线性层，将 SigLIP token 投影到 Gemma embedding space） |\n| LLM backbone | Gemma 2B (via PaliGemma) |\n| 开源状态 | ✅ weights + code, GitHub: [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi), HF 有 PyTorch port |\n| LIBERO 支持 | ✅ 有评测（LIBERO-PRO 中被评测） |\n| 改造成本 | 低（已有 LIBERO 评测代码） |\n| 论文 LIBERO 结果 | 有（LIBERO-PRO 中有结果） |\n| 备注 | **强力推荐**。Linear projection 是最简单的 connector，与 OpenVLA 的 2-layer MLP 形成鲜明对比。Action expert 通过 MoE 架构耦合。Flow matching 生成动作。 |\n\n### 11. OpenVLA-OFT (Stanford, 2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B |\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同的 Prismatic connector） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ weights + code, GitHub: [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |\n| LIBERO 支持 | ✅ 原生支持，SOTA 97.1% |\n| 改造成本 | 极低（已有完整 LIBERO fine-tune + eval） |\n| 论文 LIBERO 结果 | 有: 97.1% SR (4 suite avg) |\n| 备注 | Connector 与 OpenVLA 完全相同。改进在 fine-tuning recipe（continuous actions, action chunking, bidirectional attention）。对压缩实验来说，connector 级别的差异与 OpenVLA 相同，但 action generation 方式不同，可能影响压缩行为。 |\n\n### 12. RoboMM (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 未明确公布 |\n| Vision encoder | CLIP (via OpenFlamingo) |\n| **Connector 类型** | **3D Perception Adapter (UVFormer)** + **Cross-attention**（OpenFlamingo 风格：text queries attend to visual features through cross-attention layers） |\n| LLM backbone | OpenFlamingo (cross-attention decoder) |\n| 开源状态 | ✅ code, GitHub: [RoboUniview/RoboMM](https://github.com/RoboUniview/RoboMM) |\n| LIBERO 支持 | ✅ 有评测 |\n| 改造成本 | 低-中 |\n| 论文 LIBERO 结果 | 有: 90.7% SR |\n| 备注 | Cross-attention connector 是独特的融合方式（与 MLP/linear 的 \"先投射再拼接\" 不同）。还有 occupancy supervision 的 3D adapter。多模态解码器增强感知。 |\n\n### 13. SpatialVLA (2025, RSS)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | ~4B |\n| Vision encoder | SigLIP |\n| **Connector 类型** | **Linear projection + Ego3D Position Encoding**（PaliGemma2 的 linear connector + MLP(sinusoidal(3D positions)) 叠加到 visual tokens 上） |\n| LLM backbone | Gemma (via PaliGemma2) |\n| 开源状态 | ✅ weights + code, GitHub: [SpatialVLA/SpatialVLA](https://github.com/SpatialVLA/SpatialVLA), HF: IPEC-COMMUNITY/spatialvla-4b-224-pt |\n| LIBERO 支持 | 未确认 |\n| 改造成本 | 中（需接 LIBERO data pipeline） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | 基于 PaliGemma2，connector 本质上是 linear projection（与 π0 相同），加了 3D spatial encoding。Adaptive Action Grids 只输出 3 个 action token（其他模型 7 个）。 |\n\n### 14. DeeR-VLA (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 3B / 9B (OpenFlamingo 变体) |\n| Vision encoder | CLIP ViT-L/14 (428M params) |\n| **Connector 类型** | **Perceiver Resampler + Cross-attention**（OpenFlamingo 架构：CLIP features → Perceiver Resampler → learnable cross-attention blocks 注入 LLM 层间） |\n| LLM backbone | MPT-1B (3B 版) / MPT-7B (9B 版) |\n| 开源状态 | ✅ code + checkpoints, GitHub: [yueyang130/DeeR-VLA](https://github.com/yueyang130/DeeR-VLA) |\n| LIBERO 支持 | 需改造（paper 只有 CALVIN） |\n| 改造成本 | 中-高（需接 LIBERO pipeline，且多 exit 架构增加复杂度） |\n| 论文 LIBERO 结果 | 无（CALVIN benchmark） |\n| 备注 | **Perceiver Resampler** 与 RoboFlamingo 相同架构基础。动态 early exit 是额外功能。可作为 Perceiver Resampler 实验的替代方案。 |\n\n### 15. TraceVLA (UMD, ICLR 2025)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B (OpenVLA-based) / 4B (Phi-3-Vision-based) |\n| Vision encoder | SigLIP + DINOv2 (OpenVLA 版) / CLIP ViT (Phi-3 版) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\n| LLM backbone | Llama-2 7B (OpenVLA 版) / Phi-3 4B |\n| 开源状态 | ✅ code + weights, GitHub: [umd-huang-lab/tracevla](https://github.com/umd-huang-lab/tracevla), HF: furonghuang-lab/tracevla_7b, MIT license |\n| LIBERO 支持 | 未确认（SimplerEnv + 真机） |\n| 改造成本 | 低（基于 OpenVLA 改造） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | Connector 与 OpenVLA 相同，改进在于 visual trace prompting（在图像上叠加动作历史轨迹）。压缩行为预期与 OpenVLA 相似。 |\n\n### 16. X-VLA (ICLR 2026)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 0.9B |\n| Vision encoder | Florence-Large (DaViT) |\n| **Connector 类型** | **Linear projection + Soft Prompts**（vision features 通过 lightweight linear layer 投影到高维空间 + 每个 embodiment 有独立 learnable prompt embeddings 注入 transformer） |\n| LLM backbone | Standard transformer 24 layers (非预训练 LLM，但使用 Florence 预训练 VLM 初始化) |\n| 开源状态 | ✅ weights + code, GitHub: [2toinf/X-VLA](https://github.com/2toinf/X-VLA), HF: 2toINF/X-VLA, Apache-2.0 |\n| LIBERO 支持 | ✅ 原生支持，98% SR |\n| 改造成本 | 极低（已有 LIBERO 训练权重） |\n| 论文 LIBERO 结果 | 有: 98% SR |\n| 备注 | **强力推荐**。Linear projection connector + flow matching action generation。LIBERO SOTA 之一。小模型(0.9B)便于实验。 |\n\n### 17. ECoT / Embodied Chain-of-Thought (2024)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 7B (基于 OpenVLA) |\n| Vision encoder | SigLIP + DINOv2 (Prismatic) |\n| **Connector 类型** | **2-layer MLP projector**（与 OpenVLA 相同） |\n| LLM backbone | Llama-2 7B |\n| 开源状态 | ✅ code + weights, GitHub: [MichalZawalski/embodied-CoT](https://github.com/MichalZawalski/embodied-CoT), HF: ecot-openvla-7b-bridge/oxe |\n| LIBERO 支持 | 需改造 |\n| 改造成本 | 低（基于 OpenVLA） |\n| 论文 LIBERO 结果 | 无 |\n| 备注 | Connector 与 OpenVLA 完全相同，增加了 chain-of-thought reasoning。对 connector 压缩研究无新增价值。 |\n\n### 18. LingBot-VLA (Ant Group/Robbyant, 2026)\n\n| 字段 | 信息 |\n|------|------|\n| 参数量 | 4B |\n| Vision encoder | Qwen2.5-VL 的 ViT（2D-RoPE + window attention） |\n| **Connector 类型** | **MLP merger**（2-layer MLP with ReLU，2×2 spatial grouping 后投影 + LLM decoder 中有 cross-attention 层融合 visual features） |\n| LLM backbone | Qwen2.5-VL-3B |\n| 开源状态 | ✅ weights + code, GitHub: [Robbyant/lingbot-vla](https://github.com/Robbyant/lingbot-vla) |\n| LIBERO 支持 | 未确认 |\n| 改造成本 | 中 |\n| 论文 LIBERO 结果 | 未确认 |\n| 备注 | Qwen2.5-VL 的 MLP merger 是一种混合 connector：先做 spatial grouping（类似 pixel-shuffle 的空间压缩）再 MLP 投射。Mixture of Transformers 架构。 |\n\n---\n\n## Connector 类型覆盖分析\n\n### 已有数据的 Connector 类型\n| Connector 类型 | 代表模型 | 压缩行为 |\n|---------------|----------|----------|\n| Pixel-shuffle | SmolVLA | Cliff-edge collapse |\n| 2-layer MLP projector | OpenVLA (Prismatic) | Graded degradation |\n| Perceiver Resampler | RoboFlamingo | 训练失败 |\n\n### 可新增的 Connector 类型\n| Connector 类型 | 候选模型 | 特点 | 可行性 |\n|---------------|----------|------|--------|\n| **Linear projection** | **π0**, X-VLA, SpatialVLA | 最简单的 connector，单层线性变换 | ⭐⭐⭐ 高 |\n| **Cross-attention (Flamingo-style)** | **RoboMM** | 不在 encoder 端压缩，而是 decoder 端通过 cross-attention 选择性融合 | ⭐⭐ 中 |\n| **CNN patch → direct concat** | Octo | 无独立 connector，图像 patches 直接拼入 transformer | ⭐ 低（架构差异太大） |\n| **MLP merger + spatial grouping** | LingBot-VLA | 先空间合并再 MLP 投射 + cross-attention | ⭐⭐ 中 |\n| **Cross-attention tokenizer** | HPT | learnable tokens 通过 cross-attention 聚合 vision features | ⭐ 低（非 VLM 架构） |\n\n### 关键发现\n1. **Linear projection** 是最有价值的新增类型——π0 和 X-VLA 都用这种最简单的 connector，与 OpenVLA 的 2-layer MLP 形成对比\n2. **Cross-attention** (RoboMM 的 OpenFlamingo 架构) 从根本上不同：不投射拼接，而是 decoder 层间交叉注意力\n3. 大量模型共享 connector：OpenVLA, CogACT, LLARVA, TraceVLA, ECoT, OpenVLA-OFT 都用 **2-layer MLP**（Prismatic 或 LLaVA 架构）\n\n---\n\n## Top 推荐：最适合扩展实验的 5 个模型\n\n### 🥇 1. π0 (Physical Intelligence)\n- **Connector**: Linear projection (单层线性)\n- **推荐理由**: \n  - 与 OpenVLA 的 2-layer MLP 形成直接对比（linear vs MLP）\n  - 开源权重 + 代码，社区活跃\n  - 已有 LIBERO 评测代码\n  - PaliGemma 架构广为人知\n  - 3B 参数可在单卡运行\n- **预期价值**: Linear projection 不增加非线性变换，token 可能保留更多原始 visual feature 结构 → 压缩行为可能与 MLP 不同\n\n### 🥈 2. X-VLA\n- **Connector**: Linear projection + soft prompts\n- **推荐理由**:\n  - 同样是 linear projection，与 π0 对比看 soft prompt 的影响\n  - LIBERO 98% SR，已有训练好的 LIBERO 权重直接可用\n  - 0.9B 参数，实验成本最低\n  - ICLR 2026，最新模型\n  - Apache-2.0 开源\n- **预期价值**: 验证 linear projection 的压缩行为是否 consistent across models\n\n### 🥉 3. DeeR-VLA\n- **Connector**: Perceiver Resampler + Cross-attention (OpenFlamingo)\n- **推荐理由**:\n  - Perceiver Resampler 与 RoboFlamingo 相同架构，但 DeeR-VLA 已验证可训练（CALVIN benchmark 正常工作）\n  - 给 Perceiver Resampler 第二次机会\n  - 可对比 RoboFlamingo 的训练失败是架构问题还是实现问题\n  - Open source with checkpoints\n- **预期价值**: Perceiver Resampler 本身就做了 attention-based compression → 压缩行为可能与 MLP/linear 截然不同\n- **风险**: LIBERO 需要自己改造\n\n### 4. RoboMM\n- **Connector**: Cross-attention (OpenFlamingo) + 3D Adapter\n- **推荐理由**:\n  - Cross-attention 融合方式从根本上不同于 projection-based connectors\n  - 已有 LIBERO 结果 (90.7%)\n  - Open source\n- **预期价值**: Cross-attention 在 decoder 端动态选择 visual features → 可能展现出与 projection-based 完全不同的压缩模式\n- **风险**: 架构较复杂，3D adapter 增加变量\n\n### 5. OpenVLA-OFT\n- **Connector**: 2-layer MLP projector (与 OpenVLA 相同)\n- **推荐理由**:\n  - Connector 与 OpenVLA 相同，但 action generation 完全不同（continuous + chunking）\n  - LIBERO 97.1% SOTA\n  - 可验证 \"相同 connector + 不同 action head\" 是否影响压缩行为\n  - 已有完整 LIBERO 代码\n- **预期价值**: 作为 OpenVLA 的对照组，隔离 connector vs action head 对压缩的影响\n\n---\n\n## 不推荐的模型及原因\n\n| 模型 | 排除原因 |\n|------|----------|\n| RT-2-X | 闭源，权重不可用 |\n| GR-2 | 未开源 |\n| 3D-VLA | 3D 点云输入，与 2D VLA 差异太大 |\n| CogACT | Connector 与 OpenVLA 相同（Prismatic MLP），不新增类型 |\n| LLARVA | Connector 与 OpenVLA 类似（MLP projector），不新增类型 |\n| TraceVLA | Connector 与 OpenVLA 相同，不新增类型 |\n| ECoT | Connector 与 OpenVLA 相同，不新增类型 |\n| HPT | 非 VLM 架构，不适合 connector 压缩叙事 |\n| GR-1 | 有 Perceiver Resampler（有价值），但无 LIBERO 支持 + 视频生成架构改造成本高 |\n| Octo | 无独立 connector（CNN patch 直接拼入），架构与标准 VLM 差异太大 |\n\n---\n\n## 总结：Connector 类型 × 模型矩阵\n\n| Connector 类型 | 已有 | 推荐新增 |\n|---------------|------|----------|\n| Pixel-shuffle | SmolVLA ✅ | — |\n| 2-layer MLP projector | OpenVLA ✅ | OpenVLA-OFT（同 connector 不同 action head） |\n| Perceiver Resampler | RoboFlamingo ❌(失败) | **DeeR-VLA** |\n| **Linear projection** | — | **π0, X-VLA** |\n| **Cross-attention** | — | **RoboMM** |\n\n实现后可达 **5 种 connector 类型 × 6+ 模型**的全面对比。\n\n---\n\n## X-VLA 详细架构调研（2026-05-20 新增）\n\n### 模型身份确认\n- **名称**: X-VLA (Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model)\n- **论文**: arXiv:2510.10274, ICLR 2026\n- **GitHub**: [2toinf/X-VLA](https://github.com/2toinf/X-VLA)\n- **HuggingFace**: [2toINF/X-VLA](https://huggingface.co/collections/2toINF/x-vla)\n- **参数量**: 0.9B\n- **许可**: Apache-2.0\n- **LIBERO SR**: 98.1%\n\n### 架构详解\n\n```\nImage (224×224) → Florence-Large (DaViT) → Vision Tokens [B, N, 2048]\n    → Linear Projection + LayerNorm → [B, N, 1024]\n    → Merge with Text Token Embeddings → Florence2 Encoder (self-attention)\n    → Context Features → SoftPromptedTransformer (24 layers, hidden=1024)\n        + Soft Prompts (32 learnable embeddings per embodiment)\n        + Noised Action Tokens (flow matching)\n    → Denoised Action Trajectory [B, 30, 20]\n```\n\n**各组件详情**:\n\n| 组件 | 规格 |\n|------|------|\n| Vision Encoder | Florence-Large (DaViT): patch_stride=[4,2,2,2] → total stride 32 |\n| Vision Token 数量 | ~49 tokens (7×7 at 224×224) 或 ~576 tokens (24×24 at 768×768) — **需实际加载模型验证** |\n| Projection | Linear + LayerNorm, dim 2048 → 1024 (projection_dim=1024) |\n| Soft Prompts | 32 tokens/embodiment, 0.04% of total params |\n| Transformer | 24 layers, hidden=1024, 16 heads, mlp_ratio=4.0 |\n| Action Head | Flow matching, 30 anchor points × 20 dims (EE6D), 10 denoising steps |\n| Max Sequence | 512 tokens |\n\n### HuggingFace 权重\n| Checkpoint | 用途 | 地址 |\n|------------|------|------|\n| X-VLA-Pt | 预训练基座 (cross-embodiment) | 2toINF/X-VLA-Pt |\n| X-VLA-Libero | LIBERO 全参数微调 (98.1% SR) | 2toINF/X-VLA-Libero |\n| X-VLA-libero-*-peft | LIBERO LoRA 微调 (各 suite) | 2toINF/X-VLA-libero-spatial-peft 等 |\n\n### 环境依赖\n```\ntransformers<=4.51.3, torch, einops==0.8.1, timm==1.0.12, \naccelerate==1.2.1, peft==0.17.1, safetensors==0.4.5,\nnumpy==1.26.3, scipy==1.15.0, mmengine==0.10.5,\nfastapi, uvicorn==0.34.3, h5py==3.12.1, pyarrow==20.0.0,\nav==15.0.0, mediapy==1.2.4\n```\nLIBERO 评估另需 Python 3.8 环境。\n\n### VTC 集成方案\n**插入点**: Florence2 `_encode_image()` 输出 → **VTC** → `_merge_input_ids_with_image_features()`\n\n**改造清单**:\n1. 创建 `xvla_vtc_adapter.py`（复用 VisionTokenCompressor，hidden_dim 改 1024）\n2. 创建 XVLASmartCompressWrapper，hook Florence2 vision 输出\n3. 修改 merge 逻辑以适应压缩后的 token 数量\n4. 创建 `train_xvla_smart_compress.py`（参考 X-VLA 的 train.py + peft_train.py）\n5. 适配 flow matching loss（不同于 OpenVLA 的 cross-entropy）\n\n**与 OpenVLA VTC 的关键差异**:\n| 维度 | OpenVLA | X-VLA |\n|------|---------|-------|\n| hidden_dim | 4096 | 1024 |\n| 原始 vision tokens | 256 | ~49-576 (待验证) |\n| Action 范式 | Autoregressive (256-bin CE) | Flow matching (MSE+BCE) |\n| Connector | 2-layer MLP | Linear + LayerNorm |\n| 模型大小 | 7B | 0.9B |\n\n**预计工作量**: 8-12 小时\n- 代码改造: 4-6h（adapter + training script）\n- 环境搭建 + 模型下载: 2-3h\n- 验证 + 调试: 2-3h\n"
  }
}
````

</details>

---

### Tool result

_source line 64 · 2026-05-20T03:46:12.579797+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_xvla-setup_20260520T033718",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-20T03:46:12.579987+00:00_

报告已保存到 memory.md。总结如下：

## X-VLA 调研结论

**模型确认**: X-VLA（[2toinf/X-VLA](https://github.com/2toinf/X-VLA)），0.9B 参数，ICLR 2026，LIBERO 98.1% SR。

**架构**:
- Vision encoder: Florence-Large (DaViT)
- Connector: **Linear projection** (dim 2048→1024) + LayerNorm
- Backbone: 24-layer Transformer (hidden=1024, 16 heads)
- Action: Flow matching, 30 anchor points × 20 dims (EE6D)
- 特色: 每个 embodiment 有 32 个 learnable soft prompts

**Vision Token 数量**: DaViT total stride=32，224×224 输入下 7×7=49 tokens。但 Florence-2-Large 默认分辨率是 768×768 (24×24=576 tokens)，**需要加载模型后验证 X-VLA 实际使用的分辨率**。

**VTC 集成方案**: 插入在 Florence2 `_encode_image()` 输出和 `_merge_input_ids_with_image_features()` 之间，复用 VisionTokenCompressor（hidden_dim 改 1024）。需适配 flow matching loss。

**权重**: 使用 `2toINF/X-VLA-Libero` 作为起点（已在 LIBERO 上 fine-tune 到 98.1%）。

**预计工作量**: 8-12 小时（adapter 代码 4-6h + 环境 2-3h + 调试 2-3h）。

**与 OpenVLA 对比的关键点**: X-VLA 的 linear projection 不引入非线性变换，vision token 经过的变换远少于 OpenVLA 的 2-layer MLP。预期压缩行为与 MLP connector 存在质性差异——这正是论文需要的 "最简 connector" 数据点。

Sources:
- [X-VLA GitHub](https://github.com/2toinf/X-VLA)
- [X-VLA Paper (arXiv:2510.10274)](https://arxiv.org/abs/2510.10274)
- [X-VLA-Libero on HuggingFace](https://huggingface.co/2toINF/X-VLA-Libero)
- [X-VLA HuggingFace Collection](https://huggingface.co/collections/2toINF/x-vla)
- [Florence-2-Large Config](https://huggingface.co/microsoft/Florence-2-large)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_xvla-setup_20260520T033718"
}
```

</details>

---
