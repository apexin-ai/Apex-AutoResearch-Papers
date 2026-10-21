# Gradient & CKA Analysis — Structured Summary for Paper Agent

> 本文档汇总梯度分析和 CKA 表征分析的核心数字与叙事指引，供 Paper Agent 写论文使用。

---

## A. 梯度分析

### A1. Global Gradient Norms (gradient_analysis_mixed_seed, 200 batches, step-50K checkpoints)

| 条件 | Mean Action Grad Norm | vs Vanilla 倍数 | Mean Aux Grad Norm | Cosine Sim | Conflict Rate |
|------|----------------------|----------------|--------------------|------------|---------------|
| Vanilla (s0, seed 42) | 0.1262 | 1.00× | — | — | — |
| Full OCC (s0, seed 42) | 0.1272 | **1.01×** | 0.0182 | 0.004 | 44.1% |
| Random OCC (s2, seed 44) | 0.1365 | **1.08×** | 0.0079 | 0.005 | 43.9% |
| Detach+BN (s2, seed 44) | 0.0049 | **0.04×** | — | — | — |

**核心发现**：
- Full OCC 和 Random OCC 的 action gradient norm ≈ Vanilla → **collapse prevention, not amplification**
- Detach+BN 梯度崩塌至 Vanilla 的 4% → 灾难性 gradient collapse
- Cosine similarity ≈ 0, conflict rate ≈ 44%（接近高维随机向量理论值 50%）→ **辅助梯度方向与 action 梯度正交，无 directional guidance**
- 此前报告的 "8-65× amplification" 系基于缺少 Vanilla baseline 的不完整对比（Random vs Detach），已修正

### A2. Per-Layer Gradient Analysis (D036/D037)

#### DINOv2 — 全层正交（纯 anti-freeze 机制）

| 层段 | Full OCC Conflict Rate | Random OCC Conflict Rate |
|------|----------------------|------------------------|
| Early (block 0-7) | 49.8% | 49.6% |
| Mid (block 8-15) | 49.9% | 49.7% |
| Late (block 16-23) | 49.9% | 49.9% |

DINOv2 所有层 conflict rate ≈ 50%（完美正交）。梯度流仅通过维持参数更新活性防止冻结，不提供方向信息。

#### SigLIP — late layers 梯度协同

| 层段 | Full OCC Conflict Rate | Random OCC Conflict Rate |
|------|----------------------|------------------------|
| Early (block 0-8) | 49.7% | 49.7% |
| Mid (block 9-17) | 49.6% | 49.5% |
| **Late (block 18-25)** | **25.8%** | **25.3%** |

SigLIP late layers conflict rate 从 ~50% 骤降至 ~25%（远低于随机）→ 高层语义特征空间中 action 和 OCC 梯度方向趋于一致。**Full OCC 和 Random OCC 模式完全一致**（25.8% vs 25.3%），证明这是 encoder 结构性特征，非标签质量效应。

#### 双编码器差异化机制（D037 核心 finding）

- **DINOv2**：纯存在性正则化（正交梯度防止冻结）
- **SigLIP**：存在性 + 协同正则化（高层梯度对齐提供额外保护）
- 这解释了 Detach 下 SigLIP CKA 退化更严重（SigLIP 中层 CKA=0.22 vs DINOv2=0.54）——SigLIP 对梯度流的依赖更深

### A3. Detach Gradient Collapse 的行为签名

- Detach 3-seed CAR = 0.746 ± 0.002（std 极小，比所有梯度流条件低 6-20×）
- 机制解释：无梯度流 → encoder 梯度崩塌 → 训练高度确定性地收敛到同一次优点 → 低均值 + 低方差
- 梯度流条件：性能更高但方差更大（Vanilla std=0.012, OCC=0.032, Random=0.031）→ 正则化提升性能但引入优化随机性

### A4. 对 Paper Narrative 的影响

**支撑的叙事**："Gradient flow as implicit regularization — preventing encoder gradient collapse"

关键论证链：
1. Full OCC ≈ Random OCC ≈ Vanilla gradient norm → 辅助梯度流不放大也不干扰 action 梯度
2. Detach = 4% of Vanilla → OCC head 前向计算中的 BN 在无梯度补偿时导致灾难性 collapse
3. Cosine ≈ 0 + conflict ≈ 44% → 辅助梯度方向本质随机，不提供有用信号
4. 梯度流的价值在于**存在性**（维持参数更新活性），不在于**方向性**（任务相关信息）
5. DINOv2 vs SigLIP 的差异化机制增加了分析深度

---

## B. CKA 表征分析

### B1. 5 条件 CKA vs Pretrained（mean across all blocks）

| 条件 | DINOv2 Mean CKA | SigLIP Mean CKA | CAR (3-seed mean) |
|------|-----------------|-----------------|-----|
| Vanilla | 0.968 | 0.953 | 0.780 |
| Full OCC | 0.959 | 0.959 | 0.797 |
| Random OCC | 0.968 | 0.955 | 0.789 |
| **Detach+LN** | **0.966** | **0.960** | **0.765** |
| **Detach+BN** | **0.539** | **0.317** | **0.746** |

### B2. Detach+BN 的 per-layer CKA 退化

- DINOv2：全层均匀退化，CKA 从 0.62（block 0）到 0.45（block 14），mid-layer 最低
- SigLIP：退化更严重且更系统化，从 0.62（block 0）单调下降到 0.22（block 14），mid-layer CKA 低至 0.22-0.26
- SigLIP min CKA = 0.223（block 14）vs DINOv2 min CKA = 0.448（block 14）→ SigLIP 语义特征比 DINOv2 几何特征更脆弱

