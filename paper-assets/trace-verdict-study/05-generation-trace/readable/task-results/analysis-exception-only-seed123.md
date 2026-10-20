# analysis exception only seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exception_only_seed123_20260515T180236_result.json`
- **Structured JSON:** [`51ef01b8aed69657e915.json`](../../sessions/51/51ef01b8aed69657e915.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

**exception_only_seed123 结果摘要：**

| Seed | Accuracy | Errors |
|------|----------|--------|
| 42   | 99.83%   | 2/1190 |
| 456  | 99.83%   | 2/1190 |
| 123  | 99.83%   | 2/1190 |

- **max_diff = 0**，三个 seed 精确到小数点后四位完全一致
- 95% CI: [99.58%, 100.0%]
- Seed robustness **confirmed**：exception_only 在 3 个 seed 上结果完全稳定，每个 seed 恰好 2/1190 错误，极大概率是同一组 irreducible 样本。

---
