# analysis qwen seg spot fill

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_seg_spot_fill_20260515T110228_result.json`
- **Structured JSON:** [`bfe3c3e2268c819735aa.json`](../../sessions/bf/bfe3c3e2268c819735aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`segmentation_sensitivity.csv` 已合并为 24 行（DeepSeek 12 + Qwen 12），`segmentation_sensitivity.md` 已更新为双模型摘要。

关键结果：
- Qwen 全部 12 条件显著（Bonferroni 校正后 p < 4.2e-07）
- Qwen D 值系统性低于 DeepSeek 约 2-3 倍（与主 profiling 结果一致）
- 两个模型均保持剂量-响应关系：s015 < s020 < s025 < s030
- Qwen tercile n_eff=475/500（25 个问题 token 数不足以做 3-phase split）

---
