# diag v4 taxei recovery eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_v4-taxei-recovery-eval_20260514T205957_result.json`
- **Structured JSON:** [`819e91716ac7383729f2.json`](../../sessions/81/819e91716ac7383729f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：误报，实验正常完成。** `v4-taxei-recovery-eval` 47/47 任务全部执行完毕，结果文件 `v4_taxei_recovery_eval.json`（482KB）完整写入，recovery rate 59.6%，detection rate 0.0%。

cron 误判原因：eval 任务运行时间短，进程正常退出后 PID 不存在，加上 `injected_eval.py` 未集成 W&B logging，导致"进程 dead + 无 W&B 指标"两个条件同时满足，被判定为 failed。

`v4-vanilla-recovery-eval` 也已正常完成（recovery rate 61.7%）。4 张 GPU 全部空闲。

诊断报告已写入 `artifacts/diag_v4_taxei_recovery_eval.md`。

---
