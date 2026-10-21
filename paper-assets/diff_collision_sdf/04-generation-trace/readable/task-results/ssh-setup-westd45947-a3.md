# ssh setup westd45947 a3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_setup_westd45947_a3_20260520T033348_result.json`
- **Structured JSON:** [`557cd7e19880fb17914f.json`](../../sessions/55/557cd7e19880fb17914f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## westd-45947 环境搭建 & A3 Dry-Run 报告

### 1. 服务器环境状态

| 项目 | 状态 |
|------|------|
| GPU | 2× NVIDIA RTX PRO 6000 Blackwell, 各 ~96GB VRAM |
| Driver | 595.58.03, CUDA 13.2 |
| Python | 3.12.3 (conda base) |
| PyTorch | 2.8.0+cu128 |
| JAX/Flax | jax 0.6.2 / flax 0.10.2（仅用于配置，训练走 PyTorch） |
| 磁盘 | 数据盘 /root/autodl-tmp 250GB（已用 28GB，剩余 223GB） |

### 2. 代码和数据就绪情况

**代码** — 就绪
- `/root/colliforce-vla/` — 项目代码
- `/root/colliforce-vla/openpi/` — openpi（作为子目录引用）
- `transformers_replace` 自定义补丁已安装到 site-packages

**数据** — 就绪
- SafeLIBERO spatial: `/root/autodl-tmp/colliforce_data/safelibero_spatial/`
- SafeLIBERO object: `/root/autodl-tmp/colliforce_data/safelibero_object/`
- 数据格式已从 lerobot v3.0 转换为 v2.0（per-episode parquet, jsonl 元数据）
- SDF GT: `/root/colliforce-vla/data/sdf_gt_spatial_bowl.npz`, `sdf_gt_object_chocolate.npz`

**模型权重** — 就绪
- pi0_base: `/root/autodl-tmp/openpi_weights/pi0_base/model.safetensors`

**Norm stats** — 就绪（通过符号链接）
- `assets/a3_grad_refine_spatial_bowl` → `baseline_spatial_bowl`
- `assets/a3_grad_refine_object_pudding` → `baseline_object_pudding`

### 3. 本次修复的问题

从上一 session 接续，本次修复了 3 个问题：

1. **`language_model.model.layers` AttributeError** — openpi 的 PaliGemma 中 `language_model` 已是 `GemmaModel`（通过 `AutoModel.from_config` 创建），无需再 `.model`。修复：`train_a3_hook.py:118` 改为 `language_model.layers`

2. **lerobot v3.0 图片格式不兼容** — parquet 中图片存为 `struct{bytes, path}` dict 格式，两处代码无法处理：
   - `hf_transform_to_torch()` — 添加 dict→PIL→tensor 分支
   - `_query_hf_dataset()` — 重写以处理 Column→list 转换 + dict 图片解码

3. **`LoRALinear` 缺少 `weight` 属性** — `pi0_pytorch.py` forward 中访问 `q_proj.weight.dtype`，LoRA 注入后 `q_proj` 变为 `LoRALinear`。修复：添加 `weight`/`bias` property 代理到 `self.base`

### 4. A3 训练可以直接启动

**Dry-run 已通过。** 2 步训练完成：
- Step 1: loss=0.2363, lr=2.50e-05
- Step 2: loss=0.2592, lr=1.38e-05
- 首次运行含 torch.compile 编译约 4 分钟，后续迭代 ~2 min/step

**启动命令：**
```bash
# spatial_bowl 场景（GPU 0）
CUDA_VISIBLE_DEVICES=0 python scripts/train_a3_hook.py --scene spatial_bowl --seed 0

# object_pudding 场景（GPU 1，可并行）
CUDA_VISIBLE_DEVICES=1 python scripts/train_a3_hook.py --scene object_pudding --seed 0
```

---
