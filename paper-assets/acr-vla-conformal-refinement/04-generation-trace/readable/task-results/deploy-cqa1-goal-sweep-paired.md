# deploy cqa1 goal sweep paired

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-goal-sweep-paired_20260526T010940_result.json`
- **Structured JSON:** [`d5f433faac956bf61fa7.json`](../../sessions/d5/d5f433faac956bf61fa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**6 个 GPU 全部被占用。** 当前正在运行一批 τ-sweep 实验（从 08:32 开始，已运行约 40 分钟）：

| GPU | 当前实验 | 状态 |
|-----|---------|------|
| 0 | τ=0.05 goal s42 | 运行中 |
| 1 | τ=0.10 goal s42 | 运行中 |
| 2 | τ=0.15 goal s42 | 运行中 |
| 3 | τ=0.20 goal s42 | 运行中 |
| 4 | **τ=0.30 goal s42** | 运行中 |
| 5 | **τ=0.35 goal s42** | 运行中 |

注意：**τ=0.30 和 τ=0.35 已经在跑了**（GPU 4/5），是你要部署的 6 个实验中的 2 个。

剩余需要部署的 4 个实验：
- τ=0.40 s42
- τ=0.45 s42
- Goal VLA-only s48
- Goal Adaptive s48

当前批次预计再需 ~20 分钟完成（按 45-60 分钟总时长估算）。两个选项：

1. **等当前批次结束后部署剩余 4 个实验**（τ=0.30/0.35 已在跑，无需重复）
2. **kill 掉已完成或低优先级的实验腾出 GPU 立即部署**

怎么处理？

---
