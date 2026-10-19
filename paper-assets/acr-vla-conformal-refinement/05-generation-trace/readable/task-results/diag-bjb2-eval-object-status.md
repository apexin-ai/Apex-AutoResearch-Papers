# diag bjb2 eval object status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb2-eval-object-status_20260513T235503_result.json`
- **Structured JSON:** [`f1f0c594bea23db04ad2.json`](../../sessions/f1/f1f0c594bea23db04ad2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**进程状态：Running**

| 项目 | 详情 |
|------|------|
| PID | 117697, State=R (actively running on CPU) |
| 运行时间 | 19 小时 38 分钟 |
| GPU | 5573 MiB 显存, 12% 利用率 |
| 线程 | 211 个活跃线程 |
| RSS | ~9.5 GB |

**进度：尚未完成第一个 task 的前 5 个 rollout**

日志自启动（07:36:37, 约 19 小时前）后无新输出。代码中进度 print 每 5 个 rollout 触发一次（`if (r+1) % 5 == 0`），说明连第一个 task 的 5 个 rollout 都没跑完。

**原因分析：正常但极慢**

- 模式 `vla_only`，每步做 K=10 次 SmolVLA 推理
- 总量：10 tasks × 10 rollouts × 300 steps × 10 inferences = 300,000 次推理
- 4090 上 SmolVLA-500M 每次推理含图像预处理约 0.5-1s，单个 rollout 预估 ~25-50 分钟
- 总时长预估 **40-80 小时**，当前 19 小时约完成 25-50%

进程没卡死（wchan=0, GPU 有利用率），只是单卡 VLA 推理 + MuJoCo 仿真本身就慢。

---
