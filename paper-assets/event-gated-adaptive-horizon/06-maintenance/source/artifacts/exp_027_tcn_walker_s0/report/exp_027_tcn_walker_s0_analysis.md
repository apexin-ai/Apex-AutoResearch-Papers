# exp_027_tcn_walker_s0 Analysis

## 实验概要

| 项目 | 值 |
|------|-----|
| 方法 | TCN (Temporal Conditioning Noise): imagination rollout 时对 dt_embedding 加高斯噪声 σ=0.5×std |
| 环境 | Walker Walk |
| Seed | 0 |
| Gate config | gate_fixed_dt=2, subsample=2, h=8 |
| 目标步数 | 210K (105K 初始完成后从 112K checkpoint 续跑至 210K) |
| 退出状态 | EXIT_CODE=0，正常完成 |

## 训练完成状态

训练正常完成。最后一次 eval 在 step 105K，之后继续收集了 data collection episodes 到 112K env steps 后正常退出。不存在提前退出问题——105K 就是配置的目标步数。

## 指标轨迹

### eval_return

| Step | eval_return | 备注 |
|------|-------------|------|
| 5K   | 37.4        | 初始 |
| 15K  | 154.6       | 快速上升 |
| 25K  | 223.6       | |
| 35K  | **239.9**   | **全程峰值** |
| 45K  | 101.2       | 第一次崩塌 |
| 55K  | 70.0        | 谷底 |
| 65K  | 95.1        | |
| 75K  | 189.2       | 恢复 |
| 85K  | **35.9**    | **全程最低** |
| 95K  | 166.4       | 恢复 |
| 105K | 95.5        | **最终值** |

均值：~119。峰值 239.9 (35K)。最终 95.5。

### NVE (civo/ve_ratio)

| Step | ve_ratio | delta_ve | alert | 备注 |
|------|----------|----------|-------|------|
| 15K  | 0.0      | 0.0      | 0     | |
| 25K  | 0.1      | 0.1      | 0     | |
| 35K  | 0.2      | 0.1      | 0     | 健康阶段 |
| 45K  | 0.9      | 0.6      | 0     | 开始上升 |
| 55K  | **1.7**  | 0.8      | **1** | **CIVO Episode 1: 突破 1.5× 阈值** |
| 65K  | 1.5      | -0.1     | 0     | 边界值 |
| 75K  | 0.8      | -0.7     | 0     | 自修正 |
| 85K  | **4.0**  | 3.1      | 0     | **CIVO Episode 2: 爆发性飙升** |
| 95K  | 0.7      | -3.3     | 0     | 自修正 |
| 105K | 0.9      | 0.2      | 0     | 最终值 |

## 关键发现

### 1. NVE 双峰 CIVO 模式

训练过程中出现两次明显的 CIVO episodes：
- **Episode 1 (45K-75K)**：NVE 渐进上升到 1.7，伴随 eval 从 240→70 崩塌，随后自修正到 0.8，eval 恢复到 189。
- **Episode 2 (75K-95K)**：NVE 爆发性飙升到 **4.0**（远超 1.5× 阈值，是阈值的 2.67 倍），伴随 eval 崩塌到 35.9（全程最低），随后快速自修正到 0.7，eval 恢复到 166。

### 2. TCN 自修正效应

TCN 噪声确实产生了一种"自修正"机制——NVE 在飙升后能自发回落。但这种修正是**被动的、滞后的**：
- 修正发生在 CIVO 已经造成严重 eval 崩塌之后
- 4.0 的 NVE 峰值说明 σ=0.5×std 的噪声强度不足以**预防** CIVO，只能**延迟恢复**

### 3. Value 过估计验证

85K 时刻（NVE=4.0）：value_mean=142.5 vs eval_return=35.9 → critic 高估 4 倍，确认 CIVO 发生。
105K 时刻（NVE=0.9）：value_mean=87.5 vs eval_return=95.5 → 基本对齐，自修正有效。

### 4. eval 轨迹振荡而非收敛

eval_return 呈现剧烈振荡（240→70→189→36→166→96），没有任何收敛趋势。这种不稳定性本身就是 TCN 方法的问题——即使最终 NVE 被控制住，学习过程已被严重干扰。

## 与 Baseline 对比

| 指标 | TCN (exp_027_s0) | Walker Baseline (无干预) |
|------|-----------------|------------------------|
| 最终 eval_return | 95.5 | ~900 |
| 峰值 eval_return | 239.9 | ~900 |
| 最终 NVE | 0.9 | N/A |
| 峰值 NVE | 4.0 | N/A |

最终 eval 仅为 baseline 的 **10.6%**。峰值 eval 也仅为 baseline 的 **26.7%**。

## 结论：NEGATIVE (基于 105K 数据，实验续跑至 210K 中)

**TCN σ=0.5×std 未能达成任何一个 hypothesis 目标：**

1. ❌ **NVE < 1.5×**：NVE 两次突破 1.5×，峰值达 4.0。虽然最终回落到 0.9，但无法阻止 CIVO episodes 发生。
2. ❌ **eval > 450+**：全程最高仅 239.9，最终 95.5。远低于 50% baseline 的目标。

**根本问题**：σ=0.5×std 的噪声不足以阻止 critic 在 imagination rollout 中学到 dt-specific value bias。TCN 只提供了"事后修复"而非"事前预防"，且修复过程中 eval 已崩塌。更严重的是，整个学习过程因 CIVO 反复发作而无法稳定，导致最终性能远低于 baseline。

## 对后续实验的启示

### exp_027_sigma02 (σ=0.2×std)
仍在评估中。σ=0.2 与 σ=0.5 的动力学可能不同——更低噪声可能避免振荡而仍抑制 CIVO，也可能不足。需等 210K 完整数据，不做预判。

### exp_027_s1 (seed=1, σ=0.5×std)
用于检验双峰 CIVO + 自修正模式是否 seed-invariant。如果 s1 也出现类似的 NVE 飙升→自修正模式，则确认这是 TCN 的 systematic behavior 而非随机波动。

### 方向性判断
**TCN σ=0.5 fails — noise creates oscillatory dynamics.** σ=0.5 级别的噪声不能预防 CIVO，只产生 NVE 飙升→自修正的振荡模式，eval 在振荡中无法稳定学习。Lower σ configurations (σ=0.2) remain under evaluation — 不同噪声量级可能产生不同动力学，不做推广性结论。
