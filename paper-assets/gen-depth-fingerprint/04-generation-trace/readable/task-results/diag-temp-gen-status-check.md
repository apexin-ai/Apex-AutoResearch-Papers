# diag temp gen status check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_temp-gen-status-check_20260518T152636_result.json`
- **Structured JSON:** [`afeab953cd80275a09d1.json`](../../sessions/af/afeab953cd80275a09d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
temp_qwen06: 运行中（t=0.5 阶段）
  - tmux session: temp_qwen06（存在）
  - 当前任务: [1/2] t=0.5 top_p=0.9
  - 进度: 160/996 seeds (16%), 速度 10.12s/it, 剩余 ~2h21m
  - t=0.5 文件: /root/gen-depth-fingerprint/data/qwen3-0.6b-t05/generations_shard0.jsonl, 750 行
  - t=0.9 文件: 尚未开始（qwen3-0.6b-t09 目录不存在）
  - 预计完成 t=0.5 + t=0.9 全部: ~5h

temp_olmo: 运行中（t=0.5 阶段）
  - tmux session: temp_olmo（存在）
  - 当前任务: [1/2] t=0.5 top_p=0.9
  - 进度: 231/995 seeds (23%), 速度 8.71s/it, 剩余 ~1h51m
  - t=0.5 文件: /root/gen-depth-fingerprint/data/olmo-2-1b-t05/generations_shard0.jsonl, 1136 行
  - t=0.9 文件: 尚未开始（olmo-2-1b-t09 目录不存在）
  - 预计完成 t=0.5 + t=0.9 全部: ~4h15m

GPU 状态:
  - GPU 0: 使用中 — OLMo (PID 27216), 3616MiB/32607MiB, 50% util
  - GPU 1: 使用中 — Qwen (PID 27228), 1816MiB/32607MiB, 32% util
  - GPU 2: 空闲
  - GPU 3: 空闲
```

两个实验都在正常运行，都处于 t=0.5 的第一阶段。数据格式正确（jsonl，每条含 id/depth/text/seed_id/token_count/model 字段，每 seed 5 个 depth）。OLMo 跑得快些（8.71s vs 10.12s per seed），预计全部完成（含 t=0.9）分别在 ~4h15m 和 ~5h 后。GPU 2、3 空闲可用。

---
