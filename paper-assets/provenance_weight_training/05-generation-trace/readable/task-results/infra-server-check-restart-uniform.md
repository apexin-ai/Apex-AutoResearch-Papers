# infra server check restart uniform

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_server-check-restart-uniform_20260513T231603_result.json`
- **Structured JSON:** [`415d52fba4bc03a6ebfb.json`](../../sessions/41/415d52fba4bc03a6ebfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个训练全部正常运行，均从 checkpoint-500 恢复。

## 汇报

**服务器状态**
- GPU: 4x NVIDIA RTX PRO 6000 (98GB)，GPU 0 空闲，GPU 1/2/3 各占用 44GB
- 磁盘: 根分区 45% (17GB free)，数据盘 11% (225GB free)
- output symlink → 数据盘 ✓，HF cache 在数据盘 ✓
- 无残留进程

**Checkpoint 情况**
- 3 个 seed 均有完整的 checkpoint-500（model.safetensors 1.1GB + optimizer.pt 2.2GB + trainer_state.json）

**修复**
- 脚本 `pretrain_weighted.py` 原本不支持 `--resume_from_checkpoint`，已添加该参数并传给 `trainer.train()`

**训练提交**

| 实验 | GPU | PID | tmux session | 状态 |
|------|-----|-----|-------------|------|
| uniform_seed42 | cuda:1 | 45926 | uniform_seed42 | 运行中，step 502/6103 |
| uniform_seed123 | cuda:2 | 46075 | uniform_seed123 | 运行中，从 ckpt-500 恢复 |
| uniform_seed456 | cuda:3 | 46415 | uniform_seed456 | 运行中，从 ckpt-500 恢复 |

---
