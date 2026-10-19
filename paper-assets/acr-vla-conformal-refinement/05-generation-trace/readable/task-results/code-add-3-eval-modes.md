# code add 3 eval modes

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add-3-eval-modes_20260523T005521_result.json`
- **Structured JSON:** [`c18be4d29d30edbe4c0a.json`](../../sessions/c1/c18be4d29d30edbe4c0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**三个方向全部已在 evaluate.py 中实现，无需代码修改。**

| 方向 | Mode | 状态 | 关键实现 |
|------|------|------|----------|
| A: norm clipping | `crm_obs_only` + `--max_correction_norm` | ✓ 已有 | argparse L98, CRM 属性覆盖 L600-601, crm.py L65 clamp |
| B: selective CRM | `adaptive_conformal_crm` | ✓ 已有 | `select_action_conformal_crm()` L447-493, K=2 hardcoded, L2 gate |
| C: reconvla | `reconvla` | ✓ 已有 | `select_action_reconvla()` L269-288, 调用 `reconvla_select()` |

部署命令已写入 `artifacts/deploy_3dir_spatial_seed42.md`，5 个 GPU 并行跑 spatial seed42 × 20 rollouts。

---
