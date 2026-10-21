# deploy bjb2 28827 tau sweep goal

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-tau-sweep-goal_20260526T010924_result.json`
- **Structured JSON:** [`6894e3bcd8b44e0059dd.json`](../../sessions/68/6894e3bcd8b44e0059dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 6 个 GPU 都在运行实验，无法部署。** 当前占用情况：

| GPU | 实验 | 启动时间 |
|-----|------|---------|
| 0 | τ=0.40 spatial s42 | 07:30 |
| 1 | τ=0.45 spatial s42 | 07:30 |
| 2 | vla_only goal s45 | 07:40 |
| 3 | adaptive τ=0.25 goal s45 | 07:40 |
| 4 | vla_only goal s47 | 07:40 |
| 5 | adaptive τ=0.25 goal s47 | 07:40 |

注意：**Spatial τ=0.45 s42 已经在 GPU 1 上运行**（checkpoint 路径是 `/root/autodl-tmp/checkpoints/...`，与任务指定的 `/root/acr-vla-conformal-refinement/checkpoints/...` 不同）。

这些实验已运行约 1.5-2 小时（CPU 利用率 530%+，仍在跑），预计很快结束。

两个选项：
1. **等当前实验跑完**再部署 Goal τ-sweep（约 30 分钟内应该空出来）
2. **只部署 Goal τ-sweep 的 5 个实验**（等 GPU 空出后立即启动），Spatial τ=0.45 已在跑不需要重复

怎么处理？

---
