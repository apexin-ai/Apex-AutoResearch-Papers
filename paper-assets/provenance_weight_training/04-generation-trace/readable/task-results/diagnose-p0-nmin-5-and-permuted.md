# diagnose p0 nmin 5 and permuted

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_p0_nmin_5_and_permuted_20260524T164432_result.json`
- **Structured JSON:** [`46643519871b4f23f90a.json`](../../sessions/46/46643519871b4f23f90a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 实验 1: p0_nmin_5
- **失败点**: step 500/6103（~8%），保存 checkpoint 时
- **根因**: **磁盘空间不足**。模型 shard 写入成功，但保存 optimizer state 时磁盘写满，触发 `RuntimeError: basic_ios::clear: iostream error` → `RuntimeError: [enforce fail at inline_container.cc:668]`
- Traceback: `trainer._save_optimizer_and_scheduler` → `torch.save(optimizer.state_dict())` → iostream error

### 实验 2: permuted_score_control_seed42
- **失败点**: step 500/6103（~8%），保存 checkpoint 时
- **根因**: **磁盘空间不足**。`OSError: [Errno 28] No space left on device` — 连 checkpoint 目录都创建不了
- 路径: `/root/autodl-tmp/.../permuted_score_control_seed42/checkpoint-500`

### 实验 3: p0_batchsize_16
- **失败点**: step 0，第一个 forward pass
- **根因**: **GPU 显存不足（与磁盘无关）**。`torch.OutOfMemoryError: Tried to allocate 18.55 GiB`，GPU 总容量 95GB 已被占用 80GB。batch_size=16 对 Qwen3-0.6B 来说太大，logits float 转换需要 18.55GB。

### 共同原因分析
- **p0_nmin_5 + permuted_score_control_seed42**: 共同原因是 `/root/autodl-tmp` **磁盘满**。两个实验同时运行，在 step 500 同时尝试保存 checkpoint，把 250GB 数据盘写满。当前磁盘已恢复到 56%（111GB 可用），说明旧 checkpoint 已被清理。
- **p0_batchsize_16**: 独立原因 — GPU OOM，batch_size=16 太大。

### 是否可以直接重试

| 实验 | 能否直接重试 | 说明 |
|------|------------|------|
| p0_nmin_5 | **可以** | 当前磁盘 111GB 可用。建议先清理不需要的旧 checkpoint，并避免同时在多个实验保存大量 checkpoint |
| permuted_score_control_seed42 | **可以** | 同上 |
| p0_batchsize_16 | **需改参数** | batch_size=16 OOM，需降到 4-8，或加 gradient_checkpointing |

**建议**: 重试前检查 `/root/autodl-tmp` 下有多少旧 checkpoint 占空间，设置 `--save_total_limit 2` 已有但仍可能因多个实验同时写 checkpoint 而爆盘。如果要同时跑多个实验，考虑错开 save_steps 或减少保存频率。

---
