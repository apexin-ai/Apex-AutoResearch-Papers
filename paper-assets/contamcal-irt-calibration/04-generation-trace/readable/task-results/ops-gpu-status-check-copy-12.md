# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260514T161439_result.json`
- **Structured JSON:** [`be1f70d61d7469890e96.json`](../../sessions/be/be1f70d61d7469890e96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 (2026-05-15 ~00:16 UTC)

| GPU | 任务 | 进度 | 剩余时间 | ETA (UTC) |
|-----|------|------|----------|-----------|
| **0** | 1.5B d025 SFT 训练 | 2045/3384 steps (60%), epoch 0.59 | ~1h20m | ~01:37 |
| **1** | 1.5B batch eval → 当前 d100 aligned | GSM8K 23% (301/1319) @ 6.0s/it | ~2.5h (GSM8K+ARC+HumanEval) | ~02:45 |
| **2** | 0.5B d100 eval v4 | GSM8K 39% (511/1319) @ 5.1s/it | ~1h50m | ~02:05 |
| **3** | 0.5B d025 eval | GSM8K 29% (378/1319) @ 5.0s/it | ~2h | ~02:15 |
| **4** | 3B d005 eval | **HumanEval 57% (94/164)** @ 7.4s/it | **~9min** | **~00:25** |
| **5** | **空闲** | d005 para eval 已完成 (00:11) | — | — |

### 即将空出的 GPU

1. **GPU 5** — 已空闲
2. **GPU 4** — ~9 分钟内完成（HumanEval 最后一个 benchmark，剩 70 题）
3. **GPU 0** — ~1h20m（SFT 60%，loss 1.24，token acc 0.72）

### 注意

- GPU 0 的 lora_adapter 目录为空，adapter 尚未保存（训练结束时才写入）
- GPU 1 的 1.5B batch eval 已完成 d000 orig+para、d005 aligned+para，当前跑 d100 aligned（MMLU 完成，GSM8K 进行中）
- GPU 2 的 0.5B d100 aligned 输出目录仍为空，结果尚未写入

---
