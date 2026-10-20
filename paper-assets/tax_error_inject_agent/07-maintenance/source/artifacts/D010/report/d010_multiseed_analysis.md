# D010 Multi-Seed Validation & Recovery Eval 综合分析报告

**日期**: 2025-05-14
**实验**: D010 Phase 1 (Clean eval 多种子) + Phase 2 (Recovery eval)
**评估集**: 47 tasks (ALFWorld)

---

## 1. 数据总览

| 方法 | 训练数据量 | seed=42 | seed=0 | seed=123 | 均值 | SD | Range |
|------|-----------|---------|--------|----------|------|-----|-------|
| Vanilla SFT | 4,358 | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3%** | 3.3 pp | 6.4 pp |
| TaxEI SFT | 9,029 | 61.7% (29/47) | 46.8% (22/47) | — | **54.3%** | 10.5 pp | 14.9 pp |
| Random SFT | 9,029 | 66.0% (31/47) | 55.3% (26/47) | — | **60.7%** | 7.6 pp | 10.7 pp |
| Zero-shot | — | 42.6% (20/47) | — | — | **42.6%** | — | — |

**注**: TaxEI/Random 仅有 2 个 seed，SD 基于 n-1=1 自由度，估计极不稳定。

---

## 2. 多种子稳定性分析

### 2.1 跨 seed 波动

| 方法 | SD (pp) | Range (pp) | CV (%) | 种子数 |
|------|---------|------------|--------|--------|
| Vanilla | 3.3 | 6.4 | 5.0% | 3 |
| Random | 7.6 | 10.7 | 12.5% | 2 |
| TaxEI | 10.5 | 14.9 | 19.4% | 2 |

**观察**:
- Vanilla 跨 seed 最稳定（SD=3.3 pp），三个 seed 均落在 61.7%–68.1% 的窄带内。
- 注入训练方法（TaxEI/Random）的波动显著更大：TaxEI 的 range 达 14.9 pp，是 Vanilla 的 2.3 倍。
- **但**: 2-seed SD 本质上就是 |x₁−x₂|/√2，自由度仅 1，不能可靠估计总体方差。Vanilla 有 3 seed 的 SD 也仅基于 df=2。这些 SD 的置信区间本身极宽。

### 2.2 注入训练波动是否系统性更大？

逐 seed 配对比较揭示了一个关键模式：

| Seed | Vanilla | TaxEI | Random | Vanilla−TaxEI | Vanilla−Random |
|------|---------|-------|--------|---------------|----------------|
| 42 | 61.7% | 61.7% | 66.0% | **0.0 pp** | **−4.3 pp** |
| 0 | 68.1% | 46.8% | 55.3% | **+21.3 pp** | **+12.8 pp** |

Seed=42 时三种方法几乎无差异（甚至 Random > Vanilla）；seed=0 时注入方法大幅落后。这意味着 **方法差异与 seed 选择高度交互** — 不是一个稳定的主效应。

**可能解释**:
1. 注入数据放大了训练不稳定性：额外的 ~4,700 条注入样本引入了更多噪声，使模型对随机种子更敏感。
2. Seed=0 碰巧是一个"不利种子"，对注入方法的影响不成比例地大。
3. 样本量太小（n=47 eval tasks），评估本身的噪声掩盖了真实效应。

---

## 3. 方法间对比

### 3.1 均值比较

| 对比 | Δ均值 (pp) | Cohen's h | 效应大小 |
|------|-----------|-----------|---------|
| Vanilla vs Zero-shot | +22.7 | 0.46 | 接近中等 |
| Vanilla vs TaxEI | +11.0 | 0.22 | 小 |
| Vanilla vs Random | +4.6 | 0.09 | 可忽略 |
| Random vs TaxEI | +6.4 | 0.13 | 可忽略 |
| TaxEI vs Zero-shot | +11.7 | 0.23 | 小 |
| Random vs Zero-shot | +18.1 | 0.37 | 小-中等 |

### 3.2 个体运行的 95% 二项式置信区间 (Wilson)

| 运行 | 点估计 | 95% CI |
|------|--------|--------|
| Vanilla seed=42 | 61.7% | [46.4%, 75.5%] |
| Vanilla seed=0 | 68.1% | [52.9%, 80.5%] |
| Vanilla seed=123 | 66.0% | [50.7%, 78.8%] |
| TaxEI seed=42 | 61.7% | [46.4%, 75.5%] |
| TaxEI seed=0 | 46.8% | [32.1%, 61.9%] |
| Random seed=42 | 66.0% | [50.7%, 78.8%] |
| Random seed=0 | 55.3% | [40.1%, 69.8%] |
| Zero-shot | 42.6% | [28.3%, 57.8%] |

