# ops 008f smoke test

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_008f_smoke_test_20260514T045256_result.json`
- **Structured JSON:** [`c53506a586664af1d40e.json`](../../sessions/c5/c53506a586664af1d40e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

再确认 PID 127766 对应 GPU 进程。GPU 0 上的 106947 是另一个实验。exp_008f 刚启动约 1.5 分钟，还在 prefill 阶段（step=0 的 4 条 seed episodes），尚未开始 model training，所以 GPU 显存占用还没上来。

验证结果：

- **进程状态**: alive
- **PID 链**: 127761 (bash wrapper) → 127765 (timeout) → 127766 (python dreamer.py)
- **运行时间**: ~1.5 分钟
- **参数确认**: `--gate_dt_embed_dim 0` 已正确传入，无 argparse 报错
- **logdir**: 已创建，包含 `metrics.jsonl`、`tfevents`、`train_eps/`、`eval_eps/`
- **metrics.jsonl**: 4 条 seed episode 记录（step=0, dataset_size=2000, return 30~55），prefill 正常
- **GPU**: 尚未在 nvidia-smi 中显示（仍在 prefill 收集数据阶段，训练循环未开始），GPU 0 当前被 PID 106947 占用 4158MiB（另一个实验）

exp_008f 一切正常，正在完成 prefill，预计很快进入训练循环并占用 GPU 显存。

---
