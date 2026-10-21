# analysis diagnose restart experiments

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diagnose_restart_experiments_20260519T131056_result.json`
- **Structured JSON:** [`b8b96f638eefd9c37694.json`](../../sessions/b8/b8b96f638eefd9c37694.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CPU 时间在两次读取之间显著增长（各 +5596 jiffies），确认两个进程正在活跃计算。

## 检查结果

### 1. qwen7b_full_trace_tail512_seed42 (PID 511626, cuda:0)

| 项目 | 状态 |
|------|------|
| **进程状态** | **运行中** — 287 线程，CPU 时间 ~17 min 且持续增长 |
| **已运行时间** | ~15 分钟（预期 ~53 min） |
| **预估进度** | ~step 126/444（未到第一个 checkpoint-148） |
| **checkpoint** | 无 — output_dir 只有 tfevents 文件（10.7KB） |
| **final/** | 不存在 |
| **eval** | 未运行（训练未完成） |
| **wandb** | 未找到 wandb 目录，可能未启用或写入 wandb 云端 |

### 2. codellama13b_ae_only_seed42 (PID 512034, cuda:1)

| 项目 | 状态 |
|------|------|
| **进程状态** | **运行中** — 287 线程，CPU 时间 ~16 min 且持续增长 |
| **已运行时间** | ~14 分钟 |
| **checkpoint** | 无 — output_dir 只有 tfevents 文件（6.4KB） |
| **final/** | 不存在 |
| **eval** | 未运行（训练未完成） |
| **wandb** | 同上 |

### 结论

两个实验都**仍在正常训练中**，cron 监控丢失不影响实际训练进程。标记 failed 是误报。训练尚未到第一个 checkpoint 保存点（step 148），预计 qwen7b 还需 ~38 分钟完成，之后需手动触发 eval。

---
