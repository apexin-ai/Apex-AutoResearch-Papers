# monitor baseline eval check 20260522

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_baseline-eval-check-20260522_20260522T231528_result.json`
- **Structured JSON:** [`bd6015686efc252162e4.json`](../../sessions/bd/bd6015686efc252162e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## SmolVLA Baseline Eval — 全部完成

| experiment_id | status | success_rate |
|---|---|---|
| eval-smolvla-lerobot-spatial-seed43-v3 | **DONE** | 54.5% |
| eval-smolvla-lerobot-goal-seed43-v3 | **DONE** | 82.0% |
| eval-smolvla-lerobot-goal-seed44-v3 | **DONE** | 78.0% |

## SmolVLA 4-Suite Baseline (3-seed mean±std) — 全部齐全

| Suite | seed42 | seed43 | seed44 | Mean±Std |
|---|---|---|---|---|
| Object | 66.5% | 66.5% | 65.0% | **66.0%±0.9%** |
| Spatial | 59.5% | 54.5% | 60.0% | **58.0%±3.0%** |
| Goal | 75.5% | 82.0% | 78.0% | **78.5%±3.3%** |
| Long | — | — | — | **50.8%±2.3%** |

## CRM 4-Suite 训练

**train-crm-unified-4suite-r5**: epoch 28/50 (~56%), loss ~0.011, bjb1-32546 GPU3。

Registry 已将 3 个 eval 从 RUNNING → DONE。产出写入 `artifacts/smolvla_baseline_status_20260522.md`。

---
