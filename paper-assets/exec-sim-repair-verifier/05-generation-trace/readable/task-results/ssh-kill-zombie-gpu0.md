# ssh kill zombie gpu0

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-zombie-gpu0_20260519T221507_result.json`
- **Structured JSON:** [`cc14f1d8626336ee29a7.json`](../../sessions/cc/cc14f1d8626336ee29a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dmesg 无 OOM 记录。综合分析如下：

---

## 结果

### 1. GPU 0 状态
**✅ 已释放** — 0MiB / 0% 利用率。可用。

### 2. CWM s123 死因分析

**训练时间线**:
| 时间 (CST) | 事件 |
|---|---|
| 05-19 20:52 | tmux session `qwen3-8b-cwm-s123` 创建 |
| 05-20 03:46 | 首条日志输出（**7h 空白期**） |
| 05-20 03:52 | 训练开始（step 0/6633） |
| 05-20 06:15 | 进程死亡，日志停止写入 |

**训练进度**（存活了 ~2.4h）:
- 到达 step 300/6633（4.5%, epoch 0.14）
- eval_loss: 0.443 → 0.310 → **0.287**（持续下降，模型在学）
- train loss: 24.48 → 5.90（正常收敛）
- 保存了 3 个 checkpoint: `/root/autodl-tmp/checkpoints_repo_cwm_8b_s123/checkpoint-{100,200,300}`
- 死于第 4 次 validation 循环中（val step 2117/9335）

**死因判定**:
- 日志中 **无任何 error/traceback/OOM/CUDA error**
- dmesg **无 kernel OOM kill 记录**
- 启动命令中 **无 `timeout` wrapper**
- **结论：进程被外部信号静默杀死**

EXIT_CODE=124 通常是 GNU `timeout` 返回码，但启动命令中没有 `timeout`。最可能的原因：
1. **SeetaCloud 平台层面的资源/时间限制**（平台强制 kill 超时会话）
2. **另一个 worker/agent 误杀了 tmux session**
3. 7h 空白期（20:52→03:46）暗示 GPU 3 可能在排队等待释放，平台超时从 session 创建时算起而非从训练开始

**建议操作**：在重新提交前，确认平台是否有 session 级别的 wall-time 限制（如果从 tmux 创建时起算 9.4h，可能触发了某个 24h 以外的限制）。

---
