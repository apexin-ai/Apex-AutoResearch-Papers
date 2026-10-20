# code llama v3 eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_v3_eval_20260518T103044_result.json`
- **Structured JSON:** [`3c7ce3da918e8fe78f16.json`](../../sessions/3c/3c7ce3da918e8fe78f16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`cf_majority_voting.py` 不存在。下面是所有已完成步骤的汇总：

---

## Llama v3 Constrained 评估结果

### 1. Violations (原始)
| 类型 | 数量 | 比率 |
|------|------|------|
| ET (Entity Type) | 0 | 0.0% |
| EV (Event Vocab) | 0 | 0.0% |
| RoV (Role Vocab) | 0 | 0.0% |
| AC (Arg Constraint) | 173 | 3.8% |
| CF (Cross-Field) | 704 | 17.2% |
| **RoV+AC rate** | — | **3.8%** |

Documents: 207 checked, 39 parse failures

### 2. F1 (原始)
| 指标 | P | R | F1 |
|------|------|------|------|
| Entity | 0.3892 | 0.1140 | **0.1763** |
| Trigger ID | 0.0808 | 0.0696 | **0.0748** |
| Argument | 0.0113 | 0.0124 | **0.0118** |

### 3. Parse Failures
- **39/246** 文档解析失败（violation checker 报告）
- 注意：用户提供的 parse failure 脚本检查 `events` 字段，但实际数据用的是 `parsed_output`，导致误报 246/246。实际失败数为 39。

### 4. Post-hoc Filter 效果
- 移除 173 个 AC violation arguments（4547 → 4374）
- EV/RoV 移除: 0
- Argument F1: 0.0113 → **0.0118** (P 从 0.0113 → 0.0118)
- Entity/Trigger F1 不变
- 提升极小

### 5. CF Majority Voting
- **`cf_majority_voting.py` 脚本不存在**，无法执行。需要先创建该脚本。

---

**总结**: Constrained v3 的 EV=0%, RoV=0% 说明 schema constraint 在词汇层面完全生效。AC 3.8% 仍有残留。CF 17.2% 较高。但整体 F1 极低（Arg F1 仅 1.2%），说明模型生成质量本身是主要瓶颈，不是 constraint violation。

---
