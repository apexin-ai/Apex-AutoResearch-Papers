# ops westd38929 crash diagnosis restart

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-crash-diagnosis-restart_20260521T011901_result.json`
- **Structured JSON:** [`49f2d11951f30b09f944.json`](../../sessions/49/49f2d11951f30b09f944.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 4 个实验都在正常运行中，不需要重启。**

当前状态：
- **GPU 0** `eval_random_k095_seed42_v2`: 正在执行中，某 task Ep 10/50, task_sr=8/10
- **GPU 1** `eval_random_k07_seed42_v2`: 刚完成 task 4 (SR 38.0%), 进入 task 5
- **GPU 3** `eval_l2norm_k09_seed43_v2`: 刚完成 task 4 (SR 48.0%), 进入 task 5
- **GPU 2** `smolvla_baseline_spatial`: Task 0 完成 (SR 24.0%), 进入 task 1

SmolVLA Spatial 的资源文件问题已经被修复（session 在 09:14 创建，正常运行中）。

之前报告的"无声死亡"是误判——v2 实验在 07:32 启动后一直在跑，日志在持续更新。3 个 Object eval 都到了 task 5/10 附近，进度正常（每个 task 50 episodes，~2 eps/min，一个 task 约 25 分钟）。

额外发现：`eval_openvla_libero.py` 的实际参数名是 `--mode`（非 `--prune_mode`）和 `--k_ratio`（非 `--keep_ratio`），无 `--gpu`/`--model_path` 参数。如果后续需要重启，需要用正确的参数。

---
