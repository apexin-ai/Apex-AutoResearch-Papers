# ssh p1 qwen parse failure diagnosis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_qwen_parse_failure_diagnosis_20260518T231746_result.json`
- **Structured JSON:** [`53069ee8b644a9fbbcc7.json`](../../sessions/53/53069ee8b644a9fbbcc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。三个根因：

**根因 1（主因）：严重的重复退化**。模型在 greedy 解码下将同一事件/实体重复生成 50-100+ 次，填满 4096 token 后 JSON 被截断，parse 失败。unconstrained 模式每个失败样本平均 ~100 个 trigger 提及。生成配置没有 `repetition_penalty`。

**根因 2（constrained 专属）：Grammar schema 与 FT 格式不匹配**。`compile_event_json_schema()` 生成的 schema 要求 `{"entities": [...], "events": [...]}` 双字段，但 FT 训练数据只有 `{"events": [...]}`。xgrammar 强制模型先输出 entities，模型不会做这件事，于是幻觉式重复生成实体直到 token 耗尽，events 部分从未被生成。这就是 constrained (10%) 比 unconstrained (25%) 更差的原因。

**根因 3（次要）：`&lt;think>` token 前缀不一致**。训练数据 prompt 末尾包含 `&lt;think>\n\n&lt;/think>\n\n`，推理时 `enable_thinking=False` 不生成这些 token。模型似乎已适应（输出直接以 JSON 开头），但可能影响生成质量。

报告已写入 `artifacts/p1_qwen_parse_failure_diagnosis.md` 并注册（`art_20260518_e3da09`）。

---
