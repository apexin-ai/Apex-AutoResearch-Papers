# OpenVLA-OFT 代码调研报告

> 调研日期：2026-05-20

---

## 1. 官方仓库

### OpenVLA (主仓库)
- **URL**: https://github.com/openvla/openvla
- **Stars**: ~6,200 | **Forks**: ~734
- **License**: MIT
- **维护状况**: 活跃，63 commits on main，2025年3月更新 README 链接 OFT
- **论文**: [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) (ICML 2024)
- **机构**: Stanford, UC Berkeley, Google DeepMind, Toyota Research Institute

### OpenVLA-OFT
- **URL**: https://github.com/moojink/openvla-oft
- **Stars**: ~1,200 | **Forks**: ~169
- **License**: MIT
- **项目主页**: https://openvla-oft.github.io/
- **论文**: [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) (RSS 2025)
- **作者**: Moo Jin Kim, Chelsea Finn, Percy Liang (Stanford)
- **OFT 含义**: Optimized Fine-Tuning（非 Orthogonal Fine-Tuning）

### SafeLIBERO / VLSA-AEGIS
- **URL**: https://github.com/THU-RCSCT/vlsa-aegis | **Stars**: ~98
- **License**: MIT
- **论文**: [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)
- **数据集**: https://huggingface.co/datasets/THURCSCT/SafeLIBERO (638 MB, eval-only)

---

## 2. 依赖和环境要求

### Python 环境
| 依赖 | 版本 |
|------|------|
| Python | 3.10 |
| PyTorch | 2.2.0 |
| torchvision | 0.17.0 |
| transformers | **自定义 fork**: `git+https://github.com/moojink/transformers-openvla-oft.git` (双向注意力) |
| peft | 0.11.1 |
| timm | 0.9.10 |
| flash-attn | 2.5.5 |
| tensorflow | 2.15.0 (RLDS 数据加载) |
| tensorflow_datasets | 4.9.3 |
| diffusers | 0.30.3 |
| accelerate | ≥0.25.0 |
| dlimp | 自定义 fork: `git+https://github.com/moojink/dlimp_openvla` |
| draccus | 0.8.0 |

### 特殊依赖说明
- **transformers 必须用自定义 fork**：修改了 `modeling_llama.py`，将 causal mask 替换为 bidirectional attention（55 行改动）
- **flash-attn 2.5.5**：需要 `pip install packaging ninja && pip install "flash-attn==2.5.5" --no-build-isolation`
- **tensorflow**：仅用于 RLDS 数据加载，非训练依赖
- **LIBERO 评估额外依赖**：robosuite==1.4.1, bddl, gym, imageio[ffmpeg]

### GPU 显存要求

| 场景 | 显存需求 | 说明 |
|------|---------|------|
| 推理 (LIBERO) | ~16 GB | 单 GPU |
| 推理 (ALOHA, 3 images) | ~18 GB | 单 GPU |
| 训练 batch_size=8 | ~62 GB | A100 80GB 刚好够 |
| 训练 batch_size=8, 8 GPUs | ~62 GB × 8 | 论文实验配置 |

**结论：A100 80GB 单卡可跑训练（batch_size=8），推理无压力。**

### 参数高效方法支持
- **LoRA**: 原生支持，默认开启 (`use_lora=True`, rank=32, alpha=16, target="all-linear")
- **QLoRA**: 代码中未见明确支持，但 PEFT 0.11.1 技术上可以配合 bitsandbytes
- **Full fine-tuning**: 可关闭 LoRA，但显存需求极高（7.5B 参数）

---

## 3. Fine-tuning 流程

