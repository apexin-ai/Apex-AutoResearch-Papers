# eval home cuda0 v5 sweep or next

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_home-cuda0-v5-sweep-or-next_20260514T223415_result.json`
- **Structured JSON:** [`61fffa7a433cb4ab6d6a.json`](../../sessions/61/61fffa7a433cb4ab6d6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**当前状态：cuda:0 忙碌，无需提交新任务。**

- **GPU**: cuda:0 利用率 100%，显存 31727/32607 MiB
- **当前任务**: v5 ckpt-600 val@5120 eval 正在运行（进程可见于 ps 输出）
- **Sweep 脚本**: `run_v5_val5120_sweep.sh`（PID 3180425）已在后台运行，正在等待 ckpt-600 完成
- **Sweep 队列**: ckpt-600 完成后，脚本会自动依次跑 **ckpt-4000 → 4200 → 4400 → 4600**（val@5120），与任务要求的优先级完全一致
- **已完成**: ckpt-600 的 predictions.jsonl 已生成，但 eval_repo_cls.json 尚未写出（仍在推理中）
- **ckpt-4000~4600**: 均未开始

之前的 Worker 已经部署了 sweep 脚本覆盖了所有需要的 eval，不需要额外提交。等 ckpt-600 跑完后会自动继续。

---
