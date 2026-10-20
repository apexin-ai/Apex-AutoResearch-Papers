# monitor training progress s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-s123_20260519T135303_result.json`
- **Structured JSON:** [`da9b0529a3cbc0bd4ebe.json`](../../sessions/da/da9b0529a3cbc0bd4ebe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告 (westd-29999)

所有 4 个 GPU 正在训练 **d000 (seed=123)** — 这是 5-dosage sweep 的第一个 dosage。

| GPU | 模型 | 进度 (d000) | 速度 | d000 剩余 | 总剩余 (5 dosage) |
|-----|------|-------------|------|-----------|-------------------|
| cuda:0 | Phi-4 14.7B | **333/3125** (10.7%) | ~2.45 s/step | ~1.9h | ~11.5h |
| cuda:1 | Qwen2.5-14B | **257/3125** (8.2%) | ~3.15 s/step | ~2.5h | ~14.5h |
| cuda:2 | OLMo-2-7B | **427/3125** (13.7%) | ~1.95 s/step | ~1.5h | ~9h |
| cuda:3 | Gemma-2-9B | **278/3125** (8.9%) | ~3.0 s/step | ~2.4h | ~13.5h |

**GPU 显存/利用率:**
| GPU | 显存 | 利用率 | 温度 |
|-----|------|--------|------|
| 0 | 57,759 MiB | 93% | 71°C |
| 1 | 64,087 MiB | 95% | 63°C |
| 2 | 65,493 MiB | 99% | 66°C |
| 3 | 54,627 MiB | 92% | 51°C |

**已完成:** Qwen2.5-7B s123 全部 5 个 dosage checkpoint 已存在（跳过）。上一轮 s42 eval (eval_results_v2) 已全部完成。

**预估完成时间:** OLMo-2-7B 最快（~9h，约明日 07:00 CST），Qwen-14B 最慢（~14.5h，约明日 12:00 CST）。

---
