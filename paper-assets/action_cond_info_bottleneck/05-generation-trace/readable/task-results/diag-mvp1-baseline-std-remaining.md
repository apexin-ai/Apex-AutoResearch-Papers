# diag mvp1 baseline std remaining

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp1_baseline_std_remaining_20260515T233726_result.json`
- **Structured JSON:** [`07ad29936923bd2e0d71.json`](../../sessions/07/07ad29936923bd2e0d71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 判断：**KILLED**（进程被外部杀死）

### 时间线

| Suite | 开始时间 | 结束时间 | 状态 |
|-------|---------|---------|------|
| libero_spatial | 03:38 | 05:30 | **完成** |
| libero_object | 05:30 | 07:35 | **完成** |
| libero_goal | 07:35 | ~07:38 | **被杀，仅完成 task 0 的 3 个 episode** |
| libero_10 | — | — | **未开始** |

### 已完成 suites 的 Success Rate

| Suite | Avg SR | Episodes |
|-------|--------|----------|
| libero_spatial | **66.0%** | 500 |
| libero_object | **67.8%** | 500 |

### 依据

1. **日志无任何 error/exception/traceback/OOM** — grep 在 30MB 日志中没找到任何错误信息
2. **日志末尾是进度条**（step 229/300, libero_goal task 0），突然中断，无正常退出日志
3. **libero_goal 目录**只有 `videos/libero_goal_0/` 下 3 个 mp4 文件，无 eval_info.json
4. **libero_10 目录不存在**
5. 进程在 libero_goal 启动约 2-3 分钟后被杀，行为与外部 SIGKILL 一致（Python 无法捕获，所以日志中无记录）

### 需要重做

- **libero_goal**（全部 10 tasks）
- **libero_10**（全部 10 tasks）

---
