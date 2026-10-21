# OpenVLA LIBERO Fine-tuned 权重调研报告

**日期**: 2026-05-19
**背景**: 排查 OpenVLA 在 LIBERO-Object 上 eval 0% 问题

---

## 1. 之前 eval 用的权重

**结论：从未运行过 OpenVLA eval。之前跑的全部是 SmolVLA。**

- 服务器 bjb2-40593 上 `/root/autodl-tmp/models/` 只有三个模型：
  - `SmolVLM2-500M-Video-Instruct`
  - `smolvla_base`
  - `smolvla_libero`
- **无任何 OpenVLA 权重文件**（搜索 `/root/autodl-tmp/` 下 `*openvla*` 返回空）
- 项目代码（`evaluate.py`, `smolvla_wrapper.py`, `utils.py`）中 **零 OpenVLA 引用**
- `evaluate.py` 的 `--smolvla_path` 默认指向 `/root/autodl-tmp/models/smolvla_libero/`
- `eval_object_vla_only_seed44.json` 显示：mode="vla_only", benchmark="object", **overall SR = 10%**（这是 SmolVLA K=1 baseline，不是 OpenVLA）

plan_802 可行性分析（2026-05-17）已结论：OpenVLA 7B 与 SmolVLA CRM 完全不兼容（feature dim 4096 vs 960, deterministic vs K-sample）。

---

## 2. 可用的 LIBERO Fine-tuned OpenVLA Checkpoints

### 2.1 官方 OpenVLA (LoRA r=32, 离散 256-bin tokenized actions)

| HuggingFace Path | Suite | SR | 训练 Steps | GPU |
|---|---|---|---|---|
| `openvla/openvla-7b-finetuned-libero-spatial` | Spatial | **84.7%** | 50K | 8xA100 80GB |
| `openvla/openvla-7b-finetuned-libero-object` | Object | **88.4%** | 50K | 8xA100 80GB |
| `openvla/openvla-7b-finetuned-libero-goal` | Goal | **79.2%** | 50K | 8xA100 80GB |
| `openvla/openvla-7b-finetuned-libero-10` | Long | **53.7%** | 80K | 8xA100 80GB |

- **Action format**: 每维离散化为 256 bins（1st-99th quantile 均匀分割），7-DoF，单步输出
- **Tokenizer**: Llama-2 tokenizer + 256 action tokens
- **输入**: 单张 agentview image + language instruction，需 `--center_crop True`
- **Eval 脚本**: `openvla/openvla` repo -> `experiments/robot/libero/run_libero_eval.py`
- **模型大小**: 8B params, BF16

### 2.2 OpenVLA-OFT (连续 L1 回归, action chunks)

| HuggingFace Path | Suite | SR | 相对 base 提升 |
|---|---|---|---|
| `moojink/openvla-7b-oft-finetuned-libero-spatial` | Spatial | **97.6%** | +12.9pp |
| `moojink/openvla-7b-oft-finetuned-libero-object` | Object | **98.4%** | +10.0pp |
| `moojink/openvla-7b-oft-finetuned-libero-goal` | Goal | **97.9%** | +18.7pp |
| `moojink/openvla-7b-oft-finetuned-libero-10` | Long | **94.5%** | +40.8pp |

- **Action format**: 连续 L1 回归，MLP action head，action chunk = 8 步
- **输入**: 2-3 张图像（agentview + wrist camera）+ proprioceptive state + language
- **推理 GPU**: ~16GB VRAM（单 GPU 即可）
- **Eval 脚本**: `moojink/openvla-oft` repo -> `experiments/robot/libero/run_libero_eval.py`
- **论文**: arXiv:2502.19645
- **模型大小**: 8B params, BF16
- **关键**: 使用 `unnorm_key="libero_object_no_noops"` 做 action unnormalization

---

## 3. Action Space 兼容性对比

| 特征 | SmolVLA (ours) | OpenVLA (base) | OpenVLA-OFT |
|---|---|---|---|
| Action 格式 | 连续 7D (flow matching) | 离散 256-bin tokenized 7D | 连续 L1 回归 7D |
| Action 维度 | 7 (6D pose + 1D gripper) | 7 (6D pose + 1D gripper) | 7 (6D pose + 1D gripper) |
| Chunk size | 50 (有效 5) | 1 (单步) | 8 |
| K-samples | 是 (K=10, 用于 CGS/CRM) | 否 (确定性) | 否 (确定性) |
| Proprio 输入 | 是 (8D) | 否 | 是 |
| 图像输入 | 1 (agentview) | 1 (agentview, center_crop) | 2-3 (agentview + wrist) |
| Hidden dim | 960 | 4096 | 4096 |
| 推理显存 | ~4GB | ~16GB | ~16GB |

**核心不兼容点**：
1. OpenVLA 无 K-sample 机制 -> CRM 的 conformal 保证无法复用
2. Hidden dim 4096 vs 960 -> CRM 需要重新训练
3. Base OpenVLA 无 proprio -> 输入格式不同

---

## 4. 代码适配需求

### 场景 A: 只跑 OpenVLA baseline eval（不接 CRM）
- **不需要修改我们的代码**
- 直接用 OpenVLA 官方 eval 脚本（`openvla/openvla` 或 `moojink/openvla-oft` repo）
- 安装依赖：clone repo + `pip install -e .`
- 命令示例：
  ```bash
  # Base OpenVLA
  python experiments/robot/libero/run_libero_eval.py \
    --model_family openvla \
    --pretrained_checkpoint openvla/openvla-7b-finetuned-libero-object \
    --task_suite_name libero_object \
    --center_crop True

  # OpenVLA-OFT
  python experiments/robot/libero/run_libero_eval.py \
    --pretrained_checkpoint moojink/openvla-7b-oft-finetuned-libero-object \
    --use_l1_regression True \
    --num_images_in_input 2 \
    --use_proprio True
  ```

### 场景 B: OpenVLA + CRM（plan_802）
- 需全新 `OpenVLAWrapper`（类似 SmolVLAWrapper 但对接 OpenVLA）
- CRM 需要重新设计：obs_dim 从 960 改为 4096，放弃 K-sample conformal 保证
- 预估工作量：2-3 天
- 此方案在 plan_802 可行性分析中已评估，结论不推荐

---

## 5. 推荐方案

### 作为 baseline 对比
| 选择 | Checkpoint | 预期 SR | 适用场景 |
|---|---|---|---|
| **首选** | `openvla/openvla-7b-finetuned-libero-object` | 88.4% | 标准 baseline，论文可比 |
| 可选 | `moojink/openvla-7b-oft-finetuned-libero-object` | 98.4% | SOTA 上界参照 |

### 部署建议
- **服务器**: bjb2-40593（有 GPU 且已有 LIBERO 环境）
- **显存需求**: ~16GB（8B BF16），RTX 4090 (24GB) 可跑
- **方法**: clone `openvla/openvla` repo，用官方 eval 脚本
- **模型下载**: 从 HuggingFace 下载到 `/root/autodl-tmp/models/openvla-7b-finetuned-libero-object/`
- **耗时预估**: 下载 ~30min（模型 ~16GB），eval ~2-4h（比 SmolVLA 慢因为模型更大）

### 关键注意事项
1. OpenVLA eval 必须 clone 官方 repo，不能用我们的 evaluate.py
2. Base OpenVLA 需要 `--center_crop True`（训练时用了 random crop augmentation）
3. OpenVLA-OFT 需要 wrist camera image，确认 LIBERO 环境有 `eye_in_hand` 相机
4. 如果目的只是论文中报告 OpenVLA baseline SR，**直接引用官方数字 88.4% 即可，不必重跑**
