# verify smolvla checkpoint source

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_verify_smolvla-checkpoint-source_20260522T115941.jsonl`
- **Structured JSON:** [`fe3bcd11f439e8303ff0.json`](../../sessions/fe/fe3bcd11f439e8303ff0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-22T12:03:04.562532+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image,WebFetch,WebSearch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image,WebFetch,WebSearch",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T12:03:04.562999+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T12:03:04.563325+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls -la /root/autodl-tmp/models/smolvla_libero/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls -la /root/autodl-tmp/models/smolvla_libero/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T12:03:04.563567+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "head -50 /root/autodl-tmp/models/smolvla_libero/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "head -50 /root/autodl-tmp/models/smolvla_libero/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T12:03:04.563825+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 885516\\ndrwxr-xr-x 3 root root      4096 May 13 20:04 .\\ndrwxr-xr-x 8 root root       186 May 22 13:38 ..\\ndrwxr-xr-x 3 root root        33 May 13 20:00 .cache\\n-rw-r--r-- 1 root root      1519 May 13 20:00 .gitattributes\\n-rw-r--r-- 1 root root      1686 May 13 20:00 README.md\\n-rw-r--r-- 1 root root      2430 May 19 16:01 config.json\\n-rw-r--r-- 1 root root 906712520 May 13 20:04 model.safetensors\\n-rw-r--r-- 1 root root       660 May 13 20:00 policy_postprocessor.json\\n-rw-r--r-- 1 root root      5676 May 13 20:00 policy_postprocessor_step_0_unnormalizer_processor.safetensors\\n-rw-r--r-- 1 root root      2042 May 13 20:00 policy_preprocessor.json\\n-rw-r--r-- 1 root root      5676 May 13 20:00 policy_preprocessor_step_5_normalizer_processor.safetensors\\n-rw-r--r-- 1 root root      9631 May 13 20:00 train_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.14}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T12:03:04.564123+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n    \\\"type\\\": \\\"smolvla\\\",\\n    \\\"n_obs_steps\\\": 1,\\n    \\\"input_features\\\": {\\n        \\\"observation.state\\\": {\\n            \\\"type\\\": \\\"STATE\\\",\\n            \\\"shape\\\": [\\n                6\\n            ]\\n        },\\n        \\\"observation.images.camera1\\\": {\\n            \\\"type\\\": \\\"VISUAL\\\",\\n            \\\"shape\\\": [\\n                3,\\n                256,\\n                256\\n            ]\\n        },\\n        \\\"observation.images.camera2\\\": {\\n            \\\"type\\\": \\\"VISUAL\\\",\\n            \\\"shape\\\": [\\n                3,\\n                256,\\n                256\\n            ]\\n        },\\n        \\\"observation.images.camera3\\\": {\\n            \\\"type\\\": \\\"VISUAL\\\",\\n            \\\"shape\\\": [\\n                3,\\n                256,\\n                256\\n            ]\\n        }\\n    },\\n    \\\"output_features\\\": {\\n        \\\"action\\\": {\\n            \\\"type\\\": \\\"ACTION\\\",\\n            \\\"shape\\\": [\\n                7\\n            ]\\n        }\\n    },\\n    \\\"device\\\": \\\"cuda\\\",\\n    \\\"use_amp\\\": false,\\n    \\\"use_peft\\\": false,\\n    \\\"push_to_hub\\\": true,\\n    \\\"repo_id\\\": \\\"pepijn223/smolvla_libero\\\",\\n    \\\"private\\\": null,\\n    \\\"tags\\\": null,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T12:03:04.564430+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "head -30 /root/autodl-tmp/models/smolvla_libero/README.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "head -30 /root/autodl-tmp/models/smolvla_libero/README.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T12:03:04.564681+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"---\\nbase_model: lerobot/smolvla_base\\ndatasets: lerobot/libero\\nlibrary_name: lerobot\\nlicense: apache-2.0\\nmodel_name: smolvla\\npipeline_tag: robotics\\ntags:\\n- lerobot\\n- robotics\\n- smolvla\\n---\\n\\n# Model Card for smolvla\\n\\n&lt;!-- Provide a quick summary of what the model is/does. -->\\n\\n\\n[SmolVLA](https://huggingface.co/papers/2506.01844) is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware.\\n\\n\\nThis policy has been trained and pushed to the Hub using [LeRobot](https://github.com/huggingface/lerobot).\\nSee the full documentation at [LeRobot Docs](https://huggingface.co/docs/lerobot/index).\\n\\n---\\n\\n## How to Get Started with the Model\\n\\nFor a complete walkthrough, see the [training guide](https://huggingface.co/docs/lerobot/il_robots#train-a-policy).\\nBelow is the short version on how to train and run inference/eval:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T12:03:04.564920+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/autodl-tmp/models/smolvla_libero/.huggingface/download_metadata.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/autodl-tmp/models/smolvla_libero/.huggingface/download_metadata.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T12:03:04.565155+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/models/smolvla_libero/.huggingface/download_metadata.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T12:03:04.565400+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"smolvla\" /root/acr-vla-conformal-refinement/src/smolvla_wrapper.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"smolvla\" /root/acr-vla-conformal-refinement/src/smolvla_wrapper.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T12:03:04.565630+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"24:from lerobot.policies.smolvla.modeling_smolvla import (\\n50:    def __init__(self, pretrained_path: str = \\\"/root/autodl-tmp/models/smolvla_libero/\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T12:03:04.565865+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"smolvla\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"smolvla\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T12:03:04.566109+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"82:    p.add_argument(\\\"--smolvla_path\\\", type=str, default=\\\"/root/autodl-tmp/models/smolvla_libero/\\\")\\n83:    p.add_argument(\\\"--model\\\", type=str, default=\\\"smolvla\\\",\\n84:                   choices=[\\\"smolvla\\\", \\\"pi05\\\", \\\"openvla_oft\\\"],\\n556:        from smolvla_wrapper import SmolVLAWrapper\\n557:        print(f\\\"[eval] Loading SmolVLA from {args.smolvla_path}...\\\")\\n558:        wrapper = SmolVLAWrapper(args.smolvla_path, device=str(device))\\n835:        model_tag = f\\\"_{args.model}\\\" if args.model != \\\"smolvla\\\" else \\\"\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T12:03:04.566394+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero",
  "prompt": "Extract the model card information: who uploaded it, what is the model, what dataset was it trained on, what are the key config details (obs_dim, action_dim, number of tasks), and the download/clone instructions. Is this the official SmolVLA model?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero",
    "prompt": "Extract the model card information: who uploaded it, what is the model, what dataset was it trained on, what are the key config details (obs_dim, action_dim, number of tasks), and the download/clone instructions. Is this the official SmolVLA model?"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T12:03:04.566616+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/pepijn223/smolvla_libero",
  "prompt": "Extract the model card information: who uploaded it, what is the model, what dataset was it trained on, what are the key config details (obs_dim, action_dim, number of tasks), and the download/clone instructions. Does this model exist?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/pepijn223/smolvla_libero",
    "prompt": "Extract the model card information: who uploaded it, what is the model, what dataset was it trained on, what are the key config details (obs_dim, action_dim, number of tasks), and the download/clone instructions. Does this model exist?"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-22T12:03:04.566859+00:00_

# Model Card Information: lerobot/smolvla_libero

## Model Existence
**Yes, this model exists** and is actively maintained on Hugging Face.

## Uploader
- **Organization:** LeRobot (4.11k followers)
- **License:** Apache-2.0

## Model Description
**SmolVLA** is a compact, efficient vision-language-action (VLA) model designed for robotics that:
- Achieves competitive performance at reduced computational costs
- Can be deployed on consumer-grade hardware
- Is trained and distributed via LeRobot framework

**Paper:** [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://huggingface.co/papers/2506.01844) (arxiv: 2506.01844)

## Training Dataset
- **Dataset:** [lerobot/libero](https://huggingface.co/datasets/lerobot/libero)
- **Size:** 273k items, 5.48k downloads
- **Base Model:** [lerobot/smolvla_base](https://huggingface.co/lerobot/smolvla_base)

## Key Config Details
The page does not explicitly list `obs_dim`, `action_dim`, or specific task counts. However:
- **Policy Type:** ACT (Action Chunking Transformer)
- **Training Framework:** LeRobot
- **Downloads/Month:** 6,723

## Download/Clone Instructions

```bash
# Clone LeRobot repository
git clone https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e .[smolvla]

