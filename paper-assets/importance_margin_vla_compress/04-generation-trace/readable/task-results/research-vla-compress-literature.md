# research vla compress literature

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vla_compress_literature_20260522T103105_result.json`
- **Structured JSON:** [`3a080a9b76fffaf93653.json`](../../sessions/3a/3a080a9b76fffaf93653.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，整理报告。

---

## 1. VLA-Cache (2502.02175)
- **模型**: OpenVLA, OpenVLA-OFT, CogACT
- **Vision encoder / connector**: OpenVLA = SigLIP + MLP projector; CogACT = DINOv2+SigLIP 双编码器
- **Benchmark**: LIBERO (Spatial/Object/Goal/Long), SIMPLER (VM/VA), 真实机器人 (Kinova Jaco2, 4 tasks)
- **压缩率**: 256→100 static tokens (39% retained)，但 task-relevant tokens 重新计算，实际压缩率随层变化
- **性能**:
  - LIBERO: 75.0% → 74.7% (Δ = −0.3%)
  - Real robot: 82.1% → 84.6% (Δ = +2.5%)
  - Latency: 1.63× speedup (LIBERO), 1.24× (real robot)
- **方法**: **KV-cache 复用**（非 pruning）。利用帧间时序连续性，cosine similarity 阈值 τ=0.996 识别静态 token，复用其 KV 表示；cross-attention score 做 task-relevance 过滤，attention entropy 做 layer-adaptive 复用
- **关键发现**: Naive static token reuse 严重退化（84.4%→74.2%）；task-relevance filtering 关键；动态环境下加速增益下降
- **CV taxonomy 相关**: **无**。用 decoder attention score 做 token 选择，未涉及 CV metrics 预测 pruning tolerance

## 2. EfficientVLA (2506.10100)
- **模型**: CogACT only
- **Vision encoder / connector**: DINOv2 + SigLIP 双编码器；connector 未明确说明；LLM backbone = Llama2-7B (32 layers)；Action head = Diffusion Transformer (DiT, 10 steps)
- **Benchmark**: SIMPLER only (Visual Matching / Variant Aggregation, 4 tasks)
- **压缩率**: 256 → 56 tokens (22% retained)；测试了 112/96/72/56 多个档位
- **性能**:
  - Baseline: 74.8% (VM)
  - L=22 layers + T=56 tokens: 74.2% (Δ = −0.6%)
  - L=28 layers + T=56 tokens: 75.5% (Δ = +0.7%)
  - **1.93× speedup, 28.9% FLOPs**
  - Random dropping 灾难性: 256→112 random = **20.9%**（vs 74.8%）
- **方法**: 三合一 training-free 框架: (1) LLM layer pruning (cosine similarity 识别冗余层); (2) Visual token pruning (task-aware: cross-attention score + diversity maximization); (3) Diffusion action head caching (每 5 步缓存中间特征)
- **关键发现**: Token pruning 存在 memory-bound 瓶颈——超过某阈值后进一步减 token 收益递减；Layer pruning 有时反而提升性能；Random drop 灾难性失败是核心发现
- **CV taxonomy 相关**: **无**。未讨论 CV metrics 与 pruning tolerance 的关系

## 3. LightVLA (2509.12594)
- **模型**: OpenVLA-OFT (primary)；对比列表: π0, π0-fast, CogACT, SmolVLA, NORA, WorldVLA, FlashVLA, SP-VLA, VLA-Cache
- **Vision encoder / connector**: DINOv2 + SigLIP 双编码器，MLP projector（D'→D 投影）
- **Benchmark**: LIBERO (Spatial/Object/Goal/Long), 500 trials/suite
- **压缩率**: 512 → **78 tokens avg** (84.4% reduction)
  - Spatial: 90±15, Object: 78±11, Goal: 64±10, Long: 79±11
- **性能**:
  | Method | Spatial | Object | Goal | Long | **Avg** |
  |--------|---------|--------|------|------|---------|
  | OpenVLA-OFT baseline | 95.2% | 94.2% | 95.2% | 93.2% | 94.5% |
  | **LightVLA** | **98.4%** | **98.4%** | **98.2%** | **94.6%** | **97.4%** |
  | FlashVLA | — | — | — | — | 74.4% |
  | SP-VLA | — | — | — | — | 74.9% |
  | VLA-Cache | — | — | — | — | 74.7% |
  - **FLOPs**: 8.8→3.6 TFLOPs (−59.1%)；Latency: 34→21ms (−38.2%)
- **方法**: **Differentiable token pruning**。Language-visual cross-attention 生成 query → token scoring → Gumbel-softmax 做可微选择（straight-through estimator）；训练中学习最优 pruning pattern；无额外参数
- **关键发现**: Pruning 可以**提升**性能（+2.9%）——模型学会去除噪声 token；Gumbel noise schedule 是关键（无 noise 或固定 noise 均退化）；无明显 cliff
- **CV taxonomy 相关**: **无**。未讨论 CV metrics 预测能力。但其核心发现——learned pruning 提升性能——暗示不同 token 的 task-relevance 差异很大，这与 CV taxonomy 思路一致

## 4. VLA-Pruner (2511.16449)
- **模型**: OpenVLA, OpenVLA-OFT, π0
- **Vision encoder / connector**: 论文未明确说明（依赖所测模型自身架构）
- **Benchmark**: LIBERO (4 suites), SIMPLER (3 tasks), 真实机器人 (xArm6, 4 tasks)
- **压缩率**: 测试 50% / 25% / 12.5% retained
- **性能** (OpenVLA on LIBERO):
  | Retention | Spatial | Object | Goal | Long | Relative Acc |
  |-----------|---------|--------|------|------|-------------|
  | Baseline | 87.6% | 84.6% | 78.6% | 52.2% | 100% |
  | 50% | 88.2% | 85.8% | 79.4% | 56.4% | **>100%** |
  | 25% | 85.4% | 82.5% | 78.4% | 51.8% | 98.48% |
  | 12.5% | — | — | — | — | 88.90% |
  - **1.83× speedup, 29.96% FLOPs** (at 87.5% pruning)
  - Real robot (75% pruning): 最高 relative accuracy
- **方法**: **Dual-level plug-and-play token pruning**。(1) Prefill attention score (S_vl) → semantic relevance; (2) Action decode attention score (S_act) → execution precision，用 temporal smoothing (decaying window avg, w=3, γ=0.8) 估计; (3) Union pooling (C_vl ∪ C_act) + mRMR diversity 过滤
- **关键发现**:
  - **Semantic vs action attention 仅 ~50% 重叠（常低于 30%）**——这是核心 insight
  - Temporal smoothing 在 abrupt task switch 时失败（如 LIBERO-Long 连续操作不同物体）
  - Prefill-only 保语义丢操控；Action-only 短期好但丢语义
- **CV taxonomy 相关**: **间接相关**。Semantic/action 双系统发现暗示不同 connector 架构对 semantic vs fine-grained action 信息的传递方式不同，可能影响 pruning 敏感度。但论文本身未做此分析

---

## 综合对比表

| 论文 | 模型 | Vision Enc | Connector | Benchmark | 压缩率 (retained) | 性能保留 | 方法类型 | Training-free? |
|------|------|-----------|-----------|-----------|-------------------|---------|---------|---------------|
| VLA-Cache | OpenVLA, OFT, CogACT | SigLIP / DINOv2+SigLIP | MLP proj | LIBERO, SIMPLER, Real | 39% | −0.3% (LIBERO) | KV-cache 复用 | Yes |
| EfficientVLA | CogACT | DINOv2+SigLIP | — | SIMPLER | 22% | −0.6% | Layer+Token+Diffusion cache | Yes |
| LightVLA | OpenVLA-OFT | DINOv2+SigLIP | MLP proj | LIBERO | 15.2% (78/512) | **+2.9%** | Differentiable token pruning | No (finetune) |
| VLA-Pruner | OpenVLA, OFT, π0 | 依模型 | 依模型 | LIBERO, SIMPLER, Real | 50%/25%/12.5% | 98.5% @25% | Dual-level attention pruning | Yes |

---

## 与我们的关系

### Direct competitor 重叠度

| 维度 | 我们 | VLA-Cache | EfficientVLA | LightVLA | VLA-Pruner |
|------|------|-----------|-------------|----------|-----------|
| **LIBERO** | ✓ | ✓ | ✗ | ✓ | ✓ |
| **OpenVLA** | ✓ | ✓ | ✗ | ✓ (OFT) | ✓ |
| **π0/π0.5** | ✓ (π0.5) | ✗ | ✗ | ✓ (π0 比较) | ✓ (π0) |
| **SmolVLA** | ✓ | ✗ | ✗ | ✓ (比较) | ✗ |

- **LightVLA** 和 **VLA-Pruner** 是最直接的 competitor，模型和 benchmark 重叠最多
- **π0.5** 无任何论文测试过——我们有独占数据点
- **SmolVLA** 只有 LightVLA 提到（作为对比，非 pruning 目标）

### 我们的 CV taxonomy 贡献 novelty

1. **这 4 篇论文全部没有探讨 connector 架构对 pruning 敏感度的影响**——它们要么只测一种模型（EfficientVLA），要么测多种模型但不分析架构差异原因（VLA-Cache, VLA-Pruner）
2. **无论文使用 CV metrics 预测 pruning tolerance**——所有方法都依赖 attention score 或 learned scoring，没有建立 "vision representation quality → compression headroom" 的因果链
3. **VLA-Pruner 的 semantic/action 50% 重叠发现** 是最接近我们思路的 observation，但他们没有追问"为什么不同架构重叠度不同"
4. **LightVLA 的 pruning-improves-performance 现象** 可以用我们的 CV taxonomy 解释：高冗余 token（CV quality 低的区域）被移除后降低了 noise，这正是 CV margin 理论的推论

### 可用于 retrodict 验证的数据点

1. **EfficientVLA random drop 灾难 (74.8%→20.9%)**：CogACT 用 DINOv2+SigLIP 双编码器，token 间 importance 分布极不均匀→ CV taxonomy 应预测高方差 importance 分布
2. **VLA-Cache naive reuse 退化 (84.4%→74.2%)**：OpenVLA (SigLIP + MLP) 的 task-relevant token 若被错误复用→ MLP projector 不做 spatial pooling，位置敏感，CV taxonomy 应预测对 token identity 高度敏感
3. **LightVLA 84% pruning 仍提升性能**：OpenVLA-OFT (DINOv2+SigLIP + MLP) 512 token 有极大冗余→ CV taxonomy 应预测双编码器+MLP 的 token 冗余度很高
4. **VLA-Pruner 12.5% retention 仍保 88.9% accuracy**：极端压缩下 OpenVLA 仍可用→ 暗示 MLP projector 产生的大量 token 中信息高度集中于少数 token
5. **VLA-Pruner π0 结果**（如有具体数据）：π0 用不同 connector，对比 OpenVLA 在同压缩率下的性能差异可 retrodict

Sources:
- [VLA-Cache](https://arxiv.org/abs/2502.02175)
- [EfficientVLA](https://arxiv.org/abs/2506.10100)
- [LightVLA](https://arxiv.org/abs/2509.12594)
- [VLA-Pruner](https://arxiv.org/abs/2511.16449)

---
