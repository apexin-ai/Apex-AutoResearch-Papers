# OpenVLA Re-encoding 可行性评估

## 1. OpenVLA Vision Token 架构

| 组件 | 输出 | 维度 |
|------|------|------|
| DINOv2 ViT-L/14 | 256 tokens (16×16 patches, 224px/14) | 1024 |
| SigLIP ViT-So400M/14 | 256 tokens (同上) | 1152 |
| Channel-wise concat | 256 tokens | 2176 (1024+1152) |
| 2-layer MLP projector | 256 tokens | 4096 (= Llama-2 hidden_size) |

- **单图输入（OpenVLA 原版）**: 256 tokens × 4096 dim → Llama-2 7B
- **双图输入（OpenVLA-OFT）**: 512 tokens × 4096 dim → Llama-2 7B
- LLM backbone: Llama-2 7B（hidden_size=4096, num_attention_heads=32）
- 动作表示: 离散 tokenization（256 bins per action dim），自回归预测

## 2. 现有 Smart Compress 架构（SmolVLA）

### VisionTokenCompressor 模块
- **输入**: N=128 tokens × D=960 dim（SigLIP → pixel-shuffle connector 输出，2 cameras 拼接）
- **输出**: M=32 queries × D=960 dim（可配置 M=16/32/64/96/128）
- **结构**: M 个 learnable queries + 2 层 CrossAttentionBlock（pre-norm cross-attention + FFN）
- **参数量**: ~22M（hidden_dim=960, num_heads=12, num_layers=2, FFN ratio=4x）
- **代码**: `smart_compress_module.py` — `VisionTokenCompressor` + `SmartCompressWrapper`

### 插入位置
```
SigLIP(frozen) → connector(frozen) → 128 tokens × 960
    → VisionTokenCompressor(trainable) → M tokens × 960
    → VLM text model(frozen) + action expert(trainable) → action loss (MSE)
```

### 冻结策略
- **冻结**: SigLIP encoder + pixel-shuffle connector + VLM text model
- **可训练**: VisionTokenCompressor (~22M) + action expert + state/action projections
- 总可训练参数约占模型 5-10%

### 训练配置
- 数据: LIBERO (HuggingFaceVLA/libero)，2 cameras，state_dim=8, action_dim=7
- 优化器: AdamW, lr=1e-4, warmup=1000, total_steps=100K
- 损失函数: MSE on continuous actions（flow matching denoising）
- batch_size=4, 单 GPU 训练

## 3. 适配方案

### 3.1 维度调整

| 参数 | SmolVLA | OpenVLA | 变化 |
|------|---------|---------|------|
| hidden_dim | 960 | 4096 | 4.3x |
| 输入 tokens | 128 | 256 (或 512 for OFT) | 2-4x |
| num_heads | 12 | 32 | 2.7x |
| num_layers | 2 | 2 (可保持) | 不变 |
| VTC 参数量 | ~22M | ~403M | 18x |

VTC 在 4096 dim 下每层参数:
- Cross-attention (Q/K/V/O): 4 × 4096² ≈ 67M
- FFN (4x expansion): 2 × 4096 × 16384 ≈ 134M
- 每层 ~201M，2 层 ~403M

### 3.2 插入位置

```
DINOv2+SigLIP(frozen) → MLP projector(frozen) → 256 tokens × 4096
    → VisionTokenCompressor(trainable) → M tokens × 4096
    → Llama-2 7B(frozen + LoRA) → action token prediction (cross-entropy)
```

插入在 MLP projector 之后、LLM 之前，与 SmolVLA 方案逻辑一致。

### 3.3 训练策略: 必须搭配 LoRA

**关键差异**: SmolVLA 有独立的 action expert 模块可以适配压缩后的 token，OpenVLA 的 LLM 本身就是 action predictor。如果完全冻结 LLM，压缩 token 必须完美替代原始 token——这远比 SmolVLA 的设定更难。

**推荐方案**: VTC + LoRA on Llama-2
- VTC ~403M 参数全部可训练
- Llama-2 加 LoRA（rank=16），额外 ~8-16M 可训练参数
- 总可训练: ~420M / 7.6B ≈ 5.5%

**备选方案**: 两阶段训练
1. Stage 1: VTC distillation — 最小化压缩 token 与原始 token 在 LLM 输出分布上的 KL 散度
2. Stage 2: VTC + LoRA end-to-end fine-tune on action prediction

### 3.4 损失函数适配

SmolVLA 用 MSE（连续动作 + flow matching），OpenVLA 用 cross-entropy（离散 action tokens, 256 bins）。需要将 `SmartCompressWrapper.forward()` 中的损失计算从 MSE 改为 autoregressive cross-entropy，对接 OpenVLA 的 action tokenization。

### 3.5 需要改动的代码

| 文件 | 类型 | 估计行数 | 说明 |
|------|------|----------|------|
| `openvla_compress_module.py` | 新建 | ~300 | OpenVLA-specific wrapper，处理双 encoder fusion、action tokenization |
| `train_openvla_smart_compress.py` | 新建 | ~250 | 训练脚本，CE loss、LoRA 初始化、OpenVLA 数据加载 |
| `configs/openvla_smart_compress.yaml` | 新建 | ~40 | 配置文件 |
| `VisionTokenCompressor` | 复用 | 0 | 核心模块无需修改，只改 hidden_dim 参数 |
| **总计** | | **~590** | 3 个新文件，0 个修改 |

