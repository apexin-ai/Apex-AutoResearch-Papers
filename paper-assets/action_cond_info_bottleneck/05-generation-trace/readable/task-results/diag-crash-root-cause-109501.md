# diag crash root cause 109501

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_crash_root_cause_109501_20260515T213129_result.json`
- **Structured JSON:** [`11ff7bf430669939b887.json`](../../sessions/11/11ff7bf430669939b887.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结论

**崩溃原因：非 OOM，大概率是外部 SIGKILL 或进程前台绑定的 SSH 会话断开**

### 排除 OOM 的证据

| 检查项 | 结果 |
|--------|------|
| 日志 memory/VRAM/allocat 告警 | **无**（grep 零匹配） |
| GPU 内存使用 | 当前 ~6GB / 96GB per GPU（仅 6%） |
| 内核 OOM 日志 | 不可查（容器环境，无 kern.log/syslog/dmesg） |
| 磁盘 | 30GB 根分区用了 21GB，剩 9.4GB，未满 |

### 日志实际停止位置

进程比预想走得更远——并非 "task 1 step ~59/280"：
- libero_spatial 全部完成
- libero_object task 0 完成（50 episodes，10 个视频已保存）
- libero_object task 1 的 eval batch **5/50**，rollout 刚启动 step 0/280
- 最后写入时间 **05:33:18**，无 Traceback、无 Error，进度条截断

这种 **日志无任何错误就戛然而止** 的模式指向 SIGKILL（进程无机会写日志），而非异常退出。

### 最可能的原因

1. **SSH 会话断连导致前台进程被杀** — 如果进程直接在 SSH 终端前台运行（非 nohup/tmux/screen），SSH 断连会发送 SIGHUP→SIGKILL
2. **容器编排系统强杀** — overlay 文件系统说明这是容器，平台可能有 cgroup 内存或时间限制
3. **手动 kill** — 其他操作者或脚本发了 kill 信号

### 当前新进程状态

| PID | 用途 | GPU 内存 | 风险 |
|-----|------|---------|------|
| 294229 | 新 eval（libero_object, cuda:0） | 5959 MiB / 96GB | **极低** |
| 308788 | baseline_std_v3 libero_object（cuda:1） | 5959 MiB / 96GB | **极低** |

两个进程各占 ~6GB，96GB 显卡完全够用，**不会 OOM**。

### 建议

确认新进程 294229 是否用 `nohup` 或 `tmux`/`screen` 启动。如果是裸 SSH 前台运行，需要改成 `nohup ... &` 或在 tmux 中运行，否则 SSH 断连会再次杀死进程。

---
