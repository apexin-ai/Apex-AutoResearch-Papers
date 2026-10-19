# ssh launch v71 training manual

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch-v71-training-manual_20260517T064524_result.json`
- **Structured JSON:** [`1a9e2a569c4f93a1f8d2.json`](../../sessions/1a/1a9e2a569c4f93a1f8d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双 seed 训练已成功启动。

## 验证结果

| 项目 | 状态 |
|------|------|
| **tmux sessions** | `v71_seed1` + `v71_seed2` 均存活 |
| **训练 PID** | seed1: 3619 (主), seed2: 3693 (主) + DataLoader workers (5001-5009) |
| **GPU 显存** | GPU 0: 15007 MiB (82% util), GPU 1: 15007 MiB (94% util) |
| **初始输出** | 两个 seed 均已完成模型加载（450M params, 123K trainable / 0.0%）、数据集加载（273K frames），正在训练 |
| **错误** | 无 |

训练配置确认：scorer-only 模式，base policy frozen，20000 steps，batch_size 64，bfloat16。

---
