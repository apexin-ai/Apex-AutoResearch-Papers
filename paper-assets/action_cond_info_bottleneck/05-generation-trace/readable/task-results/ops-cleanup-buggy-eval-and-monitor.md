# ops cleanup buggy eval and monitor

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-buggy-eval-and-monitor_20260516T172525_result.json`
- **Structured JSON:** [`8e982f8f46751e6d07ed.json`](../../sessions/8e/8e982f8f46751e6d07ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就位。汇报：

**1. Kill 结果**
- PID 101853 (buggy seed2 eval): 已 kill ✓
- monitor_seed2 tmux: 已删 ✓
- monitor_seed1 tmux: 已删 ✓

**2. GPU 进程**
| GPU | PID | 显存 | 任务 |
|-----|-----|------|------|
| GPU-0 (b869...) | 111920 | 6535 MiB | fixed seed2 eval (刚启动，已在跑 rollout) |
| GPU-1 (5c82...) | 104743 | 6010 MiB | fixed seed1 eval |

**3. Tmux sessions**
- `v7_eval_fixed_seed1` — fixed seed1 eval
- `fixed_seed2_eval` — fixed seed2 eval

**4. Fixed seed2 eval 已部署确认**
- 直接启动（PID 46186 buggy seed1 eval 已自然完成，无需 monitor 等待）
- checkpoint: `acib_v7_seed2/checkpoint-20000`
- suites: libero_spatial, libero_object, libero_goal, libero_10
- 日志: `/root/autodl-tmp/v7_eval_fixed_seed2.log`
- 已进入 rollout 阶段，运行正常

---
