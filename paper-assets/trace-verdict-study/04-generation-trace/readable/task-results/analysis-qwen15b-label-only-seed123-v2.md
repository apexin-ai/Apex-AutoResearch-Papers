# analysis qwen15b label only seed123 v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708_result.json`
- **Structured JSON:** [`91e48442b01595faed3a.json`](../../sessions/91/91e48442b01595faed3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：qwen15b_label_only_seed123_v2 — **SUCCESS**

### Metrics

| 指标 | 值 |
|------|-----|
| **Accuracy** | **81.34%** (95% CI: [79.24%, 83.45%]) |
| Majority baseline | 71.51% |
| **Lift over majority** | **+9.83pp** (CI: [+7.56pp, +12.18pp]) |
| Pass P / R / F1 | 0.824 / 0.940 / 0.878 |
| Fail P / R / F1 | 0.767 / 0.496 / 0.602 |

### 对比分析

| 对比 | seed42 | seed123 | 差异 |
|------|--------|---------|------|
| Accuracy | 78.9% | 81.3% | +2.4pp |
| vs no_trace (67.31%) | +11.6pp | +14.0pp | — |

- **跨 seed 稳定性**：seed123 (81.3%) 在 seed42 (78.9%) 的 ±5pp 范围内，CI 重叠，确认跨 seed 稳定
- **label_only lift 确认**：两个 seed 平均 lift = +12.8pp (vs no_trace 67.31%)，略高于假设的 ~11pp，label formatting 贡献稳健
- **Conclusion**: success — C2 decomposition 跨 seed 稳定性得到验证

### Registry 已更新
- status: DONE, conclusion: success
- checkpoint: `/root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final`

---
