# analysis harvest bootstrap ci

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_harvest_bootstrap_ci_20260522T193052_result.json`
- **Structured JSON:** [`fe22a5a4096220fde0ba.json`](../../sessions/fe/fe22a5a4096220fde0ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地文件已存在且内容一致，无需更新。

## Bootstrap CI 结果（已完成）

| 指标 | 值 |
|------|-----|
| **mean_divergence_pp** | **31.7pp** |
| **ci_95_lower** | **3.2pp** |
| **ci_95_upper** | **48.4pp** |
| **p_value** | **0.015** |
| cr_layer_median | L2 |
| pr_layer_median | L14 |
| valid_iterations | 1000/1000 |
| reference divergence | 38.7pp |
| runtime | 2205s (~37min) |

所有指标与预期完全吻合。CI 下界 3.2pp > 0 且 p=0.015 < 0.05，divergence 统计显著。

---
