# ACR-VLA CRM Bug Audit Report
Date: 2026-05-14
Auditor: worker_diag_acr-correction-logic-review

## CRITICAL

### C1: Train/eval state dimension mismatch (6D vs 8D)

**Files:** smolvla_wrapper.py:180 vs smolvla_wrapper.py:142-145

CRM training precompute 使用 `ee_states` (6D: eef_pos + axisangle, 无 gripper)，但 eval 使用完整 8D state (含 gripper_qpos)。

SmolVLA 在 precompute 时收到零填充的 positions 6-7，产出不同的 obs_feat (960D) 和 K samples。CRM 在错误分布上训练，eval 时遇到从未见过的正确输入。

**修复**: build_training_samples 中 state 扩展到 8D（含 gripper_qpos），需要重新 precompute + retrain + re-eval。

## WARNING

### W1: ACI 死代码 — alpha 永远不更新
evaluate.py:287,303 — ACI 实例化但从未传入 action selection。

### W2: Mean 作为 base action — multimodal 分布下无效
evaluate.py:174 — ma = K_samples.mean(dim=0)，multimodal 时 mean 落在无效区域。reconvla argmin 避免了这个问题。

### W3: Conformal quantile 退化 — K=10, alpha=0.1 → 永远取 max
cgs.py:61-64 — quantile index = ceil(0.9 * 11) - 1 = 9 = max。conformal radius 无判别力。

### W4: CRM correction 无 magnitude 约束
crm.py:44 — delta 无 clamping/scaling，可产出任意大修正。

## OK (verified correct)
- CRM output 语义 (mean+delta) train/eval 一致
- Gripper 排除，mean-aggregated 独立处理
- 30D = 5×6 维度映射正确
- Train 和 eval 都在 unnormalized action space
- CGS 数学正确 (Ledoit-Wolf cov, regularized inverse, Mahalanobis)
- CRM 输入拼接顺序 [ma(30), uf(40), obs(960)] 一致
- chunk_size=50 → H_EFF=5 截断一致
