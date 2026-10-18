# ops deploy l2 k095 object and check xvla

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_l2_k095_object_and_check_xvla_20260523T042111_result.json`
- **Structured JSON:** [`c0fbd23f9377a88a495a.json`](../../sessions/c0/c0fbd23f9377a88a495a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

X-VLA Long registry 已更新为 DONE。

**关于 π0.5 L2norm k=0.95 Object seed42 v2**: Registry 中 `eval_pi05_l2norm_k095_object_seed42_v2` 条目已存在，且 `extra.previous_failure` 字段包含完整的成功结果：

| 指标 | 值 |
|------|-----|
| **Overall SR** | **98.2%** (491/500) |
| per_task_sr | [96, 98, 96, 96, 96, 100, 100, 100, 100, 100] |
| tokens_kept | 243/256 |
| wall_time | 63.2 min |
| completed_at | 2026-05-22T01:40 |

该实验昨天已经跑完且成功。是否需要：
- **A**: 直接将 v2 恢复为 DONE（复用已有结果，不重跑）
- **B**: 仍然重新部署跑一次

---

### Part 2 结果：X-VLA Random k=0.95 Long seed42 ✅ DONE

| 指标 | 值 |
|------|-----|
| **Overall SR** | **48.2%** (241/500) |
| 95% Wilson CI | [43.9%, 52.6%] |
| per_task_sr | [0, 46, 72, 90, 54, 98, 18, 10, 92, 2] |
| tokens_kept | 47/50 |
| wall_time | 91.2 min |

Random k=0.95 在 Long suite 上 48.2%，对比 hypothesis 中提到的 L2 k=0.95=47.0%，两者差距不显著（CI 重叠），说明 Long suite 下 random 和 L2 pruning 效果接近。

---
