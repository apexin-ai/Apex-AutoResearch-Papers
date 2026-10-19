# diag eval obs only object norm003 seed43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-obs-only-object-norm003-seed43-r2_20260519T044643_result.json`
- **Structured JSON:** [`aefd60e9e7d60f35a780.json`](../../sessions/ae/aefd60e9e7d60f35a780.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，汇总如下：

---

## 诊断结果

### 根因：SIGHUP (EXIT_CODE=129) + r2 启动失败

**r1（wrapper 版本）的死因：**
- exit file 明确记录 `129|2026-05-18T20:38:00Z`（SIGHUP）
- 运行到 task 5/10（ketchup）rollout 6/10 时被杀，无 Python traceback
- 日志最后一行：
  ```
  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 6/10, success so far: 0/6
  EXIT_CODE=129
  ```

**r2 从未成功启动：**
- PID 900678 在 04:42 创建了 tmux session，但 Python 进程从未产生输出（project log 时间戳仍是 May 17 原始运行）
- 无 r2 exit file，无 r2 runs/ log
- tmux session 已不在 `tmux list-sessions` 中，但 tmux server 进程仍作为孤儿存活
- 可能原因：r2 用了旧格式命令（无 wrapper），tmux session name 可能与残留的旧 session 冲突，或 GPU 1 被其他进程占用导致立即失败

### 排除因素
- **非 OOM**：系统内存 1TiB，可用 918GiB；GPU 显存每进程约 5GB，4090 有 24GB
- **非磁盘满**：/ 53%，/root/autodl-tmp 61%
- **非服务器重启**：uptime 6天
- **非 Python 错误**：无 traceback，是外部信号杀进程

### 对同服务器其他实验的影响
当前 5 个 tmux session 正常运行（norm02-k5-seed46/47、argmin-k5-seed43、lto-splitA-heldout/vla-only），GPU 负载正常。SIGHUP 问题似乎是间歇性的，不影响当前运行的实验。

### 修复建议
1. **重新提交 seed43**，使用 wrapper 格式命令，选择空闲 GPU（当前 GPU 0/1/3 负载较低）
2. 在命令中加 `nohup` 或确保 tmux session 使用 `set -g remain-on-exit on`，防止 SIGHUP 传播
3. 先清理孤儿进程 PID 900678：`kill 900678`
4. 同服务器 seed45-r2 很可能同样原因失败，需一并重跑

---