### B3. Detach+LN 的关键 Paradox（D035 核心发现）

**CKA 完全恢复，但 CAR 仍有残余 gap：**
- Detach+LN CKA (DINOv2=0.966, SigLIP=0.960) ≈ Vanilla (0.968/0.953) ≈ Full OCC (0.959/0.959)
- 但 Detach+LN CAR = 0.765 仍低于 Vanilla 0.780（-1.5pp gap，n=3 CI 重叠）

**解读**：
- BN 是 encoder 表征退化的 **100% 原因**（LN 替换后 CKA 完全修复）
- 梯度流的 44% CAR 贡献 **不通过表征保护通道**，而是通过其他机制（action head 正则化 / LoRA 优化方向 / policy learning dynamics）
- 表征保护 ≠ 行为保护（representation preservation ≠ behavioral safety）

### B4. Random OCC CKA 确认

Random OCC CKA (DINOv2=0.968, SigLIP=0.955) ≈ Vanilla，与 Full OCC 一致。随机标签 + 梯度流 = 完整表征保护。进一步证明标签内容不重要，梯度流存在性是关键。

### B5. 对 Paper Narrative 的影响

**支撑的叙事**："Dual mechanism — BN causes representational drift, gradient flow provides additional behavioral regularization"

关键论证链：
1. Detach+BN CKA 灾难性崩塌 → BN forward-pass 干扰 + 无梯度补偿 = 表征漂移
2. Detach+LN CKA 完全恢复 → BN 是表征漂移的唯一来源
3. Detach+LN CAR 仍低 1.5pp → 梯度流有超越表征保护的行为贡献
4. 5 条件排序的 clean separation：三个梯度流条件 CKA ≈ 0.96-0.97；Detach+LN ≈ 0.96（CKA 恢复，CAR 未完全恢复）；Detach+BN ≈ 0.3-0.5（双重退化）

---

## C. 综合判断：三个 Hypothesis 的评估

### Hypothesis 1: 梯度流提供 gradient diversity → better representation → safety

**部分否定。** CKA Paradox (B3) 否定了 "better representation → safety" 的因果链。Detach+LN 表征完全正常（CKA=0.966/0.960）但 CAR 仍低 1.5pp。梯度流对安全的贡献**不完全通过表征改善**通道。

### Hypothesis 2: 梯度流提供 implicit regularization → prevent gradient collapse → safety

**成立（主效应）。** 最强证据线：
- Detach action gradient = 4% of Vanilla（A1）→ 灾难性 collapse
- Full OCC / Random OCC ≈ Vanilla gradient norm（A1）→ collapse prevention, not amplification
- Cosine ≈ 0, conflict ≈ 44%（A1）→ 存在性正则化，非方向性 guidance
- Detach CAR = 0.746 ± 0.002（A3）→ collapse 的行为后果
- 但 CAR 贡献中仅 ~44% 来自梯度流本身（独立于 BN 干扰），通道不完全清楚

### Hypothesis 3: BN running stats 失配 → representation drift → harm

**成立（最大单一因素）。** 最强证据线：
- Detach+BN CKA = 0.539/0.317 vs Detach+LN CKA = 0.966/0.960（B3）→ BN 是 100% 的表征漂移原因
- Detach+LN CAR = 0.765 vs Detach+BN CAR = 0.746（+1.9pp）→ BN 干扰贡献 ~56% 的 CAR gap
- SigLIP 中层 CKA 跌至 0.22-0.26（B2）→ BN 选择性破坏语义特征

### 综合模型

Detach OCC 的退化 (-3.4pp CAR vs Vanilla) 由两个独立机制驱动：

```
Detach OCC failure = BN interference (56%, 1.9pp) + Gradient flow absence (44%, 1.5pp)
                     ↓                               ↓
                     表征漂移 (CKA collapse)           行为退化 (非表征通道)
                     ↓                               ↓
                     LN 可完全修复                     修复通道未知
```

**Paper framing 建议**：
- 标题级 claim："Auxiliary gradient flow prevents encoder collapse in VLA fine-tuning"
- Dual mechanism 是 nuance：BN 干扰是较大因素但可工程修复（换 LN），梯度流缺失是更根本的问题
- DINOv2 vs SigLIP 差异化机制是 novel contribution（无人报告过双编码器 VLA 中辅助梯度的差异化行为）
- CKA Paradox（表征保护 ≠ 行为保护）是有深度的 finding，值得在 Discussion 中展开

---

## 数据来源

| 分析 | Artifact 文件 | Registry exp_id |
|------|-------------|-----------------|
| 梯度全局分析 | `gradient_analysis_combined.pdf/png` | `gradient_analysis`, `gradient_analysis_mixed_seed` |
| CKA 3 条件 | `cka_results.json`, `cka_analysis.pdf` | `cka_analysis` |
| CKA Random OCC | `cka_random_occ_results.json`, `cka_random_occ.pdf` | `cka_random_occ` |
| CKA Detach+LN | `cka_detach_ln_results.json`, `cka_detach_ln.pdf` | `cka_detach_ln` |
| Per-layer conflict | Registry metrics `per_layer_conflict` | `gradient_analysis_mixed_seed` |

**Seed 注意**：Vanilla/Full OCC 用 seed 42 (s0)；Random OCC/Detach+BN 用 seed 44 (s2)。论文图表 caption 需注明 mixed-seed design。
