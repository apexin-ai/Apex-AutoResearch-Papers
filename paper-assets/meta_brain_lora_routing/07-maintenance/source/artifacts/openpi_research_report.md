# OpenPI (π₀) Codebase 深度技术调研报告

> 调研日期：2026-05-15
> 目标：评估在 π₀ 上实施 Meta-Brain LoRA Routing 的技术可行性

---

## 1. π₀ 模型架构与加载

### 1.1 整体架构

π₀ 是 Vision-Language-Action (VLA) flow model，基于 PaliGemma 2B VLM 扩展而来，采用 MoE-like 架构（Mixture of Tokens, MoT）。

**核心组件**：
- **视觉编码器**: SigLIP So400m/14（~400M 参数）
- **语言模型 (PaliGemma backbone)**: Gemma 2B（~2.6B 参数）
- **动作专家 (Action Expert)**: Gemma 300M（~315M 参数，从零初始化）
- **投影层**: action_in_proj, action_out_proj, time MLPs

**代码位置**:
- JAX 实现: `src/openpi/models/pi0.py` (Pi0 class, lines 47-176)
- PyTorch 实现: `src/openpi/models_pytorch/pi0_pytorch.py` (PI0Pytorch class)
- 配置: `src/openpi/models/pi0_config.py`
- Gemma 定义: `src/openpi/models/gemma.py` (JAX), `src/openpi/models_pytorch/gemma_pytorch.py` (PyTorch)

### 1.2 详细架构参数

| 组件 | 参数 | 值 |
|------|------|-----|
| **Gemma 2B (PaliGemma LLM)** | width (hidden_dim) | 2048 |
| | depth (层数) | **18** |
| | mlp_dim | 16,384 |
| | num_heads | 8 |
| | num_kv_heads | 1 (Multi-Query Attention) |
| | head_dim | 256 |
| **Gemma 300M (Action Expert)** | width | 1024 |
| | depth | **18** |
| | mlp_dim | 4,096 |
| | num_heads | 8 |
| | num_kv_heads | 1 |
| | head_dim | 256 |
| **SigLIP So400m/14** | embedding_dim | ~1152 |
| | patch_size | 14×14 |
| | input_resolution | 224×224 |
| | patches/image | 256 (16×16) |

**来源**: `src/openpi/models/gemma.py` 中的 variant 定义:
```python
# gemma_2b: width=2048, depth=18, mlp_dim=16384, num_heads=8, num_kv_heads=1, head_dim=256
# gemma_300m: width=1024, depth=18, mlp_dim=4096, num_heads=8, num_kv_heads=1, head_dim=256
```

### 1.3 注意力机制

采用 block-wise causal masking（`src/openpi/models/pi0.py`, lines 20-38）:
- VLM block: 仅关注自身（prefix tokens: images + language）
- State/proprioception block: 关注自身 + VLM（共享 action expert 权重）
- Action block: 关注所有 tokens（完全双向）

**来源**: `make_attn_mask()` 函数，通过 cumulative mask 实现不同的注意力模式。

### 1.4 动作生成 (Flow Matching)

**训练** (`compute_loss`, lines 119-150):
- 时间步 t ~ Beta(1.5, 1)，缩放到 [0.001, 0.999]
- 噪声状态: x_t = t·noise + (1-t)·actions
- 目标速度: u_t = noise - actions
- 损失: MSE(v_t, u_t)

**推理** (`sample_actions`, lines 152-201):
- 10 步 Euler 积分: t=1 (噪声) → t=0 (目标)
- 步长: dt = -1/num_steps = -0.1
- 迭代: x_{t+dt} = x_t + dt·v_t
- 使用 KV-cache 优化 prefix tokens

### 1.5 Checkpoint 来源与大小

| Checkpoint | 来源 | 格式 |
|------------|------|------|
| pi0_base | `gs://openpi-assets/checkpoints/pi0_base/params` | JAX (Flax) |
| pi0_fast_base | `gs://openpi-assets/checkpoints/pi0_fast_base/params` | JAX (Flax) |
| pi05_base | `gs://openpi-assets/checkpoints/pi05_base/params` | JAX (Flax) |
| lerobot/pi0_base | HuggingFace Hub | SafeTensors (PyTorch) |
| lerobot/pi0_libero_base | HuggingFace Hub | SafeTensors (PyTorch) |

