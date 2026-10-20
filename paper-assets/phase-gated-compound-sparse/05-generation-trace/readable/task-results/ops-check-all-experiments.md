# ops check all experiments

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_experiments_20260514T180905_result.json`
- **Structured JSON:** [`ad0f8e25831a3e3f48b0.json`](../../sessions/ad/ad0f8e25831a3e3f48b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the status report:

---

## 实验状态汇总 (2026-05-15 02:09 服务器时间)

### 1. c5b_pilot

**PID 154645** — 存活，GPU 3，运行 `run_c5b_pilot.py --sparsity 0.25 --strategy all`

另外还有 **PID 154166** — GPU 0，运行 `run_c5b_pilot.py --sparsity 0.30 --strategy all --model DeepSeek`

三个输出目录均为**空**（刚创建不久）：
- `profiling_output_c5b_pilot_s025` — 创建于 01:56
- `profiling_output_c5b_pilot_s030` — 创建于 02:05
- `profiling_output_c5b_all_s025` — 创建于 02:06

**结论：c5b_pilot 未完成，尚未产出任何结果文件。**

---

### 2. c2_n500_deepseek (GPU 0+1)

实际结果目录命名为 `profiling_output_n500_bf16_ds_{method}_s{sparsity}`（而非 `profiling/results_n500_deepseek/`）。

| Condition | 状态 | PID |
|-----------|------|-----|
| `ds_rand_s015` | **已完成** ✓ (profiling_results.json 存在) | — |
| `ds_imp_s015` | 运行中，输出为空 | 130124 (GPU 0) |
| `ds_rand_s020` | 运行中，输出为空 | 154305 (GPU 1) |

旧版（非 n500）的 `bf16_ds_imp_s015` 和 `bf16_ds_rand_s015` 均已完成。

**结论：n500 版本 s015 完成了 random，importance 仍在跑。s020 random 也在跑。**

---

### 3. c2_qw_n500 (GPU 2+3)

**PID 131864** — 存活，GPU 2，Qwen importance s015 → `profiling_output_n500_bf16_qw_imp_s015`（空）
**PID 132002** — 存活，GPU 3，Qwen random s015 → `profiling_output_n500_bf16_qw_rand_s015`（空）

另有空目录：`qw_rand_s020`、`qw_imp_s020`（已创建但无进程写入）

**结论：两个进程都在运行，尚无输出。**

---

### 4. GPU 利用率

| GPU | 型号 | 利用率 | 显存 | 进程 |
|-----|------|--------|------|------|
| 0 | RTX PRO 6000 Blackwell | **97%** | 54.3/97.9 GB | PID 130124 (ds_imp_s015) + PID 154166 (c5b s030) |
| 1 | RTX PRO 6000 Blackwell | **79%** | 21.4/97.9 GB | PID 154305 (ds_rand_s020) |
| 2 | RTX PRO 6000 Blackwell | **71%** | 34.1/97.9 GB | PID 131864 (qw_imp_s015) |
| 3 | RTX PRO 6000 Blackwell | **97%** | 55.6/97.9 GB | PID 132002 (qw_rand_s015) + PID 154645 (c5b s025) |

4 块 GPU 全部在用，GPU 0 和 GPU 3 各跑了 2 个进程。

---
