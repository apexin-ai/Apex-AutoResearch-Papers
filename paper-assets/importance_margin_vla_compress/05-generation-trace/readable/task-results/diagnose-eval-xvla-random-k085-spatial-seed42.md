# diagnose eval xvla random k085 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_xvla_random_k085_spatial_seed42_20260521T051503_result.json`
- **Structured JSON:** [`65e7659e8f98d24b7030.json`](../../sessions/65/65e7659e8f98d24b7030.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果
- **根因**: 误报（false positive）。实验已成功完成，监控系统因无 sentinel/W&B 心跳信号，5 次存活检测均未发现进程活动，自动判定为失败。
- **日志关键信息**: `Overall SR: 338/500 (67.6%)`, 95% Wilson CI: [63.4%, 71.6%], 耗时 94.9 min, 结果已保存至 `eval_results/xvla_prune_k0.85_libero_spatial.json`
- **各 Task 成绩**: T0=100%, T1=4%, T2=98%, T3=100%, T4=80%, T5=6%, T6=96%, T7=4%, T8=94%, T9=94%
- **建议**: 无需重试。需修复 eval 脚本的监控集成——添加 sentinel 文件输出或 W&B 日志，防止后续 eval 实验被误判为失败。

---
