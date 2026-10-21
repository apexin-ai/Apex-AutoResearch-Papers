# run 05B s123 pipeline cuda1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_05B_s123_pipeline_cuda1_20260516T105807_result.json`
- **Structured JSON:** [`51f0f7a86c9fa8e9a5d4.json`](../../sessions/51/51f0f7a86c9fa8e9a5d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并在运行。任务 `signals_05B_s123_v2` 在 cuda:1 上执行，pipeline 内容：

| 步骤 | 模型 | Benchmark | Signals |
|------|------|-----------|---------|
| 1 | d100_s123 | arc_challenge | s1+s2+s4 |
| 2 | d100_s123 | gsm8k | s1+s2+s4 |
| 3 | d100_s123 | mmlu | s4 only |
| 4 | d000_s123 | gsm8k | s1+s2+s4 (重算以生成 merged) |

完成后 0.5B s123 全部 signals 就齐了（d005/d025 已完成，d100/d000 正在补齐）。PID 760236，日志: `~/runs/contamcal-irt-calibration/signals_05B_s123_v2.log`。

---
