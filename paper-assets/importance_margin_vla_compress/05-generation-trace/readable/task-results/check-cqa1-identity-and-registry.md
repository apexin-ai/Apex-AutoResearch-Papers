# check cqa1 identity and registry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_identity_and_registry_20260522T180318_result.json`
- **Structured JSON:** [`a6a54d6e215fa69057c0.json`](../../sessions/a6/a6a54d6e215fa69057c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 四卡状态

| GPU | VRAM | Util | 实验 | 进度 |
|-----|------|------|------|------|
| cuda:0 | 15.4G / 24G | 38% | OpenVLA baseline Spatial k=1.0 seed42 | Step 150/280 (某 episode)，自 May22 持续运行 |
| cuda:1 | 10.2G / 24G | 22% | π0.5 Random k=0.7 **Goal** seed42 | T7进行中，T1-6完成 (281/350=80.3%) |
| cuda:2 | 10.2G / 24G | 45% | π0.5 Random k=0.5 **Goal** seed42 | T6进行中 (14/20=70%)，T1-5完成 (226/300=75.3%) |
| cuda:3 | 10.1G / 24G | 1% | π0.5 L2Norm k=0.95 **Long** seed42 | T1刚完成 (98%)，后续链式任务: k=0.9 → k=0.85 |

### 结论

- **cuda:2 不空闲**——正在跑 Random k=0.5 Goal，45% util 活跃运行。之前看到的 9727 MiB / 0% util 可能是任务间切换瞬态。**不部署新实验。**
- **cuda:3** 在跑 L2Norm k=0.95 Long（T1刚完成 98%），后面还链了 k=0.9 和 k=0.85，有活。
- **cuda:0** OpenVLA baseline Spatial 仍在跑（已运行 ~45h）。
- **cuda:1** Random k=0.7 Goal 正常推进，T7 开头 10/10=100%。
- **无卡可用于新部署。** Random k=0.9 Long seed42 需等某卡释放后再安排。

### 需补 registry 的实验

从进程看到以下可能未注册的实验：
- `eval_pi05_random_k05_goal_seed42` (cuda:2)
- `eval_pi05_random_k07_goal_seed42` (cuda:1)  
- `eval_pi05_l2norm_k095_long_seed42` (cuda:3, 含链式 k=0.9, k=0.85)

需要确认这些是否已在 registry 中。要我查一下吗？

---