### 仓库目录结构
```
openvla-oft/
├── pyproject.toml
├── SETUP.md / LIBERO.md / ALOHA.md
├── vla-scripts/
│   ├── finetune.py                  # 主训练脚本
│   ├── deploy.py                    # 部署服务
│   └── merge_lora_weights_and_save.py
├── prismatic/
│   ├── models/
│   │   ├── vlas/openvla.py          # OpenVLA wrapper
│   │   ├── vlms/prismatic.py        # PrismaticVLM base
│   │   ├── action_heads.py          # L1Regression + Diffusion heads
│   │   ├── film_vit_wrapper.py      # FiLM 语言条件化 ViT
│   │   ├── projectors.py            # ProprioProjector + NoisyActionProjector
│   │   └── load.py
│   ├── vla/
│   │   ├── constants.py             # 平台常量 (LIBERO/ALOHA/BRIDGE)
│   │   ├── action_tokenizer.py
│   │   └── datasets/                # RLDS 数据加载
│   └── training/
│       └── train_utils.py
├── experiments/robot/
│   ├── openvla_utils.py             # 推理工具函数
│   └── libero/
│       ├── run_libero_eval.py       # LIBERO 评估
│       ├── regenerate_libero_dataset.py  # HDF5 → RLDS 转换
│       └── libero_requirements.txt
```

### 训练命令
```bash
torchrun --standalone --nnodes 1 --nproc-per-node {NUM_GPUS} vla-scripts/finetune.py \
  --vla_path openvla/openvla-7b \
  --data_root_dir /PATH/TO/RLDS/DATASETS/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True \
  --use_diffusion False \
  --use_film False \
  --num_images_in_input 2 \
  --use_proprio True \
  --batch_size 8 \
  --learning_rate 5e-4 \
  --num_steps_before_decay 100000 \
  --max_steps 150005 \
  --save_freq 10000 \
  --image_aug True \
  --lora_rank 32
```

### 默认超参数

| 参数 | 值 | 说明 |
|------|-----|------|
| learning_rate | 5e-4 | AdamW |
| batch_size | 8 | per-device |
| max_steps | 200,000 (通用) / 150,005 (LIBERO) | — |
| lr_warmup_steps | 0 | 可选线性 warmup |
| num_steps_before_decay | 100,000 | 之后 LR × 0.1 |
| lora_rank | 32 | — |
| lora_alpha | 16 | min(rank, 16) |
| lora_dropout | 0.0 | — |
| image_aug | True | random crop + color jitter |
| grad_accumulation_steps | 1 | — |
| shuffle_buffer_size | 100,000 | RLDS streaming |

### LR Schedule
- `MultiStepLR(milestones=[100000], gamma=0.1)` — 在 100K step 衰减 10×
- 可选 linear warmup (默认关闭)

### 数据格式
- **要求**: RLDS (TFRecord) 格式
- **LIBERO 转换**: HDF5 → RLDS，使用 `experiments/robot/libero/regenerate_libero_dataset.py`
- **预转换数据集**: `git clone git@hf.co:datasets/openvla/modified_libero_rlds` (~10 GB)
- **OXE config 字段**:
  - `image_obs_keys`: primary (agentview), wrist (eye_in_hand)
  - `state_obs_keys`: EEF_state (6D), gripper_state (2D) → 8D proprio
  - `action_encoding`: EEF_POS, 7D (xyz + rotation + gripper)
- **No-op 过滤**: 零动作 transition 在 RLDS 转换时移除
- **图像**: 转换时旋转 180°，训练时 random crop augmentation

### LIBERO 数据集名称
- `libero_spatial_no_noops`
- `libero_object_no_noops`
- `libero_goal_no_noops`
- `libero_10_no_noops`
- `libero_4_task_suites_no_noops` (combined, 权重均为 1.0)

### 训练时间估计
- LIBERO 单 suite (500 demos): 150K steps
- 论文用 8× A100/H100，batch_size=64-128 total
- **单卡 A100 80GB 估计**: batch_size=8, ~150K steps ≈ **2-3 天**

### 已有 HuggingFace Checkpoints
| Checkpoint | Steps | 说明 |
|-----------|-------|------|
| `moojink/openvla-7b-oft-finetuned-libero-spatial` | 150K | — |
| `moojink/openvla-7b-oft-finetuned-libero-object` | 150K | — |
| `moojink/openvla-7b-oft-finetuned-libero-goal` | 50K | 注意 step 数不同 |
| `moojink/openvla-7b-oft-finetuned-libero-10` | 150K | — |
| `moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10` | 300K | Combined model, 96.8% avg |

