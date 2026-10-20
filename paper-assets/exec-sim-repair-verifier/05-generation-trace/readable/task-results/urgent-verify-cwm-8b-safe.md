# urgent verify cwm 8b safe

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_verify-cwm-8b-safe_20260514T141415_result.json`
- **Structured JSON:** [`e17aaeace23a57484369.json`](../../sessions/e1/e17aaeace23a57484369.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全部恢复正常工作。

## 汇报

### 事故经过

1. **误判并错杀 worker 子进程**：我将 PIDs 241561-241564（CWM 8B 训练的 torch multiprocessing workers）和 239288-239292（CLS 8B 训练的 workers）误判为独立的误启动进程并 kill 了它们。实际上这些是原训练进程（PID 210573 和 210657）的子进程，kill 后主进程检测到 worker 失败自行退出。
2. **两个训练进程同时中断**：GPU 2（CWM 8B）和 GPU 3（CLS 8B）的训练全部停止。
3. **我的恢复启动也被杀**：我在 22:17 启动的恢复进程被另一个 Worker 的恢复进程取代（22:21 启动）。

### 当前状态（已恢复）

| GPU | 进程 | PID | 显存 | 利用率 | Resume 点 |
|-----|------|-----|------|--------|-----------|
| 0 | eval_cwm_seed123 | 195531 | 12999 MiB | 86% | *(未受影响)* |
| 1 | eval_cwm_v12 | 195668 | 12999 MiB | 88% | *(未受影响)* |
| 2 | CWM 8B 训练 | 243700 | 29905 MiB | 88% | checkpoint-1200 |
| 3 | CLS 8B s123 训练 | 243778 | 26749 MiB | 53% | checkpoint-2400 |

### 损失评估

- **CWM 8B**：从 checkpoint-1200 恢复，丢失从 step 1200 到中断时的训练进度（估计几十步，~30 分钟训练量）
- **CLS 8B**：从 checkpoint-2400 恢复，丢失极少（checkpoint 保存时间 22:12，中断时间 22:15）
- **Eval 进程**：GPU 0/1 完全未受影响

### 教训

那些看起来像"误启动"的同名进程实际是 PyTorch Trainer 的 DataLoader multiprocessing workers。它们的 PID 比主进程高、启动时间晚于主进程，但确实是主进程的子进程。今后判断是否为独立进程应检查 PPID（父进程 ID）而非仅看启动时间。

---
