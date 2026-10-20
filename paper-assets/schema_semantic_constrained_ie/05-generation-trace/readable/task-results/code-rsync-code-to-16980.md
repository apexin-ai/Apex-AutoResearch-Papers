# code rsync code to 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsync_code_to_16980_20260517T211541_result.json`
- **Structured JSON:** [`fe12bb24e7957474e3ef.json`](../../sessions/fe/fe12bb24e7957474e3ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Rsync 结果
- 方向：westd-21461 → westd-16980
- 命令：`rsync -avz -e 'ssh -p 16980 -o StrictHostKeyChecking=no' --exclude='outputs/' --exclude='logs/' --exclude='__pycache__/' --exclude='.cache/' /root/schema_semantic_constrained_ie/ root@connect.westd.seetacloud.com:/root/schema_semantic_constrained_ie/`
- 文件传输数：14 files
- type_mask_processor.py on westd-16980: **812 行** ✓
- 关键函数验证：**通过** ✓（`_build_role_prefix_map` L352, `_build_entity_type_prefix_map` L377, `_build_role_continuation_tokens` L409）

---