**关键**: 每个 CI 宽度约 ±14 pp。大部分 CI 相互重叠。即使是 Vanilla 最好的 seed=0 (68.1%) 与 TaxEI 最差的 seed=0 (46.8%)，其 CI 仍有边缘重叠。

### 3.3 均值的简易置信区间

由于种子数极少（2-3），无法做 bootstrap。用 t 分布构造 CI：

| 方法 | 均值 | SE | 95% CI (t-based) | df |
|------|------|-----|------------------|----|
| Vanilla | 65.3% | 1.9 pp | [57.1%, 73.4%] | 2 |
| TaxEI | 54.3% | 7.5 pp | [−41.0%, 149.5%]* | 1 |
| Random | 60.7% | 5.4 pp | [−7.8%, 129.1%]* | 1 |

*df=1 时 t₀.₀₂₅=12.71，CI 完全没有意义。这证实 2-seed 设计对均值估计的统计功效为零。

---

## 4. D012 结论验证

### D012 原始结论
> "注入训练系统性损害 clean performance"

### 新证据评估

**支持 D012 的证据**:
- TaxEI seed=0 (46.8%) 大幅低于 Vanilla seed=0 (68.1%)，差距 21.3 pp
- Random seed=0 (55.3%) 也低于 Vanilla seed=0 (68.1%)，差距 12.8 pp
- 两种注入方法在 seed=0 下均出现性能下降

**反对 D012 的证据**:
- TaxEI seed=42 (61.7%) = Vanilla seed=42 (61.7%)，差距 0.0 pp
- Random seed=42 (66.0%) > Vanilla seed=42 (61.7%)，Random 反而更好 4.3 pp
- Seed=42 下注入训练完全无害，甚至有益

### 修正结论

**D012 的"系统性损害"结论 premature（过早）**。更准确的描述是：

> 注入训练增加了训练不稳定性，在某些 seed 下严重损害 clean performance（TaxEI seed=0 下降 21.3 pp），但在其他 seed 下无影响或轻微有益。"系统性损害"需要更多 seed 才能确认。

### TaxEI seed=0 的 46.8% 是异常值还是趋势？

**无法判定**。只有 2 个数据点：
- 如果它是异常值 → TaxEI 真实均值接近 61.7%，与 Vanilla 无差异
- 如果它是趋势 → TaxEI 真实均值约 54%，注入确实有害
- 需要至少 3-5 个额外 seed 才能区分这两种情况

类似地，Random seed=0 的 55.3% 同样面临相同的不确定性。

---

## 5. Recovery Eval 初步解读

### 5.1 Vanilla Recovery 结果

| 指标 | 值 | 含义 |
|------|-----|------|
| recovery_rate | 0.617 (29/47) | 61.7% 的错误注入 episode 中，模型成功纠正了注入的错误并完成任务 |
| detection_rate | 0.0 (0/47) | 模型从未显式检测到/标记出注入的错误 |

**解读**:
- **Recovery without detection**: 模型通过通用问题解决能力（重试、换策略）恢复，而非通过识别错误类型。这是一种"盲恢复"——模型遇到失败后尝试替代路径，碰巧绕过了注入的错误。
- recovery_rate=0.617 与 clean eval 的 seed=42 结果 (61.7%) 完全一致。这暗示 Vanilla 模型的 recovery 可能只是"重新做一遍"的 baseline 能力，而非真正的错误修复能力。

### 5.2 对 TaxEI Recovery Eval 的预期

TaxEI recovery eval 仍在运行 (17/47)。可能的结果及其含义：

| TaxEI Recovery 结果 | TaxEI Detection 结果 | 解读 |
|---------------------|---------------------|------|
| recovery > 0.617 | detection > 0 | **正面**: taxonomy 训练同时提升了检测和恢复能力 |
| recovery > 0.617 | detection = 0 | **部分正面**: taxonomy 提升了隐式恢复但未学会显式检测 |
| recovery ≈ 0.617 | any | **中性**: taxonomy 训练对 recovery 无影响 |
| recovery < 0.617 | any | **负面**: taxonomy 训练不仅损害 clean performance，还损害 recovery |

**关键阈值**: TaxEI recovery_rate 需要 > 0.617 才能声称 taxonomy 在错误恢复上有价值。考虑到 TaxEI 的 clean eval 均值已低于 Vanilla（54.3% vs 65.3%），如果 recovery 也不优于 Vanilla，则 TaxEI 方案全面 negative。

### 5.3 detection_rate=0 的深层含义

