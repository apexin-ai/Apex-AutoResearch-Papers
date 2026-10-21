# analysis sica d012 14b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sica_d012_14b_20260516T050551_result.json`
- **Structured JSON:** [`d1e4a76c7b437ba036e6.json`](../../sessions/d1/d1e4a76c7b437ba036e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。实验 registry 已更新为 DONE/success。

---

## 结果摘要

**D012 判定: ALL PASS** ✓

| 指标 | 值 | 阈值 | 判定 |
|------|-----|------|------|
| C0 多候选率 | 53.3% (32/60) | ≥20% | PASS |
| C1 约束提取率 | 100.0% (720/720) | ≥50% | PASS |
| C2 矛盾检出 | 34 题 | ≥5 | PASS |
| C3 SICA-SC gap | +3.3pp (73.3% vs 70.0%) | ≥+2pp | PASS |

**分域**: FOLIO 贡献全部优势 (SICA 80.0% vs SC 73.3%, +6.7pp)，ProofWriter 持平 (66.7% vs 66.7%)。

**机制**: 4 题差异全部来自 6:6 投票平局，SICA 通过约束加权 3/4 次正确打破平局。Bootstrap p=0.226 未达统计显著性，但 +2pp 的数值阈值已满足。

报告已注册: `art_20260516_951d6a`

---
