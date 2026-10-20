# ops check training progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-training-progress_20260514T234403_result.json`
- **Structured JSON:** [`bda52f769e3349498e55.json`](../../sessions/bd/bda52f769e3349498e55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度报告

**注意**：输出目录实际命名为 `profiling_output_n500_bf16_*`（非 `n500_profiling_output_bf16_*`）。

---

### 实验 1: c2_n500_deepseek（DeepSeek-R1-Distill-Qwen-7B）

tmux session `c2_n500_gpu0` 存活，两个 GPU 分别跑 gpu0/gpu1 脚本。

| Condition | 状态 | 进度 |
|-----------|------|------|
| imp_s015 | **DONE** | n=500 ✓ |
| imp_s020 | **DONE** | n=500 ✓ |
| imp_s025 | **RUNNING** | 101/500（06:55 启动，已跑 49min） |
| imp_s030 | PENDING | — |
| rand_s015 | **DONE** | n=500 ✓ |
| rand_s020 | **DONE** | n=500 ✓ |
| rand_s025 | **RUNNING** | 148/500（06:30 启动，已跑 74min） |
| rand_s030 | PENDING | — |

---

### 实验 2: c2_qw_n500_r3（Qwen2.5-7B-Instruct）

screen sessions `c2_qw_gpu2` + `c2_qw_gpu3` 存活，PID 131858 存活。无 sentinel 文件。

| Condition | 状态 | 进度 |
|-----------|------|------|
| imp_s015 | **DONE** | n=500 ✓ |
| imp_s020 | **DONE** | n=500 ✓ |
| imp_s025 | **RUNNING** | 192/500（06:27 启动，已跑 77min） |
| imp_s030 | PENDING | — |
| rand_s015 | **DONE** | n=500 ✓ |
| rand_s020 | **DONE** | n=500 ✓ |
| rand_s025 | **RUNNING** | 171/500（06:36 启动，已跑 68min） |
| rand_s030 | PENDING | — |

---

### 预估剩余时间

| 当前任务 | 速度 | 剩余 | 预计完成 |
|----------|------|------|----------|
| ds_imp_s025 | ~0.49 min/prob | 399个 → ~195min | ~10:55 |
| ds_rand_s025 | ~0.50 min/prob | 352个 → ~176min | ~10:40 |
| qw_imp_s025 | ~0.40 min/prob | 308个 → ~123min | ~09:47 |
| qw_rand_s025 | ~0.40 min/prob | 329个 → ~132min | ~09:56 |

s025 完成后自动开始 s030（每个约 3-3.5h for DS, 2.5-3h for QW）：

- **QW 实验全部完成**：预计 ~12:30-13:00
- **DS 实验全部完成**：预计 ~14:00-14:30

（以上为服务器本地时间）

---
