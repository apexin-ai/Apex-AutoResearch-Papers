# eval openvla prune k095 westd

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_openvla_prune_k095_westd_20260518T202954_result.json`
- **Structured JSON:** [`3b6015461930ef6d31e5.json`](../../sessions/3b/3b6015461930ef6d31e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。总结：

**eval_openvla_prune_k095** 已在 westd-27271 cuda:1 上启动运行：
- 脚本：`/tmp/eval_openvla_libero_gpu1.py`（CUDA_VISIBLE_DEVICES=1）
- 参数：`--mode random_prune --k_ratio 0.95 --seed 7`
- Token pruning：256 → 243（移除 13 个 token，5%）
- PID：355272，tmux session：`eval_openvla_k095`
- 日志：`eval_results/openvla_random_prune_k095_object.log`
- Registry：RUNNING

**注意**：使用 seed=7（非 42），与 OpenVLA 降级曲线其他 4 个点 (k=1.0/0.7/0.5/0.3) 保持一致。

**并行状态**：cuda:0 上已有 k=0.9 eval 在运行（PID 354660），两者独立并行。

预计 ~4-5h 完成 500 episodes。

---
