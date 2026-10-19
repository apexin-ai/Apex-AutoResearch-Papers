# diagnose mvp1 baseline plus remaining

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp1_baseline_plus_remaining_20260515T232541_result.json`
- **Structured JSON:** [`7013c9a4a32f071957bf.json`](../../sessions/70/7013c9a4a32f071957bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断报告

### 失败原因：**Cron 误报，进程实际仍在运行**

- PID 471056 正在 GPU 0 上执行 `libero_goal` eval（占用 5.8GB 显存）
- 日志中 **零错误、零异常、零 OOM**（grep 结果为空）
- dmesg 无权限读取（容器环境），但 GPU 状态正常（38°C, 0% util idle between rollouts）
- Cron 的"进程死亡 5 次"是误报——可能监控的是 bash 父脚本 PID 而非实际 `lerobot-eval` 子进程

### 已完成 Suite 结果

| Suite | Avg Success Rate | 状态 |
|-------|-----------------|------|
| **libero_spatial** | **81.6%** | ✅ 完成 (10/10 tasks) |
| **libero_object** | **88.8%** | ✅ 完成 (10/10 tasks) |

libero_spatial 逐 task：98%, 82%, 92%, 94%, 74%, 32%, 94%, 86%, 80%, 84%
libero_object 逐 task：78%, 92%, 92%, 88%, 92%, 78%, 100%, 80%, 100%, 88%

### 进行中 / 未完成

| Suite | 状态 | 进度 |
|-------|------|------|
| **libero_goal** | 🔄 运行中 | task_0 完成, task_1 进行中 (2/50 episodes) |
| **libero_10** | ⏳ 未开始 | 排在 libero_goal 之后 |

### 时间线

- libero_spatial: 03:38→05:21 (~1h43m)
- libero_object: 05:21→07:14 (~1h53m)
- libero_goal: 07:14 起，目前 ~12 分钟，预计还需 ~1.5-2h
- libero_10: 预计再 ~2h
- **全部完成预估: ~11:00-11:30 (服务器时间)**

### 建议

1. **不需要重跑**。进程仍在正常运行，让它跑完即可
2. **修复 cron 监控逻辑**——当前监控的 PID 可能是 bash 脚本的 PID 而非 `lerobot-eval` 子进程。脚本用 `set -e` + for 循环执行，bash 进程和 lerobot-eval 子进程 PID 不同
3. 将实验状态从 `failed` 改回 `running`

---
