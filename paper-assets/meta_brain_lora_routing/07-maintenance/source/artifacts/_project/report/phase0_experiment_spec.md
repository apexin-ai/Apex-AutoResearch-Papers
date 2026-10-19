# Phase 0 Experiment Specification: Perturbation-Type Classifiability from π₀ Internal Activations

> **项目**: Meta-Brain: Perturbation-Adaptive LoRA Routing
> **版本**: v1.0 | **日期**: 2026-05-15
> **关联决策**: D001 (MVP 定义), D002 (Reviewer 增强), D003 (架构修正)
> **目标会议**: CoRL 2026 — Abstract DDL 2026-05-26, Paper DDL 2026-05-29

---

## 1. 实验目标

**核心假设**: π₀ 内部激活（PaliGemma + Action Expert 的 Transformer hidden states）编码了扰动类型信息，可被轻量级 2-layer MLP probe 分类。

**Phase 0 定位**: Early-kill gate。整个 Meta-Brain 方法论依赖"扰动类型可从 VLA 内部激活诊断"这一前提——若此假设不成立，后续所有工作（LoRA bank、routing、Correction Memory）全部无效。Phase 0 以最小成本（~20 H100-hrs, 4 天）验证这一前提，给出 GO/NO-GO 判定。

**通过 → Phase 1**: LoRA Expert 训练（3 个 perturbation-specific LoRA adapters）。
**不通过 → Pivot**: 放弃 type-specific routing，退化为 universal LoRA + Correction Memory。

---

## 2. 扰动 Taxonomy

### 2.1 LIBERO-Plus 原始 7 类

LIBERO-Plus (CVPR 2026) 定义 7 个扰动维度：

| # | 扰动类型 | 定义 | π₀ baseline 成功率 |
|---|----------|------|-------------------|
| 1 | Camera Viewpoints | 改变相机位置/角度（高度、俯仰角、水平旋转） | 13.8% |
| 2 | Light Conditions | 改变场景光照（亮度、色温、方向性） | 85.0% |
| 3 | Background Textures | 改变背景/桌面纹理（图案、材质替换） | 81.4% |
| 4 | Sensor Noise | 在观测图像叠加噪声（高斯、椒盐） | — |
| 5 | Objects Layout | 重排工作空间物体位置 | — |
| 6 | Robot Initial States | 改变机器人起始关节角度/末端位置 | 6.0% |
| 7 | Language Instructions | 改写任务指令措辞 | — |

**π₀ baseline 总体平均**: 53.6%（LIBERO-Plus 报告值）

### 2.2 排除 Language Instructions

Language Instructions 被排除出本实验的 taxonomy。

**理由**: Meta-Brain 的 LoRA 修正作用于 visual/action token representation。语言扰动（指令改写/同义替换）影响的是文本输入编码，而非视觉-动作表征空间。语言扰动在 tokenization 阶段就已产生差异，不属于 LoRA 在 mid-to-late 层修正 visual token 的设计范围。此外，语言鲁棒性可通过 prompt engineering 或 text augmentation 单独解决，不需要 LoRA routing。

### 2.3 7→3 映射定义

| 3-class | 包含的 LIBERO-Plus 类型 | 映射理由 |
|---------|------------------------|----------|
| **Visual** | Camera Viewpoints, Light Conditions, Background Textures, Sensor Noise | 均扰动视觉输入流，影响 visual token representation。LoRA-V 定位 early-to-mid 层修正视觉分布偏移（camera→视角变换, light→亮度/色温, background→纹理域, noise→信噪比）。修正机制相同：校准 ViT 编码后的 visual token 在 LLM 层中的 cross-modal attention pattern |
| **Spatial** | Objects Layout | 扰动物体-动作空间映射。物体位置改变导致学习到的 reach/grasp 轨迹失效。LoRA-S 定位 mid 层调整空间注意力权重，重新对齐 spatial token 与 action planning |
| **Physical** | Robot Initial States | 扰动初始运动学状态。起始关节角/末端位置改变导致动作解码的 initial condition 错误。LoRA-P 定位 late 层调整动作解码，补偿运动学偏移 |

### 2.4 Visual 类内方差风险

Visual 类内性能差异显著：Camera 13.8% vs Light 85.0% vs Background 81.4%。Camera 扰动的严重性远高于 Light/Background。

**风险**: 分类器可能将 Camera 单独聚类，而非与 Light/Background 归为一类。

