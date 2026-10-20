# diag olmo2 s123 mmlu final

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_olmo2-s123-mmlu-final_20260520T113415_result.json`
- **Structured JSON:** [`87ada4d63988416ccc87.json`](../../sessions/87/87ada4d63988416ccc87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Cron 告警是误报。** OLMo-2 s123 eval 仍在运行：

- **PID 331098** 在 GPU 2 活跃，占用 16698 MiB
- 日志最后修改时间 19:34（刚刚）
- 当前进度：**d000_s123 评估中，86% (12165/14042)**
- 这只是第 1/5 个 dosage，后续还有 d005/d025/d050/d100

**结论**：
1. OLMo-2 s123 eval 未完成，不能更新 registry
2. GPU 2 被占用，不能提交 Gemma-2 s123 eval
3. 按 ~22 it/s 估算，d000 剩余 ~1.5 分钟，但加上后续 4 个 dosage（每个需重新加载模型+评估），预计还需 **~40-50 分钟**完成全部 5 个 dosage

需要等 OLMo-2 跑完后再执行 Part 1 和 Part 2。要设置定时检查吗？

---
