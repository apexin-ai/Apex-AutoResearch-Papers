# plan_033: dt_embedding Cosine Similarity Evolution Analysis

## Summary

Trained dt_embedding 的 dt=1 和 dt=2 向量在训练过程中始终保持强反相关，但随训练逐步放松（cosine 从 -0.95 升至 -0.65）。Frozen embedding 保持恒定近零 cosine。cosine 放松 **领先于** CIVO alert ~30-35k steps，说明 embedding 分化是早期训练动态，而非 CIVO 触发的结果。

---

## 1. 数据覆盖

| 实验 | 类型 | 环境 | Checkpoint 数 | Step 范围 | 分辨率 |
|------|------|------|-------------|-----------|--------|
| exp_066b | trained | walker | 12 | 10k–65k | 5k |
| exp_008d_s3 | trained | walker | 3 | 25k–latest(75k) | — |
| exp_008d_s4 | trained | walker | 3 | 25k–latest(75k) | — |
| exp_059_s5 | trained | walker | 3 | 25k–latest(75k) | — |
| exp_045 ext | trained | walker | 5 | 152k–302k | 50k |
| exp_010b_s0 | trained | cheetah | 3 | 25k–latest(75k) | — |
| exp_048 ext | trained | cheetah | 5 | 152k–302k | 50k |
| exp_057_s2 | frozen | walker | 6 | 25k–225k | 50k |
| exp_058_s1 | frozen | cheetah | 6 | 25k–225k | 50k |

总计 **11 个实验，~47 个 checkpoint** 的 dt_embedding 提取。

## 2. 核心发现

### 2.1 Trained dt_embedding: 渐进放松但永不到零

所有 trained 实验展现一致的动态模式：

**Walker (stitched timeline: 066b → 008d → 045):**
- 10k steps: cos = **-0.947** (near-opposite)
- 25k steps: cos ≈ **-0.93** (rate fastest here)
- 65k steps: cos = **-0.847**
- 75k steps: cos ≈ **-0.70** (跨 seed 范围: -0.70 ~ -0.86)
- 302k steps: cos = **-0.668** (extension run, 几乎停滞)

**Cheetah (stitched timeline: 010b → 048):**
- 25k steps: cos = **-0.904**
- 75k steps: cos = **-0.841**
- 302k steps: cos = **-0.639**

关键特征：
- 初始 cos ≈ -0.95（随机初始化后仅 10k step 就已高度反相关）
- **单调放松**：cos 在 0→100k 快速上升，100k+ 后趋于平缓
- **永不到零**：即使训练 300k step，cos 仍在 -0.63 ~ -0.67
- exp_045 (150k-300k) 甚至出现轻微 **re-divergence** (-0.638 → -0.668)

### 2.2 Frozen dt_embedding: 恒定近零

| 实验 | cos(dt1,dt2) | 变化量 |
|------|-------------|--------|
| exp_057 frozen walker | -0.150 | 0.000 (225k steps) |
| exp_015b frozen walker | +0.170 | — (only latest) |
| exp_058 frozen cheetah | +0.069 | 0.000 (225k steps) |

Frozen embedding 的 cos 完全恒定（符合预期），且绝对值 <0.2（near-orthogonal，随机初始化状态）。

### 2.3 exp_065 结论验证

exp_065 原始报告：trained cosine [-0.94, -0.70]，frozen cosine [-0.15, +0.07]。

**本次扩展验证**：
- Trained range 扩展为 **[-0.947, -0.639]**（加入了更早和更晚的 checkpoint）
- Frozen range 确认为 **[-0.150, +0.170]**（增加 exp_015b）
- 结论完全一致，且增加了时间动态维度

## 3. 变化率分析 (exp_066b, 5k resolution)

| Step 区间 | Δcos/10k steps | 阶段 |
|-----------|---------------|------|
| 10k→15k | -0.002 | 初始稳定 |
| 15k→25k | +0.020 | 快速放松开始 |
| 25k→45k | **+0.024** | 峰值放松速率 |
| 45k→55k | +0.019 | 开始减速 |
| 55k→65k | +0.010 | 明显减速 |

放松速率在 **25k-45k** 达到峰值，之后逐渐衰减。这与 embedding 空间的几何直觉一致：最初的大角度调整代价低，接近 -0.5 后调整变慢。

## 4. 与 CIVO Onset 的时序对比

exp_066b 中可同时观测 cosine sim 和 CIVO 指标：

