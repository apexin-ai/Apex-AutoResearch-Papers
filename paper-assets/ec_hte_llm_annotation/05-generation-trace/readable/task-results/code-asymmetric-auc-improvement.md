# code asymmetric auc improvement

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_asymmetric-auc-improvement_20260525T050424_result.json`
- **Structured JSON:** [`ab62d1da00cd9a4c2cfe.json`](../../sessions/ab/ab62d1da00cd9a4c2cfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

分析完成，结论与最初假设相反：

### 核心发现

| 诊断指标 | Per-config AUC (MC) | Pooled AUC (MC) | 解析 AUC |
|---------|--------------------|--------------------|---------|
| **Scalar (Prop 5)** | **0.97** | **0.96** | **1.00** |
| Matrix-raw (max \|B_s\|) | 0.68 | 0.86 | 0.98 |
| Matrix-ratio (\|B_s\|/\|D_s\|) | **1.00** | — | **1.00** |

### 关键结论

1. **此前报告的 AUC≈0.66 来自未归一化的 raw matrix score**（max |B_s[z,1]|），而非标量公式的退化。标量公式实际 AUC = 0.97。

2. **Raw matrix score 性能更差**，因为它测量绝对偏差放大而不归一化 naive bias |D_s|。大 pi_s 的 subgroup 同时有大 |B_s| 和大 |D_s|，但 ratio 可能 < 1（GC 有帮助）。

3. **标量公式在非对称误差下仍然有效**——threshold `score > 1` 等价于 `|B_s|/|D_s| > 1`，只要 subgroup 之间 pi_s 不同（delta_s ≠ 0）就成立，与 FPR/FNR 非对称性无关。

4. **Stress test**：当所有 subgroup 的 pi_s 完全相同（delta_s = 0）且 P(Z) 极端偏斜时，标量公式失效（AUC = 0.57），ratio-normalized matrix 仍为 1.00。但这种配置在实际 LLM 中不会出现。

**建议**：保持 Proposition 5 的标量诊断不变。B_s 矩阵对 EC-HTE 校正方法至关重要，但对诊断筛选不需要替换标量公式。

报告已写入 `artifacts/asymmetric_auc_report.md`。

---
