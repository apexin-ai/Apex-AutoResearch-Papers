# submit eval ess only and submit tau06

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval_ess_only_and_submit_tau06_20260516T032123_result.json`
- **Structured JSON:** [`f94b8190b714dd4b7eb0.json`](../../sessions/f9/f94b8190b714dd4b7eb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**汇总：**

| 任务 | 结果 |
|------|------|
| **ess_only eval** | PPL = **17.77**, loss = 2.8775, tokens = 4,077,068 |
| **ess_only registry** | → DONE (success), metrics/checkpoint/conclusion 已更新 |
| **cuda:2 状态** | 已被 tau06 训练占用 (PID 287971, 46.5 GB) |
| **tau06 训练** | RUNNING on cuda:2, nohup 后台执行 |
| **tau06 registry** | → RUNNING, spec 完整 |

**ρ=0.6 对比（eval_ppl_holdout）：**
- grid_b0.5: **17.704** (最优)
- adaptive: **17.74**
- uniform: **17.766**
- ess_only: **17.77** (最差)

ESS-only 在 ρ=0.6 下表现最差，支持 dual-constraint 优于单一约束的结论。

---
