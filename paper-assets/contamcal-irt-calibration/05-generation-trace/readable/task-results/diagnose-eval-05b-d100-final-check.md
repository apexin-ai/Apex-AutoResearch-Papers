# diagnose eval 05B d100 final check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_05B_d100_final_check_20260514T150727_result.json`
- **Structured JSON:** [`5658261984f193e75d16.json`](../../sessions/56/5658261984f193e75d16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**最终判断：Still running**

- 进程未失败，只是 MMLU 14K items 逐条推理非常慢（~5s/item → ~20h）
- 当前 GSM8K 17%，预计 **~3.5h 后全部完成**（约北京时间 05-15 02:30）
- GPU 2 被占用，不可用于其他任务
- d100_para_aligned 未自动启动，需等此实验完成后手动或串行提交

---
