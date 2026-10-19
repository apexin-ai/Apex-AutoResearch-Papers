# research smolvla lerobot

**action cond info bottleneck** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/chats/worker_research_smolvla-lerobot_20260515T111122.jsonl`
- **Structured JSON:** [`22f1aa28909bef7fc73a.json`](../../sessions/22/22f1aa28909bef7fc73a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

75 recorded events

### Tool call

_source line 1 · 2026-05-15T11:17:58.259549+00:00_

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
  "session": "worker_research_smolvla-lerobot_20260515T111122",
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

_source line 2 · 2026-05-15T11:17:58.259879+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T11:17:58.260074+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA model architecture vision language action HuggingFace 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA model architecture vision language action HuggingFace 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T11:17:58.260206+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LeRobot HuggingFace SmolVLA policy fine-tuning pipeline 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LeRobot HuggingFace SmolVLA policy fine-tuning pipeline 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T11:17:58.260329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA SigLIP vision encoder tokens dimensions action head"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA SigLIP vision encoder tokens dimensions action head"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T11:17:58.260445+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot github setup.py pyproject.toml dependencies python pytorch version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot github setup.py pyproject.toml dependencies python pytorch version"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T11:17:58.260642+00:00_

Web search results for query: "SmolVLA SigLIP vision encoder tokens dimensions action head"

Links: [{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/guides/vla-models-comparison"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Teaching Robots to Fold Clothes: SmolVLA for Bimanual Cloth Manipulation","url":"https://www.vizuaranewsletter.com/p/teaching-robots-to-fold-clothes-smolvla"},{"title":"SmolVLA: Compact Vision-Language-Action Model","url":"https://www.emergentmind.com/topics/smolvla"},{"title":"SigLIP · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/siglip"},{"title":"SigLIP2 Vision Encoder","url":"https://www.emergentmind.com/topics/siglip2-vision-encoder"},{"title":"AI and Robotics: With SmolVLA, Hugging Face Opens Vision-Language-Action Models to the Community","url":"https://www.actuia.com/en/news/ai-and-robotics-with-smolvla-hugging-face-opens-vision-language-action-models-to-the-community/"},{"title":"GenAI for Robotics: Fine-Tuning SmolVLA to Pick and Place | by Henry H | Medium","url":"https://medium.com/@henryhu1607/genai-for-robotics-fine-tuning-smolvla-to-pick-and-place-940b485e6c9b"}]

Based on the search results, here's what I found about SmolVLA's SigLIP vision encoder tokens dimensions and action head:

## Vision Encoder and Token Dimensions

SmolVLA uses a SigLIP-400M model as its vision encoder, and the language backbone is a 500M parameter transformer.

For token efficiency, SmolVLA limits the num
…[truncated 916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T11:17:58.260850+00:00_

Web search results for query: "SmolVLA model architecture vision language action HuggingFace 2025 2026"

Links: [{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"blog/smolvla.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/smolvla.md"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Hugging Face Releases SmolVLA, a Compact Open-Source Robotics Model -- Pure AI","url":"https://pureai.com/articles/2025/06/10/hugging-face-releases-smolvla.aspx"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Weekly Robotics June #1 - SmolVLA discovery and thoughts","url":"https://huggingface.co/blog/Beegbrain/daily-robotics-june"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"}]

Based on the web search results, here's comprehensive information about the SmolVLA model architecture from Hugging Face:

## Overview

SmolVLA is a 450M parameter vision-language-action model designed for affordable and efficient robotics. It is a compact (450M), open-source Vision-Language-Action model for robotics that runs on consumer 
…[truncated 1497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T11:17:58.261049+00:00_

Web search results for query: "lerobot github setup.py pyproject.toml dependencies python pytorch version"

Links: [{"title":"lerobot/pyproject.toml at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/pyproject.toml"},{"title":"cannot resolve dependency with pyproject.toml · Issue #2443 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2443"},{"title":"Installation · Hugging Face","url":"https://huggingface.co/docs/lerobot/installation"},{"title":"Installation and Setup | huggingface/lerobot | DeepWiki","url":"https://deepwiki.com/huggingface/lerobot/1.1-installation-and-setup"},{"title":"Proposal: Modernize EnvHub Environment Repository Design · Issue #2406 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2406"},{"title":"Writing your pyproject.toml - Python Packaging User Guide","url":"https://packaging.python.org/en/latest/guides/writing-pyproject-toml/"},{"title":"pytorch/pyproject.toml at main · pytorch/pytorch","url":"https://github.com/pytorch/pytorch/blob/main/pyproject.toml"},{"title":"How to contribute to 🤗 LeRobot?","url":"https://huggingface.co/docs/lerobot/contributing"},{"title":"GitHub - ai-completed/LeRobot: 🤗 LeRobot: State-of-the-art Machine Learning for Real-World Robotics in Pytorch","url":"https://github.com/ai-completed/LeRobot"},{"title":"Issues from importing `torch` in `setup.py` · Issue #265 · rusty1s/pytorch_scatter","url":"https://github.com/rusty1s/pytorch_scatter/issues/265"}]

Based on the search results, I found information about LeRobot's dependencies from their GitHub repository. Here's what I found:

## LeRobot PyProject Configuration

LeRobot specifies torchvision>=0.21.0,<0.23.0 as a dependency, which indicates the PyTorch ecosystem packages being used.

## Python and PyTorch Requirements

LeRobot requires Python >=3.12 and support for PyTorch >= 2.10. However, there are platform-specific considerations:

- TorchCodec is not available on macOS
…[truncated 747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T11:17:58.261259+00:00_

Web search results for query: "LeRobot HuggingFace SmolVLA policy fine-tuning pipeline 2025 2026"

Links: [{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"},{"title":"Parameter efficient fine-tuning with 🤗 PEFT","url":"https://huggingface.co/docs/lerobot/peft_training"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"LeRobot datasets and training | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/"}]

Based on the search results, here's what I found about LeRobot, HuggingFace, and SmolVLA policy fine-tuning pipeline:

## Overview

SmolVLA is Hugging Face's lightweight foundation model for robotics. The smolvla_base model is intended as a base model to fine tune on your specific use case.

## Model Details

The pretrained 450M smolvla_base model can be fine-tuned on your data. SmolVLA takes as input multiple camera views, the robot's current sensorimotor state, and a natural language instruction, encoded into contextual features used to condition the action expert when generating an action chunk.

## Fine-Tuning Pipeline

Trai
…[truncated 1167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T11:17:58.261469+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/smolvla",
  "prompt": "Extract all technical details about SmolVLA: model architecture, vision encoder details (SigLIP version, output dimensions, token count), language model details (SmolLM2 size), action expert architecture (number of layers, attention mechanism, flow matching details), how to load the model, how to fine-tune, configuration parameters, policy class name, and any code examples. Also extract information about freezing backbone layers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/smolvla",
    "prompt": "Extract all technical details about SmolVLA: model architecture, vision encoder details (SigLIP version, output dimensions, token count), language model details (SmolLM2 size), action expert architecture (number of layers, attention mechanism, flow matching details), how to load the model, how to fine-tune, configuration parameters, policy class name, and any code examples. Also extract information about freezing backbone layers."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T11:17:58.261678+00:00_

# SmolVLA

SmolVLA is Hugging Face’s lightweight foundation model for robotics. Designed for easy fine-tuning on LeRobot datasets, it helps accelerate your development!

  
  
  
    Figure 1. SmolVLA takes as input (i) multiple cameras views, (ii) the
    robot’s current sensorimotor state, and (iii) a natural language
    instruction, encoded into contextual features used to condition the action
    expert when generating an action chunk.
  

## Set Up Your Environment

1. Install LeRobot by following our [Installation Guide](./installation).
2. Install SmolVLA dependencies by running:

   ```bash
   pip install -e ".[smolvla]"
   ```

## Collect a dataset

SmolVLA is a base model, so fine-tuning on your own data is required for optimal performance in your setup.
We recommend recording ~50 episodes of your task as a starting point. Follow our guide to get started: [Recording a Dataset](./il_robots)

In your dataset, make sure to have enough demonstrations per each variation (e.g. the cube position on the table if it is cube pick-place task) you are introducing.

We recommend checking out the dataset linked below for reference that was used in the [SmolVLA paper](https://huggingface.co/papers/2506.01844):

🔗 [SVLA SO100 PickPlace](https://huggingface.co/spaces/lerobot/visualize_dataset?path=%2Flerobot%2Fsvla_so100_pickplace%2Fepisode_0)

In this dataset, we recorded 50 episodes across 5 distinct cube positions. For each position, we collected 10 episodes of pick-and-place interactions. This structure, repeating each variation several times, helped the model generalize better. We tried similar dataset with 25 episodes, and it was not enough leading to a bad performance. So, the data quality and quantity is definitely a key.
After you have your dataset available on the Hub, you are good to go to use our finetuning script to adapt SmolVLA to your application.

## Finetune SmolVLA on your data

Use [`smolvla_base`](https://hf.co/lerobot/smolvla_base), our pretrained 45
…[truncated 2912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T11:17:58.261856+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/lerobot/smolvla_base",
  "prompt": "Extract all technical details from this model card: model architecture details, config parameters, how to load the model (code examples), training details, input/output formats, action dimensions, vision encoder details, language model details, and any links to code or documentation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/lerobot/smolvla_base",
    "prompt": "Extract all technical details from this model card: model architecture details, config parameters, how to load the model (code examples), training details, input/output formats, action dimensions, vision encoder details, language model details, and any links to code or documentation."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T11:17:58.261989+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2506.01844v1",
  "prompt": "Extract detailed technical architecture information about SmolVLA: 1) SigLIP vision encoder - exact model name/version, input resolution, output dimensions, number of tokens before and after PixelShuffle. 2) SmolLM2 language model - exact size, hidden dimensions, number of layers. 3) Action expert - architecture details, number of layers, cross-attention mechanism, flow matching details, action chunk size. 4) How visual tokens are processed (PixelShuffle details). 5) Training setup - batch size, learning rate, optimizer. 6) Any specific numbers about model parameters breakdown."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2506.01844v1",
    "prompt": "Extract detailed technical architecture information about SmolVLA: 1) SigLIP vision encoder - exact model name/version, input resolution, output dimensions, number of tokens before and after PixelShuffle. 2) SmolLM2 language model - exact size, hidden dimensions, number of layers. 3) Action expert - architecture details, number of layers, cross-attention mechanism, flow matching details, action chunk size. 4) How visual tokens are processed (PixelShuffle details). 5) Training setup - batch size, learning rate, optimizer. 6) Any specific numbers about model parameters breakdown."
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T11:17:58.262112+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/pyproject.toml",
  "prompt": "Extract all dependency information: Python version requirement, all dependencies with version constraints (especially pytorch, torchvision, transformers, accelerate, datasets, and any other key ML dependencies). Also extract the project version, any optional dependency groups (extras), and build system requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/blob/main/pyproject.toml",
    "prompt": "Extract all dependency information: Python version requirement, all dependencies with version constraints (especially pytorch, torchvision, transformers, accelerate, datasets, and any other key ML dependencies). Also extract the project version, any optional dependency groups (extras), and build system requirements."
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T11:17:58.262228+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/peft_training",
  "prompt": "Extract all details about PEFT/LoRA training with LeRobot: how to configure LoRA for SmolVLA, which modules can be targeted, how to freeze backbone, configuration examples, training commands, and any code snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/peft_training",
    "prompt": "Extract all details about PEFT/LoRA training with LeRobot: how to configure LoRA for SmolVLA, which modules can be targeted, how to freeze backbone, configuration examples, training commands, and any code snippets."
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T11:17:58.262371+00:00_

# Parameter efficient fine-tuning with 🤗 PEFT

[🤗 PEFT](https://github.com/huggingface/peft) (Parameter-Efficient Fine-Tuning) is a library for efficiently adapting
large pretrained models such as pre-trained policies (e.g., SmolVLA, π₀, ...) to new tasks without training all
of the model's parameters while yielding comparable performance.

Install the `lerobot[peft]` optional package to enable PEFT support.

To read about all the possible methods of adaption, please refer to the [🤗 PEFT docs](https://huggingface.co/docs/peft/index).

## Training SmolVLA

In this section we'll show you how to train a pre-trained SmolVLA policy with PEFT on the libero dataset.
For brevity we're only training on the `libero_spatial` subset. We will use `lerobot/smolvla_base` as the model
to parameter efficiently fine-tune:

```
lerobot-train \
 --policy.path=lerobot/smolvla_base \
 --policy.repo_id=your_hub_name/my_libero_smolvla \
 --dataset.repo_id=HuggingFaceVLA/libero \
 --policy.output_features=null \
 --policy.input_features=null \
 --policy.optimizer_lr=1e-3 \
 --policy.scheduler_decay_lr=1e-4 \
 --env.type=libero \
 --env.task=libero_spatial \
 --steps=100000 \
 --batch_size=32 \
 --peft.method_type=LORA \
 --peft.r=64
