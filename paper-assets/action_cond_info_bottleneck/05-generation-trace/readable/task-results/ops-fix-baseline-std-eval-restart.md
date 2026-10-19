# ops fix baseline std eval restart

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-baseline-std-eval-restart_20260516T032002_result.json`
- **Structured JSON:** [`2f70e60ec40f1d0a1e64.json`](../../sessions/2f/2f70e60ec40f1d0a1e64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**1. PID 733616 是 libero_10 eval 进程**
- 命令：`lerobot-eval --env.task=libero_10 --eval.n_episodes=50 --output_dir=/root/acib/outputs/baseline_std_v3/libero_10`
- 已运行 ~17 分钟，正在正常产出结果
- 进度：task `libero_10_0` 已完成 6/50 episodes（`eval_episode_0.mp4` ~ `eval_episode_5.mp4`）
- 占用 6601 MiB on cuda:1

**2. 无需重启 eval** — 进程存活且正常工作，保留不动。

**3. cuda:1 当前 GPU 使用：**

| PID | 显存 | 身份 |
|-----|------|------|
| 733616 | 6601 MiB | baseline_std libero_10 eval（本进程） |
| 744808 | 16214 MiB | seed2 训练 |
| **合计** | **~22.8 GB / 96 GB** | 空间充裕 |

cuda:0 上还有两个进程（675231: 5910 MiB, 682233: 16214 MiB）。

---
