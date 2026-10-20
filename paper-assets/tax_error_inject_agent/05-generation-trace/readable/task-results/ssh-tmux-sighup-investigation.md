# ssh tmux sighup investigation

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_tmux-sighup-investigation_20260514T133107_result.json`
- **Structured JSON:** [`afb77e7283467cdf76b6.json`](../../sessions/af/afb77e7283467cdf76b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**找到根因了。**

Worker 日志第 8 行清楚记录了：`worker_ssh_v4-tmux-cleanup-resubmit` 在 13:28:08 UTC 执行了：

```
tmux kill-session -t v4-taxei-sft 2>/dev/null; tmux kill-session -t v4-random-sft 2>/dev/null
```

## 根因分析报告

### 直接原因

框架派发的 Worker `worker_ssh_v4-tmux-cleanup-resubmit`（启动于 2026-05-14T13:27:53Z）**主动执行了 `tmux kill-session`**，杀死了 v4-taxei-sft 和 v4-random-sft 两个 tmux session。

`tmux kill-session` 向 session 内所有进程发送 SIGHUP。启动脚本的 trap (`trap 'exit 129' HUP`) 捕获信号后以 exit code 129 退出，触发 EXIT trap 写入 `EXIT_CODE=129` 到日志。训练进程的 `Pin memory thread exited unexpectedly` 是 dataloader worker 线程被 SIGHUP 杀死的二级效应。

### 时间线 (UTC)

| 时间 | 事件 |
|------|------|
| ~13:26 | 原始 v4-taxei-sft / v4-random-sft 提交并开始训练 |
| 13:27:53 | Worker `v4-tmux-cleanup-resubmit` 被调度 |
| 13:28:08 | 执行 `tmux kill-session -t v4-taxei-sft; tmux kill-session -t v4-random-sft` |
| 13:28:12 | 确认 session 已清除 |
| 13:28:23 | 用同名 exp_id 重新提交 v4-taxei-sft |
| 13:28:26 | 重新提交 v4-random-sft |
| 13:28:48 | 旧进程 EXIT trap 写入 EXIT_CODE=129 到日志 |
| 13:30:52 | v4-taxei-sft-r2 提交（第三次尝试，改了名） |
| 13:30:54 | v4-random-sft-r2 提交 |

### 不是以下原因

- 不是 AutoDL 平台重启（uptime 174 天，v3-eval sessions 存活）
- 不是 crontab/cleanup 脚本（服务器上无 crontab）
- 不是框架 `_check_stale_workers`（那个用 SIGTERM 且只杀本地进程）
- 不是 OOM 或 GPU 错误

### 当前状态

- v4-taxei-sft-r2：运行中，cuda:2，94% util，step 67+，~1.96s/it
- v4-random-sft-r2：运行中，cuda:3，96% util
- v3-taxei-eval：运行中，cuda:0
- v3-random-eval：运行中，cuda:1
- 4 张 RTX 5090 全部在用

### 防止再次发生的建议

1. **Worker 在执行 `tmux kill-session` 前必须验证进程状态** — 先 `ps -p &lt;PID>` 确认进程是否健康、检查日志是否有错误，再决定是否 kill。ml-experiment-guide.skill.md 已有此规则但本次未被遵守。

2. **`submit_training_job` 应检测同名 tmux session 是否已存在** — 如果存在且进程健康，应拒绝提交而非静默覆盖。当前 `tmux new-session -d -s` 对已有 session 会直接报错，但 Worker 在 submit 前手动 kill 了 session，绕过了这个保护。

3. **考虑在 `tmux_backend.py` 的 kill 方法中先发 SIGTERM 等待优雅退出**，而非直接 `tmux kill-session`（后者发 SIGHUP）。当前代码对 numeric PID 会先 SIGTERM，但对 tmux session name 跳过了 SIGTERM 直接 kill-session。

---
