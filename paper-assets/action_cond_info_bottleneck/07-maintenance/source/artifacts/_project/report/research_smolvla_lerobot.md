# SmolVLA + LeRobot 调研报告

## 1. SmolVLA 模型架构

### 1.1 整体架构

SmolVLA 是 HuggingFace 发布的 450M 参数 Vision-Language-Action 模型，由两个核心组件组成：

1. **Vision-Language Model (VLM)**: SmolVLM2-500M-Video-Instruct（基于 Idefics3 架构）
2. **Action Expert**: ~100M 参数的 flow matching transformer

```
Input Images → SigLIP Vision Encoder → PixelShuffle → Linear Proj → SmolLM2 (16 layers) → VLM Features
                                                                                              ↓
Language Instruction → Tokenizer → SmolLM2 Embedding ─────────────────────────────────────────┘
                                                                                              ↓
Robot State → Linear Proj (state_proj) ──────────────────────────────────────────────── Cross-Attn
                                                                                              ↓
                                                                     Action Expert (interleaved CA + SA)
                                                                              ↓
                                                                     Flow Matching → Action Chunk (50 steps)
```

### 1.2 Vision Encoder (SigLIP)

| 参数 | 值 |
|------|-----|
| 模型 | SigLIP-Base (google/siglip-base-patch16-512) |
| hidden_size | **768** |
| image_size | 512×512 |
| patch_size | 16 |
| num_attention_heads | 12 |
| 原始输出 tokens | (512/16)² = **1024 tokens** |
| PixelShuffle factor | 4 |
| PixelShuffle 后 tokens | 1024 / 4² = **64 tokens per frame** |
| PixelShuffle 后 channel dim | 768 × 4² = 12288 → Linear Proj → 960 (匹配 LLM hidden_size) |

**关键结论**: 每张 512×512 图片经 SigLIP + PixelShuffle 后产出 **64 tokens × 960 dim** 送入 LLM。

### 1.3 Language Model (SmolLM2-360M)

| 参数 | 值 |
|------|-----|
| 架构 | VLlama3ForCausalLM (类 Llama) |
| hidden_size | **960** |
| num_hidden_layers | 32 (SmolVLA 只用前 **16 层**) |
| num_attention_heads | 15 |
| num_key_value_heads | 5 (GQA) |
| intermediate_size | 2560 |
| vocab_size | 49280 |
| activation | SiLU |
| position encoding | RoPE (theta=100000) |
| max_position_embeddings | 8192 |

### 1.4 Action Expert

| 参数 | 值 |
|------|-----|
| 参数量 | ~100M |
| hidden_dim | 0.75 × 960 = **720** |
| 层结构 | 与 VLM 层交错的 cross-attn + self-attn |
| self_attn_every_n_layers | 2（每 2 层一个 self-attn，其余为 cross-attn） |
| num_expert_layers | 0 (config 中为 0，表示 expert 与 VLM 层交织运行) [UNVERIFIED - 具体含义需看源码] |
| attention_mode | cross_attn |
| 训练目标 | Flow Matching (conditional) |
| action chunk_size | **50** |
| n_action_steps | **50** |
| 推理 denoising steps | **10** |
| noise schedule | log-normal, min_period=0.004, max_period=4.0 |

### 1.5 SmolVLA Config (完整)

```json
{
    "type": "smolvla",
    "n_obs_steps": 1,
    "chunk_size": 50,
    "n_action_steps": 50,
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
    "num_steps": 10,
    "freeze_vision_encoder": true,
    "train_expert_only": true,
    "train_state_proj": true,
    "optimizer_lr": 1e-4,
    "optimizer_betas": [0.9, 0.95],
    "scheduler_warmup_steps": 1000,
    "scheduler_decay_steps": 30000,
    "scheduler_decay_lr": 2.5e-6
}
```

### 1.6 HuggingFace 模型权重