**自动下载**：默认缓存到 `~/.cache/openpi`，可通过 `OPENPI_DATA_HOME` 修改。无需申请，直接公开下载。

**模型大小**:
- 总参数量: ~3.3B（HuggingFace 标注为 4B，含 F32 精度下的 embeddings/projections）
- Checkpoint 大小 (fp32): ~13.2 GB
- Checkpoint 大小 (bf16): ~6.6 GB

### 1.6 显存需求

| 模式 | 显存需求 | 推荐 GPU |
|------|---------|----------|
| 推理 (bf16) | > 8 GB | RTX 4090 / A6000 |
| LoRA 微调 | > 22.5 GB | RTX 4090 / A6000 |
| 全量微调 | > 70 GB | A100 80GB / H100 |

**来源**: OpenPI README 文档。

### 1.7 加载方式

**OpenPI 原生 (JAX)**:
```python
# src/openpi/training/config.py
model = config.model.create(model_rng)
# 通过 _load_weights_and_validate() 加载预训练权重
```

**OpenPI PyTorch**:
```python
import openpi.models_pytorch.pi0_pytorch
import safetensors.torch
model = PI0Pytorch(model_cfg).to(device)
safetensors.torch.load_model(model, model_path)
```

**LeRobot (HuggingFace)**:
```python
from lerobot.policies.pi0 import PI0Policy
policy = PI0Policy.from_pretrained("lerobot/pi0_base").to(device).eval()
```

---

## 2. LIBERO 环境集成

### 2.1 已有 LIBERO 支持

OpenPI 对 LIBERO 有**完整的一等支持**：

**关键文件**:
- 评测脚本: `examples/libero/main.py`
- 数据转换: `examples/libero/convert_libero_data_to_lerobot.py`
- 策略映射: `src/openpi/policies/libero_policy.py`
- Docker 配置: `examples/libero/Dockerfile`, `examples/libero/compose.yml`
- 训练配置: `src/openpi/training/config.py` 中的 `LeRobotLiberoDataConfig`

**预训练 LIBERO checkpoint**:
- `gs://openpi-assets/checkpoints/pi05_libero/params`（π₀.₅ LIBERO 微调版，96.85% 平均成功率）
- HuggingFace: `lerobot/pi0_libero_base`

### 2.2 LIBERO 评测调用方式

`examples/libero/main.py` 实现了完整的评测流程：

1. 启动 Policy Server: `scripts/serve_policy.py`
2. 客户端通过 WebSocket 连接: `WebsocketClientPolicy(host, port)`
3. 评测循环:
   - 重置环境 → 等待物体稳定 (num_steps_wait)
   - 每 `replan_steps=5` 步请求新 action chunk
   - 记录成功率和视频

**配置格式** (通过命令行参数):
- `--task_suite_name`: LIBERO 任务套件 (spatial/object/goal/10)
- `--num_trials_per_task`: 每个任务的试验次数 (默认 50)
- `--resize_size`: 图像分辨率 (224)
- `SERVER_ARGS`: 指定 checkpoint

**观测格式** (LiberoInputs, `src/openpi/policies/libero_policy.py`):
- State: `observation/state` — 8 维向量（end-effector position + rotation + gripper）
- Base image: `observation/image` — 224×224 RGB（第三人称）
- Wrist image: `observation/wrist_image` — 224×224 RGB（左手腕相机）
- Right wrist: 零填充（LIBERO 只有 2 个相机）

**动作格式** (LiberoOutputs):
- 输出前 7 维动作（从 action_dim=32 的填充中截取）
- 7 维 = 6-DoF end-effector + 1 gripper

### 2.3 LIBERO-Plus 扰动评测

**支持状态**: 可用，但需要额外安装 LIBERO-Plus 替代标准 LIBERO。

