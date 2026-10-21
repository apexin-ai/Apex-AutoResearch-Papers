# ops check a050 and verify data

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-a050-and-verify-data_20260515T044616_result.json`
- **Structured JSON:** [`c23ba386f840f882a1e8.json`](../../sessions/c2/c23ba386f840f882a1e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. a050_s42 进度

**未完成，当前在 gen_8（训练中）。**

- gen_0 ~ gen_7 已完成，gen_8 正在跑（有 `synthetic_data/` 和 `trainer/`，尚未产出 metrics）
- gen_9 尚未开始
- 进程 73737 **仍在运行**，已运行 `03:26:41`
- 配置：`num_generations 10`, `synthetic_ratio 0.50`, `seed 42`, `CUDA_VISIBLE_DEVICES=1`

预计还需 ~50 分钟完成（gen_8 剩余训练 + gen_9 完整周期，按每代 ~25min 估算）。

---

### 2. α=0.25 数据源核实

- **`a025_s42_v3/` 不存在**
- **`a025_s42/` 是唯一版本**，已完成，有 `EXIT_CODE` 和顶层 `all_metrics.json`
- 实际跑了 **11 代**（gen_0 ~ gen_10），不是 10 代

dose-response worker 用的 `a025_s42` 就是正式数据，不存在版本混淆问题。

**a025_s42 关键指标（gen_0 → gen_10）：**

| 指标 | gen_0 | gen_9 | gen_10 | drift (gen_0→gen_10) |
|------|-------|-------|--------|---------------------|
| distinct_1 | 0.0982 | 0.0590 | 0.0586 | **-40.4%** |
| distinct_2 | 0.5178 | 0.2290 | 0.2219 | **-57.1%** |
| distinct_3 | 0.8127 | 0.3438 | 0.3263 | **-59.9%** |
| perplexity | 26.95 | 22.51 | 22.32 | -17.2% |
| mauve | 0.0341 | 0.0167 | 0.0163 | -52.3% |
| effective_rank | 46.61 | 46.04 | 45.30 | -2.8% |

---

### 3. MVP (α=1.0) 数据路径

- **`results/mvp/`** — 4 个种子的重复实验：`rep_42`, `rep_43`, `rep_44`, `rep_45`，加上 `analysis/` 目录
- **`results/extended_20gen/`** — 包含 `s42/` 子目录（20 代扩展实验）

---
