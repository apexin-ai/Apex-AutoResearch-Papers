# ops verify running experiments

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-running-experiments_20260516T190236_result.json`
- **Structured JSON:** [`0cce01cc4af06855e6e6.json`](../../sessions/0c/0cce01cc4af06855e6e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/gpu_status_loop18.md`。

关键发现：
- **4 个 GPU 实验存活**：d005 eval (cuda:0, 55%), d000 mmlu signals (cuda:1), d025 eval (cuda:3, 37%), d100 eval (cuda:5)
- **1 个 CPU 实验存活**：exp_006 domain gamma v3，正在跑 stansummary (MCMC汇总)
- **2 个已死**：gsm8k signals (PID 835978) 和 15B instruct mmlu (PID 810809)
- **arc signals 已完成**：所有输出文件已生成，进程正常退出
- **gsm8k signals 实际已完成**：虽然注册的 PID 835978 死了，但非注册 PID 831936 在 cuda:4 完成了 gsm8k 全部信号计算（输出文件已存在）
- **15B instruct mmlu 从未启动**：无日志文件、无 exit file
- **GPU 2 空闲可用**，GPU 4 有残留进程可回收
- **需要清理**：kill 卡住的 PID 835593（HF 超时死循环）

---
