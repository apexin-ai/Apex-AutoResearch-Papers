# analysis exp 046 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-046-results_20260519T011307_result.json`
- **Structured JSON:** [`1ec501103fe200a63f6c.json`](../../sessions/1e/1ec501103fe200a63f6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-046 分析完成。核心结论：

**SICA 在 ProofWriter-D5 上显著劣于 SC**：

| | SC | SICA | delta |
|--|-----|------|-------|
| Accuracy | 39.33% | 36.50% | **-2.83pp** (p=0.0095) |

McNemar 不对称：SC 在 30 个问题上赢 SICA，SICA 只在 13 个问题上赢 SC。

与 exp-033 (FOLIO) 对比，效果方向完全翻转：FOLIO 上 SICA +4.90pp，ProofWriter-D5 上 SICA -2.83pp。可能原因：ProofWriter-D5 的确定性规则推理链对 Mistral-7B 太难（两种方法都不到 40%），模型无法提取有效约束，SICA 的约束重加权反而放大了噪声。

报告已写入 `artifacts/exp046_analysis.md` 并注册 (`art_20260519_203d02`)。

---
