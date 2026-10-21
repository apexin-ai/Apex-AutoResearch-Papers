# monitor urgent eval status bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_urgent-eval-status-bjb1_20260514T131552_result.json`
- **Structured JSON:** [`e8ad6aa71d607fcebd21.json`](../../sessions/e8/e8ad6aa71d607fcebd21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个进程存活，状态汇总：

```
实验名                      | PID    | 状态    | 运行时长 | 进度          | 当前 task 成功率
eval-acr-spatial-v3 (CORE) | 197057 | RUNNING | 59m      | Task 1/10, rollout 5/10 | 1/5
eval-scalar-unc-spatial-v2 | 197324 | RUNNING | 59m      | Task 1/10, rollout 5/10 | 0/5
eval-obs-only-spatial-v3   | 211961 | RUNNING | 27m      | Task 1/10, 刚加载完     | —
eval-acr-object-v3         | 197803 | RUNNING | 59m      | Task 1/10, rollout 5/10 | 0/5
```

**GPU 状态：**
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 (acr-spatial) | 20% | 20005 / 24564 MiB |
| 1 (scalar-unc) | 22% | 1459 / 24564 MiB |
| 2 (obs-only) | 17% | 1459 / 24564 MiB |
| 3 (acr-object) | 21% | 1459 / 24564 MiB |

**关键观察：**
- 所有 4 个实验都还在 **Task 1/10**，进度很早期（每个 benchmark 有 10 个 task × 10 rollouts = 100 次评估）
- 每个 rollout 最多 300 步，59 分钟才跑到第 1 个 task 的第 5 个 rollout，预估 **总时长约 20 小时**
- GPU 0 显存占用 20 GB 远高于其他 GPU 的 1.4 GB，可能是 acr_vla 模式加载了更多组件
- eval-obs-only-spatial-v3 启动较晚（27 min vs 59 min），日志中尚无 rollout 进度输出
- **eval-acr-spatial-v3 (CORE CLAIM)**：目前 task 1 前 5 个 rollout 中成功 1 次，尚不足以判断趋势

---