| Step | cos(dt1,dt2) | VE ratio | CIVO alert |
|------|-------------|----------|------------|
| 10k | -0.947 | 0.012 | — |
| 15k | -0.948 | 0.033 | — |
| 25k | -0.928 | 0.193 | — |
| 35k | -0.904 | 0.269 | — |
| 45k | -0.880 | 0.358 | — |
| 55k | -0.861 | 0.710 | **ALERT** |
| 65k | -0.847 | 0.724 | — |

**关键洞察**：
1. Cosine 放松从 **~20k step** 开始（15k时cos=-0.948仍在下降，25k时cos=-0.928开始上升）
2. CIVO alert 在 **55k step** 才触发（VE ratio > 0.7）
3. Cosine 放松 **领先 CIVO alert ~30-35k steps**
4. VE ratio 和 cosine 放松同向增长，但 VE ratio 是滞后指标

**解读**：dt_embedding 的反方向分化是训练早期的自发行为，不是 CIVO 机制触发的结果。相反，embedding 分化可能是 CIVO collapse 的**先导信号** — dt=1 和 dt=2 learning to represent fundamentally different planning horizons，这种分化加剧了后续的 value estimation divergence。

## 5. Embedding Norm 演化

| 实验 | |dt1| 变化 | |dt2| 变化 | 特征 |
|------|----------|----------|------|
| exp_066b walker | 0.23 → 0.50 (2.2x) | 0.45 → 0.63 (1.4x) | dt1 追赶 dt2 |
| exp_008d walker | 0.38 → 0.52 (1.4x) | 0.55 → 0.64 (1.2x) | 同上 |
| exp_045 walker ext | 0.64 → 0.76 (1.2x) | 0.68 → 0.75 (1.1x) | 趋于收敛 |
| exp_010b cheetah | 0.29 → 0.30 (1.0x) | 0.50 → 0.51 (1.0x) | **几乎不变** |
| exp_048 cheetah ext | 0.30 → 0.30 (1.0x) | 0.51 → 0.53 (1.0x) | 同上 |
| exp_057 frozen walker | 0.072 (const) | 0.052 (const) | 量级极小 |

**Walker vs Cheetah 差异**：
- Walker: norm 显著增长，dt1 从小 norm 追赶 dt2 → 表示 "both dt values become more expressive"
- Cheetah: norm 几乎恒定，但 cosine 仍在放松 → "direction changes without magnitude change"
- 这可能反映两个环境对 dt_embedding 的不同需求

## 6. Cross-seed 一致性

Walker trained 实验跨 seed 的 cosine @ 25k step：
- exp_008d_s1: -0.917
- exp_008d_s3: -0.868
- exp_008d_s4: -0.896
- exp_059_s5: -0.941
- exp_066b: -0.928

**Mean ± std = -0.910 ± 0.028**，高度一致。

Walker trained @ 75k step：
- exp_008d_s3: -0.699
- exp_008d_s4: -0.747
- exp_059_s5: -0.863
- exp_066b: -0.847

**Mean ± std = -0.789 ± 0.076**，seed 间差异增大（放松速率因 seed 而异）。

## 7. 对 CIVO 理论的含义

1. **dt_embedding 分化是自发的**：training pressure 自然驱使 dt=1 和 dt=2 向相反方向分化，因为它们需要编码不同的时间尺度信息
2. **分化程度与 collapse 相关**：VE ratio 和 cosine 放松正相关，暗示 dt_embedding 分化是 value estimation divergence 的结构性前提
3. **Frozen embedding 通过消除分化 channel 来避免 collapse**：frozen cos ≈ 0 意味着 dt 信息不被 differentially encoded，RSSM 无法通过 dt 区分 time scales
4. **-0.65 可能是 "equilibrium" cosine**：在 300k step 后趋于稳定，甚至轻微 re-diverge，暗示网络找到了一个平衡点

## 8. 文件索引

| 文件 | 位置 |
|------|------|
| 综合图 | `logdir/exp_065_dt_emb_cosine/cosine_evolution_comprehensive.png` |
| 066b 详细图 | `logdir/exp_065_dt_emb_cosine/cosine_vs_dynamics_066b.png` |
| 扩展分析 JSON | `logdir/exp_065_dt_emb_cosine/extended_analysis.json` |
| 原始 exp_065 结果 | `logdir/exp_065_dt_emb_cosine/results.json` |