### LIBERO 结果 (论文 Table I)

**Third-person + wrist + proprio + language (modified dataset)**:

| Policy | Spatial | Object | Goal | Long | Average |
|--------|---------|--------|------|------|---------|
| Diffusion Policy (scratch) | 78.3 | 92.5 | 68.3 | 50.5 | 72.4 |
| OpenVLA (fine-tuned) | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 |
| pi0 (fine-tuned) | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| **OpenVLA-OFT** | **97.6** | **98.4** | **97.9** | **94.5** | **97.1** |

### 推理效率 (论文 Table II, A100)

| Method | Throughput (Hz) | Latency (sec) |
|--------|----------------|---------------|
| OpenVLA (original) | 4.2 | 0.240 |
| OpenVLA-OFT (L1) | 109.7 | 0.073 |
| OpenVLA-OFT + extra inputs | 71.4 | 0.112 |

26× throughput improvement, 3× lower latency.

---

## 4. SafeLIBERO 适配

### 现有 LIBERO 支持
OpenVLA-OFT **原生支持 LIBERO fine-tuning**，包含：
- 数据转换脚本 (`regenerate_libero_dataset.py`)
- 预转换 RLDS 数据集 (HuggingFace)
- 完整评估脚本 (`run_libero_eval.py`)
- 每个 suite 的预训练 checkpoint

### SafeLIBERO 兼容性分析

| 维度 | OpenVLA-OFT 预期 | SafeLIBERO 实际 | 兼容性 |
|------|-----------------|----------------|--------|
| Action space | 7D (6 EE + 1 gripper) | 7D (相同) | ✅ 完全兼容 |
| Observation | agentview RGB + wrist RGB | 相同（LIBERO 环境） | ✅ 完全兼容 |
| Proprio | 8D (6 EEF + 2 gripper) | 相同（LIBERO 环境） | ✅ 完全兼容 |
| 数据格式 | RLDS (TFRecord) | `.pruned_init` (仅初始化状态) | ⚠️ 不兼容 |
| 训练数据 | 需要 demo trajectories | 无（eval-only benchmark） | ❌ 需要自己生成 |
| 障碍物标注 | — | 仅初始位置 (in init vector) | ⚠️ 无逐帧标注 |

### 关键发现

**SafeLIBERO 是纯评估 benchmark，不提供训练数据。** 它提供的是：
- 场景初始化文件 (`.pruned_init`): 50 行，每行是 `[Robot qpos] + [Obj poses(7)] + [Robot qvel] + [Obj vels(6)]`
- 碰撞检测逻辑 (displacement > 0.001)
- 评估协议 (4 suites × 4 tasks × 2 levels × 50 episodes = 1,600 episodes)
- 障碍物类型: Moka pots, storage boxes, milk cartons, wine bottles, mugs, books

**VLSA-AEGIS 的方法**: 推理时 post-processing，不修改模型
1. VLM (GLM-4.5V) 识别障碍物 → GroundingDINO 定位
2. RGB-D → 点云 → DBSCAN 聚类 → MVEE 椭球拟合
3. CBF-QP 约束求解: `u_safe = argmin ||u - u_vla||²` s.t. safety barrier
4. 开销仅 0.356 ms (1.86% cycle time)
5. 结果: +59.16% collision avoidance, +17.25% task success

### 适配工作清单

1. **训练数据生成**（必须，最高优先级）
   - 在 SafeLIBERO 场景中用现有 LIBERO policy 收集带障碍物的 demonstrations
   - 或使用 scripted policy / teleoperation 生成 safety-aware demos
   - 需要同时记录 occupancy ground truth（从 MuJoCo sim 中提取）

