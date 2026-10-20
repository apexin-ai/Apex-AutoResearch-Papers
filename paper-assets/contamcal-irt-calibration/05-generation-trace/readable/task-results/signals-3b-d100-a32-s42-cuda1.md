# signals 3B d100 a32 s42 cuda1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_signals_3B_d100_a32_s42_cuda1_20260516T072745_result.json`
- **Structured JSON:** [`83ce6006ce350b273d46.json`](../../sessions/83/83ce6006ce350b273d46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**提交结果：**
- **exp_id**: `exp_002_signals_3B_d100_a32_s42`
- **PID**: 724022
- **GPU**: cuda:1 (已确认占用 537 MiB)
- **Checkpoint**: `Qwen2.5-3B_d100_a32_s42_v3/lora_adapter` (lora_alpha=32 ✅)
- **Signals**: s1_embedding, s2_minkpp, s4_selfcritique × 3 benchmarks (mmlu, gsm8k, arc_challenge)
- **状态**: s1_embedding mmlu 正在计算中
- **Registry**: RUNNING

3B s42 signals 覆盖现在：d000 (cuda:4) + d005 (cuda:2) + d025 (done) + **d100 (cuda:1)** — 全部在跑。

---