| 模型 | HF Repo |
|------|---------|
| SmolVLA Base (预训练) | `lerobot/smolvla_base` |
| VLM Backbone | `HuggingFaceTB/SmolVLM2-500M-Video-Instruct` |

### 1.7 模型加载方式

```python
import torch
from lerobot.policies.smolvla import SmolVLAPolicy
from lerobot.policies.factory import make_pre_post_processors

# 加载 policy
policy = SmolVLAPolicy.from_pretrained("lerobot/smolvla_base").to("cuda").eval()

# 创建 preprocessor/postprocessor
preprocess, postprocess = make_pre_post_processors(
    policy.config,
    "lerobot/smolvla_base",
    preprocessor_overrides={"device_processor": {"device": "cuda"}},
)

# 推理
batch = preprocess(observation_dict)
with torch.inference_mode():
    action = policy.select_action(batch)
    action = postprocess(action)
```

---

## 2. LeRobot 框架

### 2.1 基本信息

| 项目 | 信息 |
|------|------|
| GitHub | https://github.com/huggingface/lerobot |
| 版本 | 0.5.2 |
| License | Apache-2.0 |
| 构建系统 | setuptools (pyproject.toml) |

### 2.2 Fine-tuning Pipeline

#### 训练脚本入口

```bash
# CLI 方式（推荐）
lerobot-train --policy.path=lerobot/smolvla_base --dataset.repo_id=user/dataset ...

# Python 方式
python lerobot/scripts/train.py ...
```

#### 配置系统

- 使用 `draccus` 库（dataclass-based config）
- 根配置类: `TrainPipelineConfig`
- 所有参数通过 CLI 覆盖: `--policy.xxx`, `--dataset.xxx`, `--batch_size` 等
- 无 YAML 配置文件，全部通过 CLI + dataclass 默认值

#### 训练命令示例

```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=${HF_USER}/mydataset \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --policy.device=cuda \
  --policy.dtype=bfloat16 \
  --wandb.enable=true
```

#### 训练循环核心

```python
# 内部结构（简化）
from accelerate import Accelerator

accelerator = Accelerator(mixed_precision="bf16")
policy = make_policy(config)
optimizer = make_optimizer(policy, config)
dataloader = make_dataloader(dataset, config)

for step, batch in enumerate(dataloader):
    batch = preprocess(batch)
    with accelerator.autocast():
        loss, outputs = policy.forward(batch)
    accelerator.backward(loss)
    optimizer.step()
    scheduler.step()
```

### 2.3 SmolVLA 在 LeRobot 中的位置

#### Policy 类名和路径

```
lerobot/policies/smolvla/
├── __init__.py            # 导出 SmolVLAPolicy
├── modeling_smolvla.py    # SmolVLAPolicy 主类
└── configuration_smolvla.py  # SmolVLAConfig 配置类
```

- **Policy 类**: `lerobot.policies.smolvla.SmolVLAPolicy`
- **Config 类**: `lerobot.policies.smolvla.SmolVLAConfig` [UNVERIFIED - 具体类名可能不同]
- **Policy type 注册名**: `"smolvla"`

#### 关键方法

| 方法 | 作用 |
|------|------|
| `SmolVLAPolicy.from_pretrained(model_id)` | 从 HF Hub 加载预训练权重 |
| `policy.forward(batch)` | 训练时前向传播，返回 (loss, outputs) |
| `policy.select_action(batch)` | 推理时生成 action chunk |
| `make_pre_post_processors()` | 创建数据预处理/后处理 pipeline |

### 2.4 冻结 Backbone 机制

#### 方式 1: Config 参数控制（默认行为）

```bash
# SmolVLA 默认 config（已内置）
--policy.freeze_vision_encoder=true   # 冻结 SigLIP
--policy.train_expert_only=true       # 只训练 action expert
--policy.train_state_proj=true        # 也训练 state projection
```

