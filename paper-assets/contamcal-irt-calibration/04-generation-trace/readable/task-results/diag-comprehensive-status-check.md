# diag comprehensive status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_comprehensive-status-check_20260520T220742_result.json`
- **Structured JSON:** [`b79cb8d46d3685f1b1a1.json`](../../sessions/b7/b79cb8d46d3685f1b1a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29999

| GPU | 任务 | PID | 状态 | 进度详情 |
|-----|------|-----|------|---------|
| cuda:0 | Gemma-2-9B d100 retrain (s0) | 437077 | RUNNING (3h56m) | 46/4159 (1%), ~3.6s/it, ETA ~4.1h |
| cuda:1 | Gemma-2 MMLU eval sweep (s0) | 437235 | RUNNING (3h52m) | 当前批次 4613/14042 (33%), ~21 it/s; 多 dosage 轮次中 |
| cuda:2 | Gemma-2 ARC eval (d005_s0) | 440101 | RUNNING (37m) | 164/1172 (14%), ~6.7 it/s, ETA ~2.5min 本轮 |
| cuda:3 | Qwen-14B s0 sweep (train) | 435054 | RUNNING (13h07m) | d000-d050 已完成; **d100 训练中** 238/4159 (6%), ~3.1s/it, ETA ~3.4h |

**DGP**: PID 435321, RUNNING (12h47m), **102/400** (26%), elapsed 800s 本轮, ETA ~39min

## cqa1-21977

| GPU | 任务 | PID | 状态 | 进度详情 |
|-----|------|-----|------|---------|
| cuda:0 | Qwen-7B s0 sweep (train d100) | 389216 | RUNNING (3h48m) | d000→d005→d025→d050 已完成; **d100** 3661/4159 (88%), ~3.5s/it, **ETA ~29min** |

Qwen-7B 各 dosage 时间线: d000 10:36 → d005 14:21 → d025 18:16 → d050 22:12 → d100 02:20 (均为 5/20-21 CST)

---
