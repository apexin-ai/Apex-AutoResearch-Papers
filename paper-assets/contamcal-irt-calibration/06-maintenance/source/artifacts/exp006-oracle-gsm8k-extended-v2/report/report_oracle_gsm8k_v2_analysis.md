# exp006-oracle-gsm8k-extended-v2 深入分析

## 1. 实验概要

| 参数 | 值 |
|------|-----|
| Benchmark | GSM8K (1319 items) |
| Models | 16 (0.5B × 9 + 1.5B × 7) |
| Exposure | Oracle dosage (d000=0, d005=0.05, d025=0.25, d100=1.0) |
| MCMC | 4 chains × 2000 warmup × 4000 samples |
| Stan model | contam_irt_4pl_simple.stan |
| Diagnostics | max_rhat=1.002, min_ess=1222, divergent=0 — **全部通过** |

## 2. Coverage Breakdown (Per-Model)

### 2.1 完整 Per-Model 对比表

| # | Scale | Dose | Raw Acc | IRT Calibrated | Ground Truth | 95% CI | Covered? | Error |
|---|-------|------|---------|---------------|--------------|--------|----------|-------|
| 0 | 0.5B | d000 | 0.340 | 0.355 | 0.340 | [0.337, 0.373] | ✓ | +0.015 |
| 1 | 0.5B | d000 | 0.365 | 0.371 | 0.365 | [0.353, 0.389] | ✓ | +0.006 |
| 2 | 0.5B | d000 | 0.369 | 0.373 | 0.369 | [0.355, 0.390] | ✓ | +0.004 |
| 3 | 0.5B | d005 | 0.360 | 0.360 | 0.358 | [0.342, 0.378] | ✓ | +0.002 |
| 4 | 0.5B | d005 | 0.362 | 0.361 | 0.358 | [0.343, 0.379] | ✓ | +0.003 |
| 5 | 0.5B | d025 | 0.366 | 0.310 | 0.358 | [0.289, 0.335] | ✗ | −0.048 |
| 6 | 0.5B | d100 | 0.380 | 0.214 | 0.358 | [0.199, 0.239] | ✗ | −0.144 |
| 7 | 0.5B | d100 | 0.357 | 0.211 | 0.358 | [0.197, 0.232] | ✗ | −0.147 |
| 8 | 0.5B | d100 | 0.365 | 0.212 | 0.358 | [0.198, 0.234] | ✗ | −0.146 |
| 9 | 1.5B | d000 | 0.633 | 0.588 | 0.633 | [0.569, 0.606] | ✗ | −0.045 |
| 10 | 1.5B | d000 | 0.637 | 0.592 | 0.637 | [0.574, 0.610] | ✗ | −0.045 |
| 11 | 1.5B | d000 | 0.654 | 0.600 | 0.654 | [0.583, 0.618] | ✗ | −0.054 |
| 12 | 1.5B | d005 | 0.648 | 0.578 | 0.641 | [0.558, 0.597] | ✗ | −0.063 |
| 13 | 1.5B | d025 | 0.654 | 0.521 | 0.641 | [0.491, 0.552] | ✗ | −0.120 |
| 14 | 1.5B | d100 | 0.650 | 0.329 | 0.641 | [0.282, 0.392] | ✗ | −0.312 |
| 15 | 1.5B | d100 | 0.650 | 0.329 | 0.641 | [0.282, 0.392] | ✗ | −0.312 |

**Coverage = 5/16 = 0.3125**

### 2.2 Coverage 按分组

| 分组 | Covered / Total | Coverage |
|------|----------------|----------|
| 0.5B d000 | 3/3 | 100% |
| 0.5B d005 | 2/2 | 100% |
| 0.5B d025 | 0/1 | 0% |
| 0.5B d100 | 0/3 | 0% |
| 1.5B d000 | 0/3 | 0% |
| 1.5B d005+ | 0/4 | 0% |

### 2.3 两个独立的失败机制

