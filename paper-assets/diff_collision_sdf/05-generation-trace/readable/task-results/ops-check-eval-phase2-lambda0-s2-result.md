# ops check eval phase2 lambda0 s2 result

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_eval_phase2_lambda0_s2_result_20260526T115657_result.json`
- **Structured JSON:** [`6ca330f8d9d9cd0b6dd3.json`](../../sessions/6c/6ca330f8d9d9cd0b6dd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron，可能已被清理或未创建。Registry 已更新为 DONE。

## eval_phase2_lambda0_s2 结果 (Phase 2 λ=0, seed 2, 10K step)

| Task | Name | TSR (%) | CAR (%) | EE Disp (m) | Frozen (%) |
|------|------|---------|---------|-------------|------------|
| 0 | orange_juice → basket | 30.0 | 56.0 | 0.3837 | 0.0 |
| 1 | chocolate_pudding → basket | 76.0 | 74.0 | 0.4059 | 0.0 |
| 2 | milk → basket | 42.0 | 74.0 | 0.3565 | 0.0 |
| 3 | bbq_sauce → basket | 66.0 | 26.0 | 0.3903 | 0.0 |
| **Mean** | | **53.5** | **57.5** | **0.3841** | **0.0** |

- Frozen rate = 0%（所有 episode 的 max_ee_displacement 均远大于 0.0001m 阈值）
- Registry 已更新：metrics、conclusion=success、checkpoint_path、log_path，状态转 DONE

---
