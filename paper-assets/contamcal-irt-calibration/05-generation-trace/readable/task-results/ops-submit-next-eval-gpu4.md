# ops submit next eval gpu4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit-next-eval-gpu4_20260515T101212_result.json`
- **Structured JSON:** [`3a5b50135ff3bc574eb4.json`](../../sessions/3a/3a5b50135ff3bc574eb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 4 被占用，无法提交。**

当前状态：
- **GPU 4**: PID 530975 正在运行 `Qwen2.5-1.5B_base_pretrained` eval（已运行 1h27m，占用 5674MiB / 24564MiB）

Checkpoint 就绪情况：

| Checkpoint | 状态 | 优先级 |
|---|---|---|
| 1.5B d005 s123 | 空目录，SFT 进行中 | P1 |
| 1.5B d100 s123 | **就绪**（adapter 73MB） | P2 |
| 1.5B d025 s123 | 空目录，SFT 进行中 | — |
| 3B d100 s42 v2 | 目录不存在 | — |
| 0.5B d005 s123 | **就绪**（adapter 35MB） | P3 |

按约束 C001/C002，GPU 4 上有活跃进程，不能提交新任务。当前 base pretrained eval 完成后，下一个应提交 **1.5B d100 s123 eval**（P1 的 d005 s123 SFT 尚未完成，P2 是最高可提交优先级）。

需要等 PID 530975 结束后再提交。

---
