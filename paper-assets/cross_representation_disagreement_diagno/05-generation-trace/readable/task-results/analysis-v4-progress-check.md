# analysis v4 progress check

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4_progress_check_20260514T142258_result.json`
- **Structured JSON:** [`29d1f0bd628691a3c28b.json`](../../sessions/29/29d1f0bd628691a3c28b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## V4 Pipeline 中间结果摘要 (79/204)

**进度**：79/204 (38.7%)，已运行 3h21m，约 5.4h 后完成（~明晨 03:40）

**C 指标全部达标**：

| 指标 | 值 | 阈值 | 状态 |
|------|-----|------|------|
| C1 Disagree rate | 31.1% | ≥10% | ✅ |
| C2 One-side correct | 87.0% | ≥40% | ✅ |
| C3 Targeted > blind | +36.3pp | +5pp | ✅ |
| C4 Localization (FOL wins) | 78.3% | ≥60% | ✅ |

**关键发现**：
- **Code Unknown 36.7%**，较上次 46.3% 显著下降，v4 truncation fix 有效
- **FOL 压倒性优势**：disagree 中 FOL 正确 78.3% vs Code 仅 8.7%
- **Targeted repair code 成功率 81.8%**，远超 blind 45.5%
- FOL accuracy 81.0% vs Code 63.3%，差距 17.7pp
- agree_wrong 6 例 (7.6%) 是 disagreement 方法的盲区

样本量 79 置信度中等，需完整 204 确认。report.md 已更新。

---