2. **Occupancy 标注生成**（必须）
   - 从 LIBERO/MuJoCo 仿真环境中提取 3D 物体位置和碰撞体
   - 生成 voxel occupancy grid 或 BEV occupancy map
   - 需要自定义 LIBERO wrapper 在每个 timestep 导出

3. **RLDS 格式扩展**（必须）
   - 在 RLDS dataset 中添加 occupancy field
   - 修改 `RLDSBatchTransform` 以加载 occupancy labels
   - 修改 OXE config 添加 occupancy key

4. **评估集成**（中等）
   - 修改 `run_libero_eval.py` 在 SafeLIBERO 场景中评估
   - 添加碰撞率 / obstacle avoidance rate 指标
   - 严格复用 VLSA-AEGIS 评估代码保证可比性

### 第三方相关工作

| 项目 | 关系 | URL |
|------|------|-----|
| VLSA-AEGIS | 用 OpenVLA-OFT 作为 baseline，CBF safety layer (inference-only) | https://github.com/THU-RCSCT/vlsa-aegis |
| QDepth-VLA | 最接近的 auxiliary head 先例（depth prediction on SigLIP features） | arXiv:2510.14836 |
| SafeVLA | CMDP + safe RL, NeurIPS 2025 Spotlight | https://github.com/PKU-Alignment/SafeVLA |
| CoFreeVLA | 双臂碰撞避免，learned risk estimator | arXiv:2601.21712 |
| RoboOccWorld | 室内 3D occupancy 场景预测 (不含 VLA) | arXiv:2505.05512 |
| LIBERO-PRO | LIBERO 评估扩展，含 OpenVLA 评估 | https://github.com/Zxy-MLlab/LIBERO-PRO |

---

## 5. 占据辅助头集成可行性

### 架构分析

OpenVLA-OFT 前向传播流程：
```
Images (224×224) → [SigLIP + DINOv2] → 256 patches/image × 2 views = 512 visual tokens
                                              ↓ (3-layer MLP projector, GELU)
Language → Llama-2 tokenizer → text tokens
                                              ↓
Proprio → ProprioProjector (2-layer MLP, GELU) → proprio token
                                              ↓
[visual tokens | text tokens | proprio token | action tokens] → Llama-2 7B (bidirectional attn)
                                              ↓
Hidden states at action positions → reshape to (B, chunk_len, action_dim * hidden_dim)
                                              ↓
L1RegressionActionHead (MLPResNet, 2 blocks) → 8×7 continuous actions
```

### 可加入辅助头的位置

| 位置 | 优势 | 劣势 | 先例 |
|------|------|------|------|
| **A) Vision encoder 输出后** ⭐推荐 | 不干扰语言语义对齐；空间信息最丰富；16×16 空间结构保留 | 仅视觉特征，无语言/proprio 上下文 | QDepth-VLA |
| B) LLM 最后层 hidden states | 融合了全部模态信息 | 可能干扰 action 预测；hidden states 已无空间结构 | — |
| C) FiLM ViT 中间层 | 有语言条件化的视觉特征 | 需要 `use_film=True`；中间层特征不稳定 | — |

### Vision Encoder 输出规格

| 属性 | 值 |
|------|-----|
| 输入分辨率 | 224×224 |
| SigLIP patch size | 14×14 → 16×16 grid |
| DINOv2 patch size | 14×14 → 16×16 grid |
| 每张图输出 | 256 patch embeddings |
| 特征维度 | SigLIP dim + DINOv2 dim (fused) → 投影到 4096 (llm_dim) |
| 空间分辨率 | 16×16 per image |
| 双目输入 | 2 views × 256 = 512 visual tokens total |

### OFT 6 项核心改动
1. **Parallel decoding** — bidirectional attention (非 causal)
2. **Action chunking** — LIBERO: K=8 steps, D=7 dims per step
3. **Continuous action** — [-1, +1] 归一化，替代 256-bin 离散化
4. **L1 regression head** — MLPResNet(2 blocks, input=llm_dim×ACTION_DIM, hidden=llm_dim)
5. **Multi-image** — 共享 ViT 处理多视角，沿 sequence 拼接
6. **FiLM conditioning** (OFT+ variant) — `x = (1+γ)⊙x + β`，per ViT block

