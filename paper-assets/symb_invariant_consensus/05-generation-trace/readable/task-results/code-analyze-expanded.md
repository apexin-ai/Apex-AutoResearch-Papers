# code analyze expanded

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze-expanded_20260516T080105_result.json`
- **Structured JSON:** [`3b9c83ea2839cd35705a.json`](../../sessions/3b/3b9c83ea2839cd35705a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署并验证通过。当前157题（全部proofwriter，FOLIO还没进来）的快照：

```
| Dataset     |   N | C0%  | SICA Acc | SC Acc  | Δ (pp) | McNemar p |
|-------------|-----|------|----------|---------|--------|-----------|
| proofwriter | 157 | 40.1 |  75.80%  |  77.07% | -1.27  | 0.7266    |
```

- SC ties: 8 (5.1%), SICA tie-acc: 50.0%
- D012 对比：tie率从8.3%降到5.1%，tie-acc从80%降到50%
- JSON详细结果已保存到 `results/analysis_expanded.json`

产出文件：`/root/symb_invariant_consensus/scripts/analyze_expanded.py`，`--help` 和实际运行均正常。804题跑完后直接执行即可出报告。

---
