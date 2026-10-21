# data comprehensive results update

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_comprehensive-results-update_20260515T081704_result.json`
- **Structured JSON:** [`3f880e25f466977896a0.json`](../../sessions/3f/3f880e25f466977896a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

新增内容：

1. **Section 4.5 扩展** — 8B s42 test@8192 完整 7 点 sweep（新增 ckpt-800/1000/1200/1400/1600），test-best 更新为 ckpt-1400 (85.47%, +12.51pp)，val-best 补入 ckpt-1000 (88.23%)，scaling gain 从 +2.44pp 修正为 +3.12pp

2. **Section 4.6 新增** — CLS 8B seed123 repo-level：val sweep 5 点（val-best ckpt-3000, 88.69%）+ test@8192 ckpt-3000 全量指标（85.60%, F1m=78.38%）

3. **Section 4.7 新增** — CLS 4B seed42 v5 extended eval：val ckpt-4600=90.07%（val-best），test ckpt-4600=83.63%

4. **Section 4.8 新增** — Multi-seed 8B repo-level 对比表（s42 vs seed123，含 CWM test 和 CLS−CWM gap ~26pp）

5. **Section 8 更新** — 3 条新 key findings（8B scaling gain、multi-seed、4B extended eval）

---
