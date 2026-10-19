# ssh launch v72 training dual

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch-v72-training-dual_20260517T101827_result.json`
- **Structured JSON:** [`a6d6c44e3252243ab48b.json`](../../sessions/a6/a6d6c44e3252243ab48b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

drift_loss 未在日志中出现。可能计算了但未打印。汇报结果：

---

**v7.2 connector+scorer 双 seed 训练已启动**

| | Seed 1 (GPU 0) | Seed 2 (GPU 1) |
|---|---|---|
| **PID** | 24197 | 24286 |
| **tmux** | v72_seed1 | v72_seed2 |
| **GPU 显存** | 15233 MiB | 15233 MiB |
| **output_dir** | acib_v7.2_connector_scorer | acib_v7.2_connector_scorer_seed2 |
| **seed** | 42 | 123 |

**确认项：**
- Trainable params: **11,919,489** (~11.9M, 2.6%) — connector 11.8M + scorer 0.1M ✓
- Freeze mode: `connector_scorer` ✓
- 训练速度: ~1.8 steps/s
- Step 100 已完成，loss 正常下降

**注意：** `drift_loss` 未在日志 step 行中出现。`--lambda_drift 0.1` 参数已传入，但训练循环的 log 格式可能没有包含 drift 项。需要检查 `train_acib.py` 的 logging 代码确认 drift loss 是否在计算但未打印。

---
