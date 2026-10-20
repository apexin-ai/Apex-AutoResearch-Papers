# run analysis tau sweep

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_analysis_tau_sweep_20260512T161805_result.json`
- **Structured JSON:** [`f90d247ff8452332451a.json`](../../sessions/f9/f90d247ff8452332451a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验稳定运行。Random eval 5% (330/6554)，速度 3.74 it/s。

**当前状态汇总：**
- 实验 PID=40057 运行正常
- Full baseline: ✅ 完成 (~9 min)
- Random eval: 5% (330/6554), 3.74 it/s, ~27 min remaining
- 之后还有: recency (~30 min) + 8 个 EMA gammas (~35-50 min each)
- **预计总完成时间: 5-7 小时（从启动算起）**

结果 JSON 会在第一个 EMA gamma 完成后开始增量写入到 `/root/carc/analysis_gamma_sweep_results.json`。

实验将自行完成。需要我继续定期轮询进度，还是你后续手动检查？

---
