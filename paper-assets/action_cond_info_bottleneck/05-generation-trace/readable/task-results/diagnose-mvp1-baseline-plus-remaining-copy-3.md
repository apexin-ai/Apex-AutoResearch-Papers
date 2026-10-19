# diagnose mvp1 baseline plus remaining

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp1_baseline_plus_remaining_20260516T094137_result.json`
- **Structured JSON:** [`ecf3d484b1d9b10e40dd.json`](../../sessions/ec/ecf3d484b1d9b10e40dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验实际已成功完成，cron 标记 failed 是误报。**

### 状态汇总

| 项目 | 结果 |
|------|------|
| PID 675231 | 已退出（正常完成后自行退出） |
| libero_10 eval | **已完成** — `eval_info.json` 存在 |
| libero_10 SR | **67.2%**（500 episodes） |
| 日志尾部 | `2026-05-16 17:22:15 All suites completed.` |
| GPU 0 | 被 PID 866194 占用（16216 MiB, 99% util），非本实验 |

### 四个 suite 最终结果

| Suite | Success Rate |
|-------|-------------|
| libero_spatial | 81.6% |
| libero_object | 88.8% |
| libero_goal | 87.8% |
| libero_10 | 67.2% |

### 原因分析

父进程 PID 471056（shell 脚本）被外部信号杀死，但子进程 PID 675231（实际 eval python 进程）不受影响继续运行并正常完成。Cron 监控只检测父进程存活 + W&B 上报，两者都不满足，所以误判 failed。

### 结论

**不需要重跑。** 所有 4 个 suite 的 eval 结果完整。GPU 0 当前被另一个进程（PID 866194）占用。

---
