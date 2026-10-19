# ops recover displacement from logs

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_recover_displacement_from_logs_20260525T131004_result.json`
- **Structured JSON:** [`710b1e09d366e853e9c0.json`](../../sessions/71/710b1e09d366e853e9c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. Per-episode displacement 在日志中？**否。**

日志每 10 个 episode 只记录 `success/collided/steps`，不含 displacement：
```
Episode 10/50: success=False, collided=True, steps=300
```
Displacement 只有 per-task 的聚合平均值 `Avg max displacement = X.XXXXm`。

### 2. 保留的 JSON？

- `/root/colliforce-vla/eval_results/` **为空**（0 文件）
- JSON 实际保存路径是 `/root/autodl-tmp/eval_results/`（未能在 3 轮内检查）

### 3. 可从日志恢复的 per-task 平均值

| eval | task 0 | task 1 | task 2 | task 3 | Avg TSR | Avg CAR |
|------|--------|--------|--------|--------|---------|---------|
| **s1_l005** (v4) | 0.0603m | 0.0929m | 0.0019m | 0.0920m | 5.5% | 52.5% |
| **s2_l005** (v4) | 0.0377m | 0.0884m | 0.0012m | 0.0885m | — | — |
| **s1_l01** (v2) | 0.0462m | 0.0619m | 0.0040m | 0.0962m | — | — |

注意：s1_l005 和 s2_l005 的日志文件名是 **v4** 不是 v2。

### 结论

**s1_l005 和 s2_l005 的 per-episode displacement 不可恢复。** 日志中只有 per-task 聚合值，没有逐 episode 的 displacement。如果需要 per-episode 粒度的数据，必须重跑。如果只需 per-task 平均值，上表数据已完整。

---
