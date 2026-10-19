# ops qwen3 check immediate

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen3_check_immediate_20260520T063145_result.json`
- **Structured JSON:** [`fe17dcf0d6f39bddd333.json`](../../sessions/fe/fe17dcf0d6f39bddd333.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen3 标注完成，post-hoc fix 已执行。结果：

| 指标 | 值 |
|------|-----|
| Total annotations | 388 |
| Jailbreak | 52 (13.4%) |
| JB with CP | 52/52 |
| CP mean | 1.4 (median=0, min=0, max=20) |
| CP relative mean | 0.045 |
| Hidden states 匹配 | 52/52 |
| **Phase 4** | **GO** |

CP 分布极度前倾（median=0, mean=1.4），说明 Qwen3 的 commitment point 出现极早。52 条 hidden states 全部就位，Phase 4 可以启动。

---
