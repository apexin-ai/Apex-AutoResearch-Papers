# diagnose eval phi4 s123 mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_phi4_s123_mmlu_20260520T152223_result.json`
- **Structured JSON:** [`46e7d3861c247d5b0c54.json`](../../sessions/46/46e7d3861c247d5b0c54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：

**实验没有失败，是 cron 监控误报。**

- PID 365465 在 GPU 2 上正常运行（State=R, GPU-Util=95%）
- d000_s123 ✅ 完成（23:04）
- d005_s123 ✅ 完成（23:17）
- d025_s123 🔄 进行中（PID 365465 当前任务）
- d050_s123 / d100_s123 待执行

**误报原因**：实验未通过 agent-ml tmux wrapper 启动，缺少 `/tmp/agent-ml-exit/eval_phi4_s123_mmlu.exit` sentinel 文件，cron 的 5× dead check 找不到注册进程，自动标记为 failed。

**处理**：将 cron 中状态改回 running，无需重跑。预计 ~23:50 CST 全部完成。

---