```

Note the `--peft.method_type` parameter that let's you select which PEFT method to use. Here we use
[LoRA](https://huggingface.co/docs/peft/main/en/package_reference/lora) (Low-Rank Adapter) which is probably the most
popular fine-tuning method to date. Low-rank adaption means that we only fine-tune a matrix with comparably low rank
instead of the full weight matrix. This rank can be specified using the `--peft.r` parameter. The higher the rank
the closer you get to full fine-tuning

There are more complex methods that have more parameters. These are not yet supported, feel free to raise an issue
if you want to see a specific PEFT method supported.

By default, PEFT will target the `q_proj` and `v_proj` layers of the LM expert in SmolVLA. It will also targe
…[truncated 1172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T11:17:58.262562+00:00_

# SmolVLA Base Model - Technical Details

## Model Overview
- **Name:** lerobot/smolvla_base
- **Type:** Vision-Language-Action (VLA) model
- **Purpose:** Compact, efficient robotics model trainable on a single GPU
- **Paper:** SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arxiv: 2506.01844)
- **Reference Implementation:** https://github.com/huggingface/lerobot

## Model Architecture & Inputs/Outputs

**Inputs:**
- Multi-view images
- Proprioceptive/state information
- Optional language instructions

**Outputs:**
- Continuous actions

**Training Objective:** Flow matching

**Action Representation:** Continuous (not tokenized)

## Loading the Model

```python
import torch
from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.policies.factory import make_pre_post_processors

# Load policy
model_id = "lerobot/smolvla_base"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
policy = SmolVLAPolicy.from_pretrained(model_id).to(device).eval()

# Create preprocessor/postprocessor
preprocess, postprocess = make_pre_post_processors(
    policy.config,
    model_id,
    preprocessor_overrides={"device_processor": {"device": str(device)}},
)
```

## Inference Example

```python
# Load dataset
dataset = LeRobotDataset("lerobot/libero")

# Get frame and run inference
batch = preprocess(dict(dataset[0]))
with torch.inference_mode():
    pred_action = policy.select_action(batch)
    pred_action = postprocess(pred_action)
```

## Training / Fine-tuning

```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/&lt;dataset> \
  --output_dir=./outputs/[RUN_NAME] \
  --policy.path=lerobot/smolvla_base \
  --policy.dtype=bfloat16 \
  --policy.device=cuda \
  --steps=100000 \
  --batch_size=4
```

**Optional policy-specific flags:**
- `-policy.chunk_size=...`
- `-policy.n_action_steps=...`
- `-policy.max_action_tokens=...`
- `-policy.gradient_checkpointing=
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T11:17:58.262728+00:00_

# LeRobot Dependency Analysis

## Project Metadata
- **Project Name:** lerobot
- **Version:** 0.5.2
- **Python Requirement:** `>=3.12`
- **License:** Apache-2.0

## Build System
- **Build Backend:** setuptools.build_meta
- **Build Requirements:** setuptools

## Core Dependencies (with version constraints)

### Machine Learning & PyTorch Stack
- torch: `>=2.7,<2.12.0`
- torchvision: `>=0.22.0,<0.27.0`
- numpy: `>=2.0.0,<2.3.0`

### Computer Vision & Media
- opencv-python-headless: `>=4.9.0,<4.14.0`
- Pillow: `>=10.0.0,<13.0.0`
- einops: `>=0.8.0,<0.9.0`

### Configuration & Hub Integration
- draccus: `==0.10.0`
- huggingface-hub: `>=1.0.0,<2.0.0`
- requests: `>=2.32.0,<3.0.0`

### Environment & Serialization
- gymnasium: `>=1.1.1,<2.0.0`
- safetensors: `>=0.4.3,<1.0.0`

### Utilities
- packaging, termcolor, tqdm, cmake, setuptools (specified versions)

## Notable Optional Dependency Groups

**Dataset Support:** datasets, pandas, pyarrow, av, torchcodec, jsonlines

**Training:** accelerate `>=1.10.0,<2.0.0`, wandb `>=0.24.0,<0.25.0`

**Transformers Integration:** transformers `>=5.4.0,<5.6.0`, peft `>=0.18.0,<1.0.0`

**Diffusion Models:** diffusers `>=0.27.2,<0.36.0`

**Robotics Hardware:** Multiple motor/robot-specific packages (feetech, dynamixel, reachy2, etc.)

**Development:** pytest, pre-commit, mypy, ruff

## Environment-Specific Notes
- Platform-specific wheels for torchcodec across Linux, macOS, Windows architectures
- Intel RealSense support varies by OS
- Some packages excluded due to dependency conflicts (e.g., robomme, robocasa)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T11:17:58.262877+00:00_

# SmolVLA Technical Architecture Details

## Vision Encoder (SigLIP)
The paper specifies using **SigLIP** as the vision encoder within SmolVLM-2, but does not provide exact model version details. The document states: *"visual tokens to 64 per frame"* after applying pixel shuffle operations, though the original input resolution before processing is not explicitly stated. Input images are resized to 512×512 for consistency with VLM requirements.

## Language Model (SmolLM2)
SmolVLA uses **SmolLM2** as its language decoder within the SmolVLM-2 backbone. Specific hidden dimensions and layer counts are not disclosed in the paper. The document mentions using *"only the first 16 layers of the large language model (LLM) within the VLM,"* indicating the full model has more layers, but exact parameter counts for SmolLM2 alone aren't provided.

## Action Expert Architecture
- **Total model parameters**: 450 million (SmolVLA-0.45B variant)
- **Action expert parameters**: ~100 million
- **Training objective**: Flow matching (conditional)
- **Action output**: Chunks of n=50 actions
- **Attention design**: *"interleave cross and causal self-attention layers"*
- **Hidden size**: 0.75×d (where d = VLM hidden dimension)
- **Inference steps**: Fixed to 10 steps during inference

## Training Configuration
- **Batch size**: 256 (global, across 4 GPUs)
- **Learning rate schedule**: Starting at 1e-4, decaying to 2.5e-6 via cosine schedule
- **Optimizer**: AdamW (β₁=0.9, β₂=0.95)
- **Training steps**: 200,000 (pretraining); 100,000-200,000 (fine-tuning)
- **Precision**: bfloat16

## Token Processing
Visual tokens are reduced through: *"pixel shuffle operation, limiting the visual tokens to 64 per frame."* The VLM processes these reduced tokens alongside language instruction tokens and state projections (single token via linear layer).

## Model Variants Tested
- SmolVLA-0.24B
- SmolVLA-0.45B (primary)
- SmolVLA-2.25B

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T11:17:58.263052+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/blog/smolvla",
  "prompt": "Extract all technical architecture details: 1) Exact SigLIP model version used (e.g. SigLIP-400M-patch14-384 or similar). 2) SmolLM2 exact size and config. 3) PixelShuffle details - original token count before shuffle and after (64). 4) Vision encoder output dimensions per token. 5) Action expert: hidden dimension, number of layers, cross-attention details. 6) VLM hidden dimension. 7) Which layers of VLM are skipped/used (first 16 layers). 8) Flow matching: number of denoising steps. 9) Any specific numbers about parameter counts for each component."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/blog/smolvla",
    "prompt": "Extract all technical architecture details: 1) Exact SigLIP model version used (e.g. SigLIP-400M-patch14-384 or similar). 2) SmolLM2 exact size and config. 3) PixelShuffle details - original token count before shuffle and after (64). 4) Vision encoder output dimensions per token. 5) Action expert: hidden dimension, number of layers, cross-attention details. 6) VLM hidden dimension. 7) Which layers of VLM are skipped/used (first 16 layers). 8) Flow matching: number of denoising steps. 9) Any specific numbers about parameter counts for each component."
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T11:17:58.263253+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com huggingface/lerobot lerobot/policies/smolvla modeling_smolvla.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com huggingface/lerobot lerobot/policies/smolvla modeling_smolvla.py"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T11:17:58.263382+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLM2 SigLIP-400M hidden dimension 1152 tokens 729 SmolLM2 135M 360M"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLM2 SigLIP-400M hidden dimension 1152 tokens 729 SmolLM2 135M 360M"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T11:17:58.263553+00:00_

Web search results for query: "site:github.com huggingface/lerobot lerobot/policies/smolvla modeling_smolvla.py"

Links: [{"title":"lerobot/examples/tutorial/smolvla/using_smolvla_example.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/examples/tutorial/smolvla/using_smolvla_example.py"},{"title":"Questions about SmolVLA design · Issue #1995 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1995"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"Details of adapting SmolVLA to other robotic arms with different configurations · Issue #2351 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2351"},{"title":"Problems with running the pretrained lerobot/smolvla_base · Issue #2374 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2374"},{"title":"SmolVLA policy uses wrong action pad key · Issue #1707 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1707"},{"title":"smolvla training bugs on 3090 · Issue #1234 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1234"},{"title":"GitHub - AndreasL9z/lerobot_SmolVLA: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/AndreasL9z/lerobot_SmolVLA"},{"title":"Add SmolVLA by mshukor · Pull Request #1175 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/pull/1175"}]

I found search results related to your query about SmolVLA in the LeRobot repository. The search returned several GitHub resources:

