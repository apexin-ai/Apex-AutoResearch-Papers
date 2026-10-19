# SmolVLA + LIBERO Fine-tuning 调研报告

**日期**: 2026-05-13

---

## 1. SmolVLA Fine-tuning 官方方式

### 模型概况
- **Model ID**: `lerobot/smolvla_base`
- **参数量**: ~450M total, ~100M trainable (action expert)
- **架构**: SmolVLM2-500M-Video-Instruct (SigLIP + SmolLM2-1.7B) + Flow-Matching Transformer action expert
- **默认 action/state**: `action.shape=[6]`, `state.shape=[6]` (SO-100/SO-101 joint position control)
- **Action chunking**: `chunk_size=50`
- **动态 padding**: 内部 pad 到 `max_action_dim=32`，输出时裁剪到实际维度

### 安装
```bash
git clone https://github.com/huggingface/lerobot.git && cd lerobot
pip install -e ".[smolvla]"       # 基础
pip install -e ".[smolvla,peft]"  # + LoRA 支持
```

### 训练命令

**Full fine-tune (action expert only, VLM frozen)**:
```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/smolvla_libero \
  --policy.device=cuda \
  --policy.dtype=bfloat16
```

**LoRA fine-tune (低显存)**:
```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --policy.output_features=null \
  --policy.input_features=null \
  --policy.optimizer_lr=1e-3 \
  --policy.scheduler_decay_lr=1e-4 \
  --steps=100000 \
  --batch_size=32 \
  --peft.method_type=LORA \
  --peft.r=64 \
  --peft.lora_alpha=64
```

PEFT 默认 target modules: `q_proj`, `v_proj` + action expert 的 `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`

### 关键超参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| steps | 20k (real) / 100k (sim) | |
| batch_size | 64 | 低显存减到 8-16 |
| optimizer_lr | 1e-4 (full) / 1e-3 (LoRA) | |
| chunk_size | 50 | 每次预测的 action 步数 |
| dtype | bfloat16 | |
| gradient_checkpointing | true | 省显存 |
| peft.r | 64 | LoRA rank |

### 关键文档
- 官方 fine-tune docs: https://huggingface.co/docs/lerobot/smolvla
- PEFT/LoRA docs: https://huggingface.co/docs/lerobot/en/peft_training
- Model card: https://huggingface.co/lerobot/smolvla_base
- Training notebook: https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb
- SmolVLA blog: https://huggingface.co/blog/smolvla
- Medium 教程: https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632

---

## 2. LIBERO 数据 → LeRobot 格式

### 现成数据集（HuggingFace Hub，无需转换）

| Dataset ID | 内容 | 规模 |
|------------|------|------|
| **`HuggingFaceVLA/libero`** | Spatial+Object+Goal+10 | 273k frames, 1693 eps |
| `lerobot/libero` | 同上 | 273k frames |
| `physical-intelligence/libero` | 同上（PI 版本） | 273k frames |
| `IPEC-COMMUNITY/libero_spatial_no_noops_*` | 仅 Spatial | 53k frames |
| `IPEC-COMMUNITY/libero_goal_no_noops_*` | 仅 Goal | 52k frames |
| `IPEC-COMMUNITY/libero_object_no_noops_*` | 仅 Object | 67k frames |
| `IPEC-COMMUNITY/libero_10_no_noops_*` | 仅 LIBERO-10 | 101k frames |
| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 | 569k frames |
| `jesbu1/libero_90_lerobot` | LIBERO-90 (π0 用) | — |

**推荐**: 直接用 `HuggingFaceVLA/libero` 或 `lerobot/libero`，无需自行转换。

### 数据格式

```
observation.images.image  → 256×256×3 (agentview, AV1 MP4)
observation.images.image2 → 256×256×3 (wrist camera)
observation.state         → float32[8]: eef_pos(3) + axis_angle(3) + gripper_qpos(2)
action                    → float32[7]: eef_delta(6) + gripper(1), clipped [-1,1]
FPS: 10 Hz
```

### 转换脚本（如需自己转换）

**方式 A: openpi 脚本 (RLDS → LeRobot)**
```bash
# https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py
uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/data --push_to_hub
```

**方式 B: any4lerobot (HDF5 → LeRobot)**
```bash
# https://github.com/Tavish9/any4lerobot/tree/main/libero2lerobot
python libero_utils/regenerate_libero_dataset.py --resolution 256 --libero_task_suite libero_90
python libero_h5.py --src-paths /path/to/libero/ --output-path /path/to/local
```

---

## 3. Action Dimension 6→7 可行性

### 不匹配分析

