# research lerobot libero recipes

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 197
- **Recorded user turns:** 0
- **Tool calls:** 98
- **Original source:** `logs/chats/worker_research_lerobot-libero-recipes_20260513T094527.jsonl`
- **Structured JSON:** [`55ea2c31d54be08e270d.json`](../../sessions/55/55ea2c31d54be08e270d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

197 recorded events

### Tool call

_source line 1 · 2026-05-13T09:51:02.653538+00:00_

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
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
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

_source line 2 · 2026-05-13T09:51:02.653844+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T09:51:02.654030+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search 1: SmolVLA fine-tuning",
  "prompt": "Search for SmolVLA fine-tuning documentation and examples. This is a VLA (Vision-Language-Action) model from HuggingFace's LeRobot framework, model ID `lerobot/smolvla_base`.\n\nDo the following searches and fetch relevant pages:\n\n1. WebSearch for \"SmolVLA fine-tuning lerobot\"\n2. WebSearch for \"SmolVLA LoRA training recipe\"\n3. WebSearch for \"lerobot smolvla finetune 2025 2026\"\n4. Fetch the HuggingFace model card: https://huggingface.co/lerobot/smolvla_base — extract: model architecture, action dimensions, supported datasets, fine-tuning instructions, training config\n5. Fetch the LeRobot GitHub README: https://github.com/huggingface/lerobot — extract: fine-tuning commands, SmolVLA references, training scripts, example configs\n6. WebSearch for \"lerobot fine-tune guide tutorial\"\n\nFor each result, record:\n- URL\n- Key information (training commands, config files, data format requirements, action_dim)\n- Whether it's directly usable for fine-tuning SmolVLA on a custom dataset\n\nCompile a comprehensive summary of all findings.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Agent",
  "tool_args": {
    "description": "Search 1: SmolVLA fine-tuning",
    "prompt": "Search for SmolVLA fine-tuning documentation and examples. This is a VLA (Vision-Language-Action) model from HuggingFace's LeRobot framework, model ID `lerobot/smolvla_base`.\n\nDo the following searches and fetch relevant pages:\n\n1. WebSearch for \"SmolVLA fine-tuning lerobot\"\n2. WebSearch for \"SmolVLA LoRA training recipe\"\n3. WebSearch for \"lerobot smolvla finetune 2025 2026\"\n4. Fetch the HuggingFace model card: https://huggingface.co/lerobot/smolvla_base — extract: model architecture, action dimensions, supported datasets, fine-tuning instructions, training config\n5. Fetch the LeRobot GitHub README: https://github.com/huggingface/lerobot — extract: fine-tuning commands, SmolVLA references, training scripts, example configs\n6. WebSearch for \"lerobot fine-tune guide tutorial\"\n\nFor each result, record:\n- URL\n- Key information (training commands, config files, data format requirements, action_dim)\n- Whether it's directly usable for fine-tuning SmolVLA on a custom dataset\n\nCompile a comprehensive summary of all findings.",
    "model": "sonnet"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T09:51:02.654258+00:00_

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
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
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

_source line 5 · 2026-05-13T09:51:02.654436+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-13T09:51:02.654569+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search 2: LeRobot + LIBERO",
  "prompt": "Search for how to use LIBERO benchmark datasets with HuggingFace LeRobot framework. LIBERO is a robot manipulation benchmark with multiple task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90).\n\nDo the following searches and fetch relevant pages:\n\n1. WebSearch for \"lerobot LIBERO dataset\"\n2. WebSearch for \"convert LIBERO to lerobot format\"\n3. WebSearch for \"lerobot LIBERO fine-tune\"\n4. WebSearch for \"huggingface lerobot libero 2025 2026\"\n5. WebSearch for \"LIBERO dataset huggingface hub\"\n6. Check if LIBERO datasets exist on HuggingFace Hub by searching: \"site:huggingface.co LIBERO lerobot dataset\"\n\nFor any relevant results, fetch the pages and extract:\n- How to convert LIBERO HDF5 data to LeRobot dataset format\n- Whether there are pre-converted LIBERO datasets on HuggingFace Hub\n- Any conversion scripts or tools\n- Data format details (observation keys, action dimensions, episode structure)\n\nCompile a comprehensive summary of all findings with URLs.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Agent",
  "tool_args": {
    "description": "Search 2: LeRobot + LIBERO",
    "prompt": "Search for how to use LIBERO benchmark datasets with HuggingFace LeRobot framework. LIBERO is a robot manipulation benchmark with multiple task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90).\n\nDo the following searches and fetch relevant pages:\n\n1. WebSearch for \"lerobot LIBERO dataset\"\n2. WebSearch for \"convert LIBERO to lerobot format\"\n3. WebSearch for \"lerobot LIBERO fine-tune\"\n4. WebSearch for \"huggingface lerobot libero 2025 2026\"\n5. WebSearch for \"LIBERO dataset huggingface hub\"\n6. Check if LIBERO datasets exist on HuggingFace Hub by searching: \"site:huggingface.co LIBERO lerobot dataset\"\n\nFor any relevant results, fetch the pages and extract:\n- How to convert LIBERO HDF5 data to LeRobot dataset format\n- Whether there are pre-converted LIBERO datasets on HuggingFace Hub\n- Any conversion scripts or tools\n- Data format details (observation keys, action dimensions, episode structure)\n\nCompile a comprehensive summary of all findings with URLs.",
    "model": "sonnet"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T09:51:02.654774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA fine-tuning lerobot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA fine-tuning lerobot 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-13T09:51:02.654902+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA LoRA training recipe lerobot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA LoRA training recipe lerobot"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T09:51:02.655022+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot smolvla finetune 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot smolvla finetune 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T09:51:02.655165+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot fine-tune guide tutorial custom dataset 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot fine-tune guide tutorial custom dataset 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T09:51:02.655301+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/lerobot/smolvla_base",
  "prompt": "Extract: model architecture, action dimensions, supported datasets, fine-tuning instructions, training config, observation/action space details, any commands or code examples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/lerobot/smolvla_base",
    "prompt": "Extract: model architecture, action dimensions, supported datasets, fine-tuning instructions, training config, observation/action space details, any commands or code examples"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T09:51:02.655427+00:00_

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
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
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

_source line 13 · 2026-05-13T09:51:02.655541+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T09:51:02.655654+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot LIBERO dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot LIBERO dataset"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T09:51:02.655764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "convert LIBERO to lerobot format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "convert LIBERO to lerobot format"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T09:51:02.655874+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot LIBERO fine-tune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot LIBERO fine-tune"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T09:51:02.655989+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot",
  "prompt": "Extract: fine-tuning commands, SmolVLA references, training scripts, example configs, data format requirements, any commands for training or fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot",
    "prompt": "Extract: fine-tuning commands, SmolVLA references, training scripts, example configs, data format requirements, any commands for training or fine-tuning"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T09:51:02.656116+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search 3: SmolVLA action dims",
  "prompt": "Search for SmolVLA's action dimension specification and architecture details. SmolVLA is a Vision-Language-Action model from HuggingFace LeRobot. We need to understand its action space (especially whether it uses 6D or 7D actions, and how the gripper action is handled).\n\nDo the following searches:\n\n1. WebSearch for \"SmolVLA action dimension architecture\"\n2. WebSearch for \"SmolVLA 7D action gripper\"\n3. WebSearch for \"SmolVLA paper arxiv\"\n4. WebSearch for \"SmolVLA action space configuration\"\n5. WebSearch for \"lerobot action_dim smolvla config\"\n6. If you find a paper or technical report, fetch it and extract the action space details\n\nAlso search for LIBERO's action space:\n7. WebSearch for \"LIBERO benchmark action space dimension\"\n8. WebSearch for \"LIBERO 7D action delta position\"\n\nFor each result, record:\n- URL\n- Action dimension details (what each dimension represents)\n- How to configure action_dim when fine-tuning\n- Any mismatch between SmolVLA's default action space and LIBERO's action space\n\nCompile findings about both SmolVLA and LIBERO action spaces, and analyze compatibility.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Agent",
  "tool_args": {
    "description": "Search 3: SmolVLA action dims",
    "prompt": "Search for SmolVLA's action dimension specification and architecture details. SmolVLA is a Vision-Language-Action model from HuggingFace LeRobot. We need to understand its action space (especially whether it uses 6D or 7D actions, and how the gripper action is handled).\n\nDo the following searches:\n\n1. WebSearch for \"SmolVLA action dimension architecture\"\n2. WebSearch for \"SmolVLA 7D action gripper\"\n3. WebSearch for \"SmolVLA paper arxiv\"\n4. WebSearch for \"SmolVLA action space configuration\"\n5. WebSearch for \"lerobot action_dim smolvla config\"\n6. If you find a paper or technical report, fetch it and extract the action space details\n\nAlso search for LIBERO's action space:\n7. WebSearch for \"LIBERO benchmark action space dimension\"\n8. WebSearch for \"LIBERO 7D action delta position\"\n\nFor each result, record:\n- URL\n- Action dimension details (what each dimension represents)\n- How to configure action_dim when fine-tuning\n- Any mismatch between SmolVLA's default action space and LIBERO's action space\n\nCompile findings about both SmolVLA and LIBERO action spaces, and analyze compatibility.",
    "model": "sonnet"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T09:51:02.656327+00:00_

Web search results for query: "SmolVLA fine-tuning lerobot 2025 2026"

Links: [{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"GitHub - huggingface/VLAb · GitHub","url":"https://github.com/huggingface/VLAb"}]

I found comprehensive information about SmolVLA fine-tuning with LeRobot. Here are the key findings:

## SmolVLA Overview

SmolVLA is a compact (450M), open-source Vision-Language-Action model for robotics that runs on consumer hardware. It's designed as a base model to fine-tune on your specific use case.

## Fine-tuning Process

You can use smolvla_base, a pretrained 450M model, and fine-tune it on your data. Training for 20k steps will roughly take ~4 hours on a single A100 GPU, though you should tune the number of steps based on performance and your use-case.

SmolVLA is a base model that requires fine-tuning on your own data for optimal performance in your setup, wi
…[truncated 845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T09:51:02.656500+00:00_

Web search results for query: "lerobot smolvla finetune 2025 2026"

Links: [{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Finetune smolvla with vision encoder · Issue #1774 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1774"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"How to evaluate finetuned SmolVLA model · Issue #1446 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1446"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"}]

Based on the web search results, here's what I found about SmolVLA finetuning in the LeRobot framework:

## SmolVLA Overview

SmolVLA is a compact (450M), open-source Vision-Language-Action model for robotics that runs on consumer hardware. It is pretrained only on compatibly licensed, open-source community-shared datasets under the lerobot tag.

## Finetuning SmolVLA

You can use smolvla_base, the pretrained 450M model, and fine-tune it on your data. Training the model for 20k steps will roughly take ~4 hrs 
…[truncated 846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T09:51:02.656670+00:00_

Web search results for query: "SmolVLA LoRA training recipe lerobot"

Links: [{"title":"lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Parameter efficient fine-tuning with 🤗 PEFT","url":"https://huggingface.co/docs/lerobot/en/peft_training"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"LeRobot datasets and training | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/"},{"title":"Training SmolVLA with LeRobot Notebook - Colab - Google","url":"https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb"}]

Based on the search results, I found comprehensive information about SmolVLA LoRA training with LeRobot:

## SmolVLA LoRA Training Recipe with LeRobot

🤗 PEFT (Parameter-Efficient Fine-Tuning) is a library for efficiently adapting large pretrained models such as SmolVLA to new tasks without training all of the model's parameters while yielding comparable performance.

### Basic Training Command

Here's an example training command: `lerobot-train --policy.path=lerobot/smolvla_base --policy.repo_id=your_hub_name/my_libero_smolvla --dataset.repo_id=HuggingFaceVLA/libero --policy.output_features=null --policy.input_features=null --policy.optimizer_lr=1e-3 --policy.scheduler_decay
…[truncated 984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T09:51:02.656824+00:00_

Web search results for query: "lerobot LIBERO dataset"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/docs/source/libero.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot · PyPI","url":"https://pypi.org/project/lerobot/"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"any4lerobot/libero2lerobot/README.md at main · Tavish9/any4lerobot","url":"https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/README.md"}]

Based on the search results, here's what I found about the LeRobot LIBERO dataset:

## Overview

LIBERO is designed for studying knowledge transfer in multitask and lifelong robot learning problems. The repository is now maintained by the Hugging Face team, with modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments.

## Dataset Contents

LIBERO provides 130 tasks grouped into four task suites: 
…[truncated 825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T09:51:02.656975+00:00_

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
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
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

_source line 24 · 2026-05-13T09:51:02.657107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T09:51:02.657227+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA action dimension architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA action dimension architecture"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-13T09:51:02.657372+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA 7D action gripper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA 7D action gripper"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T09:51:02.657495+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search 4: VLA + LIBERO prior work",
  "prompt": "Search for existing work on fine-tuning VLA (Vision-Language-Action) models on LIBERO benchmark. We want to know if anyone has already done this and what results they got.\n\nDo the following searches:\n\n1. WebSearch for \"OpenVLA LIBERO fine-tune\"\n2. WebSearch for \"VLA fine-tune LIBERO benchmark\"\n3. WebSearch for \"LIBERO fine-tuned VLA checkpoint\"\n4. WebSearch for \"OpenVLA LIBERO results 2025 2026\"\n5. WebSearch for \"pi0 LIBERO\" (Physical Intelligence's model)\n6. WebSearch for \"octo LIBERO fine-tune\"\n7. WebSearch for \"RT-2 LIBERO\" or \"diffusion policy LIBERO\"\n\nFor any relevant papers or blog posts, fetch and extract:\n- Model name and architecture\n- Fine-tuning method (full, LoRA, etc.)\n- LIBERO task suites used\n- Results/success rates\n- Training details (epochs, learning rate, batch size, GPU hours)\n- Whether checkpoints are publicly available\n- Action space configuration used\n\nCompile a comprehensive summary of all VLA + LIBERO prior work, with URLs and key results.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Agent",
  "tool_args": {
    "description": "Search 4: VLA + LIBERO prior work",
    "prompt": "Search for existing work on fine-tuning VLA (Vision-Language-Action) models on LIBERO benchmark. We want to know if anyone has already done this and what results they got.\n\nDo the following searches:\n\n1. WebSearch for \"OpenVLA LIBERO fine-tune\"\n2. WebSearch for \"VLA fine-tune LIBERO benchmark\"\n3. WebSearch for \"LIBERO fine-tuned VLA checkpoint\"\n4. WebSearch for \"OpenVLA LIBERO results 2025 2026\"\n5. WebSearch for \"pi0 LIBERO\" (Physical Intelligence's model)\n6. WebSearch for \"octo LIBERO fine-tune\"\n7. WebSearch for \"RT-2 LIBERO\" or \"diffusion policy LIBERO\"\n\nFor any relevant papers or blog posts, fetch and extract:\n- Model name and architecture\n- Fine-tuning method (full, LoRA, etc.)\n- LIBERO task suites used\n- Results/success rates\n- Training details (epochs, learning rate, batch size, GPU hours)\n- Whether checkpoints are publicly available\n- Action space configuration used\n\nCompile a comprehensive summary of all VLA + LIBERO prior work, with URLs and key results.",
    "model": "sonnet"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-13T09:51:02.657647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA paper arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA paper arxiv 2026"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T09:51:02.657782+00:00_

Web search results for query: "lerobot LIBERO fine-tune"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"},{"title":"lerobot/pi05_libero_finetuned_v044 · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned_v044"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task","url":"https://huggingface.co/docs/lerobot/en/xvla"},{"title":"lerobot/docs/source/libero.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"},{"title":"lerobot/pi05_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_base"},{"title":"lerobot/pi05_libero_finetuned_quantiles_v044 · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned_quantiles_v044"},{"title":"jirufengyu/openpi · Hugging Face","url":"https://huggingface.co/jirufengyu/openpi"}]

Based on the search results, here's what I found about LeRobot LIBERO fine-tuning:

## Overview

LeRobotLiberoDataConfig defines how to process raw LIBERO data from LeRobot dataset for training. LeRobot provides comprehensive support for fine-tuning models on the LIBERO benchmark, which is a robot manipulation simulation environment.

## Fine-tuning Process

The Physical Intelligence LIBERO base model (pi05_libero) was fine-tuned for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the HuggingFace LIBERO dataset. The fine-tuned model is available as lerobot/pi05_libero_finetuned.

## Data Preparation Steps

The fine-tuning process involve
…[truncated 738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-13T09:51:02.657940+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA action space configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA action space configuration"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T09:51:02.658062+00:00_

# LeRobot Training & Fine-tuning Commands

## Training Command

The primary training command uses configuration-based parameters:

```bash
lerobot-train \
  --policy=act \
  --dataset.repo_id=lerobot/aloha_mobile_cabinet
```

This demonstrates the basic syntax for initiating policy training with a specified model architecture and dataset source.

## Evaluation Command

For testing trained policies:

```bash
lerobot-eval \
  --policy.path=lerobot/pi0_libero_finetuned \
  --env.type=libero \
  --env.task=libero_object \
  --eval.n_episodes=10
```

## Available Policy Types

The framework supports multiple model categories suitable for training:

- **Imitation Learning**: ACT, Diffusion, VQ-BeT, Multitask DiT
- **Reinforcement Learning**: HIL-SERL, TDMPC
- **Vision-Language-Action (VLA)**: Pi0Fast, Pi0.5, GR00T N1.5, SmolVLA, XVLA

## Data Format

The **LeRobotDataset** format uses "synchronized MP4 videos (or images) for vision and Parquet files for state/action data," enabling standardized dataset sharing across the Hugging Face Hub.

## Installation

```bash
pip install lerobot
```

The documentation provides GPU/RAM requirements and expected training duration per policy type through the Compute Hardware Guide.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T09:51:02.658202+00:00_

Web search results for query: "lerobot fine-tune guide tutorial custom dataset 2025 2026"

Links: [{"title":"A Practical Guide to Fine-Tuning and Inference with GR00T N1 & LeRobot on a Custom Dataset - DEV Community","url":"https://dev.to/yuk6ra/a-practical-guide-to-fine-tuning-and-inference-with-gr00t-n1-lerobot-on-a-custom-dataset-52ec"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"Tutorial: Fine-tuning on LeRobot V2.1 Dataset","url":"https://github.com/InternRobotics/InternVLA-A1/blob/master/tutorials/finetune_on_lerobot_v21_dataset.md"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LeRobot datasets and training | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/"},{"title":"Fine-Tuning GR00T N1.5 with Phosphobot and a LeRobot SO-100/101 Arm - HackMD","url":"https://hackmd.io/@johnnynunez/HkcuHewaex"},{"title":"Getting Started with LeRobot | ReductStore","url":"https://www.reduct.store/blog/hugging-face-lerobot"},{"title":"LeRobotDataset v3.0 · Hugging Face","url":"https://huggingface.co/docs/lerobot/lerobot-dataset-v3"},{"title":"How to make a custom LeRobotDataset with v2? · Issue #547 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/547"},{"title":"lerobot · PyPI","url":"https://pypi.org/project/lerobot/"}]

I found several helpful resources on LeRobot fine-tuning with custom datasets. Here are the key results:

## Practical Guides & Tutorials

1. **GR00T N1 & LeRobot Fine-Tuning Guide** (July 2025): A comprehensive, step-by-step guide to fine-tuning the GR00T N1 model, running inference on a physical robot, and evaluating the trained model. This covers environment setup, fine-tuning with custom data, inference on physical robots, and evaluation of trained models.

2. **GR00T N1.5 with SO-
…[truncated 1111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-13T09:51:02.658389+00:00_

Web search results for query: "convert LIBERO to lerobot format"

Links: [{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"IPEC-COMMUNITY/libero_90_no_noops_lerobot · Dataset converted ideas","url":"https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"any4lerobot/libero2lerobot/README.md at main · Tavish9/any4lerobot","url":"https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/README.md"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"jirufengyu/openpi · Hugging Face","url":"https://huggingface.co/jirufengyu/openpi"},{"title":"lerobot · PyPI","url":"https://pypi.org/project/lerobot/"},{"title":"lerobot/docs/source/libero.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"}]

Based on the search results, here are the main approaches to convert LIBERO to LeRobot format:

## Official Conversion Script

The Physical Intelligence team provides a minimal example script for converting LIBERO datasets to LeRobot format, which can be run with `uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/your/data --push_to_hub`. This conversion script takes approximately 30 minutes to run.

## Alternative Conversion Tool

An alternative tool called any4lerobot can 
…[truncated 855 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T09:51:02.658544+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot action_dim smolvla config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot action_dim smolvla config"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T09:51:02.658671+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO benchmark action space dimension"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO benchmark action space dimension"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T09:51:02.658791+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO 7D action delta position"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO 7D action delta position"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T09:51:02.658917+00:00_

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
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
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

_source line 38 · 2026-05-13T09:51:02.659031+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T09:51:02.659155+00:00_

# SmolVLA Base Model - Technical Details

## Model Architecture

**Type:** Vision-Language-Action (VLA) model
- **Inputs:** Multi-view images, proprioceptive/state information, optional language instructions
- **Outputs:** Continuous actions
- **Training Objective:** Flow matching
- **Action Representation:** Continuous values
- **Intended Use:** Base model for fine-tuning on specific robotics tasks

## Action & Observation Space

- **Observations:** Multi-view images + proprioceptive state
- **Actions:** Continuous action vectors
- **Language:** Optional task instructions supported

## Supported Datasets

The model is pretrained on community datasets including:
- `lerobot/libero` (referenced in quick start examples)
- Community-driven robotics datasets

## Installation

```bash
pip install "lerobot[smolvla]"
```

For full installation with optional video dependencies (ffmpeg, torchcodec): See [official documentation](https://huggingface.co/docs/lerobot/installation)

## Inference Code

```python
import torch
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.policies.factory import make_pre_post_processors
from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy

# Load model
model_id = "lerobot/smolvla_base"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
policy = SmolVLAPolicy.from_pretrained(model_id).to(device).eval()

# Setup preprocessing/postprocessing
preprocess, postprocess = make_pre_post_processors(
    policy.config,
    model_id,
    preprocessor_overrides={"device_processor": {"device": str(device)}},
)

# Load dataset and run inference
dataset = LeRobotDataset("lerobot/libero")
frame = dict(dataset[0])
batch = preprocess(frame)

with torch.inference_mode():
    pred_action = policy.select_action(frame)
    pred_action = postprocess(pred_action)
```

## Training Configuration

### Training Step (Loss + Backward)

```python
policy.train()
batch = dict(dataset[0])
batch = preprocess(batch)

loss, ou
…[truncated 1431 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-13T09:51:02.659315+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "huggingface lerobot libero 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "huggingface lerobot libero 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T09:51:02.659442+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO dataset huggingface hub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO dataset huggingface hub"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-13T09:51:02.659560+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co LIBERO lerobot dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co LIBERO lerobot dataset"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-13T09:51:02.659684+00:00_

Web search results for query: "LIBERO benchmark action space dimension"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"BOSS: Benchmark for Observation Space Shift in Long-Horizon Task","url":"https://arxiv.org/html/2502.15679v1"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"RL with LIBERO Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html"},{"title":"LIBERO Benchmark | NVlabs/vla0 | DeepWiki","url":"https://deepwiki.com/NVlabs/vla0/4.2-libero-benchmark"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Post-train on LIBERO Benchmark · Issue #30 · Robbyant/lingbot-va","url":"https://github.com/Robbyant/lingbot-va/issues/30"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"}]

Based on the search results, the LIBERO benchmark action space is 7-dimensional continuous actions consisting of 3D end-effector position control (x, y, z), 3D rotation control (roll, pitch, yaw), and gripper control (open/close).

Additionally, the action space is defined as a 7-dimensional relative Cartesian displacement with respect to the gripper 
…[truncated 148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-13T09:51:02.659832+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA LIBERO fine-tune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA LIBERO fine-tune"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-13T09:51:02.659964+00:00_

Web search results for query: "SmolVLA action dimension architecture"

Links: [{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Pedagogical Alignment for Vision-Language-Action Models: A Comprehensive Framework for Data, Architecture, and Evaluation in Education","url":"https://arxiv.org/html/2601.13876"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Decoding SmolVLA: A Vision-Language-Action Model for Efficient and Accessible Robotics","url":"https://blog.phospho.ai/decoding-smolvla-a-vision-language-action-model-for-efficient-and-accessible-robotics/"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"blog/smolvla.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/smolvla.md"},{"title":"VLA (2) SmolVLA, ACT — XLeRobot 0.3.0 documentation","url":"https://xlerobot.readthedocs.io/en/latest/software/getting_started/VLA_smol.html"},{"title":"SmolVLA Models: Compact Vision-Language-Action Systems","url":"https://www.emergentmind.com/topics/smolvla-models"}]

Based on the search results, here's what I found about SmolVLA's action dimension architecture:

## Core Architecture

SmolVLA consists of two core components: a Vision-Language Model (VLM) that processes multimodal inputs and an action expert that outputs robot control commands. SmolVLA's action expert is a compact transformer (~100M parameters) that generates action chunks.

## Action Dimension Handling

SmolVLA uses a dynamic padding approach for handling action dimensions:

Sm
…[truncated 970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-13T09:51:02.660123+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA fine-tune LIBERO benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA fine-tune LIBERO benchmark"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-13T09:51:02.660284+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO fine-tuned VLA checkpoint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO fine-tuned VLA checkpoint"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-13T09:51:02.660411+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA LIBERO results 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA LIBERO results 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-13T09:51:02.660538+00:00_

Web search results for query: "SmolVLA 7D action gripper"

Links: [{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"Single Camera SmolVLA Training - Beginners - Hugging Face Forums","url":"https://discuss.huggingface.co/t/single-camera-smolvla-training/172719"},{"title":"GenAI for Robotics: Fine-Tuning SmolVLA to Pick and Place | by Henry H | Medium","url":"https://medium.com/@henryhu1607/genai-for-robotics-fine-tuning-smolvla-to-pick-and-place-940b485e6c9b"},{"title":"How to easily run inference with a trained model · Issue #2227 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2227"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"SoArm in Lerobot | Seeed Studio Wiki","url":"https://wiki.seeedstudio.com/lerobot_so100m_new/"}]

Based on the search results, here's what I found about SmolVLA and the 7D action gripper configuration:

## SmolVLA Overview

SmolVLA is a groundbreaking Vision-Language-Action (VLA) model with only 450 million parameter
…[truncated 1281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-13T09:51:02.660687+00:00_

Web search results for query: "lerobot action_dim smolvla config"

Links: [{"title":"VLA (2) SmolVLA, ACT — XLeRobot 0.3.0 documentation","url":"https://xlerobot.readthedocs.io/en/latest/software/getting_started/VLA_smol.html"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"`smolvla_base training`: `Expected all tensors to be on the same device` · Issue #1377 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1377"},{"title":"Training SmolVLA with LeRobot Notebook - Colab - Google","url":"https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"}]

Based on the search results, here's what I found about `action_dim` in SmolVLA config:

SmolVLA's dynamic padding supports any action space ≤ 32D, with training padding 12D actions to 32D and inference cropping back to the original 12D, using `config.action_feature.shape[0]` to auto-detect the number of actions.

The key information about `action_dim` in SmolVLA configuration:

1. **Max Action Dimension**: SmolVLA can handle action spaces up to 32D through dynamic padding

2. **Configuration Details**: During training, actions are padded to `self.config
…[truncated 611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-13T09:51:02.660841+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0 LIBERO Physical Intelligence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0 LIBERO Physical Intelligence"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-13T09:51:02.660965+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/smolvla",
  "prompt": "Extract all details: architecture, action_dim, observation space, training commands, config parameters, LoRA/PEFT options, fine-tuning instructions, data format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/smolvla",
    "prompt": "Extract all details: architecture, action_dim, observation space, training commands, config parameters, LoRA/PEFT options, fine-tuning instructions, data format requirements"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-13T09:51:02.661092+00:00_

Web search results for query: "SmolVLA paper arxiv 2026"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"[2602.24143] Robust Skills, Brittle Grounding: Diagnosing Restricted Generalization in Vision-Language Action Policies via Multi-Object Picking","url":"https://arxiv.org/abs/2602.24143"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"SmolVLA - ArXivIQ","url":"https://arxiviq.substack.com/p/smolvla"},{"title":"[2603.07404] Adaptive Capacity Allocation for Vision Language Action Fine-tuning","url":"https://arxiv.org/abs/2603.07404"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"}]

Based on the search results, here's information about the SmolVLA paper on arXiv:

## SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

SmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. The paper w
…[truncated 1364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-13T09:51:02.661248+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "octo LIBERO fine-tune results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "octo LIBERO fine-tune results"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-13T09:51:02.661414+00:00_

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
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-13T09:51:02.661567+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "diffusion policy LIBERO benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "diffusion policy LIBERO benchmark results"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-13T09:51:02.661697+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/peft_training",
  "prompt": "Extract all LoRA/PEFT fine-tuning commands, parameters, configuration options for SmolVLA, target modules, quantization settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/en/peft_training",
    "prompt": "Extract all LoRA/PEFT fine-tuning commands, parameters, configuration options for SmolVLA, target modules, quantization settings"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-13T09:51:02.661834+00:00_

Web search results for query: "LIBERO 7D action delta position"

Links: [{"title":"physical-intelligence/libero · Description of the dataset features","url":"https://huggingface.co/datasets/physical-intelligence/libero/discussions/1"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"State/Action representation in LIBERO dataset (EEF vs Joint) · Issue #637 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/637"},{"title":"Why is extra_delta_action=True in 'pi0_libero' config? · Issue #750 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/750"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"openvla/modified_libero_rlds · Detailed description of the features","url":"https://huggingface.co/datasets/openvla/modified_libero_rlds/discussions/5"},{"title":"Absolute control for LIBERO · Issue #43 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/43"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"The Libero: Volleyball’s Defensive Position | Imperial Point","url":"https://theimperialpoint.com/blog/the-libero-volleyballs-defensive-position/"}]

Based on the search results, here's what I found about LIBERO 7D action delta position:

## LIBERO 7D Action Format

LIBERO uses continuous control actions in a 7-dimensional format consisting of 6D end-effector delta plus 1D gripper. More specifically:

**Action Composition:**
The action length of 7 equals 6 Delta EEF Pose + 1 gripper (-1 for open and 1 for close)

**Delta vs. Absolute:**
In LIBERO, the raw actions in the dataset are already delta actions. This mea
…[truncated 796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-13T09:51:02.661989+00:00_

Web search results for query: "SmolVLA action space configuration"

Links: [{"title":"VLA (2) SmolVLA, ACT — XLeRobot 0.3.0 documentation","url":"https://xlerobot.readthedocs.io/en/latest/software/getting_started/VLA_smol.html"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"}]

I found comprehensive information about SmolVLA's action space configuration. Here are the key findings:

## Action Space Configuration

SmolVLA's dynamic padding supports any action space ≤ 32D, unlike other VLA models (e.g., xVLA) that may require manual action_mode configuration.

For the SO101 robot, SmolVLA uses a 6-DOF action space consisting of shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll, and gripper.

## Action Generation App
…[truncated 1179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-13T09:51:02.662140+00:00_

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
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-13T09:51:02.662333+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://docs.phospho.ai/learn/train-smolvla",
  "prompt": "Extract all training commands, configuration parameters, data format requirements, step-by-step instructions for fine-tuning SmolVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://docs.phospho.ai/learn/train-smolvla",
    "prompt": "Extract all training commands, configuration parameters, data format requirements, step-by-step instructions for fine-tuning SmolVLA"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-13T09:51:02.662492+00:00_

Web search results for query: "LIBERO dataset huggingface hub"

Links: [{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"yifengzhu-hf/LIBERO-datasets · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"openvla/modified_libero_rlds · Datasets at Hugging Face","url":"https://huggingface.co/datasets/openvla/modified_libero_rlds"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"Libero Benchmark Dataset - a IPEC-COMMUNITY Collection","url":"https://huggingface.co/collections/IPEC-COMMUNITY/libero-benchmark-dataset"}]

Based on the search results, here's information about the LIBERO dataset on Hugging Face Hub:

## Overview

LIBERO is a benchmark designed to study lifelong robot learning — the idea that robots need to keep learning and adapting with their users over time. It provides a set of standardized manipulation tasks that focus on knowledge transfer: how well a robot can apply what it has already learned to new situations.

## Available Datasets on Hugging Face

There are several LIBERO dataset repositories hosted on Huggi
…[truncated 862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-13T09:51:02.662655+00:00_

Web search results for query: "site:huggingface.co LIBERO lerobot dataset"

Links: [{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"lerobot/libero_10_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_10_image"},{"title":"lerobot/pi05_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_base"},{"title":"jesbu1/libero_90_lerobot · Datasets at Hugging Face","url":"https://huggingface.co/datasets/jesbu1/libero_90_lerobot"},{"title":"README.md · physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/blob/main/README.md"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"}]

I found several results related to LIBERO and LeRobot datasets on Hugging Face. Here's a summary:

## Main Datasets Found:

1. **lerobot/libero** - This dataset was created using LeRobot

2. **physical-intelligence/libero** - This dataset combines four individual Libero datasets: Libero-Spatial, Libero-Object, Libero-Goal and Libero-10. All datasets were taken from here and converted into LeRobot format

3. **HuggingFaceVLA/libero** - A preprocessed LIBERO dataset that is fully compatible with the current LeRobot codebase and requires no additional manipulation

## Additional Variants:

- **lerobot/libero_object_image** - A specific variant focusing on object images
- **lerobot/libero_10_image** 
…[truncated 410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-13T09:51:02.662805+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632",
  "prompt": "Extract all code, training commands, configuration, action dimensions, data format, step-by-step fine-tuning process for SmolVLA in new environments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632",
    "prompt": "Extract all code, training commands, configuration, action dimensions, data format, step-by-step fine-tuning process for SmolVLA in new environments"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-13T09:51:02.662939+00:00_

Web search results for query: "OpenVLA LIBERO fine-tune"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"openvla/openvla-7b-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-10"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"openvla/openvla-7b-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-object"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"}]

Based on the search results, here's what I found about OpenVLA LIBERO fine-tuning:

## Overview

OpenVLA was fine-tuned via LoRA (r=32) on four LIBERO task suites independently: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-10.

## Available Checkpoints

The OpenVLA 7B model was fine-tuned via LoRA (r=32) on the LIBERO-Spatial dataset from the LIBERO simulation benchmark, with similar checkpoints available for the other LIBERO task suites.

## Optimized Fine-Tuning A
…[truncated 886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-13T09:51:02.663089+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/blog/smolvla",
  "prompt": "Extract: model architecture details, action_dim, training data, fine-tuning approach, pretraining vs finetuning distinction, performance numbers, training config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/blog/smolvla",
    "prompt": "Extract: model architecture details, action_dim, training data, fine-tuning approach, pretraining vs finetuning distinction, performance numbers, training config"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-13T09:51:02.663230+00:00_

Web search results for query: "VLA fine-tune LIBERO benchmark"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"openvla/openvla-7b-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-10"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"}]

Based on the search results, here's what I found about VLA fine-tuning on the LIBERO benchmark:

## Overview

The updated OpenVLA paper (v2) discusses fine-tuning OpenVLA on a simulated benchmark, LIBERO, in Appendix E.

## Key Results

OpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1%. Additionally,
…[truncated 928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-13T09:51:02.663410+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2506.01844v1",
  "prompt": "Extract all details about action space, action dimension, action_dim configuration, how actions are represented (6D, 7D, joint angles, end-effector), gripper handling, max_action_dim, padding, and any configuration parameters related to action space. Also look for any mention of LIBERO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2506.01844v1",
    "prompt": "Extract all details about action space, action dimension, action_dim configuration, how actions are represented (6D, 7D, joint angles, end-effector), gripper handling, max_action_dim, padding, and any configuration parameters related to action space. Also look for any mention of LIBERO."
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-13T09:51:02.663554+00:00_

Web search results for query: "LIBERO fine-tuned VLA checkpoint"

Links: [{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"},{"title":"LightVLA/LIBERO.md at main · LiAutoAD/LightVLA","url":"https://github.com/LiAutoAD/LightVLA/blob/main/LIBERO.md"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"README.md · moojink/openvla-7b-oft-finetuned-libero-10 at main","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10/blob/main/README.md"},{"title":"Openvla 7b Oft Finetuned Libero Goal","url":"https://model.aibase.com/models/details/1935154868096602112"}]

Based on the search results, here's information about LIBERO fine-tuned VLA checkpoints:

## OpenVLA-OFT Fine-Tuned LIBERO Checkpoints

OpenVLA-OFT, a policy created with optimized fine-tuning techniques, achieves state-of-the-art results in LIBERO with a 97.1% average success rate across 4 task suites, outperforming π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy.

### Available Checkpoints

Several fine-tuned OpenVLA-OFT checkpoints are available on Hugging Face, including:
- `moojink/openvla-7b-oft-finetuned-libero-spatial`
- `moojink/openvla-7b-oft-finetuned-libero
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-13T09:51:02.663701+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/2259",
  "prompt": "Extract all technical details about action dimensions, action_dim configuration, how to fine-tune SmolVLA on different environments/embodiments with different action spaces, and any specific mention of 6D vs 7D actions or LIBERO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/issues/2259",
    "prompt": "Extract all technical details about action dimensions, action_dim configuration, how to fine-tune SmolVLA on different environments/embodiments with different action spaces, and any specific mention of 6D vs 7D actions or LIBERO."
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-13T09:51:02.663883+00:00_

Web search results for query: "octo LIBERO fine-tune results"

Links: [{"title":"The details of fine-tuning Octo using LIBERO · Issue #215 · openvla/openvla","url":"https://github.com/openvla/openvla/issues/215"},{"title":"FLOWER: Democratizing Generalist Robot Policies","url":"https://arxiv.org/pdf/2509.04996"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/"},{"title":"octo/examples/02_finetune_new_observation_action.py at main · octo-models/octo","url":"https://github.com/octo-models/octo/blob/main/examples/02_finetune_new_observation_action.py"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"Random behavior after fine tuning octo on new robot · Issue #29 · octo-models/octo","url":"https://github.com/octo-models/octo/issues/29"},{"title":"An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/paper.pdf"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/html/2405.12213v2"},{"title":"openvla/README.md at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/README.md"}]

Based on the web search results, I found information about fine-tuning Octo using LIBERO. Here's what the search revealed:

## Octo Fine-tuning on LIBERO

On average across the six evaluation setups, Octo outperforms the next best baseline by 52%. Each task uses ~100 target demonstrations, and importantly, the same finetuning recipe is used for all evaluation tasks, making this a good default configuration for Octo finetuning.

### Fine-tuning Approach

Octo was designed specifically to support efficient finetuning to new robot setups, including robots with different actions and different combinations of cameras and proprioceptive information.

##
…[truncated 758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-13T09:51:02.664136+00:00_

Web search results for query: "pi0 LIBERO Physical Intelligence"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"Open Sourcing π0","url":"https://www.pi.website/blog/openpi"},{"title":"Physical Intelligence open-sources Pi0 robotics foundation model","url":"https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"},{"title":"lerobot/pi0_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi0_libero_base"},{"title":"π₀ (Pi0) · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi0"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"π₀.₅ (Pi05) Policy · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi05"},{"title":"[Paper Review] Pi0, Pi0.5, Pi0-FAST - Tracing the Path of Physical Intelligence (PI)","url":"https://bequiet-log.vercel.app/pi-review"},{"title":"Pi0 fast libero checkpoint no longer works with new repo? · Issue #849 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/849"},{"title":"openpi/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/README.md"}]

Based on the search results, here's what I found about π0 LIBERO from Physical Intelligence:

## Overview

π₀ is a Vision-Language-Action model for general robot control, from Physical Intelligence. π0 Libero is a checkpoint fine-tuned for the Libero benchmark, and can be evaluated on Libero tasks out of the box.

## Key Features

π₀ is designed to be a generalist policy that can understand visual inputs, interpret natural language instructions, and control a variety of different robots across diverse tasks. It uses flow matching to augment pre-trained VLMs with continuous action outputs via flow matching, is trained across 8 distinct robot platforms, and outp
…[truncated 708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-13T09:51:02.664412+00:00_

Web search results for query: "huggingface lerobot libero 2025 2026"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LeRobot v0.4.0: Supercharging OSS Robot Learning","url":"https://huggingface.co/blog/lerobot-release-v040"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"GitHub - OpenDriveLab/AgiBot-World: [IROS 2025 Best Paper Award Finalist & IEEE TRO 2026] The Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems · GitHub","url":"https://github.com/OpenDriveLab/AgiBot-World"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Critical Unpatched Flaw Leaves Hugging Face LeRobot Open to Unauthenticated RCE","url":"https://thehackernews.com/2026/04/critical-cve-2026-25874-leaves-hugging.html"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"}]

Based on the search results, here's what I found about Hugging Face LeRobot and LIBERO in 2025-2026:

## LeRobot v0.4.0 Release

LeRobot v0.4.0 delivers a major upgrade for open-source robotics, introducing scalable Datasets v3.0, powerful new VLA models like PI0.5 and GR00T N1.5, and a new plugin system for easier hardware integration. The release also adds support for LIBERO and Meta-World simulations, simplified multi-GPU training, and a new Hugging Face Robot Lear
…[truncated 1077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-13T09:51:02.664656+00:00_

Web search results for query: "diffusion policy LIBERO benchmark results"

Links: [{"title":"nvidia/Cosmos-Policy-LIBERO-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Efficient Diffusion Transformer Policies with Mixture of Expert Denoisers for Multitask Learning","url":"https://mbreuss.github.io/MoDE_Diffusion_Policy/"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"}]

Here are the key benchmark results for diffusion policy models on the LIBERO benchmark:

## NVIDIA Cosmos-Policy Performance

The Cosmos-Policy-LIBERO-Predict2-2B model achieves state-of-the-art performance on the LIBERO simulation benchmark with a 98.5% average success rate across four task suites. More specifically, the breakdown is: Spatial: 98.1%, Object: 100.0%, Goal: 98.2%, Long: 97.6%.

## Mix
…[truncated 843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-13T09:51:02.664892+00:00_

Web search results for query: "OpenVLA LIBERO results 2025 2026"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks | Proceedings of the 2025 Workshop on Large AI Systems and Models with Privacy and Security Analysis","url":"https://dl.acm.org/doi/10.1145/3733800.3763262"},{"title":"LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"},{"title":"LIBERO-Object: Lifelong Learning in Robotic Manipulation","url":"https://www.emergentmind.com/topics/libero-object"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"}]

Based on the search results, here's what I found about OpenVLA LIBERO results from 2025-2026:

## Performance on Standard LIBERO Benchmark

Strong 2025-era VLA policies (OpenVLA, pi0, Octo variants) typically land in the 70-90 percent success range on Spatial, Object, and Goal, and 30-60 percent on LIBERO-100 depending on training recipe.

VLAs exhibit strong performance on the Li
…[truncated 1124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-13T09:51:02.665118+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/lerobot/smolvla_base",
  "prompt": "Extract the model card details including action space configuration, action_dim, max_action_dim, any config parameters, and details about what action dimensions the base model was trained on."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/lerobot/smolvla_base",
    "prompt": "Extract the model card details including action space configuration, action_dim, max_action_dim, any config parameters, and details about what action dimensions the base model was trained on."
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-13T09:51:02.665349+00:00_

# SmolVLA Fine-tuning: Training Commands & Configuration

## Primary Training Command

```bash
uv run lerobot/scripts/train.py \
--policy.path=lerobot/smolvla_base \
--dataset.repo_id=PLB/phospho-playground-mono \
--batch_size=256 \
--steps=30000 \
--wandb.enable=true \
--save_freq=5000 \
--wandb.project=smolvla
```

## Key Configuration Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `batch_size` | 256 | Training batch size |
| `steps` | 30000 | Total training iterations |
| `save_freq` | 5000 | Checkpoint frequency |
| `n_action_steps` | 50 | Must be changed in `config.json` for inference |

## Critical Configuration Requirement

**Before inference, modify the model's `config.json`:**
- Locate: `lerobot/smolvla_base/config.json`
- Change `"n_action_steps": 1,` to `"n_action_steps": 50,`

Without this adjustment, "the inference will be very slow, as the model will only predict one action at a time instead of a sequence of actions."

## Dataset Format

The training example uses the Hugging Face Hub dataset: `PLB/phospho-playground-mono` (a "pick and place" dataset).

## Environment Setup Steps

1. Install `uv` package manager
2. Clone LeRobot repository
3. Create virtual environment with Python 3.10
4. Install dependencies: `uv pip install -e ".[feetech,smolvla]"`

## Hardware Requirements

Training requires "a powerful GPU"—the documentation references NVIDIA A100, though "any modern NVIDIA GPU with sufficient VRAM should work."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-13T09:51:02.665579+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/smolvla",
  "prompt": "Extract all configuration details especially about action_dim, action space, max_action_dim, how to fine-tune for different action spaces, and any LIBERO-related information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/en/smolvla",
    "prompt": "Extract all configuration details especially about action_dim, action space, max_action_dim, how to fine-tune for different action spaces, and any LIBERO-related information."
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-13T09:51:02.665792+00:00_

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
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-13T09:51:02.666017+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/libero",
  "prompt": "Extract all technical details: how to convert LIBERO HDF5 to LeRobot format, observation keys, action dimensions, episode structure, dataset format, installation steps, training commands, and any code snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/en/libero",
    "prompt": "Extract all technical details: how to convert LIBERO HDF5 to LeRobot format, observation keys, action dimensions, episode structure, dataset format, installation steps, training commands, and any code snippets."
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-13T09:51:02.666231+00:00_

# LIBERO

LIBERO is a benchmark designed to study **lifelong robot learning** — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once. It provides a set of standardized manipulation tasks that focus on **knowledge transfer**: how well a robot can apply what it has already learned to new situations. By evaluating on LIBERO, different algorithms can be compared fairly and researchers can build on each other's work.

- Paper: [Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)
- GitHub: [Lifelong-Robot-Learning/LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
- Project website: [libero-project.github.io](https://libero-project.github.io)

![An overview of the LIBERO benchmark](https://libero-project.github.io/assets/img/libero/fig1.png)

## Available tasks

LIBERO includes **five task suites** covering **130 tasks**, ranging from simple object manipulations to complex multi-step scenarios:

| Suite          | CLI name         | Tasks | Description                                        |
| -------------- | ---------------- | ----- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | Long-horizon tasks from the LIBERO-100 collection  |

## Installation

After following the LeRobot installation instructions:

```bash
pip install -e ".[libero]"
```

LIBERO requires Linux (`sys_platform == 'linux'`). LeRobot uses MuJoCo for simulation — set the rendering backend before training or evaluation:

```bash
export MUJOCO_GL=egl  # fo
…[truncated 4883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-13T09:51:02.666473+00:00_

# Action Space Details from SmolVLA Paper

## Action Representation

The paper does not explicitly specify the dimensionality of the action space (e.g., 6D, 7D, joint angles). Instead, it focuses on **action chunks** as the primary abstraction.

### Action Chunk Configuration

SmolVLA predicts sequences of actions denoted as **𝐀_t = (a_t, ..., a_{t+n})**, where actions are grouped into chunks of size **n = 50** by default. The paper states: "the model outputs a chunk of actions" and describes this as "sequences of n (much greater than 1) low-level commands."

The ablation study (Table 12) examines chunk sizes ranging from 1 to 100 steps, finding that "chunk sizes between 10 and 50 strike a good balance between action prediction frequency and performance."

## Robot-Specific Action Details

While specific action dimensions aren't detailed, the paper mentions evaluating on:
- **SO-100/SO-101**: "six degrees of freedom" arms using "position commands"
- **Panda (LIBERO)**: "7-DOF torque-controlled robotic arm"
- **Sawyer (Meta-World)**: "4-DOF controlled robotic arm" where "the policy control[s] the position and state of the gripper"

## Training Configuration

- Flow matching is used as the training objective
- Actions are normalized implicitly through the flow matching framework
- No explicit padding or max_action_dim parameters are mentioned

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-13T09:51:02.666705+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py",
  "prompt": "Extract the full conversion script including all functions, observation keys used, action keys, how HDF5 data is read and converted to LeRobot format, and the command-line interface."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py",
    "prompt": "Extract the full conversion script including all functions, observation keys used, action keys, how HDF5 data is read and converted to LeRobot format, and the command-line interface."
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-13T09:51:02.666900+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.19645",
  "prompt": "Extract: model name and architecture, fine-tuning method (full/LoRA/etc.), LIBERO task suites used, per-suite success rates, training details (epochs, learning rate, batch size, GPU hours/days), action space configuration, whether checkpoints are public"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2502.19645",
    "prompt": "Extract: model name and architecture, fine-tuning method (full/LoRA/etc.), LIBERO task suites used, per-suite success rates, training details (epochs, learning rate, batch size, GPU hours/days), action space configuration, whether checkpoints are public"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-13T09:51:02.667068+00:00_

# SmolVLA Base Model Card Details

Based on the provided web page content, here's what I can extract about the model configuration:

## Model Overview
- **Model ID**: `lerobot/smolvla_base`
- **Type**: Vision-Language-Action (VLA) model
- **Framework**: LeRobot
- **Paper**: SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arxiv: 2506.01844)

## Input/Output Specifications

**Inputs:**
- Images (multi-view)
- Proprioceptive/state information
- Optional language instruction

**Outputs:**
- Continuous actions

## Training Configuration
- **Training Objective**: Flow matching
- **Action Representation**: Continuous
- **Intended Use**: Base model for fine-tuning on specific use cases

## Notable Limitations

**The provided webpage does NOT include:**
- Specific `action_dim` values
- `max_action_tokens` configuration
- `chunk_size` defaults
- `n_action_steps` configuration
- Details about what action dimensions the base model was trained on

## Available Configuration Flags

From the fine-tuning section, these policy-specific parameters can be set:
```
-policy.chunk_size=...
-policy.n_action_tokens=...
-policy.max_action_tokens=...
-policy.gradient_checkpointing=true
```

**Note**: For complete action space configuration details, you would need to consult the official model card on Hugging Face Hub directly or check the [LeRobot GitHub repository](https://github.com/huggingface/lerobot) and official documentation at https://huggingface.co/docs/lerobot/.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-13T09:51:02.667213+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/lerobot/libero",
  "prompt": "Extract dataset card details: what data is included, format, features/columns, observation keys, action dimensions, number of episodes per task suite, and how to load it."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/lerobot/libero",
    "prompt": "Extract dataset card details: what data is included, format, features/columns, observation keys, action dimensions, number of episodes per task suite, and how to load it."
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-13T09:51:02.667381+00:00_

# Technical Details from GitHub Issue #2259

## Action Space Dimensions

The issue mentions specific action dimensions without providing definitive technical specifications:

- **SmolVLA/π₀ pretraining specs**: The user explicitly requests clarification on "exact action and state spaces" but notes these details are not clearly documented.

- **LIBERO dataset actions**: "In HuggingFaceVLA/smol-libero the actions have dimension 7, which doesn't clearly map to 7 joint angles + gripper."

## Action Space Representations

The user's successful OpenVLA implementation used: "action space is defined as ΔEEF pose (Euler rotation) + gripper, and the state as ΔEEF pose (quaternion rotation) + gripper"

However, the document lacks official specifications for SmolVLA's expected action format.

## Fine-tuning Configuration Issues

Key problems identified:
- Model achieved "0% success" on RLBench evaluation despite training convergence
- User suspects misalignment between "state and action spaces for SmolVLA"
- No documented guidance on camera naming conventions affecting performance

## Robot Embodiments

- **SO100/SO101**: Base pretraining robot (7DoF configuration implied)
- **LIBERO**: Used for HuggingFaceVLA/smolvla_libero; unclear if "6DoF or 7DoF Franka setup"
- **Franka Panda**: User's target robot (7DoF + gripper)

The issue essentially highlights the **absence of clear documentation** regarding action dimensions and embodiment-specific configurations needed for successful transfer learning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-13T09:51:02.667549+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial",
  "prompt": "Extract: model details, fine-tuning method, training config (epochs, lr, batch size, hardware), action space, LIBERO task suite, success rate results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial",
    "prompt": "Extract: model details, fine-tuning method, training config (epochs, lr, batch size, hardware), action space, LIBERO task suite, success rate results"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-13T09:51:02.667684+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/lerobot/pi0_libero_base",
  "prompt": "Extract: model architecture, fine-tuning details, LIBERO task suite and results, training config, action space"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/lerobot/pi0_libero_base",
    "prompt": "Extract: model architecture, fine-tuning details, LIBERO task suite and results, training config, action space"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-13T09:51:02.667814+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B",
  "prompt": "Extract: model architecture, fine-tuning method, LIBERO task suite results (per suite success rates), training details, action space configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B",
    "prompt": "Extract: model architecture, fine-tuning method, LIBERO task suite results (per suite success rates), training details, action space configuration"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-13T09:51:02.667941+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RoboVLMs LIBERO benchmark VLA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RoboVLMs LIBERO benchmark VLA 2025"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-13T09:51:02.668072+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LightVLA LIBERO results fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LightVLA LIBERO results fine-tuning"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-13T09:51:02.668239+00:00_

# SmolVLA Fine-Tuning: Code, Configuration, and Process

## Training Command

The author provided a 35-line Google Colab training script:

```python
!git clone https://github.com/huggingface/lerobot.git
!cd lerobot && pip install -e ".[smolvla]"

from huggingface_hub import login
from google.colab import userdata

try:
    token = userdata.get('HF_TOKEN')
    login(token=token, add_to_git_credential=True)
except Exception:
    print("HF_TOKEN secret not found. Please login interactively:")
    login(add_to_git_credential=True)

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

!python -m lerobot.scripts.lerobot_train \
  --dataset.repo_id Xavier033/new_libero \
  --policy.repo_id Xavier033/new_libero_policy \
  --dataset.revision main \
  --policy.type smolvla \
  --policy.pretrained_path HuggingFaceVLA/smolvla_libero \
  --policy.expert_width_multiplier 0.5 \
  --policy.num_vlm_layers 0 \
  --policy.vlm_model_name HuggingFaceTB/SmolVLM2-500M-Instruct \
  --output_dir lerobot_outputs \
  --job_name smolvla_panda_pick_libero \
  --batch_size 64 \
  --steps 5000 \
  --optimizer.lr 1e-5 \
  --num_workers 4 \
  --save_freq 500 \
  --eval_freq 500 \
  --wandb.enable false \
  --policy.push_to_hub true \
  --save_checkpoint true
```

## Data Format Configuration

The `info.json` structure defines observations and actions:

**Images:**
- Resolution: 256×256 pixels
- Format: 3-channel (RGB)
- Multiple cameras: `image` and `image2`

**Observation State (8 dimensions):**
- Position: x, y, z
- Rotation: roll, pitch, yaw
- Gripper: grip_l, grip_r

**Action Space (7 dimensions):**
- Deltas: dx, dy, dz (position changes)
- Rotation deltas: droll, dpitch, dyaw
- Gripper command: grip

## Critical Statistics File

The author emphasizes using dataset-specific `stats.json` instead of LIBERO's statistics: "action_denorm = action * self.action_stats['std'] + self.action_stats['mean']"

Using incorrect statistics caused "erratic behavior" and required denormalization with the co
…[truncated 1400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-13T09:51:02.668446+00:00_

# Extraction Summary

Based on the arXiv page content provided, here's what can be determined:

**Model & Architecture:**
- Base model: OpenVLA
- Fine-tuned variant: OpenVLA-OFT (Optimized Fine-Tuning)

**Fine-Tuning Method:**
The page indicates the approach involves "parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective" but does not specify whether full fine-tuning, LoRA, or other parameter-efficient methods were used.

**LIBERO Performance:**
- "LIBERO simulation benchmark" shows improvement from 76.5% to 97.1% average success rate across four task suites
- Specific per-suite breakdown is not provided in this abstract

**Training Details:**
No information about epochs, learning rate, batch size, or computational requirements (GPU hours/days) appears on this page.

**Action Space Configuration:**
Described as "continuous action representation" with action chunking, but detailed specifications are absent.

**Checkpoint Availability:**
The paper states "We release code for OFT and pretrained model checkpoints" with a reference to a project website, indicating public availability.

**Limitation:** This is an abstract page; comprehensive implementation details likely appear in the full paper PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-13T09:51:02.668594+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/issues/637",
  "prompt": "Extract all technical details about LIBERO action space: is it EEF or joint control? What are the action dimensions? How is gripper action represented? Any details about 7D action breakdown."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Physical-Intelligence/openpi/issues/637",
    "prompt": "Extract all technical details about LIBERO action space: is it EEF or joint control? What are the action dimensions? How is gripper action represented? Any details about 7D action breakdown."
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-13T09:51:02.668722+00:00_

# LeRobot Libero Conversion Script Summary

## Full Conversion Script
The script converts Libero datasets (stored in RLDS format) to LeRobot format. The main function accepts a data directory path and optional Hugging Face Hub push capability.

## Observation and Action Keys
**Observations extracted:**
- `image`: 256×256×3 RGB image
- `wrist_image`: 256×256×3 wrist camera view
- `state`: 8-dimensional float32 proprioceptive state

**Actions:**
- 7-dimensional float32 action vector (Panda robot)

**Metadata:**
- `task`: Language instruction decoded from episodes

## Data Reading and Conversion Process
Rather than HDF5, this script reads from RLDS-formatted datasets using TensorFlow Datasets. The conversion workflow:

1. Loads raw Libero datasets via `tfds.load()`
2. Iterates through episodes and individual steps
3. Extracts observations, actions, and task descriptions
4. Calls `dataset.add_frame()` to append each timestep
5. Invokes `dataset.save_episode()` after completing each episode

## Command-Line Interface
The script uses the `tyro` library for CLI argument parsing:

**Basic usage:** `uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/data`

**With Hub upload:** `uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/data --push_to_hub`

## Key Configuration
- FPS: 10 Hz
- Robot type: Panda
- Image writer threads: 10
- Image writer processes: 5
- Multiple Libero datasets combined into single training dataset

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-13T09:51:02.668861+00:00_

# OpenVLA 7B Fine-Tuned on LIBERO-Spatial - Model Details

## Model Information
- **Base Model**: OpenVLA 7B
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **LoRA Rank**: 32
- **LoRA Dropout**: 0.0
- **Model Size**: 8B parameters
- **Tensor Type**: BF16
- **License**: MIT

## Training Configuration

| Parameter | Value |
|-----------|-------|
| **Hardware** | 8 x A100 GPUs (80GB memory) |
| **Learning Rate** | 5e-4 |
| **Batch Size** | 128 (8 GPUs × 16 samples each) |
| **Training Steps** | 50,000 gradient steps |
| **Shuffle Buffer Size** | 100,000 |
| **Quantization** | None (train or test) |
| **Gradient Accumulation** | Disabled (grad_accumulation_steps == 1) |

## Training Details
- **Dataset**: LIBERO-Spatial (from LIBERO simulation benchmark)
- **Image Augmentations**: Random crop, color jitter
- **Quantization**: No quantization at train or test time

## Action Space & Results
⚠️ **Note**: The provided web page content does not include:
- Specific action space details
- LIBERO task suite breakdown
- Success rate results/benchmarks

For detailed evaluation results and task specifications, refer to the [OpenVLA GitHub README](https://github.com/openvla/openvla/blob/main/README.md) and the [OpenVLA paper (arXiv:2406.09246)](https://arxiv.org/abs/2406.09246).

## Quick Start
```python
from transformers import AutoModelForVision2Seq

model = AutoModelForVision2Seq.from_pretrained(
    "openvla/openvla-7b-finetuned-libero-spatial",
    trust_remote_code=True,
    dtype="auto"
)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-13T09:51:02.669009+00:00_

# SmolVLA: Key Technical Details

## Model Architecture

SmolVLA consists of two core components:

### 1. Vision-Language Model (VLM) Backbone
- **Base Model**: SmolVLM2-500M-Video-Instruct
- **Vision Encoder**: SigLIP
- **Language Decoder**: SmolLM2-1.7B-Instruct
- **Visual Token Reduction**: Limited to **64 tokens per frame** (vs. 1024) using PixelShuffle
- **Layer Skipping**: Uses features from intermediate layers (configurable to **half the total layers**) for faster inference

### 2. Action Expert
- **Architecture**: Flow Matching Transformer (~100M parameters)
- **Hidden Size**: 75% of VLM's hidden dimension
- **Attention Design**: Interleaved cross-attention (CA) and self-attention (SA) blocks
  - Cross-attention: actions attend to VLM features
  - Self-attention: actions attend causally to past actions (temporal smoothness)
- **Action Representation**: Continuous action sequences (non-autoregressive prediction)
- **Training Objective**: Flow matching (guides noisy samples back to ground truth)

## Action Dimensions & Training Data

**Model Size**: 450M parameters total

**Training Data**:
- Source: LeRobot Community Datasets (publicly available, compatibly licensed)
- Volume: ~10 million frames (~487 high-quality datasets)
- **Order of magnitude smaller** than other VLAs (other models use 100M+ frames)
- Primary embodiment: SO100 robotic arm (6 DOF)
- Frame rate: Standardized at 30 FPS

**Data Processing**:
- Task annotations improved using Qwen2.5-VL-3B-Instruct (rewritten to <30 characters, action-verb prefixed)
- Camera views standardized: `OBS_IMAGE_1` (top-down), `OBS_IMAGE_2` (wrist-mounted), `OBS_IMAGE_3+` (additional)

## Pretraining vs Fine-tuning

### Pretraining Phase
- Trained on general manipulation data from LeRobot community datasets
- Impact on SO100: **51.7% → 78.3% success** (+26.6% absolute improvement)

### Fine-tuning Phase
- Task-specific post-training on target tasks
- Further boosts performance through multitask learning
- Demonstrate
…[truncated 1730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-13T09:51:02.669162+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
  "prompt": "Extract all action space details for LIBERO: action dimensions, what each dimension represents, delta vs absolute, gripper representation, any configuration parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
    "prompt": "Extract all action space details for LIBERO: action dimensions, what each dimension represents, delta vs absolute, gripper representation, any configuration parameters."
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-13T09:51:02.669328+00:00_

# LIBERO-plus

LIBERO-plus is a **robustness benchmark** for Vision-Language-Action (VLA) models built on top of [LIBERO](./libero). It systematically stress-tests policies by applying **seven independent perturbation dimensions** to the original LIBERO task set, exposing failure modes that standard benchmarks miss.

- Paper: [In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626)
- GitHub: [sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)
- Dataset: [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

![An overview of the LIBERO-plus benchmark perturbation dimensions](https://github.com/sylvestf/LIBERO-plus/raw/main/static/images/libero-plus.jpg)

## Perturbation dimensions

LIBERO-plus creates ~10 000 task variants by perturbing each original LIBERO task along these axes:

| Dimension             | What changes                                          |
| --------------------- | ----------------------------------------------------- |
| Objects layout        | Target position, presence of confounding objects      |
| Camera viewpoints     | Camera position, orientation, field-of-view           |
| Robot initial states  | Manipulator start pose                                |
| Language instructions | LLM-rewritten task description (paraphrase / synonym) |
| Light conditions      | Intensity, direction, color, shadow                   |
| Background textures   | Scene surface and object appearance                   |
| Sensor noise          | Photometric distortions and image degradation         |

## Available task suites

LIBERO-plus covers the same five suites as LIBERO:

| Suite          | CLI name         | Tasks | Max steps | Description                                        |
| -------------- | ---------------- | ----- | --------- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | 280       | Tasks requiring reasoning about spatia
…[truncated 5193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-13T09:51:02.669473+00:00_

# π₀ (Pi0) Model - Key Details

## Model Architecture

**π₀** is a Vision-Language-Action (VLA) foundation model from Physical Intelligence designed for robot control.

- **Inputs:** Multi-view images, proprioceptive/state information, optional language instructions
- **Outputs:** Continuous actions
- **Training Objective:** Flow matching
- **Action Representation:** Continuous
- **Model Size:** 4B parameters
- **Intended Use:** Base model for fine-tuning on specific robotics tasks

## Fine-tuning Configuration

Training command with configurable parameters:

```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/&lt;dataset> \
  --output_dir=./outputs/[RUN_NAME] \
  --job_name=[RUN_NAME] \
  --policy.repo_id=${HF_USER}/&lt;desired_policy_repo_id> \
  --policy.path=lerobot/pi0_libero_base \
  --policy.dtype=bfloat16 \
  --policy.device=cuda \
  --steps=100000 \
  --batch_size=4
```

**Policy-specific flags:**
- `-policy.chunk_size=...`
- `-policy.n_action_steps=...`
- `-policy.max_action_tokens=...`
- `-policy.gradient_checkpointing=true`

## LIBERO Task Suite & Evaluation

Evaluation in LIBERO simulation environment:

```bash
lerobot-eval \
  --policy.path=lerobot/pi0_libero_base \
  --env.type=libero \
  --env.task=libero_object \
  --eval.batch_size=1 \
  --eval.n_episodes=20
```

The model is specifically trained on the LIBERO benchmark dataset (`lerobot/libero`) for evaluating manipulation tasks.

## Training Configuration Example

```python
policy.train()
batch = dict(dataset[0])
batch = preprocess(batch)
loss, outputs = policy.forward(batch)
loss.backward()
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-13T09:51:02.669623+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632",
  "prompt": "Extract all details about action dimensions used, how action_dim is configured, any mismatch between SmolVLA default and the target environment, and specific config parameters used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632",
    "prompt": "Extract all details about action dimensions used, how action_dim is configured, any mismatch between SmolVLA default and the target environment, and specific config parameters used."
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-13T09:51:02.669760+00:00_

Web search results for query: "LightVLA LIBERO results fine-tuning"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"LightVLA","url":"https://liauto-research.github.io/LightVLA/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"openvla/openvla-7b-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-10"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"LightVLA/LIBERO.md at main · LiAutoAD/LightVLA","url":"https://github.com/LiAutoAD/LightVLA/blob/main/LIBERO.md"},{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"}]

Based on the search results, here's what I found about LightVLA's fine-tuning results on the LIBERO benchmark:

## LightVLA Fine-Tuning Results on LIBERO

LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.6% improvement in task success rate on the LIBERO benchmark. More specifically, compared to OpenVLA-OFT, LightVLA not only reduces FLOPs and latency by 59.1% and 38.2%, but also improves success rate by 2.9%.

## Key Technical Achievements

LightVLA is a differentiable token pruning framework for 
…[truncated 899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-13T09:51:02.669907+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx",
  "prompt": "Extract all LoRA/PEFT parameters, training commands, quantization options, target modules, full fine-tuning vs LoRA differences for SmolVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx",
    "prompt": "Extract all LoRA/PEFT parameters, training commands, quantization options, target modules, full fine-tuning vs LoRA differences for SmolVLA"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-13T09:51:02.670040+00:00_

# LeRobot LIBERO Dataset Overview

## Dataset Summary
The **lerobot/libero** dataset is a robotics manipulation dataset containing **273,465 frames** from **1,693 episodes** across **40 tasks**, collected using a Franka Panda robot.

## Dataset Structure

### Core Metadata
- **Total Episodes**: 1,693
- **Total Frames**: 273,465
- **Total Tasks**: 40
- **FPS**: 10.0
- **Split**: train (all 1,693 episodes)
- **Format**: Parquet
- **Size**: ~1.94 GB

### Features & Columns

| Feature | Data Type | Shape | Description |
|---------|-----------|-------|-------------|
| `observation.images.image` | video | [256, 256, 3] | RGB camera feed (codec: av1) |
| `observation.images.image2` | video | [256, 256, 3] | Second RGB camera feed |
| `observation.state` | float32 | [8] | Robot state vector (8D) |
| `action` | float32 | [7] | Robot action vector (7D) |
| `timestamp` | float32 | [1] | Frame timestamp |
| `frame_index` | int64 | [1] | Frame index within episode |
| `episode_index` | int64 | [1] | Episode ID (0-1,692) |
| `task_index` | int64 | [1] | Task ID (0-39) |
| `index` | int64 | [1] | Global row index |

### Observation Keys
- **observation.state**: 8-dimensional state vector (likely joint positions/angles)
- **observation.images.image**: 256×256 RGB video stream
- **observation.images.image2**: Second 256×256 RGB camera view

### Action Dimensions
- **action**: 7-dimensional action vector (consistent with 7-DOF Franka Panda arm)

## Data Format Example
```
Row with observation.state:
[-0.053, 0.007, 0.678, 3.140, 0.001, -0.089, 0.038, -0.038]

Corresponding action:
[0.016, 0, 0, 0, 0, 0, -1]
```

## How to Load

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("lerobot/libero")

# Access training split
train_split = dataset["train"]

# View sample
sample = train_split[0]
print(sample.keys())
# dict_keys(['observation.state', 'action', 'timestamp', 
#            'frame_index', 'episode_index', 'index', 'task_index',
#            'o
…[truncated 485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-13T09:51:02.670193+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/",
  "prompt": "Extract: training commands, action_dim, config parameters, data format, fine-tuning steps for SmolVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/",
    "prompt": "Extract: training commands, action_dim, config parameters, data format, fine-tuning steps for SmolVLA"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-13T09:51:02.670348+00:00_

Web search results for query: "RoboVLMs LIBERO benchmark VLA 2025"

Links: [{"title":"VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"}]

Based on the search results, here's what I found about RoboVLMs, LIBERO benchmark, and VLA in 2025:

## LIBERO Benchmark Overview

LIBERO has emerged as the dominant benchmark and is now the most widely adopted protocol for evaluating VLA models, with its standardized task suite and unified reporting metrics making it the de facto standard f
…[truncated 1392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-13T09:51:02.670499+00:00_

# LIBERO Action Space Technical Details

Based on the GitHub issue, the action space representation in LIBERO remains **ambiguous and contradictory**:

## Stated vs. Actual Representation

**Documentation claim:** Actions are in end-effector (EEF) space

**User observation:** State and action values have drastically different numerical ranges, suggesting they may use different representations

## Action Dimensions

The issue references a 7-DOF Panda arm with an expected action structure of:
- 6D end-effector pose (3D position + 3D orientation)
- 2D gripper control

However, the exact breakdown and whether orientation is represented as quaternions or axis-angles in the action vector remains unspecified in this content.

## Gripper Action

The gripper is described as a "2D" component, but specific details about how gripper actions are encoded or their control range are not provided.

## Core Problem

The issue highlights a fundamental inconsistency: state values appear to be in joint space (with values near π), while the inference pipeline constructs observations using EEF representations: `"obs['robot0_eef_pos']"` and `"obs['robot0_eef_quat']"`. This mismatch creates confusion about what delta-actions actually represent physically.

**No definitive technical specification is provided in this issue.**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-13T09:51:02.670644+00:00_

# Cosmos-Policy-LIBERO-Predict2-2B: Key Technical Details

## Model Architecture

**Architecture Type:** Diffusion transformer with latent video diffusion
- **Base Model:** Fine-tuned from [Cosmos-Predict2-2B-Video2World](https://huggingface.co/nvidia/Cosmos-Predict2-2B-Video2World)
- **Parameters:** 2B
- **Key Adaptation:** Actions, proprioceptive states, and values are encoded as latent frames and injected directly into the video model's latent diffusion sequence

## Fine-Tuning Method

**Single-stage fine-tuning** with no architectural modifications:
- **Training Steps:** 40,000 gradient steps
- **Batch Size:** 1,920 (global)
- **Hardware:** 64 H100 GPUs
- **Training Time:** ~48 hours
- **Optimization:** Full model fine-tuning (all weights updated)
- **Noise Distribution:** Hybrid log-normal-uniform (modified from base model)
- **Training Split:** 50/25/25 for policy/world model/value function objectives

## LIBERO Benchmark Results (Per Suite)

| Task Suite | Success Rate |
|------------|-------------|
| LIBERO-Spatial | 98.1% |
| LIBERO-Object | 100.0% |
| LIBERO-Goal | 98.2% |
| LIBERO-Long | 97.6% |
| **Average** | **98.5%** |

*Success rates averaged over 500 trials per suite (10 tasks × 50 episodes) across 3 random seeds (6,000 trials total)*

## Action Space Configuration

**Output:**
- **Action Chunk Size:** 16 timesteps
- **Action Dimensions:** 7-dimensional (6-DoF end-effector control + 1 gripper)
- **Denoising Steps:** 5 (configurable without retraining)
- **Noise Range:** σ_min = 4.0, σ_max = 80.0
- **Generation Mode:** Parallel (action, future state, and value generated simultaneously)

**Input:**
- Text: Natural language task description
- Images: 224×224 RGB from dual cameras (third-person + wrist-mounted)
- Proprioception: 9-dimensional state (2 gripper joints + 3 position + 4 quaternion)

## Training Dataset

**LIBERO-Cosmos-Policy:**
- 4 task suites (Spatial, Object, Goal, Long)
- 500 demonstrations per suite (50 demos × 10 tasks)
- Collection: 
…[truncated 164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-13T09:51:02.670799+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb",
  "prompt": "Extract all training commands, configuration, data format, step-by-step notebook content for SmolVLA training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb",
    "prompt": "Extract all training commands, configuration, data format, step-by-step notebook content for SmolVLA training"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-13T09:51:02.670933+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx",
  "prompt": "Extract full content: architecture, fine-tuning commands, config parameters, action dimensions, data requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx",
    "prompt": "Extract full content: architecture, fine-tuning commands, config parameters, action dimensions, data requirements"
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-13T09:51:02.671063+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero",
  "prompt": "Extract full dataset card: what task suites are included, number of episodes per suite, format details, how it differs from lerobot/libero, observation keys, and how to use it."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero",
    "prompt": "Extract full dataset card: what task suites are included, number of episodes per suite, format details, how it differs from lerobot/libero, observation keys, and how to use it."
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-13T09:51:02.671186+00:00_

# Action Dimensions and Configuration Details

## Action Vector Specification

The author's simulated Panda environment uses a **7-dimensional action vector**:

```
"action": {
    "dtype": "float32",
    "shape": [7],
    "names": ["dx", "dy", "dz", "droll", "dpitch", "dyaw", "grip"]
}
```

This represents six degrees of freedom for end-effector movement plus one gripper dimension.

## Critical Configuration Issues

**Statistics Mismatch:** The most significant problem identified was using incorrect normalization statistics. The author initially applied `stats.json` from the LIBERO dataset to their custom environment, causing severe action scaling errors. As noted: "Pointing my inference script at the `stats.json` file for my dataset dramatically reduced the erratic behavior of the arm by scaling the actions to the dimensions of my arm."

**Key Training Parameters:**
- Batch size: 64
- Learning rate: 1e-5
- Expert width multiplier: 0.5
- VLM layers: 0
- Action chunk size: 30 (3 seconds at 10Hz execution frequency)

## Environment-to-Training Distribution Misalignment

While both systems used Franka Emika Panda arms, significant visual differences existed: different arm coloring, background variations, and gripper visibility differences compared to LIBERO training data. The author successfully compensated through systematic data collection and proper statistics computation rather than architectural modifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-13T09:51:02.671330+00:00_

I cannot extract the requested training commands, configuration, data format, or notebook content because the provided web page content only shows a Google Colab sign-in page header and a link to a notebook.

The actual notebook content is not included in the material provided. To access the SmolVLA training details, you would need to:

1. Click the sign-in link and authenticate with your Google account
2. Open the full notebook at the GitHub repository path shown (huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb)
3. View the complete notebook cells containing the training instructions

I can only work with content that's directly provided to me. If you'd like me to analyze the SmolVLA training notebook, please share the actual notebook text or cells.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-13T09:51:02.671459+00:00_

# LoRA/PEFT Parameters for SmolVLA Training

## Key Parameters

**LoRA-specific settings:**
- `--peft.method_type=LORA`: Selects LoRA as the adaptation method
- `--peft.r=64`: Specifies the rank of the low-rank adapter matrices
- `--peft.lora_alpha=64`: Sets the scaling factor (scaling = lora_alpha / r)

**Target modules configuration:**
By default, the system focuses on "the `q_proj` and `v_proj` layers of the LM expert in SmolVLA" plus state and action projection matrices.

Custom targeting example:
```
--peft.target_modules='(model\.vlm_with_expert\.lm_expert\..*\.(down|gate|up)_proj|.*\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))'
```

## Training Command Example

```bash
lerobot-train \
 --policy.path=lerobot/smolvla_base \
 --policy.optimizer_lr=1e-3 \
 --policy.scheduler_decay_lr=1e-4 \
 --steps=100000 \
 --batch_size=32 \
 --peft.method_type=LORA \
 --peft.r=64 \
 --peft.lora_alpha=64
```

## Full Fine-Tuning vs LoRA

The document notes that "learning rate...can usually be scaled by a factor of 10 compared to the learning rate used for full fine-tuning." Additionally, you can specify layers for traditional fine-tuning using `--peft.full_training_modules=["state_proj"]`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-13T09:51:02.671594+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/README.md",
  "prompt": "Extract all details: how to convert LIBERO HDF5 to LeRobot format, what scripts to run, command syntax, observation keys mapped, dependencies required."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/README.md",
    "prompt": "Extract all details: how to convert LIBERO HDF5 to LeRobot format, what scripts to run, command syntax, observation keys mapped, dependencies required."
  }
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-13T09:51:02.671719+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645v1",
  "prompt": "Extract detailed results tables: per-suite success rates for OpenVLA-OFT and all baselines on LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long/10. Also extract training hyperparameters: learning rate, batch size, gradient steps, GPU hardware, training time, LoRA rank, action space details (dimensions, chunk size, tokenization method)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.19645v1",
    "prompt": "Extract detailed results tables: per-suite success rates for OpenVLA-OFT and all baselines on LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long/10. Also extract training hyperparameters: learning rate, batch size, gradient steps, GPU hardware, training time, LoRA rank, action space details (dimensions, chunk size, tokenization method)."
  }
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-13T09:51:02.671846+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/physical-intelligence/libero",
  "prompt": "Extract the full dataset card: what suites are included, data format, how it was converted to LeRobot format, features/columns, number of episodes, and how to load it."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/physical-intelligence/libero",
    "prompt": "Extract the full dataset card: what suites are included, data format, how it was converted to LeRobot format, features/columns, number of episodes, and how to load it."
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-13T09:51:02.671969+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://liauto-research.github.io/LightVLA/",
  "prompt": "Extract: model architecture, LIBERO per-suite success rates, training details, fine-tuning method, action space, comparison with baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://liauto-research.github.io/LightVLA/",
    "prompt": "Extract: model architecture, LIBERO per-suite success rates, training details, fine-tuning method, action space, comparison with baselines"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-13T09:51:02.672161+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/libero",
  "prompt": "Extract the action space specification: how many dimensions, what each dimension represents, control mode (relative/absolute), and any configuration parameters for SmolVLA fine-tuning on LIBERO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/libero",
    "prompt": "Extract the action space specification: how many dimensions, what each dimension represents, control mode (relative/absolute), and any configuration parameters for SmolVLA fine-tuning on LIBERO."
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-13T09:51:02.672379+00:00_

# LIBERO

LIBERO is a benchmark designed to study **lifelong robot learning** — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once. It provides a set of standardized manipulation tasks that focus on **knowledge transfer**: how well a robot can apply what it has already learned to new situations. By evaluating on LIBERO, different algorithms can be compared fairly and researchers can build on each other's work.

- Paper: [Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)
- GitHub: [Lifelong-Robot-Learning/LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
- Project website: [libero-project.github.io](https://libero-project.github.io)

![An overview of the LIBERO benchmark](https://libero-project.github.io/assets/img/libero/fig1.png)

## Available tasks

LIBERO includes **five task suites** covering **130 tasks**, ranging from simple object manipulations to complex multi-step scenarios:

| Suite          | CLI name         | Tasks | Description                                        |
| -------------- | ---------------- | ----- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | Long-horizon tasks from the LIBERO-100 collection  |

## Installation

After following the LeRobot installation instructions:

```bash
pip install -e ".[libero]"
```

LIBERO requires Linux (`sys_platform == 'linux'`). LeRobot uses MuJoCo for simulation — set the rendering backend before training or evaluation:

```bash
export MUJOCO_GL=egl  # fo
…[truncated 4883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-13T09:51:02.672561+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "Extract the results table comparing different VLA models on standard LIBERO benchmark: model names, per-suite success rates (Spatial, Object, Goal, Long), and any training details mentioned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2510.13626v1",
    "prompt": "Extract the results table comparing different VLA models on standard LIBERO benchmark: model names, per-suite success rates (Spatial, Object, Goal, Long), and any training details mentioned"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-13T09:51:02.672695+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SpatialVLA LIBERO fine-tune 2025 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SpatialVLA LIBERO fine-tune 2025 results"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-13T09:51:02.672820+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/2259",
  "prompt": "Get the full content of this GitHub issue about fine-tuning SmolVLA on different environments and embodiments. Extract all technical discussion about action dimensions, action_dim parameter, 6D vs 7D, and any official HuggingFace responses about configuration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/issues/2259",
    "prompt": "Get the full content of this GitHub issue about fine-tuning SmolVLA on different environments and embodiments. Extract all technical discussion about action dimensions, action_dim parameter, 6D vs 7D, and any official HuggingFace responses about configuration."
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-13T09:51:02.672945+00:00_

# SmolVLA Fine-tuning: Key Parameters and Commands

## Training Commands

**Smoke Test (1,000 steps):**
```bash
docker run --rm --gpus all --shm-size 16g \
  -v /path/to/lerobot_dataset:/data/input \
  -v /path/to/output:/outputs \
  ioaitech/lerobot-gpu:v0.5.0 \
  bash -lc 'lerobot-train \
    --policy.path=lerobot/smolvla_base \
    --dataset.repo_id=local/my_dataset \
    --dataset.root=/data/input \
    --batch_size=8 \
    --steps=1000 \
    --output_dir=/outputs/smolvla_smoke \
    --job_name=smolvla_smoke \
    --policy.device=cuda \
    --wandb.enable=false'
```

**Full Fine-tuning (20,000 steps):**
The base command uses `batch_size=64`, `steps=20000`, and requires approximately 4 hours on a single A100 GPU.

## Critical Configuration Parameters

| Parameter | Recommended Value | Notes |
|-----------|-------------------|-------|
| `--policy.path` | `lerobot/smolvla_base` | Official pretrained checkpoint |
| `--batch_size` | 64 | Start smaller for VRAM constraints |
| `--steps` | 20,000 | Baseline; begin with 1k smoke test |
| `--policy.device` | `cuda` | Use NVIDIA GPU; CPU for testing only |
| `--wandb.enable` | false | Disable for local quick tests |

## Data Format Requirements

- **Format Version:** v3.0 (use `ioaitech/lerobot-gpu:v0.5.0`)
- **Minimum Episodes:** "~50 high-quality episodes with repeated coverage per variation"
- **Fixed Shapes:** `observation.state` and `action` dimensions must remain consistent
- **Inputs:** Multi-view images, robot state, optional language, continuous actions

## Action Dimensions

The documentation does not explicitly specify `action_dim`; this parameter derives from your dataset's action space structure and remains task-dependent.

## Pre-training Requirements

"At minimum verify: Image keys are consistent across episodes" and validate task text alignment with physical objectives.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-13T09:51:02.673081+00:00_

# SmolVLA: Architecture, Fine-tuning, and Configuration

## Architecture Overview

SmolVLA is Hugging Face's lightweight robotics foundation model. The system accepts "(i) multiple cameras views, (ii) the robot's current sensorimotor state, and (iii) a natural language instruction" to generate action sequences. It processes these inputs into contextual features that condition an action expert module.

## Model Specifications

- **Base Model**: `smolvla_base` (450M parameters)
- **Training Time**: Approximately 4 hours on single A100 GPU for 20k steps
- **Fine-tuning Framework**: LeRobot with HuggingFace Hub integration

## Data Requirements

The documentation emphasizes that "data quality and quantity is definitely a key":

- **Minimum dataset**: ~50 episodes recommended as a starting point
- **Structure**: Multiple demonstrations per task variation (e.g., 10 episodes across 5 distinct cube positions = 50 total)
- **Caution**: Testing with only 25 episodes "was not enough leading to a bad performance"

## Fine-tuning Command Example

```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=${HF_USER}/mydataset \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --policy.device=cuda \
  --wandb.enable=true
```

## Configuration Parameters

- **Batch Size**: Recommended starting small and increasing incrementally
- **Training Steps**: 20,000 steps as default (tunable based on performance)
- **Device**: CUDA GPU support; Colab notebook available for CPU-limited users
- **Output Directory**: Customizable model save location

## Inference Command Structure

Evaluation uses `lerobot-record` with robot type, camera configuration, task descriptions, and fine-tuned model paths specified via command-line arguments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-13T09:51:02.673211+00:00_

# LightVLA: Extracted Information

Based on the provided content, here's what is available:

## Available Information

**Core Innovation:**
"Adaptive, performance-driven pruning of visual tokens" using "dynamic queries to evaluate visual token importance, and adopts Gumbel softmax to enable differentiable token selection."

**Performance Metrics:**
- 59.1% FLOPs reduction
- 38.2% latency reduction
- 2.6% task success rate improvement on LIBERO benchmark

## Information Not Provided

The webpage does not contain detailed specifications for:

- **Model Architecture Details**: Specific layer configurations, attention mechanisms, or network diagrams beyond the framework overview image
- **LIBERO Per-Suite Success Rates**: Only aggregate results mentioned; individual suite breakdowns unavailable
- **Training Details**: Hyperparameters, epochs, batch sizes, or optimization settings not specified
- **Fine-tuning Method**: Only that the model "learns to preserve the most informative visual tokens" through fine-tuning; specific procedures absent
- **Action Space**: Dimension or structure of robot actions not described
- **Baseline Comparisons**: The page mentions "superior efficiency and accuracy compared to existing VLA models" but provides no detailed comparative tables or results

**Note:** For complete technical specifications, the authors direct readers to the arXiv paper (2509.12594), GitHub repository, and Hugging Face model cards, which likely contain these omitted details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-13T09:51:02.673377+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/huggingface/notebooks/main/lerobot/training-smolvla.ipynb",
  "prompt": "Extract all training commands, configuration parameters, code cells, data format, action_dim details from this SmolVLA training notebook"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/huggingface/notebooks/main/lerobot/training-smolvla.ipynb",
    "prompt": "Extract all training commands, configuration parameters, code cells, data format, action_dim details from this SmolVLA training notebook"
  }
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-13T09:51:02.673511+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://learnopencv.com/smolvla-lerobot-vision-language-action-model/",
  "prompt": "Extract: architecture details, action_dim, observation space, training commands, config parameters, data format, fine-tuning steps for SmolVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://learnopencv.com/smolvla-lerobot-vision-language-action-model/",
    "prompt": "Extract: architecture details, action_dim, observation space, training commands, config parameters, data format, fine-tuning steps for SmolVLA"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-13T09:51:02.673633+00:00_

# GitHub Issue Summary: SmolVLA Fine-tuning Configuration Questions

## Key Technical Questions Raised

The issue author (@RonPlusSign) is attempting to fine-tune SmolVLA and π₀ models on RLBench using a Franka Emika Panda (7DoF + gripper) but encounters 0% evaluation success despite successful training loss convergence.

## Primary Technical Concerns

**Action/State Space Specifications:**
The author requests clarification on exact representations used during pretraining, asking whether SmolVLA uses "ΔEEF pose, absolute EEF pose, joint positions, joint velocities" and angle formats (quaternion vs. Euler).

**Camera Input Handling:**
Questions whether camera naming conventions matter and if using different camera configurations from the pretrained model would waste the pretraining effort.

**Model Selection Uncertainty:**
The author notes that `HuggingFaceVLA/smolvla_libero` appears to use 6DoF+gripper, which doesn't match their 7DoF setup, creating ambiguity about embodiment compatibility.

**Action Dimension Mystery:**
In the `HuggingFaceVLA/smol-libero` dataset, actions have dimension 7, but the mapping is unclear: "doesn't clearly map to 7 joint angles + gripper."

## Status

The issue remains open and assigned to @fracapuano. No official responses appear in the provided content, meaning the technical specifications for these models lack public documentation at this point.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-13T09:51:02.673775+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/lerobot-dataset-v3",
  "prompt": "Extract: data format spec, action/observation field names, required JSON structure, how to create a custom LeRobotDataset for fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/lerobot-dataset-v3",
    "prompt": "Extract: data format spec, action/observation field names, required JSON structure, how to create a custom LeRobotDataset for fine-tuning"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-13T09:51:02.673930+00:00_

# LeRobotDataset v3.0

`LeRobotDataset v3.0` is a standardized format for robot learning data. It provides unified access to multi-modal time-series data, sensorimotor signals and multi‑camera video, as well as rich metadata for indexing, search, and visualization on the Hugging Face Hub.

This docs will guide you to:

- Understand the v3.0 design and directory layout
- Record a dataset and push it to the Hub
- Load datasets for training with `LeRobotDataset`
- Stream datasets without downloading using `StreamingLeRobotDataset`
- Apply image transforms for data augmentation during training
- Migrate existing `v2.1` datasets to `v3.0`

## What’s new in `v3`

- **File-based storage**: Many episodes per Parquet/MP4 file (v2 used one file per episode).
- **Relational metadata**: Episode boundaries and lookups are resolved through metadata, not filenames.
- **Hub-native streaming**: Consume datasets directly from the Hub with `StreamingLeRobotDataset`.
- **Lower file-system pressure**: Fewer, larger files ⇒ faster initialization and fewer issues at scale.
- **Unified organization**: Clean directory layout with consistent path templates across data and videos.

## Installation

`LeRobotDataset v3.0` will be included in `lerobot >= 0.4.0`.

Until that stable release, you can use the main branch by following the [build from source instructions](./installation#from-source).

## Record a dataset

Run the command below to record a dataset with the SO-101 and push to the Hub:

```bash
lerobot-record \
  --robot.type=so101_follower \
  --robot.port=/dev/tty.usbmodem585A0076841 \
  --robot.id=my_awesome_follower_arm \
  --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 1920, height: 1080, fps: 30}}" \
  --teleop.type=so101_leader \
  --teleop.port=/dev/tty.usbmodem58760431551 \
  --teleop.id=my_awesome_leader_arm \
  --display_data=true \
  --dataset.repo_id=${HF_USER}/record-test \
  --dataset.num_episodes=5 \
  --dataset.single_task="Grab the black cube" \
  --d
…[truncated 10119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-13T09:51:02.674089+00:00_

Web search results for query: "SpatialVLA LIBERO fine-tune 2025 results"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"IPEC-COMMUNITY/spatialvla-4b-224-pt · Hugging Face","url":"https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models","url":"https://arxiv.org/html/2501.15830v2"},{"title":"VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting","url":"https://arxiv.org/html/2507.05116v3"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"}]

Based on the search results, here are the key findings about SpatialVLA's LIBERO fine-tuning results from 2025:

## SpatialVLA LIBERO Fine-Tuning Results

Fine-tuned SpatialVLA models achieve the highest average success rate and ranking, followed by fine-tuned OpenVLA and Octo across LIBERO benchmarks.

### Specific Performance Improvements

When fine-tuning on LIBERO small dataset tasks, initializing the feature grid with the new distribution boosts model performance by +4.6%, 
…[truncated 895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-13T09:51:02.674236+00:00_

# VLA Models Performance on LIBERO Benchmark

The paper presents extensive evaluation of 10 VLA models, but **does not include a single comprehensive table showing per-suite success rates** (Spatial, Object, Goal, Long) for all models on the standard LIBERO benchmark.

Instead, the main results appear in **Table 1**, which focuses on robustness across perturbation dimensions rather than standard benchmark performance. This table shows:

## Models Evaluated
- OpenVLA and variants (OpenVLA-OFT, OpenVLA-OFT_w, OpenVLA-OFT_m)
- π0, π0-fast
- Nora, WorldVLA, UniVLA
- RIPT-VLA

## Key Finding from Table 1
The "Original" column shows baseline performance on unperturbed tasks, ranging from 76.5% (OpenVLA) to 97.6% (OpenVLA-OFT_m). However, these represent overall success rates, not disaggregated by suite.

## Training Details Mentioned
- Models were "pre-trained on the Open X-Embodiment dataset" with 970k+ trajectories
- Fine-tuning used "150K steps using 8×A100 GPUs"
- The paper emphasizes that "high benchmark scores often conceal critical deficiencies" rather than providing detailed per-suite breakdowns

**Note:** The research prioritizes robustness analysis over standard benchmark reporting, reflecting the paper's core message about evaluating "reliability under realistic variation."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-13T09:51:02.674402+00:00_

# LIBERO Dataset Card Summary

## Overview
The **LIBERO** dataset is a robotics dataset from Hugging Face Vision Language Action Models research, designed for training vision-language-action (VLA) models for robotic manipulation tasks.

## Dataset Specifications

### Size & Structure
- **Total rows**: 273,000 (in default split)
- **Size category**: 100K - 1M
- **Format**: Parquet (auto-converted)
- **Split**: Single `train` split with 273k rows
- **Episodes**: 148 total episodes
- **Task suites**: 10 different task types

### Task Categories
The dataset includes **10 task indices** (0-9), representing different manipulation tasks within the LIBERO benchmark suite.

### Modalities
- **Image**: Dual RGB observations (256×256 px each)
  - `observation.images.image` 
  - `observation.images.image2`
- **Time-series**: State vectors and action sequences

## Data Schema

### Observation Keys
```
- observation.images.image (256×256 image)
- observation.images.image2 (256×256 image)
- observation.state (list of 8 floats - proprioceptive state)
```

### Action Format
```
- action (list of 7 floats - 6D pose + gripper command)
  Format: [x, y, z, rx, ry, rz, gripper]
```

### Metadata Fields
```
- timestamp (float32): Elapsed time in episode
- frame_index (int64): Frame number within episode (0-454 max)
- episode_index (int64): Episode identifier (0-147)
- task_index (int64): Task suite (0-9)
- index (int64): Global row index
```

## Key Features

### Dual Camera Setup
The dataset provides two synchronized camera views per timestep, enabling multi-view learning:
```python
# Access both camera perspectives
observation = {
    'images': {
        'image': camera1_view,      # 256×256 RGB
        'image2': camera2_view      # 256×256 RGB
    },
    'state': proprioceptive_data    # 8D state vector
}
```

### Sequential Episode Structure
- Episodes range from ~45-454 frames
- Each frame includes timestamped observations and corresponding actions
- Enables learning temporal dynamic
…[truncated 1582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-13T09:51:02.674556+00:00_

# LIBERO Dataset Card

## Overview
The **LIBERO** dataset is a robotics manipulation dataset hosted on Hugging Face that contains demonstrations of robotic tasks performed with a Panda robot arm. It's designed for imitation learning and robot learning research.

## Dataset Specifications

### Suites Included
The dataset contains tasks from the LIBERO benchmark, which includes manipulation tasks for robot learning evaluation.

### Data Format
- **Format**: Parquet (auto-converted from original format)
- **Size**: 100K - 1M range
- **Total Rows**: 273,000 (in default subset)
- **Modalities**: Image and Time-series data

### Structure

#### Splits
- **train**: 273,000 rows

#### Features/Columns
The dataset includes the following fields per frame:

| Column | Type | Description |
|--------|------|-------------|
| `image` | Image (256×256px) | Primary camera view |
| `wrist_image` | Image (256×256px) | Wrist-mounted camera view |
| `state` | List | Robot state vector (8 values) |
| `actions` | List | Action vector (7 values) |
| `timestamp` | float32 | Frame timestamp |
| `frame_index` | int64 | Frame number within episode |
| `episode_index` | int64 | Episode identifier |
| `task_index` | int64 | Task identifier (0-9) |
| `index` | int64 | Global sample index |

### Episodes & Tasks
- **Total Episodes**: 147
- **Tasks**: 10 different manipulation tasks
- **Frames per Episode**: Up to 454 frames

### Loading the Dataset

```python
from datasets import load_dataset

# Load the default subset
dataset = load_dataset("physical-intelligence/libero")

# Access training data
train_data = dataset['train']

# Access a single sample
sample = train_data[0]
print(sample.keys())
# Output: dict_keys(['image', 'wrist_image', 'state', 'actions', 'timestamp', 
#                     'frame_index', 'episode_index', 'task_index', 'index'])
```

### State and Action Specifications

**State Vector** (8 values): Robot joint positions and gripper state
```
[-0.053, 0.007, 0.678, 3.141, 0.002, 
…[truncated 1207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-13T09:51:02.674696+00:00_

# SmolVLA Training Notebook Extraction

## Main Training Command

```bash
python lerobot/scripts/train.py \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=${HF_USER}/mydataset \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --job_name=my_smolvla_training \
  --policy.device=cuda \
  --wandb.enable=true
```

## Key Configuration Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `--policy.path` | `lerobot/smolvla_base` | Model architecture selection |
| `--batch_size` | 64 | Samples processed per gradient update |
| `--steps` | 20000 | Total training iterations |
| `--policy.device` | cuda/mps/cpu | Hardware target (GPU/Apple Silicon/CPU) |
| `--wandb.enable` | true | Experiment tracking toggle |

## Installation Code Cells

1. **Conda bootstrap**: `pip install -q condacolab` + `condacolab.install()`
2. **LeRobot setup**: Clone repository, install FFmpeg 7.1.1, editable pip install
3. **SmolVLA dependencies**: `pip install -e ".[smolvla]"`

## Key Details

- **Expected training duration**: "about 5 hours on an NVIDIA A100" GPU
- **Dataset location**: Hugging Face Hub repository (format: `USERNAME/DATASET`)
- **Output artifacts**: Model checkpoints, logs, training plots saved to `--output_dir`
- **Action_dim**: Not explicitly specified in notebook
- **Data format**: Unspecified; requires dataset repo containing training data

## Post-Training Steps

Model checkpoint upload to Hugging Face Hub via `huggingface-cli upload` command after authentication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-13T09:51:02.674836+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero",
  "prompt": "Extract the model card details, including action space, action dimensions, what each action dimension represents, training configuration, and any notes about LIBERO action space compatibility."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero",
    "prompt": "Extract the model card details, including action space, action dimensions, what each action dimension represents, training configuration, and any notes about LIBERO action space compatibility."
  }
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-13T09:51:02.674973+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero",
  "prompt": "Extract all feature/schema details about the dataset, especially action dimensions, what each action dimension is named, state dimensions, and any notes about the action representation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero",
    "prompt": "Extract all feature/schema details about the dataset, especially action dimensions, what each action dimension is named, state dimensions, and any notes about the action representation."
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-13T09:51:02.675110+00:00_

# LIBERO to LeRobot Conversion Guide

## Overview
This conversion process transforms LIBERO HDF5 datasets into LeRobot format, incorporating improvements like enhanced resolution, action filtration, and robust error recovery.

## Key Dependencies
- LeRobot (official installation required)
- h5py
- datatrove with ray support for parallel processing
- LIBERO libraries (for trajectory regeneration)

## Conversion Workflow

### Step 1: Regenerate LIBERO Trajectories
Before conversion, preprocess the source data:
```bash
python libero_utils/regenerate_libero_dataset.py \
    --resolution 256 \
    --libero_task_suite libero_90 \
    --libero_raw_data_dir /path/to/libero/datasets/libero_90 \
    --libero_target_dir /path/to/libero/datasets/libero_90_no_noops
```

This step implements "resolution enhancement, No-op action filtration, 180° RGB frame rotation, Failed trajectory filtering."

### Step 2: Main Conversion Script
```bash
python libero_h5.py \
    --src-paths /path/to/libero/ \
    --output-path /path/to/local \
    --executor local \
    --tasks-per-job 3 \
    --workers 10
```

**Key Parameters:**
- `--src-paths`: Supports multiple dataset paths for merging
- `--executor`: Use "local" or "ray" (ray recommended for speed)
- `--tasks-per-job` and `--workers`: Adjust based on available resources
- `--resume-from-save` and `--resume-from-aggregate`: Resume interrupted conversions

## Observation Keys in Output

The converted dataset includes:
- **Image data**: `observation.images.image` (256×256×3 RGB, AV1 codec)
- **State data**: `observation.state` (8-dimensional float32)
- **Action data**: Shape [7] float32 for motor control

Native LIBERO state information is preserved via `states.ee_state` and `states.joint_state`.

## Multi-Node Processing Options

For distributed conversion:
- **Direct ray cluster**: Start head node, connect workers, execute script
- **SLURM integration**: Use provided batch script template for cluster management
- **Community managers**: Ray
…[truncated 191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-13T09:51:02.675261+00:00_

# OpenVLA-OFT: Detailed Results and Training Parameters

## LIBERO Success Rates by Task Suite

### Table I - Task Performance Comparisons

**Single Input Configuration** (third-person image + language):
| Method | Spatial | Object | Goal | Long | Average |
|--------|---------|--------|------|------|---------|
| OpenVLA (baseline) | 84.7% | 88.4% | 79.2% | 53.7% | 76.5% |
| OpenVLA + PD&AC | 91.3% | 92.7% | 90.5% | 86.5% | 90.2% |
| OpenVLA + PD&AC, Cont-L1 | 96.2% | 98.3% | 96.2% | 90.7% | 95.3% |
| OpenVLA + PD&AC, Cont-Diffusion | 96.9% | 98.1% | 95.5% | 91.1% | 95.4% |

**Multi-Input Configuration** (third-person + wrist camera + proprioceptive state):
| Method | Spatial | Object | Goal | Long | Average |
|--------|---------|--------|------|------|---------|
| π0 (fine-tuned) | 96.8% | 98.8% | 95.8% | 85.2% | 94.2% |
| **OpenVLA-OFT** | 97.6% | 98.4% | 97.9% | 94.5% | **97.1%** |

The paper states that OpenVLA-OFT achieves "state-of-the-art 97.1% average success rate" across the four LIBERO task suites, representing a substantial improvement from the baseline 76.5%.

## Training Hyperparameters for LIBERO

### Core Training Configuration

**Hardware & Compute:**
- GPU infrastructure: 8 A100/H100 GPUs
- Total batch size: 64-128 across distributed setup
- Training framework: PyTorch

**Optimization Details:**
- Learning rate: 5e-4 (initial), decayed to 5e-5 after 100K steps
- Gradient steps: 50-150K for non-diffusion methods; 100-250K for diffusion variants
- Convergence criterion: Training until mean L1 loss < 0.01 between predicted and normalized actions
- Evaluation cadence: Checkpoints evaluated every 50K steps; best performance reported

**Parameter-Efficient Fine-Tuning:**
- Technique: LoRA (Low-Rank Adaptation) employed due to smaller fine-tuning datasets (approximately 500 demonstrations versus 1M pretraining examples)

### Action Space Specifications

**Action Dimensions & Representation:**
- Original OpenVLA: 7 discrete action tokens per timestep (3 posi
…[truncated 2417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-13T09:51:02.675432+00:00_

# SmolVLA LIBERO Model Card Details

Based on the provided web page content, here's what I can extract:

## Available Information

**Model Name:** smolvla_libero
- **License:** apache-2.0
- **Base Model:** lerobot/smolvla_base
- **Framework:** LeRobot
- **Paper:** arxiv: 2506.01844 (SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics)

## Model Overview

SmolVLA is described as:
- A compact, efficient vision-language-action model
- Achieves competitive performance at reduced computational costs
- Deployable on consumer-grade hardware
- Trained and pushed to the Hub using LeRobot

## Usage Examples

**Training:**
```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/&lt;dataset> \
  --policy.type=act \
  --output_dir=outputs/train/&lt;desired_policy_repo_id> \
  --job_name=lerobot_training \
  --policy.device=cuda \
  --policy.repo_id=${HF_USER}/&lt;desired_policy_repo_id> \
  --wandb.enable=true
```

**Inference/Evaluation:**
```bash
lerobot-record \
  --robot.type=so100_follower \
  --dataset.repo_id=&lt;hf_user>/eval_&lt;dataset> \
  --policy.path=&lt;hf_user>/&lt;desired_policy_repo_id> \
  --episodes=10
```

## Missing Details

The provided web page content **does not include**:
- Specific action space definition
- Action dimensions
- Individual action dimension descriptions
- Detailed LIBERO action space compatibility notes
- Training configuration specifics

For complete technical details, refer to the [full model card](https://huggingface.co/HuggingFaceVLA/smolvla_libero) or the [SmolVLA paper](https://huggingface.co/papers/2506.01844).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-13T09:51:02.675568+00:00_

# SmolVLA Architecture and Configuration Details

## Architecture Overview

SmolVLA is a "~450M parameter" Vision-Language-Action model combining three key components:

1. **Vision-Language Backbone**: Uses SmolVLM-2 with SigLIP for visual encoding and SmolLM2 for language processing
2. **Visual Processing**: Employs global image processing (512×512 pixels) with PixelShuffle to reduce visual tokens to approximately 64 per frame
3. **Action Expert**: Flow-matching module that converts processed perceptions into robot actions

## Key Architectural Innovations

- **Layer Skipping**: Features extracted from intermediate VLM layers (around N=L/2) rather than the final layer, reducing computational overhead during inference
- **Linear Projectors**: Serve as dimensional adapters between different modules
- **Asynchronous Inference**: Enables parallel prediction of next actions before current ones complete, reducing latency

## Configuration Parameters

Core training settings from the codebase:

```
batch_size: 64
steps: 200,000
chunk_size: 50
num_vlm_layers: 16
optimizer: adamw (lr: 0.0001)
scheduler: cosine decay with warmup
num_learnable_params: ~100M (of 450M total)
```

## Observation and Action Space

**Input Features**:
- observation.image: [3, 256, 256]
- observation.image2: [3, 256, 256]
- observation.image3: [3, 256, 256]
- observation.state: [6] (robot joint positions)

**Output**:
- action: [6] dimensions (normalized)

## Training Configuration

The model uses "MEAN_STD normalization" for actions and state, with identity normalization for visual inputs. Gradient clipping is set to 10.0, and the training employs mixed precision disabled initially.

## Fine-Tuning Command

```bash
python lerobot/scripts/train.py \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=lerobot/svla_so100_stacking \
  --batch_size=64 \
  --steps=200000
```

## Dataset Format

Training uses the `lerobot/svla_so100_stacking` repository containing 174 filtered episodes from SO-100/
…[truncated 256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-13T09:51:02.675719+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2501.15830v2",
  "prompt": "Extract: per-suite LIBERO success rates table (Spatial, Object, Goal, Long) for SpatialVLA and all baselines, fine-tuning method (full vs LoRA), training hyperparameters, action space configuration, model architecture details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2501.15830v2",
    "prompt": "Extract: per-suite LIBERO success rates table (Spatial, Object, Goal, Long) for SpatialVLA and all baselines, fine-tuning method (full vs LoRA), training hyperparameters, action space configuration, model architecture details"
  }
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-13T09:51:02.675848+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "UniVLA LIBERO benchmark 2025 success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "UniVLA LIBERO benchmark 2025 success rate"
  }
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-13T09:51:02.675972+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Cosmos-Policy\" LIBERO NVIDIA VLA 2025 fine-tune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Cosmos-Policy\" LIBERO NVIDIA VLA 2025 fine-tune"
  }
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-13T09:51:02.676097+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/collections/IPEC-COMMUNITY/libero-benchmark-dataset",
  "prompt": "Extract all datasets in this collection, their names, task suites covered (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-90, LIBERO-Long), format details, and how to use them."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/collections/IPEC-COMMUNITY/libero-benchmark-dataset",
    "prompt": "Extract all datasets in this collection, their names, task suites covered (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-90, LIBERO-Long), format details, and how to use them."
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-13T09:51:02.676278+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/blog/lerobot-release-v040",
  "prompt": "Extract all details about LIBERO integration in LeRobot v0.4.0: what was added, dataset details, conversion process, training configs, and any new features related to LIBERO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/blog/lerobot-release-v040",
    "prompt": "Extract all details about LIBERO integration in LeRobot v0.4.0: what was added, dataset details, conversion process, training configs, and any new features related to LIBERO."
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-13T09:51:02.676417+00:00_

# LIBERO Dataset - Feature/Schema Details

## Overview
The LIBERO dataset is a robotics dataset containing 273k rows of demonstration data with observations, states, and actions from robotic manipulation tasks.

## Key Schema Details

### Observation Structure
- **observation.images.image**: RGB image (256x256 pixels)
- **observation.images.image2**: Second RGB image view (256x256 pixels)
- **observation.state**: List of 8 floating-point values representing robot state

### State Dimensions
The `observation.state` contains **8 values** (float32), which typically represent:
- Joint positions or end-effector pose components (6-7 DoF for a robotic arm)
- Gripper state

Example state vector:
```
[-0.053, 0.007, 0.678, 3.140, 0.001, -0.089, 0.038, -0.038]
```

### Action Dimensions
The `action` field contains **7 values** (list of floats), structured as:

```
[dx, dy, dz, droll, dpitch, dyaw, gripper]
```

**Action Components:**
1. **dx**: X-axis delta movement (translation)
2. **dy**: Y-axis delta movement (translation)
3. **dz**: Z-axis delta movement (translation)
4. **droll**: Rotation around X-axis (delta)
5. **dpitch**: Rotation around Y-axis (delta)
6. **dyaw**: Rotation around Z-axis (delta)
7. **gripper**: Gripper command (-1 for close/open, or continuous values)

### Example Action Sequences
```
[0.016, 0, 0, 0, 0, 0, -1]           # Gripper close
[-0.053, -0.085, 0.489, 0, 0, 0, 1]  # Gripper open with motion
[0.238, -0.326, 0.618, 0, 0, 0, 1]   # Motion with gripper open
```

## Additional Metadata

### Per-Sample Fields
- **timestamp**: float32 (0-45.4 range) - timing information
- **frame_index**: int64 (0-454) - frame number within episode
- **episode_index**: int64 (0-147) - episode identifier
- **task_index**: int64 (0-9) - task/subtask identifier
- **index**: int64 - global sample index

### Dataset Statistics
- **Size**: 100K - 1M range (273k rows in train split)
- **Format**: Parquet
- **Tasks**: 10 different tasks (task_index: 0-9)
- **Episodes**: 14
…[truncated 712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-13T09:51:02.676573+00:00_

Web search results for query: "UniVLA LIBERO benchmark 2025 success rate"

Links: [{"title":"[2506.19850] Unified Vision-Language-Action Model","url":"https://arxiv.org/abs/2506.19850"},{"title":"Unified Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=PklMD8PwUy"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - OpenDriveLab/UniVLA: [RSS 2025] Learning to Act Anywhere with Task-centric Latent Actions · GitHub","url":"https://github.com/OpenDriveLab/UniVLA"},{"title":"Learning to Act Anywhere with Task-centric Latent Actions","url":"https://arxiv.org/pdf/2505.06111"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Success rates of OpenVLA, pi0, pi0.5, and univla under object position... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rates-of-OpenVLA-pi0-pi05-and-univla-under-object-position-perturbations_fig1_396249917"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Robotics Advances With Unified Vision, Language And Action Learning.","url":"https://quantumzeitgeist.com/robotics-advances-with-unified-vision-language-and-action-learning/"}]

Based on the search results, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%. This represents state-of-the-art performance on the LIBERO benchmark as of 2025.

However, it's worth noting that despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications, suggesting that these headline numbers should be interpreted with caution regarding real-world robustne
…[truncated 106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-13T09:51:02.676711+00:00_

# Libero Benchmark Dataset Collection

## Datasets in Collection

The **IPEC-COMMUNITY/Libero Benchmark Dataset** collection contains 5 datasets:

| Dataset Name | Task Suite | Size | Downloads | Updated |
|---|---|---|---|---|
| `libero_spatial_no_noops_1.0.0_lerobot` | LIBERO-Spatial | 53k | 9.44k | Nov 3, 2025 |
| `libero_goal_no_noops_1.0.0_lerobot` | LIBERO-Goal | 52k | 7.76k | Nov 3, 2025 |
| `libero_object_no_noops_1.0.0_lerobot` | LIBERO-Object | 67k | 7.74k | Nov 3, 2025 |
| `libero_10_no_noops_1.0.0_lerobot` | LIBERO-10 | 101k | 8.65k | Nov 3, 2025 |
| `libero_90_no_noops_lerobot` | LIBERO-90 | 569k | 2.39k | Jul 1, 2025 |

## Task Suites Covered

- **LIBERO-Spatial**: Spatial reasoning tasks (52k samples)
- **LIBERO-Goal**: Goal-conditioned tasks (52k samples)
- **LIBERO-Object**: Object manipulation tasks (67k samples)
- **LIBERO-10**: 10-task benchmark (101k samples)
- **LIBERO-90**: 90-task benchmark (569k samples)

## Format Details

All datasets are in **LeRobot format** (denoted by `_lerobot` suffix) and have **no-ops removed** (`_no_noops`), optimized for efficient training.

## How to Use

Access datasets via Hugging Face Datasets library:

```python
from datasets import load_dataset

# Example: Load LIBERO-Spatial dataset
dataset = load_dataset("IPEC-COMMUNITY/libero_spatial_no_noops_1.0.0_lerobot")

# Example: Load LIBERO-90 (largest benchmark)
dataset = load_dataset("IPEC-COMMUNITY/libero_90_no_noops_lerobot")
```

**View & Explore**: Use the Viewer option on each dataset's Hugging Face page for interactive exploration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-13T09:51:02.676840+00:00_

# LIBERO Integration in LeRobot v0.4.0

## What Was Added

LeRobot v0.4.0 officially integrated support for **LIBERO**, one of the largest open benchmarks for Vision-Language-Action (VLA) policies. This is positioned as a major step toward building an evaluation hub for VLAs with unified setup for evaluating any VLA policy.

## LIBERO Overview

- **Scale**: Over 130 tasks available
- **Purpose**: Large open benchmark for Vision-Language-Action (VLA) policies
- **Focus**: Enables easy integration and standardized evaluation across different VLA models

## Dataset Details

The LIBERO dataset is available on the Hugging Face Hub:
- **Dataset**: [HuggingFaceVLA/libero](https://huggingface.co/datasets/HuggingFaceVLA/libero)
- **Stats**: 273k entries, 23.8k downloads, 54 likes (as of the article date)

## Documentation and Getting Started

The article references comprehensive documentation for implementation:
- **Documentation Link**: https://huggingface.co/docs/lerobot/en/libero
- The docs provide detailed setup instructions for using LIBERO with LeRobot

## Demo

The article includes a demonstration GIF showing GR00T performing tasks in LIBERO simulation environments, indicating successful integration of LIBERO simulation support alongside the VLA models.

## Context

LIBERO integration is part of a broader expansion of simulation environments in v0.4.0, alongside Meta-World support, enabling researchers to evaluate policies across diverse robotic manipulation benchmarks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-13T09:51:02.676973+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2506.01844v1",
  "prompt": "Find all mentions of: max_action_dim, action_dim, padding, 32D, action dimension, action space, SO-100, SO-101, LIBERO action, joint control vs end-effector control. Also look for Table 12 about chunk size ablation and any appendix about training configuration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2506.01844v1",
    "prompt": "Find all mentions of: max_action_dim, action_dim, padding, 32D, action dimension, action space, SO-100, SO-101, LIBERO action, joint control vs end-effector control. Also look for Table 12 about chunk size ablation and any appendix about training configuration."
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-13T09:51:02.677099+00:00_

# SpatialVLA: Key Technical Details

## LIBERO Success Rates (Table III)

| Model | Spatial | Object | Goal | Long | Average |
|-------|---------|--------|------|------|---------|
| SpatialVLA (fine-tuned) | 88.2% | 89.9% | 78.6% | 55.5% | **78.1%** |
| OpenVLA (fine-tuned) | 84.7% | 88.4% | 79.2% | 53.7% | 76.5% |
| TraceVLA (fine-tuned) | 84.6% | 85.2% | 75.1% | 54.1% | 74.8% |
| Octo (fine-tuned) | 78.9% | 85.7% | 84.6% | 51.1% | 75.1% |

SpatialVLA achieved the highest average performance across all four task suites.

## Fine-tuning Approaches

The paper evaluates two primary strategies:

1. **Full Parameter Fine-tuning**: Direct optimization of all model weights on downstream tasks
2. **LoRA Fine-tuning** (r=32, α=32): Parameter-efficient adaptation for smaller datasets like LIBERO

**Key finding**: "LoRA tuning outperforms full-parameter fine-tuning on small dataset tasks," with spatial embedding adaptation providing additional gains of 4-5% on individual LIBERO suites.

## Training Hyperparameters

- **Pre-training**: 1.1 million robot demonstrations across 64 A100 GPUs for 10 days
- **Batch size**: 2048 (pre-training); 128 (ablation studies on 8 A100s)
- **Training steps**: 120k steps (ablation experiments)
- **Epochs**: 200 epochs for LIBERO fine-tuning

## Action Space Configuration

The model discretizes continuous 7D actions into adaptive spatial grids:

- **Total tokens**: V = 8,194
- **Per-step prediction**: 3 spatial action tokens (vs. 7 in prior work)
- **Decomposition**: Translation (M_trans=4,096) + Rotation (M_rot=4,096) + Gripper (2 tokens)
- **Grid initialization**: Gaussian distribution-based equal probability binning

## Model Architecture Details

- **Vision encoder**: SigLIP for 2D semantic feature extraction
- **VLM backbone**: PaliGemma2
- **Depth estimation**: ZoeDepth for ego3D position encoding
- **Inference**: 8.5GB GPU memory, ~20Hz on RTX 4090
- **Total parameters**: 3.5B (significantly smaller than RT-2-X at 55B)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-13T09:51:02.677253+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx",
  "prompt": "Extract the full content including any conversion scripts, dataset preparation steps, training configurations, observation/action specs, and any details about how to prepare LIBERO data from scratch."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx",
    "prompt": "Extract the full content including any conversion scripts, dataset preparation steps, training configurations, observation/action specs, and any details about how to prepare LIBERO data from scratch."
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-13T09:51:02.677416+00:00_

Web search results for query: ""Cosmos-Policy" LIBERO NVIDIA VLA 2025 fine-tune"

Links: [{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://research.nvidia.com/labs/dir/cosmos-policy/cosmos_policy_index.html"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - Cosmos Cookbook","url":"https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/predict2/cosmos_policy/post_training.html"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/html/2601.16163v1"},{"title":"Understanding How NVIDIA Cosmos Policy Works | Paper: Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - BioErrorLog Tech Blog","url":"https://en.bioerrorlog.work/entry/nvidia-cosmos-policy-paper"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning | OpenReview","url":"https://openreview.net/forum?id=wPEIStHxYH"},{"title":"GitHub - NVlabs/cosmos-policy: Cosmos Policy · GitHub","url":"https://github.com/NVlabs/cosmos-policy"},{"title":"Cosmos Policy — Cosmos Lab","url":"https://research.nvidia.com/labs/cosmos-lab/cosmos-policy/"},{"title":"NVIDIA adds Cosmos Policy to its world foundation models - The Robot Report","url":"https://www.therobotreport.com/nvidia-adds-cosmos-policy-world-foundation-models/"},{"title":"cosmos-policy/README.md at main · NVlabs/cosmos-policy","url":"https://github.com/NVlabs/cosmos-policy/blob/main/README.md"},{"title":"Introducing NVIDIA Cosmos Policy for Advanced Robot Control","url":"https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control"}]

Based on the search results, here's information about Cosmos-Policy and its fine-tuning on LIBERO with NVIDIA's VLA:

## Overview

Cosmos Policy is a simple approach for adapting a large pretrained video model (Cosmos-Predict2) into an effective robot policy through a single stage of post-training on robot dem
…[truncated 1428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-13T09:51:02.677574+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2",
  "prompt": "Extract conversion script details, ideas discussed, and any technical information about the dataset format or how it was created."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2",
    "prompt": "Extract conversion script details, ideas discussed, and any technical information about the dataset format or how it was created."
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-13T09:51:02.677704+00:00_

# Search Results for Action Dimension and Configuration Details

I've thoroughly reviewed the provided document and found the following:

## Action Dimension References

**Not found**: The specific terms "max_action_dim," "action_dim," "padding," or "32D" do not appear in this paper.

## Action Space Details

The paper mentions that SmolVLA predicts "action chunks" but does not explicitly state a specific action dimensionality. The document references that the model outputs "a chunk of n low-level actions" where "n=50" during training, but the actual action vector dimensions remain unspecified in the provided text.

## Robot Platforms

**SO-100 and SO-101**: The paper describes these as "low-cost, 3D-printable robotic arms" with "six degrees of freedom" controlled via "position commands." The SO-101 represents an updated version with "better arm design" and "smoother movements."

## Table 12 - Chunk Size Ablation

This table evaluates how varying chunk sizes (n ∈ {1, 10, 30, 50, 100}) affects LIBERO benchmark performance, finding that "chunk sizes between 10 and 50 provide a good balance."

## Control Type

The paper does not explicitly distinguish between "joint control vs end-effector control" in the provided sections.

**Note**: Training configuration details and appendix information about action space specifications were not located in the supplied document excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-13T09:51:02.677844+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.19850",
  "prompt": "Extract: model architecture, LIBERO per-suite success rates (Spatial, Object, Goal, Long), fine-tuning method, training details (steps, lr, batch size, hardware), action space configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2506.19850",
    "prompt": "Extract: model architecture, LIBERO per-suite success rates (Spatial, Object, Goal, Long), fine-tuning method, training details (steps, lr, batch size, hardware), action space configuration"
  }
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-13T09:51:02.677970+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CogVLA LIBERO 97.4 results 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CogVLA LIBERO 97.4 results 2025"
  }
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-13T09:51:02.678091+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0-FAST LIBERO success rate 2025 fine-tune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0-FAST LIBERO success rate 2025 fine-tune"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-13T09:51:02.678209+00:00_

# Dataset Conversion Discussion Summary

## Key Information Extracted

### Conversion Tool
- **Tool Name**: [any4lerobot](https://github.com/Tavish9/any4lerobot)
- **Purpose**: Converts LIBERO HDF5 datasets to LeRobot format with video storage
- **Space Efficiency**: Stores observations in MP4 files rather than individual images, significantly reducing storage requirements

### Dataset Details
- **Source Format**: LIBERO HDF5 files
- **Target Format**: LeRobot format with MP4 video encoding
- **Filtering Applied**: Uses OpenVLA script-based filtering (called `libero_no_noops`)
- **Original vs. Filtered Episodes**:
  - Original LIBERO: 500 episodes per dataset (10 tasks × 50 demos)
  - Filtered versions in repo:
    - `libero_spatial_no_noops_lerobot`: 434 episodes
    - `libero_object_no_noops_lerobot`: 452 episodes

### Technical Issues & Solutions

**Video Decoding Problems**:
1. Random video corruption occurs during conversion
2. **Workaround**: Re-encode the image sequence for problematic episodes back into video
3. **Encoding Recommendation**: 
   - Current method uses `av1` encoding (occasional corruption)
   - Suggested alternative: X264 encoder (more stable)
4. **Status**: Issue primarily affects LIBERO datasets; other datasets encode without issues

### Filtering Reference
- Implementation: [regenerate_libero_dataset.py](https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/libero_utils/regenerate_libero_dataset.py)
- Details available in OpenVLA documentation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-13T09:51:02.678370+00:00_

# LIBERO Integration for LeRobot: Key Details

## Overview
LIBERO is described as "a benchmark designed to study **lifelong robot learning**" with "a set of standardized manipulation tasks that focus on **knowledge transfer**." The benchmark comprises 130 tasks across five suites.

## Task Suites Available
The documentation lists these options:
- LIBERO-Spatial (10 tasks)
- LIBERO-Object (10 tasks)
- LIBERO-Goal (10 tasks)
- LIBERO-90 (90 tasks)
- LIBERO-Long (10 tasks)

## Installation
Users must install with: `pip install -e ".[libero]"` and set the MuJoCo rendering backend via environment variable for headless systems.

## Observation & Action Specifications

**Observations include:**
- 8-dimensional proprioceptive state (end-effector position, orientation, gripper)
- Main camera view (HWC uint8 format)
- Wrist camera view (HWC uint8 format)

**Actions:**
Continuous control in a "Box(-1, 1, shape=(7,))" space—"6D end-effector delta + 1D gripper"

## Dataset & Training
The preprocessed LIBERO dataset is available at HuggingFaceVLA/libero. Documentation provides example training commands using the `lerobot-train` CLI with parameters for policy type, batch size, and training steps.

## Evaluation Protocol
The recommended approach uses "10 episodes per task across all four standard suites" for reproducible benchmarking, yielding 400 total episodes.

## Published Results Reference
The documentation reports Pi0.5 (LeRobot) achieving 97.5% average success across the four suites, with individual suite scores ranging from 96.0–99.0%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-13T09:51:02.678518+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/lerobot/configs/policy/smolvla.yaml",
  "prompt": "Extract all configuration parameters, especially action-related ones: action_dim, max_action_dim, action_feature, chunk_size, n_action_steps, state_dim, and any other relevant parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/blob/main/lerobot/configs/policy/smolvla.yaml",
    "prompt": "Extract all configuration parameters, especially action-related ones: action_dim, max_action_dim, action_feature, chunk_size, n_action_steps, state_dim, and any other relevant parameters."
  }
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-13T09:51:02.678648+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot smolvla.yaml max_action_dim action_feature config 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot smolvla.yaml max_action_dim action_feature config 2025"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-13T09:51:02.678760+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-13T09:51:02.678872+00:00_

# UniVLA Paper Summary

Based on the arXiv page content provided, I can only extract limited information:

**Available Information:**

The abstract indicates UniVLA is "a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences." It incorporates world modeling during post-training to capture causal dynamics from videos.

**Performance Metrics:**
The paper reports achieving "95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%." However, the specific per-suite breakdown (Spatial, Object, Goal, Long) is not included in this abstract.

**Not Available in Source:**
The webpage excerpt does not contain:
- Detailed model architecture specifications
- Individual LIBERO suite success rates
- Fine-tuning methodology details
- Training parameters (steps, learning rate, batch size)
- Hardware specifications
- Action space configuration

**Recommendation:**
To obtain these technical details, you would need to access the full PDF or HTML version of the paper, which are linked on this arXiv page but not fully reproduced in the content provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-13T09:51:02.679007+00:00_

Web search results for query: "CogVLA LIBERO 97.4 results 2025"

Links: [{"title":"GitHub - iLearn-Lab/NeurIPS25-CogVLA: [NeurIPS 2025] CogVLA: Cognition-Aligned Vision-Language-Action Models via Instruction-Driven Routing & Sparsification · GitHub","url":"https://github.com/iLearn-Lab/NeurIPS25-CogVLA"},{"title":"GitHub - JiuTian-VL/CogVLA: [NeurIPS 2025] CogVLA: Cognition-Aligned Vision-Language-Action Models via Instruction-Driven Routing & Sparsification","url":"https://github.com/JiuTian-VL/CogVLA"},{"title":"CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification","url":"https://arxiv.org/html/2508.21046v1"},{"title":"CogVLA: Cognition-Aligned Vision-Language-Action Model via","url":"https://arxiv.org/pdf/2508.21046"},{"title":"Next Generation VLA Model by CogVLA! Instruction-driven routing and efficient robot operation based on cognitive science | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/llm-paper/cogvla"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/cce95bd4761c6e1cbc198e0ca5fe030ab6f2ff88.pdf"},{"title":"Libero® SoC Design Suite Versions 2025.2 to 12.0 | Microchip Technology","url":"https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/fpga/libero-software-later-versions"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA","url":"https://arxiv.org/pdf/2512.00903"},{"title":"Targa Libero Ferrario 2025 One day race results","url":"https://www.procyclingstats.com/national-race/targa-libero-ferrario/2025/result"}]

Based on the search results, here's what I found about CogVLA's LIBERO 97.4 results:

CogVLA achieves state-of-the-art performance with success rates of 97.4% on the LIBERO benchmark.
…[truncated 709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-13T09:51:02.679154+00:00_

Web search results for query: "pi0-FAST LIBERO success rate 2025 fine-tune"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies","url":"https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"},{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"},{"title":"PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/952"},{"title":"[Quick Review] π_RL: Online RL Fine-tuning for Flow-based\\n Vision-Language-Action Models","url":"https://liner.com/review/%CF%80_rl-online-rl-finetuning-for-flowbased-visionlanguageaction-models"},{"title":"doremifasolatido/pi0-fast-libero-lora · Hugging Face","url":"https://huggingface.co/doremifasolatido/pi0-fast-libero-lora"},{"title":"Open Sourcing π0","url":"https://www.pi.website/blog/openpi"}]

Based on the search results, here's what I found about π0-FAST LIBERO success rates with fine-tuning:

## Key Findings:

The π0.5 model fine-tuned on LIBERO datasets achieved the following success rates: LIBERO-Spatial 97.4%, LIBERO-Object 98.4%, LIBERO-Goal 97.6%, and LIBERO-10 93.0%.

For π0 models more generally with online reinforcement learning fine-tuning, Flow-Noise boosts the average 
…[truncated 683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-13T09:51:02.679328+00:00_

Web search results for query: "lerobot smolvla.yaml max_action_dim action_feature config 2025"

Links: [{"title":"VLA (2) SmolVLA, ACT — XLeRobot 0.3.0 documentation","url":"https://xlerobot.readthedocs.io/en/latest/software/getting_started/VLA_smol.html"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"lerobot/examples/tutorial/smolvla/using_smolvla_example.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/examples/tutorial/smolvla/using_smolvla_example.py"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"config.json · lerobot/smolvla_base at 04d96c1f9167360280aaa54de31418f824d1ef48","url":"https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json"},{"title":"lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"},{"title":"`smolvla_base training`: `Expected all tensors to be on the same device` · Issue #1377 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1377"}]

Based on the search results, I found relevant information about SmolVLA configuration, particularly regarding `max_action_dim` and `action_feature`:

## SmolVLA Configuration: max_action_dim and action_feature

SmolVLA uses dynamic padding during training where actions are padded to `max_action_dim` (32D), and during inference, actions are cropped back to the original action dimensions 
…[truncated 1055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-13T09:51:02.679491+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2508.21046v1",
  "prompt": "Extract: model architecture, LIBERO per-suite success rates table comparing CogVLA to baselines, fine-tuning method (LoRA rank, full fine-tune etc.), training details (steps, lr, batch size, hardware), action space configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2508.21046v1",
    "prompt": "Extract: model architecture, LIBERO per-suite success rates table comparing CogVLA to baselines, fine-tuning method (LoRA rank, full fine-tune etc.), training details (steps, lr, batch size, hardware), action space configuration"
  }
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-13T09:51:02.679629+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0.5 LIBERO 97.4 success rate fine-tune training details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0.5 LIBERO 97.4 success rate fine-tune training details"
  }
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-13T09:51:02.679757+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MoDE MDT diffusion LIBERO 2025 success rate results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MoDE MDT diffusion LIBERO 2025 success rate results"
  }
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-13T09:51:02.679918+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json",
  "prompt": "Extract all configuration parameters from this config.json, especially: max_action_dim, action_dim, action_feature, state_feature, chunk_size, n_action_steps, input_features, output_features, and any action-space related settings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json",
    "prompt": "Extract all configuration parameters from this config.json, especially: max_action_dim, action_dim, action_feature, state_feature, chunk_size, n_action_steps, input_features, output_features, and any action-space related settings."
  }
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-13T09:51:02.680137+00:00_

# Configuration Parameters for lerobot/smolvla_base

## Key Action-Space and Dimension Settings

| Parameter | Value |
|-----------|-------|
| **max_action_dim** | 32 |
| **max_state_dim** | 32 |
| **chunk_size** | 50 |
| **n_action_steps** | 50 |
| **n_obs_steps** | 1 |

## Output Features (Action)

```json
"output_features": {
  "action": {
    "type": "ACTION",
    "shape": [6]
  }
}
```

**Action Dimension**: 6 (actual action space size)

## Input Features (State & Visual Observations)

```json
"input_features": {
  "observation.state": {
    "type": "STATE",
    "shape": [6]
  },
  "observation.image": {
    "type": "VISUAL",
    "shape": [3, 256, 256]
  },
  "observation.image2": {
    "type": "VISUAL",
    "shape": [3, 256, 256]
  },
  "observation.image3": {
    "type": "VISUAL",
    "shape": [3, 256, 256]
  }
}
```

**State Feature Dimension**: 6

## Normalization Strategy

```json
"normalization_mapping": {
  "VISUAL": "IDENTITY",
  "STATE": "MEAN_STD",
  "ACTION": "MEAN_STD"
}
```

## Summary

- **Action Space**: 6-dimensional continuous actions
- **State Space**: 6-dimensional state observations
- **Vision Input**: 3 multi-view camera inputs (256×256 RGB)
- **Action Prediction**: 50-step future action chunks
- **Model Architecture**: SmolVLM2-500M vision-language-action model

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-13T09:51:02.680387+00:00_

Web search results for query: "MoDE MDT diffusion LIBERO 2025 success rate results"

Links: [{"title":"Efficient Diffusion Transformer Policies with Mixture of Expert Denoisers for Multitask Learning","url":"https://mbreuss.github.io/MoDE_Diffusion_Policy/"},{"title":"GitHub - intuitive-robots/MoDE_Diffusion_Policy: [ICLR 25] Code for \"Efficient Diffusion Transformer Policies with Mixture of Expert Denoisers for Multitask Learning\" · GitHub","url":"https://github.com/intuitive-robots/MoDE_Diffusion_Policy"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://arxiv.org/html/2508.00697v1"},{"title":"Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals","url":"https://intuitive-robots.github.io/mdt_policy/"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"},{"title":"Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals","url":"https://arxiv.org/html/2407.05996v1"},{"title":"Goal Conditioned Imitation Learning using Score-based Diffusion Policies","url":"https://intuitive-robots.github.io/beso-website/"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Multimodal Diffusion Transformer: Learning Versatile Behavior from","url":"https://openreview.net/pdf/7f244a9f6cc676d079f8357e0e789455c22ac7da.pdf"},{"title":"nvidia/Cosmos-Policy-LIBERO-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B"}]

Based on the search results, here are the key findings for MoDE MDT diffusion LIBERO 2025 success rate results:

## MoDE Performance on LIBERO

MoDE is the first policy to achieve an over 90% success rate in the challenging LIBERO-10 experiment. MoDE surpasses prior b
…[truncated 998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-13T09:51:02.680625+00:00_

# CogVLA: Technical Architecture and Training Configuration

## Model Architecture

CogVLA employs a three-stage progressive design inspired by human multimodal coordination:

**Stage 1 - Encoder-FiLM based Aggregation Routing (EFA-Routing):** Compresses visual tokens to 25% of original scale using instruction-guided modulation. The system uses dual vision encoders (SigLIP and DINOv2) with 64 aggregation tokens each, dynamically fusing their outputs based on task instructions.

**Stage 2 - LLM-FiLM based Pruning Routing (LFP-Routing):** Applies semantic-aware token pruning within the language model, achieving approximately 50% token reduction through a shifted cosine schedule that controls retention ratios across transformer layers.

**Stage 3 - V-L-A Coupled Attention (CAtten):** Implements hierarchical attention combining causal vision-language attention with bidirectional action decoding to maintain coherence under compressed inputs.

## LIBERO Benchmark Performance

| Task Suite | CogVLA SR | Ranking |
|-----------|-----------|---------|
| Spatial   | 98.6%     | 1st     |
| Object    | 98.8%     | 1st (tied) |
| Goal      | 96.6%     | 2nd     |
| Long      | 95.4%     | 1st     |
| **Average** | **97.4%** | **1st** |

CogVLA outperformed OpenVLA-OFT (97.1%) and other state-of-the-art baselines across most task categories.

## Training Configuration

**LIBERO Fine-tuning:**
- Method: Low-Rank Adaptation (LoRA) with rank 32, α=64
- Steps: 60,000
- Batch size: 64
- Learning rate: 5e-4
- Hardware: 4×A800 GPUs (80GB)
- Evaluation: Every 10,000 steps
- Action chunk size (K): 8

**Real-world Fine-tuning (ALOHA):**
- Method: LoRA (rank 32, α=64)
- Steps: 80,000
- Batch size: 32
- Learning rate: 5e-4 (reduced to 5e-5 after 50K steps)
- Evaluation: Every 10K steps starting at step 60K
- Action chunk size (K): 25

## Action Space Configuration

The atomic action vector has dimensionality D=7, comprising:
- 3-DoF translation (ΔT)
- 3-DoF rotation (ΔR)
- Binary gripper con
…[truncated 571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-13T09:51:02.680877+00:00_

Web search results for query: "pi0.5 LIBERO 97.4 success rate fine-tune training details"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"[Feature Proposal] Add LoRA training support for pi0.5 (PyTorch backend) · Issue #842 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/842"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"𝜋_\"RL\": Online RL Fine-tuning for Flow-based Vision-Language-Action Models","url":"https://arxiv.org/html/2510.25889v1"},{"title":"π₀.₅ (Pi05) Policy · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi05"},{"title":"question about lora fine-tuning for pi0.5 · Issue #672 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/672"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"}]

Based on the search results, I found information about pi0.5 LIBERO fine-tuning with the 97.4% success rate you mentioned:

## Pi0.5 LIBERO Success Rates

The pi0.5 model achieved a 97.4% success rate on the LIBERO-Spatial task suite, along with strong performance on other LIBERO benchmarks.

## Fine-Tuning Training Details

Physical Intelligence provides example fine-tuning configs for π₀, π₀-FAST, and π₀.₅ 
…[truncated 937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 179 · 2026-05-13T09:51:02.681119+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2510.25889v1",
  "prompt": "Extract all LIBERO per-suite success rates for pi0 and pi0.5 models (baseline and fine-tuned), training details, fine-tuning method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2510.25889v1",
    "prompt": "Extract all LIBERO per-suite success rates for pi0 and pi0.5 models (baseline and fine-tuned), training details, fine-tuning method"
  }
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-13T09:51:02.681338+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Octo LIBERO success rate per suite spatial object goal long"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Octo LIBERO success rate per suite spatial object goal long"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-13T09:51:02.681549+00:00_

Web search results for query: "Octo LIBERO success rate per suite spatial object goal long"

Links: [{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"Github","url":"https://visual-cot-vla-sub.github.io/"},{"title":"CoT-VLA","url":"https://cot-vla.github.io/"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"Success rate of the π 0 model on the LIBERO-Goal, Object, Spatial and... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rate-of-the-p-0-model-on-the-LIBERO-Goal-Object-Spatial-and-Long-task-suits_tbl1_396330496"},{"title":"Libero-Object Benchmark","url":"https://www.emergentmind.com/topics/libero-object-benchmark"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models [Quick Review]","url":"https://liner.com/review/cotvla-visual-chainofthought-reasoning-for-visionlanguageaction-models"}]

Based on the search results, I found relevant information about success rates on LIBERO task suites. Here's what the search revealed:

CoT-VLA achieves the best or competitive success rates across all LIBERO task suites (Spatial, Object, Goal, Long), with an average success rate of 81.13% compared to OpenVLA's 76.5%.

More broadly, advanced approaches have set new performance benchmarks (up to 98.1% average success rate) on LIBERO tasks.

The LIBERO benchmark evaluates models across differe
…[truncated 714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-13T09:51:02.681882+00:00_

I now have comprehensive information from all sources. Here is the compiled summary:

---

## SmolVLA Fine-tuning: Comprehensive Summary

### 1. Model Overview

**Model ID:** `lerobot/smolvla_base`
**Parameters:** ~450M total (~100M trainable during default fine-tuning)
**Architecture:**
- VLM backbone: SmolVLM2-500M-Video-Instruct (SigLIP vision encoder + SmolLM2-1.7B-Instruct language decoder)
- Action Expert: Flow-Matching Transformer (~100M params), hidden size = 75% of VLM hidden dim
- Visual token compression: PixelShuffle → **64 tokens/frame** (vs. 1024 standard)
- Layer skipping: features from intermediate VLM layers (~L/2) for faster inference
- During default fine-tuning, only the action expert is trained; VLM is frozen

**Action/Observation Space (SO-100/SO-101 reference embodiment):**
- `observation.state`: [6] — robot joint positions
- `observation.image`, `observation.image2`, ... : [3, H, W] — multiple camera views (typically 256×256 or 640×480)
- `action`: [6] — normalized continuous joint commands (MEAN_STD normalization)
- Language instruction: optional string input
- Action chunking: `chunk_size=50` steps predicted per forward pass

---

### 2. Installation

```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e ".[smolvla]"
# For PEFT/LoRA support:
pip install -e ".[smolvla,peft]"
```

---

### 3. Fine-tuning Commands

**Standard full fine-tuning (recommended entry point):**
```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=${HF_USER}/mydataset \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --job_name=my_smolvla_training \
  --policy.device=cuda \
  --policy.dtype=bfloat16 \
  --wandb.enable=true
```
- ~4–5 hours on single A100 for 20k steps
- Start with batch_size=8–16 for smaller GPUs, increase as VRAM allows

**LoRA fine-tuning (PEFT — lower VRAM, ~8GB sufficient with 4-bit quantization):**
```bash
lerobot-train \
  --policy.path=lerobot/smolv
…[truncated 6666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Agent",
  "elapsed_ms": 27
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-13T09:51:02.682116+00:00_

# LIBERO Performance Results

## π0 Model Success Rates (%)

| Suite | SFT Baseline | Flow-SDE | Flow-Noise |
|-------|-------------|----------|-----------|
| Spatial | 65.3 | 98.4 | 99.0 |
| Object | 64.4 | 99.4 | 99.2 |
| Goal | 49.8 | 96.2 | 98.2 |
| Long | 51.2 | 90.2 | 93.8 |
| **Average** | **57.6** | **96.1** | **97.6** |

## π0.5 Model Success Rates (%)

| Suite | SFT Baseline | Flow-SDE | Flow-Noise |
|-------|-------------|----------|-----------|
| Spatial | 84.6 | 99.6 | 99.6 |
| Object | 95.4 | 100 | 100 |
| Goal | 84.6 | 98.8 | 99.6 |
| Long | 43.9 | 93.0 | 94.0 |
| **Average** | **77.1** | **97.9** | **98.3** |

## Fine-tuning Details

**Method**: The researchers implemented two approaches—Flow-Noise employs "a learnable noise network" integrated into denoising, while Flow-SDE "converts the deterministic ODE into an equivalent SDE" with hybrid sampling.

**Training Configuration**: During RL phase, the VLM remains frozen while "only fine-tune the 300M action expert model" for efficiency. The approach utilized PPO algorithm with "Generalized Advantage Estimation (GAE)" for advantage computation.

**Data**: π0 used 58 trajectories for standard tasks and 208 for Long tasks; π0.5 used 40 trajectories across all suites.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-13T09:51:02.682440+00:00_

Here is a comprehensive summary of all findings.

---

## LIBERO + LeRobot: Comprehensive Reference

### 1. Pre-converted Datasets on HuggingFace Hub

Multiple ready-to-use LeRobot-format LIBERO datasets exist — no conversion needed if you use these:

| Dataset | Suites | Frames | Notes |
|---|---|---|---|
| `HuggingFaceVLA/libero` | Spatial + Object + Goal + 10 | 273k | **Recommended by official docs for training** |
| `lerobot/libero` | Spatial + Object + Goal + 10 | 273,465 | 1,693 episodes, 40 tasks, Apache 2.0 |
| `physical-intelligence/libero` | Spatial + Object + Goal + 10 | 273k | PI-original, CC-BY-4.0, uses `image`/`wrist_image` keys |
| `IPEC-COMMUNITY/libero_spatial_no_noops_1.0.0_lerobot` | Spatial only | 53k | No-ops filtered, 434 episodes |
| `IPEC-COMMUNITY/libero_goal_no_noops_1.0.0_lerobot` | Goal only | 52k | No-ops filtered |
| `IPEC-COMMUNITY/libero_object_no_noops_1.0.0_lerobot` | Object only | 67k | No-ops filtered, 452 episodes |
| `IPEC-COMMUNITY/libero_10_no_noops_1.0.0_lerobot` | LIBERO-10 (Long) | 101k | No-ops filtered |
| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 | 569k | Largest; 90 tasks |
| `jesbu1/libero_90_lerobot` | LIBERO-90 | — | Used for pi0 fine-tuning |

**Note:** `lerobot/libero` and `HuggingFaceVLA/libero` contain only 4 suites (Spatial, Object, Goal, LIBERO-10). For LIBERO-90, use the IPEC-COMMUNITY collection or `jesbu1/libero_90_lerobot`.

---

### 2. Data Format

All LeRobot-format LIBERO datasets share this schema:

**Observation keys:**
- `observation.images.image` — 256×256×3 RGB, main camera (`agentview_image`), AV1-encoded MP4
- `observation.images.image2` — 256×256×3 RGB, wrist camera (`robot0_eye_in_hand_image`)
- `observation.state` — float32[8]: EEF position (3D) + axis-angle orientation (3D) + gripper qpos (2D)

**Action:** float32[7] — 6D EEF delta (xyz + rxryrz) + 1D gripper, clipped to [-1, 1]

**Metadata per frame:** `timestamp`, `frame_index`, `episode_index`, `task_index`, `index`

**FPS:**
…[truncated 4292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Agent",
  "elapsed_ms": 27
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-13T09:51:02.682674+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openvla-oft.github.io/",
  "prompt": "Extract full comparison table showing per-suite LIBERO success rates (Spatial, Object, Goal, Long) for ALL baselines including Octo, Diffusion Policy, MDT, Seer, DiT Policy, pi0, and OpenVLA variants. Also extract complete training hyperparameters table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openvla-oft.github.io/",
    "prompt": "Extract full comparison table showing per-suite LIBERO success rates (Spatial, Object, Goal, Long) for ALL baselines including Octo, Diffusion Policy, MDT, Seer, DiT Policy, pi0, and OpenVLA variants. Also extract complete training hyperparameters table."
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-13T09:51:02.682881+00:00_

I now have all the key information. Here is the compiled analysis:

---

## SmolVLA Action Space

### Base Model (`lerobot/smolvla_base`) Config
Source: `config.json` at HuggingFace

| Parameter | Value |
|---|---|
| `output_features.action.shape` | **[6]** — 6-dimensional actions |
| `input_features.observation.state.shape` | **[6]** — 6D proprioceptive state |
| `max_action_dim` | **32** (internal padding ceiling) |
| `max_state_dim` | 32 |
| `chunk_size` | 50 |
| `n_action_steps` | 50 |

The base model was trained on SO-100/SO-101 robot data, which uses a **6-DOF joint position control** scheme: `[shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll, gripper]`. This is **not** end-effector control.

### Dynamic Padding Mechanism
SmolVLA internally pads all actions to `max_action_dim=32` during training and forward passes, then crops back to `action_feature.shape[0]` for output. This means the model can accept **any action space ≤ 32D** without architectural changes — the `output_features.action.shape` in the loaded config drives the actual output dimension automatically. No manual `action_mode` override is needed.

---

## LIBERO Action Space

Source: Official LeRobot LIBERO documentation + `HuggingFaceVLA/libero` dataset schema

| Parameter | Value |
|---|---|
| Action dimension | **7** — `Box(-1, 1, shape=(7,))` |
| Breakdown | **6D end-effector delta + 1D gripper** |
| Components | `[dx, dy, dz, droll, dpitch, dyaw, gripper]` |
| Control mode | **Relative** (delta) by default; absolute mode also available |
| State dimension | **8** — `[eef_pos(3), axis-angle(3), gripper_qpos(2)]` |
| Cameras | `agentview_image` + `robot0_eye_in_hand_image` |
| Robot | Franka Panda (7-DOF arm) |

Example action vectors from the dataset:
- `[0.016, 0, 0, 0, 0, 0, -1]` — gripper close
- `[-0.053, -0.085, 0.489, 0, 0, 0, 1]` — move + gripper open

---

## Compatibility Analysis: SmolVLA base vs. LIBERO

| Dimension | SmolVLA base | LIBERO | Mismatch? |
|---|---|---|---
…[truncated 3655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Agent",
  "elapsed_ms": 26
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-13T09:51:02.683045+00:00_

# Response to Your Request

I've reviewed the webpage content thoroughly, and I must report that **neither of the specific tables you requested are present in the provided material**.

## What Is Available

The page includes:
- A visual chart labeled "LIBERO Simulation Benchmark: Task Performance" showing comparisons across the four LIBERO suites (Spatial, Object, Goal, Long) with multiple baselines
- References to achieving "97.1% average success rate" across the suites

However, the actual numerical data from that visualization is not transcribed in text form on the page.

## What Is Missing

1. **Per-suite breakdown table**: While the image shows results, the specific success rates for each baseline (Octo, Diffusion Policy, MDT, Seer, DiT Policy, π0, and various OpenVLA variants) per individual task suite are not provided in extractable text format.

2. **Training hyperparameters table**: No comprehensive hyperparameters table appears in the FAQ or methodology sections.

## Available Alternative

The FAQ section provides detailed GPU memory requirements for training different configurations, organized by dataset (LIBERO variants and ALOHA), but this differs from a traditional hyperparameters table covering learning rates, batch sizes, and optimization settings.

To obtain the complete tabular data you need, you would need to consult the full paper available at arXiv:2502.19645.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-13T09:51:02.683300+00:00_

I have sufficient data to compile the full summary. Here it is:

---

## VLA + LIBERO Prior Work: Comprehensive Summary

---

### Benchmark Setup (Standard LIBERO)

Four task suites, each with 10 tasks x 50 demonstrations (500 total):
- **LIBERO-Spatial**: same objects, varying spatial layouts
- **LIBERO-Object**: same scene, varying object types
- **LIBERO-Goal**: same scene/objects, varying goal predicates
- **LIBERO-Long** (aka LIBERO-10): long-horizon multi-step tasks

Standard evaluation: 500 test episodes per suite, success rate reported. Robot: Franka Panda, 7-DoF end-effector control + gripper. Inputs: third-person RGB + optionally wrist RGB + proprioception.

---

### Model-by-Model Results

#### 1. OpenVLA (baseline fine-tune) — arXiv:2406.09246
- **Architecture**: 7B LLM (LLaMA-2) + visual encoder (SigLIP), trained on Open X-Embodiment
- **Fine-tuning method**: LoRA r=32, α=32, no quantization
- **Training**: 50K steps, lr=5e-4, batch=128 (8×A100 80GB), image augmentations (random crop, color jitter)
- **Action space**: 7 discrete tokens per step (3 translation, 3 rotation, 1 gripper), single-step prediction
- **LIBERO results**:

| Suite | Success Rate |
|-------|-------------|
| Spatial | 84.7% |
| Object | 88.4% |
| Goal | 79.2% |
| Long | 53.7% |
| **Average** | **76.5%** |

- **Checkpoints**: Public on HuggingFace — `openvla/openvla-7b-finetuned-libero-{spatial,object,goal,10}`

---

#### 2. OpenVLA-OFT (Optimized Fine-Tuning) — arXiv:2502.19645, Feb 2025
- **Architecture**: Same 7B backbone as OpenVLA + MLP action head (4 layers, ReLU), parallel decoding
- **Fine-tuning method**: LoRA (parameter-efficient), continuous action representation (L1 regression)
- **Training**: 50K–150K steps, lr=5e-4→5e-5, batch=64–128, 8×A100/H100 80GB, 1–2 days
- **Action space**: 7-dim continuous, chunk size K=8, parallel decoding (all K actions in one forward pass)
- **LIBERO results** (multi-input: third-person + wrist + proprioception):

| Suite | Success Rate |
|--
…[truncated 8964 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Agent",
  "elapsed_ms": 25
}
```

</details>

---

### Tool call

_source line 189 · 2026-05-13T09:51:02.683519+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 190 · 2026-05-13T09:51:02.683659+00:00_

_project
dream_reports
libero-smolvla-env-report.md
manifest.yaml
method_section_draft.tex
mvp-point-reaching
pipeline-dimension-verification.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-13T09:51:02.683807+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/smolvla-libero-finetune-survey.md",
  "content": "# SmolVLA + LIBERO Fine-tuning 调研报告\n\n**日期**: 2026-05-13\n\n---\n\n## 1. SmolVLA Fine-tuning 官方方式\n\n### 模型概况\n- **Model ID**: `lerobot/smolvla_base`\n- **参数量**: ~450M total, ~100M trainable (action expert)\n- **架构**: SmolVLM2-500M-Video-Instruct (SigLIP + SmolLM2-1.7B) + Flow-Matching Transformer action expert\n- **默认 action/state**: `action.shape=[6]`, `state.shape=[6]` (SO-100/SO-101 joint position control)\n- **Action chunking**: `chunk_size=50`\n- **动态 padding**: 内部 pad 到 `max_action_dim=32`，输出时裁剪到实际维度\n\n### 安装\n```bash\ngit clone https://github.com/huggingface/lerobot.git && cd lerobot\npip install -e \".[smolvla]\"       # 基础\npip install -e \".[smolvla,peft]\"  # + LoRA 支持\n```\n\n### 训练命令\n\n**Full fine-tune (action expert only, VLM frozen)**:\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --batch_size=64 \\\n  --steps=20000 \\\n  --output_dir=outputs/train/smolvla_libero \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16\n```\n\n**LoRA fine-tune (低显存)**:\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --policy.output_features=null \\\n  --policy.input_features=null \\\n  --policy.optimizer_lr=1e-3 \\\n  --policy.scheduler_decay_lr=1e-4 \\\n  --steps=100000 \\\n  --batch_size=32 \\\n  --peft.method_type=LORA \\\n  --peft.r=64 \\\n  --peft.lora_alpha=64\n```\n\nPEFT 默认 target modules: `q_proj`, `v_proj` + action expert 的 `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`\n\n### 关键超参数\n\n| 参数 | 默认值 | 说明 |\n|------|--------|------|\n| steps | 20k (real) / 100k (sim) | |\n| batch_size | 64 | 低显存减到 8-16 |\n| optimizer_lr | 1e-4 (full) / 1e-3 (LoRA) | |\n| chunk_size | 50 | 每次预测的 action 步数 |\n| dtype | bfloat16 | |\n| gradient_checkpointing | true | 省显存 |\n| peft.r | 64 | LoRA rank |\n\n### 关键文档\n- 官方 fine-tune docs: https://huggingface.co/docs/lerobot/smolvla\n- PEFT/LoRA docs: https://huggingface.co/docs/lerobot/en/peft_training\n- Model card: https://huggingface.co/lerobot/smolvla_base\n- Training notebook: https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb\n- SmolVLA blog: https://huggingface.co/blog/smolvla\n- Medium 教程: https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632\n\n---\n\n## 2. LIBERO 数据 → LeRobot 格式\n\n### 现成数据集（HuggingFace Hub，无需转换）\n\n| Dataset ID | 内容 | 规模 |\n|------------|------|------|\n| **`HuggingFaceVLA/libero`** | Spatial+Object+Goal+10 | 273k frames, 1693 eps |\n| `lerobot/libero` | 同上 | 273k frames |\n| `physical-intelligence/libero` | 同上（PI 版本） | 273k frames |\n| `IPEC-COMMUNITY/libero_spatial_no_noops_*` | 仅 Spatial | 53k frames |\n| `IPEC-COMMUNITY/libero_goal_no_noops_*` | 仅 Goal | 52k frames |\n| `IPEC-COMMUNITY/libero_object_no_noops_*` | 仅 Object | 67k frames |\n| `IPEC-COMMUNITY/libero_10_no_noops_*` | 仅 LIBERO-10 | 101k frames |\n| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 | 569k frames |\n| `jesbu1/libero_90_lerobot` | LIBERO-90 (π0 用) | — |\n\n**推荐**: 直接用 `HuggingFaceVLA/libero` 或 `lerobot/libero`，无需自行转换。\n\n### 数据格式\n\n```\nobservation.images.image  → 256×256×3 (agentview, AV1 MP4)\nobservation.images.image2 → 256×256×3 (wrist camera)\nobservation.state         → float32[8]: eef_pos(3) + axis_angle(3) + gripper_qpos(2)\naction                    → float32[7]: eef_delta(6) + gripper(1), clipped [-1,1]\nFPS: 10 Hz\n```\n\n### 转换脚本（如需自己转换）\n\n**方式 A: openpi 脚本 (RLDS → LeRobot)**\n```bash\n# https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py\nuv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/data --push_to_hub\n```\n\n**方式 B: any4lerobot (HDF5 → LeRobot)**\n```bash\n# https://github.com/Tavish9/any4lerobot/tree/main/libero2lerobot\npython libero_utils/regenerate_libero_dataset.py --resolution 256 --libero_task_suite libero_90\npython libero_h5.py --src-paths /path/to/libero/ --output-path /path/to/local\n```\n\n---\n\n## 3. Action Dimension 6→7 可行性\n\n### 不匹配分析\n\n| | SmolVLA base | LIBERO |\n|---|---|---|\n| Action dim | **6** (joint position) | **7** (EEF delta + gripper) |\n| State dim | **6** | **8** |\n| Control type | Joint position (SO-100) | End-effector delta (Franka) |\n\n### 解决方案：自动处理\n\nSmolVLA 内部使用动态 padding（`max_action_dim=32`），fine-tune 时 **自动从数据集推断 action_dim**。使用 LIBERO 数据训练时：\n- `output_features.action.shape` 自动设为 `[7]`\n- `input_features.observation.state.shape` 自动设为 `[8]`\n- 归一化统计量从 LIBERO 数据集重新计算\n- **无需手动修改任何维度参数**\n\n关键 flags（让 trainer 从数据集推断）:\n```\n--policy.output_features=null --policy.input_features=null\n```\n\n### 已有 checkpoint\n`lerobot/smolvla_libero` — SmolVLA 在 LIBERO 上 fine-tuned 的 checkpoint，action_dim=7。\n\n---\n\n## 4. 现成的 LIBERO Fine-tuned VLA Checkpoints\n\n### SmolVLA 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `lerobot/smolvla_libero` | SmolVLA fine-tuned on LIBERO |\n\n### π0 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `lerobot/pi0_libero_base` | π0 base |\n| `lerobot/pi0_fast_libero_base` | π0-FAST |\n| `lerobot/pi05_libero_finetuned` | π0.5 fine-tuned, **97.5% avg** |\n\n### OpenVLA 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `openvla/openvla-7b-finetuned-libero-spatial` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-object` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-goal` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-10` | per-suite |\n| `moojink/openvla-7b-oft-finetuned-libero-*` | OFT 版本, **97.1% avg** |\n\n### 其他\n| Checkpoint | 说明 |\n|------------|------|\n| `nvidia/Cosmos-Policy-LIBERO-Predict2-2B` | **98.5% avg**, SOTA |\n| `IPEC-COMMUNITY/spatialvla-4b-224-pt` | SpatialVLA |\n| `lerobot/xvla-libero` | xVLA |\n\n---\n\n## 5. LIBERO SOTA 排行榜\n\n| Model | Avg SR | 方法 | 显存/GPU |\n|-------|--------|------|----------|\n| LightVLA | ~99.7% | LoRA + token pruning | 8×A100 |\n| Cosmos-Policy | 98.5% | Full FT (video diffusion) | 64×H100 |\n| π0.5 + RL | 98.3% | RL fine-tune | — |\n| π0 + RL | 97.6% | RL fine-tune | — |\n| CogVLA | 97.4% | LoRA r=32 | 4×A800 |\n| OpenVLA-OFT | 97.1% | LoRA + parallel decoding | 8×A100 |\n| UniVLA | 95.5% | Autoregressive discrete | — |\n| SpatialVLA | 78.1% | LoRA r=32 | — |\n| OpenVLA | 76.5% | LoRA r=32 | 8×A100 |\n| Octo | 75.1% | Full FT | — |\n\n---\n\n## 6. 推荐的 Fine-tuning 方案\n\n### 方案 A: 直接用已有 checkpoint（最快）\n```bash\n# lerobot/smolvla_libero 已经 fine-tuned 好了，直接评估\nlerobot-eval --policy.path=lerobot/smolvla_libero --env.type=libero --env.task=libero_spatial\n```\n\n### 方案 B: 自己 fine-tune SmolVLA on LIBERO（推荐）\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --policy.output_features=null \\\n  --policy.input_features=null \\\n  --batch_size=32 \\\n  --steps=100000 \\\n  --output_dir=outputs/smolvla_libero \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16 \\\n  --wandb.enable=true\n```\n- 4090 24GB 可跑，batch_size 调到 8-16\n- 预计训练 8-12 小时\n\n### 方案 C: LoRA fine-tune（省显存）\n同上但加 `--peft.method_type=LORA --peft.r=64 --peft.lora_alpha=64`\n\n### 关键注意事项\n1. **数据集**: 用 `HuggingFaceVLA/libero`，不需要自己转换\n2. **Action dim**: 自动从数据集推断为 7，无需手动配置\n3. **归一化**: 自动使用 LIBERO 的 stats，不需要手动处理\n4. **评估**: `lerobot-eval --env.type=libero` 集成了 LIBERO 仿真环境\n5. **已有 checkpoint**: `lerobot/smolvla_libero` 可直接使用或作为 fine-tune 起点\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/smolvla-libero-finetune-survey.md",
    "content": "# SmolVLA + LIBERO Fine-tuning 调研报告\n\n**日期**: 2026-05-13\n\n---\n\n## 1. SmolVLA Fine-tuning 官方方式\n\n### 模型概况\n- **Model ID**: `lerobot/smolvla_base`\n- **参数量**: ~450M total, ~100M trainable (action expert)\n- **架构**: SmolVLM2-500M-Video-Instruct (SigLIP + SmolLM2-1.7B) + Flow-Matching Transformer action expert\n- **默认 action/state**: `action.shape=[6]`, `state.shape=[6]` (SO-100/SO-101 joint position control)\n- **Action chunking**: `chunk_size=50`\n- **动态 padding**: 内部 pad 到 `max_action_dim=32`，输出时裁剪到实际维度\n\n### 安装\n```bash\ngit clone https://github.com/huggingface/lerobot.git && cd lerobot\npip install -e \".[smolvla]\"       # 基础\npip install -e \".[smolvla,peft]\"  # + LoRA 支持\n```\n\n### 训练命令\n\n**Full fine-tune (action expert only, VLM frozen)**:\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --batch_size=64 \\\n  --steps=20000 \\\n  --output_dir=outputs/train/smolvla_libero \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16\n```\n\n**LoRA fine-tune (低显存)**:\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --policy.output_features=null \\\n  --policy.input_features=null \\\n  --policy.optimizer_lr=1e-3 \\\n  --policy.scheduler_decay_lr=1e-4 \\\n  --steps=100000 \\\n  --batch_size=32 \\\n  --peft.method_type=LORA \\\n  --peft.r=64 \\\n  --peft.lora_alpha=64\n```\n\nPEFT 默认 target modules: `q_proj`, `v_proj` + action expert 的 `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`\n\n### 关键超参数\n\n| 参数 | 默认值 | 说明 |\n|------|--------|------|\n| steps | 20k (real) / 100k (sim) | |\n| batch_size | 64 | 低显存减到 8-16 |\n| optimizer_lr | 1e-4 (full) / 1e-3 (LoRA) | |\n| chunk_size | 50 | 每次预测的 action 步数 |\n| dtype | bfloat16 | |\n| gradient_checkpointing | true | 省显存 |\n| peft.r | 64 | LoRA rank |\n\n### 关键文档\n- 官方 fine-tune docs: https://huggingface.co/docs/lerobot/smolvla\n- PEFT/LoRA docs: https://huggingface.co/docs/lerobot/en/peft_training\n- Model card: https://huggingface.co/lerobot/smolvla_base\n- Training notebook: https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb\n- SmolVLA blog: https://huggingface.co/blog/smolvla\n- Medium 教程: https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632\n\n---\n\n## 2. LIBERO 数据 → LeRobot 格式\n\n### 现成数据集（HuggingFace Hub，无需转换）\n\n| Dataset ID | 内容 | 规模 |\n|------------|------|------|\n| **`HuggingFaceVLA/libero`** | Spatial+Object+Goal+10 | 273k frames, 1693 eps |\n| `lerobot/libero` | 同上 | 273k frames |\n| `physical-intelligence/libero` | 同上（PI 版本） | 273k frames |\n| `IPEC-COMMUNITY/libero_spatial_no_noops_*` | 仅 Spatial | 53k frames |\n| `IPEC-COMMUNITY/libero_goal_no_noops_*` | 仅 Goal | 52k frames |\n| `IPEC-COMMUNITY/libero_object_no_noops_*` | 仅 Object | 67k frames |\n| `IPEC-COMMUNITY/libero_10_no_noops_*` | 仅 LIBERO-10 | 101k frames |\n| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 | 569k frames |\n| `jesbu1/libero_90_lerobot` | LIBERO-90 (π0 用) | — |\n\n**推荐**: 直接用 `HuggingFaceVLA/libero` 或 `lerobot/libero`，无需自行转换。\n\n### 数据格式\n\n```\nobservation.images.image  → 256×256×3 (agentview, AV1 MP4)\nobservation.images.image2 → 256×256×3 (wrist camera)\nobservation.state         → float32[8]: eef_pos(3) + axis_angle(3) + gripper_qpos(2)\naction                    → float32[7]: eef_delta(6) + gripper(1), clipped [-1,1]\nFPS: 10 Hz\n```\n\n### 转换脚本（如需自己转换）\n\n**方式 A: openpi 脚本 (RLDS → LeRobot)**\n```bash\n# https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py\nuv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/data --push_to_hub\n```\n\n**方式 B: any4lerobot (HDF5 → LeRobot)**\n```bash\n# https://github.com/Tavish9/any4lerobot/tree/main/libero2lerobot\npython libero_utils/regenerate_libero_dataset.py --resolution 256 --libero_task_suite libero_90\npython libero_h5.py --src-paths /path/to/libero/ --output-path /path/to/local\n```\n\n---\n\n## 3. Action Dimension 6→7 可行性\n\n### 不匹配分析\n\n| | SmolVLA base | LIBERO |\n|---|---|---|\n| Action dim | **6** (joint position) | **7** (EEF delta + gripper) |\n| State dim | **6** | **8** |\n| Control type | Joint position (SO-100) | End-effector delta (Franka) |\n\n### 解决方案：自动处理\n\nSmolVLA 内部使用动态 padding（`max_action_dim=32`），fine-tune 时 **自动从数据集推断 action_dim**。使用 LIBERO 数据训练时：\n- `output_features.action.shape` 自动设为 `[7]`\n- `input_features.observation.state.shape` 自动设为 `[8]`\n- 归一化统计量从 LIBERO 数据集重新计算\n- **无需手动修改任何维度参数**\n\n关键 flags（让 trainer 从数据集推断）:\n```\n--policy.output_features=null --policy.input_features=null\n```\n\n### 已有 checkpoint\n`lerobot/smolvla_libero` — SmolVLA 在 LIBERO 上 fine-tuned 的 checkpoint，action_dim=7。\n\n---\n\n## 4. 现成的 LIBERO Fine-tuned VLA Checkpoints\n\n### SmolVLA 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `lerobot/smolvla_libero` | SmolVLA fine-tuned on LIBERO |\n\n### π0 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `lerobot/pi0_libero_base` | π0 base |\n| `lerobot/pi0_fast_libero_base` | π0-FAST |\n| `lerobot/pi05_libero_finetuned` | π0.5 fine-tuned, **97.5% avg** |\n\n### OpenVLA 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `openvla/openvla-7b-finetuned-libero-spatial` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-object` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-goal` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-10` | per-suite |\n| `moojink/openvla-7b-oft-finetuned-libero-*` | OFT 版本, **97.1% avg** |\n\n### 其他\n| Checkpoint | 说明 |\n|------------|------|\n| `nvidia/Cosmos-Policy-LIBERO-Predict2-2B` | **98.5% avg**, SOTA |\n| `IPEC-COMMUNITY/spatialvla-4b-224-pt` | SpatialVLA |\n| `lerobot/xvla-libero` | xVLA |\n\n---\n\n## 5. LIBERO SOTA 排行榜\n\n| Model | Avg SR | 方法 | 显存/GPU |\n|-------|--------|------|----------|\n| LightVLA | ~99.7% | LoRA + token pruning | 8×A100 |\n| Cosmos-Policy | 98.5% | Full FT (video diffusion) | 64×H100 |\n| π0.5 + RL | 98.3% | RL fine-tune | — |\n| π0 + RL | 97.6% | RL fine-tune | — |\n| CogVLA | 97.4% | LoRA r=32 | 4×A800 |\n| OpenVLA-OFT | 97.1% | LoRA + parallel decoding | 8×A100 |\n| UniVLA | 95.5% | Autoregressive discrete | — |\n| SpatialVLA | 78.1% | LoRA r=32 | — |\n| OpenVLA | 76.5% | LoRA r=32 | 8×A100 |\n| Octo | 75.1% | Full FT | — |\n\n---\n\n## 6. 推荐的 Fine-tuning 方案\n\n### 方案 A: 直接用已有 checkpoint（最快）\n```bash\n# lerobot/smolvla_libero 已经 fine-tuned 好了，直接评估\nlerobot-eval --policy.path=lerobot/smolvla_libero --env.type=libero --env.task=libero_spatial\n```\n\n### 方案 B: 自己 fine-tune SmolVLA on LIBERO（推荐）\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --policy.output_features=null \\\n  --policy.input_features=null \\\n  --batch_size=32 \\\n  --steps=100000 \\\n  --output_dir=outputs/smolvla_libero \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16 \\\n  --wandb.enable=true\n```\n- 4090 24GB 可跑，batch_size 调到 8-16\n- 预计训练 8-12 小时\n\n### 方案 C: LoRA fine-tune（省显存）\n同上但加 `--peft.method_type=LORA --peft.r=64 --peft.lora_alpha=64`\n\n### 关键注意事项\n1. **数据集**: 用 `HuggingFaceVLA/libero`，不需要自己转换\n2. **Action dim**: 自动从数据集推断为 7，无需手动配置\n3. **归一化**: 自动使用 LIBERO 的 stats，不需要手动处理\n4. **评估**: `lerobot-eval --env.type=libero` 集成了 LIBERO 仿真环境\n5. **已有 checkpoint**: `lerobot/smolvla_libero` 可直接使用或作为 fine-tune 起点\n"
  }
}
````

</details>

---

### Tool result

_source line 192 · 2026-05-13T09:51:02.684034+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/smolvla-libero-finetune-survey.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 193 · 2026-05-13T09:51:02.684295+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-13T09:51:02.684456+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-13T09:51:02.684581+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TaskOutput",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TaskOutput",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-13T09:51:02.684699+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 197 · 2026-05-13T09:51:02.684858+00:00_

报告已写入 `artifacts/smolvla-libero-finetune-survey.md`。核心结论：

### 1. SmolVLA Fine-tuning 官方方式
- `lerobot-train --policy.path=lerobot/smolvla_base --dataset.repo_id=HuggingFaceVLA/libero`
- 支持 full fine-tune（仅 action expert, VLM frozen）和 LoRA
- 官方文档: https://huggingface.co/docs/lerobot/smolvla

### 2. LIBERO 数据
**不需要自己转换**。Hub 上已有 `HuggingFaceVLA/libero`（273k frames, 4 suites），直接用。LIBERO-90 用 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`。

### 3. Action Dim 6→7
**自动处理**。SmolVLA 内部 pad 到 `max_action_dim=32`，fine-tune 时从数据集推断 `action.shape=[7]`、`state.shape=[8]`。加 `--policy.output_features=null --policy.input_features=null` 让 trainer 自动推断。

### 4. 现成 Checkpoint
- **`lerobot/smolvla_libero`** — SmolVLA 已 fine-tuned on LIBERO，可直接用
- `lerobot/pi05_libero_finetuned` — π0.5, 97.5% avg
- `moojink/openvla-7b-oft-finetuned-libero-*` — OpenVLA-OFT, 97.1% avg
- `nvidia/Cosmos-Policy-LIBERO-Predict2-2B` — SOTA 98.5%

### 5. 推荐方案
先验证 `lerobot/smolvla_libero` 是否满足需求。如需自己训练，在 4090 上用 batch_size=8-16、100k steps、bfloat16 即可跑通。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_lerobot-libero-recipes_20260513T094527"
}
```

</details>

---
