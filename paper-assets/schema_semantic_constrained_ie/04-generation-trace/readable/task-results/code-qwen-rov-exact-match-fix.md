# code qwen rov exact match fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_rov_exact_match_fix_20260518T032344_result.json`
- **Structured JSON:** [`0baa77c03d9dc0b5d1e2.json`](../../sessions/0b/0baa77c03d9dc0b5d1e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**修改内容**：`_apply_role_continuation_mask` 函数中增加 4 行（L672, L680-682）
- L672: `exact_match = partial in still_reachable` — 检测 partial 是否已精确匹配某个 allowed role
- L680-682: 若 exact match 且 token 以 `"` 开头（闭合引号），直接放行到 `tokens_allowed`

**修改后总行数**：816（原 812 + 4 行）

**rsync**：成功（westd-21461 → westd-16980）

**westd-16980 行数确认**：816，一致

**import 测试**：通过

---
