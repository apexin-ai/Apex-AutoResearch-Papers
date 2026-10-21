# ssh verify qwen3 fewrel data

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_qwen3_fewrel_data_20260517T140413_result.json`
- **Structured JSON:** [`7fb8f98bf456008ff9c5.json`](../../sessions/7f/7fb8f98bf456008ff9c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据核实完成。以下是完整结论。

---

## 核实结果

### 1. 数据文件路径

| 数据 | 路径 |
|------|------|
| Qwen3 s42 | `artifacts/d051_fewrel_n25_s42/count_curve_summary.json` |
| Qwen3 s123 | `artifacts/d051_fewrel_n25_s123/count_curve_summary.json` |
| Qwen3 s456 | `artifacts/d051_fewrel_n25_s456/count_curve_summary.json` |
| 70B s42 | `artifacts/d051_llama-3.1-70b-fp8_fewrel_n25_s42/results_count_*.jsonl`（无 count_curve_summary.json，需从 JSONL 计算） |

### 2. 论文 appendix 的 Qwen3 值 = d051 三 seed 平均值

```
   Count |  70B s42 |  Qwen s42 |  Qwen 3avg |  Paper (Qwen)
---------+----------+-----------+------------+-------------
       8 |   0.7571 |    0.8050 |     0.7965 |  0.797 ← 3avg
      16 |   0.6852 |    0.7188 |     0.7185 |  0.719 ← 3avg
      32 |   0.6008 |    0.6518 |     0.6482 |  0.648 ← 3avg
      64 |   0.5042 |    0.5393 |     0.5367 |  0.537 ← 3avg
      80 |   0.4497 |    0.5041 |     0.4955 |  0.496 ← 3avg
```

### 3. 批次不一致的根因

- **70B 只有 s42 一个 seed**（960 samples, seed=42, 25 batches）
- **Qwen3 有三个 seed**（s42/s123/s456），每个 seed 使用**不同的 960 samples 和不同的 batch type combinations**
- 论文 appendix 将 70B s42 结果与 Qwen3 三 seed 平均值并列，**跨越了不同的评估批次**

d051 的 sample_info 确认：70B 和 Qwen3 s42 共享 `seed=42, n_samples=960, n_per_rel=12, n_relations=80`，是完全相同的评估设置。s123/s456 是不同的数据采样。

### 4. 额外发现

`exp_v2_re_n25/eval_results.json` 的 count curve 值与 70B d051 s42 **完全一致**（精确到小数点后 10 位），但 preprocess.json 中 model_path 指向 `qwen3-32b-fp8`。这个文件可能被 70B 结果覆盖或存在数据混淆，不应作为 Qwen3 参考来源。

### 5. 推荐

Appendix 跨模型对比表的 Qwen3 参考值应改用 **d051_fewrel_n25_s42 单 seed 结果**：

| Count | 70B | Qwen3 (推荐修正) | Qwen3 (当前论文) |
|-------|-----|------------------|------------------|
| 8 | 0.757 | **0.805** | 0.797 |
| 16 | 0.685 | **0.719** | 0.719 |
| 32 | 0.601 | **0.652** | 0.648 |
| 64 | 0.504 | **0.539** | 0.537 |
| 80 | 0.450 | **0.504** | 0.496 |

这确保两个模型在完全相同的 960 samples × 25 batches 上评估。差异幅度在 0.4-0.8pp，对结论方向无影响，但数据严谨性要求同批次比较。

---
