# code d049 posthoc ee

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d049_posthoc_ee_20260518T102140_result.json`
- **Structured JSON:** [`a211e23be5f9f6e76e8b.json`](../../sessions/a2/a211e23be5f9f6e76e8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本完成，验证通过。

**汇报：**

| | Unconstrained | Post-hoc Filtered |
|---|---|---|
| Events | 3013 | 2291 |
| Arguments | 5467 | 23 |
| EV violations | 722 (24.0%) | 0 (0.0%) |
| RoV violations | 4094 (74.9%) | 0 (0.0%) |
| AC violations | 18 (0.3%) | 0 (0.0%) |
| Go/No-go (RoV+AC) | 0.7521 | 0.0000 |

脚本路径：`/root/schema_semantic_constrained_ie/posthoc_filter_ee.py`

Post-hoc filtering 将违规率降至 0%，但代价极大：5467 个 arguments 只剩 23 个（99.6% 被删除）。主要原因是 Qwen unconstrained 输出使用通用角色名（agent, object, location）而非 ontology 定义的专有角色（Attacker, Artifact, Place），导致 RoV 步骤删除了 74.9% 的 arguments。这正好说明 post-hoc filtering 作为 baseline 的局限性：constrained decoding 在生成时就引导模型使用正确的 role vocabulary，避免这种大规模丢弃。

---