1. **Example Usage**: The repository includes an example showing how to use SmolVLA by importing `SmolVLAPolicy` from `lerobot
…[truncated 955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T11:17:58.263735+00:00_

Web search results for query: "SmolVLM2 SigLIP-400M hidden dimension 1152 tokens 729 SmolLM2 135M 360M"

Links: [{"title":"SmolVLM to SmolVLM2: Compact Models for Multi-Image VQA - PyImageSearch","url":"https://pyimagesearch.com/2025/06/23/smolvlm-to-smolvlm2-compact-models-for-multi-image-vqa/"},{"title":"Papers Explained 346: SmolVLM. SmolVLM is a family of small, efficient… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-346-smolvlm-9b4e208fa66b"},{"title":"google/siglip-so400m-patch14-384 · hidden sizes","url":"https://huggingface.co/google/siglip-so400m-patch14-384/discussions/3"},{"title":"SmolVLM: Redefining small and efficient multimodal models","url":"https://arxiv.org/html/2504.05299v1"},{"title":"transformers/src/transformers/models/smolvlm/modeling_smolvlm.py at main · huggingface/transformers","url":"https://github.com/huggingface/transformers/blob/main/src/transformers/models/smolvlm/modeling_smolvlm.py"},{"title":"Paper Review: SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features | by Andrew Lukyanenko | Medium","url":"https://artgor.medium.com/paper-review-siglip-2-multilingual-vision-language-encoders-with-improved-semantic-understanding-b7b578002adc"},{"title":"SigLIP2 Vision Encoder","url":"https://www.emergentmind.com/topics/siglip2-vision-encoder"},{"title":"HuggingFaceTB/SmolVLM2-2.2B-Instruct · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolVLM2-2.2B-Instruct"},{"title":"blog/smolervlm.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/smolervlm.md"},{"title":"nvidia/PS3-1.5K-SigLIP2 · Hugging Face","url":"https://huggingface.co/nvidia/PS3-1.5K-SigLIP2"}]

Based on the search results, I found relevant information about SmolVLM2, SigLIP-400M, and the related components:

## Key Findings:

**SmolVLM2 Architecture:**
SmolVLM-2.2B uses a 400M SigLIP-SO400M vision encoder and a 1.7B-parameter SmolLM2 ba
…[truncated 797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T11:17:58.263908+00:00_

# SmolVLA Technical Architecture Details

Based on the provided documentation, here are the technical architecture specifications:

## 1. **Vision Encoder (SigLIP)**
- **Model Version**: Not explicitly specified in the document
- The document states: "SigLIP vision encoder" but does not provide the exact model variant (e.g., SigLIP-400M-patch14-384)
- Part of the SmolVLM2-500M backbone

## 2. **Language Model (SmolLM2)**
- **Size**: 1.7B parameters
- **Full name**: SmolLM2-1.7B-Instruct
- **Config**: Serves as the language decoder in the VLM backbone

## 3. **Visual Token Reduction (PixelShuffle)**
- **Original token count**: 1,024 tokens (from a 512×512 image)
- **Reduced token count**: 64 tokens per frame
- **Reduction ratio**: ~16:1 compression
- **Method**: PixelShuffle used as "an efficient shuffling technique"
- **Runtime behavior**: Uses "only the global image" rather than image tiling

## 4. **Vision Encoder Output Dimensions**
- **Not specified** in the documentation

## 5. **Action Expert (Flow Matching Transformer)**
- **Parameter count**: ~100M parameters
- **Hidden dimension**: **75% of VLM's hidden size** (exact VLM dimension not stated)
- **Number of layers**: Not explicitly specified
- **Attention pattern**: Interleaved cross-attention (CA) and self-attention (SA)
  - Cross-attention: Action tokens attend to VLM features
  - Self-attention: Causal attention to past action tokens
- **Architecture style**: Transformer with interleaved attention blocks

## 6. **VLM Hidden Dimension**
- **Not explicitly specified** in the document
- Inferred only that action expert uses 75% of this dimension

## 7. **VLM Layer Usage**
- **Layers used**: Up to **layer N = 16** (half of total layers)
- **Rationale**: "Layer skipping" halves compute cost
- **Benefit**: "Minimal performance loss" with 50% speedup
- **Prior knowledge**: "Early layers often provide better representations for downstream tasks"

## 8. **Flow Matching Details**
- **Denoising steps**: Not specifie
…[truncated 957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T11:17:58.264094+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/lerobot/policies/smolvla/modeling_smolvla.py",
  "prompt": "Extract the complete class structure: 1) SmolVLAPolicy class - what it inherits from, key methods (forward, select_action, etc.), how it loads from pretrained. 2) Action expert class name and structure. 3) How vision encoder is accessed and used. 4) How VLM layers are skipped (the layer skipping mechanism). 5) Any dimension constants (hidden_size, etc.). 6) Flow matching implementation details. 7) How the model freezes/unfreezes components. 8) Configuration class name and key parameters. 9) Import statements showing key dependencies. List all class names and their line numbers if visible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/blob/main/lerobot/policies/smolvla/modeling_smolvla.py",
    "prompt": "Extract the complete class structure: 1) SmolVLAPolicy class - what it inherits from, key methods (forward, select_action, etc.), how it loads from pretrained. 2) Action expert class name and structure. 3) How vision encoder is accessed and used. 4) How VLM layers are skipped (the layer skipping mechanism). 5) Any dimension constants (hidden_size, etc.). 6) Flow matching implementation details. 7) How the model freezes/unfreezes components. 8) Configuration class name and key parameters. 9) Import statements showing key dependencies. List all class names and their line numbers if visible."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T11:17:58.264226+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T11:17:58.264347+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/lerobot/policies/smolvla/configuration_smolvla.py",
  "prompt": "Extract the complete SmolVLA configuration: all config parameters with their default values, especially: vision encoder config, language model config, action expert config (hidden_size, num_layers, etc.), chunk_size, n_action_steps, flow matching parameters, VLM path/name, any dimension parameters, freeze options, and the class hierarchy."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/blob/main/lerobot/policies/smolvla/configuration_smolvla.py",
    "prompt": "Extract the complete SmolVLA configuration: all config parameters with their default values, especially: vision encoder config, language model config, action expert config (hidden_size, num_layers, etc.), chunk_size, n_action_steps, flow matching parameters, VLM path/name, any dimension parameters, freeze options, and the class hierarchy."
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T11:17:58.264469+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct",
  "prompt": "Extract the model architecture details: SigLIP vision encoder exact version, hidden dimensions, number of layers, vocabulary size, and any config parameters that show the exact dimensions used in this model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct",
    "prompt": "Extract the model architecture details: SigLIP vision encoder exact version, hidden dimensions, number of layers, vocabulary size, and any config parameters that show the exact dimensions used in this model."
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T11:17:58.264605+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T11:17:58.264714+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/tree/main/lerobot/policies/smolvla",
  "prompt": "List all files in the SmolVLA policy directory and their descriptions. What files are included? Is there a separate file for the action expert?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/tree/main/lerobot/policies/smolvla",
    "prompt": "List all files in the SmolVLA policy directory and their descriptions. What files are included? Is there a separate file for the action expert?"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T11:17:58.264829+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T11:17:58.264943+00:00_

# SmolVLM2-500M-Video-Instruct Architecture Details

Based on the provided web page content, here are the available architecture details:

## Vision Encoder
- **Type:** SigLIP (Sigmoid Loss for Image-Text Pre-training)
- **Specific Version:** `google/siglip-base-patch16-512`
- **Patch Size:** 16x16
- **Input Resolution:** 512x512

## Text Decoder
- **Base Model:** SmolLM2-360M-Instruct
- **Language:** English

## Model Size & Efficiency
- **Parameter Count:** 500M (500 million)
- **GPU RAM Required:** 1.8GB for video inference
- **Data Type:** bfloat16 (as shown in code examples)

## Training Configuration
- **Training Data:** 3.3M samples from 10 different datasets
- **Data Distribution:**
  - Image: 34.4%
  - Text: 20.2%
  - Video: 33.0%
  - Multi-image: 12.3%

## Architecture Family
- **Based on:** [Idefics3](https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3)

**Note:** The web page does not provide granular architectural specifications such as exact hidden dimensions, number of transformer layers, vocabulary size, or detailed config parameters. For these specifics, you would need to access the model's config files directly from the Hugging Face Hub repository or the model card's detailed technical documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T11:17:58.265099+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/huggingface/lerobot/main/lerobot/policies/smolvla/modeling_smolvla.py",
  "prompt": "Extract the complete class structure: 1) All class names defined in this file. 2) SmolVLAPolicy class - inheritance, key methods (forward, select_action, from_pretrained, etc.), how it initializes subcomponents. 3) Action expert class - name, architecture, hidden dim, number of layers. 4) How vision encoder features are extracted. 5) Layer skipping mechanism - which parameter controls it, how it works. 6) Flow matching implementation - noise schedule, number of steps. 7) Freezing/unfreezing mechanism. 8) Any hardcoded dimensions or important constants. 9) Configuration references. List key code snippets and line numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/huggingface/lerobot/main/lerobot/policies/smolvla/modeling_smolvla.py",
    "prompt": "Extract the complete class structure: 1) All class names defined in this file. 2) SmolVLAPolicy class - inheritance, key methods (forward, select_action, from_pretrained, etc.), how it initializes subcomponents. 3) Action expert class - name, architecture, hidden dim, number of layers. 4) How vision encoder features are extracted. 5) Layer skipping mechanism - which parameter controls it, how it works. 6) Flow matching implementation - noise schedule, number of steps. 7) Freezing/unfreezing mechanism. 8) Any hardcoded dimensions or important constants. 9) Configuration references. List key code snippets and line numbers."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T11:17:58.265217+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T11:17:58.265327+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/huggingface/lerobot/main/lerobot/policies/smolvla/configuration_smolvla.py",
  "prompt": "Extract all configuration parameters with their default values. Especially: 1) VLM model name/path 2) Action expert parameters (hidden_size, num_layers, num_heads) 3) chunk_size, n_action_steps 4) Flow matching parameters (num_steps, sigma) 5) Vision-related params 6) Freeze/training params 7) Class names and inheritance 8) Any references to SigLIP dimensions or token counts."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/huggingface/lerobot/main/lerobot/policies/smolvla/configuration_smolvla.py",
    "prompt": "Extract all configuration parameters with their default values. Especially: 1) VLM model name/path 2) Action expert parameters (hidden_size, num_layers, num_heads) 3) chunk_size, n_action_steps 4) Flow matching parameters (num_steps, sigma) 5) Vision-related params 6) Freeze/training params 7) Class names and inheritance 8) Any references to SigLIP dimensions or token counts."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T11:17:58.265442+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T11:17:58.265570+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "google/siglip-base-patch16-512 hidden_size output_dim num_tokens config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "google/siglip-base-patch16-512 hidden_size output_dim num_tokens config"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T11:17:58.265710+00:00_

Web search results for query: "google/siglip-base-patch16-512 hidden_size output_dim num_tokens config"

Links: [{"title":"transformers/src/transformers/models/siglip/modeling_siglip.py at main · huggingface/transformers","url":"https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip/modeling_siglip.py"},{"title":"google/siglip-base-patch16-512 · Hugging Face","url":"https://huggingface.co/google/siglip-base-patch16-512"},{"title":"Siglip Base Patch16 512 · Models · Dataloop","url":"https://dataloop.ai/library/model/google_siglip-base-patch16-512/"},{"title":"SigLIP · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/siglip"},{"title":"siglip-base-patch16-512 huggingface.co api & google siglip-base-patch16-512 github AI Model - Toolify","url":"https://www.toolify.ai/ai-model/google-siglip-base-patch16-512"},{"title":"transformers/src/transformers/models/siglip/configuration_siglip.py at main · huggingface/transformers","url":"https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip/configuration_siglip.py"},{"title":"README.md · google/siglip-base-patch16-512 at main","url":"https://huggingface.co/google/siglip-base-patch16-512/blob/main/README.md"},{"title":"SigLIP2 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/siglip2"},{"title":"siglip-base-patch16-512","url":"https://bytez.com/model/google/siglip-base-patch16-512"},{"title":"siglip2-so400m-patch16-512-jax","url":"https://www.promptlayer.com/models/siglip2-so400m-patch16-512-jax"}]

Based on the search results, I found information about the google/siglip-base-patch16-512 model. Here's what I discovered regarding your query:

## Model Configuration Details

The model accepts text sequences with a maximum length of 64 tokens, which answers the `num_tokens` parameter you asked about.

However, the search results do not contain the specific configuration values for `hidden_size` and `output_dim` for the google/s
…[truncated 928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T11:17:58.265880+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/google/siglip-base-patch16-512",
  "prompt": "Extract the model's config details: hidden_size, image_size, patch_size, num_hidden_layers, num_attention_heads, intermediate_size, and the number of output tokens (image_size/patch_size)^2. What are the exact dimensions of the vision encoder output?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/google/siglip-base-patch16-512",
    "prompt": "Extract the model's config details: hidden_size, image_size, patch_size, num_hidden_layers, num_attention_heads, intermediate_size, and the number of output tokens (image_size/patch_size)^2. What are the exact dimensions of the vision encoder output?"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T11:17:58.265999+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"huggingface/lerobot\" SmolVLAPolicy \"class SmolVLA\" configuration action_expert num_layers hidden_size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"huggingface/lerobot\" SmolVLAPolicy \"class SmolVLA\" configuration action_expert num_layers hidden_size"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T11:17:58.266111+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/pull/1175",
  "prompt": "Extract key implementation details from this PR that adds SmolVLA: file paths created, class names, architecture parameters, config defaults, action expert details, and any code snippets showing the model structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/pull/1175",
    "prompt": "Extract key implementation details from this PR that adds SmolVLA: file paths created, class names, architecture parameters, config defaults, action expert details, and any code snippets showing the model structure."
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T11:17:58.266235+00:00_

# SigLIP Model Config Details

Based on the provided webpage content, **the specific configuration details (hidden_size, num_hidden_layers, num_attention_heads, intermediate_size) are not included in the page content**.

However, from the information available, I can extract:

## Available Information:

- **Model**: google/siglip-base-patch16-512
- **Image Size**: 512x512
- **Patch Size**: 16
- **Output Tokens (spatial dimensions)**: `(512/16)² = 32² = 1,024 tokens`

## What's Missing:

The following configuration parameters are **not provided** in the webpage:
- `hidden_size`
- `num_hidden_layers`
- `num_attention_heads`
- `intermediate_size`

## How to Access Complete Config:

To get the exact configuration details, you would need to:

1. **Check the model's `config.json`** file on the Hugging Face Hub
2. **Use the Transformers library**:
```python
from transformers import AutoConfig

