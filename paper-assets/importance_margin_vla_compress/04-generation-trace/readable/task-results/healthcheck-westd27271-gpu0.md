# healthcheck westd27271 gpu0

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_healthcheck-westd27271-gpu0_20260523T214715_result.json`
- **Structured JSON:** [`53d85c28fdd8f3e13df4.json`](../../sessions/53/53d85c28fdd8f3e13df4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 0: `eval_openvla_l2norm_k05_goal_seed42_v3`
- **状态: 正常运行中**
- 日志最后更新: 05:45（服务器时间），正在执行 Task 7/10 `put the cream cheese in the bowl`，已完成 Ep 10/50
- 进程 PID 380585 运行 2h42m，GPU 占用 15946 MiB，GPU util 72%
- 速度 ~2.0 eps/min，之前报告的 2.5h 无更新判断有误——日志在持续写入
- 已完成 tasks 1-6 的结果：SR = 0.28, 0.34, 0.66, 0.06, 0.66, 0.20

### GPU 1: `eval_openvla_baseline_long_seed42`
- **状态: 正常运行中**
- 正在执行 Task 8/10 `put both the alphabet soup and the cream cheese box in the basket`，已完成 Ep 40/50
- 进程 PID 291093 运行 6h08m，GPU util 84%
- 速度 ~1.1 eps/min，接近完成（剩余 Task 8 最后 10 eps + Task 9 + Task 10）

两个实验都正常推进，无 stall。

---
