# diag westd post restart

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-post-restart_20260519T124520_result.json`
- **Structured JSON:** [`0681d3570a9fa067aa0d.json`](../../sessions/06/0681d3570a9fa067aa0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. Cell C v3 训练 — 已死亡 (OOM)

- **4 张 GPU 全部空闲**：0% 利用率，0 MiB 显存占用
- **退出码**：1（崩溃）
- **死因**：`torch.OutOfMemoryError` — 在 `loss.backward()` 阶段（`dp_actor.py:468`）尝试分配 8.76 GiB 失败
  - GPU 0 总容量 94.97 GiB，PyTorch 已分配 118.48 GiB（跨 FSDP shards），仅剩 ~5-6 GiB 可用
  - 两个 worker（pid 43190, 43724）同时 OOM
- **日志**：`/root/runs/cost-verify-agent-rl/8b_cell_c_v3.log`
- **关键信息**：`ppo_mini_batch_size=4` 对 8B 模型 + 4 GPU FSDP 在 backward pass 时显存不够。需要降 mini_batch_size 或启用 gradient checkpointing / offload。

### 2. ScienceWorld 数据提取 — 存活

- **PID 51279**：运行中，已运行 15 分 38 秒
- **命令**：`python3 /root/autodl-tmp/extract_scienceworld_sft_optimized.py`
- **输出文件**（partial，仍在写入）：
  - `scienceworld_sft_train_partial.jsonl` — 619 条，33.4 MB
  - `scienceworld_sft_val_partial.jsonl` — 322 条，16.0 MB
- 最终文件 `scienceworld_sft_train.jsonl` 尚未生成（提取未完成）

### 3. 磁盘

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/`（根） | 30G | 14G | 17G | 46% |
| `/root/autodl-tmp` | 250G | 80G | 171G | 32% |

磁盘充足，无风险。

---