# Train/Finetune
lerobot-train \
  --dataset.repo_id=&lt;HF_USER>/&lt;dataset> \
  --policy.type=act \
  --policy.path=lerobot/smolvla_libero \
  --output_dir=outputs/train/my_smolvla
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T12:03:04.567121+00:00_

# SmolVLA Libero Model Card Summary

## Who Uploaded It
**HuggingFaceVLA** (Hugging Face Vision Language Action Models Research organization)

## What is the Model
**SmolVLA** - A compact, efficient vision-language-action model designed for robotics that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. Published June 2, 2025 (arXiv: 2506.01844).

## Training Dataset
The model card doesn't explicitly specify the training dataset for this particular variant (`smolvla_libero`). However, it's associated with **LIBERO** tasks and can be fine-tuned on datasets like `lerobot/svla_so101_pickplace`.

## Base Model
- **Base Model:** `lerobot/smolvla_base`
- **Status:** Fine-tuned variant

## Key Config Details
The model card does **not provide specific configuration details** like `obs_dim`, `action_dim`, or number of tasks in the excerpt provided.

## Download/Clone Instructions

**Using LeRobot library:**
```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e .[smolvla]
```

**Training:**
```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/&lt;dataset> \
  --policy.path=HuggingFaceVLA/smolvla_libero \
  --batch_size=64 \
  --steps=20000 \
  --policy.device=cuda
```

