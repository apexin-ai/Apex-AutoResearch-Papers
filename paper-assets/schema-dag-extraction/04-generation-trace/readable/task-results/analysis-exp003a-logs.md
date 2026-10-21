# analysis exp003a logs

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp003a_logs_20260515T050603_result.json`
- **Structured JSON:** [`29a56434d3a5bef7d89c.json`](../../sessions/29/29a56434d3a5bef7d89c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结如下：

## exp003a_prompt_v2_rerun 分析结果

**状态**: 两个 mode (exp1 + exp2) 均成功完成。首次运行因 script path 错误失败，retry 修复后正常。

**V2 vs V1 (exp001) text_match 对比**:

| count | v1 F1 | v2 F1 | delta | v1 pred/gold | v2 pred/gold |
|-------|-------|-------|-------|-------------|-------------|
| 1     | 0.184 | **0.323** | **+76%** | 6.85 | 2.97 |
| 6     | 0.155 | **0.306** | **+97%** | 7.02 | 2.10 |
| 12    | 0.246 | **0.347** | **+41%** | 3.38 | 0.90 |
| 22    | 0.322 | 0.299 | -7%  | 2.27 | 0.79 |
| 44    | 0.473 | 0.445 | -6%  | 1.33 | 0.78 |
| 64    | 0.463 | 0.414 | -11% | 0.80 | 0.47 |

**核心发现**: Prompt v2 成功解决了 over-prediction 问题（count_1 pred/gold 从 6.85x 降至 2.97x），precision 全面提升（+22%~+157%），低 count 段 F1 大幅改善。但矫枉过正：高 count 段出现 under-prediction（pred/gold<1），recall 下降 27-39%，F1 微降。整体判定 **partial success** —— v2 作为 over-prediction 的修复有效，但需要进一步调优以平衡高 count 段的 recall。

---
