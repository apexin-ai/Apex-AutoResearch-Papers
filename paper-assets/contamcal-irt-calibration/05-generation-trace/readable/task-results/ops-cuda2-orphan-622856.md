# ops cuda2 orphan 622856

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda2_orphan_622856_20260515T203102_result.json`
- **Structured JSON:** [`b2cacd4b7bb60103df47.json`](../../sessions/b2/b2cacd4b7bb60103df47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **PID 622856 已死**，进程不存在。无需 kill。
- **cuda:2 当前占用**：6797 MiB，唯一进程是 PID 623491（6788 MiB）——这应该是合法实验 exp_001_eval_3B_d005_s123_gsm8k 的子进程（registry PID 623480 的 child）。
- PID 622856 的 7526 MiB 显存已自动释放。cuda:2 空闲显存 17285 MiB。

**结论**：orphan 进程已自行退出，cuda:2 恢复正常，无需人工干预。

---
