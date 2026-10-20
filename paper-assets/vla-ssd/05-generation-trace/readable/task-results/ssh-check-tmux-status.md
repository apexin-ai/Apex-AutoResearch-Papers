# ssh check tmux status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-tmux-status_20260515T175741_result.json`
- **Structured JSON:** [`268ffd3aefe6e98387d5.json`](../../sessions/26/268ffd3aefe6e98387d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### Tmux Sessions
| Session | 状态 |
|---------|------|
| `lg_gc_untrained` | 存在，运行中 |
| `lg_gc_dino` | **不存在** |

### GPU 使用
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| GPU 0 | RTX PRO 6000 Blackwell (96GB) | 0% | 1747/97887 MiB — 被 `python` (PID 635369) 占用 |
| GPU 1 | RTX PRO 6000 Blackwell (96GB) | 0% | 空闲 |

占用 GPU 0 的进程：`train_probes.py --features_dir untrained_libero_goal/ --probe_type goal_classification`

### 任务状态
| 任务 | 状态 | 详情 |
|------|------|------|
| `lg_gc_dino` | **已完成** (EXIT_CODE=0) | 最终结果: acc=0.8626, traj_acc=1.0, F1=0.8412, 保存到 `results/dinov2_libero_goal/goal_classification/` |
| `lg_gc_untrained` | **运行中** | 当前在 Layer 24/33, 最新: Layer 23 acc=0.9991, F1=0.9990 |

---
