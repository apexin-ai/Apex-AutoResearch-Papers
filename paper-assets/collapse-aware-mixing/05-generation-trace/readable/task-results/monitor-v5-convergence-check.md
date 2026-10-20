# monitor v5 convergence check

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5_convergence_check_20260512T172140_result.json`
- **Structured JSON:** [`05c25580f639db3cd7f0.json`](../../sessions/05/05c25580f639db3cd7f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告：mvp_pilot_v5 — **正常收敛**

### 训练（已完成）
- **1373/1373 steps 全部完成**，耗时 51 分钟
- **平均 train_loss = 2.5459**，最后三次 logging：2.5317 → 2.5311 → 2.5417（稳定在 2.5 附近，正常范围 2-4 内）
- **grad_norm 极稳定**：始终 ~1.0（远低于 10 的警戒线）
- **无 NaN/Inf**
- 对比 v4（lr=1e-5 在 step 760 发散至 loss 106-116），v5 的 lr=2e-6 完全修复了发散问题

### Checkpoint 评估（进行中）
- 共 10 个 checkpoint + 1 个最终 = **11 个待评估**
- 已完成 2/11，正在评估第 3 个（step 456）
- 每个 checkpoint 评估耗时 ~13 分钟
- 已有评估指标：
  - ckpt-152: eff_rank=670.7, ppl=12.80
  - ckpt-304: eff_rank=665.6, ppl=12.80（ppl 稳定，eff_rank 略降 — 合理）

### 预估剩余时间
9 个 checkpoint 待评估 × ~13 min/each ≈ **约 2 小时完成全部 G0 评估**。

---
