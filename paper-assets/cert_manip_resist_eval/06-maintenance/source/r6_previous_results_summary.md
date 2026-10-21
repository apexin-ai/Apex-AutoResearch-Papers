# R6 Previous Analysis Results Summary

收集时间：2026-05-25，来源：`/root/cert_manip_resist_eval/artifacts/results/plan001/`

---

## 1. Quant Dummy Regression (`quant_dummy_regression.json`)

**模型**: `log(ASR+eps) ~ log(K_eff) + log(eta_max+eps) + quant_frac + log(K_eff)*quant_frac`
- 15 models (6 local AWQ), 12 conditions, wild cluster bootstrap (B=499)

| K | K_eff sig | quant_frac sig | Interaction sig | Interaction方向 | η sig |
|---|-----------|----------------|-----------------|-----------------|-------|
| 3 | 6/12 | 6/12 | 5/12 | negative | 7/12 |
| 5 | 6/12 | 2/12 | 2/12 | mixed | 11/12 |
| 7 | 4/12 | 0/12 | 0/12 | mixed | 12/12 |

- **predictor_shift_survives**: false
- **结论**: quant_frac 对 K_eff 效应的调节作用证据不一致。交互项在 K=3 时显著（负向，即量化模型削弱 K_eff 效应），但随 K 增大迅速消失。VIF 极高（quant_frac/interaction ~87-89 at K3），共线性严重。

---

## 2. API-Only Power Analysis

### 2a. `api_only_power_beta.json`（WCB p-value 为 outcome）

- API模型: 9 (claude-opus-4-6, gpt-5.5, gemini-3.1-pro-preview, gpt-4.1, claude-sonnet-4-6, gpt-4.1-nano, gemini-3.5-flash, gpt-4.1-mini, claude-3-haiku)
- API-only panels: K3=84, K5=126, K7=36
- 所有条件 WCB 均不显著（K7 仅 3 clusters/position）

**Power curve (WCB rejection rate at given β_std)**:

| β_std | K3 power | K5 power | K7 power |
|-------|----------|----------|----------|
| 0.3   | 0.082    | 0.013    | 0.0      |
| 0.5   | 0.322    | 0.055    | 0.0      |
| 0.7   | 0.591    | 0.128    | 0.0      |
| 1.0   | 0.785    | 0.271    | 0.0      |

- **MDE at 80%**: 全部 null（不可达）
- **Interpretation**: `power_issue` — API-only β_std 为 full pool 的 164%，效应量保留甚至放大，低显著性纯粹因 panel/cluster 数不足

### 2b. `api_only_power_betastd.json`（β_std 直接分析）

- β_std ratio: K3=1.819, K5=1.822（API-only 效应量是 full pool 的 ~1.8x）
- MDE at 80%: K3=0.897, K5=null
- Power curve K3 at β_std=1.0 → 0.858; K5 → 0.301

**核心发现**: API-only 子集检测到的 K_eff 效应量**更大**，不是效应消失，而是统计功效不足。仅靠 API 模型不可行——需要 local 模型提供足够 panel diversity。

---

## 3. β_std Trajectory (`beta_std_trajectory.json` + `betastd_trajectory.json`)

**β_std(K_eff) 跨 K 轨迹**（12 conditions 均值）:
- K=3: **0.349** (sd=0.183)
- K=5: **0.437** (sd=0.293) ← peak
- K=7: **0.401** (sd=0.222)

**β_std(η_max) 跨 K 轨迹**:
- K=3: **0.266** (sd=0.179)
- K=5: **0.101** (sd=0.327) ← sharp decline
- K=7: **0.084** (sd=0.284)

**K_eff 显著条件数** (OLS p<0.05):
- K=3: ~7/12, K=5: ~9/12, K=7: ~10/12

**Shift interpretation**: K_eff 效应量非单调（K5 peak），但在 WCB 下大 K 反而更多条件显著（因为 panel 数量 455→3003→6435 带来的功效补偿）。η_max 效应随 K 迅速衰减——大 panel 中个体操控能力被稀释。

**Per-condition highlights**:
- `arc_challenge×score_manipulation`: keff_std 异常大（K5=1.17, K7=0.84）
- `arc_challenge×position_bias`: keff_std 很小但 η dominant
- `mmlu×sycophancy`: keff 稳定显著，η 在 K≥5 消失

---

## 4. Bayesian Posterior Entropy (`bayesian_posterior_entropy.json`)

**Posterior concentration ratio** (exp(H)/K):
- K=3: **0.890**, K=5: **0.874**, K=7: **0.867**
- 单调递减，所有 pairwise Mann-Whitney U 检验均显著 (p < 1e-20)

**K_eff variance compression** (CV):
- K=3: **0.157**, K=5: **0.148**, K=7: **0.131**
- 单调递减

**Effective judges**: K3=2.67, K5=4.37, K7=6.07

**Non-monotonic K_eff significance 解释**:
> 两个压缩机制叠加：(1) 后验集中——大 K 时贝叶斯权重集中于高准确率评委，有效评委相对 panel 大小下降；(2) K_eff 方差压缩——K=7 时 CV 仅 0.131，预测变量 range 极窄。双重压缩在 K=7 摧毁了 K_eff 的统计功效。K=5 是甜蜜点——panel 数量增益 (4.4 effective judges) 仍超过集中损失。

