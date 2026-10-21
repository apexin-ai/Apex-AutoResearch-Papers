# analysis r13 oracle gap multimodel

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r13_oracle_gap_multimodel_20260518T143927_result.json`
- **Structured JSON:** [`44d763fbef277232ef95.json`](../../sessions/44/44d763fbef277232ef95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The oracle script uses `prepare_dataset()` which only loads the default dataset (R1-8B). It's hardcoded — no model parameter. No oracle results exist for other models.

**结论：其他 3 模型（OT-7B, R1-32B, QwQ-32B）无现成 oracle gap 数据。**

- `d4_oracle.log` 仅包含 R1-8B 的结果（N=43 test traces, K=5 early detection rate 76.7%）
- `oracle_upper_bound.py` 调用 `prepare_dataset()` 不接受模型参数，只加载默认数据集（R1-8B）
- 搜索所有 artifacts 目录，其他模型的实验（exp_ot7b_full_pipeline, hidden_states_r1_32b, hidden_states_qwq_32b）均无 oracle 相关输出
- 论文中的 85.5% oracle gap 数据仅来自 R1-8B

建议正文标注 oracle gap 85.5% 仅适用于 R1-8B，或注明 "reported for R1-8B"。

---
