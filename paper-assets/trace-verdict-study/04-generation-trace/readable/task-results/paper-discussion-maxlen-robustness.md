# paper discussion maxlen robustness

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_discussion_maxlen_robustness_20260516T024623_result.json`
- **Structured JSON:** [`008c6957c85b0c2953b3.json`](../../sessions/00/008c6957c85b0c2953b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。新小节 **"Sensitivity to Evaluation Context Length"** 插入在 Error Analysis 和 Limitations 之间（第 51–73 行），包含：

- **Full trace fragile**: 79.16% → 28.49%（100% 预测 fail），学到截断 artifact 而非 trace 语义
- **VOTA context-dependent**: 84.45%（长上下文）vs 16.0%（短上下文截断删除结构化后缀）
- **Exception-only robust**: 99.33% 不受 max_length 影响，输入天然短，无截断分布偏移
- 结论段：signal brevity → fewer failure modes，呼应核心论点

---
