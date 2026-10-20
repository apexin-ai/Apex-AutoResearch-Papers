# analysis full trace seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_full_trace_seed123_20260523T041603_result.json`
- **Structured JSON:** [`dd8490662023be9c4b67.json`](../../sessions/dd/dd8490662023be9c4b67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**full_trace_seed123 分析结果：**

| 指标 | seed123 | seed42 | Delta |
|------|---------|--------|-------|
| Accuracy | 79.58% | 81.76% | -2.18pp |
| Fail F1 | 0.6620 | 0.6851 | -0.0231 |
| Lift | +8.07pp | +10.25pp | -2.18pp |
| 95% CI | [77.1%, 82.0%] | — | — |

**Conclusion: SUCCESS** — accuracy 差值 -2.18pp 在 ±3pp 阈值内，seed42 的 81.76% 落在 seed123 的 95% CI [77.1%, 82.0%] 内，两个 seed 统计一致。

已完成：
1. 运行分类评估（evaluate.py）并提取指标
2. Registry 更新为 DONE/success，含完整 metrics
3. 分析报告写入 artifacts 并注册（art_20260523_f72a14）

---
