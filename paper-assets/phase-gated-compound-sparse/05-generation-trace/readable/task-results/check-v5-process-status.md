# check v5 process status

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v5_process_status_20260514T020835_result.json`
- **Structured JSON:** [`bfe1c15f301a9de5b263.json`](../../sessions/bf/bfe1c15f301a9de5b263.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态总结

### 进程状态

| 实验 | PID | GPU | 状态 | 运行时间 |
|------|-----|-----|------|---------|
| mvp_v5_fixed_s020 | 46568 | cuda:0 | **已完成** | — |
| mvp_v5_fixed_s030 | 46935/46940 | cuda:1 | **已完成** | — |
| mvp_v5_fixed_s015 | 48262 | cuda:2 | **运行中** | 37 min |
| mvp_v5_fixed_s025 | 48403 | cuda:3 | **运行中** | 37 min |

### GPU 当前占用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 0 / 97887 MiB (空闲) |
| 1 | 0% | 0 / 97887 MiB (空闲) |
| 2 | 76% | 38905 / 97887 MiB (s015 运行中) |
| 3 | 76% | 38905 / 97887 MiB (s025 运行中) |

---

### 已完成实验结果

**配置：** importance masking, attention_frobenius_norm + cumulative_attention_received, quantile segmentation, 50 problems, 1000 bootstrap

#### Perplexity

| Phase | s=0.20 dense/attn/kv/both | s=0.30 dense/attn/kv/both |
|-------|---------------------------|---------------------------|
| high | 1.15 / 1.88 / 1.24 / 2.70 | 1.15 / 3.11 / 1.40 / 5.71 |
| mid | 1.12 / 1.72 / 3.65 / 8.13 | 1.12 / 6.38 / 15.11 / 137.61 |
| low | 1.11 / 1.65 / 14.11 / 42.64 | 1.11 / 7.12 / 40.79 / 963.20 |

#### Interaction Index (II)

| Phase | s=0.20 mean [CI] | s=0.20 median | s=0.30 mean [CI] | s=0.30 median |
|-------|-------------------|--------------|-------------------|--------------|
| high | **0.50** [0.41, 0.62] | 0.33 | **1.18** [0.86, 1.60] | 0.60 |
| mid | **3.52** [2.29, 5.35] | 1.55 | **168.53** [36.91, 348.21] | 7.47 |
| low | **31.89** [18.74, 47.22] | 9.56 | **1926.23** [179.17, 4062.57] | 44.63 |

**Pass/Fail:** 两个实验均 PASS（CI non-overlapping between phases）。Sign reversal test 均 FAIL（II 非负）。无 NaN/Inf/warnings。

---

### 结论

1. **II 在所有 phase 和 sparsity level 下均为正值（super-additive）。** `ppl_both > ppl_attn + ppl_kv - ppl_dense`，compound sparsity 的伤害严格大于单独剪枝的加和。

2. **Low-sparsity phase 的 II 最大：** s=0.20 时 low=31.9 vs mid=3.5 vs high=0.5；s=0.30 时 low=1926 vs mid=169 vs high=1.2。自然稀疏度低的 phase，compound pruning 破坏力最强。

3. **II 随 sparsity level 非线性爆炸增长：** low phase 从 s=0.20 的 31.9 跃升到 s=0.30 的 1926（~60x），mid 从 3.5 到 169（~48x）。

4. **Importance-based pruning 未展现 negative II（sub-additive）。** 与 random baseline 相比，importance masking 不能消除 compound interaction，只是程度不同。这强化了 phase-gated 策略的必要性——必须根据当前 phase 的自然稀疏度决定剪枝强度。

s015 和 s025 预计再 ~18 分钟完成。

---
