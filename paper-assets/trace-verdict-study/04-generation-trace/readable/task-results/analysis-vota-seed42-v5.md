# analysis vota seed42 v5

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vota_seed42_v5_20260515T041020_result.json`
- **Structured JSON:** [`eace17c5b16bd2488df8.json`](../../sessions/ea/eace17c5b16bd2488df8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。下面是完整结果。

---

## vota_seed42_v5 实验结果

**Conclusion: SUCCESS** | MVP VERDICT: PASS

### 核心指标

| 指标 | 值 |
|------|------|
| accuracy | **99.41%** [98.9%, 99.8%] |
| majority_baseline | 71.51% |
| lift (vs majority) | +27.9pp |
| lift_vs_notrace | **+24.3pp** [+21.8, +26.8]pp |
| n | 1190 |

### Per-class

| | Precision | Recall | F1 |
|------|------|------|------|
| pass | 1.000 | 0.992 | 0.996 |
| fail | 0.980 | 1.000 | 0.990 |

### 训练指标

| 指标 | 值 |
|------|------|
| train_loss | 0.050 |
| eval_loss | 0.087 |
| eval_mean_token_accuracy | 0.983 |
| wall_clock | 8443s (2h21m) |

### 对比分析

| 对比 | 差异 | 95% CI | 显著性 |
|------|------|------|------|
| **vs no_trace (v4)** | +24.3pp (75.1% → 99.4%) | [+21.8, +26.8]pp | *** |
| **vs full_trace (v5)** | +17.7pp (81.8% → 99.4%) | [+15.5, +19.8]pp | *** |
| **vs vota v4** | +3.8pp (95.6% → 99.4%) | — | v5 提升明显 |

**关键发现：**
- v5 VOTA 从 v4 的 95.6% 提升到 99.4%，修复 chat template overhead 后效果显著
- VOTA 的 fail recall 从 v4 的 85.3% 跃升至 100%（所有 fail 样本都被正确识别）
- pass precision 达到 100%（无 false positive）
- VOTA >> full_trace (+17.7pp)，证明 trace 压缩（只保留 assertion snapshots）优于完整 trace

---