默认 fine-tuning 时：
- SigLIP vision encoder: **冻结**
- SmolLM2 语言模型层: **冻结**（train_expert_only=true 时）
- Action expert: **可训练**
- State projection: **可训练**

#### 方式 2: PEFT/LoRA（参数高效微调）

```bash
pip install "lerobot[peft]"  # 安装 PEFT 依赖

lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --peft.method_type=LORA \
  --peft.r=64 \
  --policy.optimizer_lr=1e-3 \
  --steps=100000 \
  --batch_size=32
```

**LoRA 默认 target modules**: `q_proj`, `v_proj` (LM expert) + `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`

**自定义 target**:
```bash
--peft.target_modules='(model\.vlm_with_expert\.lm_expert\..*\.(down|gate|up)_proj|.*\.(state_proj|action_in_proj|action_out_proj))'
```

**指定模块全量微调**（不用 LoRA）:
```bash
--peft.full_training_modules=["state_proj"]
```

### 2.5 数据加载流程

#### LeRobotDataset v3.0 格式

```
dataset_repo/
├── data/
│   └── chunk-000/
│       └── file_000.parquet    # 多 episode 的帧级数据（state, action, timestamp）
├── videos/
│   └── camera1/
│       └── chunk-000/
│           └── file_000.mp4    # 多 episode 视频
└── meta/
    ├── info.json               # 数据集元信息
    ├── stats.json              # 归一化统计量
    ├── tasks.parquet           # 任务描述
    └── episodes/
        └── chunk-000/
            └── file_000.parquet  # Episode 索引
```

#### 数据字段

- **observation.state**: 机器人关节状态 (shape: [6] for SO100)
- **observation.images.camera1**: 图像帧 (shape: [3, H, W])
- **action**: 机器人动作 (shape: [6] for SO100)
- **timestamp**: 时间戳
- **episode_index**: Episode 编号
- **task**: 任务文本描述

#### DataLoader 结构

```python
from lerobot.datasets.lerobot_dataset import LeRobotDataset

# 从 HF Hub 加载
dataset = LeRobotDataset("user/dataset_name")

# 访问单帧
frame = dataset[0]
# → {"observation.state": tensor, "observation.images.camera1": tensor, "action": tensor, ...}

# 内部使用标准 PyTorch DataLoader
dataloader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True)
```

#### 归一化

- **VISUAL**: IDENTITY（不归一化，图像已是 [0,1]）
- **STATE**: MEAN_STD 归一化
- **ACTION**: MEAN_STD 归一化
- 统计量存储在 `meta/stats.json`

---

## 3. 依赖清单

### 3.1 核心依赖

| 包 | 版本要求 | 说明 |
|----|---------|------|
| Python | **>=3.12** | 必须 3.12+ |
| torch | **>=2.7, <2.12.0** | PyTorch |
| torchvision | >=0.22.0, <0.27.0 | |
| transformers | **>=5.4.0, <5.6.0** | HF Transformers (注意是 5.x!) |
| accelerate | **>=1.10.0, <2.0.0** | 多 GPU / 混合精度 |
| numpy | >=2.0.0, <2.3.0 | |
| einops | >=0.8.0, <0.9.0 | |
| safetensors | >=0.4.3, <1.0.0 | 权重格式 |
| huggingface-hub | >=1.0.0, <2.0.0 | Hub 交互 |
| draccus | ==0.10.0 | 配置系统 |
| peft | >=0.18.0, <1.0.0 | LoRA 支持 |
| wandb | >=0.24.0, <0.25.0 | 实验跟踪 |

### 3.2 SmolVLA 专属依赖

安装方式: `pip install -e ".[smolvla]"` 或 `pip install "lerobot[smolvla]"`

包含 transformers + peft 等 VLM 相关依赖。

### 3.3 其他可选依赖组

