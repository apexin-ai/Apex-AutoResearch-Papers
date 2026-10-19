# analysis harvest sensitivity final

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_harvest_sensitivity_final_20260522T222039_result.json`
- **Structured JSON:** [`0d8785ee3a13cf97d65d.json`](../../sessions/0d/0d8785ee3a13cf97d65d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v3 仍在运行。** Threshold ≥3 进度 64/128，ETA ~65 min（从该 checkpoint 算起）。

现有的 `advbench_classifier_sensitivity.json` 是之前 v2 运行的结果（时间戳 05:57），与 v3 日志数值不同。

## v3 当前结果（2/3 thresholds 完成）

| | Threshold ≥1 | Threshold ≥2 | Threshold ≥3 |
|---|---|---|---|
| **样本数** | 159 JB / 361 safe | 304 JB / 216 safe | 453 JB / 67 safe |
| **JB rate** | 30.6% | 58.5% | 87.1% |
| **CR-composite best** | L2 (6.5%) = 0.306 | L0 (0.0%) = 0.430 | *running...* |
| **Precision best** | L12 (38.7%) = 0.725 | L5 (16.1%) = 0.892 | *running...* |
| **Divergence** | 32.2pp | 16.1pp | *running...* |
| **Replicated (>15pp)** | Yes | Yes | *pending* |

## 与已有 JSON (v2) 的差异

v2 JSON 给出 threshold ≥1 divergence = 58.0pp，v3 日志给出 32.2pp。Threshold ≥2 接近（16.2 vs 16.1）。best layer 位置也不同（v2: L3/L21，v3: L2/L12）。v3 可能使用了不同的 window size 或参数。

**建议等 v3 完成后再收割。** 按 ETA 估算，threshold ≥3 大约还需 ~60 min（96/128 和 128/128 两个 checkpoint）。完成后脚本会覆写 JSON。

---
