# exp deepseek traj v2 fixed s42

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_deepseek-traj-v2-fixed-s42_20260516T135307_result.json`
- **Structured JSON:** [`8b4ad64abfe2a353b8af.json`](../../sessions/8b/8b4ad64abfe2a353b8af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**TRAJ v2 (seed 42) 已在运行中，无需重新启动。**

| 项目 | 值 |
|------|-----|
| PID | 511676 |
| GPU | cuda:2 (17338 MiB) |
| 进度 | 503/756 steps (66%), epoch 2 进行中 |
| Total steps | 756 (3 epochs × 252 steps/epoch) |
| 速度 | ~3.9s/step |
| 剩余 | ~253 steps × 3.9s ≈ **16-17 分钟后完成** |
| Eval loss (epoch 1) | 0.0923 |
| LABEL_MAP | `{1: "resolved", 0: "unresolved"}` ✓ |
| 输出目录 | `/root/autodl-tmp/checkpoints_deepseek_traj_v2/` |

Prompt 格式确认使用 resolved/unresolved。训练 loss 从 0.39 → 0.088 下降正常。预计约 21:55 UTC 完成。

---