**缓解**: 6-class 对照实验可检验此风险。若 6-class accuracy > 50% 且 Visual 子类间混淆度低，说明激活空间确实区分了 Camera 与 Light/Background，后续可升级为 6 个 LoRA Expert。

**映射理由**: 尽管严重性差异大，四类扰动的修正机制相同——都是视觉流校准（recalibrating visual token representations after ViT encoding）。LoRA-V 通过修正 early-to-mid 层的 cross-modal attention 来补偿视觉分布偏移，这一机制对 camera/light/background/noise 均适用。

---

## 3. 模型架构

### 3.1 π₀ Backbone

| 组件 | 参数 |
|------|------|
| **PaliGemma VLM** | SigLIP So400m/14 (ViT, ~400M params) + Gemma 2B LLM |
| **Gemma 2B** | 18 layers, hidden_dim=2048, mlp_dim=16384, 8 heads (MQA, 1 KV head), head_dim=256 |
| **Action Expert** | Gemma 300M, 18 layers, hidden_dim=1024, mlp_dim=4096, 8 heads (MQA) |
| **总参数量** | ~3.3B |
| **动作生成** | Flow matching, 10-step Euler integration |

### 3.2 激活提取层

| Transformer | 提取层 (0-indexed) | 层数 | Hidden dim |
|-------------|-------------------|------|------------|
| PaliGemma (Gemma 2B) | {2, 4, 6, 8, 10, 12, 14, 16} | 8 | 2048 |
| Action Expert (Gemma 300M) | {2, 6, 10, 14} | 4 | 1024 |
| **合计** | | **12** | |

> ⚠️ **修正说明**: IDEA_BRIEF 原写 layers {4, 8, 12, 16, 20, 24, 28, 32}，基于错误的 32 层假设。π₀ 实际使用 Gemma 2B (18 layers, index 0-17)。已修正为 18 层范围内的均匀采样。（决策 D003）

**PyTorch hook 路径**:
- PaliGemma: `model.paligemma_with_expert.paligemma.language_model.layers[i]` (i=0..17)
- Action Expert: `model.paligemma_with_expert.gemma_expert.model.layers[i]` (i=0..17)

### 3.3 分类器架构

与 SAFE (NeurIPS 2025) 保持一致：

```
Input (pooled activations) → Linear(input_dim, 256) → ReLU → Linear(256, num_classes)
```

- **Hidden dim**: 256
- **Activation**: ReLU
- **Loss**: Cross-entropy (3-class, 6-class), BCE (binary)
- **Optimizer**: AdamW
- **Training**: 50 epochs, batch_size=64, 5-fold cross-validation

**Input dim 计算** (以 `both` + `mean` pooling 为例):
- PaliGemma: 8 layers × 2048 = 16,384
- Action Expert: 4 layers × 1024 = 4,096
- Total: 20,480

---

## 4. 数据收集方案

### 4.1 Episode 分布

| 条件 | Episodes | 说明 |
|------|----------|------|
| Nominal (无扰动) | ~100 | Binary anomaly detection 的 negative class |
| Camera Viewpoints | ~80 | |
| Light Conditions | ~80 | |
| Background Textures | ~80 | |
| Sensor Noise | ~80 | |
| Objects Layout | ~80 | |
| Robot Initial States | ~80 | |
| **总计** | **~580** | |

覆盖 LIBERO 全 4 个 task suite (Spatial/Object/Goal/Long)，每个 suite 内均匀采样任务。

### 4.2 每 Episode 采集内容

每次 π₀ 推理（每 5 env steps 一次，每 episode ~40-80 次推理）记录：

1. **PaliGemma 8 层 hidden states** — 按 4 种 pooling 策略存储
2. **Action Expert 4 层 hidden states** — 按 4 种 pooling 策略存储
3. **元数据**: episode_id, task_name, perturbation_type, step_idx, success/failure

### 4.3 Pooling 策略

同时存储 4 种 pooling 结果，在训练阶段选择最优：

| Pooling | 操作 | 输出维度 (per layer) |
|---------|------|---------------------|
| `mean` | 全序列 mean pooling | hidden_dim |
| `first` | 取第一个 token | hidden_dim |
| `last` | 取最后一个 token | hidden_dim |
| `first_last` | 拼接 first + last token | hidden_dim × 2 |

### 4.4 存储估算

使用 pooled fp16 (方案 D)：