**失败机制 1: Cross-scale theta 估计偏差（影响所有 1.5B）**
- 1.5B d000 models exposure=0，gamma 项不参与 → calibrated score = IRT 纯能力预测
- 但 IRT 系统性低估 1.5B 约 4-5pp（calibrated ~0.59 vs ground truth ~0.64）
- 原因：1319 个 item 的 (a, b, c, d) 参数需同时拟合 0.5B 和 1.5B 两个能力水平，theta 先验 N(0,1) 将 1.5B theta 拉向 0
- 只有 16 个 model 约束 ~5280 个 item 参数，严重欠定

**失败机制 2: Gamma 过校正（影响所有 d025+ 模型）**
- gamma=3.77 [2.74, 4.71]——非常大的正效应
- 但 GSM8K 实际 dose-response < 2pp（MC benchmark 对 contamination 几乎免疫）
- 0.5B d100 raw acc ≈ 0.358-0.380 vs d000 ≈ 0.340-0.369——差异极小
- IRT 却将 d100 校正到 0.21——比真实 clean accuracy 低 15pp

## 3. PPP 诊断

```
overall_ppp = 0.0
obs_mean_acc = 0.4869
pred_mean_acc = 0.3938
residual_mae = 0.096
```

- PPP=0 表示 16000 次 posterior predictive replications 中，**没有任何一次**生成的数据比观测数据"更极端"
- 模型预测均值准确率 0.394 vs 观测 0.487——差距 9.3pp
- 这是系统性低估，不是随机波动

**根因**: IRT 模型将 contaminated items 的高正确率归因于 gamma*exposure（而非 theta），导致 theta 被系统性压低。当计算 calibrated_score (exposure=0) 时，被压低的 theta 产生过低的预测。

## 4. Gamma 的悖论：信号真实但校正错误

### 4.1 为什么 gamma=3.77 显著正向？

Stan 模型: `eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i,j]`

gamma 显著正向说明：在 **item 层面**，contaminated models 确实在 contaminated items 上有更高的 P(correct)。这是真实的 contamination 信号。

### 4.2 为什么校正后的分数是错的？

GSM8K 的 contamination 效应是**再分配型**而非**加法型**：
- **加法型**（HumanEval）：contamination → 更多 items 答对 → accuracy ↑ → gamma 校正有效
- **再分配型**（GSM8K MC）：contamination → contaminated items 答对率↑，但其他 items 答对率可能↓ → aggregate accuracy ≈ 不变 → gamma 校正过度

当 gamma 从 eta 中移除（计算 calibrated_score），相当于说"如果这些 contaminated items 的答对率和 uncontaminated items 一样"。但模型同时压低了 theta，所以预测的 clean performance 远低于实际。

### 4.3 数学解释

对于 d100 0.5B:
- 真实情况: raw acc ≈ 0.365, clean acc ≈ 0.358, **Δ ≈ 0.007**
- IRT 拟合: gamma=3.77, 对 contaminated items 的 eta 加了 3.77
- 但 theta 被压低以补偿（否则 overall accuracy 会远高于观测值）
- 移除 gamma 后: eta 大幅下降 → calibrated ≈ 0.21, **Δ = −0.147**
- 过校正倍数: **147/7 ≈ 21×**

## 5. Memory 矛盾的解释

### Memory 声称
> "Coverage collapse 根因: N 不够而非 Model Misspecification"
> "exp006-oracle-gsm8k-extended baselines 在 N=16 模型上 C95=1.00, C80=0.94"

### 实际情况

这是**概念混淆**: C95=1.00 来自 **v1 实验的 B0_raw baseline**，不是 IRT 模型。

Registry 证据:
- `exp006-oracle-gsm8k-extended` (v1): IRT fitting **failed** (Operation not permitted)，但 baselines 成功 → B0_raw C95=1.00
- `exp006-oracle-gsm8k-extended-v2`: IRT fitting **succeeded** → IRT C95=0.3125

B0_raw 的 C95=1.00 是因为它根本不做任何校正——raw accuracy 就是 ground truth（GSM8K contamination 不影响 MC accuracy）。这恰恰证明**不需要校正**，而非"N 够了就能校正好"。

### 修正后的结论