config = AutoConfig.from_pretrained("google/siglip-base-patch16-512")
print(config)
```

3. **Check the official repository**: https://github.com/google-research/big_vision

The webpage focuses on usage examples rather than detailed architectural specifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T11:17:58.266414+00:00_

Web search results for query: ""huggingface/lerobot" SmolVLAPolicy "class SmolVLA" configuration action_expert num_layers hidden_size"

Links: [{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"lerobot/examples/tutorial/smolvla/using_smolvla_example.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/examples/tutorial/smolvla/using_smolvla_example.py"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"Training SmolVLA with LeRobot Notebook - Colab - Google","url":"https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"Bring Your Own Policies","url":"https://huggingface.co/docs/lerobot/en/bring_your_own_policies"},{"title":"phospho starter pack documentation","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"it seems that the pretrained weights for the action expert head are not being loaded for SmolVLA. · Issue #2215 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2215"}]

I found information about SmolVLAPolicy and its architecture. Let me search for more specific configuration details about the parameters you mentioned.

Links: [{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html
…[truncated 3255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T11:17:58.266609+00:00_

# SmolVLA Implementation Details

## Overview
This PR introduces SmolVLA, a compact vision-language-action model designed for robotics. The implementation enables training and inference on consumer-grade hardware.

## Key Files and Structure

The PR adds SmolVLA support across the LeRobot framework:

- **Policy Type**: `smolvla` registered in the policy factory
- **Model Architecture**: Built on SmolVLM-2 as the vision-language backbone
- **Dependencies**: Installed via `pip install -e ".[smolvla]"`

## Core Components

**Model Composition**:
- Pretrained vision-language model (SmolVLM-2)
- Action expert module for robot control predictions
- Support for multi-robot and task conditioning through text inputs

**Key Features**:
- "drastically reduces both training and inference costs"
- Trainable on single GPU setups
- Deployable on consumer-grade GPUs or CPUs
- Achieves "performance comparable to VLAs that are 10x larger"

## Training Usage

```python
# Finetune pretrained model
python lerobot/scripts/train.py \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=lerobot/svla_so100_stacking
```

## Inference

```python
policy = SmolVLAPolicy.from_pretrained("lerobot/smolvla_base")
```

## Technical Handling

Observations support both tensor and list (text) inputs. The implementation includes preprocessing logic that skips tensor-specific operations for string lists containing task descriptions and robot type identifiers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T11:17:58.266776+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/lerobot/smolvla_base/raw/main/config.json",
  "prompt": "Extract the complete JSON config showing all architecture parameters. I need: action_expert config (hidden_size, num_layers, num_heads, etc.), VLM config (model name, n_layers_to_skip), chunk_size, n_action_steps, flow matching parameters, any vision-related dimensions, and all other config values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/lerobot/smolvla_base/raw/main/config.json",
    "prompt": "Extract the complete JSON config showing all architecture parameters. I need: action_expert config (hidden_size, num_layers, num_heads, etc.), VLM config (model name, n_layers_to_skip), chunk_size, n_action_steps, flow matching parameters, any vision-related dimensions, and all other config values."
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T11:17:58.266905+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/examples/tutorial/smolvla/using_smolvla_example.py",
  "prompt": "Extract the complete code showing how SmolVLA is loaded, configured, and used. Show the imports, model loading, preprocessing, inference steps, and any configuration details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/blob/main/examples/tutorial/smolvla/using_smolvla_example.py",
    "prompt": "Extract the complete code showing how SmolVLA is loaded, configured, and used. Show the imports, model loading, preprocessing, inference steps, and any configuration details."
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T11:17:58.267024+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://learnopencv.com/smolvla-lerobot-vision-language-action-model/",
  "prompt": "Extract technical architecture details about SmolVLA: 1) SigLIP encoder specifics (hidden dimensions, output tokens). 2) SmolLM2 details (hidden size, layers). 3) Action expert details (hidden size, layers, attention structure). 4) PixelShuffle specifics (how 1024 tokens become 64). 5) Flow matching details (number of inference steps). 6) Any diagrams descriptions showing the architecture. 7) Code examples for loading/training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://learnopencv.com/smolvla-lerobot-vision-language-action-model/",
    "prompt": "Extract technical architecture details about SmolVLA: 1) SigLIP encoder specifics (hidden dimensions, output tokens). 2) SmolLM2 details (hidden size, layers). 3) Action expert details (hidden size, layers, attention structure). 4) PixelShuffle specifics (how 1024 tokens become 64). 5) Flow matching details (number of inference steps). 6) Any diagrams descriptions showing the architecture. 7) Code examples for loading/training."
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T11:17:58.267242+00:00_

# SmolVLA Configuration Extraction

## Complete JSON Config

```json
{
    "type": "smolvla",
    "n_obs_steps": 1,
    "input_features": {
        "observation.state": {
            "type": "STATE",
            "shape": [6]
        },
        "observation.images.camera1": {
            "type": "VISUAL",
            "shape": [3, 256, 256]
        },
        "observation.images.camera2": {
            "type": "VISUAL",
            "shape": [3, 256, 256]
        },
        "observation.images.camera3": {
            "type": "VISUAL",
            "shape": [3, 256, 256]
        }
    },
    "output_features": {
        "action": {
            "type": "ACTION",
            "shape": [6]
        }
    },
    "device": "cuda",
    "use_amp": false,
    "chunk_size": 50,
    "n_action_steps": 50,
    "normalization_mapping": {
        "VISUAL": "IDENTITY",
        "STATE": "MEAN_STD",
        "ACTION": "MEAN_STD"
    },
    "max_state_dim": 32,
    "max_action_dim": 32,
    "resize_imgs_with_padding": [512, 512],
    "vlm_model_name": "HuggingFaceTB/SmolVLM2-500M-Video-Instruct",
    "load_vlm_weights": true,
    "num_vlm_layers": 16,
    "num_expert_layers": 0,
    "self_attn_every_n_layers": 2,
    "expert_width_multiplier": 0.75,
    "attention_mode": "cross_attn",
    "prefix_length": 0,
    "optimizer_lr": 0.0001,
    "optimizer_betas": [0.9, 0.95],
    "optimizer_eps": 1e-08,
    "optimizer_weight_decay": 1e-10,
    "optimizer_grad_clip_norm": 10,
    "scheduler_warmup_steps": 1000,
    "scheduler_decay_steps": 30000,
    "scheduler_decay_lr": 2.5e-06,
    "min_period": 0.004,
    "max_period": 4.0,
    "num_steps": 10,
    "use_cache": true,
    "freeze_vision_encoder": true,
    "train_expert_only": true,
    "train_state_proj": true
}
```

## Key Architecture Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Action Output** | 6-dim | 6 DOF robot action |
| **State Input** | 6-dim | Robot state (joint positions) |
| **Vision Input** | 3×256×
…[truncated 810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T11:17:58.267417+00:00_

# SmolVLA Loading and Usage

## Imports
The code imports key components:
```python
import torch
from lerobot.policies import make_pre_post_processors
from lerobot.policies.smolvla import SmolVLAPolicy
from lerobot.policies.utils import build_inference_frame, make_robot_action
```

## Model Loading
"model = SmolVLAPolicy.from_pretrained(model_id)" where model_id references "lerobot/smolvla_base". This loads a pretrained policy from the Hub.

## Preprocessing Configuration
The code establishes preprocessing and postprocessing functions via "make_pre_post_processors(model.config, model_id, preprocessor_overrides=...)" to handle device compatibility and data normalization.

## Inference Loop
During each inference step:
1. Obtain robot observations via "robot.get_observation()"
2. Build an inference frame using "build_inference_frame(observation=obs, ds_features=dataset_features, device=device, task=task, robot_type=robot_type)"
3. Apply preprocessing transformations
4. Execute "model.select_action(obs)" to generate predictions
5. Apply postprocessing and convert to robot-compatible format using "make_robot_action()"
6. Send commands via "robot.send_action(action)"

## Configuration Details
Camera specifications must match training data. The example uses two OpenCV cameras at 640x480 resolution, 30 fps. Device placement (MPS/CUDA/CPU) is configurable.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T11:17:58.267599+00:00_

# SmolVLA Technical Architecture Details

Based on the provided content, here's what's explicitly documented:

## Available Architecture Details

**Model Size & Parameters:**
- "approximately **450 million parameters**" - notably compact compared to larger VLA models
- 100M learnable parameters during fine-tuning
- 16 VLM layers (reduced from full model)

**Vision Backbone:**
- Uses **SigLIP** for visual feature encoding
- Processes images at **512×512 pixels** globally
- **PixelShuffle** reduces visual tokens to approximately **64 per image**
- No specific hidden dimensions provided in the article

**Language Model:**
- **SmolLM2** component processes textual instructions
- **Layer skipping** uses features from intermediate layer (~L/2) rather than final layer
- 16 total VLM layers in deployed version
- No hidden size specifications disclosed

**Action Expert:**
- Uses **flow matching** approach for action generation
- Employs **linear projection layers** as dimensional adapters
- Interleaved attention for smooth kinematics
- Exact architecture specs (hidden dimensions, layer count) not detailed

**Inference Optimization:**
- Asynchronous inference reduces latency between action predictions
- Typical inference time: "**0.086982 seconds**" (mentioned in code example)

## Notable Gaps

The article lacks specific technical details on:
- SigLIP hidden dimensions and output token counts
- SmolLM2 exact layer configuration and hidden sizes
- Action expert layer architecture
- Flow matching inference step counts
- Complete architectural diagrams with numerical specifications

The focus emphasizes accessibility over exhaustive technical documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T11:17:58.267780+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct/raw/main/config.json",
  "prompt": "Extract the model config: hidden_size, num_hidden_layers, num_attention_heads, intermediate_size, vocab_size, and any other architectural parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct/raw/main/config.json",
    "prompt": "Extract the model config: hidden_size, num_hidden_layers, num_attention_heads, intermediate_size, vocab_size, and any other architectural parameters."
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-15T11:17:58.267906+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/google/siglip-base-patch16-512/raw/main/config.json",
  "prompt": "Extract vision_config parameters: hidden_size, num_hidden_layers, num_attention_heads, intermediate_size, image_size, patch_size. Calculate the number of output tokens: (image_size/patch_size)^2."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/google/siglip-base-patch16-512/raw/main/config.json",
    "prompt": "Extract vision_config parameters: hidden_size, num_hidden_layers, num_attention_heads, intermediate_size, image_size, patch_size. Calculate the number of output tokens: (image_size/patch_size)^2."
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T11:17:58.268032+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot training script entry point \"lerobot-train\" \"lerobot/scripts/train.py\" main function"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot training script entry point \"lerobot-train\" \"lerobot/scripts/train.py\" main function"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T11:17:58.268162+00:00_

# Model Configuration Extraction

## Primary Architectural Parameters

| Parameter | Value |
|-----------|-------|
| **hidden_size** | 960 |
| **num_hidden_layers** | 32 |
| **num_attention_heads** | 15 |
| **intermediate_size** | 2560 |
| **vocab_size** | 49,152 |

## Additional Architectural Details

**Attention Configuration:**
- `num_key_value_heads`: 5 (grouped query attention)
- `attention_bias`: false
- `attention_dropout`: 0.0

**Activation & Normalization:**
- `hidden_act`: silu (Swish Linear Unit)
- `rms_norm_eps`: 1e-05

**Positional Encoding:**
- `max_position_embeddings`: 8,192
- `rope_theta`: 100,000
- `rope_interleaved`: false
- `rope_scaling`: null (no scaling)

**Model Type & Framework:**
- `model_type`: llama
- `architectures`: LlamaForCausalLM
- `torch_dtype`: bfloat16
- `transformers_version`: 4.42.3

**Token IDs:**
- `bos_token_id`: 1
- `eos_token_id`: 2
- `pad_token_id`: 2

**Other Settings:**
- `use_cache`: true (KV cache enabled)
- `tie_word_embeddings`: true
- `mlp_bias`: false
- `pretraining_tp`: 1

This is a **Llama-based model** with 960-dimensional embeddings, 32 transformer layers, and grouped query attention (15 query heads / 5 key-value heads).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T11:17:58.268308+00:00_

# SigLIP Vision Config Analysis

Based on the provided configuration, here's what I can extract:

## Available Parameters

From the `vision_config`:
- **image_size**: 512
- **model_type**: siglip_vision_model

## Missing Parameters

The following parameters are **not present** in the provided configuration:
- `hidden_size`
- `num_hidden_layers`
- `num_attention_heads`
- `intermediate_size`
- `patch_size`

## Notes

To calculate the number of output tokens using the formula `(image_size/patch_size)²`, you would need the `patch_size` parameter. For example:

```python
# Example calculation (requires patch_size)
image_size = 512
patch_size = 16  # typical value, not provided in config

