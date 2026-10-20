# debug mvp 001c crash

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_mvp-001c-crash_20260511T235804_result.json`
- **Structured JSON:** [`89fd0f042959c0ee9fde.json`](../../sessions/89/89fd0f042959c0ee9fde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正在运行，模型已加载，正在 generate 第一道竞赛题（max_new_tokens=4096，预计需要几分钟）。日志会在 generate 完成后更新。

**诊断报告：**

| 项目 | 详情 |
|------|------|
| **崩溃原因** | screen session 被外部终止（非 OOM、非代码 bug）。原始日志只重定向 stdout，stderr 丢失。Dry-run 验证脚本逻辑完全正常 |
| **修复内容** | 1) 用 tmux 替代 screen；2) 日志改为 `> log 2>&1` 捕获 stderr；3) 杀掉残留的旧 screen 进程（PID 9307）避免 GPU 冲突和日志文件写入竞争 |
| **新 PID** | **10401** |
| **tmux session** | `mvp-001c` 存活 |

注意：还发现一个意外的旧 screen session（PID 9300，07:55 启动）仍在跑 v3，已一并清理。两个 v3 进程同时写 `mvp_run_v3.log` 会互相覆盖。

---
