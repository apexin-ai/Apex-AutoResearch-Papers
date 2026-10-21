# code block corr fix v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_block-corr-fix-v2_20260512T090020_result.json`
- **Structured JSON:** [`7b1d38d77bd0b127b710.json`](../../sessions/7b/7b1d38d77bd0b127b710.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. Per-sample predictions
之前不存在。修改 eval_verifier.py 添加了 `--save_predictions` 选项，用 GPU 2 重跑了 bfloat16 推理，生成 `eval_results_bf16_predictions.json`（1890 samples）。

### 2. 采用方案
修改 eval_verifier.py + 写纯 CPU 分析脚本 `block_corr_from_predictions.py`，用 GPU 2 跑推理后立即跑 CPU 分析。

### 3. v1 (4-bit) vs v2 (bf16) 对比

| 指标 | v1 (4-bit) | v2 (bf16) | 变化 |
|------|-----------|----------|------|
| **accuracy** | 85.93% | **87.51%** | +1.58pp ✓ |
| **ICC** | 0.2329 | **0.1909** | -0.042 |
| **DEFF** | 4.6197 | **3.9676** | -0.65 |
| all_correct observed | 46 | 46 | 不变 |
| all_correct expected (i.i.d.) | 12.76 | 16.35 | +3.59 |
| **all_correct ratio** | 3.60x | **2.81x** | -0.79x |
| error_std | 0.1747 | 0.1531 | -0.022 |
| **error_std ratio** | 2.05x | **1.89x** | -0.16x |

### 4. 结论
- accuracy 偏差已消除（87.51% = 主评估结果）
- Block-correlation 结论不变：**ICC=0.19, p<0.0001, 高度显著**
- 4-bit 量化人为放大了 block-correlation 表观强度（DEFF 4.62→3.97），因为量化误差本身也是 block-correlated 的
- 修正后 DEFF=3.97 仍意味着有效独立样本量约为名义的 1/4

---