| 指标 | 值 |
|------|-----|
| 每次推理 (12 层, mean pooling, fp16) | 12 × (2048+1024)/12 × 2 ≈ 36 KB |
| 更精确：PaliGemma 8×2048×2 + Expert 4×1024×2 | 32,768 + 8,192 = 40,960 B ≈ 40 KB |
| 4 种 pooling | ×4 ≈ 160 KB |
| 每 episode (60 次推理, 4 pooling) | ~9.6 MB |
| 580 episodes | **~5.4 GB** |
| 仅 mean pooling (主方案) | **~0.95 GB** |

磁盘预算充裕。4 种 pooling 全存储 (~5.4 GB) 可承受，避免二次采集。

---

## 5. 评估 Protocol

### 5.A 3-class 分类（主实验）

**类别**: Visual / Spatial / Physical

**数据**: 480 perturbed episodes (排除 nominal)，按 7→3 映射。
- Visual: ~320 episodes (camera + light + background + noise)
- Spatial: ~80 episodes (layout)
- Physical: ~80 episodes (robot)

> 注意类别不平衡：Visual 占 ~67%。使用 class-weighted loss 或 balanced sampling。

**指标**:
- Overall accuracy
- Per-class accuracy / precision / recall / F1
- Macro-F1 (类别不平衡下比 accuracy 更有信息量)
- 3×3 normalized confusion matrix (行归一化 = recall, 列归一化 = precision)

### 5.B 6-class 分类（对照实验）

**类别**: Camera / Light / Background / Noise / Layout / Robot

**数据**: 同 5.A 的 480 perturbed episodes，保持原始 6 类标签。

**指标**:
- 同 5.A 全部指标
- 6×6 normalized confusion matrix
- Visual 子类间混淆矩阵（Camera vs Light vs Background vs Noise）

**用途**: 若 6-class accuracy > 50%（chance = 16.7%），证明激活空间对 fine-grained 扰动类型有区分力，后续可用 6 个 LoRA Expert 替代 3 个。

### 5.C Binary anomaly detection（Sanity check）

**类别**: Nominal / Perturbed

**数据**: 全部 580 episodes（100 nominal + 480 perturbed）。

**指标**:
- ROC-AUC
- Precision-Recall curve + AUC-PR
- F1 @ optimal threshold

**用途**: Binary 是比 3-class 更弱的假设。
- Binary 失败（ROC-AUC < 0.70）→ 激活提取本身有问题（hook 位置/pooling/数据质量），需排查基础设施。
- Binary 成功但 3-class 失败 → 激活编码了"有扰动"但未编码扰动类型，需增强输入（+ proprioception + visual change detection）。

### 5.D Cross-cutting 分析

**D1. Per-layer accuracy breakdown**

对每个单独层训练分类器，绘制 layer index vs accuracy 曲线。揭示扰动信息在哪些层最富集。

**D2. PaliGemma-only vs Action Expert-only vs Combined**

| 激活源 | 输入层 | 预期信号 |
|--------|--------|----------|
| PaliGemma-only | 8 层, 2048-dim | Visual 和 Spatial 扰动（视觉-语言融合空间） |
| Expert-only | 4 层, 1024-dim | Physical 扰动（动作解码空间） |
| Both (Combined) | 12 层 | 全部扰动类型 |

对比三种 activation source 的分类性能，验证双 Transformer 互补假设。

**D3. Pooling 策略对比**

3 pooling (mean / first / first_last) × 3 activation source × 3 classifier mode，报告最优组合。

**D4. t-SNE / UMAP 可视化**

对最优层组合的 pooled activations 做降维可视化：
- 按 3-class 着色
- 按 6-class 着色
- 按 nominal/perturbed 着色

直观展示聚类结构。如果 3-class 不可分但 binary 可分，可视化会直接暴露。

---

## 6. Hyperparameter Sweep

### 6.1 Sweep Grid

| 维度 | 值 | 数量 |
|------|-----|------|
| Pooling | mean, first, first_last | 3 |
| Activation source | paligemma_only, expert_only, both | 3 |
| Learning rate | 1e-2, 1e-3, 1e-4 | 3 |

**每个 classifier mode**: 3 × 3 × 3 = **27 configs**

### 6.2 总训练量

| Classifier mode | Configs | CV folds | Total runs |
|-----------------|---------|----------|------------|
| 3-class | 27 | 5 | 135 |
| 6-class | 27 | 5 | 135 |
| Binary | 27 | 5 | 135 |
| **合计** | | | **405** |

### 6.3 时间估算

