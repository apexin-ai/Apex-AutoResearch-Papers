# code plan 017 multi seed

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_017_multi_seed_20260514T073854_result.json`
- **Structured JSON:** [`4e60d30c1f6cfa2c3a4a.json`](../../sessions/4e/4e60d30c1f6cfa2c3a4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正在正常运行。当前状态：

**已完成：**
- Baseline PPL (no quant): **9.8106**
- Uniform 4-bit PPL: **15.4454**

**正在进行：**
- Seed 0 profiling: **20/336** evals（每 20 步打印一次，~12s/eval）
- Seed 0 profiling 预计剩 ~63 分钟

**预估时间线：**
- 每个 seed：profiling ~67min + solver + eval ~10min ≈ 77min
- 3 个 seed 串行 ≈ 3.5-4 小时（含已完成的 baseline eval）

**注意事项：**
- 进程 PID 199409 在 GPU 0 运行，但不在 tmux 里（直接用 `>` 重定向到 multi_seed.log）
- 如果需要安全起见，可以考虑进程是否会因 parent 退出而终止
- Registry 已更新为 RUNNING
- checkpoint 文件会在每个 seed 完成时保存到 `multi_seed_checkpoint_s{seed}.json`

---
