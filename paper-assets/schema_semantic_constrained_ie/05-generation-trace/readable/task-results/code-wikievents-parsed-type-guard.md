# code wikievents parsed type guard

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_parsed_type_guard_20260517T183336_result.json`
- **Structured JSON:** [`6599bf7354b937d9319b.json`](../../sessions/65/6599bf7354b937d9319b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器修复完成。

**修改内容**: `parse_model_output()` 中的两处 `return json.loads(...)` 改为先检查 `isinstance(result, dict)`，非 dict（如 list）时跳过，继续尝试 regex `\{...\}` 提取，最终无法得到 dict 则返回 None。

**覆盖范围**: 所有调用 `parse_model_output` 的地方（line 629 的 `parsed_p1.get`、line 688 的 `parsed_p2.get`、line 987-989 的 `parsed.get`）都不会再因 list 返回值 crash。line 968-969 的已有守卫作为额外保险保留。

---
