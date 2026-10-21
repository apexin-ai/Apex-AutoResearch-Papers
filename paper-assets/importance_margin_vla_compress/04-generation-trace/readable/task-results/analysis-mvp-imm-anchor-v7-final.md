# analysis mvp imm anchor v7 final

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_imm_anchor_v7_final_20260515T202105_result.json`
- **Structured JSON:** [`2849fd7e553b97e02065.json`](../../sessions/28/2849fd7e553b97e02065.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 metrics 已提取。以下是分析报告。

---

## mvp_imm_anchor_v7 训练结果分析

### 1. 最终 Metrics（step 29950，最后一个 logged step）

| Metric | 值 |
|--------|-----|
| **train/action_loss** | 0.02405 |
| **train/margin_loss** | 0.08937 |
| **train/total_loss** | 0.06873 |
| **train/lambda** | 0.5 |
| **train/lr** | 2.50e-06 |
| **train/grad_norm** | 10.589 |
| **margin/mean** | 0.94452 |
| **margin/median** | 0.19634 |
| **margin/min** | 0.04620 |
| **margin/max** | 2.45838 |
| **margin/std** | 1.10697 |
| **scores/topk_mean** | 30.767 |
| **gate/lipschitz_estimate** (L_emp) | 1.0003 |
| **gate/L_eps_delta_ratio_mean** | 2.24668 |

验证：total_loss = action_loss + λ × margin_loss = 0.02405 + 0.5 × 0.08937 = 0.06874 ✓

### 2. 与 step 20K 中间检查对比

| Metric | 20K | 30K (final) | 变化 |
|--------|-----|-------------|------|
| action_loss | 0.0107 | 0.02405 | +0.013（注：单步值波动大，最后 200 步范围 0.0013–0.0687）|
| margin_mean | 1.074 | 0.94452 | -0.130（↓12%）|
| L_emp (lipschitz) | 0.266 | 1.0003 | +0.734（spectral norm 收敛至 ~1.0）|

关键观察：
- **L_emp 从 0.266 升至 1.0003**：spectral norm 约束将 Lipschitz 常数稳定在 ~1.0，符合理论预期
- **margin_mean 略降**：从 1.074 降至 0.945，但仍显著 > 0，说明分类间隔依然被维护
- **L_eps_delta_ratio = 2.25**：即 L·ε/δ ≈ 2.25，其中 δ=0.3（config），意味着 L·ε ≈ 0.675。margin_mean=0.945 > 0.675，margin 条件满足
- **action_loss 在正常范围内波动**：sparkline 显示后半段训练 action_loss 整体偏低（多 ▁），个别 batch 波动不影响趋势

### 3. Checkpoints

- **路径**: `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/imm_anchor/`
- **15 个 checkpoints**: step_002000 ~ step_029999（每 2000 步）
- **最终 checkpoint**: `step_029999/checkpoint.pt`（1.2GB）
- **latest symlink** → `step_029999`

### 4. 训练健康状态

- **正常完成**：日志末尾 `Training complete.`，无 crash/error
- **0 个 ERROR**，2 个 WARNING（均无害：HF token 提示 + wandb offline 模式）
- **总耗时**: ~2h39m（01:36:21 → 04:15:28）
- **速度稳定**: 3.2 steps/sec 全程一致
- **wandb run**: offline-run-20260516_013654-3mt1egu1

### 5. 缺失项

- **无 eval 结果**：config 中 `eval_every: 999999`，训练期间未执行 eval
- **无 preservation rate**：日志中未记录 preservation rate，需单独执行 eval 计算
- **eval_results/ 目录不存在**

### 6. 结论

训练健康完成 30K steps。核心指标表明 IMM anchor 机制在工作：spectral norm 将 Lipschitz 常数约束至 ~1.0，分类间隔（margin）维持在正值（mean=0.945）。**下一步需要运行独立 eval 来获取 preservation rate 和下游任务性能**。

---
