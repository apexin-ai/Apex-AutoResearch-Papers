# code r9 r1 8b fpr 5seed pvalues

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r9_r1_8b_fpr_5seed_pvalues_20260518T081612_result.json`
- **Structured JSON:** [`8c075c21981ff0e0ad30.json`](../../sessions/8c/8c075c21981ff0e0ad30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
R1-8B FPR 5-seed Bootstrap p-values:
| Seed | HS FPR | Text FPR | Δ FPR   | p-value | HB pass (0.0125)? |
|------|--------|----------|---------|---------|-------------------|
| 0    | 0.1611 | 0.1649   | -0.0038 | 0.4400  | NO                |
| 1    | 0.0614 | 0.1659   | -0.1045 | 0.0000  | YES               |
| 2    | 0.1230 | 0.1764   | -0.0534 | 0.0930  | NO                |
| 3    | 0.1484 | 0.1666   | -0.0182 | 0.2930  | NO                |
| 4    | 0.1001 | 0.1760   | -0.0759 | 0.0210  | NO                |

Seeds passing HB: 1/5
```

HS FPR 方向一致（所有 seed 都 HS ≤ text），但统计显著性非常不稳定。只有 seed 1 通过 HB 校正阈值 0.0125，seed 4 的 p=0.021 接近但未通过，其余 3 个 seed p-value 远高于 0.05。seed 0 差异几乎为零 (Δ=-0.004)。

结论：R1-8B FPR 的 HS-vs-text 优势**跨 seed 不稳定**，原始 seed=42 的 p=0.044 属于偏乐观的 split。

已保存至 `artifacts/exp_r9_r1_8b_fpr_seed_pvalues/results.json`。

---
