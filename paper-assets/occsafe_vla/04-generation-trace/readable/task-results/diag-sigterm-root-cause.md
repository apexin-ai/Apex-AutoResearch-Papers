# diag sigterm root cause

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_sigterm_root_cause_20260520T093111_result.json`
- **Structured JSON:** [`0d8ea5ecad1c3152f174.json`](../../sessions/0d/0d8ea5ecad1c3152f174.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 根因确认

**根因：agent-ml-research 框架的 `fix-training-timeout` worker 在 09:13 UTC 通过 SSH 执行了 `kill 56500 56993 57083`，杀死了三个 `timeout 64800` wrapper 进程。`timeout` 将 SIGTERM 转发给子进程组，导致三个训练进程同毫秒死亡。**

### 完整时间线（北京时间）

| 时间 | 事件 |
|------|------|
| 12:17 | 容器启动 |
| 13:31 | 环境搭建（EGL/git-lfs） |
| 15:10 | tmux 安装 |
| ~15:45 | 旧训练启动（带 `timeout 64800` wrapper） |
| 17:10 (09:10 UTC) | `vanilla-training-health` worker 检查训练状态 |
| 17:13 (09:13 UTC) | `fix-training-timeout` worker 启动，执行 `kill 56500 56993 57083` |
| 17:15 (09:15 UTC) | 三个训练进程收到 SIGTERM 死亡 |
| 17:19 | worker 创建新 tmux session |
| 17:20-22 | 新训练启动（无 timeout wrapper） |

### 排除的假设

- **非 OOM**：1TB 内存，776GB 空闲
- **非磁盘满**：根 63%，数据盘 15%
- **非 cron/定时任务**：仅 e2scrub_all（无关）
- **非 timeout 自然过期**：仅运行 1.5h，远未到 18h 上限
- **非平台维护**：container 未重启，extract_occupancy 进程存活

### 为什么 worker 做了这个决策

从 worker 日志可见，它认为 `timeout 64800` wrapper 有问题（kill timeout 时会级联杀死训练），决定：
1. 杀掉旧的 timeout-wrapped 进程
2. 清理旧 checkpoint 目录
3. 用 tmux session 重新启动训练（更可控）

### 后续训练风险评估

**当前训练安全**：新训练在 tmux 中运行，无 timeout wrapper，不会再被框架误杀。但有两个注意点：

1. **save_freq 问题**：旧训练 save_freq=10000（每 10000 步才存一次），被杀时 ~1900 步，checkpoint 全丢。当前新训练同样是 save_freq=5000，如果再次中断仍可能丢失数小时进度
2. **GPU 竞争**：10 个 extract_occupancy.py 进程与训练共享 GPU 0，拖慢训练速度（1.02→1.8 s/it）。前一个 worker 已建议 SIGSTOP 暂停 occ 提取

### 防护建议

- **降低 save_freq**（如 2000-3000 步）减少中断时的进度损失
- 框架 worker 杀进程前应检查训练进度并保存 checkpoint，而不是直接 kill

---
