# ssh lm eval downstream 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_lm_eval_downstream_41312_20260517T230239_result.json`
- **Structured JSON:** [`7ec3355cc9ed592f0fb6.json`](../../sessions/7e/7ec3355cc9ed592f0fb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型评估均已完成。汇总结果：

| Benchmark | Metric | adaptive_fix_seed42 | uniform_seed42 | Δ |
|-----------|--------|--------------------:|---------------:|---:|
| arc_challenge | acc | 0.3174 | 0.3208 | -0.0034 |
| arc_challenge | acc_norm | 0.3430 | 0.3481 | -0.0051 |
| arc_easy | acc | 0.6503 | 0.6574 | -0.0071 |
| arc_easy | acc_norm | 0.6157 | 0.6128 | +0.0029 |
| hellaswag | acc | 0.3785 | 0.3805 | -0.0020 |
| hellaswag | acc_norm | 0.4785 | 0.4836 | -0.0051 |
| piqa | acc | 0.6872 | 0.6861 | +0.0011 |
| piqa | acc_norm | 0.6866 | 0.6877 | -0.0011 |
| winogrande | acc | 0.5777 | 0.5856 | -0.0079 |

两个模型在 5 个 benchmark 上表现非常接近（差异均在 stderr 范围内）。uniform_seed42 在大多数指标上略高（平均 Δ ≈ -0.003），但差异不具统计显著性。

结果已保存在服务器上：
- `/root/autodl-tmp/provenance_weight_training/output/lm_eval/adaptive_fix_seed42/`
- `/root/autodl-tmp/provenance_weight_training/output/lm_eval/qwen06b_uniform_seed42/`

---
