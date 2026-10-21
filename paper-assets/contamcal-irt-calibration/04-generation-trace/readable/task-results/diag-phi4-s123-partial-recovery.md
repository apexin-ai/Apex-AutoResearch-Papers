# diag phi4 s123 partial recovery

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_phi4-s123-partial-recovery_20260520T152350_result.json`
- **Structured JSON:** [`66fe50df1f4ce0550589.json`](../../sessions/66/66fe50df1f4ce0550589.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正常运行中，无需干预。

**当前状态：**

| Dosage | 状态 | Accuracy |
|--------|------|----------|
| d000 | 完成 | 76.31% |
| d005 | 完成 | 75.92% |
| d025 | 运行中 (57%, 8095/14042) | — |
| d050 | 待运行 | — |
| d100 | 待运行 | — |

PID 365465 在 cuda:2 上正常运行（31706 MiB），原脚本会顺序跑完 d025 → d050 → d100。

**预计时间：**
- d025 剩余 ~5 分钟（18.4 items/s）
- d050、d100 各 ~13 分钟
- 全部完成约 **31 分钟后**（~23:50 CST）

---