### Action Head 详细架构
```python
# L1RegressionActionHead
MLPResNet(
    num_blocks=2,
    input_dim=llm_dim * ACTION_DIM,    # 4096 * 7 = 28672
    hidden_dim=llm_dim,                 # 4096
    output_dim=action_dim               # 7
)
# Input: hidden states at action positions, reshaped to (B, chunk_len, action_dim * hidden_dim)
# Output: (B, chunk_len, action_dim) = (B, 8, 7) continuous actions
# Loss: L1Loss
```

### LIBERO 平台常量
```python
NUM_ACTIONS_CHUNK = 8
ACTION_DIM = 7
PROPRIO_DIM = 8
ACTION_TOKEN_BEGIN_IDX = 31743
```

### Occupancy Head 设计建议

```python
class OccupancyHead(nn.Module):
    """Auxiliary occupancy prediction from fused ViT features."""
    # Input: visual features [B, 256, D_fused] per view (before LLM projection)
    # Output: BEV occupancy [B, H, W] or 3D voxel [B, X, Y, Z]
    
    # Option 1: Lightweight MLP + reshape (类似 QDepth-VLA)
    #   256 patches → MLP → 16×16 BEV grid → upsample → target resolution
    
    # Option 2: Cross-view transformer + 3D lifting
    #   Dual-view features → cross-attention → 3D voxel queries → occupancy logits
    
    # Option 3: BEV projection (最轻量)
    #   Flatten dual-view features → linear → BEV grid (H×W) → sigmoid
```

### 多任务/辅助损失先例

| 方法 | 辅助任务 | 架构位置 | 损失权重策略 |
|------|---------|---------|-------------|
| QDepth-VLA | 量化深度预测 (VQ-VAE, K=256, 16×16) | SigLIP 输出后，LLM 融合前 | 指数衰减 λ₀=0.01 |
| RT-2 | 无辅助 | — | — |
| VLSA-AEGIS | 无训练 (inference-time CBF) | — | — |
| **本项目 (提议)** | 3D occupancy / BEV occupancy | Fused ViT 输出后 | 参考 QDepth-VLA 衰减 |

### 训练策略建议
- **Loss**: `L_total = L_action (L1) + λ(t) * L_occupancy (BCE / focal loss)`
- **λ schedule**: 参考 QDepth-VLA 指数衰减 (λ₀=0.01)，避免辅助任务干扰主任务收敛
- **LoRA 兼容性**: occupancy head 全参数训练，VLA backbone 仅 LoRA，不冲突
- **梯度流选择**:
  - 方案 A: 梯度回传到 vision encoder (端到端，可能提升空间感知)
  - 方案 B: detach visual features (纯 auxiliary supervision，更安全)
  - 建议先 B 后 A

---

## 6. 风险与挑战

### 高风险
| 风险 | 影响 | 缓解措施 |
|------|------|---------|
| **Occupancy GT 生成困难** — SafeLIBERO 无现成标注，需从仿真提取 | 阻塞整个 pipeline | 写 MuJoCo wrapper 提取 collision body → voxelization；先用简化版 (BEV) 验证 |
| **自定义 transformers fork** — 依赖作者修改版，版本锁定于 Llama-2 | 后续升级困难，与新版 transformers 不兼容 | 将 bidirectional attention patch 最小化并记录 diff；长期考虑 port 到 transformers 4.x |
| **训练数据不足** — 标准 LIBERO 每 suite 仅 500 demos，SafeLIBERO 场景更少 | 辅助头欠拟合 | 在 sim 中批量生成 + 数据增强（obstacle 位置随机化） |

