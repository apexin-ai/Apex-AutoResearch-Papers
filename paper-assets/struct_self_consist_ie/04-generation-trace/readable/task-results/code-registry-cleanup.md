# code registry cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_registry_cleanup_20260518T215719_result.json`
- **Structured JSON:** [`484083201913a552c78b.json`](../../sessions/48/484083201913a552c78b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

后台 agent 完成，9 个温度消融多 seed 实验全部注册成功。

**最终汇总**:

| 操作 | 数量 |
|---|---|
| degen_rate_source 新增标注 | 2 (exp_029a, exp_029b) |
| degen_rate 值需修正 | 0 |
| 新注册实验 | **13** (4 CoNLL/FewNERD 多 seed + 9 温度消融多 seed) |
| 仍有旧 sample_f1_pct_zero 残留 | 2 (exp_003_ner_wnut17, exp_003_wnut17_eval — WNUT17 无 unified audit) |
| 待决定是否注册 | 8 (N=8 CoNLL, FewNERD seed789 分片, rank8, scale 等) |

---
