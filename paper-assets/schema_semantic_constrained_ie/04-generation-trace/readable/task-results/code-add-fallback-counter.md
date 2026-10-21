# code add fallback counter

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add_fallback_counter_20260514T061237_result.json`
- **Structured JSON:** [`98bbd50353e91dc54855.json`](../../sessions/98/98bbd50353e91dc54855.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。改动汇总：

| 行号 | 改动 |
|------|------|
| 35 | `import logging` |
| 45 | `logger = logging.getLogger(__name__)` |
| 204 | `self._grammar_first_skip_count = 0`（`__init__` 中初始化） |
| 387-388 | `any_allowed_valid=False` 分支中 `+= 1` + `logger.warning(...)` |
| 397-399 | `reset()` 中：count > 0 时 `logger.info` 汇总，然后归零 |

行为：每次 fallback 触发时打一条 WARNING（含累计次数），每次 `reset()`（即一次 `generate()` 结束）打一条 INFO 汇总并归零。不影响现有 masking 逻辑。下次实验自动生效。

---
