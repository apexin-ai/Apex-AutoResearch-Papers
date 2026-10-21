# analysis a1 bootstrap corrected

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a1_bootstrap_corrected_20260519T184730_result.json`
- **Structured JSON:** [`a8a68048244396b089ca.json`](../../sessions/a8/a8a68048244396b089ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 方法 | 95% CI |
|------|--------|
| Bootstrap-only (resample, no noise) | **[3.02, 20.10]** |
| Noise-propagated (resample + N(0, 0.88²)) | **[2.98, 20.08]** |

两组 CI 几乎相同——noise-propagated CI 仅比 bootstrap-only 宽约 0.04–0.06 pp。这是因为 FP8 noise σ=0.88 pp 远小于 batch 间的 sampling variance（high-BCS 组标准差 ~10 pp），噪声贡献被 resample variance 淹没了。

两组 CI 下界均 >0，delta=10.94 pp 在两种方法下都显著排除零。

---
