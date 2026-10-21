# OpenPI (π0) 部署报告 — westd-35807

## 1. 仓库结构

```
/root/autodl-tmp/openpi/               # clone 在 autodl-tmp（避免根分区占用）
├── src/openpi/
│   ├── models/                         # JAX 模型定义
│   │   ├── gemma.py                    # Config + get_config(), 双 expert 架构
│   │   ├── pi0.py                      # JAX Pi0 (flow matching)
│   │   ├── pi0_config.py              # Pi0Config dataclass
│   │   ├── model.py                    # BaseModelConfig, Observation
│   │   └── lora.py                     # LoRA 实现
│   ├── models_pytorch/                 # PyTorch 版本
│   │   ├── pi0_pytorch.py             # PI0Pytorch (我们使用的)
│   │   ├── gemma_pytorch.py           # PaliGemmaWithExpertModel (HF transformers)
│   │   ├── preprocessing_pytorch.py   # 图像/状态预处理
│   │   └── transformers_replace/      # HF transformers 补丁文件
│   ├── training/
│   │   ├── config.py                   # 所有训练配置 (含 LIBERO)
│   │   ├── weight_loaders.py          # CheckpointWeightLoader (GCS)
│   │   └── data_loader.py
│   └── policies/
│       └── libero_policy.py           # LIBERO 推理策略
├── scripts/
│   └── train_pytorch.py               # PyTorch 训练入口
├── examples/
│   └── convert_jax_model_to_pytorch.py # JAX→PyTorch 权重转换
└── /root/colliforce-vla/openpi → symlink
```

## 2. 权重下载

### 方式
- **来源**: HuggingFace `lerobot/pi0_base`（PyTorch safetensors 格式，已转换好）
- **Key 格式验证**: 与 openpi `PI0Pytorch` state_dict 完全兼容（777 tensors）
- **大小**: 14 GB (F32), 3.50B 参数
- **路径**: `/root/autodl-tmp/openpi_weights/pi0_base/model.safetensors`
- **下载方式**: `wget` 通过 AutoDL 代理，速度 ~2-5 MB/s，预计 ~90 分钟

### 下载状态
- 下载进行中（PID 22419）
- 验证完成后可直接 `safetensors.torch.load_model(model, path)` 加载

### 备选方式
- GCS 原始 JAX 权重: `gs://openpi-assets/checkpoints/pi0_base/params`（orbax 格式，需转换）
- 转换脚本: `examples/convert_jax_model_to_pytorch.py`
- GCS 在 AutoDL 上极慢（~200 KB/s），不推荐

## 3. Forward Pass 验证结果

### 环境
- Python 3.10, torch 2.8.0+cu128, transformers 4.53.2
- RTX PRO 6000 Blackwell 94 GB
- `pytorch_compile_mode=None`, `dtype="float32"`

### Inference (sample_actions, 10 denoise steps)
| 指标 | 值 |
|------|-----|
| Output shape | `[1, 50, 32]` (B=1, action_horizon=50, action_dim=32) |
| Output dtype | float32 |
| 推理时间 | 0.54s |
| 模型显存 | 13.06 GB |
| 峰值显存 | 13.30 GB |

### Training (forward, loss computation)
| 指标 | 值 |
|------|-----|
| Loss shape | `[1, 50, 32]` (per-element MSE) |
| Loss mean (random weights) | 3.5792 |
| forward 时间 | 0.59s |
| 峰值显存 | 19.65 GB |

### suffix_out 验证
```
suffix_out shape (inference): [1, 50, 1024]  ✅
suffix_out shape (training):  [1, 50, 1024]  ✅
```
- Hook point: `model.action_out_proj` 的 input (即 action_out_proj 之前的 suffix_out)
- 维度: `[B, action_horizon, action_expert_width=1024]`

## 4. LIBERO Fine-tune 配置

### 已有配置 (training/config.py)

| 配置名 | 模型 | LoRA | 特点 |
|--------|------|------|------|
| `pi0_libero` | Pi0Config() | 无 (全量微调) | 30K steps, pi0_base 权重 |
| `pi0_libero_low_mem_finetune` | gemma_2b_lora + gemma_300m_lora | rank=16/32 | 30K steps, 低显存 |
| `pi0_fast_libero` | Pi0FASTConfig | 无 | FAST tokenizer 版 |
| `pi05_libero` | Pi0Config(pi05=True) | 无 | action_horizon=10 |

### PyTorch 微调流程
1. 下载权重到 `/root/autodl-tmp/openpi_weights/pi0_base/`
2. 配置中设 `pytorch_weight_path="/root/autodl-tmp/openpi_weights/pi0_base"`
3. `torchrun --nproc_per_node=4 scripts/train_pytorch.py pi0_libero --exp_name <name>`

## 5. 遇到的问题和解决方案

| 问题 | 原因 | 解决 |
|------|------|------|
| Python 版本不满足 (需 >=3.11) | pyproject.toml 约束 | 手动安装依赖，跳过 `pip install -e .` |
| JAX 导入失败 | PyTorch 版代码仍 import JAX 模块 | 安装 `jax[cpu]` + `flax` (仅用于 import) |
| `jaxtyping` 版本不兼容 | 最新版 API 变化 | 降级到 `jaxtyping==0.2.36` |
| `transformers` 版本不兼容 | 5.8.1 缺少 openpi 补丁依赖 | 降级到 `4.53.2` + 应用 transformers_replace 补丁 |
| numpy metadata 冲突 | conda/pip 双 dist-info | 删除旧的 numpy-2.2.6.dist-info |
| torch.compile dtype 错误 | bfloat16 模型 + float32 中间计算冲突 | 设 `pytorch_compile_mode=None` 或 `dtype="float32"` |
| GCS 下载极慢 | AutoDL 代理到 GCS 网络差 | 改用 HuggingFace `lerobot/pi0_base` + wget |
| HF mirror 大文件下载失败 | hf-mirror.com 连接重置 | 直接 wget huggingface.co（走 AutoDL 代理） |

## 6. 依赖安装清单

```bash
# 核心 (已安装)
pip install jax[cpu] flax jaxtyping==0.2.36 safetensors tyro beartype
pip install sentencepiece numpydantic ml-collections dm-tree
pip install orbax-checkpoint optax chex equinox treescope
pip install ml-dtypes opt-einsum wadler-lindig msgpack gcsfs
pip install transformers==4.53.2

# transformers 补丁
cp -r openpi/src/openpi/models_pytorch/transformers_replace/models/* \
  $(python -c "import transformers; import os; print(os.path.dirname(transformers.__file__))")/models/
```