| Group | 主要包 |
|-------|--------|
| `datasets` | datasets, pandas, pyarrow, av, torchcodec |
| `diffusion` | diffusers >=0.27.2, <0.36.0 |
| `dev` | pytest, pre-commit, ruff, mypy |

### 3.4 安装大小预估

| 组件 | 大小 |
|------|------|
| PyTorch (CUDA 12.x) | ~2.5 GB |
| transformers + tokenizers | ~500 MB |
| lerobot + 依赖 | ~200 MB |
| SmolVLA 模型权重 (smolvla_base) | ~900 MB (450M params × bf16) |
| SmolVLM2-500M (首次加载时下载) | ~1 GB |
| **总计预估** | **~5 GB** |

### 3.5 安装命令

```bash
# 基础安装
pip install lerobot

# SmolVLA 完整支持
pip install "lerobot[smolvla]"

# 开发模式
git clone https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e ".[smolvla]"
```

---

## 4. 关键文件路径（LeRobot repo 中）

```
lerobot/
├── lerobot/
│   ├── policies/
│   │   ├── smolvla/
│   │   │   ├── __init__.py
│   │   │   ├── modeling_smolvla.py      # SmolVLAPolicy 主类
│   │   │   └── configuration_smolvla.py # 配置类
│   │   ├── factory.py                   # make_policy(), make_pre_post_processors()
│   │   └── utils.py                     # build_inference_frame(), make_robot_action()
│   ├── scripts/
│   │   └── train.py                     # lerobot-train 入口（或 lerobot_train.py）
│   ├── datasets/
│   │   └── lerobot_dataset.py           # LeRobotDataset 类
│   └── configs/                         # TrainPipelineConfig 等 [UNVERIFIED 具体路径]
├── examples/
│   └── tutorial/smolvla/
│       └── using_smolvla_example.py     # 使用示例
├── docs/
│   └── source/
│       ├── smolvla.mdx
│       └── peft_training.mdx
└── pyproject.toml                       # 依赖定义
```

---

## 5. 对我们项目的关键观察

### 适合做 Information Bottleneck 的切入点

1. **Vision Encoder 输出层**：SigLIP → PixelShuffle 后的 64 tokens (960-dim)，这是一个天然的 bottleneck 位置
2. **VLM Layer 16 输出**：VLM 只用前 16 层的输出送给 action expert，这层的 representation 是 action-conditioning 的核心
3. **Action Expert 的 Cross-Attention**：action tokens attend to VLM features，可以在这里施加信息约束
4. **State Projection**：单 token 通过 linear projection，维度转换点

### 训练效率

- 默认只训练 action expert (~100M params)，VLM 冻结
- 单 A100 上 20k steps ≈ 4 小时
- 50 episodes 数据即可 fine-tune
- 支持 LoRA 进一步降低训练成本

### 注意事项

- **transformers 版本要求 5.4+**：这是较新版本，需确认与其他依赖兼容性
- **Python >=3.12**：不支持 3.11 及以下
- `num_expert_layers: 0` 的具体含义需要阅读源码确认 [UNVERIFIED]
- Action expert 的确切层数未从公开文档中明确获得 [UNVERIFIED]

---

## Sources

- [SmolVLA Blog](https://huggingface.co/blog/smolvla)
- [SmolVLA Paper (arXiv:2506.01844)](https://arxiv.org/abs/2506.01844)
- [lerobot/smolvla_base Model Card](https://huggingface.co/lerobot/smolvla_base)
- [LeRobot SmolVLA Docs](https://huggingface.co/docs/lerobot/smolvla)
- [LeRobot PEFT Training](https://huggingface.co/docs/lerobot/peft_training)
- [LeRobot GitHub](https://github.com/huggingface/lerobot)
- [LeRobot pyproject.toml](https://github.com/huggingface/lerobot/blob/main/pyproject.toml)
- [SmolVLM2-500M-Video-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct)
- [SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct)
- [LeRobotDataset v3.0](https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3)
