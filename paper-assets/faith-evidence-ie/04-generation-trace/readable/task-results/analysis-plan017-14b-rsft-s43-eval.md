# analysis plan017 14b rsft s43 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan017_14b_rsft_s43_eval_20260523T204723_result.json`
- **Structured JSON:** [`43c4d06c5563da3fe76e.json`](../../sessions/43/43c4d06c5563da3fe76e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

**plan017_14b_rsft_s43_eval** — Ign-F1 = **0.5815**

| 对比项 | 值 |
|--------|------|
| s43 dev with-evi | 0.5815 |
| s42 dev with-evi | 0.5886 |
| **Seed 间差异** | **−0.71pp** |
| s43 dev no-evi | 0.5713 |
| **s43 dev evidence tax** | **−1.02pp**（evidence 有帮助） |
| s42 dev evidence tax | −4.54pp |

关键发现：
1. **两 seed 可复现性合理**，差 0.71pp
2. **s43 dev evidence tax (−1.02pp) 远小于 s42 (−4.54pp)**，因为 s43 no-evi 模型本身更强（0.5713 vs 0.5432）
3. **Dev→Test tax 方向翻转**在两个 seed 上一致出现（dev: evidence 有帮助；test: 中性/微负），确认是系统性模式而非 seed 噪声

Registry 已更新为 DONE(success)，分析报告已注册。

---
