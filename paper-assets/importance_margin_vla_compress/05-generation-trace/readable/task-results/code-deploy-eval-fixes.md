# code deploy eval fixes

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deploy-eval-fixes_20260515T190148_result.json`
- **Structured JSON:** [`3c8e215286aac50ba90d.json`](../../sessions/3c/3c8e215286aac50ba90d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三处修改全部到位，语法验证通过：

| 修改 | 行号 | 状态 |
|------|------|------|
| `import hashlib` | 18 | OK |
| `hashlib.md5` 替换 `hash()` | 260-261 | OK |
| `prune_idx` 限定 n_visual 范围 | 181-182 | OK |
| docstring 更新 | (已含) | OK |
| 语法检查 `py_compile` | — | SYNTAX_OK |

---
