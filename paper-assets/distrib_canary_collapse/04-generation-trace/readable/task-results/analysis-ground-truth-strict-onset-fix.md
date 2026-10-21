# analysis ground truth strict onset fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ground_truth_strict_onset_fix_20260516T065519_result.json`
- **Structured JSON:** [`3310044ef552bf64af43.json`](../../sessions/33/3310044ef552bf64af43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**严格不等式修复验证全部通过：**

| 验证项 | 结果 |
|--------|------|
| canary onset (token_entropy, ece) | gen 1 ✓ |
| perplexity onset | gen 1（与 canary 相同）✓ |
| distinct_1/2/3 onset | gen 9/3/3（晚于 canary）✓ |
| 严格 `<` 排除 →perplexity | 2 pairs 排除 ✓ |
| 新参考集 | 6 pairs（全部 canary→distinct_*）✓ |
| FNR | 0%（6/6 全部 4/4 检出）✓ |
| 阈值敏感性 2×/3×/5× | 完全一致，均为 6 pairs ✓ |

Artifact 已注册：`art_20260516_091a25`，报告位于 `artifacts/_project/report/ground_truth_redefine_v2_analysis.md`，JSON 数据在服务器 `artifacts/ground_truth_redefine_v2_results.json`。

---
