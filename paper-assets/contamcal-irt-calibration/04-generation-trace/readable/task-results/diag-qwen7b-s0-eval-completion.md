# diag qwen7b s0 eval completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen7b-s0-eval-completion_20260520T234913_result.json`
- **Structured JSON:** [`064a94d45f7b56ffd6eb.json`](../../sessions/06/064a94d45f7b56ffd6eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ARC 进程仍在运行（PID 417433，20506 MiB GPU），当前在 d000 eval 中。日志的 tee 缓冲导致文件看起来没更新。

## Qwen-7B s0 Eval Results

### MMLU 5-shot — DONE
| Dosage | Accuracy | Correct/Total |
|--------|----------|---------------|
| d000   | 66.32%   | 9313/14042    |
| d005   | 64.68%   | 9083/14042    |
| d025   | 65.67%   | 9221/14042    |
| d050   | 65.78%   | 9237/14042    |
| d100   | 65.29%   | 9168/14042    |

**Δ(d100−d000) = −1.03pp**

### ARC 25-shot — RUNNING
d000 正在执行中（~34% 进度），d005–d100 尚未开始。ARC 5 dosage 串行，预估还需 ~1 小时完成全部。

暂不更新 registry，等 ARC 全部完成后再一起写入。

---
