# fix fitd dd strategy shift

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fitd-dd-strategy-shift_20260517T205447_result.json`
- **Structured JSON:** [`a45dab3c5ac506a50813.json`](../../sessions/a4/a45dab3c5ac506a50813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

### 1. 修复前后 intended_strategy 值域对比

| 文件 | 修复前 | 修复后 | 操作 |
|------|--------|--------|------|
| fitd_all.jsonl | {1, 2, 4, 6} | {0, 1, 3, 5} | -1 |
| deceptive_delight_all.jsonl | {1, 3, 4, 5, 6, 7} | {0, 2, 3, 4, 5, 6} | -1 |
| crescendo_all.jsonl | {0, 1, 2, 3, 4, 5, 6, 7} | 未修改 | 已是 0-based |

### 2. 转移矩阵摘要

**Crescendo** (250 convs, 1818 transitions, strategies: none/rapport_building/authority_appeal/emotional_manipulation/logical_reframing/role_assignment/gradual_escalation/obfuscation)
- role_assignment → role_assignment: 545 (自循环最强)
- obfuscation → obfuscation: 173
- emotional_manipulation → role_assignment: 95

**FITD** (80 convs, 541 transitions, strategies: none/rapport_building/emotional_manipulation/role_assignment)
- role_assignment → role_assignment: 161
- none → role_assignment: 80
- rapport_building → emotional_manipulation: 80

**Deceptive Delight** (80 convs, 565 transitions, strategies: none/authority_appeal/emotional_manipulation/logical_reframing/role_assignment/gradual_escalation)
- emotional_manipulation → role_assignment: 129
- none → gradual_escalation: 80
- gradual_escalation → emotional_manipulation: 80

### 3. 编码一致性确认

三个文件现在均为 **0-based 编码**。`merge_and_split.py` 的 +1 逻辑将作为唯一的 shift 入口，统一将所有策略映射到 1-based 供下游使用。

---
