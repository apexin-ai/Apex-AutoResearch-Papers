# code exp fewshot bcs mitigation

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_fewshot_bcs_mitigation_20260517T124103_result.json`
- **Structured JSON:** [`cf7cbca8fa1809fc341e.json`](../../sessions/cf/cf7cbca8fa1809fc341e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并在运行。

**总结：**
- 脚本: `/root/schema-dag-extraction/src/run_fewshot_bcs.py`
- 数据: FewRel 80-rel (train+val, 56000 samples), test=960 (12/rel), fewshot pool=688+/rel
- 条件: 0-shot / 1-shot / 5-shot × count_8 / count_16 × low-BCS / high-BCS (25 batches per group)
- 总推理次数: 43,200 (300 conditions × ~144 samples/batch avg)
- BCS 分组: 从 60 个随机 batch 中取 BCS 最低 25 和最高 25
- 输出: `artifacts/fewshot_bcs_mitigation/` (results_incremental.jsonl + analysis.json)
- Registry: `exp_fewshot_bcs_mitigation` status=RUNNING

---
