# diagnose eval obs only spatial norm02 k5 seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-spatial-norm02-k5-seed44-r2_20260519T162741_result.json`
- **Structured JSON:** [`5bc28266375623b0dd2f.json`](../../sessions/5b/5bc28266375623b0dd2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/diagnose_spatial_k5_seed44_r2.md`。

**核心发现：**

- **spatial-K5-seed44 实际已完成**，success_rate = **37.0%**（JSON 时间 May 19 23:45）。ROADMAP 提到的 GPU2 untracked 进程就是它，已正常跑完。
- spatial-K5-seed45 也已完成：**34.0%**
- object random-selection K5 seed43 也已完成：**11.0%**

这 3 个实验都是 untracked 手动进程完成的，不写 sentinel 文件，所以 managed r2 重试检测不到，自动判定失败。**是误报，不需要重试。**

**真正缺失的是：**
- object random-selection K5 seed44 — 无 JSON，需重试
- object random-selection K5 seed45 — 无 JSON，需重试

当前 GPU 0/4/5 空闲，可用于重试这两个实验。

---