- 每个 config (50 epochs, batch_size=64, ~580 episodes): **< 15 min** on single H100
- 27 configs × 5 folds × 3 modes = 405 runs × 15 min = ~101 hours (sequential)
- 4 GPU 并行: ~25 hours → **约 1 天**
- 实际更快：大部分 config 的数据集很小（pooled activations），训练在 CPU 上几分钟内完成

---

## 7. GO/NO-GO 判据

| 条件 | 判定 | 行动 |
|------|------|------|
| Binary ROC-AUC ≥ 0.75 **且** 3-class macro-F1 > 70% **且** confusion matrix 无严重混淆 (任意两类间 > 30%) | **GO** | 进入 Phase 1 LoRA Expert 训练 |
| Binary ROC-AUC ≥ 0.75 **且** 3-class macro-F1 50-70% | **AUGMENT** | 增强 router 输入：+ proprioception history + visual change detection features。2 天 contingency (Days 5-6)。重新训练 PAR，若提升至 >70% → GO |
| Binary ROC-AUC < 0.70 | **RETHINK** | 激活提取有根本问题。排查：换层选择 / 换 pooling 策略 / 换 token 位置（action-only vs full-seq） / 检查 hook 实现 |
| Binary ROC-AUC ≥ 0.75 **但** 3-class macro-F1 < 50% | **PIVOT** | 激活编码了"有扰动"但未编码类型。放弃 type-specific routing，退化为 universal LoRA + Correction Memory |
| 6-class accuracy > 50% | **信息** | 可升级为 6 个 LoRA Expert（更细粒度 routing） |
| Confusion matrix 某两类 > 30% 互相混淆 | **信息** | 考虑合并该两类或重定义 taxonomy |

### 7.1 Chance-level 参考

| Mode | Chance level | GO 阈值 | 倍数 |
|------|-------------|---------|------|
| Binary | 50% (class-balanced) | 75% ROC-AUC | 1.5× |
| 3-class | 33.3% (均匀) / 66.7% (majority class) | 70% macro-F1 | 2.1× / 1.05× |
| 6-class | 16.7% | 50% accuracy | 3.0× |

> 3-class 因 Visual 占 ~67%，majority-class baseline 已经很高。用 macro-F1 而非 accuracy 作为判据，避免被 Visual 的高占比拉高 overall accuracy 掩盖 Spatial/Physical 的差表现。

---

## 8. 资源预算

### 8.1 计算资源

| 阶段 | 内容 | H100-hrs | 墙钟时间 |
|------|------|----------|---------|
| 数据收集 | 冻结 π₀ rollout 580 episodes + 激活记录 | ~15 | 1-2 天 (4 GPU 并行) |
| 分类器训练 + sweep | 405 runs (3 modes × 27 configs × 5 folds) | ~5 | 0.5-1 天 |
| **Phase 0 总计** | | **~20** | **2-4 天** |

### 8.2 详细时间线

| Day | 内容 | GPU 利用 |
|-----|------|---------|
| Day 1 | 环境搭建：OpenPI + LIBERO-Plus + PyTorch hooks | 0 (setup) |
| Day 1-2 | 数据收集：冻结 π₀ rollout 580 episodes，记录 12 层 pooled activations | 4× H100 并行 rollout |
| Day 3 | 分类器训练 + hyperparameter sweep | 4× H100 并行 sweep |
| Day 4 | 评估 + 可视化 + GO/NO-GO 判定 | 1× H100 (eval) |

### 8.3 存储需求

| 内容 | 大小 |
|------|------|
| Pooled activations (4 pooling, fp16) | ~5.4 GB |
| π₀ checkpoint (bf16) | ~6.6 GB |
| 分类器 checkpoints (405 runs) | ~1 GB |
| LIBERO-Plus 环境 + 依赖 | ~10 GB |
| **总计** | **~23 GB** |

### 8.4 硬件需求

- **最低**: 1× H100 80GB（可完成全部实验，墙钟时间 ~5-7 天）
- **推荐**: 4× H100 80GB（并行 rollout + sweep，墙钟时间 ~2-4 天）
- **LoRA 微调显存**: > 22.5 GB（Phase 0 不需要，Phase 1 才用）
- **推理显存**: > 8 GB (bf16)

---

## 9. 风险与缓解

