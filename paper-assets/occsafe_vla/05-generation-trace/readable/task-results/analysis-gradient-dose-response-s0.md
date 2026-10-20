# analysis gradient dose response s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_dose_response_s0_20260525T072629_result.json`
- **Structured JSON:** [`6ac881154066229548f8.json`](../../sessions/6a/6ac881154066229548f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果与第一次运行一致（微小浮点差异）。

4 个 s0 条件的梯度分析完成：
- JSON: `/root/autodl-tmp/analysis/gradient_dose_response_s0/results.json`
- PDF/PNG: `/root/autodl-tmp/analysis/gradient_dose_response_s0/gradient_dose_response.{pdf,png}`

cutoff s0 checkpoints 仍未从 34685 SCP 到位。脚本已更新支持共享 OCC head，一旦 cutoff s0 checkpoints 到位，重新运行即可自动纳入分析。

**当前结果摘要**:

| 条件 | Action Grad (mean) | Aux Grad (mean) | Cosine Sim | Conflict Rate |
|------|-------------------|-----------------|------------|---------------|
| Vanilla | 7.554 | 0 | 0 | 0 |
| Full OCC BN | 8.895 | 0.167 | -0.018 | 0.470 |
| Detach BN | 5.905 | 0 | 0 | 0 |
| Full OCC LN | 11.930 | 0.260 | -0.000 | 0.471 |

关键发现：
1. Full OCC 条件的 aux 梯度确实注入 vision backbone（BN: 0.167, LN: 0.260）
2. Detach 条件验证了梯度切断（0 aux 梯度）
3. Action/Aux 梯度方向近正交（cosine ~0），conflict rate ~47%（接近随机水平50%），说明 OCC 梯度不与 action 梯度冲突
4. Full OCC LN 的 action 梯度最大（11.93），可能与 GroupNorm vs BatchNorm 的梯度特性相关

---
