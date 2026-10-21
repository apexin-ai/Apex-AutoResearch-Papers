# analysis kill and pure rescore

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kill-and-pure-rescore_20260515T172357_result.json`
- **Structured JSON:** [`c32b64ed169aa4ac7369.json`](../../sessions/c3/c32b64ed169aa4ac7369.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**SC = SICA = 63.6% (7/11)**

| 关键发现 | 详情 |
|---------|------|
| P5 翻转成功 | sat_ratio=4.8%, A+C fallback → SC=80 → ✓（旧 SICA=120 已纠正）|
| P10 未翻转 | sat_ratio=30% > 20% 阈值, 维持 NORMAL 模式, 本身就正确 |
| P7 parser 异常 | 72 raw → 1 unique, 去重过度但碰巧结果正确 |
| 4 题失败 | P2/P8/P9/P11 全因 SC 无共识答案, 非 scorer 问题 |

**结论：当前 SICA 未超越 SC。A+C fallback 防止了 P5 退化，但瓶颈在 answer extraction / trace generation，不在约束评分。**

---
