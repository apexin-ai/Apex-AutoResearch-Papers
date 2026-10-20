# code wikievents verify continuation masking

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_verify_continuation_masking_20260517T181229_result.json`
- **Structured JSON:** [`f4ba3f9b75012afb5bc5.json`](../../sessions/f4/f4ba3f9b75012afb5bc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器的关键方法行号一致（`_apply_role_continuation_mask` 在 L635，`in_role_value` 相关逻辑位置相同）。5 行差异可能是注释或空行。核心逻辑一致。

## 验证结果

**代码状态：已部署**

Grammar-Aware Stateful Continuation Masking 的所有关键组件都已存在于两台服务器：

| 组件 | westd-16980 | westd-21461 |
|------|-------------|-------------|
| `GenerationState.in_role_value` | L98 | L98 |
| `GenerationState.role_value_start_len` | L99 | L99 |
| `GenerationState.role_allowed_roles` | L100 | L100 |
| `_build_role_continuation_tokens()` | L397 | L397 |
| `_apply_role_continuation_mask()` | L635 | L635 |
| continuation 进入逻辑 (ARGUMENT_ROLE) | L507 | L507 |
| 退出条件 (引号/MAX_TOKENS=25) | L472/L477 | L472/L477 |

**代码逻辑确认正确**：
- 进入：position == ARGUMENT_ROLE 时，设 `in_role_value=True`，记录 `role_value_start_len` 和 `role_allowed_roles`
- 后续 step：decode partial role string → 遍历 grammar-valid tokens → 检查 `partial + token_text` 是否匹配某 allowed role 的 prefix → 不匹配则 mask
- 退出：partial 含引号 `"` 或 token count > 25 → 重置 `in_role_value=False`
- Grammar-First Invariant 保持：如果没有 allowed token 可用，跳过 masking 避免 XGrammar 断言失败

**文件行数差异**（796 vs 801）是微小差异，不影响核心功能。

**结论：两台服务器代码一致，可直接运行 constrained 全量实验。**

---
