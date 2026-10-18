# gpu gemma2 rerun v2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_gemma2_rerun_v2_20260514T162542_result.json`
- **Structured JSON:** [`af956f746aa024c2f7d3.json`](../../sessions/af/af956f746aa024c2f7d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 运行正常：

1. **修复验证** — L181, L270 两处 `.float().view` 已到位
2. **GPU 占用** — GPU 0 python 进程 7496MiB
3. **Baseline PPL = 9.3785** — 正常范围（不是之前 bug 时的 711）
4. **Profiling 已开始** — L0H0 @2bit delta=0.001494, @4bit delta=-0.000607，非零 delta 确认修复生效

日志路径: `/root/runs/ratekv/gemma2_9b_rerun_v2.log`，tmux session: `gemma2_9b_full_pipeline`。1008 个 head 需要跑一段时间。

---
