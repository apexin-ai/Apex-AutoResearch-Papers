# code kl divergence run

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kl-divergence-run_20260519T200627_result.json`
- **Structured JSON:** [`5a6d5af8d78e82b64542.json`](../../sessions/5a/5a6d5af8d78e82b64542.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

KL divergence 脚本运行完成。结果如下：

## Aggregate 统计（Layer 18, 20 tasks × 5 paraphrases = 100 comparisons）

| 指标 | 值 |
|------|-----|
| **Mean KL** | **6.968e-05** |
| **Std KL** | 2.647e-05 |
| **Median KL** | 6.507e-05 |
| **Min KL** | 2.697e-05 |
| **Max KL** | 1.506e-04 |

## Per-task Mean KL

| Task | Mean KL | Std KL |
|------|---------|--------|
| libero_spatial_8 | 9.580e-05 | 3.051e-05 |
| libero_spatial_6 | 8.875e-05 | 3.153e-05 |
| libero_goal_2 | 8.255e-05 | 8.266e-06 |
| libero_spatial_7 | 8.053e-05 | 2.329e-05 |
| libero_90_89 | 8.049e-05 | 2.163e-05 |
| libero_90_22 | 7.992e-05 | 2.013e-05 |
| libero_90_17 | 7.700e-05 | 2.185e-05 |
| libero_90_15 | 7.696e-05 | 4.155e-05 |
| libero_90_74 | 7.614e-05 | 2.643e-05 |
| libero_90_30 | 7.196e-05 | 2.926e-05 |
| libero_90_16 | 7.072e-05 | 1.539e-05 |
| libero_goal_8 | 6.950e-05 | 3.066e-05 |
| libero_90_67 | 6.671e-05 | 6.654e-06 |
| libero_goal_3 | 6.160e-05 | 2.331e-05 |
| libero_90_10 | 6.039e-05 | 2.193e-05 |
| libero_goal_6 | 5.674e-05 | 1.221e-05 |
| libero_90_19 | 5.503e-05 | 8.534e-06 |
| libero_90_68 | 5.109e-05 | 1.617e-05 |
| libero_90_31 | 4.785e-05 | 1.319e-05 |
| libero_10_5 | 4.381e-05 | 1.421e-05 |

## 结论

所有 KL divergence 值极小（~10⁻⁵ 量级），说明 Layer 18 的注意力分布对指令 paraphrase 高度不变——paraphrase 几乎不改变内部表征。

**结果文件**: `/root/afford_invar/results/phase0/kl_divergence.json`（137KB，含 per-head 细节）

**GPU**: 4×L20（96GB each），模型已卸载，当前 GPU 空闲。运行约 30 秒完成。

---
