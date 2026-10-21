# D127: Phase Transition 理论分析

**Date**: 2026-05-20
**Data source**: D120 TY-fixed full rerun + generalize/ + scale_check/ experiments

## 1. Dose-Response Data (Pythia-410M WikiText fp32)

| α | Seeds | PermG values | Mean |
|------|-------|--------------|------|
| 0.00 | s42 | [0] | 0.0 |
| 0.05 | s42 | [0] | 0.0 |
| 0.10 | s42,s43 | [0, 3] | 1.5 |
| 0.25 | s42,s43 | [0, 0] | 0.0 |
| 0.30 | s42 | [0] | 0.0 |
| 0.35 | s42 | [0] | 0.0 |
| 0.40 | s42 | [0] | 0.0 |
| 0.45 | s42 | [0] | 0.0 |
| **0.50** | **s42,s43,s44** | **[6, 6, 6]** | **6.0** |
| 0.60 | — | pending M046 | — |
| 0.75 | s42 | [6] | 6.0 |
| 1.00 | s43 | [6] | 6.0 |

**注**: α=0.60 的两个现有实验被排除：v3_d080（pre-bugfix）和 s43（仅 10 代）。M046 canonical sweep 将提供干净数据。

## 2. Phase Transition Classification

### 跳变特征
- **α≤0.45**: 所有 seed 的 PermG=0（唯一例外 α=0.10 s43=3，可能为噪声）
- **α=0.50**: 3 个 seed **全部** PermG=6，无中间值
- 跳变幅度：mean 0.3 → 6.0（20× increase）

### Sigmoid 拟合
- **α_c = 0.476**, steepness k = 200.0（hit upper bound = 比可拟合的更陡）
- R² = 0.969, AIC = -8.90
- Transition width (10%–90%): **Δα ≈ 0.020**

### Power Law 拟合
- A = 9.79, α_c = 0.450, β = 0.385
- R² = 0.808, AIC = 9.30

### 拟合比较
| Model | R² | AIC | α_c |
|-------|-----|------|------|
| **Sigmoid** | **0.969** | **-8.90** | 0.476 |
| Power law | 0.808 | 9.30 | 0.450 |

**Sigmoid 显著优于 power law**（ΔR²=0.16, ΔAIC=18.2）。

### 结论：Steep Crossover (approaching first-order)

跳变从 0→6 在 Δα<0.05 内完成，sigmoid steepness k 达到上界 (200)，transition width ≈ 0.02。这比 second-order (continuous) phase transition 陡峭得多。

但严格来说，这是一个 **steep crossover** 而非 true first-order transition：
1. 数据分辨率限制：α=0.45 和 α=0.50 之间没有中间点（α=0.47, 0.48 等）
2. k 达到拟合上界，说明数据无法区分 k=200 和 k=∞（true discontinuity）
3. 有限样本（8 pairs）的 PermG 本身是离散的，不可能观测到连续渐变

**对应 Truong & Truong (2025) 的 universality classes**:
- 观测到的 sharp jump 更接近 **convex/irreversible** class
- α=0.60 的 non-monotonic dip（如确认）可能暗示 hysteresis，但当前数据不充分

## 3. α=0.60 Non-Monotonic Dip

现有数据：
- a060_s42_fp32_v3_d080: PermG=3/8（pre-D080 bugfix，dtype 不确定）
- a060_s43_fp32: PermG=0/8（仅 10 代，非标准）

**判断**: 无法从现有数据确认 non-monotonic dip 是真实现象还是实验 artifact。M046 canonical sweep 的 α=0.60 结果将是关键证据。

## 4. Model Scale vs. Causal Signal (α=1.0)

| Model | Params | PermG (seeds) | Mean | Failure mode |
|-------|--------|---------------|------|--------------|
| Pythia-410M | 0.41B | 6 (s43) | 6.0 | — |
| Qwen3.5-0.8B | 0.8B | 8,6 (s42,s43) | 7.0 | — |
| Pythia-1.4B | 1.4B | 2,6 (s42,s43) | 4.0 | entropy saturation (s42) |
| SmolLM3-3B | 3.0B | 3 (s42) | 3.0 | entropy U-shape decoupling |
| Pythia-6.9B | 6.9B | 7 (s42, bf16) | 7.0 | — (bf16 only) |

### 关键发现

**模型规模与 PermG 无单调关系。** 信号强度排序为：
- Qwen-0.8B (7.0) ≈ Pythia-6.9B (7.0) > Pythia-410M (6.0) > Pythia-1.4B (4.0) > SmolLM3-3B (3.0)

信号弱化的根因是 **entropy trajectory shape**，而非 model scale：
1. **SmolLM3-3B**: entropy 呈强 U 型（gen 0→2 骤降至 0.94，gen 10 反弹至 1.70），与 distinct 单调下降方向相反，破坏 Granger 因果。ECE 通道 3/3 保留。
2. **Pythia-1.4B s42**: entropy gen 2 后饱和于 ~1.28（动态范围仅 ±0.08），信号被噪声淹没。s43 的 PermG=6 证明非系统性问题。

**更大模型不一定更 robust 或更 vulnerable。** Critical ratio 是否随 scale shift 无法从当前数据确定——需要对不同模型做完整 alpha sweep。

## 5. Critical Ratio vs. Gu et al. (2025)

Gu et al. 的 framework 预测 critical mixing ratio r_c ~ f(N, D, quality_gap)，但：
- Gu 研究的是 **single-pass** training，我们是 **iterative** (T=11 代)
- 迭代设置下 effective contamination ≈ 1-(1-α)^T：
  - α=0.50, T=11: effective ≈ 99.95%
  - α=0.45, T=11: effective ≈ 99.88%
  - 两者几乎相同，但 PermG 从 0 跳到 6
- 因此我们的 α_c ≈ 0.48 是 **per-generation causation detection threshold**，不是 collapse threshold
- 直接与 Gu 的 single-pass r_c 比较不恰当

**可引用角度**: 我们的发现与 Gu 互补——Gu 刻画的是 collapse 何时发生（数据累积视角），我们刻画的是 collapse 何时可被 **因果检测**（检测灵敏度视角）。

## 6. 图表

已生成并保存至 westd-17855:
- `artifacts_phase_transition/fig_phase_transition.pdf/png`: PermG vs α dose-response with sigmoid + power law fit overlay
- `artifacts_phase_transition/fig_model_scale_onset.pdf/png`: Model scale comparison bar chart with failure mode annotations

## 7. 论文 Implications

1. **Phase transition framing**: 可在 Discussion 中将 α_c≈0.48 称为 "detection threshold"，sigmoid fit 的 steep crossover 特征表明 causal signal 的出现是近乎开关式的（sub-critical → super-critical），有潜力写为 "sharp onset of causal detectability"
2. **Not first-order**: 避免直接 claim "first-order phase transition"（需要更密采样和更长时间序列验证），建议用 "steep crossover" 或 "near-discontinuous onset"
3. **Model scale**: 信号弱化不是 scale 效应，而是 canary metric trajectory 与 downstream metric 的耦合/解耦问题。ECE 在所有模型上比 entropy 更鲁棒（D126 结论）
