# ops kill dup and submit docred constrained

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_dup_and_submit_docred_constrained_20260516T053534_result.json`
- **Structured JSON:** [`f9a84d0bc83086e3cde4.json`](../../sessions/f9/f9a84d0bc83086e3cde4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

| 步骤 | 结果 |
|------|------|
| Kill PID 7813 (重复 SciERC) | ✅ SIGTERM 成功 |
| 清理残留 jsonl | ✅ 已删除 |
| 提交 DocRED constrained | ✅ PID **8347**, tmux `w6_mistral_docred_constrained` |
| xgrammar 版本 | **0.1.33** ✅ |
| 错误检查 | **0 errors** ✅ |
| GPU 1 占用 | 15282MiB, 86% util ✅ |

当前 westd-21461 两块 GPU 满载：
- **GPU 0**: PID 7740 — docred unconstrained
- **GPU 1**: PID 8347 — docred constrained (grammar compilation 中，~96 relations，首条输出预计 ~10min)

---