### 中等风险
| 风险 | 影响 | 缓解措施 |
|------|------|---------|
| **辅助头干扰 action 预测** — 多任务学习可能降低主任务性能 | 成功率下降 | 梯度 detach / 权重衰减 schedule / 先冻结主任务再联合训练 |
| **显存压力** — 加入 occupancy head + 3D output 增加显存 | batch_size 需缩小 | 用 BEV (2D) 替代 3D voxel；gradient checkpointing；混合精度 |
| **评估协议不统一** — SafeLIBERO 碰撞检测逻辑需嵌入评估脚本 | 结果与 VLSA-AEGIS 不可比 | 严格复用 VLSA-AEGIS 评估代码 |
| **GPU 间 performance 差异** — 论文提到不同 GPU 上性能可能显著下降 | 在非 A100 上结果不稳定 | 统一使用 A100 80GB |

### 低风险
| 风险 | 影响 | 缓解措施 |
|------|------|---------|
| LoRA + 辅助头训练稳定性 | 训练不收敛 | 参考 QDepth-VLA 的 loss weight schedule |
| RLDS 格式扩展 | 数据加载 bug | 单元测试 + 小 batch 验证 |
| 评估时 center_crop 遗漏 | 性能异常低 | 文档已明确要求 `center_crop=True` |

---

## 7. 预估工作量

| 阶段 | 任务 | 预估时间 | 前置依赖 |
|------|------|---------|---------|
| **Phase 1: 环境搭建** | 配置 OpenVLA-OFT 训练环境，安装依赖（含自定义 fork），跑通 inference | 2-3 天 | GPU 服务器就绪 |
| **Phase 2: Baseline 复现** | 用预训练 checkpoint 在标准 LIBERO + SafeLIBERO 上评估，确认 baseline 数字 | 1-2 天 | Phase 1 |
| **Phase 3: 数据 Pipeline** | 编写 MuJoCo wrapper 提取 occupancy GT；在 SafeLIBERO 场景中生成训练数据；转换为扩展 RLDS 格式 | 5-7 天 | Phase 1 |
| **Phase 4: 模型修改** | 实现 OccupancyHead，修改 forward pass，添加多任务 loss，修改数据加载 | 3-5 天 | Phase 3 |
| **Phase 5: 训练** | 在 A100 上训练 occupancy-augmented OpenVLA-OFT；调参 | 3-5 天 (含调参) | Phase 4 |
| **Phase 6: 评估与消融** | SafeLIBERO 全评估 + 消融实验 + 结果分析 + 与 VLSA-AEGIS baseline 对比 | 3-4 天 | Phase 5 |
| **总计** | — | **~3-4 周** | — |

### 关键路径
```
环境搭建 (P1) → 数据 Pipeline (P3) → 模型修改 (P4) → 训练 (P5) → 评估 (P6)
                  ↑ 最不确定环节
Baseline 复现 (P2) 可与 P3 并行
```

Phase 3（数据生成）是最不确定的环节——MuJoCo/LIBERO 环境搭建和 occupancy 提取可能因版本兼容性问题耗时更久。

---

## 8. 核心结论

1. **OpenVLA-OFT 原生支持 LIBERO**——有完整的 fine-tuning pipeline、预训练 checkpoint、评估脚本，适配成本低
2. **SafeLIBERO 是 eval-only benchmark**——需要自行生成带 occupancy 标注的训练数据，这是最大工作量
3. **辅助头最佳位置**：SigLIP+DINOv2 fused visual features 输出后（LLM projection 前），参考 QDepth-VLA 的设计
4. **A100 80GB 单卡够用**（batch_size=8 训练 ~62GB），加 occupancy head 后用 BEV (2D) 可控制显存增量
5. **学术新颖性明确**：目前无人将 occupancy prediction 作为 auxiliary head 集成到 VLA 中
   - QDepth-VLA 验证了 auxiliary geometric supervision 可行（depth）
   - VLSA-AEGIS 验证了 safety constraint + OpenVLA-OFT 可行（inference-only CBF）
   - 本项目填补两者之间的 gap：learned occupancy-aware safety，端到端训练
6. **License 无障碍**：OpenVLA-OFT (MIT)、SafeLIBERO (MIT)、VLSA-AEGIS (MIT) 均为开放许可
