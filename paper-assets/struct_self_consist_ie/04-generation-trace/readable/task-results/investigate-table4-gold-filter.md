# investigate table4 gold filter

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_table4_gold_filter_20260516T033256_result.json`
- **Structured JSON:** [`411fcc62e24ef6c0d0ff.json`](../../sessions/41/411fcc62e24ef6c0d0ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。结论：

## 审计结果：**filtering 一致，无需修正**

**Hypothesis A 正确**：
- `_full` = gold-filtered (排除 697 个 gold-empty instances)，**n=2756**
- `_conditional` = gold-filtered + 排除 greedy-F1=0，4B n=2641，8B n=2676

**关键证据**：
1. `report.json` 中 `correlation_softjaccard_vs_f1_full` 明确记录 `"n": 2756`，而非 3453
2. `run_mvp_pilot.py` 源码注释：`# Full ρ: on gold-nonempty instances`
3. 4B 和 8B 都由同一个 `run_mvp_pilot.py` pipeline 生成，filtering 逻辑完全一致

**数值对照**：

| | SJ ρ | FK ρ | n | filtering |
|---|---|---|---|---|
| Table 1 (8B) | .436 | .400 | 2756 | gold-filtered |
| Table 4 (4B) | .422 | .418 | 2756 | gold-filtered |

`n_instances: 3453` 是原始数据集大小的元数据，不参与 ρ 计算。`_full` 后缀命名易误导，但实际值无误。

已将审计结论写入 registry notes 和 `output/review_round9_experiments/table4_gold_filter_audit.json`。

---
