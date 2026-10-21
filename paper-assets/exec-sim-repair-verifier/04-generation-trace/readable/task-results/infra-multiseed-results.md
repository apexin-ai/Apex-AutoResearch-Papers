# infra multiseed results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_multiseed-results_20260512T031801_result.json`
- **Structured JSON:** [`528c157efaa3375a3e59.json`](../../sessions/52/528c157efaa3375a3e59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Let me compute statistics and report.

| Metric | Seed 42 | Seed 123 | Seed 456 | Mean | Std |
|--------|---------|----------|----------|------|-----|
| **overall_accuracy** | 87.83 | 89.52 | 87.88 | **88.41** | 0.96 |
| **pass_f1** | 88.06 | 89.64 | 87.53 | **88.41** | 1.10 |
| **fail_f1** | 87.59 | 89.40 | 88.21 | **88.40** | 0.92 |
| pass_precision | 89.45 | 91.76 | 93.60 | **91.60** | 2.08 |
| pass_recall | 86.71 | 87.63 | 82.21 | **85.52** | 2.90 |
| fail_precision | 86.20 | 87.34 | 83.12 | **85.55** | 2.18 |
| fail_recall | 89.04 | 91.56 | 93.97 | **91.52** | 2.47 |

**状态确认：**
- 3 seeds 训练全部正常完成（log EXIT_CODE=0，所有检查 PASS）
- 3 个 best checkpoint 目录完整（adapter_model.safetensors ~45MB each）
- GPU 空闲：0% 利用率，0 MiB 显存占用

**观察：**
- 3 seeds 的 accuracy 和 F1 一致性好，std < 1.1pp
- Seed 456 呈现明显的 precision-recall tradeoff 偏移：pass_precision 最高(93.60) 但 pass_recall 最低(82.21)，fail 方向相反
- Seed 123 整体最优（accuracy 89.52，两类 F1 均最高）
- Precision/recall 的 seed 间方差（std ~2-3pp）大于 F1 方差（~1pp），说明不同 seed 的决策边界位置有差异但整体判别力稳定

---
