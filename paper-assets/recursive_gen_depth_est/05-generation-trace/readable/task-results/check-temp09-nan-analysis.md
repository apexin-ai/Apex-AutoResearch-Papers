# check temp09 nan analysis

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_temp09_nan_analysis_20260520T042400_result.json`
- **Structured JSON:** [`6f7564e72ac481af2ebe.json`](../../sessions/6f/6f7564e72ac481af2ebe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **Total**: 20,000 samples
- **NaN**: 仅 1 个样本（Line 7160, depth=1），skew_ppl 和 kurt_ppl 同时为 NaN
- **Inf**: 无
- **影响**: 0.005%，可忽略。catastrophic cancellation 仅因该样本 token-level PPL 方差极小导致高阶矩计算不稳定，不影响整体实验结论

已追加到 `qwen25_14b_temp09_analysis.md` 的 Notes 部分。

---
