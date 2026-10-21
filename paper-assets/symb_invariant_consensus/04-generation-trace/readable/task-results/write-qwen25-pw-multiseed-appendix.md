# write qwen25 pw multiseed appendix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_qwen25-pw-multiseed-appendix_20260524T062045_result.json`
- **Structured JSON:** [`4292ff530abb62aaf64a.json`](../../sessions/42/4292ff530abb62aaf64a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。修改清单：

**数据来源**：
- seed42: Table 1 canonical (SC=74.00, SICA=71.50)
- seed123: results.json SC=72.33, SICA 修正为 70.83 (原 71.17)
- seed456: results.json SC=73.00, SICA=72.17
- seed789: results.json SC=73.50, SICA=71.50

**appendix.tex 修改**：
1. **L1376 caption**: "four" → "five", 删除 "Qwen3-14B results pending."
2. **L1413–1420 新增行**: Qwen2.5-14B × PW 4 seeds + Mean±SD (SC 73.21±0.71, SICA 71.50±0.55, Δ -1.71±0.71)
3. **L1427 summary**: "eight" → "twelve", 范围下界 -1.33 → -0.83, 新增 Qwen2.5-14B 描述句

编译通过，无 undefined references。

---
