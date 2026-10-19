# 诊断报告：westd-28034 上 3+1 个 eval 实验 SIGHUP 失败

**诊断时间**: 2026-05-21 07:25 UTC  
**服务器**: westd-28034 (4× RTX 5090 32GB, 754GB RAM, UTC+8)

## 根因：tmux 服务器崩溃

旧 tmux 服务器在 ~07:19 UTC 崩溃/死亡，导致所有挂载的 tmux session 收到 SIGHUP 信号。

**排除项**:
- ❌ 服务器重启 — uptime 7天23小时，无重启记录
- ❌ OOM Kill — 754GB RAM 仅用 22GB，dmesg 无 OOM 记录
- ❌ GPU 故障 — nvidia-smi 正常，4 GPU 全部在线
- ❌ SSH 断连 — tmux 设计上可以存活 SSH 断连，且所有 session 同时死亡

**证据**:
1. exit file: `129|2026-05-21T07:19:24Z` (SIGHUP at 07:19:24 UTC)
2. 旧 tmux socket 已不存在，新 socket born at 07:22:03 UTC
3. 所有实验在同一时刻被杀，无 error traceback，无 OOM，指向进程外部原因
4. Docker 容器环境无 systemd journal/syslog，无法追溯 tmux 进程死亡的精确触发器

**可能的 tmux 崩溃触发器**（无法确认，缺乏系统日志）:
- 平台级进程管理/清理
- tmux 服务器进程 bug
- 容器 cgroup 限制

## 时间线 (UTC)

| 时间 | 事件 |
|------|------|
| ~04:45 | 4 个 eval 实验在 tmux sessions 中启动 |
| 07:19:24 | tmux server 崩溃 → SIGHUP → 全部 EXIT_CODE=129 |
| 07:19:43 | ckpt5000-v2 由自动恢复系统通过 nohup 重启 (PID 497834, GPU 0) |
| 07:21-07:22 | Registry 轮询检测到失败，on_failed hooks 触发 |
| 07:22:03 | 新 tmux server 创建，ckpt6000/6500/7000 重启 |
| 07:26 | Registry 更新为 RUNNING 状态 |

## 各实验状态

| 实验 | 原 PID | 新 PID | GPU | 后端 | 当前状态 |
|------|--------|--------|-----|------|----------|
| exp-003-eval-ckpt5000-v2 | 495837 | 497834 | cuda:0 | nohup → /tmp/eval_ckpt5000v2.log | ✅ RUNNING (20/362 as of 07:24) |
| exp-003-eval-ckpt6000 | - | 498446 | cuda:1 | tmux | ✅ RUNNING |
| exp-003-eval-ckpt6500 | - | 498584 | cuda:2 | tmux | ✅ RUNNING |
| exp-003-eval-ckpt7000 | - | 498666 | cuda:3 | tmux | ✅ RUNNING |

**日志关键信息**: 所有实验在被杀前已完成模型加载（Qwen3-8B + LoRA + NLI）并开始 eval 推理（362 pairs），无 error traceback，纯粹是 SIGHUP 外部中断。

## GPU 状态

```
GPU 0: RTX 5090  16854MiB/32607MiB  48% util  (ckpt5000-v2)
GPU 1: RTX 5090  16844MiB/32607MiB  48% util  (ckpt6000)
GPU 2: RTX 5090  16844MiB/32607MiB  48% util  (ckpt6500)
GPU 3: RTX 5090  16844MiB/32607MiB  50% util  (ckpt7000)
```

全部 GPU 正在使用，内存占用 ~16.8GB/32.6GB，利用率 48-50%。

## 结论

1. **无需人工干预** — 自动恢复系统（kill-cleanup-restart worker）已在 3 分钟内完成全部重启
2. **Registry 已更新** — 4 个实验均为 RUNNING 状态，retry_count 已递增
3. **数据完整性** — 旧 run 未产生结果文件（results 目录无对应 JSON），重启从头开始，无脏数据风险
4. **根因不可完全追溯** — Docker 容器缺乏系统日志，tmux 崩溃的精确原因无法确认。如果频繁复现，建议考虑使用 nohup 或 screen 替代 tmux 作为后端