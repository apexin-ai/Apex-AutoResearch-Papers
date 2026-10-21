# analysis cf violation rootcause

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cf_violation_rootcause_20260514T021039_result.json`
- **Structured JSON:** [`906500de5563a1427199.json`](../../sessions/90/906500de5563a1427199.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，结果保存到 `outputs/cf_violation_analysis.json`。关键发现：

### Dimension 1: Within-Relations CF（同 entity 在不同 relation 中 type 不一致）

| Mode | Violations | CF Rate |
|------|-----------|---------|
| unconstrained | 1 | 0.04% |
| full_s1 | 10 | 0.36% |
| full_s2 | 18 | **0.72%** |

S2 最高，但绝对数量不大（18个）。最常见冲突模式：`Part-of|Used-for` 对 (5次)，`Feature-of|Used-for` (3次)。

### Dimension 2: Entity-vs-Relation EVR（Pass1 entity type ≠ Pass2 relation head/tail type）

| Mode | Violations | EVR Rate | Affected Samples |
|------|-----------|----------|-----------------|
| unconstrained | 3 | 0.09% | 2 |
| **full_s1** | **248** | **7.34%** | **167** |
| full_s2 | 182 | 5.54% | 131 |

**意外发现**：S1 的 EVR 违反率 (7.34%) 比 S2 (5.54%) 还高。这说明 S1 单通道在一个 JSON 中同时生成 entities 和 relations 时，也会产生内部不一致——entity list 中的 type 和 relation triple 中的 head_type/tail_type 不匹配。

S2 的 EVR 主要 drift 模式：
- `Generic↔OtherScientificTerm` (60次) — 占比最大
- `Generic↔Material` (28次)
- `Generic↔Metric` (20次)

大量 drift 涉及 **Generic** type，说明 Pass 2 的 semantic constraint 倾向于将 Pass 1 标注为 Generic 的 entity 重新分配为更具体的 type（或反向），因为 Generic 在 domain/range 约束中与具体 type 的 valid_pairs 不同。

---
