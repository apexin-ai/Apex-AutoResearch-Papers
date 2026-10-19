# analyze eval stepwise s0 l1 26k v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_stepwise_s0_l1_26k_v2_20260527T055311_result.json`
- **Structured JSON:** [`153f580f3e02a0e2da51.json`](../../sessions/15/153f580f3e02a0e2da51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## eval_stepwise_s0_l1_26k_v2 结果

| | 26K v2 (--pi05 fixed) | 24K (no --pi05) | LoRA baseline |
|---|---|---|---|
| **CAR** | 53.5% | 55.5% | 54.5% |
| **Frozen** | **0.0%** | 29.5% | 0.0% |
| **dfCAR** | **53.5%** | 36.9% | 54.5% |
| **TSR** | 53.0% | — | — |

**结论**：frozen 问题完全由缺失 `--pi05` 导致，非 SDF 训练退化。修复后 dfCAR=53.5%，仅比 LoRA baseline 低 1pp，SDF 辅助损失 (λ=1.0) 未损害碰撞避免能力。

**已完成操作**：
- Registry 已更新为 DONE/success，含完整 metrics
- Cron 已删除

**28K checkpoint**：不存在。训练当前在 step 27505/30000 (92%)，约 38 分钟后到达 28K，剩余 ~3.2h 完成全部 30K。

---
