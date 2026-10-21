# diagnose exp 008 re seed123

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_008_re_seed123_20260514T152030_result.json`
- **Structured JSON:** [`36e8e301addff950bfe7.json`](../../sessions/36/36e8e301addff950bfe7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：negative（正常完成但未达标）**

实验 551 个 RE 实例全部处理完毕，关键指标：
- Greedy F1 = 0.4229，Oracle F1 = 0.6244（headroom +0.2015）
- 44.1% 样本 F1=0（过高）
- Structural > Surface = NO（κ 相关性不如 Soft Jaccard）
- Verdict = FAIL

Registry 已更新为 DONE/negative，metrics 已写入。CRON 监控不存在（可能已被其他流程清除）。

---