## Is This Official?
**Yes** - This is the official SmolVLA model released by HuggingFace's VLA research team, available on the Hugging Face Hub with an Apache 2.0 license.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T12:03:04.567472+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "python3 -c \"import json; m=json.load(open('/root/autodl-tmp/crm_cache_v5/object/manifest.json')); print(json.dumps({k:v for k,v in m.items() if 'model' in k.lower() or 'path' in k.lower()}, indent=2))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "python3 -c \"import json; m=json.load(open('/root/autodl-tmp/crm_cache_v5/object/manifest.json')); print(json.dumps({k:v for k,v in m.items() if 'model' in k.lower() or 'path' in k.lower()}, indent=2))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T12:03:04.567711+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T12:03:04.567938+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ps aux | grep -E \"lerobot|smolvla\" | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ps aux | grep -E \"lerobot|smolvla\" | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T12:03:04.568164+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T12:03:04.568424+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/autodl-tmp/models/smolvla_libero/train_config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/autodl-tmp/models/smolvla_libero/train_config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T12:03:04.569029+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n    \\\"dataset\\\": {\\n        \\\"repo_id\\\": \\\"lerobot/libero\\\",\\n        \\\"root\\\": null,\\n        \\\"episodes\\\": null,\\n        \\\"image_transforms\\\": {\\n            \\\"enable\\\": false,\\n            \\\"max_num_transforms\\\": 3,\\n            \\\"random_order\\\": false,\\n            \\\"tfs\\\": {\\n                \\\"brightness\\\": {\\n                    \\\"weight\\\": 1.0,\\n                    \\\"type\\\": \\\"ColorJitter\\\",\\n                    \\\"kwargs\\\": {\\n                        \\\"brightness\\\": [\\n                            0.8,\\n                            1.2\\n                        ]\\n                    }\\n                },\\n                \\\"contrast\\\": {\\n                    \\\"weight\\\": 1.0,\\n                    \\\"type\\\": \\\"ColorJitter\\\",\\n                    \\\"kwargs\\\": {\\n                        \\\"contrast\\\": [\\n                            0.8,\\n                            1.2\\n                        ]\\n                    }\\n                },\\n                \\\"saturation\\\": {\\n                    \\\"weight\\\": 1.0,\\n                    \\\"type\\\": \\\"ColorJitter\\\",\\n                    \\\"kwargs\\\": {\\n                        \\\"saturation\\\": [\\n                            0.5,\\n                            1.5\\n                        ]\\n                    }\\n                },\\n                \\\"hue\\\": {\\n                    \\\"weight\\\": 1.0,\\n                    \\\"type\\\": \\\"ColorJitter\\\",\\n                    \\\"kwargs\\\": {\\n                        \\\"hue\\\": [\\n                            -0.05,\\n                            0.05\\n                        ]\\n                    }\\n                },\\n                \\\"sharpness\\\": {\\n                    \\\"weight\\\": 1.0,\\n                    \\\"type\\\": \\\"SharpnessJitter\\\",\\n
…[truncated 8127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T12:03:04.569332+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/pepijn223/smolvla_libero",
  "prompt": "Does this repo exist? If it redirects, where does it redirect to? List the repo_id, model card info, and any config details visible on the page. Is this the same as HuggingFaceVLA/smolvla_libero or lerobot/smolvla_libero?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/pepijn223/smolvla_libero",
    "prompt": "Does this repo exist? If it redirects, where does it redirect to? List the repo_id, model card info, and any config details visible on the page. Is this the same as HuggingFaceVLA/smolvla_libero or lerobot/smolvla_libero?"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T12:03:04.569588+00:00_

# Repository Information

**Yes, this repo exists.** Based on the web page content, here are the details:

## Repo Identity
- **Repo ID:** `lerobot/smolvla_libero`
- **This is NOT the same as** `HuggingFaceVLA/smolvla_libero` — it belongs to the `lerobot` organization

## Model Card Info
- **Model Name:** SmolVLA (fine-tuned variant)
- **Base Model:** [lerobot/smolvla_base](/lerobot/smolvla_base)
- **License:** apache-2.0
- **Paper:** arxiv: 2506.01844
- **Downloads (last month):** 6,723

## Dataset
- **Training Dataset:** [lerobot/libero](https://huggingface.co/datasets/lerobot/libero)

## Key Details
SmolVLA is described as:
> "a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware."

The model was trained and pushed using the [LeRobot](https://github.com/huggingface/lerobot) framework for robotics applications.

## No Redirect
The page does not indicate any redirect — this is the canonical location for the model.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T12:03:04.569918+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls -la /root/autodl-tmp/models/smolvla_libero/.cache/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls -la /root/autodl-tmp/models/smolvla_libero/.cache/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T12:03:04.570150+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/autodl-tmp/models/smolvla_libero/.cache/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/autodl-tmp/models/smolvla_libero/.cache/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T12:03:04.570405+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x 3 root root   33 May 13 20:00 .\\ndrwxr-xr-x 3 root root 4096 May 13 20:04 ..\\ndrwxr-xr-x 3 root root   76 May 13 20:00 huggingface\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T12:03:04.570632+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-22T12:03:04.570896+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/CACHEDIR.TAG\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/.gitignore\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/policy_postprocessor_step_0_unnormalizer_processor.safetensors.lock\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/model.safetensors.lock\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/.gitattributes.lock\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/policy_postprocessor.json.lock\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/policy_preprocessor.json.lock\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/policy_preprocessor_step_5_normalizer_processor.safetensors.lock\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/README.md.lock\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/config.json.lock\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/policy_preprocessor.json.metadata\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/train_config.json.lock\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/.gitattributes.metadata\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/policy_postprocessor.json.metadata\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/train_config.json.metadata\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/config.json.metadata\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/README.md.metadata\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/policy_preprocessor_step_5_normalizer_processor.safetensors.metadata\\n/root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/policy_postprocessor_step_0_unnormalizer_processor.safetensors.metadata\\n/root/autodl-tmp/models/smolvla_li
…[truncated 166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T12:03:04.571164+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download: Is a directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T12:03:04.571409+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/api/models/HuggingFaceVLA/smolvla_libero",
  "prompt": "Extract the model metadata: repo_id, sha, lastModified, siblings (filenames and sizes), tags, and any config info. I need to compare this model with another version."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/api/models/HuggingFaceVLA/smolvla_libero",
    "prompt": "Extract the model metadata: repo_id, sha, lastModified, siblings (filenames and sizes), tags, and any config info. I need to compare this model with another version."
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-22T12:03:04.571633+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/api/models/lerobot/smolvla_libero",
  "prompt": "Extract the model metadata: repo_id, sha, lastModified, siblings (filenames and sizes), tags, and any config info. I need to compare this model with another version."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/api/models/lerobot/smolvla_libero",
    "prompt": "Extract the model metadata: repo_id, sha, lastModified, siblings (filenames and sizes), tags, and any config info. I need to compare this model with another version."
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-22T12:03:04.571879+00:00_

# Model Metadata Extraction

## Core Metadata

| Field | Value |
|-------|-------|
| **Repo ID** | `HuggingFaceVLA/smolvla_libero` |
| **SHA** | `6721902bc4d61e50a3bfdb11dfb4cb626f05d102` |
| **Last Modified** | `2025-09-17T07:58:34.000Z` |
| **Created** | `2025-09-17T07:53:54.000Z` |
| **Storage** | 1.22 GB |

## Siblings (Files)

| Filename | Purpose |
|----------|---------|
| `.gitattributes` | Git configuration |
| `README.md` | Documentation |
| `config.json` | Model configuration |
| `model.safetensors` | Model weights |
| `policy_postprocessor.json` | Post-processing config |
| `policy_postprocessor_step_1_unnormalizer_processor.safetensors` | Denormalization weights |
| `policy_preprocessor.json` | Pre-processing config |
| `policy_preprocessor_step_5_normalizer_processor.safetensors` | Normalization weights |

## Tags & Configuration

**Tags:** `robotics`, `lerobot`, `smolvla`, `safetensors`, `apache-2.0`

**Card Data:**
```json
{
  "base_model": "lerobot/smolvla_base",
  "datasets": "unknown",
  "library_name": "lerobot",
  "license": "apache-2.0",
  "model_name": "smolvla",
  "pipeline_tag": "robotics"
}
```

## Additional Info

- **Pipeline Tag:** robotics
- **Library:** lerobot
- **Base Model:** `lerobot/smolvla_base`
- **Downloads:** 24,475
- **Likes:** 14
- **Gated:** No
- **Related Space:** HuggingFaceVLA/libero-vla-leaderboard

**Note:** File sizes are not provided in the JSON data. You'll need to query the Hugging Face API or download metadata to get individual file sizes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T12:03:04.572141+00:00_

# Model Metadata Extraction

## Core Information
- **repo_id**: `lerobot/smolvla_libero`
- **sha**: `31d453f7edd78c839a8bbc39744a292686daf0de`
- **lastModified**: `2026-03-24T04:51:22.000Z`
- **createdAt**: `2026-03-24T04:47:06.000Z`

## Siblings (Files)
```
.gitattributes
README.md
config.json
model.safetensors
policy_postprocessor.json
policy_postprocessor_step_0_unnormalizer_processor.safetensors
policy_preprocessor.json
policy_preprocessor_step_5_normalizer_processor.safetensors
train_config.json
```

**Note**: Individual file sizes are not provided in the metadata, but total storage used: `906,718,196 bytes (~907 MB)`

## Tags
```
lerobot, safetensors, robotics, smolvla, 
dataset:lerobot/libero, arxiv:2506.01844,
base_model:lerobot/smolvla_base, license:apache-2.0, region:us
```

## Configuration Info
- **base_model**: `lerobot/smolvla_base`
- **dataset**: `lerobot/libero`
- **library_name**: `lerobot`
- **license**: `apache-2.0`
- **pipeline_tag**: `robotics`
- **model_name**: `smolvla`
- **author**: `lerobot`
- **downloads**: 6,723
- **likes**: 2
- **gated**: false
- **disabled**: false

## For Comparison
To compare with another version, focus on:
1. **SHA hash** - Will differ if any files changed
2. **lastModified** - Check version timestamps
3. **Sibling files** - Compare file lists and architecture changes in config.json and train_config.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T12:03:04.572507+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/model.safetensors.metadata",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/model.safetensors.metadata",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T12:03:04.572747+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"31d453f7edd78c839a8bbc39744a292686daf0de\\n9a9f6413e42c0f332fccbce9a0dc796af2790f82cf002f791cdbf7e01e1afca8\\n1778673860.1380239\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T12:03:04.572969+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/config.json.metadata",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/config.json.metadata",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-22T12:03:04.573187+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/README.md.metadata",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/autodl-tmp/models/smolvla_libero/.cache/huggingface/download/README.md.metadata",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-22T12:03:04.573443+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"31d453f7edd78c839a8bbc39744a292686daf0de\\n3558454eb6a96ae2d7d581b2550e6bd9ca53944f\\n1778673607.9401467\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T12:03:04.573669+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"31d453f7edd78c839a8bbc39744a292686daf0de\\n87293179763b567d75a6c22e2cff007c2ce406eb\\n1778673607.9682748\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T12:03:04.573951+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero/raw/main/config.json",
  "prompt": "Show the full raw JSON content of this config file. I need to see all fields including input_features, output_features, obs_dim, action_dim, vlm_model_name, chunk_size, repo_id, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero/raw/main/config.json",
    "prompt": "Show the full raw JSON content of this config file. I need to see all fields including input_features, output_features, obs_dim, action_dim, vlm_model_name, chunk_size, repo_id, etc."
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-22T12:03:04.574189+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/lerobot/smolvla_libero/raw/main/config.json",
  "prompt": "Show the full raw JSON content of this config file. I need to see all fields including input_features, output_features, obs_dim, action_dim, vlm_model_name, chunk_size, repo_id, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/lerobot/smolvla_libero/raw/main/config.json",
    "prompt": "Show the full raw JSON content of this config file. I need to see all fields including input_features, output_features, obs_dim, action_dim, vlm_model_name, chunk_size, repo_id, etc."
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-22T12:03:04.574515+00:00_

# Full Raw JSON Configuration

Here is the complete configuration file:

```json
{
    "type": "smolvla",
    "n_obs_steps": 1,
    "input_features": {
        "observation.images.image": {
            "type": "VISUAL",
            "shape": [3, 256, 256]
        },
        "observation.images.image2": {
            "type": "VISUAL",
            "shape": [3, 256, 256]
        },
        "observation.state": {
            "type": "STATE",
            "shape": [8]
        }
    },
    "output_features": {
        "action": {
            "type": "ACTION",
            "shape": [7]
        }
    },
    "device": "cuda",
    "use_amp": false,
    "push_to_hub": true,
    "repo_id": "None",
    "private": null,
    "tags": null,
    "license": null,
    "chunk_size": 50,
    "n_action_steps": 1,
    "normalization_mapping": {
        "VISUAL": "IDENTITY",
        "STATE": "MEAN_STD",
        "ACTION": "MEAN_STD"
    },
    "max_state_dim": 32,
    "max_action_dim": 32,
    "resize_imgs_with_padding": [512, 512],
    "empty_cameras": 0,
    "adapt_to_pi_aloha": false,
    "use_delta_joint_actions_aloha": false,
    "tokenizer_max_length": 48,
    "num_steps": 10,
    "use_cache": true,
    "freeze_vision_encoder": true,
    "train_expert_only": true,
    "train_state_proj": true,
    "optimizer_lr": 0.0001,
    "optimizer_betas": [0.9, 0.95],
    "optimizer_eps": 1e-08,
    "optimizer_weight_decay": 1e-10,
    "optimizer_grad_clip_norm": 10,
    "scheduler_warmup_steps": 1000,
    "scheduler_decay_steps": 30000,
    "scheduler_decay_lr": 2.5e-06,
    "vlm_model_name": "HuggingFaceTB/SmolVLM2-500M-Instruct",
    "load_vlm_weights": true,
    "add_image_special_tokens": false,
    "attention_mode": "cross_attn",
    "prefix_length": 0,
    "pad_language_to": "longest",
    "num_expert_layers": -1,
    "num_vlm_layers": 0,
    "self_attn_every_n_layers": 2,
    "expert_width_multiplier": 0.5,
    "min_period": 0.004,
    "max_period": 4.0
}
```

## Key Configuration Details

| 
…[truncated 410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T12:03:04.574858+00:00_

# Full Raw JSON Configuration

Here is the complete configuration file content:

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
            "shape": [7]
        }
    },
    "device": "cuda",
    "use_amp": false,
    "use_peft": false,
    "push_to_hub": true,
    "repo_id": "pepijn223/smolvla_libero",
    "private": null,
    "tags": null,
    "license": null,
    "pretrained_path": "lerobot/smolvla_base",
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
    "empty_cameras": 0,
    "adapt_to_pi_aloha": false,
    "use_delta_joint_actions_aloha": false,
    "tokenizer_max_length": 48,
    "num_steps": 10,
    "use_cache": true,
    "freeze_vision_encoder": false,
    "train_expert_only": false,
    "train_state_proj": true,
    "optimizer_lr": 0.0001,
    "optimizer_betas": [0.9, 0.95],
    "optimizer_eps": 1e-08,
    "optimizer_weight_decay": 1e-10,
    "optimizer_grad_clip_norm": 10.0,
    "scheduler_warmup_steps": 1000,
    "scheduler_decay_steps": 25000,
    "scheduler_decay_lr": 2.5e-06,
    "vlm_model_name": "HuggingFaceTB/SmolVLM2-500M-Video-Instruct",
    "load_vlm_weights": true,
    "add_image_special_tokens": false,
    "attention_mode": "cross_attn",
    "prefix_length": 0,
    "pad_language
…[truncated 656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-22T12:03:04.575255+00:00_

核实完毕。结论如下：

---

## 结果

### 1. 我们用的是哪个？

**`lerobot/smolvla_libero`**（不是 `HuggingFaceVLA/smolvla_libero`）。

证据：下载 metadata 中的 commit SHA `31d453f7edd78c839a8bbc39744a292686daf0de` 精确匹配 `lerobot/smolvla_libero`。config.json 中的 `repo_id: "pepijn223/smolvla_libero"` 是训练者的个人 repo，后来发布为 `lerobot/smolvla_libero`。

### 2. 这两个是不是同一个模型？

**不是。架构和训练配置有根本性差异。**

| 配置项 | `HuggingFaceVLA/smolvla_libero` (Sep 2025) | `lerobot/smolvla_libero` (Mar 2026) ← 我们用的 |
|--------|---------------------------------------------|------------------------------------------------|
| VLM backbone | SmolVLM2-500M-**Instruct** | SmolVLM2-500M-**Video**-Instruct |
| state_dim | **8** | **6** |
| 相机数量 | **2** (image, image2) | **3** (camera1, camera2, camera3) |
| n_action_steps | **1** | **50** |
| freeze_vision_encoder | **true** | **false** |
| train_expert_only | **true** | **false** |
| num_vlm_layers | **0** | **16** |
| num_expert_layers | **-1** (all) | **0** |
| expert_width_multiplier | **0.5** | **0.75** |
| 模型大小 | ~1.22 GB | ~907 MB |

### 3. 差异总结

这是两代不同的 SmolVLA LIBERO 微调：
- **`HuggingFaceVLA/`** — 旧版 (v1)，冻结视觉编码器、只训练 expert layers、单步 action、2 相机、8 维 state
- **`lerobot/`** — 新版 (v2)，全参微调、50 步 action chunking、3 相机、6 维 state、Video backbone

如果要切换到 `HuggingFaceVLA/smolvla_libero`，wrapper 代码需要改动（相机数量、state 维度、action steps 都不同）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_verify_smolvla-checkpoint-source_20260522T115941"
}
```

</details>

---
