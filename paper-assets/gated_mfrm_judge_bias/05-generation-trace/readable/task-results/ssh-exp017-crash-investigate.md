# ssh exp017 crash investigate

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp017_crash_investigate_20260523T070536_result.json`
- **Structured JSON:** [`0e88482005dacc0ae2ac.json`](../../sessions/0e/0e88482005dacc0ae2ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

**进程仍在运行，未退出。**

| 项目 | 状态 |
|------|------|
| 进程 | PID 318082，`python run_exp017.py`，CPU 111%，内存 ~4GB，正在运行 |
| tmux | `exp-017` session 存在，创建于 15:04:02 |
| OOM | dmesg 无权限读取，但进程活着说明没被 kill |
| 错误 | 日志无任何 error/traceback/segfault |

**已完成进度：** 8/800 iterations（7 条结果已写入 CSV，当前正在跑 N=8 seed=7）。每个 iteration 约 63-70 秒（MCMC 4 chains × 6000 samples），日志输出被缓冲所以看起来"停了"，实际是 stdout 还没 flush。

**预估剩余时间：** ~793 iterations × ~65s ≈ **14.3 小时**。

**注意事项：** 日志中有 UserWarning——MCMC 4 chains 在单 GPU 上串行执行（非并行），这是速度慢的原因。如果想加速，可以在脚本开头加 `numpyro.set_host_device_count(4)` 让 CPU chains 并行，但当前进程不需要重启，它在正常跑。

---
