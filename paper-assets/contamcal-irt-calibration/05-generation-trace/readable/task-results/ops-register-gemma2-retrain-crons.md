# ops register gemma2 retrain crons

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_register-gemma2-retrain-crons_20260520T220556_result.json`
- **Structured JSON:** [`ab918c8dbdd92de4f676.json`](../../sessions/ab/ab918c8dbdd92de4f676.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已获取。汇总如下：

| Session | GPU | PID | 任务 | 运行时间 |
|---------|-----|-----|------|---------|
| `gemma2_d100_retrain` | cuda:0 | **437077** | train_sft gemma-2-9b d100 s0 (alpha=32) | 1h52m |
| `gemma2_mmlu_s0` | cuda:1 | **437235** | evaluate gemma-2-9b d000_s0 MMLU | 1h48m |
| `gemma2_arc_s0` | cuda:2 | **437317** | evaluate gemma-2-9b d000_s0 ARC | 1h47m |

另外 cuda:3 上有 PID **435054** — Qwen2.5-14B d100 s0 训练（已运行 11h03m）。

三个日志文件均存在且正在写入（最后更新 06:06）。

---
