# research smolvla libero gap deep dive

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 111
- **Recorded user turns:** 0
- **Tool calls:** 55
- **Original source:** `logs/chats/worker_research_smolvla_libero_gap_deep_dive_20260517T001826.jsonl`
- **Structured JSON:** [`c1a5728a8204ffa09675.json`](../../sessions/c1/c1a5728a8204ffa09675.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

111 recorded events

### Tool call

_source line 1 · 2026-05-17T00:25:31.964119+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__ssh_read_only",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__ssh_read_only",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T00:25:31.964765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T00:25:31.965003+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github huggingface lerobot smolvla libero training config yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github huggingface lerobot smolvla libero training config yaml"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T00:25:31.965161+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA paper LIBERO benchmark results 87.3 success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA paper LIBERO benchmark results 87.3 success rate"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T00:25:31.965541+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot smolvla libero fine-tuning batch size learning rate hyperparameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot smolvla libero fine-tuning batch size learning rate hyperparameters"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T00:25:31.965763+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress/configs -type f -name \"*.yaml\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress/configs -type f -name \"*.yaml\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T00:25:31.966029+00:00_

Web search results for query: "github huggingface lerobot smolvla libero training config yaml"

Links: [{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"GitHub - huggingface/VLAb · GitHub","url":"https://github.com/huggingface/VLAb"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"Training SmolVLA with LeRobot Notebook - Colab - Google","url":"https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"lerobot/examples/tutorial/smolvla/using_smolvla_example.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/examples/tutorial/smolvla/using_smolvla_example.py"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"Question about the HuggingFaceVLA/smolvla_libero Model Configuration · Issue #2294 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2294"},{"title":"lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"}]

Based on the search results, I found relevant information about SmolVLA, LeRobot, and LIBERO training configurations. Here's what I found:

## Training Configuration

To train SmolVLA with LeRobot, you can use commands like: `lerobot-train \ --policy.path=lerobot/smolvla_base \ --dataset.repo_id=${HF_USER}/mydataset \ --batch_size=64 \ --steps=20000 \ --output_dir=outputs/train/my_smolvla \ --job_name=my_smolvla_training \ --policy.device=cuda \ --wandb.enable=true`

## LIBERO Benchmark Sup
…[truncated 1086 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T00:25:31.966427+00:00_

Web search results for query: "SmolVLA paper LIBERO benchmark results 87.3 success rate"

Links: [{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]","url":"https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"SmolVLA: compact VLA for robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/smolvla-compact-vla-for-robot-policy-b30604ac23c5"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"SmolVLA: Compact Vision-Language-Action Model","url":"https://www.emergentmind.com/topics/smolvla"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"[Literature Review] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://www.themoonlight.io/en/review/smolvla-a-vision-language-action-model-for-affordable-and-efficient-robotics"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"}]

Based on the search results, I found detailed information about the SmolVLA paper and its LIBERO benchmark results.

The 0.45B parameter SmolVLA achieves an average success rate of 87.3% on LIBER
…[truncated 722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T00:25:31.966739+00:00_

Web search results for query: "lerobot smolvla libero fine-tuning batch size learning rate hyperparameters"

Links: [{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Parameter efficient fine-tuning with 🤗 PEFT","url":"https://huggingface.co/docs/lerobot/en/peft_training"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task","url":"https://huggingface.co/docs/lerobot/en/xvla"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"}]

Based on the search results, here are the key hyperparameters and training configurations for SmolVLA fine-tuning on LIBERO:

## Official LIBERO Fine-tuning Configuration

For PEFT (Parameter Efficient Fine-Tuning) on LIBERO, the recommended hyperparameters include:
- **Learning Rate**: `--policy.optimizer_lr=1e-3`
- **Learning Rate Decay**: `--policy.scheduler_decay_lr=1e-4`
- **Batch Size**: `--batch_s
…[truncated 1022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T00:25:31.967001+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/configs/baseline.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_anchor.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_delta01_lambda01.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_delta05_lambda10.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_k75.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_anchor_v7_1.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_anchor_v8.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_anchor_v8b_twostage.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_anchor_v8_1.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_anchor_v8_2.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_two_stage.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/imm_anchor_v8c_annealing.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/baseline_v6_alpha16.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/libero_baseline.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/libero_imm.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/libero_full_ft.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/libero_imm_twostage.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/libero_imm_twostage_fullft.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/libero_expert_only_ft.yaml\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T00:25:31.967217+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/3287",
  "prompt": "Extract all training hyperparameters discussed: batch size, learning rate, lr scheduler, warmup steps, training steps, gradient accumulation, weight decay, optimizer, image resolution, action normalization, dataset version. Also extract any official responses from maintainers about the correct config to reproduce SmolVLA LIBERO results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/issues/3287",
    "prompt": "Extract all training hyperparameters discussed: batch size, learning rate, lr scheduler, warmup steps, training steps, gradient accumulation, weight decay, optimizer, image resolution, action normalization, dataset version. Also extract any official responses from maintainers about the correct config to reproduce SmolVLA LIBERO results."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T00:25:31.967376+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/smolvla",
  "prompt": "Extract the complete training command and all hyperparameters for SmolVLA LIBERO fine-tuning. Include batch size, learning rate, lr scheduler, warmup steps, training steps, optimizer, image resolution, action normalization settings, eval settings. Look for any section about LIBERO benchmark training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/en/smolvla",
    "prompt": "Extract the complete training command and all hyperparameters for SmolVLA LIBERO fine-tuning. Include batch size, learning rate, lr scheduler, warmup steps, training steps, optimizer, image resolution, action normalization settings, eval settings. Look for any section about LIBERO benchmark training."
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T00:25:31.967561+00:00_

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
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T00:25:31.967747+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/configs/libero_baseline.yaml",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/configs/libero_baseline.yaml",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T00:25:31.967890+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/configs/libero_expert_only_ft.yaml",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/configs/libero_expert_only_ft.yaml",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T00:25:31.968030+00:00_

# Training Hyperparameters Discussion - GitHub Issue #3287

## Explicitly Mentioned Parameters

From the issue description, the following hyperparameters are discussed:

- **Batch Size:** 64 (mentioned for simulation benchmarks)
- **Training Steps:** 100,000
- **Episodes per task (evaluation):** 10

## Parameters NOT Provided

The issue explicitly requests but does not contain responses for:
- Learning rate
- Learning rate scheduler details
- Gradient accumulation steps
- Weight decay
- Optimizer specification
- Image resolution
- Action normalization approach
- Dataset version
- Warmup steps

## Key Context

The user states they followed the ablation setup from Section 4.7 with: `load_vlm_weights=True`, `freeze_vision_encoder=True`, `train_expert_only=True`

## Official Responses

**No maintainer responses are present** in this extracted content. The issue is an open inquiry requesting clarification on the exact reproduction recipe, not a resolved issue with official guidance.

The user notes significant performance gaps versus paper results (e.g., 44.8% vs ~71% on libero_10) and seeks confirmation on training methodology and hyperparameter specifications, but these questions remain unanswered in the provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T00:25:31.968246+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# LIBERO baseline: SmolVLA + LoRA fine-tuning, no IMM.\\n# Matches SmolVLA paper protocol for LIBERO benchmark.\\n#\\n# Official SmolVLA LIBERO results (paper): 87.3% avg\\n#   Spatial=90%, Object=96%, Goal=92%, Long=71%\\n#\\n# Training: lerobot-train uses policy.type=smolvla with train_expert_only=True\\n# We use LoRA fine-tuning from smolvla_base for IMM compatibility.\\n\\nmodel:\\n  name: smolvla\\n  pretrained: \\\"/root/autodl-tmp/.hf_cache/lerobot/smolvla_base\\\"\\n  lora:\\n    rank: 32\\n    alpha: 16\\n    dropout: 0.05\\n    target_modules_regex: \\\"(vlm_with_expert\\\\\\\\.lm_expert\\\\\\\\..*\\\\\\\\.(q|v)_proj|(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))\\\"\\n\\nimm:\\n  enabled: false\\n\\ndataset:\\n  repo_id: \\\"HuggingFaceVLA/libero\\\"\\n  features:\\n    state_dim: 8       # eef_pos(3) + axis_angle(3) + gripper_qpos(2)\\n    action_dim: 7      # 6D EEF delta + 1D gripper\\n    cameras:\\n      - \\\"observation.images.image\\\"        # agentview\\n      - \\\"observation.images.image2\\\"       # wrist (robot0_eye_in_hand)\\n\\ntraining:\\n  total_steps: 100000\\n  batch_size: 4\\n  eval_batch_size: 1\\n  num_workers: 4\\n  lr: 1.0e-4\\n  betas: [0.9, 0.95]\\n  weight_decay: 1.0e-10\\n  warmup_steps: 1000\\n  decay_lr: 2.5e-6\\n  grad_clip: 10.0\\n  eval_every: 5000\\n  save_every: 10000\\n  log_every: 50\\n  output_dir: \\\"checkpoints/libero_baseline\\\"\\n  seed: 42\\n\\nevaluation:\\n  # Offline eval metrics (perturbation robustness)\\n  perturbations: [0.0, 0.01, 0.02, 0.05]\\n  pruning_ratio: 0.5\\n  max_eval_batches: 50\\n\\n# LIBERO sim eval protocol (for eval_success_rate_libero.py)\\nlibero_eval:\\n  suites:\\n    - libero_spatial\\n    - libero_object\\n    - libero_goal\\n    - libero_10\\n  n_episodes_per_task: 10    # 10 tasks/suite × 10 eps = 100 eps/suite\\n  control_mode: \\\"relative\\\"\\n  cameras: \\\"agentview_image,robot0_ey
…[truncated 236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T00:25:31.968447+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# LIBERO Expert-Only FT: freeze VLM backbone, train action expert + projections only.\\n# Expected trainable: ~100M params (lm_expert + state/action projections).\\n# Expected frozen: ~350M params (vlm.model backbone + vision encoder).\\n\\n_base_: libero_baseline.yaml\\n\\nmodel:\\n  train_expert_only: true\\n  lora:\\n    rank: 0\\n\\ntraining:\\n  output_dir: \\\"checkpoints/libero_expert_only_ft\\\"\\n  save_every: 10000\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T00:25:31.968790+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2506.01844v1",
  "prompt": "Find the LIBERO benchmark training hyperparameters: batch size, learning rate, lr scheduler, warmup, training steps, optimizer, image resolution. Also find Table with LIBERO results showing per-suite breakdown (Spatial, Object, Goal, Long, 10). What is the exact 87.3% number - is it mean of 4 suites or 5? How many episodes per task for evaluation? What action normalization is used? What is the effective batch size for LIBERO fine-tuning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2506.01844v1",
    "prompt": "Find the LIBERO benchmark training hyperparameters: batch size, learning rate, lr scheduler, warmup, training steps, optimizer, image resolution. Also find Table with LIBERO results showing per-suite breakdown (Spatial, Object, Goal, Long, 10). What is the exact 87.3% number - is it mean of 4 suites or 5? How many episodes per task for evaluation? What action normalization is used? What is the effective batch size for LIBERO fine-tuning?"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T00:25:31.969130+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/1316",
  "prompt": "Extract information about SmolVLA LIBERO evaluation protocol: max_steps per suite, number of episodes, action space, control mode, any normalization details, and any performance gaps reported by users trying to reproduce results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/issues/1316",
    "prompt": "Extract information about SmolVLA LIBERO evaluation protocol: max_steps per suite, number of episodes, action space, control mode, any normalization details, and any performance gaps reported by users trying to reproduce results."
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T00:25:31.969453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"normalize\\|normalization\\|action_norm\\|NORMALIZE\\|unnormalize\" /root/autodl-tmp/importance_margin_vla_compress/src/ --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -rn \"normalize\\|normalization\\|action_norm\\|NORMALIZE\\|unnormalize\" /root/autodl-tmp/importance_margin_vla_compress/src/ --include=\"*.py\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T00:25:31.969611+00:00_

# LIBERO Benchmark Training Details

## Training Hyperparameters

Based on the document's implementation section:

- **Batch size**: 64
- **Learning rate**: Starts at 1e-4, decays to minimum of 2.5e-6
- **LR scheduler**: "cosine learning rate schedule" after 100-step warmup
- **Warmup steps**: 100
- **Training steps**: 100,000
- **Optimizer**: AdamW with β₁=0.9, β₂=0.95
- **Image resolution**: 512×512

## LIBERO Results Table

The document presents results showing performance across four suites:

| Suite | Performance |
|-------|-------------|
| Spatial | 90% |
| Object | 96% |
| Goal | 92% |
| Long | 71% |
| **Average** | **87.3%** |

The 87.3% figure represents the mean of these four suites (not five).

## Evaluation Protocol

"10 trials per task" were conducted with "binary completion criteria."

## Not Specified in Document

The document does not explicitly detail:
- Action normalization method
- Effective batch size (only states the 64 batch size for fine-tuning, but doesn't clarify if multi-GPU training affects this)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T00:25:31.969752+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/configs/libero_full_ft.yaml",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/configs/libero_full_ft.yaml",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T00:25:31.970206+00:00_

# SmolVLA LIBERO Evaluation Protocol - Information Summary

Based on the provided GitHub issue content, I cannot extract the requested technical details about SmolVLA's LIBERO evaluation protocol. 

The issue (opened June 16, 2025) contains a **question rather than documentation**. The user asks: "Could you elaborate on the details of the fine-tuning process? (which parameters were trained/frozen, optimizer, gradient steps, etc..)"

**What is absent from this content:**
- Max steps per suite specifications
- Episode count details
- Action space definitions
- Control mode parameters
- Normalization procedures
- Reported performance gaps or reproduction issues

**What is present:**
Only a reference that the authors "fine-tuned the SmolVLA baseline to the Franka Emika Panda and the Swayer arm to perform evaluation on the LIBERO and MetaSim benchmark respectively," but without implementation specifics.

To obtain the evaluation protocol details you're seeking, you would need to:
1. Consult the SmolVLA paper itself (referenced as impressive by the issue author)
2. Check the LeRobot repository's documentation or code
3. Review responses to this GitHub issue if they were provided

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T00:25:31.970403+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T00:25:31.970549+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# LIBERO Full Expert FT: freeze VLM+vision, full train action expert (no LoRA)\\n\\n_base_: libero_baseline.yaml\\n\\nmodel:\\n  train_expert_only: true\\n  lora:\\n    rank: 0\\n\\ntraining:\\n  output_dir: \\\"checkpoints/libero_full_ft\\\"\\n  save_every: 10000\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T00:25:31.970678+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"normalize\\|normalization\\|action_norm\\|unnormalize\" /root/autodl-tmp/importance_margin_vla_compress/src/ --include=\"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -rn \"normalize\\|normalization\\|action_norm\\|unnormalize\" /root/autodl-tmp/importance_margin_vla_compress/src/ --include=\"*.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T00:25:31.970804+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T00:25:31.970926+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress/src -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress/src -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T00:25:31.971051+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/autodl-tmp/importance_margin_vla_compress/src': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T00:25:31.971189+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/2294",
  "prompt": "Extract details about SmolVLA LIBERO model configuration differences, training parameters, action normalization, image preprocessing, and any resolution of the configuration discrepancy reported."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/issues/2294",
    "prompt": "Extract details about SmolVLA LIBERO model configuration differences, training parameters, action normalization, image preprocessing, and any resolution of the configuration discrepancy reported."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T00:25:31.971321+00:00_

# SmolVLA LIBERO Model Configuration Analysis

## Key Configuration Differences

The issue identifies several discrepancies between the original `lerobot/smolvla_base` and the LIBERO-specific checkpoint:

**VLM Model Selection:**
- Base model uses "HuggingFaceTB/SmolVLM2-500M-Video-Instruct"
- LIBERO version uses "HuggingFaceTB/SmolVLM2-500M-Instruct"

**Critical Layer Configuration Mismatch:**

The most significant concern involves VLM layer count. According to the issue, the LIBERO config sets `"num_vlm_layers": 0`, but "it becomes 32 when model is initialized." This contrasts with the base model's 16 layers, diverging from the paper's specification of using "half of them (16 layers)."

**Additional Parameter Changes:**
- `pad_language_to`: Changed from "max_length" to "longest"
- `num_expert_layers`: Modified from 0 to -1
- `expert_width_multiplier`: Reduced from 0.75 to 0.5

## Outstanding Questions

The issue reporter requests the original model checkpoint and training recipe to verify LIBERO benchmark reproducibility, noting the configuration inconsistencies prevent accurate replication of published results. No resolution or response from maintainers is visible in the provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T00:25:31.971478+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress -maxdepth 2 -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress -maxdepth 2 -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T00:25:31.971628+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/imm/__init__.py\\n/root/autodl-tmp/importance_margin_vla_compress/imm/acis.py\\n/root/autodl-tmp/importance_margin_vla_compress/imm/soft_topk.py\\n/root/autodl-tmp/importance_margin_vla_compress/imm/losses.py\\n/root/autodl-tmp/importance_margin_vla_compress/imm/metrics.py\\n/root/autodl-tmp/importance_margin_vla_compress/imm/token_selection.py\\n/root/autodl-tmp/importance_margin_vla_compress/imm/smolvla_wrapper.py\\n/root/autodl-tmp/importance_margin_vla_compress/train.py\\n/root/autodl-tmp/importance_margin_vla_compress/evaluate.py\\n/root/autodl-tmp/importance_margin_vla_compress/_lerobot_compat.py\\n/root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py\\n/root/autodl-tmp/importance_margin_vla_compress/verify_grad_isolation.py\\n/root/autodl-tmp/importance_margin_vla_compress/train_twostage.py\\n/root/autodl-tmp/importance_margin_vla_compress/scripts/analyze_margin_distribution.py\\n/root/autodl-tmp/importance_margin_vla_compress/scripts/eval_checkpoint_trajectory.py\\n/root/autodl-tmp/importance_margin_vla_compress/scripts/analyze_keep_ratio_sensitivity.py\\n/root/autodl-tmp/importance_margin_vla_compress/scripts/visualize_token_importance.py\\n/root/autodl-tmp/importance_margin_vla_compress/scripts/plot_checkpoint_trajectory.py\\n/root/autodl-tmp/importance_margin_vla_compress/scripts/test_action_diversity_by_step.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_sim.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_success_rate.py\\n/root/autodl-tmp/importance_margin_vla_compress/test_mode_collapse.py\\n/root/autodl-tmp/importance_margin_vla_compress/test_inference_fixes.py\\n/root/autodl-tmp/importance_margin_vla_compress/scan_collapse.py\\n/root/autodl-tmp/importance_margin_vla_compress/test_pretrained_sim.py\\n/root/autodl-tmp/importance_margin_vla_compress/diag_ep42.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_form
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T00:25:31.971771+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "ls /root/autodl-tmp/importance_margin_vla_compress/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "ls /root/autodl-tmp/importance_margin_vla_compress/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T00:25:31.971924+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\n_lerobot_compat.py\\nanalyze_gate.py\\nartifacts\\ncheckpoints\\nconfigs\\ndiag_ep42.py\\neval_acis_overhead.py\\neval_formal_bound.py\\neval_pruning_sweep.py\\neval_pruning_sweep.py.bak\\neval_results\\neval_seed0_100k_all.log\\neval_seed0_object.log\\neval_sim.py\\neval_success_rate.py\\neval_success_rate.py.bak\\neval_success_rate_libero.py\\neval_token_importance.py\\nevaluate.py\\nevaluate.py.bak\\nevaluate.py.bak2\\nevaluate.py.bak_pre_d028\\ngen_figures.py\\nimm\\nlogs\\nresults\\nrun_d014_eval.sh\\nrun_eval_v8_fixed.sh\\nrun_mvp.sh\\nrun_traj_28k_30k_v2.sh\\nrun_traj_eval_28k_30k.sh\\nrun_traj_eval_补跑.sh\\nrun_v8_1_final_eval.sh\\nrun_v8_final_eval.sh\\nrun_v8b_final_eval.sh\\nrun_v8c_final_eval.sh\\nscan_collapse.py\\nscripts\\ntest_inference_fixes.py\\ntest_mode_collapse.py\\ntest_pretrained_sim.py\\ntrain.py\\ntrain_twostage.py\\ntrain_twostage.py.bak\\nverify_grad_isolation.py\\nwandb\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T00:25:31.972084+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github huggingface lerobot smolvla action normalization dataset stats libero normalize_inputs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github huggingface lerobot smolvla action normalization dataset stats libero normalize_inputs"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T00:25:31.972304+00:00_

Web search results for query: "github huggingface lerobot smolvla action normalization dataset stats libero normalize_inputs"

Links: [{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"SmolVLA have poor performance · Issue #1370 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1370"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"Details of adapting SmolVLA to other robotic arms with different configurations · Issue #2351 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2351"},{"title":"lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"Releases · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/releases"}]

I found relevant search results about LeRobot's SmolVLA policy, action normalization, and LIBERO dataset. Here's a summary of the key information:

## SmolVLA and Action Normalization

SmolVLA is Hugging Face's lightweight foundation model for robotics, designed for easy fine-tuning on LeRobot datasets. SmolVLA-450M outperforms much larger VLAs and strong baselines such as ACT on simulation (LIBERO, Meta-World) and real-world tasks (SO100, SO101).

## Normalization and Dataset Stats

When working with action normalization in LeRobot, naming keys are encoded inside the normalization statistics layer, and if your data contai
…[truncated 1021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T00:25:31.972480+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "head -150 /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "head -150 /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T00:25:31.972688+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"IMM Training Pipeline for SmolVLA + LIBERO.\\n\\nUsage:\\n    python train.py --config configs/baseline.yaml\\n    python train.py --config configs/imm_anchor.yaml\\n    python train.py --config configs/imm_anchor.yaml --resume checkpoints/imm_anchor/latest\\n\\nTwo modes:\\n  - Baseline: L_action only (flow matching MSE), no ACIS/margin loss.\\n  - IMM: L_action + lambda * L_margin with ACIS scoring + token selection + warmup.\\n\\nDepends: lerobot, torch, wandb, peft.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport copy\\nimport json\\nimport logging\\nimport os\\nimport signal\\nimport sys\\nimport time\\nfrom pathlib import Path\\nfrom typing import Any, Dict, Optional\\n\\nimport torch\\nimport torch.nn.functional as F\\nimport wandb\\nimport yaml\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\n\\n\\ndef parse_args():\\n    parser = argparse.ArgumentParser(description=\\\"IMM training for SmolVLA on LIBERO\\\")\\n    parser.add_argument(\\\"--config\\\", type=str, required=True, help=\\\"Path to YAML config file\\\")\\n    parser.add_argument(\\\"--resume\\\", type=str, default=None, help=\\\"Path to checkpoint dir to resume from\\\")\\n    parser.add_argument(\\\"--gpu\\\", type=int, default=0, help=\\\"GPU index (use CUDA_VISIBLE_DEVICES for physical mapping)\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--wandb_project\\\", type=str, default=\\\"imm-vla-compress\\\", help=\\\"W&B project name\\\")\\n    parser.add_argument(\\\"--wandb_run\\\", type=str, default=None, help=\\\"W&B run name (auto-generated if None)\\\")\\n    return parser.parse_args()\\n\\n\\ndef load_config(confi
…[truncated 4023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T00:25:31.972843+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"normalize\\|normalization\\|action_norm\\|unnormalize\\|dataset_stats\\|norm_stats\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"normalize\\|normalization\\|action_norm\\|unnormalize\\|dataset_stats\\|norm_stats\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T00:25:31.972973+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T00:25:31.973099+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"normalize\\|normalization\\|action_norm\\|unnormalize\\|dataset_stats\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"normalize\\|normalization\\|action_norm\\|unnormalize\\|dataset_stats\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T00:25:31.973351+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T00:25:31.973499+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"batch_size\\|warmup\\|scheduler\\|cosine\\|lr_schedule\\|learning_rate\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"batch_size\\|warmup\\|scheduler\\|cosine\\|lr_schedule\\|learning_rate\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T00:25:31.973627+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T00:25:31.973749+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"normalize\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"normalize\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-17T00:25:31.973882+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-17T00:25:31.974002+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"normalize\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"normalize\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-17T00:25:31.974124+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T00:25:31.974527+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"batch_size\\|warmup\\|scheduler\\|cosine\\|lr_schedule\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"batch_size\\|warmup\\|scheduler\\|cosine\\|lr_schedule\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T00:25:31.974717+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T00:25:31.974847+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"image_shape\\|image_size\\|resize\\|resolution\\|256\\|512\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"image_shape\\|image_size\\|resize\\|resolution\\|256\\|512\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T00:25:31.974977+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-17T00:25:31.975098+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"batch_size\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"batch_size\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T00:25:31.975250+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"221:        batch_size=train_cfg.get(\\\"batch_size\\\", 4),\\n609:    eval_dataloader = make_dataloader(eval_dataset, {**config, \\\"training\\\": {**train_cfg, \\\"batch_size\\\": train_cfg.get(\\\"eval_batch_size\\\", train_cfg.get(\\\"batch_size\\\", 4))}})\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T00:25:31.975371+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"warmup\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"warmup\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-17T00:25:31.975511+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"10:  - IMM: L_action + lambda * L_margin with ACIS scoring + token selection + warmup.\\n244:    warmup_steps = train_cfg.get(\\\"warmup_steps\\\", 1000)\\n248:    warmup = LinearLR(optimizer, start_factor=1e-8, end_factor=1.0, total_iters=warmup_steps)\\n249:    cosine = CosineAnnealingLR(optimizer, T_max=total_steps - warmup_steps, eta_min=decay_lr)\\n250:    return SequentialLR(optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps])\\n331:    warmup_steps = schedule.get(\\\"warmup_steps\\\", 0)\\n334:    if step < warmup_steps:\\n337:    anneal_progress = min(1.0, (step - warmup_steps) / anneal_steps)\\n360:        \\\"warmup_steps\\\": imm_cfg.get(\\\"warmup_steps\\\", 1000),\\n597:            \\\"warmup_steps\\\": ts_cfg.get(\\\"stage1_warmup_steps\\\", 500),\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T00:25:31.975639+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"cosine\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"cosine\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-17T00:25:31.975755+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"image_shape\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"image_shape\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-17T00:25:31.975897+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"249:    cosine = CosineAnnealingLR(optimizer, T_max=total_steps - warmup_steps, eta_min=decay_lr)\\n250:    return SequentialLR(optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps])\\n340:    if sched_type == \\\"cosine\\\":\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T00:25:31.976035+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"118:        image_shape = tuple(features.get(\\\"image_shape\\\", (3, 256, 256)))\\n127:                type=FeatureType.VISUAL, shape=image_shape\\n129:        log.info(\\\"Updated cameras: %s -> %s (shape=%s)\\\", old_cam_keys, cameras, image_shape)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T00:25:31.976173+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"image_shape\" /root/autodl-tmp/importance_margin_vla_compress/configs/libero_baseline.yaml",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"image_shape\" /root/autodl-tmp/importance_margin_vla_compress/configs/libero_baseline.yaml",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T00:25:31.976303+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-17T00:25:31.976419+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "head -80 /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "head -80 /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-17T00:25:31.976585+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO Success Rate Evaluation for SmolVLA / IMM models.\\n\\nEvaluates per-task and overall success rate on LIBERO benchmark suites.\\n\\nUsage:\\n    python eval_success_rate_libero.py \\\\\\n        --checkpoint checkpoints/libero_full_ft/step_025000/checkpoint.pt \\\\\\n        --config configs/libero_baseline.yaml \\\\\\n        --suite libero_object \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n    \\\"libero_90\\\": 400,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"LIBERO success rate evaluation\\\")\\n    p.add_argument(\\\"--checkpoint\\\", type=str, required=True,\\n                   help=\\\"Path to checkpoint.pt\\\")\\n    p.add_argument(\\\"--config\\\", type=str, default=\\\"configs/libero_baseline.yaml\\\",\\n                   help=\\\"Path to YAML config\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\",\\n                   choices=list(SUITE_MAX_STEPS.keys()),\\n                   help=\\\"LIBERO suite name\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=i
…[truncated 1219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-17T00:25:31.976740+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"max_steps\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -rn \"max_steps\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-17T00:25:31.976873+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"66:    p.add_argument(\\\"--max_steps\\\", type=int, default=None,\\n249:    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 400)\\n253:             args.suite, device, args.mode, args.num_episodes, max_steps)\\n332:            for step in range(max_steps):\\n413:        \\\"max_steps\\\": max_steps,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-17T00:25:31.976996+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/libero",
  "prompt": "Extract the official lerobot LIBERO training command for SmolVLA, especially batch size, steps, learning rate, any action normalization settings, image resolution, and evaluation protocol (max_steps per suite, episodes). Look for any mention of dataset statistics or normalization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/docs/lerobot/libero",
    "prompt": "Extract the official lerobot LIBERO training command for SmolVLA, especially batch size, steps, learning rate, any action normalization settings, image resolution, and evaluation protocol (max_steps per suite, episodes). Look for any mention of dataset statistics or normalization."
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-17T00:25:31.977209+00:00_

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
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-17T00:25:31.977426+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_seed0_object.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_seed0_object.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-17T00:25:31.977595+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 06:56:05 [INFO] Suite: libero_object | Device: cuda:0 | Mode: baseline | Episodes/task: 50 | Max steps: 280\\n2026-05-17 06:56:05 [INFO] Loading model from checkpoints/libero_full_ft_seed0_100k/checkpoint.pt ...\\n2026-05-17 06:56:19 [INFO] Updated state feature shape: (6,) -> (8,)\\n2026-05-17 06:56:19 [INFO] Updated action feature shape: (6,) -> (7,)\\n2026-05-17 06:56:19 [INFO] Updated cameras: ['observation.images.camera1', 'observation.images.camera2', 'observation.images.camera3'] -> ['observation.images.image', 'observation.images.image2'] (shape=(3, 256, 256))\\n2026-05-17 06:56:19 [INFO] LoRA applied: rank=32, alpha=16, trainable params: 1485312\\n2026-05-17 06:56:19 [INFO] Model loaded in 14.8s\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-17 06:56:19 [WARNING] No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-17 06:56:19 [WARNING] It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-17 06:56:19 [WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-17 06:56:20 [INFO] No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n2026-05-17 06:56:20 [INFO] Suite 'libero_object' has 10 tasks, evaluating 10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-17 06:56:20 [INFO] --- Task 0: pick up the alphabet soup and place it in the basket ---\\n2026-05-17 06:56:28 [INFO]   Ep 1/50 | FAIL | steps=280\\n2026-05-17 06:56:33 [INFO]   Ep 2/50 | FAIL | steps=280\\n2026-05-17 06:56:38 [INFO]   Ep 3/50 | FAIL | steps=280\\n2026-05-17 06:56:43 [INFO]   Ep 4/50 | FAIL | steps=280\\n2026-05-17 06:56:48 [INFO]   Ep 5/50 | FAIL | steps=280\\n2026-05-17 06:56:53 [INFO]   Ep 6/50 | FAIL | steps=2
…[truncated 1109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-17T00:25:31.977743+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"lora\" /root/autodl-tmp/importance_margin_vla_compress/configs/libero_baseline.yaml",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -rn \"lora\" /root/autodl-tmp/importance_margin_vla_compress/configs/libero_baseline.yaml",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-17T00:25:31.977878+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"13:  lora:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-17T00:25:31.978008+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"train_expert_only\" /root/autodl-tmp/importance_margin_vla_compress/configs/libero_baseline.yaml",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"train_expert_only\" /root/autodl-tmp/importance_margin_vla_compress/configs/libero_baseline.yaml",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-17T00:25:31.978157+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"7:# Training: lerobot-train uses policy.type=smolvla with train_expert_only=True\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-17T00:25:31.978354+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -200 /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "tail -200 /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-17T00:25:31.978573+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    return actions[0, :, :original_action_dim]  # (chunk_size, action_dim)\\n\\n\\n# --- Statistics ---------------------------------------------------------------\\n\\ndef wilson_ci(successes: int, total: int, z: float = 1.96):\\n    if total == 0:\\n        return 0.0, 0.0, 1.0\\n    p = successes / total\\n    denom = 1 + z ** 2 / total\\n    center = (p + z ** 2 / (2 * total)) / denom\\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\\n    return center, max(0.0, center - spread), min(1.0, center + spread)\\n\\n\\n# --- Main ---------------------------------------------------------------------\\n\\ndef run_evaluation(args):\\n    device = torch.device(f\\\"cuda:{args.gpu}\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 400)\\n    output_path = Path(args.output or f\\\"eval_results/libero_{args.suite}.json\\\")\\n\\n    log.info(\\\"Suite: %s | Device: %s | Mode: %s | Episodes/task: %d | Max steps: %d\\\",\\n             args.suite, device, args.mode, args.num_episodes, max_steps)\\n\\n    np.random.seed(args.seed)\\n    torch.manual_seed(args.seed)\\n\\n    # Load model\\n    log.info(\\\"Loading model from %s ...\\\", args.checkpoint)\\n    t0 = time_mod.time()\\n    policy, wrapper, config = load_model(args, device)\\n    log.info(\\\"Model loaded in %.1fs\\\", time_mod.time() - t0)\\n\\n    from train import get_tokenizer_from_policy\\n    tokenizer = get_tokenizer_from_policy(policy)\\n\\n    ds_cfg = config.get(\\\"dataset\\\", {})\\n    camera_keys = ds_cfg.get(\\\"features\\\", {}).get(\\\"cameras\\\", [\\n        \\\"observation.images.image\\\", \\\"observation.images.image2\\\"\\n    ])\\n\\n    connector = None\\n    if args.mode == \\\"acis_prune\\\":\\n        connector = find_connector(policy.model)\\n        if connector is None:\\n            raise RuntimeError(\\\"Cannot find connector for 
…[truncated 5972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-17T00:25:31.978788+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "head -250 /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "head -250 /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-17T00:25:31.979213+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO Success Rate Evaluation for SmolVLA / IMM models.\\n\\nEvaluates per-task and overall success rate on LIBERO benchmark suites.\\n\\nUsage:\\n    python eval_success_rate_libero.py \\\\\\n        --checkpoint checkpoints/libero_full_ft/step_025000/checkpoint.pt \\\\\\n        --config configs/libero_baseline.yaml \\\\\\n        --suite libero_object \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n    \\\"libero_90\\\": 400,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"LIBERO success rate evaluation\\\")\\n    p.add_argument(\\\"--checkpoint\\\", type=str, required=True,\\n                   help=\\\"Path to checkpoint.pt\\\")\\n    p.add_argument(\\\"--config\\\", type=str, default=\\\"configs/libero_baseline.yaml\\\",\\n                   help=\\\"Path to YAML config\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\",\\n                   choices=list(SUITE_MAX_STEPS.keys()),\\n                   help=\\\"LIBERO suite name\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=i
…[truncated 7096 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-17T00:25:31.979556+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "ls /root/autodl-tmp/importance_margin_vla_compress/eval_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "ls /root/autodl-tmp/importance_margin_vla_compress/eval_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-17T00:25:31.979796+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"action_diversity_by_step.json\\neval_baseline_v5_bypass_acis.json\\neval_baseline_v5_final.json\\neval_baseline_v5_fixed.json\\neval_baseline_v5_step10000.json\\neval_baseline_v5_step5000.json\\neval_imm_v7_2_bypass_acis.json\\neval_imm_v7_2_final.json\\neval_imm_v7_2_step010000.json\\neval_imm_v7_2_step020000.json\\neval_imm_v7_final.json\\neval_imm_v8_1_acis_prune.json\\neval_imm_v8_1_bypass.json\\neval_imm_v8_1_standard.json\\neval_imm_v8_bypass_final.json\\neval_imm_v8_bypass_fixed.json\\neval_imm_v8_final.json\\neval_imm_v8_final_30k.json\\neval_imm_v8_fixed.json\\neval_imm_v8_step002000.json\\neval_imm_v8_step002000_bypass.json\\neval_imm_v8b_acis_prune.json\\neval_imm_v8b_bypass.json\\neval_imm_v8b_standard.json\\neval_imm_v8c_acis_prune.json\\neval_imm_v8c_bypass.json\\neval_imm_v8c_standard.json\\nfull_ft_100k_libero_object_formal.json\\nfull_ft_seed0_100k_libero_object.json\\nfull_ft_seed0_100k_libero_spatial.json\\ngate_report.json\\ngate_report_v7_2.json\\ngate_report_v8_1_final.json\\ngate_report_v8_final.json\\ngate_report_v8_step2k.json\\ngate_report_v8b_final.json\\ngate_report_v8c_final.json\\nimm_v2_fullft_libero_object.json\\nimm_v2_fullft_libero_object.log\\nlerobot_eval_investigation.md\\nlibero_libero_goal.json\\nlibero_libero_object.json\\nlibero_libero_spatial.json\\nofficial_eval_final_report.md\\npruning_sweep.json\\npruning_sweep_v2.json\\npruning_sweep_v2.log\\nsim_rollout_diagnosis.md\\nsim_success_rate.json\\nsuccess_rate.json\\ntemp08_success_rate.json\\ntrajectory\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-17T00:25:31.980014+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"action_horizon\\|n_action_steps\\|action_steps\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"action_horizon\\|n_action_steps\\|action_steps\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-17T00:25:31.980231+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-17T00:25:31.980421+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/full_ft_seed0_100k_libero_object.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/full_ft_seed0_100k_libero_object.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-17T00:25:31.980687+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"mode\\\": \\\"baseline\\\",\\n  \\\"checkpoint\\\": \\\"checkpoints/libero_full_ft_seed0_100k/checkpoint.pt\\\",\\n  \\\"config\\\": \\\"configs/libero_full_ft.yaml\\\",\\n  \\\"total_episodes\\\": 500,\\n  \\\"total_successes\\\": 255,\\n  \\\"overall_success_rate\\\": 0.51,\\n  \\\"wilson_ci_95\\\": [\\n    0.4663,\\n    0.5536\\n  ],\\n  \\\"num_episodes_per_task\\\": 50,\\n  \\\"max_steps\\\": 280,\\n  \\\"action_horizon\\\": 50,\\n  \\\"seed\\\": 42,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the alphabet soup and place it in the basket\\\",\\n      \\\"success_count\\\": 2,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.04,\\n      \\\"mean_steps\\\": 274.0\\n    },\\n    \\\"1\\\": {\\n      \\\"task_id\\\": 1,\\n      \\\"task_description\\\": \\\"pick up the cream cheese and place it in the basket\\\",\\n      \\\"success_count\\\": 37,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.74,\\n      \\\"mean_steps\\\": 161.1\\n    },\\n    \\\"2\\\": {\\n      \\\"task_id\\\": 2,\\n      \\\"task_description\\\": \\\"pick up the salad dressing and place it in the basket\\\",\\n      \\\"success_count\\\": 28,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.56,\\n      \\\"mean_steps\\\": 185.6\\n    },\\n    \\\"3\\\": {\\n      \\\"task_id\\\": 3,\\n      \\\"task_description\\\": \\\"pick up the bbq sauce and place it in the basket\\\",\\n      \\\"success_count\\\": 34,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.68,\\n      \\\"mean_steps\\\": 174.2\\n    },\\n    \\\"4\\\": {\\n      \\\"task_id\\\": 4,\\n      \\\"task_description\\\": \\\"pick up the ketchup and place it in the basket\\\",\\n      \\\"success_count\\\": 27,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.5
…[truncated 1606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-17T00:25:31.980917+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/full_ft_100k_libero_object_formal.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/full_ft_100k_libero_object_formal.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-17T00:25:31.981220+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"mode\\\": \\\"baseline\\\",\\n  \\\"checkpoint\\\": \\\"checkpoints/libero_full_ft_100k/checkpoint.pt\\\",\\n  \\\"config\\\": \\\"configs/libero_full_ft.yaml\\\",\\n  \\\"total_episodes\\\": 500,\\n  \\\"total_successes\\\": 224,\\n  \\\"overall_success_rate\\\": 0.448,\\n  \\\"wilson_ci_95\\\": [\\n    0.405,\\n    0.4918\\n  ],\\n  \\\"num_episodes_per_task\\\": 50,\\n  \\\"max_steps\\\": 280,\\n  \\\"action_horizon\\\": 50,\\n  \\\"seed\\\": 42,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the alphabet soup and place it in the basket\\\",\\n      \\\"success_count\\\": 1,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.02,\\n      \\\"mean_steps\\\": 277.2\\n    },\\n    \\\"1\\\": {\\n      \\\"task_id\\\": 1,\\n      \\\"task_description\\\": \\\"pick up the cream cheese and place it in the basket\\\",\\n      \\\"success_count\\\": 23,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.46,\\n      \\\"mean_steps\\\": 207.4\\n    },\\n    \\\"2\\\": {\\n      \\\"task_id\\\": 2,\\n      \\\"task_description\\\": \\\"pick up the salad dressing and place it in the basket\\\",\\n      \\\"success_count\\\": 31,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.62,\\n      \\\"mean_steps\\\": 177.3\\n    },\\n    \\\"3\\\": {\\n      \\\"task_id\\\": 3,\\n      \\\"task_description\\\": \\\"pick up the bbq sauce and place it in the basket\\\",\\n      \\\"success_count\\\": 37,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.74,\\n      \\\"mean_steps\\\": 161.5\\n    },\\n    \\\"4\\\": {\\n      \\\"task_id\\\": 4,\\n      \\\"task_description\\\": \\\"pick up the ketchup and place it in the basket\\\",\\n      \\\"success_count\\\": 30,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.6,\\n  
…[truncated 1602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-17T00:25:31.981545+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"chunk_size\\|n_action_steps\\|action_horizon\" /root/autodl-tmp/importance_margin_vla_compress/imm/smolvla_wrapper.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -rn \"chunk_size\\|n_action_steps\\|action_horizon\" /root/autodl-tmp/importance_margin_vla_compress/imm/smolvla_wrapper.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-17T00:25:31.981750+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-17T00:25:31.981911+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot SmolVLA n_action_steps chunk_size default action execution steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot SmolVLA n_action_steps chunk_size default action execution steps"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-17T00:25:31.982040+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"chunk_size\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"chunk_size\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-17T00:25:31.982231+00:00_

Web search results for query: "lerobot SmolVLA n_action_steps chunk_size default action execution steps"

Links: [{"title":"Asynchronous Inference · Hugging Face","url":"https://huggingface.co/docs/lerobot/async"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"VLA (2) SmolVLA, ACT — XLeRobot 0.3.0 documentation","url":"https://xlerobot.readthedocs.io/en/latest/software/getting_started/VLA_smol.html"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"Real-Time Chunking (RTC) · Hugging Face","url":"https://huggingface.co/docs/lerobot/rtc"},{"title":"`smolvla_base training`: `Expected all tensors to be on the same device` · Issue #1377 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1377"},{"title":"config.json · lerobot/smolvla_base at 04d96c1f9167360280aaa54de31418f824d1ef48","url":"https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json"},{"title":"Evaluation of Policies on Libero · Issue #2731 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2731"},{"title":"SmolVLA: compact VLA for robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/smolvla-compact-vla-for-robot-policy-b30604ac23c5"}]

Based on the search results, I found relevant information about SmolVLA parameters and action execution:

The default value for `n_action_steps` in SmolVLA is 50, which represents the number of action steps in each action chunk that the model predicts.

Regarding the asynchronous inference parameters, the default values of `actions_per_chunk` and `chunk_size_threshold` were found to work well in the experiments developed for the SmolVLA paper, though specific numeric defaults aren't explicitly stated in the available d
…[truncated 758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-17T00:25:31.982412+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"202:    chunk_size = 50  # SmolVLA default\\n205:    delta_timestamps = {\\\"action\\\": [i / meta.fps for i in range(chunk_size)]}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-17T00:25:31.982546+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json",
  "prompt": "Extract all configuration parameters: chunk_size, n_action_steps, image resolution, normalization settings, action_dim, state_dim, num_vlm_layers, expert layers, any learning rate or training parameters mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json",
    "prompt": "Extract all configuration parameters: chunk_size, n_action_steps, image resolution, normalization settings, action_dim, state_dim, num_vlm_layers, expert layers, any learning rate or training parameters mentioned."
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-17T00:25:31.982674+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/2731",
  "prompt": "Extract what action_steps / n_action_steps people use for LIBERO evaluation with SmolVLA. What is the recommended value? Any mention of action_horizon and its impact on success rate?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/huggingface/lerobot/issues/2731",
    "prompt": "Extract what action_steps / n_action_steps people use for LIBERO evaluation with SmolVLA. What is the recommended value? Any mention of action_horizon and its impact on success rate?"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-17T00:25:31.982812+00:00_

# SmoLVLA Base Configuration Parameters

## Core Architecture Parameters
- **chunk_size**: 50
- **n_action_steps**: 50
- **n_obs_steps**: 1
- **num_vlm_layers**: 16
- **num_expert_layers**: 0
- **self_attn_every_n_layers**: 2
- **expert_width_multiplier**: 0.75

## Dimension Parameters
- **max_state_dim**: 32
- **max_action_dim**: 32
- **action shape**: [6]
- **state shape**: [6]

## Image Processing
- **image resolution**: 3 channels × 256×256 (for input images)
- **resize_imgs_with_padding**: [512, 512]
- **num_cameras**: 3 (image, image2, image3)
- **empty_cameras**: 0

## Normalization Settings
```json
{
  "VISUAL": "IDENTITY",
  "STATE": "MEAN_STD",
  "ACTION": "MEAN_STD"
}
```

## Optimizer Configuration
- **optimizer_lr**: 0.0001
- **optimizer_betas**: [0.9, 0.95]
- **optimizer_eps**: 1e-08
- **optimizer_weight_decay**: 1e-10
- **optimizer_grad_clip_norm**: 10

## Scheduler Configuration
- **scheduler_warmup_steps**: 1000
- **scheduler_decay_steps**: 30000
- **scheduler_decay_lr**: 2.5e-06

## Training Parameters
- **freeze_vision_encoder**: true
- **train_expert_only**: true
- **train_state_proj**: true
- **load_vlm_weights**: true
- **use_cache**: true

## VLM Settings
- **vlm_model_name**: HuggingFaceTB/SmolVLM2-500M-Video-Instruct
- **tokenizer_max_length**: 48
- **num_steps**: 10
- **attention_mode**: cross_attn
- **prefix_length**: 0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-17T00:25:31.982958+00:00_

# SmolVLA LIBERO Evaluation: Action Steps Analysis

Based on the provided GitHub issue content, there is **no discussion or recommendation regarding action_steps/n_action_steps values for LIBERO evaluation with SmolVLA**.

The issue documents a feature mismatch error encountered during evaluation, where the policy configuration specifies `'n_action_steps': 50` but does not address optimal values or their impact on performance.

## Key Observation

The configuration shown includes: `'n_action_steps': 50` and `'chunk_size': 50`, but the issue focuses entirely on resolving camera name mismatches between the dataset and environment rather than exploring action step parameters.

**No mention of action_horizon or its impact on success rates appears in this issue.**

The user's problem stems from incompatible feature names (`observation.images.image` vs. the expected `observation.images.top/wrist`), not from action step configuration concerns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-17T00:25:31.983194+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"dataset_stats\\|norm_stats\\|normalize_stat\\|NormalizeTransform\\|normalize_inputs\\|unnormalize\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"dataset_stats\\|norm_stats\\|normalize_stat\\|NormalizeTransform\\|normalize_inputs\\|unnormalize\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-17T00:25:31.983373+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-17T00:25:31.983504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/_lerobot_compat.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/_lerobot_compat.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-17T00:25:31.983648+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compatibility shim for lerobot 0.5.x API changes.\\n\\nlerobot 0.5.x moved from lerobot.common.{policies,datasets} to\\nlerobot.{policies,datasets}. The policies __init__ has a groot dataclass\\nbug on Python 3.12, so we stub it out before importing smolvla.\\n\\\"\\\"\\\"\\nimport sys\\nimport types\\n\\ndef _patch_lerobot_policies():\\n    key = \\\"lerobot.policies\\\"\\n    if key not in sys.modules or isinstance(sys.modules[key], types.ModuleType):\\n        try:\\n            import lerobot.policies\\n        except (TypeError, ImportError):\\n            import lerobot\\n            stub = types.ModuleType(key)\\n            stub.__path__ = [p + \\\"/policies\\\" for p in lerobot.__path__]\\n            stub.__package__ = key\\n            sys.modules[key] = stub\\n\\n            smolvla_key = \\\"lerobot.policies.smolvla\\\"\\n            if smolvla_key not in sys.modules:\\n                smolvla_stub = types.ModuleType(smolvla_key)\\n                smolvla_stub.__path__ = [p + \\\"/smolvla\\\" for sp in stub.__path__ for p in [sp]]\\n                smolvla_stub.__package__ = smolvla_key\\n                sys.modules[smolvla_key] = smolvla_stub\\n\\n_patch_lerobot_policies()\\n\\nfrom lerobot.policies.smolvla.configuration_smolvla import SmolVLAConfig\\nfrom lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy\\nfrom lerobot.datasets import LeRobotDataset\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-17T00:25:31.983789+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"dataset_stats\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"dataset_stats\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-17T00:25:31.983918+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-17T00:25:31.984054+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"normalize\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"normalize\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-17T00:25:31.984204+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-17T00:25:31.984325+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"LeRobotDataset\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"LeRobotDataset\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-17T00:25:31.984451+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"197:    from lerobot.datasets.lerobot_dataset import LeRobotDataset\\n198:    from lerobot.datasets.dataset_metadata import LeRobotDatasetMetadata\\n204:    meta = LeRobotDatasetMetadata(repo_id)\\n207:    dataset = LeRobotDataset(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-17T00:25:31.984577+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "head -230 /root/autodl-tmp/importance_margin_vla_compress/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "head -230 /root/autodl-tmp/importance_margin_vla_compress/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-17T00:25:31.984841+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"IMM Training Pipeline for SmolVLA + LIBERO.\\n\\nUsage:\\n    python train.py --config configs/baseline.yaml\\n    python train.py --config configs/imm_anchor.yaml\\n    python train.py --config configs/imm_anchor.yaml --resume checkpoints/imm_anchor/latest\\n\\nTwo modes:\\n  - Baseline: L_action only (flow matching MSE), no ACIS/margin loss.\\n  - IMM: L_action + lambda * L_margin with ACIS scoring + token selection + warmup.\\n\\nDepends: lerobot, torch, wandb, peft.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport copy\\nimport json\\nimport logging\\nimport os\\nimport signal\\nimport sys\\nimport time\\nfrom pathlib import Path\\nfrom typing import Any, Dict, Optional\\n\\nimport torch\\nimport torch.nn.functional as F\\nimport wandb\\nimport yaml\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\n\\n\\ndef parse_args():\\n    parser = argparse.ArgumentParser(description=\\\"IMM training for SmolVLA on LIBERO\\\")\\n    parser.add_argument(\\\"--config\\\", type=str, required=True, help=\\\"Path to YAML config file\\\")\\n    parser.add_argument(\\\"--resume\\\", type=str, default=None, help=\\\"Path to checkpoint dir to resume from\\\")\\n    parser.add_argument(\\\"--gpu\\\", type=int, default=0, help=\\\"GPU index (use CUDA_VISIBLE_DEVICES for physical mapping)\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--wandb_project\\\", type=str, default=\\\"imm-vla-compress\\\", help=\\\"W&B project name\\\")\\n    parser.add_argument(\\\"--wandb_run\\\", type=str, default=None, help=\\\"W&B run name (auto-generated if None)\\\")\\n    return parser.parse_args()\\n\\n\\ndef load_config(confi
…[truncated 7157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 111 · 2026-05-17T00:25:31.985107+00:00_

I have all the information needed. Here's the complete analysis:

---

## === 差异分析 ===

| 对比项 | 我们 | SmolVLA 官方 | 差异影响 |
|--------|------|-------------|----------|
| **Batch size** | **4** | **64** | **极高 (16x)** |
| 总样本量 (steps×batch) | 400K | 6.4M | 极高 (16x) |
| 训练步数 | 100K | 100K | 无 |
| 学习率 | 1e-4 | 1e-4 | 无 |
| LR scheduler | cosine | cosine | 无 |
| **Warmup steps** | **1000** | **100** | 低 |
| Decay LR (eta_min) | 2.5e-6 | 2.5e-6 | 无 |
| Optimizer | AdamW β=(0.9,0.95) | AdamW β=(0.9,0.95) | 无 |
| Weight decay | 1e-10 | 1e-10 | 无 |
| Gradient clipping | 10.0 | 10.0 | 无 |
| 图像分辨率 (env render) | 256×256 | 256×256 | 无 |
| 模型内部 resize | 512×512 | 512×512 | 无 |
| Action normalization | MEAN_STD | MEAN_STD | 无 (训练时) |
| State normalization | MEAN_STD | MEAN_STD | 无 (训练时) |
| n_action_steps (eval) | 50 | 50 | 无 |
| 训练模式 | train_expert_only | train_expert_only | 无 |
| 可训练参数 | ~100M | ~100M | 无 |
| Eval episodes/task | 50 | 10 | 无 (更严格) |
| Max steps (Object) | 280 | 280 | 无 |
| 数据集 | HuggingFaceVLA/libero | HuggingFaceVLA/libero | 无 |
| **Eval 归一化处理** | **可能缺 unnormalize** | **lerobot-eval 内置处理** | **中等** |

## === 87.3% 引用来源 ===

- **论文**: [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/html/2506.01844v1)
- **87.3% = 4 个 suite 的平均值** (不是 5 个):
  - Spatial: 90%
  - Object: **96%**
  - Goal: 92%
  - Long (libero_10): 71%
- 评估协议: 10 episodes per task × 10 tasks/suite = 100 episodes/suite
- 模型大小: 0.45B (SmolVLA-base)

对比我们 Object suite: **44.8% (seed=42) / 51.0% (seed=0)** vs 官方 **96%** — 差距 45-51 个百分点。

## === Gap 根因排序 ===

### 1. [最关键] Batch Size: 4 vs 64 (16x 差距)

这是**决定性差异**。

- 我们: 4 × 100K = **400K 样本**
- 官方: 64 × 100K = **6.4M 样本**
- 16x 数据曝光差距，对 10 个 task 并行学习是致命的
- Per-task 分布: 我们每个 task 仅 ~40K 样本，不足以收敛
- 证据: 你的结果中容易 task (cream cheese: 74%, bbq sauce: 68-74%) 部分收敛，难 task (alphabet soup: 2-4%) 完全失败 — 典型的欠训练模式
- GitHub issue [#3287](https://github.com/huggingface/lerobot/issues/3287) 也怀疑官方可能用了多 GPU (4×64=256 effective batch)，但未获官方回复

### 2. [中等] 可能的 Eval 归一化 Bug

你的 eval 脚本 `predict_actions()` 直接调用 `policy.model.sample_actions()`，绕过了 `SmolVLAPolicy` 的 `normalize_inputs()` / `unnormalize_outputs()` 方法。

- 训练时 LeRobotDataset 返回归一化后的 state/action
- Eval 时 `obs_to_batch()` 传入 RAW state（未归一化）
- 模型输出归一化后的 action，直接 clip 到 [-1,1] 使用（未反归一化）
- LIBERO action 本身在 [-1,1]，所以 MEAN_STD 偏移不大，部分 task 仍能工作
- 但对精度要求高的 task（如 alphabet soup），归一化偏移足以导致抓取失败

### 3. [低] Warmup Steps: 1000 vs 100

多浪费 900 步在极低 LR，影响不大但略微减少有效训练量。

### 4. [确认非问题] 其他项

- 图像分辨率: 都是 256→512 (model internal resize)，一致
- Action space, control mode, max_steps: 一致
- train_expert_only: 一致
- n_action_steps=50: 一致 (SmolVLA 默认执行完整 chunk)

## === 建议修复 ===

**优先级 1: Batch Size → 64**
```yaml
training:
  batch_size: 64        # 从 4 改为 64
  # 单 GPU VRAM 不够就用 gradient accumulation:
  # batch_size: 8
  # gradient_accumulation_steps: 8  # effective batch = 64
```

如果单 GPU (24GB) 放不下 batch=64:
- SmolVLA expert-only ~100M params + 2张 256×256 图 → 估计 batch=8~16 可行
- 用 `gradient_accumulation_steps` 补到 effective 64

**优先级 2: 修复 Eval 归一化**
```python
# 替换 predict_actions() 为:
@torch.no_grad()
def predict_actions(policy, batch: dict) -> torch.Tensor:
    # 使用 policy 层级接口，自动处理 normalize/unnormalize
    actions = policy.select_action(batch)
    return actions
```

或者手动加归一化:
```python
# 在 obs_to_batch 中对 state 做 normalize
state_mean = policy.config.normalization_mapping["observation.state"].mean
state_std = policy.config.normalization_mapping["observation.state"].std
state_normalized = (state - state_mean) / state_std

# 对 model output 做 unnormalize
action_mean = policy.config.normalization_mapping["action"].mean
action_std = policy.config.normalization_mapping["action"].std
action_raw = action_normalized * action_std + action_mean
```

**优先级 3: Warmup → 100**
```yaml
training:
  warmup_steps: 100     # 从 1000 改为 100
```

**快速验证建议**: 先只改 batch_size=64 (或 grad_accum 到 effective 64)，保持 100K steps，观察是否能到 80%+。如果 VRAM 限制只能到 batch=16，那需要 400K steps 才能达到同样的总样本量。

Sources:
- [SmolVLA Paper (arxiv)](https://arxiv.org/html/2506.01844v1)
- [GitHub Issue #3287 - Replication Inquiry](https://github.com/huggingface/lerobot/issues/3287)
- [GitHub Issue #2294 - LIBERO Config Discrepancy](https://github.com/huggingface/lerobot/issues/2294)
- [LeRobot LIBERO Docs](https://huggingface.co/docs/lerobot/libero)
- [SmolVLA HuggingFace Docs](https://huggingface.co/docs/lerobot/en/smolvla)
- [smolvla_base config.json](https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_smolvla_libero_gap_deep_dive_20260517T001826"
}
```

</details>

---
