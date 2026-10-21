# diag repo level cwm v10

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_repo-level-cwm-v10_20260513T063451_result.json`
- **Structured JSON:** [`6d2033b2b2d61821dc41.json`](../../sessions/6d/6d2033b2b2d61821dc41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，报告已写入 `artifacts/diag_cwm_v10.md`。

**结论**：

- **根因**：进程在 eval 阶段（1281/9335 eval samples）被杀，exit code 1，但日志无任何 traceback——异常输出因缓冲丢失。排除 OOM（cgroup oom_kill=0）、磁盘满（数据盘 43%）、内核 OOM killer（dmesg 空）
- **训练本身已无意义**：step 400 后严重过拟合，eval_loss 从 0.298 一路涨到 0.370，train_loss 降到 0.09
- **3 个 checkpoint 存活**：400（BEST）、1600、1700，全部完整
- **checkpoint-400 正在被评估**：GPU 2 上两个 eval 进程运行中，accuracy ~70.6%（720/9784）
- **不需要重启训练**，等 eval 完成即可

---
