# analysis reverse cutoff s2 v2 eval failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reverse_cutoff_s2_v2_eval_failure_20260527T041446_result.json`
- **Structured JSON:** [`35ec462fed487ae05d4f.json`](../../sessions/35/35ec462fed487ae05d4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**总结**：
- **失败原因**：westd-10894 GPU 硬件挂起（与 registry 原有记录一致，但实际进度比之前记录的更远——到了 T7 33/50，而非 T5 27/50）
- **数据状态**：7/10 tasks 有完整结果（仅存在于日志中，无持久化结果文件），T7-T9 未完成
- **部分均值**：TSR=0.854, CAR=0.677（不完整，缺 3 个 task）
- **需要重跑**：如需完整 10-task 结果，需要重新启动 eval

---
