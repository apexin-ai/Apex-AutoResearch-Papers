# verify seed4 v2 and seed5 gpu

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_seed4_v2_and_seed5_gpu_20260521T081044_result.json`
- **Structured JSON:** [`8b4413033fba266a4d40.json`](../../sessions/8b/8b4413033fba266a4d40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### bjb1-17606 — Seed 4 v2 ✅

| 项目 | 状态 |
|------|------|
| PID | 存活 — GPU 进程 PID 299577, 299578 (`actor_rollout_init_model`) |
| GPU 0 | 4339 MiB / 97887 MiB, 0% util（模型加载阶段） |
| GPU 1 | 4339 MiB / 97887 MiB, 0% util（模型加载阶段） |
| CUDA_VISIBLE_DEVICES | `0,1` ✅ |
| save_freq | `5` ✅ |
| 阶段 | 正在初始化模型（Qwen3 1.72B），尚未开始训练 |

### westd-47453 — Seed 5 v2 ✅

| 项目 | 状态 |
|------|------|
| GPU 0 | 36857 MiB / 97887 MiB, **100% util** — 已在训练 |
| GPU 1 | 36755 MiB / 97887 MiB, **100% util** — 已在训练 |
| GPU 2 | **0 MiB, 0% util** — 空闲 ✅ |
| GPU 3 | **0 MiB, 0% util** — 空闲 ✅ |
| W&B | run `yyoghk1f`，名称 `exp029-seed5-episode-level` |
| 进度 | 数据加载完成 (494/494)，已进入训练循环 |

**结论**：两个实验均正常运行在正确的 GPU 上。westd GPU 2,3 空闲，可以启动 Seed 6 v3。

---
