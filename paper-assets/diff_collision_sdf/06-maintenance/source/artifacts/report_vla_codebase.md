# VLA 基座代码库调研报告

> 调研日期：2026-05-19
> 目的：评估 openpi (π0) 和 OpenVLA-OFT 作为 ColliForce-VLA MVP 基座的适合度

---

## 1. 仓库概览

| 项目 | openpi (π0) | OpenVLA-OFT |
|------|------------|-------------|
| 仓库地址 | [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | [moojink/openvla-oft](https://github.com/moojink/openvla-oft) |
| Stars | ~11,900 | ~1,200 |
| 最近更新 | 2026-05-19（活跃维护） | 2025 Q2（论文发布后维护） |
| License | Apache-2.0 | MIT |
| 框架 | JAX/Flax（主）+ PyTorch（辅） | PyTorch / HuggingFace |
| 基础论文 | π0: A Vision-Language-Action Flow Model | arXiv:2502.19645 |

---

## 2. 模型架构概述

### 2.1 openpi (π0)

**双专家 Transformer 架构**：

- **Vision Encoder**: SigLIP So400m/14, 224×224 输入, 196 tokens/image, dim=2048
- **Expert 0 (PaliGemma/Gemma 2B)**: 处理 prefix（图像 + 语言），width=2048, depth=18, 8 heads
- **Expert 1 (Action Expert/Gemma 300M)**: 处理 suffix（state + noisy actions），width=1024, depth=18

核心设计：两个 Expert **共享 Attention（Q/K/V concat 后联合计算）但有独立的 FFN**。Action Expert 的参数量远小于 PaliGemma Expert。

**Action Head**:
```
action_in_proj: Linear(action_dim → 1024)   # 将 action 投射到 expert 宽度
action_out_proj: Linear(1024 → action_dim)   # 从 expert 特征解码回 action
```

**训练目标**: Flow Matching — 预测噪声到干净 action 的 velocity field，loss = MSE(v_t, noise - actions)

**推理**: Euler ODE solver，默认 10 步去噪

**数据流**:
1. Images → SigLIP → `[B, 196*num_imgs, 2048]`
2. Language → Gemma embedder → `[B, max_token_len, 2048]`
3. State → state_proj → `[B, 1, 1024]`; Noisy actions → action_in_proj → `[B, action_horizon, 1024]`
4. Prefix + Suffix → 双专家 Transformer (18 layers, shared attention)
5. `suffix_out[:, -action_horizon:]` → action_out_proj → predicted velocity

### 2.2 OpenVLA-OFT

**Prismatic VLM + 独立 Action Head 架构**：

- **Vision Backbone**: Fused DINOv2 + SigLIP（dual backbone, 特征 concat），256 patches/image
- **Projector**: 2-layer MLP (GELU), vision_dim → llm_dim
- **LLM Backbone**: Llama-2 7B (Vicuna-7B), hidden_size=4096, 32 layers

**Action Head** (独立 nn.Module):
```
L1RegressionActionHead:
  Input: (B, NUM_ACTIONS_CHUNK * ACTION_DIM, 4096)
  MLPResNet: LayerNorm → Linear(input_dim*ACTION_DIM, 4096) → ReLU → 2x ResNetBlock → Linear(4096, action_dim)
  Output: (B, NUM_ACTIONS_CHUNK, ACTION_DIM)
```

**OFT 的核心改进**（非 Orthogonal Fine-Tuning，而是一组优化策略）：
1. **并行解码**: 替代自回归逐 token 生成，一次前向得到所有 action token 的 hidden states
2. **Action chunking**: 预测 K 个连续 action（LIBERO: 8, ALOHA: 25）
3. **连续 action 表示**: 替代 256-bin 离散化
4. **L1 回归损失**: 替代 cross-entropy

**推理速度**: ~26x faster（1 次前向 vs 56 次自回归前向）

---

## 3. Fine-tune 接口分析

### 3.1 openpi — 添加辅助任务 Head

**配置系统**: `tyro` CLI + Python dataclass，预定义 config 在 `src/openpi/training/config.py`

**冻结机制**: `Pi0Config.get_freeze_filter()` 返回 Flax NNX filter
- LoRA fine-tune: 冻结 Gemma LLM 参数，只训练 LoRA + action expert
- PathRegex 模式匹配：`".*llm.*"`, `".*lora.*"` 等

**添加 SDF decoder 的方法**:

```python
# 在 Pi0.__init__() 或 PI0Pytorch.__init__() 中:
self.sdf_decoder = SDFDecoderHead(input_dim=1024, ...)  # action expert width

# 在 compute_loss() 中，Transformer 前向之后:
suffix_features = suffix_out[:, -self.action_horizon:]  # [B, action_horizon, 1024]
sdf_pred = self.sdf_decoder(suffix_features)
sdf_loss = sdf_criterion(sdf_pred, sdf_target)
total_loss = flow_loss + lambda_sdf * sdf_loss
```

**优势**: 新增参数不匹配 `".*llm.*"` 正则，默认可训练，freeze filter 无需修改。

**替代方案**: Cross-attend 到 prefix features `[B, ~636, 2048]`（视觉 token），适合 SDF 这种空间几何任务。

**关键文件**:
- `src/openpi/models/pi0.py` — 模型定义、compute_loss
- `src/openpi/models/gemma.py` — 双专家 Transformer
- `src/openpi/models_pytorch/pi0_pytorch.py` — PyTorch 版本
- `src/openpi/training/config.py` — 训练配置

### 3.2 OpenVLA-OFT — 添加辅助任务 Head

**配置系统**: `draccus` (dataclass-based config) + `@draccus.wrap()`

**冻结机制**: `freeze_backbones()` 支持多种策略
- `"finetune"` / `"vla-train"`: Vision 冻结, Projector + LLM 训练
- `"last-layer-finetune"`: 只解冻 LLM 最后一层
- `"vla-sandwich-train"`: Vision + Projector 训练, 只解冻 LLM 最后一层

**添加 SDF decoder 的方法**:

```python
# 参照 L1RegressionActionHead 的模式:
class SDFDecoderHead(nn.Module):
    def __init__(self, input_dim=4096, hidden_dim=..., output_dim=...):
        ...

# 在 finetune.py 中:
sdf_head = init_module(SDFDecoderHead, "sdf_head", cfg, device_id,
    {"input_dim": vla.module.llm_dim, ...}, to_bf16=True)

# 训练循环中:
last_hidden_states = language_model_output.hidden_states[-1]  # (B, seq_len, 4096)
# 可取任意位置的 hidden states 输入 SDF decoder
sdf_pred = sdf_head(last_hidden_states[:, vision_positions, :])
```

**优势**: Action Head 已经是独立 nn.Module，有独立 optimizer 参数、独立保存/加载。模式成熟，添加新 head 完全遵循相同 pattern。

**关键文件**:
- `prismatic/models/action_heads.py` — Action Head 定义（SDF Head 模板）
- `prismatic/extern/hf/modeling_prismatic.py` — HF 兼容模型，forward + predict_action
- `vla-scripts/finetune.py` — 训练循环、head 初始化、loss 计算
- `prismatic/models/projectors.py` — Projector 定义

---

## 4. Action Token Intermediate Features 分析

### 4.1 openpi

| 特征 | 维度 | 位置 |
|------|------|------|
| Prefix output (视觉+语言) | `[B, ~636, 2048]` | Expert 0, 18 层后 |
| Suffix output (state+action) | `[B, 1+action_horizon, 1024]` | Expert 1, 18 层后 |
| **Action features (SDF 最佳挂载点)** | **`[B, action_horizon, 1024]`** | Expert 1 最后一层 |
| 中间层特征 | 需修改 scan loop (JAX) 或 hook (PyTorch) | 每层均可 |

**可访问性**:
- JAX 版本：层级特征需修改 `nn.scan` loop，不够方便
- **PyTorch 版本**：`gemma_pytorch.py` 中层级循环是显式 for-loop，可直接添加 hook 或在循环中截取，**推荐使用 PyTorch 版本**

### 4.2 OpenVLA-OFT

| 特征 | 维度 | 位置 |
|------|------|------|
| Vision patch embeddings | `[B, 256, 4096]` (经 projector 后) | LLM 输入层 |
| 全序列 hidden states | `[B, seq_len, 4096]` | 每层均可 (32+1 层) |
| **Action token hidden states** | **`[B, NUM_ACTIONS_CHUNK*ACTION_DIM, 4096]`** | 最后一层（已有提取逻辑） |
| Projector features (pre-LLM 视觉) | 需 `output_projector_features=True` | Projector 输出 |

**可访问性**:
- `output_hidden_states=True` 已是默认行为，返回所有 32 层 + embedding 层的 hidden states
- 序列布局：`[BOS] [vision_patches(256)] [proprio(1)] [text_tokens] [action_tokens(K*D)] [STOP]`
- **已有成熟的 hidden state 提取和路由机制**

---

## 5. 对比与推荐

### 关键维度对比

| 维度 | openpi (π0) | OpenVLA-OFT | ColliForce-VLA 偏好 |
|------|------------|-------------|-------------------|
| Action 中间表示维度 | 1024 | 4096 | 4096 更丰富 ✓ |
| 添加辅助 Head 难度 | 中等（需改模型类） | **低（独立模块模式成熟）** | OFT ✓ |
| Hidden state 可访问性 | JAX 需改 scan; PyTorch 可行 | **开箱即用** | OFT ✓ |
| 训练框架 | JAX FSDP (主) / PyTorch DDP (辅) | **PyTorch FSDP/DDP** | OFT ✓ |
| 模型质量 (LIBERO) | 高（π0 预训练数据 10k+ 小时） | **97.1% 成功率** | 相当 |
| 推理速度 | 10 步 ODE (~10x 前向) | **1 次前向** | OFT ✓ |
| 社区活跃度 | 11.9k stars, 活跃维护 | 1.2k stars, 较少维护 | openpi ✓ |
| SDF 梯度传播 | Flow matching ODE loop 需 differentiable solver | **单次前向，梯度直接回传** | OFT ✓ |
| 模型规模 | ~2.5B (2B + 300M) | 7B | openpi 更轻量 ✓ |

### 推荐：OpenVLA-OFT 作为 MVP 基座

**理由**:

1. **辅助任务集成最简单**: Action Head 已是独立 nn.Module，有成熟的初始化、训练、保存模式。添加 SDF decoder 完全遵循现有 pattern，无需修改核心模型类。

2. **Hidden state 访问开箱即用**: `output_hidden_states=True` 已是标准流程，返回所有 32 层 hidden states。序列中每个位置（视觉、语言、action）的 hidden state 都可直接提取。

3. **梯度传播友好**: 单次前向+L1 回归，action 预测完全可微。SDF gradient 可直接通过 action head hidden states 回传到 backbone，无需处理 ODE solver 的梯度问题（openpi 的 flow matching 需要 10 步 Euler 循环）。

4. **纯 PyTorch 生态**: 与大多数 ML 研究工具链兼容（wandb、accelerate、deepspeed 等），调试方便。

5. **4096 维 hidden state**: 比 openpi 的 1024 维 action expert 表示更丰富，为 SDF decoder 提供更多信息容量。

**openpi 作为备选的优势**:
- 更小模型（2.5B vs 7B），显存/速度友好
- 社区更活跃，长期维护有保障
- Flow matching 架构本身优雅
- 如果后续需要更强的预训练基础（10k+ 小时机器人数据），openpi 有明显优势

---

## 6. Blockers 与风险

### OpenVLA-OFT
- **仓库维护活跃度较低**: 论文发布后更新不频繁，遇到 bug 可能需要自行修复
- **模型较大 (7B)**: 训练需要更多 GPU 显存；单卡 A100 80GB 可跑但余量不大
- **Llama-2 7B 作为 backbone**: 不是最新的 LLM，但对 VLA 任务影响不大

### openpi
- **JAX/Flax 为主**: 如果团队 PyTorch 经验为主，开发效率受影响（虽有 PyTorch 版但功能不完整）
- **Flow matching ODE 的梯度**: 10 步 Euler 循环的梯度回传需要 differentiable ODE solver 或 adjoint method，增加 SDF 集成复杂度
- **双专家架构**: 修改需要理解两个 expert 的交互机制，学习曲线较陡

### 共同风险
- 两个仓库都没有 SDF 相关功能的先例，集成需要从零开始
- 训练数据格式需要扩展以包含 SDF ground truth
- Action refinement (用 SDF gradient 修正 action) 的具体实现方式需要进一步设计

---

## 7. 下一步建议

1. **Fork openvla-oft**，在 `prismatic/models/action_heads.py` 中实现 `SDFDecoderHead`
2. 先用 dummy SDF target 验证训练流程跑通（梯度正常回传、loss 下降）
3. 再接入真实的可微分 workspace SDF 模块
4. 如果 7B 模型显存压力过大，再考虑切换到 openpi PyTorch 版本（1024 维 action expert 仍然足够）
