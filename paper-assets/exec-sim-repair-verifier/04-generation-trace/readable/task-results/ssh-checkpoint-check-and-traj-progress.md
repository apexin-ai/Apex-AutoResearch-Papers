# ssh checkpoint check and traj progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_checkpoint-check-and-traj-progress_20260523T092715_result.json`
- **Structured JSON:** [`fd15f81531affe84a66d.json`](../../sessions/fd/fd15f81531affe84a66d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

---

## 任务 1：Qwen3 CWM Checkpoint 存在性检查

### Qwen3-8B CWM（3 个目录）

| 目录 | Checkpoints | Best Step |
|------|------------|-----------|
| `checkpoints_cwm8b` | 956, 1434 | **956** |
| `checkpoints_cwm8b_seed123` | 956, 1434 | **956** |
| `checkpoints_cwm8b_seed456` | 956, 1434 | **956** |

### Qwen3-4B CWM（4 个目录）

| 目录 | Checkpoints | Best Step |
|------|------------|-----------|
| `checkpoints_cwm_seed123` | 956, 1434 | **956** |
| `checkpoints_cwm_seed789` | 956, 1434 | **956** |
| `checkpoints_cwm_rank32` | 478, 1434 | **478** |
| `checkpoints_cwm_rank32_alpha64` | 956, 1434 | **956** |

### Qwen3-14B CWM（2 个目录，在 `/root/autodl-tmp/checkpoints/`）

| 目录 | Checkpoints | Best Step |
|------|------------|-----------|
| `cwm14b-func-s123` | 956, 1434 | **956** |
| `cwm14b-func-s456` | 478, 1434 | **478** |

### 空目录
- `checkpoints_repo_cwm` — 空
- `checkpoints_cwm_rank64` — 空

### Step 300-400 范围判定

**所有 CWM 目录中均没有 step 300-400 范围的 checkpoint。** 现存 checkpoint 只有 step 478、956、1434 三档。最接近的是 step 478（出现在 `checkpoints_cwm_rank32` 和 `cwm14b-func-s456`）。

8B 主实验（3 个 seed）最早可用的 checkpoint 是 step 956，step 300-400 范围的中间 checkpoint 已被 `save_total_limit` 自动清理。

---

## 任务 2：TRAJ 14B 训练进度

3 个进程均正常运行中，GPU 0/1/2 利用率 77-88%，GPU 3 空闲。

| Seed | GPU | PID | Step | Total | Epoch | Loss | ETA |
|------|-----|-----|------|-------|-------|------|-----|
| s42 | 0 | 265154 | 155 | 756 | 1/3 | 尚未输出 | ~1h16m |
| s123 | 1 | 265560 | 154 | 756 | 1/3 | 尚未输出 | ~1h16m |
| s456 | 2 | 265996 | 148 | 756 | 1/3 | 尚未输出 | ~1h16m |

- 速度：~7.4-7.6 s/step
- 训练启动时间：17:08-17:09，已运行约 19 分钟
- Loss 尚未在 log 中输出（logging_steps 可能设较大值，或首次 log 在后续 step）
- 每个 epoch 252 步，当前均在第 1 个 epoch 的 ~60% 位置
- 预计 3 个 epoch 全部完成时间：约 18:45 左右

---