VisionTokenCompressor 本身是维度无关的（hidden_dim 作为参数传入），无需修改代码，只需在 config 中设 hidden_dim=4096, num_heads=32。

## 4. 训练成本估算

### 显存需求
| 组件 | FP16 显存 |
|------|-----------|
| OpenVLA 7B (frozen) | ~14 GB |
| VTC 403M (trainable) | ~0.8 GB |
| LoRA adapters | ~0.03 GB |
| AdamW 优化器状态 (VTC) | ~3.2 GB |
| 激活值 + 梯度 (batch_size=4) | ~15-25 GB |
| **总计** | **~35-45 GB** |

### 训练时间估算
- SmolVLA Smart Compress: 100K steps, batch_size=4, ~10 hours on 1× RTX 4090
- OpenVLA forward pass: ~50x slower (7B vs 135M LLM, 256 vs 128 tokens)
- 但 LLM 冻结 + 只需 prefix forward（不需要 autoregressive decoding during training）: 实际约 10-20x
- **预估**: 100K steps → 4-8 天 on 1× A100 80GB, 或 1-2 天 on 4× A100 80GB
- 用 gradient checkpointing 可降低显存至 ~30GB，适配 1× A100 40GB

### GPU 需求
- **最低**: 1× A100 80GB（或 2× A100 40GB with model parallel）
- **推荐**: 4× A100 80GB（加速训练 + 更大 batch size）
- 当前服务器 RTX 4090 24GB 不够（需 35-45GB）

## 5. 风险和挑战

### 高风险
1. **LLM 适配困难**: OpenVLA 没有独立 action expert，LLM 必须直接处理压缩 token。即使加 LoRA，7B 参数的 LLM 对 LoRA 的适配能力可能不足以弥补信息损失。
2. **离散 action tokenization 对压缩更敏感**: 连续动作的 MSE loss 容忍小误差，但离散 token 的 cross-entropy 对每个 token 的预测都要求精确，信息损失可能导致错误的 action bin 选择。

### 中风险
3. **VTC 模块过大**: 403M 参数的 VTC 本身就接近一个中等 LLM 的规模，训练不稳定风险增加。可考虑降低 FFN ratio（4x→2x）或减少层数（2→1）以降至 ~100-200M。
4. **计算成本高**: 需要 A100 级 GPU，当前 4090 无法直接训练。
5. **双 encoder 特征融合**: DINOv2+SigLIP 的 fused 特征可能比 SmolVLA 的 SigLIP-only 特征有更复杂的信息结构，VTC 需要更强的压缩能力。

### 低风险
6. **代码适配工作量可控**: VTC 核心模块可直接复用，主要工作在 wrapper 和训练脚本。
7. **数据兼容性**: OpenVLA 和 SmolVLA 都可以在 LIBERO 上训练，数据流水线改动小。

## 6. 现有相关工作

| 方法 | 类型 | 压缩率 | 性能 | 备注 |
|------|------|--------|------|------|
| **Compressor-VLA** (2025.11) | 训练式，双通道压缩 (STC+SRC) | 512→160 (3.2x) | 97.1% (vs OFT 97.3%) | 最接近我们方案，instruction-guided |
| **TEAM-VLA** (2025.12) | Training-free, token merge | 1.5x speedup | 99.2% (vs OFT 97.6%) | 无需训练，但压缩率低 |
| **FlashVLA** (2025) | Training-free, action reuse | 55.7% FLOPs↓ | 竞争力强 | 动作级复用，非 token 压缩 |
| **SP-VLA** (2025) | 联合调度+剪枝 | - | - | 系统级优化 |
| **VLA-Cache** (2025) | KV cache 优化 | - | - | 推理时缓存背景 token |

**Compressor-VLA 是最直接的竞品/参考**，验证了 cross-attention 压缩在 OpenVLA 上可行。其双通道设计（语义+空间）值得借鉴。

## 7. 结论和建议

### 可行性评分: 3.5 / 5

**技术上可行，但需要显著的工程和计算投入。**

### 核心判断
- VisionTokenCompressor 的 cross-attention 架构是维度无关的，适配 OpenVLA 的 4096 dim 只需改参数
- 但 OpenVLA 缺少独立 action expert 这一事实，使得"冻结 LLM + 只训 VTC"的策略比 SmolVLA 难度大得多，必须搭配 LoRA
- Compressor-VLA 已经验证了类似方法在 OpenVLA 上可行（512→160, 97.1%），说明 cross-attention 压缩确实 work
- 主要瓶颈是计算资源：需要 A100 80GB 级别 GPU，当前 4090 不够

### 建议
1. **如果目标是验证方法通用性**: 值得做，~600 行代码 + 1-2 周 A100 训练时间
2. **如果目标是超越 Compressor-VLA**: 需要设计差异化（如 importance-margin guidance, adaptive compression ratio），否则难以形成贡献
3. **快速验证路径**: 先在 OpenVLA 上做 training-free 的 random token pruning 实验（类似 SmolVLA 上已做过的），确认 OpenVLA 对 token 压缩的敏感度曲线，再决定是否投入训练式压缩
4. **计算资源**: 申请或租用 A100 80GB 实例（AutoDL A100 约 3-5 元/小时），预算约 500-1000 元完成初步验证