num_output_tokens = (image_size / patch_size) ** 2
# num_output_tokens = (512 / 16)² = 32² = 1,024 tokens
```

## Recommendation

The provided JSON configuration appears to be a minimal version. To access the complete vision configuration parameters, you may need to:
1. Check the full model config file (typically `config.json` in the model repository)
2. Load the full model configuration via Hugging Face transformers:

```python
from transformers import AutoConfig

config = AutoConfig.from_pretrained("google/siglip-base-patch16-512")
vision_config = config.vision_config
print(vision_config)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T11:17:58.268586+00:00_

Web search results for query: "lerobot training script entry point "lerobot-train" "lerobot/scripts/train.py" main function"

Links: [{"title":"Imitation Learning on Real-World Robots · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/il_robots"},{"title":"Training and Evaluation | huggingface/lerobot | DeepWiki","url":"https://deepwiki.com/huggingface/lerobot/3-training-and-evaluation"},{"title":"Getting Started with Real-World Robots","url":"https://huggingface.co/docs/lerobot/en/getting_started_real_world_robot"},{"title":"lerobot · PyPI","url":"https://pypi.org/project/lerobot/"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"GitHub - mytechnotalent/lerobot: Train a robot brain from zero to 100% success in 60 seconds flat — no hardware, pure NumPy, pure magic. Built on HuggingFace LeRobot standards.","url":"https://github.com/mytechnotalent/lerobot"},{"title":"LeRobot Imitation Learning for OMX | ROBOTIS","url":"https://ai.robotis.com/omx/lerobot_imitation_learning_omx"},{"title":"fourier-lerobot/examples/4_train_policy_with_script.md at main · FFTAI/fourier-lerobot","url":"https://github.com/FFTAI/fourier-lerobot/blob/main/examples/4_train_policy_with_script.md"},{"title":"lerobot/docs/source/il_robots.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/il_robots.mdx"},{"title":"LeRobot SO-ARM100 Train Guide – AIFITLAB","url":"https://aifitlab.com/blogs/tech-blogs/lerobot-so-arm100-train-guide"}]

Based on the search results, here's what I found about the LeRobot training script entry point:

## Training Script Entry Points

LeRobot provides two ways to run the training script:

1. **Command-line entry point**: To train a policy to control your robot, use the lerobot-train script.

2. **Direct Python script**: You can also use the python lerobot/scripts/train.py script.

