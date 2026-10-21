# diagnose dead s47 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dead_s47_cqa1_20260529T025224_result.json`
- **Structured JSON:** [`cef8b4d5ea99b7d8976f.json`](../../sessions/ce/cef8b4d5ea99b7d8976f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**两个"消失"的实验都正常跑完了**，进程退出是因为实验结束（EXIT_CODE=0），不是崩溃：

| 实验 | 状态 | SR | Episodes |
|------|------|-----|----------|
| Attn k=0.7 seed47 | ✅ 完成 | **54.4%** | 500/500 |
| L2norm k=0.5 seed47 | ✅ 完成 | **50.0%** | 500/500 |
| Attn k=0.75 seed47 | 🔄 运行中 | ~46.7% (T0-T8) | 450/500, Task 9 ep 40/50 |

Attn k=0.75 还剩最后 10 个 episode，约 5 分钟内完成。cqa1 四张卡全部在跑 seed47 实验（k095_v2 在 cuda:0, k09 在 cuda:1, k075 在 cuda:2, random_k085 在 cuda:3）。

---
