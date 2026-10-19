# ops quick eval alive check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_quick-eval-alive-check_20260516T203156_result.json`
- **Structured JSON:** [`40e384ff07a70681c6cc.json`](../../sessions/40/40e384ff07a70681c6cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 进程均**存活**，正在执行 rollout：

| PID | 任务 | 运行时间 | 显存 |
|-----|------|---------|------|
| 104743 | v7_contrastive seed1 eval | 3h10m | 3842 MiB (GPU 1) |
| 111920 | v7_seed2 eval | 3h06m | 4367 MiB (GPU 0) |

当前进度：两者都在跑 rollout（280 steps），running_success_rate=0.0% 表明当前 episode 尚未成功。GPU 利用率低（0-1%）是正常的——eval rollout 主要是 CPU 模拟 + 间歇性 GPU 推理。

---
