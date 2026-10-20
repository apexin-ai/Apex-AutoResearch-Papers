# code deploy eval westd21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deploy_eval_westd21461_20260518T081400_result.json`
- **Structured JSON:** [`91124279d23c70e188b3.json`](../../sessions/91/91124279d23c70e188b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**部署完成。最终状态：**

| 文件 | westd-16980 | westd-21461 |
|---|---|---|
| `run_v3_eval.sh` | ✅ 原始 | ✅ 已部署，可执行 |
| `violation_checker_wikievents.py` | ✅ | ✅ 已存在 |
| `eval_event_extraction.py` | ✅ | ✅ 已存在 |
| `ontology_constraints_wikievents.json` | ✅ | ✅ 已存在 |

两台服务器路径一致（`/root/schema_semantic_constrained_ie/`），无需路径调整。westd-21461 上 eval 全套脚本和数据就绪，可直接运行。

---
