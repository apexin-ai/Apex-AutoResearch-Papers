# ops verify 4 jobs alive v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_4_jobs_alive_v2_20260525T095721_result.json`
- **Structured JSON:** [`c462dd3c1f3013d6c2c6.json`](../../sessions/c4/c462dd3c1f3013d6c2c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告：1 存活 / 3 已死

| 任务 | 状态 | 说明 |
|------|------|------|
| `train_pi05_a1_spatial_bowl_s0_l005` | ✗ 已死 | `ValueError: quantile stats must be provided if use_quantile_norm is True. Key state is missing q01 or q99.` EXIT_CODE=1 |
| `train_pi05_phase2_lambda0_s0` | ✓ 存活 | Step 7/10000, loss=0.1352, ~1.6s/it, GPU 0 占用 7.64GB/19.27GB |
| `eval_pi05_a1_30k_s1_l005_v2` | ✗ 已死 | `unrecognized arguments: --checkpoint_path ... --scene object_pudding` EXIT_CODE=2 |
| `eval_pi05_a1_30k_s2_l005_v2` | ✗ 已死 | 同上，参数解析错误 EXIT_CODE=2 |

**GPU**: 仅 GPU 0 在用 (8%, 7819MiB/97887MiB)，GPU 1-3 空闲。

**崩溃原因**:
- **spatial_bowl 训练**: quantile normalization 配置问题 — `use_quantile_norm=True` 但缺少 q01/q99 统计量
- **两个 eval**: `eval_safelibero.py` 不认识 `--checkpoint_path` 和 `--scene` 参数，启动脚本参数写错了

---