| | SmolVLA base | LIBERO |
|---|---|---|
| Action dim | **6** (joint position) | **7** (EEF delta + gripper) |
| State dim | **6** | **8** |
| Control type | Joint position (SO-100) | End-effector delta (Franka) |

### 解决方案：自动处理

SmolVLA 内部使用动态 padding（`max_action_dim=32`），fine-tune 时 **自动从数据集推断 action_dim**。使用 LIBERO 数据训练时：
- `output_features.action.shape` 自动设为 `[7]`
- `input_features.observation.state.shape` 自动设为 `[8]`
- 归一化统计量从 LIBERO 数据集重新计算
- **无需手动修改任何维度参数**

关键 flags（让 trainer 从数据集推断）:
```
--policy.output_features=null --policy.input_features=null
```

### 已有 checkpoint
`lerobot/smolvla_libero` — SmolVLA 在 LIBERO 上 fine-tuned 的 checkpoint，action_dim=7。

---

## 4. 现成的 LIBERO Fine-tuned VLA Checkpoints

### SmolVLA 系列
| Checkpoint | 说明 |
|------------|------|
| `lerobot/smolvla_libero` | SmolVLA fine-tuned on LIBERO |

### π0 系列
| Checkpoint | 说明 |
|------------|------|
| `lerobot/pi0_libero_base` | π0 base |
| `lerobot/pi0_fast_libero_base` | π0-FAST |
| `lerobot/pi05_libero_finetuned` | π0.5 fine-tuned, **97.5% avg** |

### OpenVLA 系列
| Checkpoint | 说明 |
|------------|------|
| `openvla/openvla-7b-finetuned-libero-spatial` | per-suite |
| `openvla/openvla-7b-finetuned-libero-object` | per-suite |
| `openvla/openvla-7b-finetuned-libero-goal` | per-suite |
| `openvla/openvla-7b-finetuned-libero-10` | per-suite |
| `moojink/openvla-7b-oft-finetuned-libero-*` | OFT 版本, **97.1% avg** |

### 其他
| Checkpoint | 说明 |
|------------|------|
| `nvidia/Cosmos-Policy-LIBERO-Predict2-2B` | **98.5% avg**, SOTA |
| `IPEC-COMMUNITY/spatialvla-4b-224-pt` | SpatialVLA |
| `lerobot/xvla-libero` | xVLA |

---

## 5. LIBERO SOTA 排行榜

| Model | Avg SR | 方法 | 显存/GPU |
|-------|--------|------|----------|
| LightVLA | ~99.7% | LoRA + token pruning | 8×A100 |
| Cosmos-Policy | 98.5% | Full FT (video diffusion) | 64×H100 |
| π0.5 + RL | 98.3% | RL fine-tune | — |
| π0 + RL | 97.6% | RL fine-tune | — |
| CogVLA | 97.4% | LoRA r=32 | 4×A800 |
| OpenVLA-OFT | 97.1% | LoRA + parallel decoding | 8×A100 |
| UniVLA | 95.5% | Autoregressive discrete | — |
| SpatialVLA | 78.1% | LoRA r=32 | — |
| OpenVLA | 76.5% | LoRA r=32 | 8×A100 |
| Octo | 75.1% | Full FT | — |

---

## 6. 推荐的 Fine-tuning 方案

### 方案 A: 直接用已有 checkpoint（最快）
```bash
# lerobot/smolvla_libero 已经 fine-tuned 好了，直接评估
lerobot-eval --policy.path=lerobot/smolvla_libero --env.type=libero --env.task=libero_spatial
```

### 方案 B: 自己 fine-tune SmolVLA on LIBERO（推荐）
```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --policy.output_features=null \
  --policy.input_features=null \
  --batch_size=32 \
  --steps=100000 \
  --output_dir=outputs/smolvla_libero \
  --policy.device=cuda \
  --policy.dtype=bfloat16 \
  --wandb.enable=true
```
- 4090 24GB 可跑，batch_size 调到 8-16
- 预计训练 8-12 小时

### 方案 C: LoRA fine-tune（省显存）
同上但加 `--peft.method_type=LORA --peft.r=64 --peft.lora_alpha=64`

### 关键注意事项
1. **数据集**: 用 `HuggingFaceVLA/libero`，不需要自己转换
2. **Action dim**: 自动从数据集推断为 7，无需手动配置
3. **归一化**: 自动使用 LIBERO 的 stats，不需要手动处理
4. **评估**: `lerobot-eval --env.type=libero` 集成了 LIBERO 仿真环境
5. **已有 checkpoint**: `lerobot/smolvla_libero` 可直接使用或作为 fine-tune 起点
