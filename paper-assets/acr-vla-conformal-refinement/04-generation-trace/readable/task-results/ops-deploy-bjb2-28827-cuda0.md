# ops deploy bjb2 28827 cuda0

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-bjb2-28827-cuda0_20260516T083602_result.json`
- **Structured JSON:** [`a065ac31958a3a2b3810.json`](../../sessions/a0/a065ac31958a3a2b3810.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**总结：**

| 项目 | 状态 |
|------|------|
| eval-mag-perdof-norm003-object | ✓ DONE，overall SR = 14% |
| eval-scalar-object-seed45 | ✓ RUNNING on bjb2-28827:cuda:0 (PID 224623) |

新实验详情：
- **模式**: `crm_scalar`，norm=0.1，seed=45，LIBERO object
- **Checkpoint**: `/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt` (327,966 params)
- **GPU**: 5645 MiB 已占用，10 tasks 已加载，正在 rollout

---
