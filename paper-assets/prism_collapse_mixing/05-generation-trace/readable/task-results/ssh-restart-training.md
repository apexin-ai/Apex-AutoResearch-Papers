# ssh restart training

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_restart-training_20260515T203617_result.json`
- **Structured JSON:** [`37730de59e2731be3aa7.json`](../../sessions/37/37730de59e2731be3aa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重启成功。报告：

---

**崩溃原因**：`train.py:79` 的 `wandb.init()` 因无 API key 报错 `UsageError: No API key configured`

**已有数据**：
- `synthetic/synthetic_gen1_seed42.jsonl` (320M) ✓
- `synthetic/synthetic_gen1_seed137.jsonl` (320M) ✓
- `mixed/mixed_gen1_seed42.jsonl` (899M) ✓
- `mixed/mixed_gen1_seed137.jsonl` (899M) ✓
- `checkpoints/` 空（训练失败未产出）

**run_pipeline.py 修改**：无需修改，4 个步骤均已有跳过逻辑。重启后自动跳过 synthetic 和 mix，直接从 train 开始。

**重启状态**：
- tmux `mvp_collapse_decoupling`：运行中 ✓
- 环境变量：`WANDB_MODE=disabled HF_HUB_OFFLINE=1` ✓
- GPU：两张 GPU 各占用 1372 MiB，正在训练
- PID：`198116`（seed42, cuda:0）、`198117`（seed137, cuda:1）
- 父进程 `run_pipeline.py` PID：`197985`

---