## M
…[truncated 601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T11:17:58.268943+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/1995",
  "prompt": "Extract any technical details about SmolVLA's architecture discussed in this issue, especially: num_expert_layers meaning, how action expert layers work, cross-attention structure, and any code references or explanations from maintainers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/issues/1995",
    "prompt": "Extract any technical details about SmolVLA's architecture discussed in this issue, especially: num_expert_layers meaning, how action expert layers work, cross-attention structure, and any code references or explanations from maintainers."
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-15T11:17:58.269161+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://deepwiki.com/huggingface/lerobot/3-training-and-evaluation",
  "prompt": "Extract: 1) Training pipeline architecture (DataLoader, Trainer, training loop steps). 2) Data format and loading (LeRobotDataset structure, how episodes are stored). 3) Entry point for training (train.py or lerobot-train). 4) How policies are registered and loaded. 5) Multi-GPU training support. 6) Any configuration system details (draccus, YAML, CLI args)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://deepwiki.com/huggingface/lerobot/3-training-and-evaluation",
    "prompt": "Extract: 1) Training pipeline architecture (DataLoader, Trainer, training loop steps). 2) Data format and loading (LeRobotDataset structure, how episodes are stored). 3) Entry point for training (train.py or lerobot-train). 4) How policies are registered and loaded. 5) Multi-GPU training support. 6) Any configuration system details (draccus, YAML, CLI args)."
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T11:17:58.269353+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LeRobot dataset format parquet episodes structure observation action 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LeRobot dataset format parquet episodes structure observation action 2025"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T11:17:58.269576+00:00_

# SmolVLA Architecture Technical Details from Issue #1995

Based on the GitHub issue, here are the technical concerns raised about SmolVLA's design:

## Cross-Attention Structure
The issue questions whether linear projections of VLM keys and values in the cross-attention layer are necessary. The author notes: "They have compatible shape without the projection, and ROPE is not applied after the projection."

## Embedding Scaling
SmolVLA multiplies image and text embeddings by `sqrt(dim)` before feeding them to LLM and expert layers—a step not found in the original SmolVLM implementation, potentially altering feature distribution.

## Positional Encoding Differences
SmolVLA uses a ROPE max frequency of 10,000, differing from SmolVLM's 100,000, which could affect position encoding effectiveness.

## Attention Masking
Unlike SmolVLM's causal masking across all layers, SmolVLA implements attention patterns similar to PaliGemma, allowing bidirectional attention for images.

**Note:** The issue was closed as "not planned," and no maintainer responses explaining these architectural choices are visible in the provided content. The `num_expert_layers` parameter and specific expert layer mechanics are mentioned in the issue title but not detailed in the discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-15T11:17:58.269826+00:00_

# LeRobot Training and Evaluation Architecture

## 1. Training Pipeline Architecture

The training pipeline centers on the `train()` function in `lerobot_train.py`. It uses Hugging Face's `Accelerator` for device management and multi-GPU support. The core loop calls `update_policy()` for each batch, which performs:

- Forward pass through the policy inside `accelerator.autocast()` for mixed precision
- Backward pass via `accelerator.backward(loss)`
- Gradient clipping when configured
- Learning rate scheduler steps at every batch (not epoch-based)
- Optional `policy.update()` calls for techniques like EMA

The training loop includes periodic checkpointing, metric logging to WandB, and mid-training evaluation when an environment is configured.

## 2. Data Format and Loading

The system uses `LeRobotDataset` to manage episode data. While the document references this structure, specific details about episode storage format are documented in the "LeRobotDataset" section. Training consumes batches from a DataLoader created via factory functions that instantiate both the dataset and corresponding processors.

## 3. Entry Points for Training

Two CLI commands govern the workflow:

- **`lerobot-train`**: Main supervised training via `TrainPipelineConfig`
- **`lerobot-eval`**: Independent evaluation using `EvalPipelineConfig`

Both commands accept configuration through command-line arguments that override a root dataclass config.

## 4. Policy Registration and Loading

Policies are instantiated through factory functions: `make_policy()` creates and device-places policies, while `make_pre_post_processors()` constructs normalization pipelines. If `--policy.path` is set, the configuration loads from that checkpoint and sets `pretrained_path` automatically during validation.

## 5. Multi-GPU Training Support

The framework integrates Hugging Face `Accelerate` for distributed training. The document mentions DDP configuration and multi-process launch are covered in the "Multi-GPU 
…[truncated 422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T11:17:58.270102+00:00_

Web search results for query: "LeRobot dataset format parquet episodes structure observation action 2025"

Links: [{"title":"LeRobot Dataset Format","url":"https://docs.phospho.ai/learn/lerobot-dataset"},{"title":"LeRobotDataset v3.0 · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3"},{"title":"`LeRobotDataset:v3.0`: Bringing large-scale datasets to `lerobot`","url":"https://huggingface.co/blog/lerobot-datasets-v3"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LeRobotDataset | huggingface/lerobot | DeepWiki","url":"https://deepwiki.com/huggingface/lerobot/2-core-concepts"},{"title":"Unit 2: Understand the LeRobot Dataset Format — LeRobot Learning Path | SVRC Academy","url":"https://www.roboticscenter.ai/learn/paths/lerobot/unit-2-explore-datasets"},{"title":"Getting Started with LeRobot | ReductStore","url":"https://www.reduct.store/blog/hugging-face-lerobot"},{"title":"Dataset Engineering, Training, and Inference Experiments on a “Low-Cost” Arm using LeRobot V3 | by Heyang Huang | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/behind-a-failed-robot-learning-project-dataset-engineering-training-and-inference-efc1c2bd10e8"},{"title":"Porting Large Datasets to LeRobot Dataset v3.0","url":"https://huggingface.co/docs/lerobot/en/porting_datasets_v3"},{"title":"LeRobotDataset v3.0","url":"https://huggingface.co/docs/lerobot/main/en/lerobot-dataset-v3"}]

Based on the web search results, here's comprehensive information about the LeRobot dataset format:

## Overview

LeRobotDataset v3.0 is a standardized format for robot learning data that provides unified access to multi-modal time-series data, sensorimotor signals and multi-camera video, as well as rich metadata for indexing, search, and visualization on the Hugging Face Hub.

## Storage Structure

A core v3 principle is decoupling storage from 
…[truncated 2012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T11:17:58.270394+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct/raw/main/config.json",
  "prompt": "Extract all config parameters, especially: 1) vision_config (hidden_size, num_hidden_layers, image_size, patch_size, num_attention_heads). 2) text_config (hidden_size, num_hidden_layers, num_attention_heads, intermediate_size). 3) Any connector/projection config. 4) The model_type. 5) Any pixel shuffle parameters. List all key-value pairs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct/raw/main/config.json",
    "prompt": "Extract all config parameters, especially: 1) vision_config (hidden_size, num_hidden_layers, image_size, patch_size, num_attention_heads). 2) text_config (hidden_size, num_hidden_layers, num_attention_heads, intermediate_size). 3) Any connector/projection config. 4) The model_type. 5) Any pixel shuffle parameters. List all key-value pairs."
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-15T11:17:58.270609+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot SmolVLA freeze backbone train_expert_only gradient checkpointing data loading"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot SmolVLA freeze backbone train_expert_only gradient checkpointing data loading"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-15T11:17:58.270812+00:00_

# SmolVLM Configuration Parameters

## Model Type
- **model_type**: `smolvlm`
- **Architecture**: `SmolVLMForConditionalGeneration`

---

## Vision Config
```json
{
  "hidden_size": 768,
  "image_size": 512,
  "num_attention_heads": 12,
  "patch_size": 16,
  "model_type": "smolvlm_vision",
  "tie_word_embeddings": false,
  "use_base_siglip": false,
  "max_image_size": {
    "longest_edge": 512
  },
  "size": {
    "longest_edge": 2048
  }
}
```

---

## Text Config
```json
{
  "architectures": ["VLlama3ForCausalLM"],
  "hidden_size": 960,
  "num_hidden_layers": 32,
  "num_attention_heads": 15,
  "num_key_value_heads": 5,
  "intermediate_size": 2560,
  "head_dim": 64,
  "max_position_embeddings": 8192,
  "vocab_size": 49280,
  "model_type": "llama",
  "torch_dtype": "bfloat16",
  "_flash_attn_2_enabled": true,
  "rms_norm_eps": 1e-05,
  "rope_theta": 100000,
  "rope_interleaved": false,
  "qk_layer_norms": false,
  "use_resampler": false,
  "pad_token_id": 2
}
```

---

## Connector/Projection Config (Perceiver)
```json
{
  "resampler_depth": 6,
  "resampler_n_heads": 16,
  "resampler_n_latents": 64,
  "resampler_head_dim": 96,
  "qk_layer_norms_perceiver": false
}
```

---

## Pixel Shuffle Parameters
- **pixel_shuffle_factor**: `4`
- **scale_factor**: `4`

---

## Special Tokens
- **image_token_id**: `49190`
- **pad_token_id**: `128002`

---

## Additional Parameters
- **transformers_version**: `4.47.1`
- **use_cache**: `false`
- **use_reentrant_checkpointing**: `false`
- **tie_word_embeddings**: `false`
- **torch_dtype**: `float32` (global)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T11:17:58.271044+00:00_

Web search results for query: "lerobot SmolVLA freeze backbone train_expert_only gradient checkpointing data loading"

Links: [{"title":"Release 0.6.0 · Issue #3134 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3134"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"π₀ (Pi0) · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/pi0"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task","url":"https://huggingface.co/docs/lerobot/en/xvla"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"}]

Based on the web search results, here's what I found regarding your query about LeRobot SmolVLA with the parameters you mentioned:

## Key Findings:

**Gradient Checkpointing for SmolVLA:**
Gradient checkpointing is noted as a feature that is currently only available on Pi0 and XVLA models, with plans to extend to all policies including SmolVLA.

**train_expert_only Parameter:**
Setting `train_expert_only=true` freezes the VLM and trains only the action expert and projections, allowing finetuning with reduced memory usage. This parameter is documented in the context of the Pi0 policy training.

**Freeze Ba
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-15T11:17:58.271362+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T11:17:58.271579+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T11:17:58.271815+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_smolvla_lerobot.md",
  "content": "# SmolVLA + LeRobot 调研报告\n\n## 1. SmolVLA 模型架构\n\n### 1.1 整体架构\n\nSmolVLA 是 HuggingFace 发布的 450M 参数 Vision-Language-Action 模型，由两个核心组件组成：\n\n1. **Vision-Language Model (VLM)**: SmolVLM2-500M-Video-Instruct（基于 Idefics3 架构）\n2. **Action Expert**: ~100M 参数的 flow matching transformer\n\n```\nInput Images → SigLIP Vision Encoder → PixelShuffle → Linear Proj → SmolLM2 (16 layers) → VLM Features\n                                                                                              ↓\nLanguage Instruction → Tokenizer → SmolLM2 Embedding ─────────────────────────────────────────┘\n                                                                                              ↓\nRobot State → Linear Proj (state_proj) ──────────────────────────────────────────────── Cross-Attn\n                                                                                              ↓\n                                                                     Action Expert (interleaved CA + SA)\n                                                                              ↓\n                                                                     Flow Matching → Action Chunk (50 steps)\n```\n\n### 1.2 Vision Encoder (SigLIP)\n\n| 参数 | 值 |\n|------|-----|\n| 模型 | SigLIP-Base (google/siglip-base-patch16-512) |\n| hidden_size | **768** |\n| image_size | 512×512 |\n| patch_size | 16 |\n| num_attention_heads | 12 |\n| 原始输出 tokens | (512/16)² = **1024 tokens** |\n| PixelShuffle factor | 4 |\n| PixelShuffle 后 tokens | 1024 / 4² = **64 tokens per frame** |\n| PixelShuffle 后 channel dim | 768 × 4² = 12288 → Linear Proj → 960 (匹配 LLM hidden_size) |\n\n**关键结论**: 每张 512×512 图片经 SigLIP + PixelShuffle 后产出 **64 tokens × 960 dim** 送入 LLM。\n\n### 1.3 Language Model (SmolLM2-360M)\n\n| 参数 | 值 |\n|------|-----|\n| 架构 | VLlama3ForCausalLM (类 Llama) |\n| hidden_size | **960** |\n| num_hidden_layers | 32 (SmolVLA 只用前 **16 层**) |\n| num_attention_heads | 15 |\n| num_key_value_heads | 5 (GQA) |\n| intermediate_size | 2560 |\n| vocab_size | 49280 |\n| activation | SiLU |\n| position encoding | RoPE (theta=100000) |\n| max_position_embeddings | 8192 |\n\n### 1.4 Action Expert\n\n| 参数 | 值 |\n|------|-----|\n| 参数量 | ~100M |\n| hidden_dim | 0.75 × 960 = **720** |\n| 层结构 | 与 VLM 层交错的 cross-attn + self-attn |\n| self_attn_every_n_layers | 2（每 2 层一个 self-attn，其余为 cross-attn） |\n| num_expert_layers | 0 (config 中为 0，表示 expert 与 VLM 层交织运行) [UNVERIFIED - 具体含义需看源码] |\n| attention_mode | cross_attn |\n| 训练目标 | Flow Matching (conditional) |\n| action chunk_size | **50** |\n| n_action_steps | **50** |\n| 推理 denoising steps | **10** |\n| noise schedule | log-normal, min_period=0.004, max_period=4.0 |\n\n### 1.5 SmolVLA Config (完整)\n\n```json\n{\n    \"type\": \"smolvla\",\n    \"n_obs_steps\": 1,\n    \"chunk_size\": 50,\n    \"n_action_steps\": 50,\n    \"max_state_dim\": 32,\n    \"max_action_dim\": 32,\n    \"resize_imgs_with_padding\": [512, 512],\n    \"vlm_model_name\": \"HuggingFaceTB/SmolVLM2-500M-Video-Instruct\",\n    \"load_vlm_weights\": true,\n    \"num_vlm_layers\": 16,\n    \"num_expert_layers\": 0,\n    \"self_attn_every_n_layers\": 2,\n    \"expert_width_multiplier\": 0.75,\n    \"attention_mode\": \"cross_attn\",\n    \"num_steps\": 10,\n    \"freeze_vision_encoder\": true,\n    \"train_expert_only\": true,\n    \"train_state_proj\": true,\n    \"optimizer_lr\": 1e-4,\n    \"optimizer_betas\": [0.9, 0.95],\n    \"scheduler_warmup_steps\": 1000,\n    \"scheduler_decay_steps\": 30000,\n    \"scheduler_decay_lr\": 2.5e-6\n}\n```\n\n### 1.6 HuggingFace 模型权重\n\n| 模型 | HF Repo |\n|------|---------|\n| SmolVLA Base (预训练) | `lerobot/smolvla_base` |\n| VLM Backbone | `HuggingFaceTB/SmolVLM2-500M-Video-Instruct` |\n\n### 1.7 模型加载方式\n\n```python\nimport torch\nfrom lerobot.policies.smolvla import SmolVLAPolicy\nfrom lerobot.policies.factory import make_pre_post_processors\n\n# 加载 policy\npolicy = SmolVLAPolicy.from_pretrained(\"lerobot/smolvla_base\").to(\"cuda\").eval()\n\n# 创建 preprocessor/postprocessor\npreprocess, postprocess = make_pre_post_processors(\n    policy.config,\n    \"lerobot/smolvla_base\",\n    preprocessor_overrides={\"device_processor\": {\"device\": \"cuda\"}},\n)\n\n# 推理\nbatch = preprocess(observation_dict)\nwith torch.inference_mode():\n    action = policy.select_action(batch)\n    action = postprocess(action)\n```\n\n---\n\n## 2. LeRobot 框架\n\n### 2.1 基本信息\n\n| 项目 | 信息 |\n|------|------|\n| GitHub | https://github.com/huggingface/lerobot |\n| 版本 | 0.5.2 |\n| License | Apache-2.0 |\n| 构建系统 | setuptools (pyproject.toml) |\n\n### 2.2 Fine-tuning Pipeline\n\n#### 训练脚本入口\n\n```bash\n# CLI 方式（推荐）\nlerobot-train --policy.path=lerobot/smolvla_base --dataset.repo_id=user/dataset ...\n\n# Python 方式\npython lerobot/scripts/train.py ...\n```\n\n#### 配置系统\n\n- 使用 `draccus` 库（dataclass-based config）\n- 根配置类: `TrainPipelineConfig`\n- 所有参数通过 CLI 覆盖: `--policy.xxx`, `--dataset.xxx`, `--batch_size` 等\n- 无 YAML 配置文件，全部通过 CLI + dataclass 默认值\n\n#### 训练命令示例\n\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=${HF_USER}/mydataset \\\n  --batch_size=64 \\\n  --steps=20000 \\\n  --output_dir=outputs/train/my_smolvla \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16 \\\n  --wandb.enable=true\n```\n\n#### 训练循环核心\n\n```python\n# 内部结构（简化）\nfrom accelerate import Accelerator\n\naccelerator = Accelerator(mixed_precision=\"bf16\")\npolicy = make_policy(config)\noptimizer = make_optimizer(policy, config)\ndataloader = make_dataloader(dataset, config)\n\nfor step, batch in enumerate(dataloader):\n    batch = preprocess(batch)\n    with accelerator.autocast():\n        loss, outputs = policy.forward(batch)\n    accelerator.backward(loss)\n    optimizer.step()\n    scheduler.step()\n```\n\n### 2.3 SmolVLA 在 LeRobot 中的位置\n\n#### Policy 类名和路径\n\n```\nlerobot/policies/smolvla/\n├── __init__.py            # 导出 SmolVLAPolicy\n├── modeling_smolvla.py    # SmolVLAPolicy 主类\n└── configuration_smolvla.py  # SmolVLAConfig 配置类\n```\n\n- **Policy 类**: `lerobot.policies.smolvla.SmolVLAPolicy`\n- **Config 类**: `lerobot.policies.smolvla.SmolVLAConfig` [UNVERIFIED - 具体类名可能不同]\n- **Policy type 注册名**: `\"smolvla\"`\n\n#### 关键方法\n\n| 方法 | 作用 |\n|------|------|\n| `SmolVLAPolicy.from_pretrained(model_id)` | 从 HF Hub 加载预训练权重 |\n| `policy.forward(batch)` | 训练时前向传播，返回 (loss, outputs) |\n| `policy.select_action(batch)` | 推理时生成 action chunk |\n| `make_pre_post_processors()` | 创建数据预处理/后处理 pipeline |\n\n### 2.4 冻结 Backbone 机制\n\n#### 方式 1: Config 参数控制（默认行为）\n\n```bash\n# SmolVLA 默认 config（已内置）\n--policy.freeze_vision_encoder=true   # 冻结 SigLIP\n--policy.train_expert_only=true       # 只训练 action expert\n--policy.train_state_proj=true        # 也训练 state projection\n```\n\n默认 fine-tuning 时：\n- SigLIP vision encoder: **冻结**\n- SmolLM2 语言模型层: **冻结**（train_expert_only=true 时）\n- Action expert: **可训练**\n- State projection: **可训练**\n\n#### 方式 2: PEFT/LoRA（参数高效微调）\n\n```bash\npip install \"lerobot[peft]\"  # 安装 PEFT 依赖\n\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --peft.method_type=LORA \\\n  --peft.r=64 \\\n  --policy.optimizer_lr=1e-3 \\\n  --steps=100000 \\\n  --batch_size=32\n```\n\n**LoRA 默认 target modules**: `q_proj`, `v_proj` (LM expert) + `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`\n\n**自定义 target**:\n```bash\n--peft.target_modules='(model\\.vlm_with_expert\\.lm_expert\\..*\\.(down|gate|up)_proj|.*\\.(state_proj|action_in_proj|action_out_proj))'\n```\n\n**指定模块全量微调**（不用 LoRA）:\n```bash\n--peft.full_training_modules=[\"state_proj\"]\n```\n\n### 2.5 数据加载流程\n\n#### LeRobotDataset v3.0 格式\n\n```\ndataset_repo/\n├── data/\n│   └── chunk-000/\n│       └── file_000.parquet    # 多 episode 的帧级数据（state, action, timestamp）\n├── videos/\n│   └── camera1/\n│       └── chunk-000/\n│           └── file_000.mp4    # 多 episode 视频\n└── meta/\n    ├── info.json               # 数据集元信息\n    ├── stats.json              # 归一化统计量\n    ├── tasks.parquet           # 任务描述\n    └── episodes/\n        └── chunk-000/\n            └── file_000.parquet  # Episode 索引\n```\n\n#### 数据字段\n\n- **observation.state**: 机器人关节状态 (shape: [6] for SO100)\n- **observation.images.camera1**: 图像帧 (shape: [3, H, W])\n- **action**: 机器人动作 (shape: [6] for SO100)\n- **timestamp**: 时间戳\n- **episode_index**: Episode 编号\n- **task**: 任务文本描述\n\n#### DataLoader 结构\n\n```python\nfrom lerobot.datasets.lerobot_dataset import LeRobotDataset\n\n# 从 HF Hub 加载\ndataset = LeRobotDataset(\"user/dataset_name\")\n\n# 访问单帧\nframe = dataset[0]\n# → {\"observation.state\": tensor, \"observation.images.camera1\": tensor, \"action\": tensor, ...}\n\n# 内部使用标准 PyTorch DataLoader\ndataloader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True)\n```\n\n#### 归一化\n\n- **VISUAL**: IDENTITY（不归一化，图像已是 [0,1]）\n- **STATE**: MEAN_STD 归一化\n- **ACTION**: MEAN_STD 归一化\n- 统计量存储在 `meta/stats.json`\n\n---\n\n## 3. 依赖清单\n\n### 3.1 核心依赖\n\n| 包 | 版本要求 | 说明 |\n|----|---------|------|\n| Python | **>=3.12** | 必须 3.12+ |\n| torch | **>=2.7, <2.12.0** | PyTorch |\n| torchvision | >=0.22.0, <0.27.0 | |\n| transformers | **>=5.4.0, <5.6.0** | HF Transformers (注意是 5.x!) |\n| accelerate | **>=1.10.0, <2.0.0** | 多 GPU / 混合精度 |\n| numpy | >=2.0.0, <2.3.0 | |\n| einops | >=0.8.0, <0.9.0 | |\n| safetensors | >=0.4.3, <1.0.0 | 权重格式 |\n| huggingface-hub | >=1.0.0, <2.0.0 | Hub 交互 |\n| draccus | ==0.10.0 | 配置系统 |\n| peft | >=0.18.0, <1.0.0 | LoRA 支持 |\n| wandb | >=0.24.0, <0.25.0 | 实验跟踪 |\n\n### 3.2 SmolVLA 专属依赖\n\n安装方式: `pip install -e \".[smolvla]\"` 或 `pip install \"lerobot[smolvla]\"`\n\n包含 transformers + peft 等 VLM 相关依赖。\n\n### 3.3 其他可选依赖组\n\n| Group | 主要包 |\n|-------|--------|\n| `datasets` | datasets, pandas, pyarrow, av, torchcodec |\n| `diffusion` | diffusers >=0.27.2, <0.36.0 |\n| `dev` | pytest, pre-commit, ruff, mypy |\n\n### 3.4 安装大小预估\n\n| 组件 | 大小 |\n|------|------|\n| PyTorch (CUDA 12.x) | ~2.5 GB |\n| transformers + tokenizers | ~500 MB |\n| lerobot + 依赖 | ~200 MB |\n| SmolVLA 模型权重 (smolvla_base) | ~900 MB (450M params × bf16) |\n| SmolVLM2-500M (首次加载时下载) | ~1 GB |\n| **总计预估** | **~5 GB** |\n\n### 3.5 安装命令\n\n```bash\n# 基础安装\npip install lerobot\n\n# SmolVLA 完整支持\npip install \"lerobot[smolvla]\"\n\n# 开发模式\ngit clone https://github.com/huggingface/lerobot.git\ncd lerobot\npip install -e \".[smolvla]\"\n```\n\n---\n\n## 4. 关键文件路径（LeRobot repo 中）\n\n```\nlerobot/\n├── lerobot/\n│   ├── policies/\n│   │   ├── smolvla/\n│   │   │   ├── __init__.py\n│   │   │   ├── modeling_smolvla.py      # SmolVLAPolicy 主类\n│   │   │   └── configuration_smolvla.py # 配置类\n│   │   ├── factory.py                   # make_policy(), make_pre_post_processors()\n│   │   └── utils.py                     # build_inference_frame(), make_robot_action()\n│   ├── scripts/\n│   │   └── train.py                     # lerobot-train 入口（或 lerobot_train.py）\n│   ├── datasets/\n│   │   └── lerobot_dataset.py           # LeRobotDataset 类\n│   └── configs/                         # TrainPipelineConfig 等 [UNVERIFIED 具体路径]\n├── examples/\n│   └── tutorial/smolvla/\n│       └── using_smolvla_example.py     # 使用示例\n├── docs/\n│   └── source/\n│       ├── smolvla.mdx\n│       └── peft_training.mdx\n└── pyproject.toml                       # 依赖定义\n```\n\n---\n\n## 5. 对我们项目的关键观察\n\n### 适合做 Information Bottleneck 的切入点\n\n1. **Vision Encoder 输出层**：SigLIP → PixelShuffle 后的 64 tokens (960-dim)，这是一个天然的 bottleneck 位置\n2. **VLM Layer 16 输出**：VLM 只用前 16 层的输出送给 action expert，这层的 representation 是 action-conditioning 的核心\n3. **Action Expert 的 Cross-Attention**：action tokens attend to VLM features，可以在这里施加信息约束\n4. **State Projection**：单 token 通过 linear projection，维度转换点\n\n### 训练效率\n\n- 默认只训练 action expert (~100M params)，VLM 冻结\n- 单 A100 上 20k steps ≈ 4 小时\n- 50 episodes 数据即可 fine-tune\n- 支持 LoRA 进一步降低训练成本\n\n### 注意事项\n\n- **transformers 版本要求 5.4+**：这是较新版本，需确认与其他依赖兼容性\n- **Python >=3.12**：不支持 3.11 及以下\n- `num_expert_layers: 0` 的具体含义需要阅读源码确认 [UNVERIFIED]\n- Action expert 的确切层数未从公开文档中明确获得 [UNVERIFIED]\n\n---\n\n## Sources\n\n- [SmolVLA Blog](https://huggingface.co/blog/smolvla)\n- [SmolVLA Paper (arXiv:2506.01844)](https://arxiv.org/abs/2506.01844)\n- [lerobot/smolvla_base Model Card](https://huggingface.co/lerobot/smolvla_base)\n- [LeRobot SmolVLA Docs](https://huggingface.co/docs/lerobot/smolvla)\n- [LeRobot PEFT Training](https://huggingface.co/docs/lerobot/peft_training)\n- [LeRobot GitHub](https://github.com/huggingface/lerobot)\n- [LeRobot pyproject.toml](https://github.com/huggingface/lerobot/blob/main/pyproject.toml)\n- [SmolVLM2-500M-Video-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct)\n- [SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct)\n- [LeRobotDataset v3.0](https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3)\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_smolvla_lerobot.md",
    "content": "# SmolVLA + LeRobot 调研报告\n\n## 1. SmolVLA 模型架构\n\n### 1.1 整体架构\n\nSmolVLA 是 HuggingFace 发布的 450M 参数 Vision-Language-Action 模型，由两个核心组件组成：\n\n1. **Vision-Language Model (VLM)**: SmolVLM2-500M-Video-Instruct（基于 Idefics3 架构）\n2. **Action Expert**: ~100M 参数的 flow matching transformer\n\n```\nInput Images → SigLIP Vision Encoder → PixelShuffle → Linear Proj → SmolLM2 (16 layers) → VLM Features\n                                                                                              ↓\nLanguage Instruction → Tokenizer → SmolLM2 Embedding ─────────────────────────────────────────┘\n                                                                                              ↓\nRobot State → Linear Proj (state_proj) ──────────────────────────────────────────────── Cross-Attn\n                                                                                              ↓\n                                                                     Action Expert (interleaved CA + SA)\n                                                                              ↓\n                                                                     Flow Matching → Action Chunk (50 steps)\n```\n\n### 1.2 Vision Encoder (SigLIP)\n\n| 参数 | 值 |\n|------|-----|\n| 模型 | SigLIP-Base (google/siglip-base-patch16-512) |\n| hidden_size | **768** |\n| image_size | 512×512 |\n| patch_size | 16 |\n| num_attention_heads | 12 |\n| 原始输出 tokens | (512/16)² = **1024 tokens** |\n| PixelShuffle factor | 4 |\n| PixelShuffle 后 tokens | 1024 / 4² = **64 tokens per frame** |\n| PixelShuffle 后 channel dim | 768 × 4² = 12288 → Linear Proj → 960 (匹配 LLM hidden_size) |\n\n**关键结论**: 每张 512×512 图片经 SigLIP + PixelShuffle 后产出 **64 tokens × 960 dim** 送入 LLM。\n\n### 1.3 Language Model (SmolLM2-360M)\n\n| 参数 | 值 |\n|------|-----|\n| 架构 | VLlama3ForCausalLM (类 Llama) |\n| hidden_size | **960** |\n| num_hidden_layers | 32 (SmolVLA 只用前 **16 层**) |\n| num_attention_heads | 15 |\n| num_key_value_heads | 5 (GQA) |\n| intermediate_size | 2560 |\n| vocab_size | 49280 |\n| activation | SiLU |\n| position encoding | RoPE (theta=100000) |\n| max_position_embeddings | 8192 |\n\n### 1.4 Action Expert\n\n| 参数 | 值 |\n|------|-----|\n| 参数量 | ~100M |\n| hidden_dim | 0.75 × 960 = **720** |\n| 层结构 | 与 VLM 层交错的 cross-attn + self-attn |\n| self_attn_every_n_layers | 2（每 2 层一个 self-attn，其余为 cross-attn） |\n| num_expert_layers | 0 (config 中为 0，表示 expert 与 VLM 层交织运行) [UNVERIFIED - 具体含义需看源码] |\n| attention_mode | cross_attn |\n| 训练目标 | Flow Matching (conditional) |\n| action chunk_size | **50** |\n| n_action_steps | **50** |\n| 推理 denoising steps | **10** |\n| noise schedule | log-normal, min_period=0.004, max_period=4.0 |\n\n### 1.5 SmolVLA Config (完整)\n\n```json\n{\n    \"type\": \"smolvla\",\n    \"n_obs_steps\": 1,\n    \"chunk_size\": 50,\n    \"n_action_steps\": 50,\n    \"max_state_dim\": 32,\n    \"max_action_dim\": 32,\n    \"resize_imgs_with_padding\": [512, 512],\n    \"vlm_model_name\": \"HuggingFaceTB/SmolVLM2-500M-Video-Instruct\",\n    \"load_vlm_weights\": true,\n    \"num_vlm_layers\": 16,\n    \"num_expert_layers\": 0,\n    \"self_attn_every_n_layers\": 2,\n    \"expert_width_multiplier\": 0.75,\n    \"attention_mode\": \"cross_attn\",\n    \"num_steps\": 10,\n    \"freeze_vision_encoder\": true,\n    \"train_expert_only\": true,\n    \"train_state_proj\": true,\n    \"optimizer_lr\": 1e-4,\n    \"optimizer_betas\": [0.9, 0.95],\n    \"scheduler_warmup_steps\": 1000,\n    \"scheduler_decay_steps\": 30000,\n    \"scheduler_decay_lr\": 2.5e-6\n}\n```\n\n### 1.6 HuggingFace 模型权重\n\n| 模型 | HF Repo |\n|------|---------|\n| SmolVLA Base (预训练) | `lerobot/smolvla_base` |\n| VLM Backbone | `HuggingFaceTB/SmolVLM2-500M-Video-Instruct` |\n\n### 1.7 模型加载方式\n\n```python\nimport torch\nfrom lerobot.policies.smolvla import SmolVLAPolicy\nfrom lerobot.policies.factory import make_pre_post_processors\n\n# 加载 policy\npolicy = SmolVLAPolicy.from_pretrained(\"lerobot/smolvla_base\").to(\"cuda\").eval()\n\n# 创建 preprocessor/postprocessor\npreprocess, postprocess = make_pre_post_processors(\n    policy.config,\n    \"lerobot/smolvla_base\",\n    preprocessor_overrides={\"device_processor\": {\"device\": \"cuda\"}},\n)\n\n# 推理\nbatch = preprocess(observation_dict)\nwith torch.inference_mode():\n    action = policy.select_action(batch)\n    action = postprocess(action)\n```\n\n---\n\n## 2. LeRobot 框架\n\n### 2.1 基本信息\n\n| 项目 | 信息 |\n|------|------|\n| GitHub | https://github.com/huggingface/lerobot |\n| 版本 | 0.5.2 |\n| License | Apache-2.0 |\n| 构建系统 | setuptools (pyproject.toml) |\n\n### 2.2 Fine-tuning Pipeline\n\n#### 训练脚本入口\n\n```bash\n# CLI 方式（推荐）\nlerobot-train --policy.path=lerobot/smolvla_base --dataset.repo_id=user/dataset ...\n\n# Python 方式\npython lerobot/scripts/train.py ...\n```\n\n#### 配置系统\n\n- 使用 `draccus` 库（dataclass-based config）\n- 根配置类: `TrainPipelineConfig`\n- 所有参数通过 CLI 覆盖: `--policy.xxx`, `--dataset.xxx`, `--batch_size` 等\n- 无 YAML 配置文件，全部通过 CLI + dataclass 默认值\n\n#### 训练命令示例\n\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=${HF_USER}/mydataset \\\n  --batch_size=64 \\\n  --steps=20000 \\\n  --output_dir=outputs/train/my_smolvla \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16 \\\n  --wandb.enable=true\n```\n\n#### 训练循环核心\n\n```python\n# 内部结构（简化）\nfrom accelerate import Accelerator\n\naccelerator = Accelerator(mixed_precision=\"bf16\")\npolicy = make_policy(config)\noptimizer = make_optimizer(policy, config)\ndataloader = make_dataloader(dataset, config)\n\nfor step, batch in enumerate(dataloader):\n    batch = preprocess(batch)\n    with accelerator.autocast():\n        loss, outputs = policy.forward(batch)\n    accelerator.backward(loss)\n    optimizer.step()\n    scheduler.step()\n```\n\n### 2.3 SmolVLA 在 LeRobot 中的位置\n\n#### Policy 类名和路径\n\n```\nlerobot/policies/smolvla/\n├── __init__.py            # 导出 SmolVLAPolicy\n├── modeling_smolvla.py    # SmolVLAPolicy 主类\n└── configuration_smolvla.py  # SmolVLAConfig 配置类\n```\n\n- **Policy 类**: `lerobot.policies.smolvla.SmolVLAPolicy`\n- **Config 类**: `lerobot.policies.smolvla.SmolVLAConfig` [UNVERIFIED - 具体类名可能不同]\n- **Policy type 注册名**: `\"smolvla\"`\n\n#### 关键方法\n\n| 方法 | 作用 |\n|------|------|\n| `SmolVLAPolicy.from_pretrained(model_id)` | 从 HF Hub 加载预训练权重 |\n| `policy.forward(batch)` | 训练时前向传播，返回 (loss, outputs) |\n| `policy.select_action(batch)` | 推理时生成 action chunk |\n| `make_pre_post_processors()` | 创建数据预处理/后处理 pipeline |\n\n### 2.4 冻结 Backbone 机制\n\n#### 方式 1: Config 参数控制（默认行为）\n\n```bash\n# SmolVLA 默认 config（已内置）\n--policy.freeze_vision_encoder=true   # 冻结 SigLIP\n--policy.train_expert_only=true       # 只训练 action expert\n--policy.train_state_proj=true        # 也训练 state projection\n```\n\n默认 fine-tuning 时：\n- SigLIP vision encoder: **冻结**\n- SmolLM2 语言模型层: **冻结**（train_expert_only=true 时）\n- Action expert: **可训练**\n- State projection: **可训练**\n\n#### 方式 2: PEFT/LoRA（参数高效微调）\n\n```bash\npip install \"lerobot[peft]\"  # 安装 PEFT 依赖\n\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --peft.method_type=LORA \\\n  --peft.r=64 \\\n  --policy.optimizer_lr=1e-3 \\\n  --steps=100000 \\\n  --batch_size=32\n```\n\n**LoRA 默认 target modules**: `q_proj`, `v_proj` (LM expert) + `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`\n\n**自定义 target**:\n```bash\n--peft.target_modules='(model\\.vlm_with_expert\\.lm_expert\\..*\\.(down|gate|up)_proj|.*\\.(state_proj|action_in_proj|action_out_proj))'\n```\n\n**指定模块全量微调**（不用 LoRA）:\n```bash\n--peft.full_training_modules=[\"state_proj\"]\n```\n\n### 2.5 数据加载流程\n\n#### LeRobotDataset v3.0 格式\n\n```\ndataset_repo/\n├── data/\n│   └── chunk-000/\n│       └── file_000.parquet    # 多 episode 的帧级数据（state, action, timestamp）\n├── videos/\n│   └── camera1/\n│       └── chunk-000/\n│           └── file_000.mp4    # 多 episode 视频\n└── meta/\n    ├── info.json               # 数据集元信息\n    ├── stats.json              # 归一化统计量\n    ├── tasks.parquet           # 任务描述\n    └── episodes/\n        └── chunk-000/\n            └── file_000.parquet  # Episode 索引\n```\n\n#### 数据字段\n\n- **observation.state**: 机器人关节状态 (shape: [6] for SO100)\n- **observation.images.camera1**: 图像帧 (shape: [3, H, W])\n- **action**: 机器人动作 (shape: [6] for SO100)\n- **timestamp**: 时间戳\n- **episode_index**: Episode 编号\n- **task**: 任务文本描述\n\n#### DataLoader 结构\n\n```python\nfrom lerobot.datasets.lerobot_dataset import LeRobotDataset\n\n# 从 HF Hub 加载\ndataset = LeRobotDataset(\"user/dataset_name\")\n\n# 访问单帧\nframe = dataset[0]\n# → {\"observation.state\": tensor, \"observation.images.camera1\": tensor, \"action\": tensor, ...}\n\n# 内部使用标准 PyTorch DataLoader\ndataloader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True)\n```\n\n#### 归一化\n\n- **VISUAL**: IDENTITY（不归一化，图像已是 [0,1]）\n- **STATE**: MEAN_STD 归一化\n- **ACTION**: MEAN_STD 归一化\n- 统计量存储在 `meta/stats.json`\n\n---\n\n## 3. 依赖清单\n\n### 3.1 核心依赖\n\n| 包 | 版本要求 | 说明 |\n|----|---------|------|\n| Python | **>=3.12** | 必须 3.12+ |\n| torch | **>=2.7, <2.12.0** | PyTorch |\n| torchvision | >=0.22.0, <0.27.0 | |\n| transformers | **>=5.4.0, <5.6.0** | HF Transformers (注意是 5.x!) |\n| accelerate | **>=1.10.0, <2.0.0** | 多 GPU / 混合精度 |\n| numpy | >=2.0.0, <2.3.0 | |\n| einops | >=0.8.0, <0.9.0 | |\n| safetensors | >=0.4.3, <1.0.0 | 权重格式 |\n| huggingface-hub | >=1.0.0, <2.0.0 | Hub 交互 |\n| draccus | ==0.10.0 | 配置系统 |\n| peft | >=0.18.0, <1.0.0 | LoRA 支持 |\n| wandb | >=0.24.0, <0.25.0 | 实验跟踪 |\n\n### 3.2 SmolVLA 专属依赖\n\n安装方式: `pip install -e \".[smolvla]\"` 或 `pip install \"lerobot[smolvla]\"`\n\n包含 transformers + peft 等 VLM 相关依赖。\n\n### 3.3 其他可选依赖组\n\n| Group | 主要包 |\n|-------|--------|\n| `datasets` | datasets, pandas, pyarrow, av, torchcodec |\n| `diffusion` | diffusers >=0.27.2, <0.36.0 |\n| `dev` | pytest, pre-commit, ruff, mypy |\n\n### 3.4 安装大小预估\n\n| 组件 | 大小 |\n|------|------|\n| PyTorch (CUDA 12.x) | ~2.5 GB |\n| transformers + tokenizers | ~500 MB |\n| lerobot + 依赖 | ~200 MB |\n| SmolVLA 模型权重 (smolvla_base) | ~900 MB (450M params × bf16) |\n| SmolVLM2-500M (首次加载时下载) | ~1 GB |\n| **总计预估** | **~5 GB** |\n\n### 3.5 安装命令\n\n```bash\n# 基础安装\npip install lerobot\n\n# SmolVLA 完整支持\npip install \"lerobot[smolvla]\"\n\n# 开发模式\ngit clone https://github.com/huggingface/lerobot.git\ncd lerobot\npip install -e \".[smolvla]\"\n```\n\n---\n\n## 4. 关键文件路径（LeRobot repo 中）\n\n```\nlerobot/\n├── lerobot/\n│   ├── policies/\n│   │   ├── smolvla/\n│   │   │   ├── __init__.py\n│   │   │   ├── modeling_smolvla.py      # SmolVLAPolicy 主类\n│   │   │   └── configuration_smolvla.py # 配置类\n│   │   ├── factory.py                   # make_policy(), make_pre_post_processors()\n│   │   └── utils.py                     # build_inference_frame(), make_robot_action()\n│   ├── scripts/\n│   │   └── train.py                     # lerobot-train 入口（或 lerobot_train.py）\n│   ├── datasets/\n│   │   └── lerobot_dataset.py           # LeRobotDataset 类\n│   └── configs/                         # TrainPipelineConfig 等 [UNVERIFIED 具体路径]\n├── examples/\n│   └── tutorial/smolvla/\n│       └── using_smolvla_example.py     # 使用示例\n├── docs/\n│   └── source/\n│       ├── smolvla.mdx\n│       └── peft_training.mdx\n└── pyproject.toml                       # 依赖定义\n```\n\n---\n\n## 5. 对我们项目的关键观察\n\n### 适合做 Information Bottleneck 的切入点\n\n1. **Vision Encoder 输出层**：SigLIP → PixelShuffle 后的 64 tokens (960-dim)，这是一个天然的 bottleneck 位置\n2. **VLM Layer 16 输出**：VLM 只用前 16 层的输出送给 action expert，这层的 representation 是 action-conditioning 的核心\n3. **Action Expert 的 Cross-Attention**：action tokens attend to VLM features，可以在这里施加信息约束\n4. **State Projection**：单 token 通过 linear projection，维度转换点\n\n### 训练效率\n\n- 默认只训练 action expert (~100M params)，VLM 冻结\n- 单 A100 上 20k steps ≈ 4 小时\n- 50 episodes 数据即可 fine-tune\n- 支持 LoRA 进一步降低训练成本\n\n### 注意事项\n\n- **transformers 版本要求 5.4+**：这是较新版本，需确认与其他依赖兼容性\n- **Python >=3.12**：不支持 3.11 及以下\n- `num_expert_layers: 0` 的具体含义需要阅读源码确认 [UNVERIFIED]\n- Action expert 的确切层数未从公开文档中明确获得 [UNVERIFIED]\n\n---\n\n## Sources\n\n- [SmolVLA Blog](https://huggingface.co/blog/smolvla)\n- [SmolVLA Paper (arXiv:2506.01844)](https://arxiv.org/abs/2506.01844)\n- [lerobot/smolvla_base Model Card](https://huggingface.co/lerobot/smolvla_base)\n- [LeRobot SmolVLA Docs](https://huggingface.co/docs/lerobot/smolvla)\n- [LeRobot PEFT Training](https://huggingface.co/docs/lerobot/peft_training)\n- [LeRobot GitHub](https://github.com/huggingface/lerobot)\n- [LeRobot pyproject.toml](https://github.com/huggingface/lerobot/blob/main/pyproject.toml)\n- [SmolVLM2-500M-Video-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct)\n- [SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct)\n- [LeRobotDataset v3.0](https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3)\n"
  }
}
````

</details>

---

### Tool result

_source line 72 · 2026-05-15T11:17:58.272185+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_smolvla_lerobot.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-15T11:17:58.272357+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T11:17:58.272483+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla-lerobot_20260515T111122",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-15T11:17:58.272700+00:00_

报告已完成，写入到 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_smolvla_lerobot.md`。

核心发现：

**SmolVLA 架构**: SigLIP-Base (768-dim, 1024 tokens → PixelShuffle → 64 tokens) + SmolLM2-360M (960-dim, 只用前 16/32 层) + Action Expert (~100M, hidden=720, flow matching 10步推理, chunk=50)

**LeRobot 框架**: `lerobot-train` CLI 入口，draccus dataclass 配置，policy 类为 `lerobot.policies.smolvla.SmolVLAPolicy`，默认冻结 VLM 只训练 expert，支持 LoRA

**依赖**: Python >=3.12, PyTorch >=2.7, transformers >=5.4.0（注意是 5.x），总安装约 5GB

**对 information bottleneck 项目的切入点**: VLM layer-16 输出到 action expert 的 cross-attention 接口是最自然的约束位置；PixelShuffle 后的 64 tokens 也是天然 bottleneck。

有 3 处标注了 `[UNVERIFIED]`（`num_expert_layers=0` 的确切含义、action expert 的精确层数、配置类名），需要阅读源码确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_smolvla-lerobot_20260515T111122"
}
```

</details>

---
