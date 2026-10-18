# ops c5 gripper bugfix retrain

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c5_gripper_bugfix_retrain_20260519T222001_result.json`
- **Structured JSON:** [`5440ce312b51ba5fa349.json`](../../sessions/54/5440ce312b51ba5fa349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Step 50 的 loss 已输出。关键指标：

- **grip_loss = 0.6485** — 低于 0.69（ln2 ≈ random baseline），修复生效，gripper 开始学习 ✓
- arm_loss = 0.0797
- total_loss = 0.1497

## 任务完成总结

| 项目 | 结果 |
|------|------|
| **代码修复** | L144: `binary_cross_entropy_with_logits` → `binary_cross_entropy`; L148: `0.01` → `0.1` |
| **旧进程** | PID 47691 已 kill，GPU 1 显存已释放 |
| **旧 checkpoint** | 重命名为 `roboflamingo_libero_c5_buggy_20260519` |
| **新训练** | PID 53406, GPU 1 (48GB), 99% 利用率 |
| **exp_id** | `train_c5_roboflamingo_v2` |
| **log** | `/root/autodl-tmp/importance_margin_vla_compress/logs/train_c5_roboflamingo_v2.log` |
| **save_dir** | `/root/autodl-tmp/checkpoints/roboflamingo_libero_c5_v2` |
| **Step 50 grip_loss** | 0.6485 < 0.69 — 修复生效，gripper 正在学习 |
| **GPU 0 (C4)** | 未受影响，PID 26118 正常运行 |

---
