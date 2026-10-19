# diagnose eval adaptive k spatial p75 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-adaptive-k-spatial-p75-seed44_20260520T130411_result.json`
- **Structured JSON:** [`eed3d2739e119e180362.json`](../../sessions/ee/eed3d2739e119e180362.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因**：实验已正常完成全部评估，EXIT_CODE=129 是进程写完结果后收到 SIGHUP（tmux session 断开），属于 **false failure**。与同服务器 P90-seed42 同一模式。

**结果**：
- SR = **33.0%** (33/100)，与 P75 seed42 (31%) / seed43 (34%) 一致
- adaptive stats: avg_K=5.05, fast_path=61.8%, mean_l2=0.092
- JSON 文件完整，10 tasks 全部有结果

**处理**：无需重试。需手动修正 conclusion=success 并补录 metrics。

---
