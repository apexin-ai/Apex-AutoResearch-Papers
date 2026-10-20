# diag bjb2 urgent check and run

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb2-urgent-check-and-run_20260518T075430_result.json`
- **Structured JSON:** [`e050f0d8adfabe96dd03.json`](../../sessions/e0/e050f0d8adfabe96dd03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

---

## 状态总览

| tmux session | 状态 | 内容 |
|---|---|---|
| `tc_phase3` | **已完成** | Qwen t=0.9 特征提取 (4558 条) |
| `exp054_resume` | **已完成** | Llama instruct 特征提取 + 评估 |
| `feat_qwen_t09` | **已完成** | Qwen t=0.9 特征提取 (shard, 2413 条, 被 tc_phase3 覆盖) |
| `feat_t05` | **已完成** | Pythia t=0.9 特征提取 (4536 条) |

GPU 全部空闲，无运行进程。

## 数据行数

| 文件 | 行数 (含 header) |
|---|---|
| `features_qwen3-1.7b-t09.csv` | 4559 (4558 条记录) |
| `features_llama-3.2-3b-instruct.csv` | 4975 (4974 条记录) |
| `features_pythia-2.8b-t09.csv` | 4537 (4536 条记录) |

## Llama-3.2-3B Instruct 评估结果

**分类性能** (Instruct vs Base):

| 指标 | Instruct | Base | Delta |
|---|---|---|---|
| Binary F1 | 0.8381 [0.828, 0.847] | 0.8488 [0.839, 0.859] | -0.011 |
| 3-class F1 | 0.5437 [0.530, 0.558] | 0.7424 [0.728, 0.755] | -0.199 |

**Spearman ρ (Instruct)**:

| Feature | ρ | p-value |
|---|---|---|
| entropy_mean | +0.2299 | 1.09e-60 |
| entropy_std | +0.2623 | 4.54e-79 |
| entropy_min | -0.0027 | 8.47e-01 |
| entropy_max | +0.2036 | 1.07e-47 |
| tail_decay | +0.1198 | 2.33e-17 |
| ttr | -0.1411 | 1.55e-23 |
| hapax_ratio | -0.1157 | 2.65e-16 |

**Spearman ρ (Base)**:

| Feature | ρ | p-value |
|---|---|---|
| entropy_mean | -0.6270 | 0.00 |
| entropy_std | -0.1597 | 4.09e-28 |
| entropy_min | -0.3981 | 1.58e-177 |
| entropy_max | +0.0859 | 3.90e-09 |
| tail_decay | -0.0631 | 1.55e-05 |
| ttr | -0.6856 | 0.00 |
| hapax_ratio | -0.6975 | 0.00 |

**方向反转**: 3/7 特征 (entropy_mean, entropy_std, tail_decay)

## Qwen t=0.9 温度评估

**LOGO Binary F1** (重跑，使用完整 4558 条数据):

| Model | t=0.5 | t=0.7 | t=0.9 | t=1.0 |
|---|---|---|---|---|
| pythia-2.8b | 0.8136 | 0.7395 | 0.4804 | — |
| qwen3-1.7b | 0.7506 | 0.7505 | **0.5659** | 0.3670 |

**Qwen t=0.9 Spearman ρ** (4558 条, depth 分布: {0:996, 1:984, 2:946, 3:860, 4:772}):

| Feature | ρ | p-value |
|---|---|---|
| entropy_mean | -0.3739 | 3.46e-151 |
| entropy_std | -0.0443 | 2.75e-03 |
| entropy_min | -0.2119 | 1.92e-47 |
| entropy_max | +0.0888 | 1.94e-09 |
| tail_decay | -0.0862 | 5.52e-09 |
| ttr | -0.5141 | 5.46e-306 |
| hapax_ratio | -0.5352 | 0.00 |

## 错误

无错误。所有任务正常完成。

---
