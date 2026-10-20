# infra cuda1 investigation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cuda1-investigation_20260516T215637_result.json`
- **Structured JSON:** [`4ab87f2d375ec3e1a43e.json`](../../sessions/4a/4ab87f2d375ec3e1a43e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

**nvidia-smi 输出摘要：**
- GPU 0: 21% 利用率, 3943MiB 已用 — PID 612881 (python) + PID 614980 (python)
- GPU 1: 18% 利用率, 4161MiB 已用 — PID 614980 (python)

**cuda:1 上的进程：**
| 字段 | 值 |
|------|------|
| PID | 614980 |
| 命令行 | `python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --logdir logdir/exp_019a_v2_pickcube_baseline --steps 200000 --seed 1 --compile False --device cuda:1 --gate_enabled False --checkpoint_every 50000` |
| 启动时间 | Sun May 17 04:12:30 2026 (约 1.75 小时前) |
| GPU 显存占用 | 4152MiB (cuda:1) + 643MiB (cuda:0, 可能是 envpool/渲染) |

**结论：** 这是 **exp_019a_v2_pickcube_baseline**（ManiSkill3 PickCube baseline，无 gate），正常运行中。

**建议动作：** 需要更新 registry，将该实验标记为 RUNNING，设备为 cuda:1，PID 614980。无需 kill。

---
