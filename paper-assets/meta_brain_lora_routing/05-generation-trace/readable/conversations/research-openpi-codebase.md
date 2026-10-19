# research openpi codebase

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 0
- **Tool calls:** 46
- **Original source:** `logs/chats/worker_research_openpi-codebase_20260515T103420.jsonl`
- **Structured JSON:** [`b9fedbcdf4a44727bb8d.json`](../../sessions/b9/b9fedbcdf4a44727bb8d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

93 recorded events

### Tool call

_source line 1 · 2026-05-15T10:41:49.894621+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T10:41:49.894928+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T10:41:49.895120+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenPI pi0 Physical Intelligence github repository architecture model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenPI pi0 Physical Intelligence github repository architecture model"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T10:41:49.895250+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0 model architecture PaliGemma robot policy Physical Intelligence 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0 model architecture PaliGemma robot policy Physical Intelligence 2025"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T10:41:49.895367+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openpi LIBERO evaluation fine-tuning LoRA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openpi LIBERO evaluation fine-tuning LoRA 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T10:41:49.895523+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Physical Intelligence pi0 checkpoint huggingface model size parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Physical Intelligence pi0 checkpoint huggingface model size parameters"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T10:41:49.895684+00:00_

Web search results for query: "Physical Intelligence pi0 checkpoint huggingface model size parameters"

Links: [{"title":"π₀ (Pi0) · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi0"},{"title":"lerobot/pi0_base · Hugging Face","url":"https://huggingface.co/lerobot/pi0_base"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"lerobot/pi05_base · Hugging Face","url":"https://huggingface.co/lerobot/pi05_base"},{"title":"lerobot/pi0_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi0_libero_base"},{"title":"π0 and π0-FAST: Vision-Language-Action Models for General Robot Control","url":"https://huggingface.co/blog/pi0"},{"title":"Models · Hugging Face","url":"https://huggingface.co/docs/transformers/en/main_classes/model"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"},{"title":"Robotics Foundation Models by Physical Intelligence: OpenPi | by Siamak Yousefi | Medium","url":"https://medium.com/@siamak.yousefi.1984_58741/robotics-foundation-models-by-physical-intelligence-openpi-663dc55aa9d3"}]

Based on the search results, I found information about the Physical Intelligence π0 checkpoint on Hugging Face:

The π0 model has 4B parameters. This information is visible on the Hugging Face model cards for various π0 checkpoints available on the platform.

π₀ is a Vision-Language-Action model for general robot control, from Physical Intelligence. π0 (Pi-Zero) is a Vision-Language-Action (VLA) model designed for generalist robot control that builds upon large-scale pretraining and flow matching-based action generation.

The base checkpoints are available on Hugging Face through the LeRobot repository, with models like `lerobot/pi0_base` and `lerobot/pi0_libero_base` both featurin
…[truncated 136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T10:41:49.895876+00:00_

Web search results for query: "OpenPI pi0 Physical Intelligence github repository architecture model"

Links: [{"title":"GitHub - allenzren/open-pi-zero: Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence · GitHub","url":"https://github.com/allenzren/open-pi-zero"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"openpi/src/openpi/training/config.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/src/openpi/training/config.py"},{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"},{"title":"Physical Intelligence open-sources Pi0 robotics foundation model","url":"https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"},{"title":"GitHub - Tonghe-Zhang/openpi-physical-intelligence · GitHub","url":"https://github.com/Tonghe-Zhang/openpi-physical-intelligence"},{"title":"Open Sourcing π0","url":"https://www.pi.website/blog/openpi"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py"},{"title":"GitHub - Shiduo-zh/openpi · GitHub","url":"https://github.com/Shiduo-zh/openpi"},{"title":"question about lora fine-tuning for pi0.5 · Issue #672 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/672"}]

Based on the search results, here's information about the OpenPI pi0 Physical Intelligence GitHub repository and its architecture:

## Repository Overview

Physical Intelligence has released the code and weights for Pi0 as part of its experimental openpi repository on GitHub. The official repository is located at https://github.com/Physical-Intelligence/openpi.

…[truncated 1337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T10:41:49.896100+00:00_

Web search results for query: "openpi LIBERO evaluation fine-tuning LoRA 2025"

Links: [{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"[Feature Proposal] Add LoRA training support for pi0.5 (PyTorch backend) · Issue #842 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/842"},{"title":"question about lora fine-tuning for pi0.5 · Issue #672 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/672"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"RL on π0 and π0.5 Models — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/pi0.html"},{"title":"doremifasolatido/pi0-fast-libero-lora · Hugging Face","url":"https://huggingface.co/doremifasolatido/pi0-fast-libero-lora"},{"title":"Poor training performance (3.3% success rate) with pi0 model on locally downloaded official LIBERO dataset · Issue #804 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/804"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"Does VLA model really have generalisation capabilities? Or is it just a overfit? | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/does-vla-model-really-have-generalisation-capabilities-or-is-it-just-a-overfit-270ffd7a04db"}]

Based on the search results, here's what I found about openpi LIBERO evaluation fine-tuning with LoRA in 2025:

## Overview

A native LoRA training pipeline for the PyTorch version of pi0.5 has been implemented, which is lightweight 
…[truncated 1326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T10:41:49.896303+00:00_

Web search results for query: "pi0 model architecture PaliGemma robot policy Physical Intelligence 2025"

Links: [{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"},{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"},{"title":"Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies","url":"https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"},{"title":"π 0 : Our First Generalist Policy","url":"https://www.pi.website/blog/pi0"},{"title":"π0 robot policy model. π0[1] is a generalist robot policy… | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/%CF%800-robot-policy-model-50d50b739a40"},{"title":"Robotics Foundation Models by Physical Intelligence: OpenPi | by Siamak Yousefi | Medium","url":"https://medium.com/@siamak.yousefi.1984_58741/robotics-foundation-models-by-physical-intelligence-openpi-663dc55aa9d3"},{"title":"π0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://www.pi.website/download/pi0.pdf"},{"title":"GitHub - allenzren/open-pi-zero: Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence · GitHub","url":"https://github.com/allenzren/open-pi-zero"},{"title":"π0 and π0-FAST: Vision-Language-Action Models for General Robot Control","url":"https://huggingface.co/blog/pi0"},{"title":"Physical AI: The Next Frontier in AI and Robotics to Build Truly Autonomous Machines[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202604.0549"}]

Based on the search results, here's comprehensive information about the π₀ model architecture from Physical Intelligence:

## Overview

π₀ is a prototype model that combines large-scale multi-task and multi-robot data collection with a new network architecture
…[truncated 2561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T10:41:49.896535+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/README.md",
  "prompt": "Extract all information about: model architecture, checkpoint download, LIBERO evaluation, fine-tuning, LoRA support, model size, GPU requirements. List all important file paths mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/README.md",
    "prompt": "Extract all information about: model architecture, checkpoint download, LIBERO evaluation, fine-tuning, LoRA support, model size, GPU requirements. List all important file paths mentioned."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T10:41:49.896685+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py",
  "prompt": "Extract all training config details: model names, checkpoint paths, LoRA config, training hyperparameters, LIBERO-related configs. Show the full class definitions and important constants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py",
    "prompt": "Extract all training config details: model names, checkpoint paths, LoRA config, training hyperparameters, LIBERO-related configs. Show the full class definitions and important constants."
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T10:41:49.896808+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/tree/main/src/openpi/models",
  "prompt": "List all files in the models directory. Extract any information about model architecture, file names, and their purposes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi/tree/main/src/openpi/models",
    "prompt": "List all files in the models directory. Extract any information about model architecture, file names, and their purposes."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T10:41:49.896933+00:00_

# OpenPI Models Directory Contents

## Files and Structure

The `/src/openpi/models` directory contains the following components:

**Core Model Files:**
- `model.py` - Base model implementation
- `pi0.py` - Primary model architecture
- `pi0_config.py` - Configuration settings for PI-0
- `gemma.py` - Gemma model integration
- `siglip.py` - Vision encoder component
- `vit.py` - Vision Transformer implementation
- `tokenizer.py` - Token processing utility

**Optimized Variants:**
- `gemma_fast.py` - Performance-optimized Gemma variant
- `pi0_fast.py` - Accelerated PI-0 implementation

**Supporting Components:**
- `lora.py` - Low-Rank Adaptation implementation
- `utils/` - Utility functions subdirectory

**Test Files:**
- `model_test.py`, `pi0_test.py`, `lora_test.py`, `tokenizer_test.py` - Unit tests for respective modules

## Purpose Overview

This directory houses the machine learning model architectures for the OpenPI project, including vision encoders (ViT, SigLIP), language model integration (Gemma), and training optimization techniques (LoRA adapters).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T10:41:49.897089+00:00_

# OpenPI: Robotics Models - Key Information

## Model Architecture

The repository contains three vision-language-action (VLA) model types:

1. **π₀**: "a flow-based vision-language-action model (VLA)"
2. **π₀-FAST**: "an autoregressive VLA, based on the FAST action tokenizer"
3. **π₀.₅**: "an upgraded version of π₀ with better open-world generalization trained with knowledge insulation"

All models use pre-training on 10k+ hours of robot data and support fine-tuning capabilities.

## Checkpoint Downloads

Base models and fine-tuned checkpoints are available via Google Cloud Storage:
- **π₀ base**: `gs://openpi-assets/checkpoints/pi0_base`
- **π₀-FAST base**: `gs://openpi-assets/checkpoints/pi0_fast_base`
- **π₀.₅ base**: `gs://openpi-assets/checkpoints/pi05_base`

Checkpoints automatically download to `~/.cache/openpi` by default, configurable via `OPENPI_DATA_HOME`.

## LIBERO Evaluation

A π₀.₅ model fine-tuned for LIBERO achieves "state-of-the-art performance" per the documentation. The conversion process is provided in `examples/libero/convert_libero_data_to_lerobot.py`, with pre-converted datasets available for direct use.

## Fine-Tuning Process

Three-step workflow:

1. **Data conversion** to LeRobot dataset format
2. **Training config definition** with normalization statistics computation
3. **Policy server deployment** for inference testing

Key command: `uv run scripts/compute_norm_stats.py --config-name [model]` followed by training execution.

## LoRA Support

LoRA (low-rank adaptation) is **supported in JAX implementations** with minimum GPU memory requirement of "> 22.5 GB" for fine-tuning via LoRA. However, **PyTorch implementation does not yet support LoRA training**.

## Model Size & GPU Requirements

| Mode | Memory | Example GPU |
|------|--------|-------------|
| Inference | > 8 GB | RTX 4090 |
| Fine-tuning (LoRA) | > 22.5 GB | RTX 4090 |
| Fine-tuning (Full) | > 70 GB | A100/H100 |

## Important File Paths

- `src/openpi/training/config.py` - 
…[truncated 505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T10:41:49.897246+00:00_

# Training Configuration Details

## Model Names & Architectures

The codebase supports three primary model types:
- **PI0**: Base model using PaliGemma tokenizer
- **PI05**: Enhanced variant with discrete state input support
- **PI0_FAST**: Optimized architecture using FAST tokenizer

## Checkpoint Paths

Key pre-trained checkpoints referenced:
- `gs://openpi-assets/checkpoints/pi0_base/params`
- `gs://openpi-assets/checkpoints/pi05_base/params`
- `gs://openpi-assets/checkpoints/pi0_fast_base/params`
- `gs://openpi-assets/checkpoints/pi05_droid/params`

## LoRA Configuration

Low-memory fine-tuning utilizes model variants:
- `paligemma_variant="gemma_2b_lora"`
- `action_expert_variant="gemma_300m_lora"`

"The freeze filter defines which parameters should be frozen during training" via `model_config.get_freeze_filter()`. EMA decay is disabled for LoRA: `ema_decay=None`.

## Training Hyperparameters

**Default TrainConfig fields:**
- `num_train_steps`: 30,000 (configurable per task)
- `batch_size`: 32 (256 for large datasets like DROID)
- `seed`: 42
- `num_workers`: 2
- `log_interval`: 100 steps
- `save_interval`: 1,000 steps

**Optimizer defaults:**
- Learning rate schedule: `CosineDecaySchedule`
- Optimizer: `AdamW`
- EMA decay: 0.99 (standard), 0.999 (PI05)

## LIBERO-Related Configurations

**LeRobotLiberoDataConfig** manages dataset integration:
- Repack transform remaps dataset keys to inference pipeline keys
- Data transforms apply robot-specific preprocessing
- `extra_delta_transform`: Controls delta action conversion (disabled for LIBERO)
- `prompt_from_task=True`: Loads task instructions as prompts

**Fine-tuning examples:**
- Full fine-tuning: 30,000 steps, batch size 32
- LoRA fine-tuning: Same steps, frozen non-LoRA parameters
- PI0-FAST variant: `action_dim=7, action_horizon=10, max_token_len=180`

## DataConfigFactory Class Pattern

Abstract base defining:
- `repo_id`: LeRobot dataset identifier
- `assets`: Location configuration for normalization stat
…[truncated 259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T10:41:49.897429+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/pi0.py",
  "prompt": "Extract the COMPLETE model architecture: class names, forward method, all layers, hidden dimensions, attention heads, number of layers, how actions are generated, flow matching implementation. Show class hierarchies and key method signatures with line numbers if possible. Include ALL import statements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/pi0.py",
    "prompt": "Extract the COMPLETE model architecture: class names, forward method, all layers, hidden dimensions, attention heads, number of layers, how actions are generated, flow matching implementation. Show class hierarchies and key method signatures with line numbers if possible. Include ALL import statements."
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T10:41:49.897583+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/gemma.py",
  "prompt": "Extract the COMPLETE Gemma model architecture: class definitions, layer count, hidden_dim, num_heads, attention implementation, MLP implementation, all config parameters. Show the full class hierarchy and key method signatures. Include information about how layers are numbered/indexed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/gemma.py",
    "prompt": "Extract the COMPLETE Gemma model architecture: class definitions, layer count, hidden_dim, num_heads, attention implementation, MLP implementation, all config parameters. Show the full class hierarchy and key method signatures. Include information about how layers are numbered/indexed."
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T10:41:49.897706+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/pi0_config.py",
  "prompt": "Extract ALL configuration details: model variants, parameter counts, hidden dimensions, number of layers, attention heads, LoRA config options, freeze filters, all dataclass fields and their defaults."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/pi0_config.py",
    "prompt": "Extract ALL configuration details: model variants, parameter counts, hidden dimensions, number of layers, attention heads, LoRA config options, freeze filters, all dataclass fields and their defaults."
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T10:41:49.897820+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/lora.py",
  "prompt": "Extract the COMPLETE LoRA implementation: which layers get LoRA, rank, alpha, target modules, how LoRA is applied to the model, all class definitions and methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/lora.py",
    "prompt": "Extract the COMPLETE LoRA implementation: which layers get LoRA, rank, alpha, target modules, how LoRA is applied to the model, all class definitions and methods."
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T10:41:49.897955+00:00_

# Pi0 Configuration Details

## Model Variants
- **PaliGemma variant**: `"gemma_2b"` (default)
- **Action expert variant**: `"gemma_300m"` (default)
- **Pi05 mode**: Boolean flag enabling discrete state input and larger token length (200 vs 48)

## Dataclass Fields & Defaults

| Field | Default | Type |
|-------|---------|------|
| `dtype` | `"bfloat16"` | str |
| `paligemma_variant` | `"gemma_2b"` | Variant |
| `action_expert_variant` | `"gemma_300m"` | Variant |
| `action_dim` | 32 | int |
| `action_horizon` | 50 | int |
| `max_token_len` | 200 (pi05) / 48 | int |
| `pi05` | False | bool |
| `discrete_state_input` | Matches pi05 | bool |
| `pytorch_compile_mode` | `"max-autotune"` | str |

## Freeze Filter Configuration

The freeze mechanism uses regex path matching with these patterns:
- `".*llm.*"` – targets main gemma parameters
- `".*llm.*_1.*"` – targets action expert parameters  
- `".*lora.*"` – excludes LoRA parameters when enabled

**LoRA behavior**: When LoRA appears in either variant name, corresponding base parameters freeze while LoRA parameters remain trainable.

## Input/Output Specifications

- **Images**: Three camera views (base_0, left_wrist_0, right_wrist_0) at 3-channel resolution
- **State**: `[batch_size, action_dim]` float32
- **Prompt tokens**: `[batch_size, max_token_len]` int32
- **Actions output**: `[batch_size, action_horizon, action_dim]` float32

**Note**: Hidden dimensions, layer counts, and attention head parameters are not specified in this configuration file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T10:41:49.898123+00:00_

# Gemma Model Architecture Overview

## Core Configuration Structure

The model defines a `Config` dataclass with these parameters:
- `width`: embedding/hidden dimension
- `depth`: number of transformer layers
- `mlp_dim`: feed-forward hidden dimension
- `num_heads`: query heads
- `num_kv_heads`: key-value heads
- `head_dim`: per-head dimension
- `lora_configs`: optional LoRA adaptations

## Model Variants

Four primary variants with increasing scale:

| Variant | Width | Depth | MLP Dim | Heads | KV Heads |
|---------|-------|-------|---------|-------|----------|
| dummy | 64 | 4 | 128 | 8 | 1 |
| gemma_300m | 1024 | 18 | 4096 | 8 | 1 |
| gemma_2b | 2048 | 18 | 16384 | 8 | 1 |

LoRA variants add rank-16 or rank-32 adaptations to attention and FFN layers.

## Class Hierarchy

**`Module`** (main transformer)
- `Embedder`: Token embedding with scaling
- `layers`: Scanned `Block` instances (depth = 18)
- `final_norms`: Per-expert RMSNorm layers

**`Block`** (transformer layer)
- `Attention`: Multi-head self-attention with RoPE
- `RMSNorm`: Root mean square normalization (with optional AdaRMS conditioning)
- `lora.FeedForward`: Gated feed-forward network

**`Attention`**
- Supports grouped query attention (GQA)
- Applies RoPE rotational embeddings
- Maintains KV cache for inference
- Uses masked softmax with bias of -2.3819763e38

**`FeedForward`**
- Two linear projections with GELU gating
- Pattern: gate_proj → gelu → multiply → output_proj

## Layer Naming Convention

Layers follow a naming pattern for multi-expert support: first expert uses base name (e.g., "attn"), subsequent experts append index suffix (e.g., "attn_1"). This enables loading pre-trained PaliGemma weights for the primary expert while initializing additional experts from scratch.

## Key Implementation Details

- Computations use mixed precision with float32 for normalization variance
- Residual connections employ gated mechanisms when conditioning is present
- Batch dimension sharding constraints app
…[truncated 63 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T10:41:49.898271+00:00_

# LoRA Implementation Overview

## Configuration Class
The `LoRAConfig` dataclass defines LoRA parameters:
- **Rank**: Primary hyperparameter controlling the decomposition dimension
- **Alpha**: Scaling factor (default 1.0)
- **Init function**: Parameter initialization (default normal distribution with stddev=0.01)
- **RSLoRA**: Enables rank-stabilized variant per arxiv paper 2312.03732
- **Axes**: Target weight dimensions, typically the final two axes
- **Label**: Einsum axis identifier

The `scaling_value` property computes: `alpha / sqrt(rank)` (with RSLoRA) or `alpha / rank`

## Target Modules

**Einsum class**: Generic adapter supporting any operation using einsum notation. Creates low-rank matrices `w_a` and `w_b` with shapes derived from specified axes.

**FeedForward class**: Applies LoRA to two specific layers:
1. Gating projection: decomposes the gating weight matrix
2. Linear output: decomposes the linear transformation

## Application Method

LoRA augments base weights additively:
```
output = base_output + (x @ w_a @ w_b) * scaling_value
```

For Einsum, the equation is decomposed into two chained operations using an intermediate axis label. For FeedForward, sequential matrix multiplications compute the low-rank contribution before scaling and addition.

Both implementations preserve input dtype precision handling through explicit casting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T10:41:49.898450+00:00_

# Pi0 Model Architecture Analysis

## Class Hierarchy

```
BaseModel (from openpi.models.model)
└── Pi0 (lines 47-176)
```

## Key Classes and Components

### Main Model Class: `Pi0`

**Constructor** (`__init__`, lines 49-79):
- Inherits from `_model.BaseModel`
- Initializes with `pi0_config.Pi0Config` and `nnx.Rngs`

**Core Submodules:**
- `self.PaliGemma`: `nnx.Dict` containing:
  - `llm`: Gemma language model (dual-config for PaliGemma + action expert)
  - `img`: SigLiP vision encoder (So400m/14 variant, no pooling)
- `self.action_in_proj`: `nnx.Linear(action_dim → width)`
- `self.action_out_proj`: `nnx.Linear(width → action_dim)`

**Conditional Pi0.5 Modules:**
- **Pi0.5 path**: `time_mlp_in`, `time_mlp_out` (Linear layers for adaptive RMS)
- **Pi0 path**: `state_proj`, `action_time_mlp_in`, `action_time_mlp_out`

## Key Methods

| Method | Signature | Purpose |
|--------|-----------|---------|
| `embed_prefix` | `(obs: Observation) → (tokens, input_mask, ar_mask)` | Encodes images and language inputs |
| `embed_suffix` | `(obs, noisy_actions, timestep) → (tokens, mask, ar_mask, adarms_cond)` | Encodes actions and timestep embeddings |
| `compute_loss` | `(rng, observation, actions, train) → loss` | Training objective using flow matching |
| `sample_actions` | `(rng, observation, num_steps, noise) → actions` | Diffusion-based action generation |

## Flow Matching Implementation

**Training** (lines 119-150):
- Sample timestep `t` from Beta(1.5, 1) distribution, scaled to [0.001, 0.999]
- Compute noisy state: `x_t = t·noise + (1-t)·actions`
- Target velocity: `u_t = noise - actions`
- Predict velocity `v_t` via forward pass
- Loss: mean squared error between `v_t` and `u_t`

**Inference** (lines 152-201):
- Iterative denoising with `num_steps` (default 10)
- Time step convention: `t=1` (noise) → `t=0` (target)
- Integration: `x_{t+dt} = x_t + dt·v_t` with `dt = -1/num_steps`
- KV-cache optimization for prefix tokens
- Termination: `while time ≥ -dt/2`

## Attenti
…[truncated 1193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T10:41:49.898633+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/model.py",
  "prompt": "Extract the complete BaseModel class definition, forward method, any hook mechanisms, layer access patterns. Show how the model processes inputs and returns outputs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/model.py",
    "prompt": "Extract the complete BaseModel class definition, forward method, any hook mechanisms, layer access patterns. Show how the model processes inputs and returns outputs."
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T10:41:49.898756+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/policies/libero_policy.py",
  "prompt": "Extract everything about LIBERO policy: data mapping, observation format, action format, normalization, how it connects to the model. Show all class definitions and key methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/policies/libero_policy.py",
    "prompt": "Extract everything about LIBERO policy: data mapping, observation format, action format, normalization, how it connects to the model. Show all class definitions and key methods."
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T10:41:49.898878+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/tree/main/examples/libero",
  "prompt": "List all files in the LIBERO examples directory. Extract information about evaluation scripts, data conversion, config files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi/tree/main/examples/libero",
    "prompt": "List all files in the LIBERO examples directory. Extract information about evaluation scripts, data conversion, config files."
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T10:41:49.898991+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openpi pytorch implementation pi0 model forward pass intermediate layers hooks site:github.com/Physical-Intelligence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openpi pytorch implementation pi0 model forward pass intermediate layers hooks site:github.com/Physical-Intelligence"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T10:41:49.899118+00:00_

# LIBERO Policy Integration Overview

## Data Mapping & Observation Format

The `LiberoInputs` class transforms dataset inputs into model-compatible format. It accepts observations with three components:

- **State**: `"observation/state"` - 8-dimensional vector
- **Base image**: `"observation/image"` - 224×224 RGB (third-person view)
- **Wrist image**: `"observation/wrist_image"` - 224×224 RGB (left wrist camera)

The system supports "three image inputs at the moment: one third-person view, and two wrist views (left and right)."

## Image Processing

The `_parse_image()` method standardizes images to uint8 format with shape (H,W,C):
- Converts float32 to uint8 (scaling by 255)
- Rearranges channel-first (C,H,W) to channel-last (H,W,C)

## Model Input Structure

The processed inputs dictionary contains:

```python
{
    "state": observation/state,
    "image": {
        "base_0_rgb": parsed_base_image,
        "left_wrist_0_rgb": parsed_wrist_image,
        "right_wrist_0_rgb": zero_padded_array
    },
    "image_mask": {...},  # Indicates valid images
    "actions": [...],      # Training only
    "prompt": "instruction" # Language command
}
```

## Action Format

The `LiberoOutputs` class extracts action outputs. Since "actions are padded above to fit the model action dimension," the inference returns "the first 7 actions" representing the actual task-relevant dimensions, discarding padding.

## Key Components

- **Model Type Parameter**: Determines PI0 vs PI0-FAST masking behavior
- **Language Grounding**: Optional prompt field for instruction-following
- **Frozen Dataclasses**: Both transform classes use immutable configuration

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T10:41:49.899268+00:00_

# BaseModel Class Definition

## Complete Class Structure

The `BaseModel` class is an abstract base for all model implementations:

```python
@dataclasses.dataclass
class BaseModel(nnx.Module, abc.ABC):
    action_dim: int
    action_horizon: int
    max_token_len: int
```

## Abstract Methods

The class defines two abstract methods that subclasses must implement:

**1. compute_loss**: Calculates training loss given observations and target actions. Returns "float32[*b ah]" shaped tensors where *b represents batch dimensions and ah is action horizon.

**2. sample_actions**: Generates action predictions from observations using random number generation for stochastic sampling.

## Input/Output Processing

The model processes inputs through the `Observation` dataclass, which contains:
- Images dictionary (multiple camera views in [-1, 1] range)
- Image masks for validity tracking
- Low-dimensional robot state
- Optional tokenized prompts and masks
- Optional autoregressive masks for fast inference

Output is typed as "float32[*b ah ad]" where ad represents action dimensions.

## Design Pattern

The class follows a template pattern where subclasses inherit shared attributes (action_dim, action_horizon, max_token_len) and must implement compute_loss and sample_actions according to the specific model architecture. There are no explicit hook mechanisms or direct layer access patterns shown—the implementation relies on NNX's module system for parameter management.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T10:41:49.899411+00:00_

Web search results for query: "openpi pytorch implementation pi0 model forward pass intermediate layers hooks site:github.com/Physical-Intelligence"

No links found.

The search did not return any results. This could mean that:

1. The specific repository or documentation you're looking for at `github.com/Physical-Intelligence` may not be publicly available or indexed by search engines yet
2. The exact combination of terms (openpi, pytorch, pi0 model, forward pass, intermediate layers, hooks) may not appear together in publicly indexed content
3. The content might be behind authentication or not yet published

You might want to try:
- Visiting the Physical Intelligence GitHub organization directly to browse their repositories
- Searching with fewer or different keywords
- Checking if there's recent documentation or release announcements about the pi0 model
- Looking at the repository's issues, discussions, or pull requests for implementation details

Would you like me to try a different search query with modified terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T10:41:49.899588+00:00_

# LIBERO Examples Directory Contents

## Files Listed

The directory contains the following files:

1. **Dockerfile** - Container configuration for running the example
2. **README.md** - Documentation and setup instructions
3. **compose.yml** - Docker Compose configuration
4. **convert_libero_data_to_lerobot.py** - Data conversion script
5. **main.py** - Primary execution script
6. **requirements.in** - Base dependency specifications
7. **requirements.txt** - Locked dependency versions

## Key Information

**Data Conversion**: The `convert_libero_data_to_lerobot.py` script handles transforming LIBERO benchmark data into LeRobot format.

**Evaluation Results**: The documentation shows model performance across multiple task suites, with the π0.5 checkpoint achieving an average score of 96.85% across LIBERO Spatial, Object, Goal, and 10-task variants.

**Setup Requirements**: Git submodules must be initialized with `git submodule update --init --recursive` before running the benchmark.

**Configuration**: The example supports customization via `SERVER_ARGS` for checkpoint selection and `CLIENT_ARGS` for task suite specification, with specific guidance for handling graphics rendering issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T10:41:49.899742+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/tree/main/src/openpi/models/pi0_pytorch",
  "prompt": "List all files in the PyTorch pi0 directory. Show any model definitions, forward methods, layer structures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi/tree/main/src/openpi/models/pi0_pytorch",
    "prompt": "List all files in the PyTorch pi0 directory. Show any model definitions, forward methods, layer structures."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T10:41:49.899857+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T10:41:49.899993+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com/Physical-Intelligence/openpi \"pytorch\" model forward layers transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com/Physical-Intelligence/openpi \"pytorch\" model forward layers transformer"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T10:41:49.900115+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/siglip.py",
  "prompt": "Extract the SigLIP vision encoder architecture: input resolution, patch size, embedding dimension, number of layers, output dimension. Show class definitions and configuration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/siglip.py",
    "prompt": "Extract the SigLIP vision encoder architecture: input resolution, patch size, embedding dimension, number of layers, output dimension. Show class definitions and configuration."
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T10:41:49.900231+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/main.py",
  "prompt": "Extract the complete LIBERO evaluation script: how inference is called, how episodes are run, success rate computation, environment setup, model loading. Show all key functions and their signatures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/main.py",
    "prompt": "Extract the complete LIBERO evaluation script: how inference is called, how episodes are run, success rate computation, environment setup, model loading. Show all key functions and their signatures."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T10:41:49.900350+00:00_

Web search results for query: "site:github.com/Physical-Intelligence/openpi "pytorch" model forward layers transformer"

No links found.

The search didn't return any results. This could mean:

1. The specific GitHub repository path (github.com/Physical-Intelligence/openpi) either doesn't exist, has a different URL structure, or the repository is private
2. The combination of search terms (pytorch, model forward layers transformer) may not appear together in the repository's publicly indexed content
3. The repository might not be indexed by search engines

If you're looking for information about this project, you might want to try:
- Visiting the GitHub URL directly if you know it
- Searching without the site restriction using just the project name and keywords
- Checking if the repository name or organization name might be slightly different

Would you like me to try a different search approach?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T10:41:49.900509+00:00_

# Vision Encoder Architecture Analysis

Based on the provided code, this is a **Vision Transformer (ViT) implementation**, not SigLIP. Here's the architecture specification:

## Key Configuration Parameters

The `decode_variant()` function defines multiple model sizes with these parameters:

| Variant | Width | Depth | MLP Dim | Num Heads |
|---------|-------|-------|---------|-----------|
| Ti (Tiny) | 192 | 12 | 768 | 3 |
| S (Small) | 384 | 12 | 1536 | 6 |
| B (Base) | 768 | 12 | 3072 | 12 |
| L (Large) | 1024 | 24 | 4096 | 16 |

## Core Class Definitions

**Primary Module:** The `_Module` class encompasses the full ViT encoder with these key attributes:

- `"patch_size"` - defaults to (16, 16)
- `"width"` - embedding dimension (768 for Base)
- `"depth"` - transformer layers (12 for Base)
- `"num_heads"` - attention heads
- `"pool_type"` - aggregation method: "gap" (global average), "map" (multihead attention), or "tok" (class token)

**Supporting Components:**
- `Encoder` - stacked transformer blocks with optional scan/rematerialization
- `Encoder1DBlock` - single layer with self-attention and MLP
- `MAPHead` - multihead attention pooling mechanism
- `MlpBlock` - feed-forward network (4× expansion default)

## Note

Input resolution isn't explicitly specified in this code excerpt—it's determined at runtime during patch extraction based on image dimensions and patch size.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T10:41:49.900651+00:00_

# LIBERO Evaluation Script Overview

## Main Entry Point
```python
def eval_libero(args: Args) -> None
```
Orchestrates the complete evaluation pipeline across all tasks in a benchmark suite.

## Key Functions & Signatures

**Environment Setup:**
```python
def _get_libero_env(task, resolution, seed)
```
Creates an `OffScreenRenderEnv` instance with specified task BDDL file and camera resolution. Returns environment and task description string.

**Utility:**
```python
def _quat2axisangle(quat)
```
Converts quaternion to axis-angle representation (3D rotation vector).

## Inference Flow

The script queries a remote model server via `WebsocketClientPolicy`:
```python
client = _websocket_client_policy.WebsocketClientPolicy(args.host, args.port)
```

**Inference Call:**
```python
action_chunk = client.infer(element)["actions"]
```

Where `element` contains:
- Preprocessed observation images (main camera + wrist camera)
- Robot state (end-effector position, rotation, gripper status)
- Task language prompt

## Episode Execution Loop

1. Reset environment with fixed initial state
2. Wait `num_steps_wait` timesteps for object stabilization
3. Every `replan_steps` actions: request new action chunk from model
4. Execute individual actions until episode completes (success) or `max_steps` exceeded
5. Record frames for video replay

## Success Rate Computation

```python
logging.info(f"Success rate: {total_successes / total_episodes * 100:.1f}%")
```

Tracks cumulative successes across all episodes and tasks, logging rates at task and overall completion levels.

## Configuration Parameters (Args Dataclass)

- Model server: `host`, `port`
- Image: `resize_size` (224px)
- Planning: `replan_steps` (5 actions per inference)
- Tasks: `task_suite_name`, `num_trials_per_task` (50)
- Output: `video_out_path`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T10:41:49.900806+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Physical-Intelligence/openpi\" pytorch train_pytorch.py pi0 model implementation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Physical-Intelligence/openpi\" pytorch train_pytorch.py pi0 model implementation 2025"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T10:41:49.900921+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/tree/main/src/openpi",
  "prompt": "List all directories and files in the src/openpi directory. Show the complete project structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi/tree/main/src/openpi",
    "prompt": "List all directories and files in the src/openpi directory. Show the complete project structure."
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T10:41:49.901034+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/scripts/train.py",
  "prompt": "Extract the complete training script: how model is loaded, training loop, optimizer, loss computation, checkpoint saving. Show all imports and key function signatures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/scripts/train.py",
    "prompt": "Extract the complete training script: how model is loaded, training loop, optimizer, loss computation, checkpoint saving. Show all imports and key function signatures."
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T10:41:49.901152+00:00_

# OpenPI src/openpi Directory Structure

Based on the GitHub repository content, here is the complete project structure for `src/openpi`:

## Directories
- **models** - Model definitions and implementations
- **models_pytorch** - PyTorch-specific model code
- **policies** - Policy implementations
- **serving** - Serving/inference infrastructure
- **shared** - Shared utilities and common code
- **training** - Training-related modules and scripts

## Files
- `__init__.py` - Package initialization
- `conftest.py` - Test configuration (pytest)
- `py.typed` - Type checking marker file
- `transforms.py` - Data transformation utilities
- `transforms_test.py` - Tests for transform functionality

The repository contains 11.9k stars and maintains active development with 223 open issues and 57 pull requests, indicating this is a well-used robotics/AI project from Physical Intelligence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T10:41:49.901285+00:00_

# Training Script Overview

## Key Imports
The script uses JAX/Flax for neural network training with these primary dependencies:
- `flax.nnx` for model architecture
- `optax` for optimization
- `jax` for computation
- `wandb` for experiment tracking
- Custom modules: `openpi.training.config`, `openpi.training.optimizer`, `openpi.training.checkpoints`

## Model Loading Process

**Initialization function signature:**
```python
def init_train_state(
    config: _config.TrainConfig, init_rng: at.KeyArrayLike, 
    mesh: jax.sharding.Mesh, *, resume: bool
) -> tuple[training_utils.TrainState, Any]
```

Model loading involves:
1. Creating model via `config.model.create(model_rng)`
2. Loading partial weights using `_load_weights_and_validate()` 
3. Converting frozen parameters to bfloat16
4. Initializing optimizer state with trainable parameters only

## Training Loop

```python
def train_step(
    config: _config.TrainConfig, rng: at.KeyArrayLike,
    state: training_utils.TrainState,
    batch: tuple[_model.Observation, _model.Actions]
) -> tuple[training_utils.TrainState, dict[str, at.Array]]
```

The loop executes for `config.num_train_steps` iterations, performing:
- Loss computation via `model.compute_loss()` with training flag enabled
- Gradient calculation using `nnx.value_and_grad()`
- Parameter updates through optimizer

## Optimizer & Loss

- Optimizer created via `_optimizer.create_optimizer()` with learning rate schedule
- Loss computed as mean of chunked losses: `jnp.mean(chunked_loss)`
- Exponential moving average (EMA) applied to parameters when configured

## Checkpointing

Checkpoints saved at intervals via `_checkpoints.save_state()` when `step % config.save_interval == 0`. Resume capability restores state using `_checkpoints.restore_state()`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T10:41:49.901460+00:00_

Web search results for query: ""Physical-Intelligence/openpi" pytorch train_pytorch.py pi0 model implementation 2025"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"openpi/src/openpi/models_pytorch/pi0_pytorch.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/src/openpi/models_pytorch/pi0_pytorch.py"},{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"},{"title":"openpi/src/openpi/training/config.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/src/openpi/training/config.py"},{"title":"Open Sourcing π0","url":"https://www.pi.website/blog/openpi"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"Physical-Intelligence/openpi | DeepWiki","url":"https://deepwiki.com/Physical-Intelligence/openpi"},{"title":"openpi/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/README.md"},{"title":"README.md · lerobot/pi05_libero_base at b9e89c2a0ab45eae172b9c7f19d5a9ce2b391b26","url":"https://huggingface.co/lerobot/pi05_libero_base/blob/b9e89c2a0ab45eae172b9c7f19d5a9ce2b391b26/README.md"},{"title":"Physical Intelligence open-sources Pi0 robotics foundation model","url":"https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"}]

Based on the search results, I can provide you with comprehensive information about the Physical-Intelligence/openpi PyTorch training implementation:

## PyTorch Support in OpenPI

In September 2025, Physical Intelligence released PyTorch support in openpi and released pi05, an upgraded version of pi0 with bett
…[truncated 1422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T10:41:49.901641+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/pi0_pytorch.py",
  "prompt": "Extract the COMPLETE PyTorch Pi0 model: class definitions, forward method, all layers, how attention works, how to access intermediate layers, layer indexing. Show imports, class hierarchies, and ALL method signatures. Focus especially on the transformer layers and how they can be accessed for hook registration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/pi0_pytorch.py",
    "prompt": "Extract the COMPLETE PyTorch Pi0 model: class definitions, forward method, all layers, how attention works, how to access intermediate layers, layer indexing. Show imports, class hierarchies, and ALL method signatures. Focus especially on the transformer layers and how they can be accessed for hook registration."
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T10:41:49.901763+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/tree/main/src/openpi/models_pytorch",
  "prompt": "List ALL files in this directory. Show the complete list of PyTorch model files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi/tree/main/src/openpi/models_pytorch",
    "prompt": "List ALL files in this directory. Show the complete list of PyTorch model files."
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T10:41:49.901876+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/scripts/train_pytorch.py",
  "prompt": "Extract the complete PyTorch training script: model loading, training loop, loss computation, optimizer, LoRA setup, checkpoint management. Show all imports and key function signatures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/scripts/train_pytorch.py",
    "prompt": "Extract the complete PyTorch training script: model loading, training loop, loss computation, optimizer, LoRA setup, checkpoint management. Show all imports and key function signatures."
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T10:41:49.901992+00:00_

# PyTorch Model Files in openpi/src/openpi/models_pytorch

Based on the GitHub directory listing, the following files are present in this directory:

1. **gemma_pytorch.py** - PyTorch implementation for Gemma model
2. **pi0_pytorch.py** - PyTorch implementation for PI-0 model
3. **preprocessing_pytorch.py** - Data preprocessing utilities for PyTorch
4. **transformers_replace/models/** - Subdirectory containing additional model implementations

The directory appears to contain the core PyTorch-based neural network models and preprocessing components for the OpenPI project, which focuses on physical intelligence implementations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T10:41:49.902127+00:00_

# PyTorch Training Script: Key Components

## Imports
```python
import torch
import torch.distributed as dist
import torch.nn.parallel
import safetensors.torch
import wandb
import openpi.models_pytorch.pi0_pytorch
import openpi.training.config as _config
import openpi.training.data_loader as _data
```

## Model Loading

**Function signature:**
```python
def build_datasets(config: _config.TrainConfig):
    data_loader = _data.create_data_loader(
        config, framework="pytorch", shuffle=True
    )
    return data_loader, data_loader.data_config()
```

The script instantiates the PI0Pytorch model and loads pre-trained weights:
```python
model = openpi.models_pytorch.pi0_pytorch.PI0Pytorch(model_cfg).to(device)
if config.pytorch_weight_path is not None:
    safetensors.torch.load_model(model, model_path)
```

## Training Loop Structure

**Core loop:**
```python
while global_step < config.num_train_steps:
    for observation, actions in loader:
        # Data preparation
        observation = jax.tree.map(lambda x: x.to(device), observation)
        actions = actions.to(device)
        
        # Forward pass
        losses = model(observation, actions)
        loss = losses.mean()
        
        # Backward pass
        loss.backward()
        
        # Gradient clipping
        torch.nn.utils.clip_grad_norm_(
            model.parameters(), 
            max_norm=config.optimizer.clip_gradient_norm
        )
        
        # Optimizer step
        optim.step()
        optim.zero_grad(set_to_none=True)
```

## Optimizer Configuration

**Setup:**
```python
optim = torch.optim.AdamW(
    model.parameters(),
    lr=peak_lr,
    betas=(config.optimizer.b1, config.optimizer.b2),
    eps=config.optimizer.eps,
    weight_decay=config.optimizer.weight_decay,
)
```

Learning rate scheduling uses cosine decay: "if step < warmup_steps... cosine decay"

## DDP & Checkpoint Management

**Distributed setup:**
```python
def setup_ddp():
    use_ddp = int(os.environ.get("WORLD_S
…[truncated 761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T10:41:49.902291+00:00_

# PyTorch Pi0 Model Architecture

## Class Definition & Imports

```python
import torch
from torch import nn
import torch.nn.functional as F

class PI0Pytorch(nn.Module):
    def __init__(self, config)
```

The model inherits from `nn.Module` and requires a configuration object specifying `paligemma_variant`, `action_expert_variant`, `action_dim`, `dtype`, and `action_horizon`.

## Core Components

**Main submodules:**
- `paligemma_with_expert`: `PaliGemmaWithExpertModel` (contains vision tower, language model, and action expert)
- `action_in_proj`: Linear layer (action_dim → expert_width)
- `action_out_proj`: Linear layer (expert_width → action_dim)
- Conditional MLPs for time embedding (PI0.5 variant uses `time_mlp_in/out`; base uses `action_time_mlp_in/out`)

## Transformer Layer Access

Access transformer layers through the composed model:

```python
self.paligemma_with_expert.paligemma.language_model.layers[i]
self.paligemma_with_expert.paligemma.vision_tower.layers[i]
self.paligemma_with_expert.gemma_expert.model.layers[i]
```

Each layer contains `self_attn` with `q_proj`, `k_proj`, `v_proj` weights.

## Forward Method Signatures

**Training forward:**
```python
def forward(self, observation, actions, noise=None, time=None) -> Tensor
```
Returns MSE loss between predicted and target noise.

**Inference sampling:**
```python
@torch.no_grad()
def sample_actions(self, device, observation, noise=None, num_steps=10) -> Tensor
```
Iteratively denoises actions using Euler steps over diffusion timesteps.

**Denoising step:**
```python
def denoise_step(self, state, prefix_pad_masks, past_key_values, x_t, timestep)
```

## Attention Mechanism

**2D attention mask creation:**
```python
def make_att_2d_masks(pad_masks, att_masks)
```
Constructs causal/prefix-LM attention patterns where tokens attend based on cumulative attention mask values. Output shape: `(batch, seq_len, seq_len)`.

**Attention mask preparation for transformers:**
```python
def _prepare_attention_masks
…[truncated 1160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T10:41:49.902470+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/gemma_pytorch.py",
  "prompt": "Extract the COMPLETE Gemma PyTorch model: class definitions, layer structure, hidden dimensions, num_heads, num_layers, attention implementation, MLP implementation, how layers are indexed/named. Show the exact module hierarchy so I know the path to access each transformer layer (e.g., model.layers[0].self_attn). Include ALL configuration parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/gemma_pytorch.py",
    "prompt": "Extract the COMPLETE Gemma PyTorch model: class definitions, layer structure, hidden dimensions, num_heads, num_layers, attention implementation, MLP implementation, how layers are indexed/named. Show the exact module hierarchy so I know the path to access each transformer layer (e.g., model.layers[0].self_attn). Include ALL configuration parameters."
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-15T10:41:49.902596+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/issues/842",
  "prompt": "Extract the full proposal for LoRA training support in PyTorch: what has been implemented, what's the status, technical approach, which layers get LoRA, configuration options."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi/issues/842",
    "prompt": "Extract the full proposal for LoRA training support in PyTorch: what has been implemented, what's the status, technical approach, which layers get LoRA, configuration options."
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T10:41:49.902717+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/issues/672",
  "prompt": "Extract information about LoRA fine-tuning for pi0.5: current status, workarounds, technical details about how to apply LoRA."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi/issues/672",
    "prompt": "Extract information about LoRA fine-tuning for pi0.5: current status, workarounds, technical details about how to apply LoRA."
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T10:41:49.902854+00:00_

# Gemma PyTorch Model Structure from Provided Code

Based on the code excerpt, I can identify the following Gemma model hierarchy:

## Module Hierarchy
```
GemmaForCausalLM
└── model (GemmaModel)
    ├── embed_tokens (removed in this implementation)
    ├── layers[0..num_hidden_layers-1]
    │   ├── input_layernorm
    │   ├── self_attn
    │   │   ├── q_proj
    │   │   ├── k_proj
    │   │   ├── v_proj
    │   │   ├── o_proj
    │   │   └── head_dim (attribute)
    │   ├── post_attention_layernorm
    │   └── mlp
    │       ├── up_proj
    │       └── down_proj
    └── norm (final layer normalization)
```

## Configuration Parameters
The code instantiates Gemma with these settings:
- **head_dim**: Custom parameter
- **hidden_size**: Model width dimension
- **intermediate_size**: MLP expansion dimension
- **num_attention_heads**: Attention head count
- **num_hidden_layers**: Transformer depth
- **num_key_value_heads**: KV cache heads
- **vocab_size**: 257,152 tokens
- **hidden_activation**: "gelu_pytorch_tanh"
- **torch_dtype**: "float32"
- **use_adarms**: Boolean for adaptive layer modulation
- **adarms_cond_dim**: Conditioning dimension when enabled

## Key Implementation Details
The attention mechanism uses "eager" computation via `modeling_gemma.eager_attention_forward()`, rotary position embeddings through `modeling_gemma.apply_rotary_pos_emb()`, and gated residual connections via `modeling_gemma._gated_residual()`. Layer outputs concatenate embeddings from multiple models before attention processing, enabling cross-model interaction within shared transformer layers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T10:41:49.902999+00:00_

# LoRA Fine-Tuning for Pi0.5: Current Status

## Issue Summary
A user inquired whether existing Pi0 LoRA fine-tuning configurations could be adapted for Pi0.5 by simply replacing model references and updating checkpoint weights.

## Current Status
The repository lacks explicit Pi0.5 LoRA fine-tuning configurations in `src/openpi/training/config.py`, though Pi0 examples are available.

## Proposed Approach
The user suggested a straightforward adaptation strategy: "just replace `pi0` with `pi05` and set weights url to be `gs://openpi-assets/checkpoints/pi05_base/params`" without additional modifications.

## Technical Details from Example
The existing Pi0-FAST configuration demonstrates key LoRA setup components:
- Model instantiation with specific action dimensions and token lengths
- PaliGemma variant selection ("gemma_2b_lora")
- Checkpoint weight loading mechanism
- Freeze filter configuration matching the model setup
- EMA decay disabled for LoRA training

## Key Consideration
The user appropriately questions whether this simple substitution is sufficient or if other changes are necessary—suggesting this remains an open question in the community documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T10:41:49.903132+00:00_

# LoRA Training Support Proposal for π0.5 (PyTorch)

## Implementation Status
The proposal is currently **open** (Issue #842, filed January 11, 2026). The author has completed a working implementation and indicates readiness to submit a pull request pending project alignment approval.

## Technical Approach

**Pure PyTorch Implementation**: The solution avoids external dependencies like `peft`, remaining "lightweight and efficient" while maintaining tight integration with the existing codebase.

## Target Layers for LoRA Adapters

The implementation injects adapters into transformer components:
- **Attention mechanisms**: `q_proj`, `k_proj`, `v_proj`, `o_proj`
- **FFN/MLP layers**: `gate_proj`, `up_proj`, `down_proj`

## Configuration & Performance Metrics

**Tested Configuration** (Hybrid approach with LoRA rank=16):
- Total trainable parameters: 441.15M (12.11% of model)
- LoRA adapters alone: 26.54M (0.73%)
- Vision encoder (unfrozen): 412.44M

**Validation Results**:
- Hardware: Single RTX 4090 (24GB VRAM)
- Training: 30k steps, batch size 16, ~16GB peak usage
- Libero benchmark performance averaged 96.95% across spatial, object, goal, and 10-task variants

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T10:41:49.903296+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/blog/pi0",
  "prompt": "Extract all technical details about pi0 and pi0-FAST models: parameter counts, architecture details, hidden dimensions, number of layers, training data, GPU requirements, checkpoint sizes, model variants. Include any performance benchmarks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/blog/pi0",
    "prompt": "Extract all technical details about pi0 and pi0-FAST models: parameter counts, architecture details, hidden dimensions, number of layers, training data, GPU requirements, checkpoint sizes, model variants. Include any performance benchmarks."
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-15T10:41:49.903431+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://deepwiki.com/Physical-Intelligence/openpi",
  "prompt": "Extract the complete architecture overview: model structure, module paths, layer counts, hidden dimensions, how JAX and PyTorch implementations relate, data flow, training pipeline. Focus on technical details about the model internals."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://deepwiki.com/Physical-Intelligence/openpi",
    "prompt": "Extract the complete architecture overview: model structure, module paths, layer counts, hidden dimensions, how JAX and PyTorch implementations relate, data flow, training pipeline. Focus on technical details about the model internals."
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T10:41:49.903553+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2410.24164v1",
  "prompt": "Extract ALL technical architecture details from the pi0 paper: model size, hidden dimensions, number of layers, attention heads, action expert dimensions, SigLIP variant, training details, inference speed, action chunk size, flow matching parameters. Focus on Section 3 (Method) and any architecture figures/tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2410.24164v1",
    "prompt": "Extract ALL technical architecture details from the pi0 paper: model size, hidden dimensions, number of layers, attention heads, action expert dimensions, SigLIP variant, training details, inference speed, action chunk size, flow matching parameters. Focus on Section 3 (Method) and any architecture figures/tables."
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T10:41:49.903684+00:00_

# OpenPI Architecture Overview

## Model Structure

The documentation provides architectural comparisons rather than detailed internal specifications. The three model variants share a common inheritance pattern:

**Core Interface:** All models inherit from `BaseModel` with the signature: `__call__(observation: Observation, actions: Actions | None, train: bool)`

**Model Variants:**

| Model | Generation Method | Frameworks |
|-------|------------------|-----------|
| π₀ | "Flow matching to generate continuous actions through iterative denoising" | JAX, PyTorch |
| π₀-FAST | "Tokenizes actions into discrete tokens via the FAST action tokenizer, enabling autoregressive generation" | JAX only |
| π₀.₅ | "Flow matching + knowledge insulation" | JAX, PyTorch |

## Data Flow Architecture

**Input Structure:**
- `Observation` dataclasses containing: `images` (camera views), `state` (proprioceptive data), `prompt_tokens` (language instructions)
- Output: `Actions` arrays with shape `(batch_size, action_horizon, action_dim)`

**Processing Pipeline:** "Four-stage transforms (repack→data→normalize→model)"

## Framework Comparison

The document contrasts JAX and PyTorch capabilities:

| Feature | JAX | PyTorch |
|---------|-----|---------|
| Mixed Precision | "bf16 activations, fp32 weights/gradients" | Full bf16 or fp32 only |
| Distributed Training | Multi-GPU sharding | DDP only |
| Fine-tuning | LoRA supported | Full fine-tuning only |
| Dataset Support | RLDS/DROID native | LeRobot only |

**Critical Gap:** The provided content lacks specific layer counts, hidden dimensions, parameter counts, and detailed module paths—these technical internals are not documented in the overview material.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-15T10:41:49.903843+00:00_

# Technical Details: π0 and π0-FAST Models

Based on the provided documentation, here are the available technical specifications:

## Model Architecture & Parameters

**Unfortunately, specific technical details are NOT provided in this document:**
- ❌ Parameter counts
- ❌ Hidden dimensions
- ❌ Number of transformer layers
- ❌ Model size variants

## Training Data

- **7 robotic platforms** used for training
- **68 unique tasks** covered
- **π0-FAST+**: Trained on **1 million action sequences** from:
  - Single-arm robots
  - Bimanual manipulators
  - Mobile manipulation robots

## Architecture Overview

π0 is a **Vision-Language-Action (VLA) model** based on:
- **Transformers** (similar foundation to PaliGemma)
- **Flow matching** for action generation (continuous normalizing flows)
- **Three token types**:
  - Prefix tokens (images + text)
  - State tokens (robot environment state)
  - Action tokens (motor commands)

## Key Differences: π0 vs π0-FAST

| Aspect | π0 | π0-FAST |
|--------|-----|---------|
| Action Generation | Flow matching (diffusion-based) | Autoregressive |
| Training Speed | Baseline | **5x faster** |
| Tokenization | Direct action output | FAST tokenizer |

## FAST Tokenizer Specifications

**Hyperparameters:**
- Scaling coefficient (for DCT rounding)
- BPE vocabulary size
- **2 total hyperparameters** (described as robust across datasets)

**Process:**
1. Quantile normalization to [-1, 1]
2. Discrete Cosine Transform (DCT) per action dimension
3. Scale-and-round operation
4. Byte Pair Encoding (BPE) compression

## Installation

```bash
pip install -e ".[pi0]"
```

## Model Access

- **π0 Collection**: [Hugging Face LeRobot π0 Models](https://huggingface.co/collections/lerobot/pi0-models-67a0f92dc62e52ace7220eba)
- **π0-FAST Collection**: [Hugging Face LeRobot π0-FAST Models](https://huggingface.co/collections/lerobot/pi0fast-models-67eab97cc139d6f20513ff4a)
- **FAST Tokenizer**: [physical-intelligence/fast](https://huggingface.co/physical-inte
…[truncated 815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T10:41:49.904047+00:00_

# π₀ Technical Architecture Details

## Model Size & Parameters
The π₀ model comprises 3.3 billion total parameters:
- **VLM Backbone**: PaliGemma (3B parameters)
- **Action Expert**: 300M parameters (initialized from scratch)

## VLM Backbone Configuration
Based on Gemma 2B with these specifications:
- Width: 2,048
- Depth: 18 layers
- MLP dimension: 16,384
- Attention heads: 18
- Key-value heads: 1
- Head dimension: 256
- Uses multi-query attention

## Action Expert Architecture
Downsized for inference efficiency:
- Width: 1,024
- MLP dimension: 4,096
- Routed separately from VLM backbone through mixture-of-experts pattern

## Action Representation
- **Action Chunk Size**: H=50 (future action steps)
- **Control Frequency**: Up to 50 Hz for dexterous tasks
- **Action Dimensionality**: Maximum 18 dimensions (accommodates dual 6-DoF arms + 2 grippers + mobile base + torso)
- Zero-padding used for robots with lower-dimensional action spaces

## Flow Matching Configuration
- **Integration Steps**: 10 steps at inference
- **Integration Step Size**: δ=0.1
- **Timestep Sampling**: Beta distribution emphasizing lower (noisier) timesteps
- **Cutoff Parameter**: s=0.999

## Input/Output Processing
- **Input modalities**: 2-3 RGB images, language commands, proprioceptive state (joint angles)
- **Attention mask**: Blockwise causal with 3 blocks (images/language, state, actions)
- **Action tokens**: Full bidirectional attention among action tokens

## Inference Performance
On NVIDIA RTX 4090:
- Image encoding: 14 ms
- Observation forward pass: 32 ms
- 10× action flow passes: 27 ms
- **Total on-board inference**: 73 ms
- Off-board (with network): 86 ms

## Training Details
- **Pre-training mixture**: 903M proprietary timesteps + OXE/Bridge/DROID data (total ~10,000 hours)
- **Data weighting**: Task-robot combinations weighted by n^0.43 for balance
- **Training steps**: 700k (full model) vs 160k (compute-parity comparison)
- **Flow matching loss**: Conditional on noisy action dis
…[truncated 47 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T10:41:49.904242+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openpi checkpoint size GB download pi0_base pi0_fast_base \"gs://openpi-assets\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openpi checkpoint size GB download pi0_base pi0_fast_base \"gs://openpi-assets\""
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-15T10:41:49.904363+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/gemma.py",
  "prompt": "Extract ONLY the variant configuration definitions - the exact code that maps variant names to (width, depth, mlp_dim, num_heads, num_kv_heads, head_dim) values. Show ALL defined variants including LoRA variants. Also show the LoRA config defaults (rank, alpha, target modules)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models/gemma.py",
    "prompt": "Extract ONLY the variant configuration definitions - the exact code that maps variant names to (width, depth, mlp_dim, num_heads, num_kv_heads, head_dim) values. Show ALL defined variants including LoRA variants. Also show the LoRA config defaults (rank, alpha, target modules)."
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-15T10:41:49.904502+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0 LIBERO-Plus perturbed evaluation benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0 LIBERO-Plus perturbed evaluation benchmark 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T10:41:49.904624+00:00_

# Gemma Variant Configurations

Based on the source code, here are all defined variants:

## Standard Variants

**dummy:**
- width: 64, depth: 4, mlp_dim: 128, num_heads: 8, num_kv_heads: 1, head_dim: 16

**gemma_300m:**
- width: 1024, depth: 18, mlp_dim: 4096, num_heads: 8, num_kv_heads: 1, head_dim: 256
- Parameters: ~311M

**gemma_2b:**
- width: 2048, depth: 18, mlp_dim: 16,384, num_heads: 8, num_kv_heads: 1, head_dim: 256

## LoRA Variants

**gemma_300m_lora:**
- Same architecture as gemma_300m
- LoRA configs: attn (rank=32, alpha=32.0), ffn (rank=32, alpha=32.0)

**gemma_2b_lora:**
- Same architecture as gemma_2b
- LoRA configs: attn (rank=16, alpha=16.0), ffn (rank=16, alpha=16.0)

## LoRA Configuration Pattern

LoRA is applied to two target modules: attention layers ("attn") and feed-forward networks ("ffn"), each with independently specified rank and scaling alpha values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-15T10:41:49.904773+00:00_

Web search results for query: "openpi checkpoint size GB download pi0_base pi0_fast_base "gs://openpi-assets""

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"openpi — Trossen Robotics Trossen Arm Documentation","url":"https://docs.trossenrobotics.com/trossen_arm/main/tutorials/openpi.html"},{"title":"Trendshift - Ask AI","url":"https://trendshift.io/admin/repository/ask-ai/12902"},{"title":"openpi/src/openpi/training/config.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/src/openpi/training/config.py"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"GitHub - qrafty-ai/pi-openpi: OpenPIE - Open source Pi0 implementation with RECAP training · GitHub","url":"https://github.com/qrafty-ai/pi-openpi"},{"title":"GitHub - gist-ailab/contact-openpi · GitHub","url":"https://github.com/gist-ailab/contact-openpi"},{"title":"\"\"\"See _CONFIGS for the list of available configs.\"\"\" import abc","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py"},{"title":"OpenPi π₀.₅ on Jetson Thor | Jetson AI Lab","url":"https://www.jetson-ai-lab.com/tutorials/openpi_on_thor/"},{"title":"Question about downloading checkpoint of pi0.5 · Issue #597 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/597"}]

Based on the search results, I found information about OpenPI checkpoints and their download locations. Here's what I found:

## Checkpoint Downloads

Checkpoints are automatically downloaded from gs://openpi-assets and are cached in ~/.cache/openpi when needed. You can overwrite the download path by setting the OPENPI_DATA_HOME environment variable.

## Available Base Models

The π₀ base model is available at `gs://openpi-assets/checkpoints/pi0_base` for fine-t
…[truncated 665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T10:41:49.904953+00:00_

Web search results for query: "pi0 LIBERO-Plus perturbed evaluation benchmark 2025 2026"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"}]

I found comprehensive information about your search query. Here are the key findings:

## LIBERO-Plus Benchmark Overview

LIBERO-Plus is focused on in-depth robustness analysis of Vision-Language-Action models. The benchmark offers a robust evaluation framework with 7 perturbation dimensions and 21 sub-dimensions, providing a fine-grained difficulty scale from L1 to L5 for systematic assessment of model performance across various challenges.

## 
…[truncated 1065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T10:41:49.905123+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/sylvestf/LIBERO-plus",
  "prompt": "Extract: how to run perturbed evaluation with pi0, what perturbation types are supported, how to integrate with openpi, setup requirements, evaluation scripts."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/sylvestf/LIBERO-plus",
    "prompt": "Extract: how to run perturbed evaluation with pi0, what perturbation types are supported, how to integrate with openpi, setup requirements, evaluation scripts."
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-15T10:41:49.905243+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openpi pi0 model checkpoint file size safetensors GB inference memory usage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openpi pi0 model checkpoint file size safetensors GB inference memory usage"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-15T10:41:49.905361+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/preprocessing_pytorch.py",
  "prompt": "Extract the preprocessing pipeline: how images are processed, sequence length computation, how tokens are counted, any information about total sequence length during inference."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/models_pytorch/preprocessing_pytorch.py",
    "prompt": "Extract the preprocessing pipeline: how images are processed, sequence length computation, how tokens are counted, any information about total sequence length during inference."
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T10:41:49.905507+00:00_

# Image Preprocessing Pipeline Analysis

## Image Processing Steps

The preprocessing function handles images through these sequential operations:

1. **Format Normalization**: Images are converted to `[B, H, W, C]` format if originally in `[B, C, H, W]`

2. **Resizing**: Images are resized to `(224, 224)` resolution using `"resize_with_pad_torch"` if needed

3. **Training Augmentations** (when `train=True`):
   - **Non-wrist cameras**: Random cropping at 95% of original size, followed by resizing back to original dimensions
   - **Rotation**: Random angles between -5 and 5 degrees applied via `grid_sample`
   - **Brightness**: Multiplicative factor between 0.7-1.3
   - **Contrast**: Scaling relative to mean intensity (factor 0.6-1.4)
   - **Saturation**: Color channel adjustment (factor 0.5-1.5)
   - **Value clamping**: All augmented values constrained to `[0, 1]` range

4. **Format Conversion**: Final output returns to `[B, C, H, W]` format

## Mask Generation

"masks are created as all-ones if not present in observation, otherwise preserved from input"

## Sequence Length Information

**Not provided in this document.** The code focuses on per-image preprocessing but contains no information regarding total sequence length during inference, token counting methodology, or inference-time sequence composition.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-15T10:41:49.905646+00:00_

# LIBERO-Plus: Evaluation and Integration Details

## Perturbation Types Supported

The benchmark includes **7 perturbation dimensions**:

1. Objects Layout - confounding objects and target displacement
2. Camera Viewpoints - position, orientation, and field-of-view changes
3. Robot Initial States - manipulator pose variations
4. Language Instructions - LLM-based instruction rewrites
5. Light Conditions - intensity, direction, color, and shadow variations
6. Background Textures - scene and surface appearance changes
7. Sensor Noise - photometric distortions and image degradation

## Running Perturbed Evaluation

The documentation states: "The evaluation method is almost identical to `LIBERO`. The only required modification is adjusting `num_trials_per_task` from 50 to 1 in your configuration."

Task mappings between IDs, perturbation categories, and difficulty levels are available in `.libero/libero/benchmark/task_classification.json`.

## π₀ Model Performance

π₀ achieved 53.6% average performance across perturbations, with notable strength in light conditions (85.0%) and background textures (81.4%), but weakness in robot initial states (6.0%).

## Setup Requirements

Installation requires:
- Clone the LIBERO-Plus repository
- Install with `pip install -e .`
- Download assets from Hugging Face
- Install additional dependencies: `apt install libexpat1 libfontconfig1-dev libpython3-stdlib libmagickwand-dev`
- Run `pip install -r extra_requirements.txt`

## Integration Note

The repository explicitly states: "Simply replace the originally installed LIBERO repository with our repository without modifying your code," enabling seamless integration with existing projects.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-15T10:41:49.905859+00:00_

Web search results for query: "openpi pi0 model checkpoint file size safetensors GB inference memory usage"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"OpenPi π₀.₅ on Jetson Thor | Jetson AI Lab","url":"https://www.jetson-ai-lab.com/tutorials/openpi_on_thor/"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"Torch SD-based models tensor invalid for input size · Issue #95 · huggingface/safetensors","url":"https://github.com/huggingface/safetensors/issues/95"},{"title":"Trendshift - Ask AI","url":"https://trendshift.io/admin/repository/ask-ai/12902"},{"title":"Understand downloading the Model Checkpoint File (.ckpt/.safetensors)","url":"https://app.studyraid.com/en/read/32065/1401082/downloading-the-model-checkpoint-file-ckptsafetensors"},{"title":"exla-ai/openpie-0.6 · Hugging Face","url":"https://huggingface.co/exla-ai/openpie-0.6"},{"title":"openpi — Trossen Robotics Trossen Arm Documentation","url":"https://docs.trossenrobotics.com/trossen_arm/main/tutorials/openpi.html"},{"title":"PEFT checkpoint format","url":"https://huggingface.co/docs/peft/en/developer_guides/checkpoint"},{"title":"\"\"\"See _CONFIGS for the list of available configs.\"\"\" import abc","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py"}]

Let me search for more specific information about the model file size and inference memory requirements.

Links: [{"title":"Estimate GPU Memory (VRAM) - Shayan Geek","url":"https://shayangeek.com/en/estimate-gpu-memory-needed-for-ai-model/"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"How Much Memory Does Your LLM Really Need? | Skymod","url":"https://skymod.tech/how-much-memory-does-your-llm-really-need-a-practical-guide-to-inference-vram-consum
…[truncated 4185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-15T10:41:49.906044+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/lerobot/pi0_base",
  "prompt": "Extract ALL information: model size, parameter count, checkpoint file sizes, safetensors size, configuration, architecture details, required libraries, usage examples."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/lerobot/pi0_base",
    "prompt": "Extract ALL information: model size, parameter count, checkpoint file sizes, safetensors size, configuration, architecture details, required libraries, usage examples."
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-15T10:41:49.906166+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/pi0",
  "prompt": "Extract ALL technical details: model architecture, parameter counts, training configuration, action dimensions, image input specs, sequence length, inference code examples, GPU memory requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/pi0",
    "prompt": "Extract ALL technical details: model architecture, parameter counts, training configuration, action dimensions, image input specs, sequence length, inference code examples, GPU memory requirements."
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-15T10:41:49.906351+00:00_

# π₀ (Pi0)

π₀ is a **Vision-Language-Action model for general robot control**, from Physical Intelligence. The LeRobot implementation is adapted from their open source [OpenPI](https://github.com/Physical-Intelligence/openpi) repository.

## Model Overview

π₀ represents a breakthrough in robotics as the first general-purpose robot foundation model developed by [Physical Intelligence](https://www.physicalintelligence.company/blog/pi0). Unlike traditional robot programs that are narrow specialists programmed for repetitive motions, π₀ is designed to be a generalist policy that can understand visual inputs, interpret natural language instructions, and control a variety of different robots across diverse tasks.

### The Vision for Physical Intelligence

As described by Physical Intelligence, while AI has achieved remarkable success in digital domains, from chess-playing to drug discovery, human intelligence still dramatically outpaces AI in the physical world. To paraphrase Moravec's paradox, winning a game of chess represents an "easy" problem for AI, but folding a shirt or cleaning up a table requires solving some of the most difficult engineering problems ever conceived. π₀ represents a first step toward developing artificial physical intelligence that enables users to simply ask robots to perform any task they want, just like they can with large language models.

### Architecture and Approach

π₀ combines several key innovations:

- **Flow Matching**: Uses a novel method to augment pre-trained VLMs with continuous action outputs via flow matching (a variant of diffusion models)
- **Cross-Embodiment Training**: Trained on data from 8 distinct robot platforms including UR5e, Bimanual UR5e, Franka, Bimanual Trossen, Bimanual ARX, Mobile Trossen, and Mobile Fibocom
- **Internet-Scale Pre-training**: Inherits semantic knowledge from a pre-trained 3B parameter Vision-Language Model
- **High-Frequency Control**: Outputs motor commands at up to 50 Hz for real-time dextero
…[truncated 4053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T10:41:49.906558+00:00_

# LeRobot π₀ (Pi0) Base Model - Complete Information

## Model Overview
- **Model Name:** lerobot/pi0_base
- **Type:** Vision-Language-Action (VLA) Foundation Model
- **Organization:** Physical Intelligence (via LeRobot/Hugging Face)
- **License:** Gemma
- **Original Paper:** "π0: A Vision-Language-Action Flow Model for General Robot Control"
- **Reference Implementation:** https://github.com/Physical-Intelligence/openpi

## Model Specifications

### Architecture & Parameters
- **Total Parameters:** 4B (4 Billion)
- **Tensor Type:** F32 (Float32)
- **Format:** Safetensors
- **Action Representation:** Continuous
- **Training Objective:** Flow matching

### Model Capabilities
- **Inputs:** 
  - Multi-view images
  - Proprioceptive/state information
  - Optional language instructions
- **Outputs:** Continuous robot actions
- **Intended Use:** Base model for fine-tuning on specific robotics tasks

## Installation & Usage

### Installation
```bash
pip install "lerobot[pi]@git+https://github.com/huggingface/lerobot.git"
```

### Quick Start - Inference
```python
import torch
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.policies.factory import make_pre_post_processors
from lerobot.policies.pi0 import PI0Policy

# Load policy
model_id = "lerobot/pi0_base"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

policy = PI0Policy.from_pretrained(model_id).to(device).eval()

preprocess, postprocess = make_pre_post_processors(
    policy.config,
    model_id,
    preprocessor_overrides={"device_processor": {"device": str(device)}},
)

# Load dataset
dataset = LeRobotDataset("lerobot/libero")

# Inference on a frame
episode_index = 0
from_idx = dataset.meta.episodes["dataset_from_index"][episode_index]
frame_index = from_idx
frame = dict(dataset[frame_index])

batch = preprocess(frame)
with torch.inference_mode():
    pred_action = policy.select_action(batch)
    pred_action = postprocess(pred_action)
```

### Training/Fine-tuning
```b
…[truncated 1605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T10:41:49.906775+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/ 2>/dev/null || echo \"Directory does not exist\"",
  "description": "Check if artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/ 2>/dev/null || echo \"Directory does not exist\"",
    "description": "Check if artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T10:41:49.906900+00:00_

Directory does not exist

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-15T10:41:49.907020+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts",
  "description": "Create artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts",
    "description": "Create artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T10:41:49.907132+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-15T10:41:49.907339+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/openpi_research_report.md",
  "content": "# OpenPI (π₀) Codebase 深度技术调研报告\n\n> 调研日期：2026-05-15\n> 目标：评估在 π₀ 上实施 Meta-Brain LoRA Routing 的技术可行性\n\n---\n\n## 1. π₀ 模型架构与加载\n\n### 1.1 整体架构\n\nπ₀ 是 Vision-Language-Action (VLA) flow model，基于 PaliGemma 2B VLM 扩展而来，采用 MoE-like 架构（Mixture of Tokens, MoT）。\n\n**核心组件**：\n- **视觉编码器**: SigLIP So400m/14（~400M 参数）\n- **语言模型 (PaliGemma backbone)**: Gemma 2B（~2.6B 参数）\n- **动作专家 (Action Expert)**: Gemma 300M（~315M 参数，从零初始化）\n- **投影层**: action_in_proj, action_out_proj, time MLPs\n\n**代码位置**:\n- JAX 实现: `src/openpi/models/pi0.py` (Pi0 class, lines 47-176)\n- PyTorch 实现: `src/openpi/models_pytorch/pi0_pytorch.py` (PI0Pytorch class)\n- 配置: `src/openpi/models/pi0_config.py`\n- Gemma 定义: `src/openpi/models/gemma.py` (JAX), `src/openpi/models_pytorch/gemma_pytorch.py` (PyTorch)\n\n### 1.2 详细架构参数\n\n| 组件 | 参数 | 值 |\n|------|------|-----|\n| **Gemma 2B (PaliGemma LLM)** | width (hidden_dim) | 2048 |\n| | depth (层数) | **18** |\n| | mlp_dim | 16,384 |\n| | num_heads | 8 |\n| | num_kv_heads | 1 (Multi-Query Attention) |\n| | head_dim | 256 |\n| **Gemma 300M (Action Expert)** | width | 1024 |\n| | depth | **18** |\n| | mlp_dim | 4,096 |\n| | num_heads | 8 |\n| | num_kv_heads | 1 |\n| | head_dim | 256 |\n| **SigLIP So400m/14** | embedding_dim | ~1152 |\n| | patch_size | 14×14 |\n| | input_resolution | 224×224 |\n| | patches/image | 256 (16×16) |\n\n**来源**: `src/openpi/models/gemma.py` 中的 variant 定义:\n```python\n# gemma_2b: width=2048, depth=18, mlp_dim=16384, num_heads=8, num_kv_heads=1, head_dim=256\n# gemma_300m: width=1024, depth=18, mlp_dim=4096, num_heads=8, num_kv_heads=1, head_dim=256\n```\n\n### 1.3 注意力机制\n\n采用 block-wise causal masking（`src/openpi/models/pi0.py`, lines 20-38）:\n- VLM block: 仅关注自身（prefix tokens: images + language）\n- State/proprioception block: 关注自身 + VLM（共享 action expert 权重）\n- Action block: 关注所有 tokens（完全双向）\n\n**来源**: `make_attn_mask()` 函数，通过 cumulative mask 实现不同的注意力模式。\n\n### 1.4 动作生成 (Flow Matching)\n\n**训练** (`compute_loss`, lines 119-150):\n- 时间步 t ~ Beta(1.5, 1)，缩放到 [0.001, 0.999]\n- 噪声状态: x_t = t·noise + (1-t)·actions\n- 目标速度: u_t = noise - actions\n- 损失: MSE(v_t, u_t)\n\n**推理** (`sample_actions`, lines 152-201):\n- 10 步 Euler 积分: t=1 (噪声) → t=0 (目标)\n- 步长: dt = -1/num_steps = -0.1\n- 迭代: x_{t+dt} = x_t + dt·v_t\n- 使用 KV-cache 优化 prefix tokens\n\n### 1.5 Checkpoint 来源与大小\n\n| Checkpoint | 来源 | 格式 |\n|------------|------|------|\n| pi0_base | `gs://openpi-assets/checkpoints/pi0_base/params` | JAX (Flax) |\n| pi0_fast_base | `gs://openpi-assets/checkpoints/pi0_fast_base/params` | JAX (Flax) |\n| pi05_base | `gs://openpi-assets/checkpoints/pi05_base/params` | JAX (Flax) |\n| lerobot/pi0_base | HuggingFace Hub | SafeTensors (PyTorch) |\n| lerobot/pi0_libero_base | HuggingFace Hub | SafeTensors (PyTorch) |\n\n**自动下载**：默认缓存到 `~/.cache/openpi`，可通过 `OPENPI_DATA_HOME` 修改。无需申请，直接公开下载。\n\n**模型大小**:\n- 总参数量: ~3.3B（HuggingFace 标注为 4B，含 F32 精度下的 embeddings/projections）\n- Checkpoint 大小 (fp32): ~13.2 GB\n- Checkpoint 大小 (bf16): ~6.6 GB\n\n### 1.6 显存需求\n\n| 模式 | 显存需求 | 推荐 GPU |\n|------|---------|----------|\n| 推理 (bf16) | > 8 GB | RTX 4090 / A6000 |\n| LoRA 微调 | > 22.5 GB | RTX 4090 / A6000 |\n| 全量微调 | > 70 GB | A100 80GB / H100 |\n\n**来源**: OpenPI README 文档。\n\n### 1.7 加载方式\n\n**OpenPI 原生 (JAX)**:\n```python\n# src/openpi/training/config.py\nmodel = config.model.create(model_rng)\n# 通过 _load_weights_and_validate() 加载预训练权重\n```\n\n**OpenPI PyTorch**:\n```python\nimport openpi.models_pytorch.pi0_pytorch\nimport safetensors.torch\nmodel = PI0Pytorch(model_cfg).to(device)\nsafetensors.torch.load_model(model, model_path)\n```\n\n**LeRobot (HuggingFace)**:\n```python\nfrom lerobot.policies.pi0 import PI0Policy\npolicy = PI0Policy.from_pretrained(\"lerobot/pi0_base\").to(device).eval()\n```\n\n---\n\n## 2. LIBERO 环境集成\n\n### 2.1 已有 LIBERO 支持\n\nOpenPI 对 LIBERO 有**完整的一等支持**：\n\n**关键文件**:\n- 评测脚本: `examples/libero/main.py`\n- 数据转换: `examples/libero/convert_libero_data_to_lerobot.py`\n- 策略映射: `src/openpi/policies/libero_policy.py`\n- Docker 配置: `examples/libero/Dockerfile`, `examples/libero/compose.yml`\n- 训练配置: `src/openpi/training/config.py` 中的 `LeRobotLiberoDataConfig`\n\n**预训练 LIBERO checkpoint**:\n- `gs://openpi-assets/checkpoints/pi05_libero/params`（π₀.₅ LIBERO 微调版，96.85% 平均成功率）\n- HuggingFace: `lerobot/pi0_libero_base`\n\n### 2.2 LIBERO 评测调用方式\n\n`examples/libero/main.py` 实现了完整的评测流程：\n\n1. 启动 Policy Server: `scripts/serve_policy.py`\n2. 客户端通过 WebSocket 连接: `WebsocketClientPolicy(host, port)`\n3. 评测循环:\n   - 重置环境 → 等待物体稳定 (num_steps_wait)\n   - 每 `replan_steps=5` 步请求新 action chunk\n   - 记录成功率和视频\n\n**配置格式** (通过命令行参数):\n- `--task_suite_name`: LIBERO 任务套件 (spatial/object/goal/10)\n- `--num_trials_per_task`: 每个任务的试验次数 (默认 50)\n- `--resize_size`: 图像分辨率 (224)\n- `SERVER_ARGS`: 指定 checkpoint\n\n**观测格式** (LiberoInputs, `src/openpi/policies/libero_policy.py`):\n- State: `observation/state` — 8 维向量（end-effector position + rotation + gripper）\n- Base image: `observation/image` — 224×224 RGB（第三人称）\n- Wrist image: `observation/wrist_image` — 224×224 RGB（左手腕相机）\n- Right wrist: 零填充（LIBERO 只有 2 个相机）\n\n**动作格式** (LiberoOutputs):\n- 输出前 7 维动作（从 action_dim=32 的填充中截取）\n- 7 维 = 6-DoF end-effector + 1 gripper\n\n### 2.3 LIBERO-Plus 扰动评测\n\n**支持状态**: 可用，但需要额外安装 LIBERO-Plus 替代标准 LIBERO。\n\n**LIBERO-Plus** (https://github.com/sylvestf/LIBERO-plus) 提供 7 个扰动维度:\n1. 物体布局 (Objects Layout)\n2. 相机视角 (Camera Viewpoints)\n3. 机器人初始状态 (Robot Initial States)\n4. 语言指令 (Language Instructions)\n5. 光照条件 (Light Conditions)\n6. 背景纹理 (Background Textures)\n7. 传感器噪声 (Sensor Noise)\n\n**集成方式**: \"Simply replace the originally installed LIBERO repository with our repository without modifying your code\" — 直接替换 LIBERO 库即可，评测代码无需修改。唯一改动: `num_trials_per_task` 从 50 改为 1。\n\n**π₀ 在 LIBERO-Plus 上的基线表现**: 平均 53.6%（光照 85.0%，背景 81.4%，但机器人初始状态仅 6.0%）。\n\n---\n\n## 3. LoRA Fine-tuning 支持\n\n### 3.1 JAX 实现 — 已有完整支持\n\n**代码位置**: `src/openpi/models/lora.py`\n\n**LoRA 变体定义** (`src/openpi/models/gemma.py`):\n```\ngemma_2b_lora:    rank=16, alpha=16.0 (attn + ffn)\ngemma_300m_lora:  rank=32, alpha=32.0 (attn + ffn)\n```\n\n**训练配置** (`src/openpi/training/config.py`):\n- 使用 `paligemma_variant=\"gemma_2b_lora\"` + `action_expert_variant=\"gemma_300m_lora\"`\n- Freeze filter: 冻结非 LoRA 的 LLM 参数，仅训练 LoRA 权重\n- EMA decay: 禁用 (`ema_decay=None`)\n- 其他默认: 30k steps, batch_size=32, AdamW + Cosine Decay\n\n**LoRA 目标模块**:\n- Attention: q_proj, k_proj, v_proj, o_proj (通过 Einsum 类)\n- FFN: gate_proj, up_proj, down_proj (通过 FeedForward 类)\n\n**LoRA 实现特点**:\n- 支持 RSLoRA (rank-stabilized LoRA): `scaling = alpha / sqrt(rank)`\n- 纯 additive: `output = base_output + (x @ w_a @ w_b) * scaling`\n- 不依赖外部库（如 peft），自实现\n\n### 3.2 PyTorch 实现 — 官方不支持，社区有方案\n\n**官方状态**: OpenPI 的 PyTorch 训练脚本 (`scripts/train_pytorch.py`) **不支持 LoRA**，仅支持全量微调。\n\n**社区方案** (Issue #842):\n- 纯 PyTorch LoRA 实现，不依赖 peft\n- 注入到 Attention (q/k/v/o_proj) 和 MLP (gate/up/down_proj)\n- Rank=16 时 LoRA 参数: 26.5M (0.73% of total)\n- 可选解冻 Vision Encoder: 额外 412M trainable (12.11% total)\n- 单 RTX 4090 可训练，~16GB 峰值显存\n- LIBERO 上达到 96.95% 平均成功率\n- **状态**: PR 未合并，但代码完整可用\n\n**LeRobot 方案**:\n- HuggingFace LeRobot 提供了 Pi0 的 PyTorch 训练脚本\n- 支持 `train_expert_only=true` 冻结 VLM 仅训练 action expert\n- 不原生支持 LoRA，但可通过 HuggingFace PEFT 库扩展\n\n### 3.3 推荐方案\n\n对于本项目的 Meta-Brain LoRA Routing：\n1. **首选**: 基于 OpenPI JAX 实现，已有完整 LoRA 支持\n2. **备选**: 采用 Issue #842 的 PyTorch LoRA 实现（更灵活，更容易加 hook）\n3. **替代**: 使用 LeRobot PyTorch + HuggingFace PEFT 库\n\n---\n\n## 4. 中间层激活提取\n\n### 4.1 模型前向传播路径\n\n**JAX 实现** (`src/openpi/models/pi0.py`):\n```\nPi0.__call__()\n  → embed_prefix(obs)        # SigLIP 编码图像 + tokenize 文本\n  → embed_suffix(obs, noisy_actions, timestep)  # 编码动作 + 时间步\n  → self.PaliGemma['llm'](tokens, ...)  # Gemma Module forward (18 layers)\n  → action_out_proj(...)     # 投影到动作空间\n```\n\n**PyTorch 实现** (`src/openpi/models_pytorch/pi0_pytorch.py`):\n```\nPI0Pytorch.forward(observation, actions)\n  → _preprocess_observation()\n  → embed_prefix(obs)\n  → embed_suffix(obs, noisy_actions, timestep)\n  → paligemma_with_expert(tokens, ...)\n  → action_out_proj(...)\n```\n\n### 4.2 已有 Hook 机制\n\n**OpenPI 没有已有的 hook 机制或中间层输出接口。** 需要自行添加。\n\n### 4.3 PyTorch Hook 注册方案（推荐）\n\nPyTorch 实现支持标准的 `register_forward_hook`，模块路径如下：\n\n**PaliGemma LLM 层 (hidden_dim=2048)**:\n```python\nmodel.paligemma_with_expert.paligemma.language_model.layers[i]\n# i = 0..17 (共 18 层)\n\n# 子模块:\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].self_attn\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].self_attn.q_proj\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].self_attn.o_proj\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].mlp\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].input_layernorm\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].post_attention_layernorm\n```\n\n**Action Expert 层 (hidden_dim=1024)**:\n```python\nmodel.paligemma_with_expert.gemma_expert.model.layers[i]\n# i = 0..17 (共 18 层)\n# 子模块结构同上\n```\n\n**Vision Encoder 层**:\n```python\nmodel.paligemma_with_expert.paligemma.vision_tower.layers[i]\n```\n\n### 4.4 关键发现：层数只有 18，不是 32！\n\n**⚠️ 重要**: π₀ 的 Transformer 深度为 **18 层**（layers[0]..layers[17]），而非 32 层。\n\n用户原计划提取 layers {4,8,12,16,20,24,28,32} — **其中 layers 20,24,28,32 不存在**。\n\n**推荐调整方案**:\n| 原计划 | 可行方案 A (8 层均匀采样) | 可行方案 B (偏重深层) |\n|--------|--------------------------|---------------------|\n| {4,8,12,16,20,24,28,32} | {1,3,5,7,9,11,13,15} | {2,4,6,8,10,12,14,16} |\n\n**或者同时提取两个 Expert 的激活**（获得更丰富的信息）:\n- PaliGemma layers: {2, 5, 8, 11, 14, 17}\n- Action Expert layers: {2, 5, 8, 11, 14, 17}\n- 共 12 层激活，覆盖两个 transformer\n\n### 4.5 Hook 实现代码示例\n\n```python\nclass ActivationExtractor:\n    def __init__(self, model, layer_indices):\n        self.activations = {}\n        self.hooks = []\n        \n        for idx in layer_indices:\n            # Hook PaliGemma LLM layers\n            layer = model.paligemma_with_expert.paligemma.language_model.layers[idx]\n            handle = layer.register_forward_hook(\n                lambda module, input, output, idx=idx: \n                    self.activations.__setitem__(f'llm_layer_{idx}', output[0].detach())\n            )\n            self.hooks.append(handle)\n            \n            # Hook Action Expert layers\n            expert_layer = model.paligemma_with_expert.gemma_expert.model.layers[idx]\n            handle = expert_layer.register_forward_hook(\n                lambda module, input, output, idx=idx:\n                    self.activations.__setitem__(f'expert_layer_{idx}', output[0].detach())\n            )\n            self.hooks.append(handle)\n    \n    def remove_hooks(self):\n        for h in self.hooks:\n            h.remove()\n```\n\n---\n\n## 5. 技术估算\n\n### 5.1 序列长度分析\n\nLIBERO 评测时的 token 构成：\n| 组件 | Tokens | 说明 |\n|------|--------|------|\n| Base image | 256 | 224×224 / 14×14 patches |\n| Left wrist image | 256 | 224×224 / 14×14 patches |\n| Right wrist image | 256 | 零填充（LIBERO 只有 2 相机），但仍占序列位置 |\n| Text prompt | 48 | max_token_len (pi0 默认) |\n| State | 1 | 投影到 hidden_dim |\n| Action tokens | 50 | action_horizon=50 |\n| **Total** | **~867** | |\n\n### 5.2 每条 Rollout 激活存储估算\n\n**假设条件**:\n- 8 层采样（PaliGemma LLM 层）\n- hidden_dim = 2048 (PaliGemma)\n- seq_len ≈ 867\n- replan_steps = 5，每 5 个 env step 做一次推理\n- 每 episode 约 200-400 env steps → ~40-80 次推理\n\n**方案 A: 存储完整序列激活 (fp32)**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理每层 | 2048 × 867 × 4 bytes = 7.1 MB |\n| 每次推理 8 层 | 56.8 MB |\n| 每 episode (60 次推理) | 3.4 GB |\n| 500 episodes | **1.7 TB** |\n\n**方案 B: 仅存储 action token 位置的激活 (fp32)**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理每层 | 2048 × 50 × 4 bytes = 0.41 MB |\n| 每次推理 8 层 | 3.3 MB |\n| 每 episode (60 次推理) | 197 MB |\n| 500 episodes | **96 GB** |\n\n**方案 C: Action tokens + fp16**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理 8 层 | 1.6 MB |\n| 每 episode (60 次推理) | 98 MB |\n| 500 episodes | **48 GB** |\n\n**方案 D: 池化后的层表征 (mean pooling over seq_len, fp16)**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理每层 | 2048 × 2 bytes = 4 KB |\n| 每次推理 8 层 | 32 KB |\n| 每 episode (60 次推理) | 1.9 MB |\n| 500 episodes | **0.95 GB** |\n\n### 5.3 推理速度估算\n\n**来源**: π₀ 论文 (Table 4) 在 RTX 4090 上的测量:\n- Image encoding: 14 ms\n- Observation forward pass: 32 ms\n- 10× action flow passes: 27 ms\n- **单次推理总计**: 73 ms\n\n**H100 估算** (约 2× 4090 推理性能):\n- 单次推理: ~35-40 ms\n- 每 episode (60 次推理): ~2.4 s（纯模型推理时间）\n- 加上环境仿真时间: 每 episode 约 30-60 秒\n- **500 episodes 总时间**: ~4-8 小时（单 H100）\n\n**注意**: 如果需要存储激活，推理时需额外内存存储 hook 输出，峰值显存约增加 50-100 MB。\n\n### 5.4 训练资源估算\n\n**LoRA 微调 500 episodes 数据**:\n- 数据: 500 episodes × ~200 steps × 7-dim action = ~70K 训练样本\n- 训练时间 (单 A6000/4090): 10k-30k steps × ~0.5s/step ≈ 1.4-4.2 小时\n- 显存: ~16-22 GB (LoRA)\n\n---\n\n## 6. 风险与阻塞项\n\n### 6.1 高风险项\n\n| 风险 | 严重性 | 说明 | 缓解方案 |\n|------|--------|------|----------|\n| **层数不匹配** | 🔴 高 | 模型仅 18 层，原计划 8 层采样中有 4 层不存在 | 调整为 {2,4,6,8,10,12,14,16} |\n| **PyTorch LoRA 未官方支持** | 🟡 中 | PyTorch 训练不原生支持 LoRA，需用社区方案或自实现 | 采用 Issue #842 的实现，或用 JAX 训练 + PyTorch 推理 |\n| **激活存储量大** | 🟡 中 | 完整序列存储 500 episodes 需 1.7TB | 使用方案 B/C/D 减少存储 |\n\n### 6.2 中等风险项\n\n| 风险 | 说明 | 缓解方案 |\n|------|------|----------|\n| JAX vs PyTorch 精度差异 | LeRobot PyTorch 转换后性能有下降，官方建议微调 | 可用 JAX checkpoint 作为 baseline 对比 |\n| Flow matching 推理开销 | 每次推理需要 10 步迭代去噪 | 已有 KV-cache 优化，单次 73ms 可接受 |\n| LIBERO-Plus 集成 | 需要替换 LIBERO 库，可能有版本兼容问题 | 使用 Docker 隔离环境 |\n\n### 6.3 非阻塞项\n\n- Checkpoint 下载: 公开可用，无需申请\n- 数据转换: 已有 LeRobot 格式转换脚本\n- 评测脚本: 完整可用，包含 Docker 配置\n- 多 GPU 支持: PyTorch DDP 已实现\n\n---\n\n## 7. 推荐技术方案\n\n### 7.1 总体架构\n\n```\n[LIBERO Env] → [π₀ with Hooks] → [Activation Buffer]\n                     ↓                    ↓\n              [Action Output]    [Meta-Brain Router]\n                                        ↓\n                                 [LoRA Selection]\n                                        ↓\n                               [Task-Specific LoRA]\n```\n\n### 7.2 具体步骤\n\n**Phase 1: 基础设施搭建**\n1. 安装 OpenPI (PyTorch 版) + LIBERO 环境\n2. 验证 `lerobot/pi0_base` 或 `pi0_libero_base` checkpoint 加载\n3. 运行标准 LIBERO 评测确认 baseline 性能\n\n**Phase 2: 激活提取**\n1. 在 PyTorch 模型上注册 forward hooks\n2. 选择层: PaliGemma layers {2,4,6,8,10,12,14,16}\n3. 使用方案 B (action tokens only, fp16): 每 500 episodes ~48 GB\n4. 收集 LIBERO 全 4 个 task suite 的激活\n\n**Phase 3: LoRA 训练**\n1. 基于 Issue #842 的 PyTorch LoRA 实现\n2. 或使用 JAX 原生 LoRA 训练 (gemma_2b_lora + gemma_300m_lora)\n3. 每个 task suite 训练一个 LoRA adapter\n4. LoRA config: rank=16, alpha=16.0, target=attn+ffn\n\n**Phase 4: Meta-Brain Router**\n1. 输入: 中间层激活 (8 layers × hidden_dim)\n2. 输出: LoRA adapter 选择/混合权重\n3. 训练: 使用收集的激活-任务标签对\n\n### 7.3 硬件需求\n\n| 阶段 | GPU 需求 | 时间估算 |\n|------|---------|---------|\n| LIBERO 评测 + 激活收集 | 1× H100/A100 | ~8 小时 |\n| LoRA 训练 (4 adapters) | 1× A6000/4090 | ~16 小时 |\n| Meta-Brain Router 训练 | 1× A6000 | ~2 小时 |\n| 总磁盘 | ~100 GB (激活) + ~10 GB (checkpoints) | |\n\n---\n\n## 8. 关键代码引用索引\n\n| 内容 | 文件路径 | 说明 |\n|------|---------|------|\n| Pi0 模型定义 (JAX) | `src/openpi/models/pi0.py:47-176` | Pi0 class, forward/loss/sample |\n| Pi0 模型定义 (PyTorch) | `src/openpi/models_pytorch/pi0_pytorch.py` | PI0Pytorch class |\n| Gemma 变体配置 | `src/openpi/models/gemma.py` | width/depth/heads 定义 |\n| Gemma PyTorch | `src/openpi/models_pytorch/gemma_pytorch.py` | GemmaForCausalLM 层结构 |\n| LoRA 实现 (JAX) | `src/openpi/models/lora.py` | Einsum, FeedForward adapters |\n| 模型配置 | `src/openpi/models/pi0_config.py` | Pi0Config dataclass |\n| 训练配置 | `src/openpi/training/config.py` | TrainConfig, LIBERO 数据配置 |\n| 训练脚本 (JAX) | `scripts/train.py` | JAX 训练循环 |\n| 训练脚本 (PyTorch) | `scripts/train_pytorch.py` | PyTorch 训练循环 |\n| LIBERO 策略映射 | `src/openpi/policies/libero_policy.py` | LiberoInputs/Outputs |\n| LIBERO 评测 | `examples/libero/main.py` | 完整评测流程 |\n| 数据转换 | `examples/libero/convert_libero_data_to_lerobot.py` | LIBERO → LeRobot |\n| SigLIP 视觉编码器 | `src/openpi/models/siglip.py` | So400m/14 ViT |\n| 注意力 mask | `src/openpi/models/pi0.py:20-38` | make_attn_mask() |\n| Flow matching | `src/openpi/models/pi0.py:119-150` | compute_loss() |\n| 推理采样 | `src/openpi/models/pi0.py:152-201` | sample_actions() |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/openpi_research_report.md",
    "content": "# OpenPI (π₀) Codebase 深度技术调研报告\n\n> 调研日期：2026-05-15\n> 目标：评估在 π₀ 上实施 Meta-Brain LoRA Routing 的技术可行性\n\n---\n\n## 1. π₀ 模型架构与加载\n\n### 1.1 整体架构\n\nπ₀ 是 Vision-Language-Action (VLA) flow model，基于 PaliGemma 2B VLM 扩展而来，采用 MoE-like 架构（Mixture of Tokens, MoT）。\n\n**核心组件**：\n- **视觉编码器**: SigLIP So400m/14（~400M 参数）\n- **语言模型 (PaliGemma backbone)**: Gemma 2B（~2.6B 参数）\n- **动作专家 (Action Expert)**: Gemma 300M（~315M 参数，从零初始化）\n- **投影层**: action_in_proj, action_out_proj, time MLPs\n\n**代码位置**:\n- JAX 实现: `src/openpi/models/pi0.py` (Pi0 class, lines 47-176)\n- PyTorch 实现: `src/openpi/models_pytorch/pi0_pytorch.py` (PI0Pytorch class)\n- 配置: `src/openpi/models/pi0_config.py`\n- Gemma 定义: `src/openpi/models/gemma.py` (JAX), `src/openpi/models_pytorch/gemma_pytorch.py` (PyTorch)\n\n### 1.2 详细架构参数\n\n| 组件 | 参数 | 值 |\n|------|------|-----|\n| **Gemma 2B (PaliGemma LLM)** | width (hidden_dim) | 2048 |\n| | depth (层数) | **18** |\n| | mlp_dim | 16,384 |\n| | num_heads | 8 |\n| | num_kv_heads | 1 (Multi-Query Attention) |\n| | head_dim | 256 |\n| **Gemma 300M (Action Expert)** | width | 1024 |\n| | depth | **18** |\n| | mlp_dim | 4,096 |\n| | num_heads | 8 |\n| | num_kv_heads | 1 |\n| | head_dim | 256 |\n| **SigLIP So400m/14** | embedding_dim | ~1152 |\n| | patch_size | 14×14 |\n| | input_resolution | 224×224 |\n| | patches/image | 256 (16×16) |\n\n**来源**: `src/openpi/models/gemma.py` 中的 variant 定义:\n```python\n# gemma_2b: width=2048, depth=18, mlp_dim=16384, num_heads=8, num_kv_heads=1, head_dim=256\n# gemma_300m: width=1024, depth=18, mlp_dim=4096, num_heads=8, num_kv_heads=1, head_dim=256\n```\n\n### 1.3 注意力机制\n\n采用 block-wise causal masking（`src/openpi/models/pi0.py`, lines 20-38）:\n- VLM block: 仅关注自身（prefix tokens: images + language）\n- State/proprioception block: 关注自身 + VLM（共享 action expert 权重）\n- Action block: 关注所有 tokens（完全双向）\n\n**来源**: `make_attn_mask()` 函数，通过 cumulative mask 实现不同的注意力模式。\n\n### 1.4 动作生成 (Flow Matching)\n\n**训练** (`compute_loss`, lines 119-150):\n- 时间步 t ~ Beta(1.5, 1)，缩放到 [0.001, 0.999]\n- 噪声状态: x_t = t·noise + (1-t)·actions\n- 目标速度: u_t = noise - actions\n- 损失: MSE(v_t, u_t)\n\n**推理** (`sample_actions`, lines 152-201):\n- 10 步 Euler 积分: t=1 (噪声) → t=0 (目标)\n- 步长: dt = -1/num_steps = -0.1\n- 迭代: x_{t+dt} = x_t + dt·v_t\n- 使用 KV-cache 优化 prefix tokens\n\n### 1.5 Checkpoint 来源与大小\n\n| Checkpoint | 来源 | 格式 |\n|------------|------|------|\n| pi0_base | `gs://openpi-assets/checkpoints/pi0_base/params` | JAX (Flax) |\n| pi0_fast_base | `gs://openpi-assets/checkpoints/pi0_fast_base/params` | JAX (Flax) |\n| pi05_base | `gs://openpi-assets/checkpoints/pi05_base/params` | JAX (Flax) |\n| lerobot/pi0_base | HuggingFace Hub | SafeTensors (PyTorch) |\n| lerobot/pi0_libero_base | HuggingFace Hub | SafeTensors (PyTorch) |\n\n**自动下载**：默认缓存到 `~/.cache/openpi`，可通过 `OPENPI_DATA_HOME` 修改。无需申请，直接公开下载。\n\n**模型大小**:\n- 总参数量: ~3.3B（HuggingFace 标注为 4B，含 F32 精度下的 embeddings/projections）\n- Checkpoint 大小 (fp32): ~13.2 GB\n- Checkpoint 大小 (bf16): ~6.6 GB\n\n### 1.6 显存需求\n\n| 模式 | 显存需求 | 推荐 GPU |\n|------|---------|----------|\n| 推理 (bf16) | > 8 GB | RTX 4090 / A6000 |\n| LoRA 微调 | > 22.5 GB | RTX 4090 / A6000 |\n| 全量微调 | > 70 GB | A100 80GB / H100 |\n\n**来源**: OpenPI README 文档。\n\n### 1.7 加载方式\n\n**OpenPI 原生 (JAX)**:\n```python\n# src/openpi/training/config.py\nmodel = config.model.create(model_rng)\n# 通过 _load_weights_and_validate() 加载预训练权重\n```\n\n**OpenPI PyTorch**:\n```python\nimport openpi.models_pytorch.pi0_pytorch\nimport safetensors.torch\nmodel = PI0Pytorch(model_cfg).to(device)\nsafetensors.torch.load_model(model, model_path)\n```\n\n**LeRobot (HuggingFace)**:\n```python\nfrom lerobot.policies.pi0 import PI0Policy\npolicy = PI0Policy.from_pretrained(\"lerobot/pi0_base\").to(device).eval()\n```\n\n---\n\n## 2. LIBERO 环境集成\n\n### 2.1 已有 LIBERO 支持\n\nOpenPI 对 LIBERO 有**完整的一等支持**：\n\n**关键文件**:\n- 评测脚本: `examples/libero/main.py`\n- 数据转换: `examples/libero/convert_libero_data_to_lerobot.py`\n- 策略映射: `src/openpi/policies/libero_policy.py`\n- Docker 配置: `examples/libero/Dockerfile`, `examples/libero/compose.yml`\n- 训练配置: `src/openpi/training/config.py` 中的 `LeRobotLiberoDataConfig`\n\n**预训练 LIBERO checkpoint**:\n- `gs://openpi-assets/checkpoints/pi05_libero/params`（π₀.₅ LIBERO 微调版，96.85% 平均成功率）\n- HuggingFace: `lerobot/pi0_libero_base`\n\n### 2.2 LIBERO 评测调用方式\n\n`examples/libero/main.py` 实现了完整的评测流程：\n\n1. 启动 Policy Server: `scripts/serve_policy.py`\n2. 客户端通过 WebSocket 连接: `WebsocketClientPolicy(host, port)`\n3. 评测循环:\n   - 重置环境 → 等待物体稳定 (num_steps_wait)\n   - 每 `replan_steps=5` 步请求新 action chunk\n   - 记录成功率和视频\n\n**配置格式** (通过命令行参数):\n- `--task_suite_name`: LIBERO 任务套件 (spatial/object/goal/10)\n- `--num_trials_per_task`: 每个任务的试验次数 (默认 50)\n- `--resize_size`: 图像分辨率 (224)\n- `SERVER_ARGS`: 指定 checkpoint\n\n**观测格式** (LiberoInputs, `src/openpi/policies/libero_policy.py`):\n- State: `observation/state` — 8 维向量（end-effector position + rotation + gripper）\n- Base image: `observation/image` — 224×224 RGB（第三人称）\n- Wrist image: `observation/wrist_image` — 224×224 RGB（左手腕相机）\n- Right wrist: 零填充（LIBERO 只有 2 个相机）\n\n**动作格式** (LiberoOutputs):\n- 输出前 7 维动作（从 action_dim=32 的填充中截取）\n- 7 维 = 6-DoF end-effector + 1 gripper\n\n### 2.3 LIBERO-Plus 扰动评测\n\n**支持状态**: 可用，但需要额外安装 LIBERO-Plus 替代标准 LIBERO。\n\n**LIBERO-Plus** (https://github.com/sylvestf/LIBERO-plus) 提供 7 个扰动维度:\n1. 物体布局 (Objects Layout)\n2. 相机视角 (Camera Viewpoints)\n3. 机器人初始状态 (Robot Initial States)\n4. 语言指令 (Language Instructions)\n5. 光照条件 (Light Conditions)\n6. 背景纹理 (Background Textures)\n7. 传感器噪声 (Sensor Noise)\n\n**集成方式**: \"Simply replace the originally installed LIBERO repository with our repository without modifying your code\" — 直接替换 LIBERO 库即可，评测代码无需修改。唯一改动: `num_trials_per_task` 从 50 改为 1。\n\n**π₀ 在 LIBERO-Plus 上的基线表现**: 平均 53.6%（光照 85.0%，背景 81.4%，但机器人初始状态仅 6.0%）。\n\n---\n\n## 3. LoRA Fine-tuning 支持\n\n### 3.1 JAX 实现 — 已有完整支持\n\n**代码位置**: `src/openpi/models/lora.py`\n\n**LoRA 变体定义** (`src/openpi/models/gemma.py`):\n```\ngemma_2b_lora:    rank=16, alpha=16.0 (attn + ffn)\ngemma_300m_lora:  rank=32, alpha=32.0 (attn + ffn)\n```\n\n**训练配置** (`src/openpi/training/config.py`):\n- 使用 `paligemma_variant=\"gemma_2b_lora\"` + `action_expert_variant=\"gemma_300m_lora\"`\n- Freeze filter: 冻结非 LoRA 的 LLM 参数，仅训练 LoRA 权重\n- EMA decay: 禁用 (`ema_decay=None`)\n- 其他默认: 30k steps, batch_size=32, AdamW + Cosine Decay\n\n**LoRA 目标模块**:\n- Attention: q_proj, k_proj, v_proj, o_proj (通过 Einsum 类)\n- FFN: gate_proj, up_proj, down_proj (通过 FeedForward 类)\n\n**LoRA 实现特点**:\n- 支持 RSLoRA (rank-stabilized LoRA): `scaling = alpha / sqrt(rank)`\n- 纯 additive: `output = base_output + (x @ w_a @ w_b) * scaling`\n- 不依赖外部库（如 peft），自实现\n\n### 3.2 PyTorch 实现 — 官方不支持，社区有方案\n\n**官方状态**: OpenPI 的 PyTorch 训练脚本 (`scripts/train_pytorch.py`) **不支持 LoRA**，仅支持全量微调。\n\n**社区方案** (Issue #842):\n- 纯 PyTorch LoRA 实现，不依赖 peft\n- 注入到 Attention (q/k/v/o_proj) 和 MLP (gate/up/down_proj)\n- Rank=16 时 LoRA 参数: 26.5M (0.73% of total)\n- 可选解冻 Vision Encoder: 额外 412M trainable (12.11% total)\n- 单 RTX 4090 可训练，~16GB 峰值显存\n- LIBERO 上达到 96.95% 平均成功率\n- **状态**: PR 未合并，但代码完整可用\n\n**LeRobot 方案**:\n- HuggingFace LeRobot 提供了 Pi0 的 PyTorch 训练脚本\n- 支持 `train_expert_only=true` 冻结 VLM 仅训练 action expert\n- 不原生支持 LoRA，但可通过 HuggingFace PEFT 库扩展\n\n### 3.3 推荐方案\n\n对于本项目的 Meta-Brain LoRA Routing：\n1. **首选**: 基于 OpenPI JAX 实现，已有完整 LoRA 支持\n2. **备选**: 采用 Issue #842 的 PyTorch LoRA 实现（更灵活，更容易加 hook）\n3. **替代**: 使用 LeRobot PyTorch + HuggingFace PEFT 库\n\n---\n\n## 4. 中间层激活提取\n\n### 4.1 模型前向传播路径\n\n**JAX 实现** (`src/openpi/models/pi0.py`):\n```\nPi0.__call__()\n  → embed_prefix(obs)        # SigLIP 编码图像 + tokenize 文本\n  → embed_suffix(obs, noisy_actions, timestep)  # 编码动作 + 时间步\n  → self.PaliGemma['llm'](tokens, ...)  # Gemma Module forward (18 layers)\n  → action_out_proj(...)     # 投影到动作空间\n```\n\n**PyTorch 实现** (`src/openpi/models_pytorch/pi0_pytorch.py`):\n```\nPI0Pytorch.forward(observation, actions)\n  → _preprocess_observation()\n  → embed_prefix(obs)\n  → embed_suffix(obs, noisy_actions, timestep)\n  → paligemma_with_expert(tokens, ...)\n  → action_out_proj(...)\n```\n\n### 4.2 已有 Hook 机制\n\n**OpenPI 没有已有的 hook 机制或中间层输出接口。** 需要自行添加。\n\n### 4.3 PyTorch Hook 注册方案（推荐）\n\nPyTorch 实现支持标准的 `register_forward_hook`，模块路径如下：\n\n**PaliGemma LLM 层 (hidden_dim=2048)**:\n```python\nmodel.paligemma_with_expert.paligemma.language_model.layers[i]\n# i = 0..17 (共 18 层)\n\n# 子模块:\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].self_attn\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].self_attn.q_proj\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].self_attn.o_proj\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].mlp\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].input_layernorm\nmodel.paligemma_with_expert.paligemma.language_model.layers[i].post_attention_layernorm\n```\n\n**Action Expert 层 (hidden_dim=1024)**:\n```python\nmodel.paligemma_with_expert.gemma_expert.model.layers[i]\n# i = 0..17 (共 18 层)\n# 子模块结构同上\n```\n\n**Vision Encoder 层**:\n```python\nmodel.paligemma_with_expert.paligemma.vision_tower.layers[i]\n```\n\n### 4.4 关键发现：层数只有 18，不是 32！\n\n**⚠️ 重要**: π₀ 的 Transformer 深度为 **18 层**（layers[0]..layers[17]），而非 32 层。\n\n用户原计划提取 layers {4,8,12,16,20,24,28,32} — **其中 layers 20,24,28,32 不存在**。\n\n**推荐调整方案**:\n| 原计划 | 可行方案 A (8 层均匀采样) | 可行方案 B (偏重深层) |\n|--------|--------------------------|---------------------|\n| {4,8,12,16,20,24,28,32} | {1,3,5,7,9,11,13,15} | {2,4,6,8,10,12,14,16} |\n\n**或者同时提取两个 Expert 的激活**（获得更丰富的信息）:\n- PaliGemma layers: {2, 5, 8, 11, 14, 17}\n- Action Expert layers: {2, 5, 8, 11, 14, 17}\n- 共 12 层激活，覆盖两个 transformer\n\n### 4.5 Hook 实现代码示例\n\n```python\nclass ActivationExtractor:\n    def __init__(self, model, layer_indices):\n        self.activations = {}\n        self.hooks = []\n        \n        for idx in layer_indices:\n            # Hook PaliGemma LLM layers\n            layer = model.paligemma_with_expert.paligemma.language_model.layers[idx]\n            handle = layer.register_forward_hook(\n                lambda module, input, output, idx=idx: \n                    self.activations.__setitem__(f'llm_layer_{idx}', output[0].detach())\n            )\n            self.hooks.append(handle)\n            \n            # Hook Action Expert layers\n            expert_layer = model.paligemma_with_expert.gemma_expert.model.layers[idx]\n            handle = expert_layer.register_forward_hook(\n                lambda module, input, output, idx=idx:\n                    self.activations.__setitem__(f'expert_layer_{idx}', output[0].detach())\n            )\n            self.hooks.append(handle)\n    \n    def remove_hooks(self):\n        for h in self.hooks:\n            h.remove()\n```\n\n---\n\n## 5. 技术估算\n\n### 5.1 序列长度分析\n\nLIBERO 评测时的 token 构成：\n| 组件 | Tokens | 说明 |\n|------|--------|------|\n| Base image | 256 | 224×224 / 14×14 patches |\n| Left wrist image | 256 | 224×224 / 14×14 patches |\n| Right wrist image | 256 | 零填充（LIBERO 只有 2 相机），但仍占序列位置 |\n| Text prompt | 48 | max_token_len (pi0 默认) |\n| State | 1 | 投影到 hidden_dim |\n| Action tokens | 50 | action_horizon=50 |\n| **Total** | **~867** | |\n\n### 5.2 每条 Rollout 激活存储估算\n\n**假设条件**:\n- 8 层采样（PaliGemma LLM 层）\n- hidden_dim = 2048 (PaliGemma)\n- seq_len ≈ 867\n- replan_steps = 5，每 5 个 env step 做一次推理\n- 每 episode 约 200-400 env steps → ~40-80 次推理\n\n**方案 A: 存储完整序列激活 (fp32)**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理每层 | 2048 × 867 × 4 bytes = 7.1 MB |\n| 每次推理 8 层 | 56.8 MB |\n| 每 episode (60 次推理) | 3.4 GB |\n| 500 episodes | **1.7 TB** |\n\n**方案 B: 仅存储 action token 位置的激活 (fp32)**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理每层 | 2048 × 50 × 4 bytes = 0.41 MB |\n| 每次推理 8 层 | 3.3 MB |\n| 每 episode (60 次推理) | 197 MB |\n| 500 episodes | **96 GB** |\n\n**方案 C: Action tokens + fp16**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理 8 层 | 1.6 MB |\n| 每 episode (60 次推理) | 98 MB |\n| 500 episodes | **48 GB** |\n\n**方案 D: 池化后的层表征 (mean pooling over seq_len, fp16)**\n\n| 指标 | 值 |\n|------|-----|\n| 每次推理每层 | 2048 × 2 bytes = 4 KB |\n| 每次推理 8 层 | 32 KB |\n| 每 episode (60 次推理) | 1.9 MB |\n| 500 episodes | **0.95 GB** |\n\n### 5.3 推理速度估算\n\n**来源**: π₀ 论文 (Table 4) 在 RTX 4090 上的测量:\n- Image encoding: 14 ms\n- Observation forward pass: 32 ms\n- 10× action flow passes: 27 ms\n- **单次推理总计**: 73 ms\n\n**H100 估算** (约 2× 4090 推理性能):\n- 单次推理: ~35-40 ms\n- 每 episode (60 次推理): ~2.4 s（纯模型推理时间）\n- 加上环境仿真时间: 每 episode 约 30-60 秒\n- **500 episodes 总时间**: ~4-8 小时（单 H100）\n\n**注意**: 如果需要存储激活，推理时需额外内存存储 hook 输出，峰值显存约增加 50-100 MB。\n\n### 5.4 训练资源估算\n\n**LoRA 微调 500 episodes 数据**:\n- 数据: 500 episodes × ~200 steps × 7-dim action = ~70K 训练样本\n- 训练时间 (单 A6000/4090): 10k-30k steps × ~0.5s/step ≈ 1.4-4.2 小时\n- 显存: ~16-22 GB (LoRA)\n\n---\n\n## 6. 风险与阻塞项\n\n### 6.1 高风险项\n\n| 风险 | 严重性 | 说明 | 缓解方案 |\n|------|--------|------|----------|\n| **层数不匹配** | 🔴 高 | 模型仅 18 层，原计划 8 层采样中有 4 层不存在 | 调整为 {2,4,6,8,10,12,14,16} |\n| **PyTorch LoRA 未官方支持** | 🟡 中 | PyTorch 训练不原生支持 LoRA，需用社区方案或自实现 | 采用 Issue #842 的实现，或用 JAX 训练 + PyTorch 推理 |\n| **激活存储量大** | 🟡 中 | 完整序列存储 500 episodes 需 1.7TB | 使用方案 B/C/D 减少存储 |\n\n### 6.2 中等风险项\n\n| 风险 | 说明 | 缓解方案 |\n|------|------|----------|\n| JAX vs PyTorch 精度差异 | LeRobot PyTorch 转换后性能有下降，官方建议微调 | 可用 JAX checkpoint 作为 baseline 对比 |\n| Flow matching 推理开销 | 每次推理需要 10 步迭代去噪 | 已有 KV-cache 优化，单次 73ms 可接受 |\n| LIBERO-Plus 集成 | 需要替换 LIBERO 库，可能有版本兼容问题 | 使用 Docker 隔离环境 |\n\n### 6.3 非阻塞项\n\n- Checkpoint 下载: 公开可用，无需申请\n- 数据转换: 已有 LeRobot 格式转换脚本\n- 评测脚本: 完整可用，包含 Docker 配置\n- 多 GPU 支持: PyTorch DDP 已实现\n\n---\n\n## 7. 推荐技术方案\n\n### 7.1 总体架构\n\n```\n[LIBERO Env] → [π₀ with Hooks] → [Activation Buffer]\n                     ↓                    ↓\n              [Action Output]    [Meta-Brain Router]\n                                        ↓\n                                 [LoRA Selection]\n                                        ↓\n                               [Task-Specific LoRA]\n```\n\n### 7.2 具体步骤\n\n**Phase 1: 基础设施搭建**\n1. 安装 OpenPI (PyTorch 版) + LIBERO 环境\n2. 验证 `lerobot/pi0_base` 或 `pi0_libero_base` checkpoint 加载\n3. 运行标准 LIBERO 评测确认 baseline 性能\n\n**Phase 2: 激活提取**\n1. 在 PyTorch 模型上注册 forward hooks\n2. 选择层: PaliGemma layers {2,4,6,8,10,12,14,16}\n3. 使用方案 B (action tokens only, fp16): 每 500 episodes ~48 GB\n4. 收集 LIBERO 全 4 个 task suite 的激活\n\n**Phase 3: LoRA 训练**\n1. 基于 Issue #842 的 PyTorch LoRA 实现\n2. 或使用 JAX 原生 LoRA 训练 (gemma_2b_lora + gemma_300m_lora)\n3. 每个 task suite 训练一个 LoRA adapter\n4. LoRA config: rank=16, alpha=16.0, target=attn+ffn\n\n**Phase 4: Meta-Brain Router**\n1. 输入: 中间层激活 (8 layers × hidden_dim)\n2. 输出: LoRA adapter 选择/混合权重\n3. 训练: 使用收集的激活-任务标签对\n\n### 7.3 硬件需求\n\n| 阶段 | GPU 需求 | 时间估算 |\n|------|---------|---------|\n| LIBERO 评测 + 激活收集 | 1× H100/A100 | ~8 小时 |\n| LoRA 训练 (4 adapters) | 1× A6000/4090 | ~16 小时 |\n| Meta-Brain Router 训练 | 1× A6000 | ~2 小时 |\n| 总磁盘 | ~100 GB (激活) + ~10 GB (checkpoints) | |\n\n---\n\n## 8. 关键代码引用索引\n\n| 内容 | 文件路径 | 说明 |\n|------|---------|------|\n| Pi0 模型定义 (JAX) | `src/openpi/models/pi0.py:47-176` | Pi0 class, forward/loss/sample |\n| Pi0 模型定义 (PyTorch) | `src/openpi/models_pytorch/pi0_pytorch.py` | PI0Pytorch class |\n| Gemma 变体配置 | `src/openpi/models/gemma.py` | width/depth/heads 定义 |\n| Gemma PyTorch | `src/openpi/models_pytorch/gemma_pytorch.py` | GemmaForCausalLM 层结构 |\n| LoRA 实现 (JAX) | `src/openpi/models/lora.py` | Einsum, FeedForward adapters |\n| 模型配置 | `src/openpi/models/pi0_config.py` | Pi0Config dataclass |\n| 训练配置 | `src/openpi/training/config.py` | TrainConfig, LIBERO 数据配置 |\n| 训练脚本 (JAX) | `scripts/train.py` | JAX 训练循环 |\n| 训练脚本 (PyTorch) | `scripts/train_pytorch.py` | PyTorch 训练循环 |\n| LIBERO 策略映射 | `src/openpi/policies/libero_policy.py` | LiberoInputs/Outputs |\n| LIBERO 评测 | `examples/libero/main.py` | 完整评测流程 |\n| 数据转换 | `examples/libero/convert_libero_data_to_lerobot.py` | LIBERO → LeRobot |\n| SigLIP 视觉编码器 | `src/openpi/models/siglip.py` | So400m/14 ViT |\n| 注意力 mask | `src/openpi/models/pi0.py:20-38` | make_attn_mask() |\n| Flow matching | `src/openpi/models/pi0.py:119-150` | compute_loss() |\n| 推理采样 | `src/openpi/models/pi0.py:152-201` | sample_actions() |\n"
  }
}
````

</details>

---

### Tool result

_source line 86 · 2026-05-15T10:41:49.907910+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/openpi_research_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-15T10:41:49.908130+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/openpi_research_report.md",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/openpi_research_report.md",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T10:41:49.908283+00:00_

1	# OpenPI (π₀) Codebase 深度技术调研报告
2	
3	> 调研日期：2026-05-15
4	> 目标：评估在 π₀ 上实施 Meta-Brain LoRA Routing 的技术可行性
5	
6	---
7	
8	## 1. π₀ 模型架构与加载
9	
10	### 1.1 整体架构

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-15T10:41:49.908411+00:00_

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
  "session": "worker_research_openpi-codebase_20260515T103420",
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

_source line 90 · 2026-05-15T10:41:49.908553+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-15T10:41:49.908710+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "meta_brain_lora_routing",
  "file": "memory.md",
  "content": "# OpenPI Research Summary (2026-05-15)\n\n## Key Finding: π₀ Architecture\n- Backbone: PaliGemma (SigLIP So400m/14 + Gemma 2B) + Action Expert (Gemma 300M)\n- Total: ~3.3B params, **18 transformer layers** (NOT 32)\n- Gemma 2B: width=2048, depth=18, 8 heads, MQA\n- Action Expert: width=1024, depth=18, 8 heads\n- Flow matching (10-step Euler) for action generation\n\n## LIBERO Integration\n- Full first-class support in OpenPI\n- Evaluation: `examples/libero/main.py` via WebSocket policy server\n- π₀.₅ LIBERO checkpoint: 96.85% avg success\n- LIBERO-Plus perturbed eval: drop-in replacement for LIBERO lib\n\n## LoRA Support\n- JAX: native LoRA (rank=16/32, attn+ffn targets)\n- PyTorch: NOT official, but Issue #842 has working implementation (26.5M params, 96.95% on LIBERO)\n- LeRobot: no native LoRA, can extend with PEFT\n\n## Activation Extraction\n- PyTorch hook path: `model.paligemma_with_expert.paligemma.language_model.layers[i]` (i=0..17)\n- Action expert: `model.paligemma_with_expert.gemma_expert.model.layers[i]`\n- Recommended layers: {2,4,6,8,10,12,14,16} (adjust from original {4,8,12,16,20,24,28,32})\n\n## Storage Estimates (500 episodes)\n- Full seq fp32: 1.7 TB | Action tokens fp16: 48 GB | Pooled fp16: 0.95 GB\n\n## Full report: `artifacts/openpi_research_report.md`\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "meta_brain_lora_routing",
    "file": "memory.md",
    "content": "# OpenPI Research Summary (2026-05-15)\n\n## Key Finding: π₀ Architecture\n- Backbone: PaliGemma (SigLIP So400m/14 + Gemma 2B) + Action Expert (Gemma 300M)\n- Total: ~3.3B params, **18 transformer layers** (NOT 32)\n- Gemma 2B: width=2048, depth=18, 8 heads, MQA\n- Action Expert: width=1024, depth=18, 8 heads\n- Flow matching (10-step Euler) for action generation\n\n## LIBERO Integration\n- Full first-class support in OpenPI\n- Evaluation: `examples/libero/main.py` via WebSocket policy server\n- π₀.₅ LIBERO checkpoint: 96.85% avg success\n- LIBERO-Plus perturbed eval: drop-in replacement for LIBERO lib\n\n## LoRA Support\n- JAX: native LoRA (rank=16/32, attn+ffn targets)\n- PyTorch: NOT official, but Issue #842 has working implementation (26.5M params, 96.95% on LIBERO)\n- LeRobot: no native LoRA, can extend with PEFT\n\n## Activation Extraction\n- PyTorch hook path: `model.paligemma_with_expert.paligemma.language_model.layers[i]` (i=0..17)\n- Action expert: `model.paligemma_with_expert.gemma_expert.model.layers[i]`\n- Recommended layers: {2,4,6,8,10,12,14,16} (adjust from original {4,8,12,16,20,24,28,32})\n\n## Storage Estimates (500 episodes)\n- Full seq fp32: 1.7 TB | Action tokens fp16: 48 GB | Pooled fp16: 0.95 GB\n\n## Full report: `artifacts/openpi_research_report.md`\n"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-15T10:41:49.908848+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openpi-codebase_20260515T103420",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 93 · 2026-05-15T10:41:49.909003+00:00_

调研完成。报告已写入 `artifacts/openpi_research_report.md`，摘要已更新到 `memory.md`。

## 核心发现

**架构**: π₀ 基于 PaliGemma (SigLIP + Gemma 2B) + Action Expert (Gemma 300M)，总计 ~3.3B 参数。Transformer 深度 **18 层**（不是 32），这意味着原计划的 layers {4,8,12,16,20,24,28,32} 中后四个不存在，需调整为 {2,4,6,8,10,12,14,16}。

**LIBERO 集成**: OpenPI 有完整的一等 LIBERO 支持，包括评测脚本、数据转换、Docker 配置。LIBERO-Plus 扰动评测通过直接替换 LIBERO 库即可使用。

**LoRA 支持**: JAX 原生支持（rank=16, attn+ffn）；PyTorch 官方不支持，但 Issue #842 有完整社区实现（单 4090 可训练，LIBERO 96.95%）。

**激活提取**: PyTorch 版可通过标准 `register_forward_hook` 在 `model.paligemma_with_expert.paligemma.language_model.layers[i]` 注册 hook。

**主要风险**:
1. 🔴 层数仅 18，需重新设计采样策略
2. 🟡 PyTorch LoRA 需要用未合并的社区 PR
3. 🟡 完整激活存储量大（1.7TB），建议只存 action tokens (48GB) 或池化表征 (0.95GB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_openpi-codebase_20260515T103420"
}
```

</details>

---