| 风险 | 严重性 | 说明 | 缓解方案 |
|------|--------|------|----------|
| **PyTorch LoRA 用社区 PR** | 🟡 中 | Issue #842 的实现未合并到 OpenPI 主线 | 代码完整可用（26.5M params, 96.95% on LIBERO）；Phase 0 不需要 LoRA，仅需 inference hooks |
| **层索引已修正** | ✅ 已解决 | 原 {4,8,12,16,20,24,28,32} 基于 32 层假设 | 修正为 PaliGemma {2,4,6,8,10,12,14,16} + Expert {2,6,10,14}（D003） |
| **激活存储量** | 🟢 低 | Pooled fp16 控制在 ~5.4 GB | 远小于磁盘预算，无需压缩 |
| **LIBERO-Plus 集成** | 🟢 低 | "直接替换 LIBERO 库"，评测代码无需修改 | Docker 隔离环境；唯一改动 num_trials=1 |
| **3-class 类别不平衡** | 🟡 中 | Visual ~67% / Spatial ~17% / Physical ~17% | Class-weighted loss + balanced sampling + 用 macro-F1 替代 accuracy |
| **Hook 实现正确性** | 🟡 中 | PyTorch forward hook 可能改变计算图或显存 | Phase 0 开始前先验证：对比有/无 hook 的 action 输出一致性 |
| **Rollout 耗时超预期** | 🟡 中 | 580 episodes × 30-60s each ≈ 5-10 hours (单 GPU) | 4 GPU 并行 → 1.5-2.5 hours；nohup 后台执行 |
| **分类器过拟合** | 🟡 中 | 数据量小 (~580 episodes)，分类器可能过拟合 | 5-fold CV 防止 overfitting；2-layer MLP 容量有限（SAFE 同架构） |

---

## 附录 A: 与 SAFE (NeurIPS 2025) 的对比

| 维度 | SAFE | Phase 0 (Meta-Brain) |
|------|------|---------------------|
| 任务 | Binary failure detection | 3-class / 6-class perturbation classification + binary |
| 输入 | Final-layer activations | Multi-layer activations (12 layers, 2 Transformers) |
| 分类器 | 2-layer MLP, hidden=256 | 同 SAFE |
| Pooling | Mean over sequence | Mean / first / last / first+last (sweep) |
| 数据规模 | Unseen tasks, zero-shot | Task-specific, same-task |
| 性能 | 78.0% ROC-AUC (binary) | 目标：>75% ROC-AUC (binary), >70% macro-F1 (3-class) |

Phase 0 比 SAFE 的优势：(1) 多层而非仅 final-layer，信号更丰富；(2) 双 Transformer 提供互补信号；(3) same-task 而非 zero-shot，降低难度。
Phase 0 比 SAFE 的劣势：(1) multi-class 比 binary 更难；(2) 某些扰动类型间的边界可能模糊。

## 附录 B: 已有代码基础

`artifacts/phase0/configs.py` 已定义：

- `PERTURBATION_TYPES_6CLASS` / `PERTURBATION_TYPES_3CLASS` — 类别映射
- `CLASS_6_TO_3_MAPPING` — 7→3 映射表
- `PALIGEMMA_LAYERS` / `EXPERT_LAYERS` — 激活提取层
- `POOLING_STRATEGIES` — pooling 策略
- `SWEEP_POOLINGS` / `SWEEP_SOURCES` / `SWEEP_LRS` — sweep grid
- `GO_NOGO` — 阈值（注：configs.py 中阈值偏保守，以本文档第 7 节为准）
- `compute_input_dim()` — 分类器输入维度计算

待实现：
- 激活提取 hook (`ActivationExtractor`)
- 数据收集 pipeline (rollout + hook + save)
- 分类器训练/评估 (train + sweep + 5-fold CV)
- 可视化 (confusion matrix + t-SNE/UMAP)

## 附录 C: π₀ LIBERO-Plus Baseline 参考值

来源：LIBERO-Plus 论文 + VLA-GSE (2605.06175)

| 方法 | LIBERO-Plus 均值 | Camera | Light | Background | Robot | Noise | Layout |
|------|-----------------|--------|-------|------------|-------|-------|--------|
| π₀ (frozen) | 53.6% | 13.8% | 85.0% | 81.4% | 6.0% | — | — |
| VLA-GSE (Qwen3-VL-4B) | 81.2% | 64.4% | 97.3% | 97.3% | 68.5% | 79.4% | 82.6% |
| SRPO | 82.1% | — | — | — | — | — | — |
| CorridorVLA | 83.21% | — (按 task category 报告) | | | | | |

Camera 和 Robot 是 π₀ 最薄弱的两个维度，也是 Meta-Brain routing 最有价值的修正目标。
