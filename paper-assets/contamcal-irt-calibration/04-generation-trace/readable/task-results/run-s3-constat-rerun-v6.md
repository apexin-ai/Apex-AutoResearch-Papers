# run s3 constat rerun v6

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_s3_constat_rerun_v6_20260515T210057_result.json`
- **Structured JSON:** [`22549925fd66c032ac86.json`](../../sessions/22/22549925fd66c032ac86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s3_constat 重跑完成，3 个 benchmark 全部成功：

| Benchmark | Items | Score Range | Mean |
|-----------|-------|-------------|------|
| mmlu | 6596 | [-1.0, 1.0] | -0.0173 |
| gsm8k | 228 | [-1.0, 1.0] | 0.0636 |
| arc_challenge | 697 | [-1.0, 1.0] | 0.0215 |

输出文件：
- `signal_s3_constat_mmlu.json`
- `signal_s3_constat_gsm8k.json`
- `signal_s3_constat_arc_challenge.json`

均在 `/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/` 下。item count 与 paraphrase eval 中的 per_item 数量一致（set intersection 正常工作），bug 已修复确认。

---
