# verify v5 r2 launch

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_v5-r2-launch_20260514T021118_result.json`
- **Structured JSON:** [`2e3f128805c835a27227.json`](../../sessions/2e/2e3f128805c835a27227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: s020_r2 / s030_r2 启动确认 ✓

| 项目 | s020_r2 | s030_r2 |
|------|---------|---------|
| tmux session | `mvp_v5_fixed_s020_r2` ✓ | `mvp_v5_fixed_s030_r2` ✓ |
| GPU | cuda:0, 23145 MiB, 77% util | cuda:1, 23145 MiB, 80% util |
| 进度 | 3/50 (processing problem 3) | 3/50 (processing problem 3) |
| NaN skip | `Skipped 1 NaN attention layers: [27]` ✓ 修复生效 | 同上 ✓ |

**注意**：原始 submit_training_job 失败原因是 `python: command not found`——没有激活 conda。已手动用 `source conda.sh && conda activate base` 重新启动。

---

### Part 2: s015 / s025 完整结果

两个实验均已完成（50 problems, 各 ~1356 segments）。

#### Phase 分布（两个实验共享，相同 model/data）

| Phase | n_tokens | n_segments |
|-------|----------|------------|
| high_sparsity | 25,862 | 511 |
| mid_sparsity | 27,996 | 391 |
| low_sparsity | 32,349 | 454 |

#### Perplexity

| Phase | Sparsity | dense | attn | kv | both |
|-------|----------|-------|------|------|------|
| **high_sparsity** | 0.15 | 1.1462 | 1.8077 | 1.2147 | 2.2835 |
| | 0.25 | 1.1462 | 2.0845 | 1.3108 | 3.4623 |
| **mid_sparsity** | 0.15 | 1.1226 | 1.6033 | 2.1276 | 3.9408 |
| | 0.25 | 1.1226 | 2.0249 | 6.1778 | 16.4148 |
| **low_sparsity** | 0.15 | 1.1105 | 1.5982 | 6.7451 | 16.9987 |
| | 0.25 | 1.1105 | 1.8101 | 23.8919 | 104.1749 |

#### Interaction Index (II)

| Phase | Sparsity | mean | median | winsorized_mean | CI [low, high] | skewness | outliers |
|-------|----------|------|--------|-----------------|----------------|----------|----------|
| **high_sparsity** | 0.15 | 0.306 | 0.205 | 0.289 | [0.256, 0.359] | 2.21 | 4 |
| | 0.25 | 0.851 | 0.584 | 0.802 | [0.703, 0.999] | 1.91 | 4 |
| **mid_sparsity** | 0.15 | 1.274 | 0.696 | 1.139 | [0.895, 1.749] | 4.20 | 2 |
| | 0.25 | 9.306 | 4.522 | 8.156 | [6.092, 13.303] | 3.05 | 2 |
| **low_sparsity** | 0.15 | 8.786 | 2.627 | 8.408 | [5.294, 12.684] | 2.32 | 1 |
| | 0.25 | 96.715 | 30.903 | 94.931 | [59.642, 143.188] | 1.48 | 0 |

#### Pass/Fail

| 实验 | ci_overlap_test | sign_reversal_test | overall |
|------|----------------|-------------------|---------|
| s015 | PASS (low vs mid non-overlapping) | FAIL (无 sign reversal) | **PASS** |
| s025 | PASS (low vs mid non-overlapping) | FAIL (无 sign reversal) | **PASS** |

#### 关键观察

- **Phase 梯度清晰**：II 值 high < mid < low，且三个 phase 的 bootstrap CI 完全不重叠，sparsity 越高差距越大
- **KV 主导交互**：low_sparsity phase 的 kv PPL 远高于 attn PPL（s025: kv=23.89 vs attn=1.81），说明 KV cache pruning 在低稀疏 phase 破坏性极强
- **非线性放大**：从 s015→s025，low_sparsity II 从 8.79 跳到 96.71（11x），而 high_sparsity 仅从 0.31 到 0.85（2.7x）
- **sign_reversal_test 均 FAIL**：各 phase 都没有出现 II < 0 的情况（即没有 sub-additive 交互），全部是 super-additive

---
