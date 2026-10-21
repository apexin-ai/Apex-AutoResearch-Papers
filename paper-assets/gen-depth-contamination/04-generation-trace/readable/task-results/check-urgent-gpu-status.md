# check urgent gpu status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_urgent_gpu_status_20260516T175648_result.json`
- **Structured JSON:** [`db5d1e98ea993aeb158d.json`](../../sessions/db/db5d1e98ea993aeb158d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 3987/24564 MiB | 49% | **在跑** — exp-022 `qwen_cont256__olmo` (PID 65356) |
| 1 | 0/24564 MiB | 0% | **空闲** |
| 2 | 0/24564 MiB | 0% | **空闲** |
| 3 | 3089/24564 MiB | 41% | **在跑** — exp-022 `qwen_cont256__olmo` (PID 66243) |

---

## exp-024 (arXiv domain) — 已完成

**K\* = 3**

| 对比 | AUC | JSD |
|------|-----|-----|
| 0v1 | 0.9948 ± 0.0008 | 0.2030 |
| 1v2 | 0.8581 ± 0.0123 | 0.0773 |
| **2v3** | **0.6436 ± 0.0219** | **0.0198** |
| 3v4 | 0.5440 ± 0.0164 | 0.0083 |
| 4v5 | 0.5299 ± 0.0242 | 0.0077 |

Top-3 features: freq_entropy (9880), surp_std (8425), surp_mean (7643)

---

## exp-025 (Pythia arXiv) — 未启动

结果目录 `results/exp_025_pythia_arxiv/` 不存在，无相关进程。`download_arxiv_seed.py` (PID 25732) 仍在运行，可能是前置依赖。

---

## exp-022 (cross-scorer matrix) — 进行中

- **已完成**: 11 组合（有 summary.txt）
- **当前在跑**: `qwen_cont256__olmo`（cuda:0 + cuda:3 各一个进程，处于 feature extraction 阶段 ~75-85%）
- **注意**: 两个脚本 (`exp022_cuda0.sh` + `exp022_cross_scorer_matrix.sh`) 同时对同一 combo 写同一目录，可能冲突

---

## 可用卡

**GPU 1 和 GPU 2 完全空闲**，可立即分配新任务。

**风险提示**: exp-022 的两个脚本疑似重复跑同一个 combo (`qwen_cont256__olmo`)，建议检查是否需要 kill 其中一个以避免文件写冲突。

---