所有方法 detection=0 意味着：
1. 当前的 eval protocol 可能对"检测"的定义过于严格（需要显式输出特定标记？）
2. 或者 SFT 训练根本不足以教会模型"元认知"——识别自己（或环境）的错误类型
3. 如果 TaxEI 也是 detection=0，则 taxonomy-aware 训练在元认知层面完全失败

---

## 6. 统计功效讨论

### 6.1 McNemar Test 的检测能力 (n=47)

McNemar test 基于 discordant pairs（两种方法结果不同的 task）。

假设 discordant 比例为 30%（~14 tasks），80% power, α=0.05：
- 需要 |b−c|² / (b+c) ≥ 3.84
- 14 个 discordant pairs 中需要至少 11 vs 3 的分裂
- 对应 accuracy 差异约 **17 pp** (8/47)

假设 discordant 比例为 40%（~19 tasks）：
- 需要至少 14 vs 5 的分裂
- 对应约 **19 pp** 差异

| 假设 discordant 率 | 可检测最小差异 (80% power) |
|-------------------|-------------------------|
| 20% (~9 pairs) | ~15 pp |
| 30% (~14 pairs) | ~17 pp |
| 40% (~19 pairs) | ~19 pp |

### 6.2 当前观察效应 vs 检测阈值

| 对比 | 观察 Δ (均值) | 逐 seed Δ 范围 | 可检测？ |
|------|-------------|---------------|---------|
| Vanilla vs TaxEI | 11.0 pp | 0.0 – 21.3 pp | **边缘**: seed=0 的 21.3 pp 可能可检测，seed=42 的 0 pp 不可能 |
| Vanilla vs Random | 4.6 pp | −4.3 – 12.8 pp | **不可检测**: 远低于阈值 |

### 6.3 多种子波动暗示的问题

跨 seed 波动达 10-15 pp，这与方法间差异的量级相当。这意味着：

1. **当前实验设计 underpowered**: 单个 seed 的结果包含约 ±7-10 pp 的训练随机性噪声（加上 ±7 pp 的评估噪声），总噪声可达 ±12-15 pp。方法间的真实差异需要远大于此才能被可靠检测。
2. **最少需要 5+ seeds**: 要将均值的 SE 降到 3 pp 以下（使 10 pp 差异可检测），需要 SD²/n < 9，即 n > SD²/9 ≈ 110/9 ≈ 12 seeds（对 TaxEI）。即使是 Vanilla 的 SD=3.3，也需要 n≥3 seeds。
3. **评估集太小**: n=47 tasks 本身就带来约 ±7 pp 的二项式噪声。扩大评估集到 100+ tasks 可将此噪声降到 ±5 pp。

---

## 7. 总结与建议

### 7.1 可以确认的结论

1. **所有 SFT 方法 > Zero-shot**: 全部 7 个 SFT 运行均超过 42.6% baseline，最低也有 46.8%。SFT 训练有效。
2. **注入训练增加不稳定性**: TaxEI/Random 的跨 seed 波动（10-15 pp）明显大于 Vanilla（6 pp），尽管 2-seed 估计不够精确。
3. **Vanilla recovery 是"盲恢复"**: detection_rate=0 表明恢复不依赖错误识别。

### 7.2 不能确认的结论

1. **"注入训练系统性损害 clean performance"**: Seed=42 下无损害，seed=0 下严重损害。证据不足以判定"系统性"。
2. **TaxEI vs Random 的优劣**: 均值差 6.4 pp，但每种方法只有 2 个 seed，完全无法区分。
3. **任何方法间的统计显著差异**: n=47 tasks × 2-3 seeds 的设计对 <15 pp 的效应完全 underpowered。

### 7.3 如果要继续本方向

| 改进 | 预期收益 | 成本 |
|------|---------|------|
| 为 TaxEI/Random 各补 3 个 seed (共 5 seeds) | 均值 SE 降到 ~4-5 pp | 6 次训练 + eval |
| 扩大评估集到 134 tasks (ALFWorld 全集) | 二项式 SE 从 7pp 降到 4pp | 评估时间 ×3 |
| 两者同时 | 总 SE < 4 pp，可检测 10 pp 差异 | 高 |

### 7.4 当前证据的最诚实总结

> 在 n=47, 2-3 seeds 的实验规模下，我们观察到注入训练 **可能** 损害 clean performance（均值下降 5-11 pp）并增加训练不稳定性，但效应大小与实验噪声（跨 seed 波动 10-15 pp）在同一量级，无法排除零效应的可能。Recovery eval 显示 Vanilla 模型已具备 61.7% 的盲恢复能力，TaxEI 的 recovery eval 结果将决定 taxonomy 方案是否有任何正面价值。
