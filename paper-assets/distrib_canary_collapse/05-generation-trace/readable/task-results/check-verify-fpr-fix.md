# check verify fpr fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_verify_fpr_fix_20260517T173738_result.json`
- **Structured JSON:** [`8253a1016b7e315ad730.json`](../../sessions/82/8253a1016b7e315ad730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修正已确认生效，汇总如下：

### 各处当前实际值

| 位置 | 内容 | 状态 |
|------|------|------|
| **Line 319** (`tab:fpr_fnr` Threshold 行) | `20.8\% (12.5--37.5)` | 正确 |
| **Line 114** (`tab:method_comparison` Threshold 行) | `20.8 & 0 & 0 & 33.3 & 100 & 20.8` | 正确 |
| **Line 232** (正文 FPR 描述) | `20.8\% (threshold)` | 正确 |
| **Line 59** (62.5% 出现处) | 指 spurious-signal rate excluding TY，非 Threshold FPR，无需修改 | 正确 |

- `grep "29.2"` 返回 exit code 1（零匹配），旧值已完全清除
- 无需额外修复
- 编译状态未重新验证（文件内容已正确，无变更需要触发编译）

---