**LIBERO-Plus** (https://github.com/sylvestf/LIBERO-plus) 提供 7 个扰动维度:
1. 物体布局 (Objects Layout)
2. 相机视角 (Camera Viewpoints)
3. 机器人初始状态 (Robot Initial States)
4. 语言指令 (Language Instructions)
5. 光照条件 (Light Conditions)
6. 背景纹理 (Background Textures)
7. 传感器噪声 (Sensor Noise)

**集成方式**: "Simply replace the originally installed LIBERO repository with our repository without modifying your code" — 直接替换 LIBERO 库即可，评测代码无需修改。唯一改动: `num_trials_per_task` 从 50 改为 1。

**π₀ 在 LIBERO-Plus 上的基线表现**: 平均 53.6%（光照 85.0%，背景 81.4%，但机器人初始状态仅 6.0%）。

---

## 3. LoRA Fine-tuning 支持

### 3.1 JAX 实现 — 已有完整支持

**代码位置**: `src/openpi/models/lora.py`

**LoRA 变体定义** (`src/openpi/models/gemma.py`):
```
gemma_2b_lora:    rank=16, alpha=16.0 (attn + ffn)
gemma_300m_lora:  rank=32, alpha=32.0 (attn + ffn)
```

**训练配置** (`src/openpi/training/config.py`):
- 使用 `paligemma_variant="gemma_2b_lora"` + `action_expert_variant="gemma_300m_lora"`
- Freeze filter: 冻结非 LoRA 的 LLM 参数，仅训练 LoRA 权重
- EMA decay: 禁用 (`ema_decay=None`)
- 其他默认: 30k steps, batch_size=32, AdamW + Cosine Decay

**LoRA 目标模块**:
- Attention: q_proj, k_proj, v_proj, o_proj (通过 Einsum 类)
- FFN: gate_proj, up_proj, down_proj (通过 FeedForward 类)

**LoRA 实现特点**:
- 支持 RSLoRA (rank-stabilized LoRA): `scaling = alpha / sqrt(rank)`
- 纯 additive: `output = base_output + (x @ w_a @ w_b) * scaling`
- 不依赖外部库（如 peft），自实现

### 3.2 PyTorch 实现 — 官方不支持，社区有方案

**官方状态**: OpenPI 的 PyTorch 训练脚本 (`scripts/train_pytorch.py`) **不支持 LoRA**，仅支持全量微调。

**社区方案** (Issue #842):
- 纯 PyTorch LoRA 实现，不依赖 peft
- 注入到 Attention (q/k/v/o_proj) 和 MLP (gate/up/down_proj)
- Rank=16 时 LoRA 参数: 26.5M (0.73% of total)
- 可选解冻 Vision Encoder: 额外 412M trainable (12.11% total)
- 单 RTX 4090 可训练，~16GB 峰值显存
- LIBERO 上达到 96.95% 平均成功率
- **状态**: PR 未合并，但代码完整可用

**LeRobot 方案**:
- HuggingFace LeRobot 提供了 Pi0 的 PyTorch 训练脚本
- 支持 `train_expert_only=true` 冻结 VLM 仅训练 action expert
- 不原生支持 LoRA，但可通过 HuggingFace PEFT 库扩展

### 3.3 推荐方案

对于本项目的 Meta-Brain LoRA Routing：
1. **首选**: 基于 OpenPI JAX 实现，已有完整 LoRA 支持
2. **备选**: 采用 Issue #842 的 PyTorch LoRA 实现（更灵活，更容易加 hook）
3. **替代**: 使用 LeRobot PyTorch + HuggingFace PEFT 库

---

## 4. 中间层激活提取

### 4.1 模型前向传播路径

**JAX 实现** (`src/openpi/models/pi0.py`):
```
Pi0.__call__()
  → embed_prefix(obs)        # SigLIP 编码图像 + tokenize 文本
  → embed_suffix(obs, noisy_actions, timestep)  # 编码动作 + 时间步
  → self.PaliGemma['llm'](tokens, ...)  # Gemma Module forward (18 layers)
  → action_out_proj(...)     # 投影到动作空间
```

**PyTorch 实现** (`src/openpi/models_pytorch/pi0_pytorch.py`):
```
PI0Pytorch.forward(observation, actions)
  → _preprocess_observation()
  → embed_prefix(obs)
  → embed_suffix(obs, noisy_actions, timestep)
  → paligemma_with_expert(tokens, ...)
  → action_out_proj(...)
```

### 4.2 已有 Hook 机制

**OpenPI 没有已有的 hook 机制或中间层输出接口。** 需要自行添加。

### 4.3 PyTorch Hook 注册方案（推荐）

PyTorch 实现支持标准的 `register_forward_hook`，模块路径如下：

**PaliGemma LLM 层 (hidden_dim=2048)**:
```python
model.paligemma_with_expert.paligemma.language_model.layers[i]
# i = 0..17 (共 18 层)

# 子模块:
model.paligemma_with_expert.paligemma.language_model.layers[i].self_attn
model.paligemma_with_expert.paligemma.language_model.layers[i].self_attn.q_proj
model.paligemma_with_expert.paligemma.language_model.layers[i].self_attn.o_proj
model.paligemma_with_expert.paligemma.language_model.layers[i].mlp
model.paligemma_with_expert.paligemma.language_model.layers[i].input_layernorm
model.paligemma_with_expert.paligemma.language_model.layers[i].post_attention_layernorm
```

**Action Expert 层 (hidden_dim=1024)**:
```python
model.paligemma_with_expert.gemma_expert.model.layers[i]
# i = 0..17 (共 18 层)
# 子模块结构同上
```

**Vision Encoder 层**:
```python
model.paligemma_with_expert.paligemma.vision_tower.layers[i]
```

### 4.4 关键发现：层数只有 18，不是 32！

**⚠️ 重要**: π₀ 的 Transformer 深度为 **18 层**（layers[0]..layers[17]），而非 32 层。

用户原计划提取 layers {4,8,12,16,20,24,28,32} — **其中 layers 20,24,28,32 不存在**。

**推荐调整方案**:
| 原计划 | 可行方案 A (8 层均匀采样) | 可行方案 B (偏重深层) |
|--------|--------------------------|---------------------|
| {4,8,12,16,20,24,28,32} | {1,3,5,7,9,11,13,15} | {2,4,6,8,10,12,14,16} |

**或者同时提取两个 Expert 的激活**（获得更丰富的信息）:
- PaliGemma layers: {2, 5, 8, 11, 14, 17}
- Action Expert layers: {2, 5, 8, 11, 14, 17}
- 共 12 层激活，覆盖两个 transformer

### 4.5 Hook 实现代码示例

```python
class ActivationExtractor:
    def __init__(self, model, layer_indices):
        self.activations = {}
        self.hooks = []
        
        for idx in layer_indices:
            # Hook PaliGemma LLM layers
            layer = model.paligemma_with_expert.paligemma.language_model.layers[idx]
            handle = layer.register_forward_hook(
                lambda module, input, output, idx=idx: 
                    self.activations.__setitem__(f'llm_layer_{idx}', output[0].detach())
            )
            self.hooks.append(handle)
            
            # Hook Action Expert layers
            expert_layer = model.paligemma_with_expert.gemma_expert.model.layers[idx]
            handle = expert_layer.register_forward_hook(
                lambda module, input, output, idx=idx:
                    self.activations.__setitem__(f'expert_layer_{idx}', output[0].detach())
            )
            self.hooks.append(handle)
    
    def remove_hooks(self):
        for h in self.hooks:
            h.remove()
```

---

## 5. 技术估算

### 5.1 序列长度分析

LIBERO 评测时的 token 构成：
| 组件 | Tokens | 说明 |
|------|--------|------|
| Base image | 256 | 224×224 / 14×14 patches |
| Left wrist image | 256 | 224×224 / 14×14 patches |
| Right wrist image | 256 | 零填充（LIBERO 只有 2 相机），但仍占序列位置 |
| Text prompt | 48 | max_token_len (pi0 默认) |
| State | 1 | 投影到 hidden_dim |
| Action tokens | 50 | action_horizon=50 |
| **Total** | **~867** | |

### 5.2 每条 Rollout 激活存储估算

**假设条件**:
- 8 层采样（PaliGemma LLM 层）
- hidden_dim = 2048 (PaliGemma)
- seq_len ≈ 867
- replan_steps = 5，每 5 个 env step 做一次推理
- 每 episode 约 200-400 env steps → ~40-80 次推理

**方案 A: 存储完整序列激活 (fp32)**

| 指标 | 值 |
|------|-----|
| 每次推理每层 | 2048 × 867 × 4 bytes = 7.1 MB |
| 每次推理 8 层 | 56.8 MB |
| 每 episode (60 次推理) | 3.4 GB |
| 500 episodes | **1.7 TB** |

**方案 B: 仅存储 action token 位置的激活 (fp32)**

| 指标 | 值 |
|------|-----|
| 每次推理每层 | 2048 × 50 × 4 bytes = 0.41 MB |
| 每次推理 8 层 | 3.3 MB |
| 每 episode (60 次推理) | 197 MB |
| 500 episodes | **96 GB** |

**方案 C: Action tokens + fp16**

| 指标 | 值 |
|------|-----|
| 每次推理 8 层 | 1.6 MB |
| 每 episode (60 次推理) | 98 MB |
| 500 episodes | **48 GB** |

**方案 D: 池化后的层表征 (mean pooling over seq_len, fp16)**

| 指标 | 值 |
|------|-----|
| 每次推理每层 | 2048 × 2 bytes = 4 KB |
| 每次推理 8 层 | 32 KB |
| 每 episode (60 次推理) | 1.9 MB |
| 500 episodes | **0.95 GB** |

### 5.3 推理速度估算

**来源**: π₀ 论文 (Table 4) 在 RTX 4090 上的测量:
- Image encoding: 14 ms
- Observation forward pass: 32 ms
- 10× action flow passes: 27 ms
- **单次推理总计**: 73 ms

**H100 估算** (约 2× 4090 推理性能):
- 单次推理: ~35-40 ms
- 每 episode (60 次推理): ~2.4 s（纯模型推理时间）
- 加上环境仿真时间: 每 episode 约 30-60 秒
- **500 episodes 总时间**: ~4-8 小时（单 H100）

**注意**: 如果需要存储激活，推理时需额外内存存储 hook 输出，峰值显存约增加 50-100 MB。

### 5.4 训练资源估算

**LoRA 微调 500 episodes 数据**:
- 数据: 500 episodes × ~200 steps × 7-dim action = ~70K 训练样本
- 训练时间 (单 A6000/4090): 10k-30k steps × ~0.5s/step ≈ 1.4-4.2 小时
- 显存: ~16-22 GB (LoRA)

---

## 6. 风险与阻塞项

### 6.1 高风险项

| 风险 | 严重性 | 说明 | 缓解方案 |
|------|--------|------|----------|
| **层数不匹配** | 🔴 高 | 模型仅 18 层，原计划 8 层采样中有 4 层不存在 | 调整为 {2,4,6,8,10,12,14,16} |
| **PyTorch LoRA 未官方支持** | 🟡 中 | PyTorch 训练不原生支持 LoRA，需用社区方案或自实现 | 采用 Issue #842 的实现，或用 JAX 训练 + PyTorch 推理 |
| **激活存储量大** | 🟡 中 | 完整序列存储 500 episodes 需 1.7TB | 使用方案 B/C/D 减少存储 |

### 6.2 中等风险项

| 风险 | 说明 | 缓解方案 |
|------|------|----------|
| JAX vs PyTorch 精度差异 | LeRobot PyTorch 转换后性能有下降，官方建议微调 | 可用 JAX checkpoint 作为 baseline 对比 |
| Flow matching 推理开销 | 每次推理需要 10 步迭代去噪 | 已有 KV-cache 优化，单次 73ms 可接受 |
| LIBERO-Plus 集成 | 需要替换 LIBERO 库，可能有版本兼容问题 | 使用 Docker 隔离环境 |

### 6.3 非阻塞项

- Checkpoint 下载: 公开可用，无需申请
- 数据转换: 已有 LeRobot 格式转换脚本
- 评测脚本: 完整可用，包含 Docker 配置
- 多 GPU 支持: PyTorch DDP 已实现

---

## 7. 推荐技术方案

### 7.1 总体架构

```
[LIBERO Env] → [π₀ with Hooks] → [Activation Buffer]
                     ↓                    ↓
              [Action Output]    [Meta-Brain Router]
                                        ↓
                                 [LoRA Selection]
                                        ↓
                               [Task-Specific LoRA]
```

### 7.2 具体步骤

**Phase 1: 基础设施搭建**
1. 安装 OpenPI (PyTorch 版) + LIBERO 环境
2. 验证 `lerobot/pi0_base` 或 `pi0_libero_base` checkpoint 加载
3. 运行标准 LIBERO 评测确认 baseline 性能

**Phase 2: 激活提取**
1. 在 PyTorch 模型上注册 forward hooks
2. 选择层: PaliGemma layers {2,4,6,8,10,12,14,16}
3. 使用方案 B (action tokens only, fp16): 每 500 episodes ~48 GB
4. 收集 LIBERO 全 4 个 task suite 的激活

**Phase 3: LoRA 训练**
1. 基于 Issue #842 的 PyTorch LoRA 实现
2. 或使用 JAX 原生 LoRA 训练 (gemma_2b_lora + gemma_300m_lora)
3. 每个 task suite 训练一个 LoRA adapter
4. LoRA config: rank=16, alpha=16.0, target=attn+ffn

**Phase 4: Meta-Brain Router**
1. 输入: 中间层激活 (8 layers × hidden_dim)
2. 输出: LoRA adapter 选择/混合权重
3. 训练: 使用收集的激活-任务标签对

### 7.3 硬件需求

| 阶段 | GPU 需求 | 时间估算 |
|------|---------|---------|
| LIBERO 评测 + 激活收集 | 1× H100/A100 | ~8 小时 |
| LoRA 训练 (4 adapters) | 1× A6000/4090 | ~16 小时 |
| Meta-Brain Router 训练 | 1× A6000 | ~2 小时 |
| 总磁盘 | ~100 GB (激活) + ~10 GB (checkpoints) | |

---

## 8. 关键代码引用索引

| 内容 | 文件路径 | 说明 |
|------|---------|------|
| Pi0 模型定义 (JAX) | `src/openpi/models/pi0.py:47-176` | Pi0 class, forward/loss/sample |
| Pi0 模型定义 (PyTorch) | `src/openpi/models_pytorch/pi0_pytorch.py` | PI0Pytorch class |
| Gemma 变体配置 | `src/openpi/models/gemma.py` | width/depth/heads 定义 |
| Gemma PyTorch | `src/openpi/models_pytorch/gemma_pytorch.py` | GemmaForCausalLM 层结构 |
| LoRA 实现 (JAX) | `src/openpi/models/lora.py` | Einsum, FeedForward adapters |
| 模型配置 | `src/openpi/models/pi0_config.py` | Pi0Config dataclass |
| 训练配置 | `src/openpi/training/config.py` | TrainConfig, LIBERO 数据配置 |
| 训练脚本 (JAX) | `scripts/train.py` | JAX 训练循环 |
| 训练脚本 (PyTorch) | `scripts/train_pytorch.py` | PyTorch 训练循环 |
| LIBERO 策略映射 | `src/openpi/policies/libero_policy.py` | LiberoInputs/Outputs |
| LIBERO 评测 | `examples/libero/main.py` | 完整评测流程 |
| 数据转换 | `examples/libero/convert_libero_data_to_lerobot.py` | LIBERO → LeRobot |
| SigLIP 视觉编码器 | `src/openpi/models/siglip.py` | So400m/14 ViT |
| 注意力 mask | `src/openpi/models/pi0.py:20-38` | make_attn_mask() |
| Flow matching | `src/openpi/models/pi0.py:119-150` | compute_loss() |
| 推理采样 | `src/openpi/models/pi0.py:152-201` | sample_actions() |
