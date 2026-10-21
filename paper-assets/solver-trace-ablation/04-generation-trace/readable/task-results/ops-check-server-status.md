# ops check server status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-server-status_20260513T230158_result.json`
- **Structured JSON:** [`9ac3f957bb6b3feaa96a.json`](../../sessions/9a/9ac3f957bb6b3feaa96a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### PID 存活状态

| 实验 ID | PID | 状态 | 退出码 | 说明 |
|---------|-----|------|--------|------|
| plan001-exec-only-s42 | 83029 | **DEAD** | 2 | 22:20:57Z 即退出 |
| plan001-exec-only-s42-r2 | 84896 | **ALIVE** | — | 训练中 |
| plan001-exec-only-s42-r3 | 85710 | **DEAD** | 1 | 22:42:59Z 即退出 |
| plan005-sta-low-s42 | 85790 | **ALIVE** | — | 训练中 |
| plan003-eval-exec-only-r5 | 83690 | **DEAD** | 0 | 正常完成，输出 177KB |

### 训练进度

| 实验 | 当前步数 | 进度 | 速度 | tqdm 预估剩余 |
|------|---------|------|------|--------------|
| plan001-exec-only-s42-r2 | 158/500 | 31.6% | ~7.5s/step | ~43 min |
| plan005-sta-low-s42 | 149/500 | 29.8% | ~8.1s/step | ~47 min |

最新 reward：
- **r2** (exec_only): step 158 reward=0.375, prove_rate=0.375
- **sta-low**: step 149 reward=0.000, prove_rate=0.000（波动大，step 147 曾达 0.834）

### GPU 使用

| GPU | 显存 | 利用率 | 占用者 |
|-----|------|--------|--------|
| cuda:0 | 80323/97887 MiB (82%) | 91% | plan001-exec-only-s42-r2 |
| cuda:1 | 80355/97887 MiB (82%) | 91% | plan005-sta-low-s42 |

### 已完成实验

- **plan003-eval-exec-only-r5**: 输出存在于 `/root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json` (177KB)

### 死进程（可清理）

- PID 83029 (plan001-exec-only-s42) — exit code 2，启动即失败
- PID 85710 (plan001-exec-only-s42-r3) — exit code 1，启动即失败

这两个无需清理（进程已不存在），但日志值得检查以了解失败原因。两个存活的训练预计约 45 分钟后完成。

---
