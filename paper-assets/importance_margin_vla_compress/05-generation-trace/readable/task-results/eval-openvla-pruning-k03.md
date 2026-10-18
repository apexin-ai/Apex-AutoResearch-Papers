# eval openvla pruning k03

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_openvla_pruning_k03_20260518T010204_result.json`
- **Structured JSON:** [`02f0c55d2811f0453767.json`](../../sessions/02/02f0c55d2811f0453767.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动，运行正常：

- **PID**: 768723 (子进程在 GPU 1 上)
- **GPU 1**: 16108 MiB 已用，83% 利用率
- **状态**: 模型已加载，正在 Task 1/10 执行 eval
- **Pruning**: 256 → 76 vision tokens (k=0.3)
- **日志**: `eval_results/openvla_random_prune_k03_object.log`
- **JSON 输出**: 完成后自动保存到 `eval_results/openvla_random_prune_k03_object.json`

注意：`submit_training_job` 工具不存在，用了和 k=0.7 相同的 nohup 方式启动。由于脚本硬编码了 `CUDA_VISIBLE_DEVICES="0"`，创建了一份 sed 修改后的副本（`/tmp/eval_openvla_libero_gpu1.py`）将其改为 `"1"`。

---
