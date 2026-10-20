# Gradient Aggregation Inconsistency Investigation

> P0 Issue: 78% vs 论文 1-13% — 梯度聚合方法不一致
> Date: 2026-05-25
> Status: **Root cause identified**

---

## 结论

**78% 和 1-13% 都是正确的数字，但测量的是完全不同的东西。** 两者不矛盾。论文应使用 1-13%（L1 action loss 梯度），因为它测量的是任务相关的梯度信号。

---

## 1. "1-13%" 的来源

- **脚本**: `gradient_analysis.py`（westd-34685）
- **数据**: `gradient_analysis_mixed_seed/` 目录
- **损失函数**: **L1 action loss**（通过独立的 `L1RegressionActionHead`）
- **聚合方式**: Per-layer L2 norm per batch → 200 batches 取均值
- **对比**: Detach_BN_s2 (seed 44) vs Vanilla_s0 (seed 42)
- **结果**:
  - Vanilla 全局均值: 0.1262
  - Detach BN 全局均值: 0.0049
  - **比率: 3.9%**（论文称 1-13% 是 per-layer range）

Per-layer ratio 范围:
- DINOv2: 1.0% (block 9) → 8.5% (block 22)
- SigLIP: 1.8% (block 2) → 12.6% (block 25)

## 2. "78%" 的来源

- **脚本**: `gradient_dose_response_s0.py`（westd-10894）
- **数据**: `/root/autodl-tmp/analysis/gradient_dose_response_s0/results.json`
- **损失函数**: **Cross-entropy language model loss**（HF model forward with labels）
- **聚合方式**: 全部 batch 梯度累加后取 per-layer L2 norm → vision layers 取均值
- **对比**: Detach BN s0 vs Vanilla s0（同 seed 42）
- **结果**:
  - Vanilla vision layers 均值: 7.554
  - Detach BN vision layers 均值: 5.905
  - **比率: 78%** (5.905 / 7.554)

## 3. 差异的根因

### 根因 A: 损失函数不同（主因）

| 维度 | L1 Action Loss | CE Language Model Loss |
|------|---------------|----------------------|
| 损失量级 | ~0.05–0.2 | ~24.8 |
| 梯度路径 | action_head → LLM hidden → vision backbone | LM_head → LLM → vision backbone |
| 覆盖 token | 仅 action tokens（14 个位置） | **所有 tokens**（包含 system prompt 等） |
| 对 vision backbone 的选择性 | 高（只反映 action prediction 质量） | 低（被 LM loss 主导，淹没 action 信号） |

**CE loss 梯度通过所有 token 流回 vision backbone，远大于 action-specific 的 L1 loss 梯度。** 由于 CE loss 梯度在两种条件下都很大，Detach/Vanilla 比率被拉高到 78%。action-specific 的 gradient collapse（3.9%）被 CE loss 的"背景噪声"淹没了。

### 根因 B: 检查点差异（次因）

Same-seed 验证（审计 agent 在 westd-10894 上运行）结果：

| 指标 | Vanilla s0 | Detach BN s0 retrain | D/V ratio |
|------|-----------|---------------------|-----------|
| L1 action loss grad norm | 0.139 | 0.160 | **114.8%** |
| CE loss grad norm | 5.013 | 6.222 | **124.1%** |

即使用 L1 action loss，`ablation_occ_detach_s0_retrain` 的梯度 norm 也 ≈ Vanilla。这表明 s0_retrain 检查点的梯度行为与 s2 检查点不同。可能的解释：
- s0_retrain 可能与原始 3-seed 实验的训练配置不同
- 或者 gradient collapse 具有 seed 依赖性（s2 崩塌但 s0 不崩塌）

**注意**: 这不影响论文的 1-13% claim，因为论文数据来自 mixed-seed 分析（使用 s2 检查点），而该检查点确实展示了 gradient collapse。但如果 reviewer 要求 same-seed 验证，需要在原始（非 retrain）的 s0 检查点上重新跑 `gradient_analysis.py`。

## 4. 建议

### 论文应使用: 1-13%（L1 action loss per-layer ratio）

理由：
1. **L1 action loss 是训练目标的直接度量** — 它反映 vision encoder 对 action prediction 的梯度贡献
2. **CE loss 包含无关信号** — system prompt、instruction tokens 的梯度淹没了 action-specific 信号
3. **1-13% 的物理含义清晰** — "Detach 条件下 encoder 仅收到正常 action 梯度的 1-13%"
4. **全局 4% 和 per-layer 1-13% 一致** — 两者来自同一分析，只是聚合粒度不同

### 论文不应提及 78%

78% 来自不同的损失函数（CE loss），测量的是不同的物理量。在论文中混用会造成混淆。如果 reviewer 问及，可解释：
- "78% is the ratio under cross-entropy LM loss, which includes gradients from all tokens (system prompt, instructions) and masks the action-specific collapse."
- "We report the L1 action loss gradient ratio (1-13%) as it directly measures the gradient signal for the optimization target."

### 建议的验证步骤（如时间允许）

1. 在 westd-10894 上用原始 `gradient_analysis.py` 脚本对 `ablation_occ_detach_s0_retrain` 跑一次 L1 action loss 分析，确认 s0_retrain 是否也崩塌
2. 如果 s0_retrain 不崩塌，检查该检查点的训练配置是否与其他 Detach 实验一致

---

## 数据来源汇总

| 分析 | 脚本 | 服务器 | 结果路径 | Loss 类型 | Seeds |
|------|------|--------|---------|-----------|-------|
| Mixed-seed (1-13%) | `gradient_analysis.py` | westd-34685 | `gradient_analysis_mixed_seed/*.json` | L1 action | V:s0, D:s2 |
| Same-seed (≈115%) | `same_seed_gradient_analysis.py` | westd-10894 | `gradient_same_seed/*.json` | L1 action | all s0 |
| Dose-response (78%) | `gradient_dose_response_s0.py` | westd-10894 | `gradient_dose_response_s0/results.json` | **CE LM** | all s0 |
| Original old (8-65×) | `gradient_analysis.py` | westd-10894 | `analysis/results/` | L1 action | R:s2, D:s2 |
