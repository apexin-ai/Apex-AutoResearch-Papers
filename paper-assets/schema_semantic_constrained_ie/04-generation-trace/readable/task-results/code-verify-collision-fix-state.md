# code verify collision fix state

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_collision_fix_state_20260518T033040_result.json`
- **Structured JSON:** [`f0a10cf32a0654ae6073.json`](../../sessions/f0/f0a10cf32a0654ae6073.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 文件行数
| 服务器 | 当前文件 | .bak | .bak_before_grammar_fix |
|--------|---------|------|------------------------|
| westd-21461 | **816 行** (32428 bytes, May 18 11:25) | 796 行 (May 18 05:01) | 544 行 (May 18 00:05) |
| westd-16980 | **816 行** | — | — |

两台服务器文件一致（816 行）。

### Fix 1: 碰撞组 continuation mask — **不存在**

在 westd-21461 的三个版本（当前、.bak、.bak_before_grammar_fix）和 westd-16980 上，以下关键词全部零匹配：
- `collision_group`
- `_build_entity_type_collision`
- `_apply_entity_type_continuation`
- `in_entity_type_value`

**碰撞组代码从未被写入文件。** 不是丢失，是从未存在。

### Fix 2: Qwen RoV exact-match fix — **存在**

两台服务器均在第 672、680 行找到 `exact_match`：
- L672: `exact_match = partial in still_reachable`
- L680: `if exact_match and text.startswith('"'):`

.bak（796 行）中 `exact_match` 匹配数为 0，说明此 fix 是 .bak → 当前版本期间新增的（+20 行，796→816）。

### 结论

| Fix | westd-21461 | westd-16980 |
|-----|-------------|-------------|
| 碰撞组 continuation mask | **缺失（从未写入）** | **缺失** |
| Qwen RoV exact-match | **存在** (L672, L680) | **存在** (L672, L680) |

**可能原因**：碰撞组 fix 的 worker 可能只做了分析/规划，没有实际执行文件写入；或者写入被回滚。文件变化轨迹（544 → 796 → 816）只体现了 grammar fix 和 Qwen RoV fix 两次修改，碰撞组代码从未出现在任何版本中。

---
