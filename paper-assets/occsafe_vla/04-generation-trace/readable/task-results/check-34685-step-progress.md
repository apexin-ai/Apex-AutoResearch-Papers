# check 34685 step progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_34685-step-progress_20260527T104255_result.json`
- **Structured JSON:** [`450d3e7aad3904d89f10.json`](../../sessions/45/450d3e7aad3904d89f10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685 训练进度报告

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 99% | 62.2/97.9 GB |
| cuda:1 | 99% | 62.2/97.9 GB |
| cuda:2 | 65% | 62.2/97.9 GB |
| cuda:3 | 99% | 63.0/97.9 GB |

### 训练进度

| 实验 | 当前 step | 总 step | 进度 | 剩余时间(估) | 速度 |
|------|-----------|---------|------|-------------|------|
| detach_ln_v2_s1 (cuda:0) | 41,172 | 50,005 | 82% | ~2h 41min | ~1.08 it/s |
| detach_ln_s4 (cuda:1) | 41,210 | 50,005 | 82% | ~2h 33min | ~1.08 it/s |
| ablation_occ_detach_s4 (cuda:2) | 38,371 | 50,005 | 77% | ~3h 14min | ~1.06 it/s |
| mvp_occ_s4 (cuda:3) | 38,307 | 50,005 | 77% | ~3h 14min | ~1.06 it/s |

所有实验预计在 **~3.25h 内完成**，远早于 2026-05-28 12:00 UTC 截止时间。

### 磁盘
`/root/autodl-tmp`: 319G/350G (91%), 剩余 32G — 偏紧但够用。

### Eval 脚本
`run_libero_eval_safe.py` **不存在**于指定路径。服务器上有以下 eval 脚本可用：
- `/root/occsafe_vla/openvla-oft/vla-scripts/evaluate_safelibero.py`
- `/root/occsafe_vla/eval/eval_safelibero.py`
- `/root/occsafe_vla/eval_batch_34685.sh`

---
