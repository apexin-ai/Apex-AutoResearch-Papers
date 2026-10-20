# diag qwen14b s0 mmlu results and arc eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen14b-s0-mmlu-results-and-arc-eval_20260520T201249_result.json`
- **Structured JSON:** [`5f0d0feda016f9da91be.json`](../../sessions/5f/5f0d0feda016f9da91be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data gathered. Here's the situation:

## Qwen-14B s0 MMLU Results
**Status: NOT AVAILABLE — s0 training still in progress**

Training sweep timeline (cuda:3):
- d000: done (May 20, 20:38)
- d005: done (May 21, 00:09) — 3h31m
- d025: done (May 21, 03:46) — 3h37m
- d050: **training now** (started ~03:46, ~3.5h per dosage → ETA ~07:20)
- d100: **not started** → ETA ~10:50

MMLU eval cannot run until all 5 dosage checkpoints are complete (~7 more hours).

### Existing s42/s123 MMLU data for reference

| Dosage | s42 | s123 |
|--------|---------|---------|
| d000   | 69.44%  | 68.67%  |
| d005   | 69.01%  | 70.84%  |
| d025   | 62.04%  | 63.68%  |
| d050   | 59.41%  | 60.99%  |
| d100   | 60.07%  | 55.93%  |

- s42: Δ(d100−d0) = **−9.37pp**
- s123: Δ(d100−d0) = **−12.74pp**

(Note: 任务描述中 s42/s123 标签反了 — 实际数据 s42=−9.37pp, s123=−12.74pp)

## n=3 MMLU Bootstrap
**Status: BLOCKED — 需要 s0 数据**

Bootstrap 脚本已就绪：`/root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py`

## ARC s0 Eval
**Status: NOT STARTED — checkpoints not ready**

cuda:0 空闲，ARC eval 脚本模板已有 (`eval_qwen14b_arc_s42.sh`)，MMLU eval 脚本也已存在 (`eval_qwen14b_s0_mmlu.sh`)。等 s0 训练全部完成后，MMLU eval 应先于 ARC eval 运行。

### 下一步
训练完成后需依次：
1. 跑 MMLU s0 eval（脚本已就绪）
2. 跑 ARC s0 eval（需创建脚本）
3. n=3 bootstrap（3 个 seed 的 Δ(d100) 值）

---
