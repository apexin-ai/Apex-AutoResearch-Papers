# ops read eval fast

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read_eval_fast_20260515T134441_result.json`
- **Structured JSON:** [`9d6109434be774c08483.json`](../../sessions/9d/9d6109434be774c08483.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件都成功读取，但输出被截断（中间省略了约 269241 字符）。文件内容结构：

**eval_exp1.json** 和 **eval_exp2.json** 都包含按 `count_{N}_random_{M}` 组织的评估结果，每个条目包含：
- `accuracy`, `correct`, `total`, `bcs`
- `count_key`, `num_types`, `batch_types`
- `per_type_accuracy`（每种关系类型的细分准确率）

可见的数据范围：
- **exp1** 从 `count_1_random_0` 开始（单类型，12 samples/type）
- **exp2** 到 `count_16_random_24` 结束（16 类型，192 samples/batch）

输出总量过大（~270K 字符），单次 SSH 返回被截断。如需完整内容，需要分文件读取或用 `python3 -c` 提取摘要统计。要我分别读取两个文件，或者直接提取汇总指标？

---
