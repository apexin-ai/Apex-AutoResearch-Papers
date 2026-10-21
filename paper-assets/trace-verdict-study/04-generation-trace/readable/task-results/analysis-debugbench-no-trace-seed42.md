# analysis debugbench no trace seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_debugbench_no_trace_seed42_20260516T011024_result.json`
- **Structured JSON:** [`3b0706930ba77f8f4d21.json`](../../sessions/3b/3b0706930ba77f8f4d21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。实验结果汇总：

## debugbench_no_trace_seed42 — SUCCESS

| Condition | Accuracy | Pass F1 | Fail F1 |
|-----------|----------|---------|---------|
| **no_trace** | **96.71%** | 0.967 | 0.967 |
| vota | 99.77% | 0.998 | 0.998 |

**关键发现**：
- no_trace baseline 准确率 96.7%（CI: [94.8%, 98.4%]），fine-tuned 7B 模型仅凭代码即可高效判断 bug
- VOTA（含 trace）比 no_trace 高 +3.06pp，CI 不重叠，差异统计显著
- trace 增益主要体现在 pass_recall（0.936 → 0.995）——trace 帮助模型正确识别"代码无 bug"的情况
- 模型在 no_trace 条件下偏向预测 fail（fail_recall=1.0），加入 trace 后偏向消除

Registry 已更新为 DONE/success，分析报告已注册为 artifact。

---
