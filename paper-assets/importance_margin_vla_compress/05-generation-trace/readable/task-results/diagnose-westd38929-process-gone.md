# diagnose westd38929 process gone

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd38929_process_gone_20260525T165936_result.json`
- **Structured JSON:** [`0ab8cd1734e7fdbf65ae.json`](../../sessions/0a/0ab8cd1734e7fdbf65ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新。汇总：

| exp_id | conclusion | 进度 | 部分结果 | 失败原因 |
|--------|-----------|------|---------|---------|
| eval_openvla_attn_k07_long_seed42 | **failed** | Task 3/10 Ep20 截断 | T1=38.0%, T2=24.0% | 进程静默终止，无错误日志 |
| eval_openvla_l2norm_k07_long_seed42 | **failed** | Task 3/10 Ep20 截断 | T1=42.0%, T2=34.0% | 进程静默终止，无错误日志 |
| eval_openvla_random_k07_long_seed42 | **failed** | Task 3/10 Ep40 截断 | T1=48.0%, T2=46.0% | 进程静默终止，无错误日志 |
| eval_openvla_l2norm_k085_long_seed42 | **failed** | Task 3/10 Ep40 截断 | T1=62.0%, T2=48.0% | 进程静默终止，无错误日志 |

4 个实验全部失败。日志均只有 40-42 行，在 Task 3 中途被截断，无 Traceback/OOM/Error 信息。4 个进程同时在 Task 3 附近死亡，高度怀疑是 4 GPU 同时运行导致系统内存不足被 OOM killer 杀掉，或实例被关机。重跑时建议减少并行数（如 2 个一组）或监控系统内存。

---
