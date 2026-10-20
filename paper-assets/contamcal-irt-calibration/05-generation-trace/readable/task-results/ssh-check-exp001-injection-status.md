# ssh check exp001 injection status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_exp001_injection_status_20260513T232029_result.json`
- **Structured JSON:** [`cc236e8cb344897daff1.json`](../../sessions/cc/cc236e8cb344897daff1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_001_sft_injection 最终状态：SUCCESS（已确认）**

SSH 验证结果：
- `mmlu_paraphrases.json`: 27M, 14042 条 ✓
- `arc_challenge_paraphrases.json`: 1.7M, 1172 条 ✓
- `gsm8k_paraphrases.json`: 2.1M, 1319 条 ✓
- `humaneval_paraphrases.json`: 489K（额外产出）
- vLLM 进程已正常 shutdown，无残留进程
- JSON 格式完整，含 similarity/bleu/passed_qc 等 QC 字段

Registry 已更新：`conclusion=success`，`failure_reason` 已清除。Cron 5 次误判源于监控旧 PID，实际生成任务已全部正常完成。

---
