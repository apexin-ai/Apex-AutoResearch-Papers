# ops urgent cqa1 status check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-cqa1-status-check_20260519T040043_result.json`
- **Structured JSON:** [`77f8a0be7f28cc2c4d28.json`](../../sessions/77/77f8a0be7f28cc2c4d28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集，汇总如下。

---

## GPU 状态 (cqa1-22115, 2026-05-19 12:01 UTC)

| GPU | Util | Memory | PID | 实验 |
|-----|------|--------|-----|------|
| 0 | **0%** | 0 / 24564 MiB | — | 空闲 (pythia_retrain_depth7 已完成) |
| 1 | **95%** | 15163 / 24564 MiB | 114228 | exp_code_qwen7b |
| 2 | **96%** | 16007 / 24564 MiB | 96340 | exp_code_llama8b |
| 3 | **96%** | 14511 / 24564 MiB | 107037 | exp_code_mistral7b |

---

## 实验状态总表

```
exp_id               | 状态              | K* | AUC (0v1, 1v2)       | GPU util
---------------------+-------------------+----+----------------------+---------
exp_code_pythia1b4   | DONE              | 1  | 0.959, 0.598         | —
exp_code_qwen1b5     | DONE              | 2  | 0.939, 0.738         | —
exp_code_llama8b     | RUNNING depth4 30%| —  | —                    | 96%
exp_code_mistral7b   | RUNNING depth2 94%| —  | —                    | 96%
exp_code_qwen7b      | RUNNING depth2 25%| —  | —                    | 95%
exp_pythia_retrain_d7| DONE (registry)   | —  | —                    | 0% (空闲)
```

---

## 详细进度

**exp_code_llama8b** (cuda:2, PID 96340, 非 96335)
- 当前: depth 4, 421/1375 (30%), ~5.9s/it
- 已完成 data: depth_0 ~ depth_3
- results/ 目录: 空（未到 scoring 阶段）
- 预估剩余: depth4 剩 ~1h34m + depth5 ~2h15m + scoring ~30m ≈ **~4.5h**

**exp_code_mistral7b** (cuda:3, PID 107037)
- 当前: depth 2, 1294/1375 (94%), ~5.7s/it
- 已完成 data: depth_0, depth_1
- depth2 即将完成 (~8min)，然后 depth 3/4/5 + scoring
- 预估剩余: **~7h**

**exp_code_qwen7b** (cuda:1, PID 114228)
- 当前: depth 2, 339/1375 (25%), ~5.5s/it
- 已完成 data: depth_0, depth_1
- 预估剩余: depth2 ~1h35m + depth 3/4/5 ~6h18m + scoring ≈ **~8.5h**

---

## 已完成实验 AUC 详情

**exp_code_pythia1b4** (K\* = 1):
| Pair | Mean AUC | 5-fold values |
|------|----------|---------------|
| 0v1 | 0.9592 ± 0.0036 | 0.958, 0.958, 0.966, 0.960, 0.955 |
| 1v2 | 0.5983 ± 0.0050 | 0.601, 0.588, 0.600, 0.600, 0.602 |
| 2v3 | 0.5215 ± 0.0128 | 0.524, 0.512, 0.531, 0.502, 0.538 |
| 3v4 | 0.5152 ± 0.0120 | 0.498, 0.533, 0.509, 0.512, 0.524 |
| 4v5 | 0.5046 ± 0.0137 | 0.498, 0.482, 0.507, 0.522, 0.513 |

**exp_code_qwen1b5** (K\* = 2):
| Pair | Mean AUC | 5-fold values |
|------|----------|---------------|
| 0v1 | 0.9388 ± 0.0047 | 0.936, 0.938, 0.947, 0.939, 0.933 |
| 1v2 | 0.7382 ± 0.0132 | 0.737, 0.750, 0.724, 0.756, 0.724 |
| 2v3 | 0.5300 ± 0.0073 | 0.520, 0.525, 0.534, 0.530, 0.542 |
| 3v4 | 0.5022 ± 0.0074 | 0.499, 0.512, 0.510, 0.497, 0.493 |
| 4v5 | 0.5219 ± 0.0056 | 0.531, 0.523, 0.523, 0.515, 0.518 |

---

## 备注

- `analyze_code_crossmodel.py` 存在，但 3 个 7B/8B 实验均未完成，现在运行只有 pythia1b4 和 qwen1b5 两组数据，建议等全部完成后再跑。
- **cuda:0 确认空闲**，可分配新任务。
- llama8b 的实际 PID 是 96340（可能 96335 是父进程/launcher）。

---
