# ssh urgent sampling fix both servers

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_sampling_fix_both_servers_20260522T155313_result.json`
- **Structured JSON:** [`b4e640e09d7ac045c4b5.json`](../../sessions/b4/b4e640e09d7ac045c4b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器均已修复，验证通过：

| 服务器 | 写入 open | 读取 open |
|--------|----------|----------|
| **autodl-5090** | L671 ✅ `errors="replace"` | L686 ✅ `errors="replace"` |
| **autodl-5090-c** | L673 ✅ `errors="replace"` | L688 ✅ `errors="replace"` |

两台服务器的 sampling.py 现在读写两处 `open()` 调用都有 `errors="replace"` 防护。已创建带时间戳的 `.bak` 备份。运行中的进程不受影响，crash 后重跑或新启动的进程将使用修复版代码。

---
