# audit cqa1 32758 preparing fix

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1-32758-preparing-fix_20260523T121452_result.json`
- **Structured JSON:** [`24deac05906ad944091f.json`](../../sessions/24/24deac05906ad944091f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cqa1-32758 审计完成。汇总：

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| **eval-supp-obj-reconvla-s44** | cuda:0 | 180869 | PREPARING → **RUNNING** ✓ |
| **eval-supp-k2mean-object-s44** | cuda:3 | 177864 | PREPARING → **RUNNING** ✓ |
| **eval-supp-spatial-vla-only-s43** | cuda:5 | 181173 | PREPARING → **RUNNING** ✓ |
| eval-supp-k2mean-spatial-s44 | cuda:1 | 174449 | RUNNING ✓ |
| eval-supp-long-k2mean-s42 | cuda:4 | 172251 | RUNNING ✓ |
| eval-supp-long-vla-only-s43 | cuda:2 | 199664 | RUNNING ✓ |

所有 6 个实验进程均为 `Rl`（running）状态，显存正常占用（4.8-6.5 GB/卡）。3 个 PREPARING 已通过 QUEUED → RUNNING 转换修复，已注册每小时 cron 监控。

---
