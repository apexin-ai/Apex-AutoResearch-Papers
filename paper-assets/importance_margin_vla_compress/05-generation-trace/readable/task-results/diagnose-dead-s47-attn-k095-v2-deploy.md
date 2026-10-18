# diagnose dead s47 attn k095 v2 deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dead_s47_attn_k095_v2_deploy_20260529T025236_result.json`
- **Structured JSON:** [`9685b72b4deede893ed5.json`](../../sessions/96/9685b72b4deede893ed5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。

## 总结

- **v1 失败原因**：无任何痕迹（无日志、无 sentinel、无结果），进程从未成功运行。最可能是 GPU 0 被 l2norm 实验占用时启动导致 OOM 即时崩溃，且未通过 submit_training_job 部署所以无错误捕获。
- **v2 部署**：无需重新部署——实验已在 cqa1 GPU 0 上运行（PID 726668，10:27 UTC 启动），Task 0 完成（88%），Task 1 进行中。Registry 已更新为 RUNNING。
- **注意**：该进程未通过 submit_training_job 启动，缺少 sentinel trap，完成后需要手动检查结果。

---
