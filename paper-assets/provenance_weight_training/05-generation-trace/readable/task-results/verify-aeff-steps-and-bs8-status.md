# verify aeff steps and bs8 status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_aeff_steps_and_bs8_status_20260523T200220_result.json`
- **Structured JSON:** [`f9b484245ae7ee91d121.json`](../../sessions/f9/f9b484245ae7ee91d121.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务1: aeff_only 训练步数

- seed42: 文件 24412 行，最后一条 step=6102 → **实际 6103 步**（每步 4 条日志，24412/4=6103）
- seed123: 文件 24412 行，最后一条 step=6102 → **实际 6103 步**
- `pretrain_weighted.py` 中 `--num_train_tokens` 默认值 = **None**（远程版本与本地一致）
- **结论：步数正好是标准 6103 步，未训练过多。** 虽然命令行缺少 `--num_train_tokens 200000000`，但实际训练恰好在 6103 步停止。可能原因：数据集总 token 数恰好约等于 200M（一个完整 epoch ≈ 6103 步），或者有其他停止机制（如 `--max_steps` 参数在命令行中传入但你没列出）。建议复查实际启动命令确认。

## 任务2: B=8 seed456 状态

- **bs8_nmin4_adaptive_seed456_r2**: RUNNING — step 4633/6103（76%），ETA ~2h
- **bs8_nmin4_uniform_seed456_r2**: RUNNING — step 4773/6103（78%），ETA ~2h
- GPU 状态:
  - cuda:0 — **占用**（100% util, 92098 MiB）
  - cuda:1 — 空闲（0%, 0 MiB）
  - cuda:2 — **占用**（100% util, 92066 MiB）
  - cuda:3 — 空闲（0%, 0 MiB）

B=8 两个实验仍在运行，约 2 小时后完成。cuda:1 和 cuda:3 空闲，但 cuda:0 被 adaptive 占用。seed456 启动需等 B=8 完成释放 cuda:0。

---
