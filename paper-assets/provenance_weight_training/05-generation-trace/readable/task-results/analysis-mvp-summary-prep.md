# analysis mvp summary prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp-summary-prep_20260514T233059_result.json`
- **Structured JSON:** [`6eba3fac1ea5777fcc43.json`](../../sessions/6e/6eba3fac1ea5777fcc43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已保存并注册（`art_20260514_ce7251`）。

Registry 验证结果：所有数字与提供值一致。

**MVP 判定：PASS**
- seed42: 102.6%, seed123: 90.4%, aggregate: 95.6%（均 ≥ 90% 阈值）
- adaptive_fix 在零超参调优下达到 grid-best 95.6% 的改善量

主要风险：best-b=0.5 在搜索边界，扩展至 b<0.5 可能拉低 ratio；约 60% batch 的 b*≈0，改善主要靠少数高污染 batch 的选择性降权。seed456 grid 完成后需更新。

---