| 声称 | 修正 |
|------|------|
| "Coverage collapse 因为 N 不够" | **错误**。N=16 oracle IRT coverage 仍然 31%。问题是 model structure |
| "N↑ 后 coverage 恢复" | **仅对 B0_raw 成立**（因为它不校正）。IRT 无论 N 多大都会过校正 |
| "不需要修改 IRT 模型结构" | **需要修改**。当前模型在 contamination-immune benchmarks 上系统性过校正 |

## 6. Baseline 对比

| 方法 | MAE | C95 | C80 | Kendall τ |
|------|-----|-----|-----|-----------|
| B0_raw | 0.005 | 1.00 | 0.94 | 0.838 |
| B4_linear_regression | 0.008 | — | — | — |
| B5_emperor | 0.005 | 1.00 | 0.94 | 0.838 |
| B6_dcr_fuzzy | 0.138 | 0.56 | 0.56 | 0.415 |
| **IRT_4pl_gamma** | **0.092** | **0.31** | **0.25** | **0.505** |

IRT 是倒数第二，仅好于 DCR fuzzy (B6)。在 GSM8K 上，不做任何校正 (B0_raw) 比 IRT 好 18× MAE 和 3.2× coverage。

## 7. 对论文 Framing 的影响

### 7.1 核心问题

当前 IRT 模型对 GSM8K 这类 contamination-immune MC benchmark 有本质缺陷：
- 能正确检测 item-level contamination signal (gamma >> 0)
- 但将此信号用于 score correction 时严重过校正
- "做了校正比不做更差"对论文是致命的

### 7.2 建议的 Framing 调整

**Option A: 分离检测与校正**
- gamma 作为 contamination **detection** 指标（"是否存在 contamination"）→ 有效
- 校正只在 accuracy-sensitive benchmarks（如 HumanEval）上声称
- GSM8K/MMLU 等 MC benchmarks 的发现是："contamination is detectable at item level but doesn't inflate aggregate MC scores"——这本身是有价值的发现

**Option B: 修改模型结构**
- 当前: 统一 gamma 假设 contamination 对所有 items 均匀提升 P(correct)
- 改进: per-item 或 per-item-group gamma，或增加约束使得 sum(gamma_effect) 与观测到的 aggregate accuracy change 一致
- 更根本的: 增加 benchmark-specific gamma scaling，或 dose-response 约束

**Option C: 限定适用范围**
- 明确声明 IRT 校正方法适用于 contamination 实际影响分数的 benchmark（HumanEval、open-ended generation）
- MC benchmarks 用作 contamination detection（不是 correction）的 validation case

### 7.3 最推荐路径

**Option A**（分离检测与校正），因为：
1. 不需要重新设计模型，利用已有结果
2. "contamination detectable but doesn't inflate MC scores" 是有文献支撑的发现
3. ARC negative gamma + GSM8K over-correction 共同支撑 "discriminative validity" narrative
4. HumanEval 的强 dose-response 作为 correction 的 positive case

## 8. 是否需要修改 IRT 模型结构？

**短期（当前论文）: 不需要**，用 framing 解决。

**中期（revision 或 follow-up）: 建议以下修改**
1. **Benchmark-conditional gamma**: 不同 benchmark 允许不同 gamma，而非全局共享
2. **Constrained calibration**: 增加约束使校正幅度不超过观测到的 raw accuracy change
3. **Separate theta estimation**: 先用 d000 models only 估计 item 参数，再引入 contaminated models 估计 gamma——避免 gamma 窃取 theta

## 9. 关键结论

1. **Coverage 31.25% 的根因是 model misspecification，不是 N 不足**
2. **Memory 中 "C95=1.00" 是 B0_raw baseline 的指标，不是 IRT 的**——概念混淆导致错误结论
3. **Gamma=3.77 是真实的 item-level contamination signal**，但不能直接用于 aggregate score correction
4. **GSM8K 的 contamination 效应是再分配型**：改变哪些 items 答对，不改变多少 items 答对
5. **论文需要区分 contamination detection（IRT 有效）和 score correction（仅在 accuracy-sensitive benchmarks 有效）**
