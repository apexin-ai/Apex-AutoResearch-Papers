# diagnose eval pi05 random k085 object seed43 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k085_object_seed43_postfix_20260525T002240_result.json`
- **Structured JSON:** [`ce48db905e6f0b083a3c.json`](../../sessions/ce/ce48db905e6f0b083a3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成：

- **状态**：实验已正常完成（全部 500 episodes 跑完），进程正常退出
- **overall_sr = 4.8%**（24/500）
- 结果文件：`/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.85_libero_object_seed43.json`
- 日志最后一行确认 `RESULT: libero_object prune=random keep=0.85 SR=4.8%`
- cron 报 "Process gone, no sentinel" 是因为 exit sentinel 文件不存在（`/tmp/agent-ml-exit/` 下无该文件），但实验实际已成功完成

Registry 已更新：status=DONE, conclusion=success, metrics={overall_sr: 0.048}。

---