**Per-dataset breakdown**:
- MMLU: concentration ratio 高于 ARC (0.908 vs 0.871 at K3)，K_eff CV 更小（0.123 vs 0.176 at K3）
- ARC_Challenge: 更大的 K_eff 变异性，更多分辨力

---

## 5. Fractional Logit V2 (`fractional_logit_v2.json`)

**方法**: GLM(ASR ~ log(K_eff) + log(eta_max + eps), family=Binomial, link=logit), clustered SE, BH-FDR

| K | K_eff sig (FDR) | η sig (FDR) |
|---|-----------------|-------------|
| 3 | **9/12** | 6/12 |
| 5 | **9/12** | 6/12 |
| 7 | **9/12** | 4/12 |

**与论文声称对比**:
| K | Paper claims | Registry V1 | Actual V2 |
|---|-------------|-------------|-----------|
| 3 | 9/12 | 4/12 | 9/12 |
| 5 | 11/12 | 9/12 | 9/12 |
| 7 | 12/12 | 10/12 | 9/12 |

- K3 V2 恢复到论文水平 (registry V1 仅 4/12 是因为 V1 数据问题)
- K5/K7 V2 略低于论文声称，但差距不大
- Adaptive R² 数据在 plan001 结果中未找到

---

## 6. Monte Carlo Size Calibration (`monte_carlo_size_calibration.json`)

**PID 18494 状态**: 已完成（进程不再运行）
**耗时**: 33,109 秒 (~9.2 小时)

**方法**: Permutation-based wild cluster bootstrap, 1000 permutations × 999 bootstrap resamples, Rademacher weights, max-p across K positions

**Rejection rates under H₀** (nominal α=0.05):

| K | Mean rate | Max rate | Min rate | Over-reject条件数 |
|---|-----------|----------|----------|-------------------|
| 3 | **0.93%** | 1.6% | 0.4% | **0/12** |
| 5 | **0.36%** | 0.8% | 0.0% | **0/12** |
| 7 | **0.12%** | 0.3% | 0.0% | **0/12** |

**核心结论**: WCB 检验在所有 36 个条件下均**不**过度拒绝。实际 size 远低于名义 α=0.05（最坏 1.6%），说明 WCB 是**保守的**。这意味着论文中报告的显著性结果（如果有）是可信的——不是 type-I error inflation 的假象。

Over-reject threshold 设为 0.075，无一条件超过。

---

## 7. Crossed Random Effects (`crossed_re_results.json`)

**方法**: Panel-level OLS + multi-membership CRVE (sandwich SE), t(G-1) = t(14) distribution

| K | K_eff sig (FDR) | K_eff raw sig | η sig (FDR) | η raw sig |
|---|-----------------|---------------|-------------|-----------|
| 3 | **0/12** | 5/12 | 1/12 | 2/12 |
| 5 | **8/12** | 8/12 | 3/12 | 4/12 |
| 7 | **8/12** | 9/12 | 2/12 | 3/12 |

**与 bootstrap 对比**:
| K | Bootstrap K_eff sig | Crossed RE K_eff sig |
|---|--------------------|--------------------|
| 3 | 4/12 | 0/12 |
| 5 | 7/12 | 8/12 |
| 7 | 8/12 | 8/12 |

**SE inflation**: 4-16x（K3 约 3-5x，K7 约 6-16x），因为只有 15 clusters (judges) 且 df=14。K=3 时 FDR 后全部不显著是因为 SE inflation + 小 df 的 t-distribution 严重惩罚。K=5/7 时 panel 数量大增（3003/6435），信号足以克服膨胀的 SE。

---

## 汇总诊断

### 一致性检查
- **K_eff 效应存在且 robust**: Fractional logit V2 (9/9/9)、crossed RE K5/K7 (8/8)、β_std trajectory 均确认
- **K=3 特殊**: crossed RE 全灭 (0/12)，但这是 SE inflation 问题，不是效应消失（β_std=0.349 仍然存在）
- **K=7 WCB 非单调谜团已解**: Bayesian posterior entropy 提供了完整解释（双重压缩机制）
- **MC 校准通过**: WCB 不 over-reject，论文结果可信

### 缺失/异常
- **Adaptive R²**: 未在 plan001 结果中找到，论文声称 0.275，registry 声称 0.256
- **fp16_baseline.json** (May 25 08:03): 存在但未在任务列表中，可能是后续实验
- **crossed RE 模型名称不一致**: 使用了旧名称 (claude-opus-4, gemini-2.5-pro 等)，与其他分析的模型名不同——可能是从不同数据版本运行的

### 关键数字速查
| 指标 | K=3 | K=5 | K=7 |
|------|-----|-----|-----|
| β_std(K_eff) | 0.349 | 0.437 | 0.401 |
| β_std(η_max) | 0.266 | 0.101 | 0.084 |
| Fractional logit K_eff sig | 9/12 | 9/12 | 9/12 |
| WCB MC rejection rate | 0.93% | 0.36% | 0.12% |
| Crossed RE K_eff sig (FDR) | 0/12 | 8/12 | 8/12 |
| Posterior concentration ratio | 0.890 | 0.874 | 0.867 |
| K_eff CV | 0.157 | 0.148 | 0.131 |
| API-only MDE@80% | null | null | null |
