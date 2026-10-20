# diagnose eval gemma2 mmlu s0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gemma2_mmlu_s0_20260520T222949_result.json`
- **Structured JSON:** [`11c2a8c2ecd6e1414ac8.json`](../../sessions/11/11c2a8c2ecd6e1414ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：实验没有失败，是 cron 误报。**

- 进程 PID 445288 在 cuda:1 上正常运行，已完成 d000（accuracy=0.6488）和 d005（accuracy=0.6414），d025 正在评估中（~29%），d050 待开始
- 每个 dosage 约 11 分钟，预计 ~06:49 CST 全部完成
- **误判原因**：cron 检测逻辑查找 W&B sentinel/metrics，但此 eval 脚本只写本地 `.done` sentinel，不使用 W&B
- evaluate.py md5 已验证与 reference hash 一致，lora_alpha=32 已确认
- 诊断报告已写入 `artifacts/eval_gemma2_mmlu_s0_diagnosis.md`

---
