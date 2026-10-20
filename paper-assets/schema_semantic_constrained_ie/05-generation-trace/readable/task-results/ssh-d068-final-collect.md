# ssh d068 final collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d068_final_collect_20260519T164313_result.json`
- **Structured JSON:** [`9c604900dc24bf210062.json`](../../sessions/9c/9c604900dc24bf210062.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/report/d068_guided_beam.md`。

**关键发现**: 4 个 beta 值（0.0, 0.5, 1.0, 2.0）的 **violation rate 全部为 0%**。fine-tuned Qwen3-8B 的 beam 候选中没有任何 constraint violation，因此 penalty re-ranking 无实际效果。beta=0.0（标准 beam search）的 F1 反而最高（Entity 0.7429, Relation 0.5442），beta>0 时 F1 略降。

**注意**:
1. 实验仍在运行（约 20% 完成，test.json 有 551 samples 而非预期的 100 docs），当前数字是中间结果
2. 预计每组还需 ~1-1.5 小时完成
3. Guided beam 更适合 zero-shot/few-shot 场景——fine-tuned 模型已内化了 schema 约束

---
