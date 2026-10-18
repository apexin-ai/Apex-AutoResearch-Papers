# mvp nli count and sync

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_mvp_nli_count_and_sync_20260520T142108_result.json`
- **Structured JSON:** [`a85d110ae6415a07c58e.json`](../../sessions/a8/a85d110ae6415a07c58e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## NLI 统计结果

| 阈值 | 通过数 | 比例 |
|------|--------|------|
| NLI ≥ 0.85 | 95/100 | 95.0% |
| NLI ≥ 0.88 | 95/100 | 95.0% |
| **NLI ≥ 0.90** | **95/100** | **95.0%** |
| NLI ≥ 0.92 | 93/100 | 93.0% |
| NLI ≥ 0.95 | 90/100 | 90.0% |

**PRIMARY gate (NLI ≥ 0.90): 95/100**，其中 formal 59 条、casual 36 条。

NLI_cf 均值 0.9422 (std=0.2032)，BERTScore_cf 均值 0.8932 (std=0.0730)。

## 代码同步确认

- `judge_scoring.py` — 已同步，无 `passed_cf` 过滤（grep 返回 0 匹配）
- `ate_analysis.py` — 已同步，含 `primary: nli_cf≥0.90` 分层分析逻辑

---
