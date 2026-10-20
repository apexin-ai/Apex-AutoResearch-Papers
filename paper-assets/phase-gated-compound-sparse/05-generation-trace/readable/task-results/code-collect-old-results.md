# code collect old results

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_collect_old_results_20260515T215848_result.json`
- **Structured JSON:** [`fecde44e4ed40fab5a4f.json`](../../sessions/fe/fecde44e4ed40fab5a4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果汇总

### GPU 状态
| GPU | 使用率 | 显存 | 运行进程 |
|-----|--------|------|----------|
| 0 | 93% | 30.5/97.9 GB | DS dense_8k (PID 277995, 33min) + QW rand_s025 profiling (PID 281024, 1min) |
| 1 | 74% | 16.6/97.9 GB | DS s015_8k (PID 278395, 32min) + QW rand_s030 profiling (PID 281448, <1min) |
| 2 | 71% | 15.5/97.9 GB | DS s020_8k_v2 (PID 280643, 5min) |
| 3 | 0% | 空闲 | — |

---

### 1. DS dense_8k — 仍在运行
PID 277995, 已运行 33 分钟，输出文件 `accuracy_ds_dense_8k.json` 尚未生成。

### 2. DS s015_8k — 仍在运行
PID 278395, 已运行 32 分钟，输出文件 `accuracy_ds_s015_8k.json` 尚未生成。

### 3. QW batch2 结果（problems 51-100）— 已完成 ✓

全部 5 个 QW condition 的 batch2 都已完成，文件在 `analysis_output/`：

| Condition | Correct | Total | Accuracy | max_new_tokens |
|-----------|---------|-------|----------|----------------|
| **dense** | 24 | 50 | **0.48** | 8192 |
| **s015** | 19 | 50 | **0.38** | 8192 |
| **s020** | 22 | 50 | **0.44** | 2048 |
| **s025** | 17 | 50 | **0.34** | 2048 |
| **s030** | 12 | 50 | **0.24** | 8192 |

**注意**：s020 和 s025 的 batch2 使用了 `max_new_tokens=2048`，而其余三个用的是 8192，配置不一致。

### QW 完整 100 题 dose curve（batch1 + batch2 合并）

如果 batch1 也是 50 题，结合之前的数据（batch1 s030 = 7/50 = 0.14），s030 合并结果 = (7+12)/100 = **0.19**。其他 condition 需要 batch1 数据才能合并。

---

### 额外发现
- GPU 2 上还在跑一个 **DS s020_8k_v2** eval（PID 280643, 5min），非任务要求的实验
- GPU 0/1 上各新启动了 QW random sparsity GSM8K profiling 任务

---
