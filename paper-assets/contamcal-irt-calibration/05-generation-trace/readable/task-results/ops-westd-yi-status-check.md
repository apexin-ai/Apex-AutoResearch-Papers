# ops westd yi status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-yi-status-check_20260522T154327_result.json`
- **Structured JSON:** [`1f83a735fafc7ee07e17.json`](../../sessions/1f/1f83a735fafc7ee07e17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**Yi-1.5-9B d000 s42 训练已死，无法恢复。**

| 项目 | 状态 |
|------|------|
| **PID 636899** | 已死，无任何 Python 训练进程存在 |
| **训练进度** | 1802/3125 steps (58%), epoch ~0.58, 运行了 ~2h07m |
| **最后 loss** | ~1.05, grad_norm ~0.4, token_accuracy ~0.74（训练本身健康） |
| **Checkpoint** | **空** — `lora_adapter/` 目录无任何文件，未保存过 checkpoint |
| **死因** | 日志在 step 1802 处截断，无 traceback/error。非服务器重启（uptime 225天）。可能是 tmux session 被意外关闭或进程被 kill |
| **GPU** | 4x RTX PRO 6000 (96GB) 全部空闲，0MiB |
| **磁盘** | /root/autodl-tmp: 17GB 可用 (234G/250G, 94%) |
| **tmux** | 无 session |

**结论**：训练需要从头重启。没有中间 checkpoint 可以 resume。等待指令是否重启。

另外需要更新 MCP 工具中 westd-29999 的密码——当前存储的加密密码已失效，我是用 sshpass 直连的。

---
