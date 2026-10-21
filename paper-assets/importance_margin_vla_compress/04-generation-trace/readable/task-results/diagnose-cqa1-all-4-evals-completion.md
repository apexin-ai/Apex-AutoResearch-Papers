# diagnose cqa1 all 4 evals completion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_all_4_evals_completion_20260519T110218_result.json`
- **Structured JSON:** [`9f0756aa61622bca40c1.json`](../../sessions/9f/9f0756aa61622bca40c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| Eval | SR | 95% CI | Registry |
|------|-----|--------|---------|
| M=32 official | **运行中** (task 0, ep 14/50) | - | RUNNING |
| M=32 seed44 | **59.6%** | [55.2%, 63.8%] | updated ✓, cron deleted ✓ |
| M=64 seed44 | **64.4%** | [60.1%, 68.5%] | updated ✓, cron deleted ✓ |
| M=96 seed44 | **52.8%** | [48.4%, 57.1%] | updated ✓, cron deleted ✓ |

M=32 official 仍在 GPU:3 上运行（刚启动约 2 小时，在 task 0 ep 14/50，预计还需数小时）。M=32 official 的 cron 保留未删。

---
