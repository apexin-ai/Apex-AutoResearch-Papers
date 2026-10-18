# ops launch xvla baselines spatial goal cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch-xvla-baselines-spatial-goal-cqa1_20260520T225343_result.json`
- **Structured JSON:** [`ebc4072d359e4ad5f28a.json`](../../sessions/eb/ebc4072d359e4ad5f28a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已成功启动并注册。

## 汇总

| 实验 | tmux session | GPU | 显存占用 | 状态 |
|------|-------------|-----|---------|------|
| **Spatial baseline** | `eval_xvla_baseline_spatial_seed42` | GPU 0 | 4601 MiB | RUNNING，Task 0 开始（"pick up the black bowl..."） |
| **Goal baseline** | `eval_xvla_baseline_goal_seed42` | GPU 3 | 4520 MiB | RUNNING，Task 0 开始（"open the middle drawer..."） |

- 模型加载正常：879.5M params, float32
- Vision tokens: 50/50 (100%), no pruning applied
- Suite 正确识别：libero_spatial / libero_goal，各 10 个 task
- 日志路径：`/tmp/eval_xvla_baseline_spatial.log` 和 `/tmp/eval_xvla_baseline_goal.log`

---
