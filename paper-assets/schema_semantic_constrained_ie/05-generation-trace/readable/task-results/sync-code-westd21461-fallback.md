# sync code westd21461 fallback

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_sync_code-westd21461-fallback_20260522T054942_result.json`
- **Structured JSON:** [`e686efbf767d3b8c3da2.json`](../../sessions/e6/e686efbf767d3b8c3da2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

同步完成。

**已同步文件**（westd-16980 → westd-21461，旧版本已 `.bak` 备份）：

| 文件 | 状态 |
|------|------|
| `run_constrained_extraction.py` | 已同步，`--lora_path` 参数可用 |
| `violation_checker_wikievents.py` | 已同步 |
| `eval_event_extraction.py` | 已同步 |
| `analyze_ac_violations.py` | 已同步 |

**无需同步**：`compiler/`（12 文件全部一致）、`prompts/`（2 文件全部一致）、其余共享的 `.py` 文件。

现在可以在 westd-21461 上直接用 `--lora_path` 参数启动推理，无需 monkey-patch。

---
