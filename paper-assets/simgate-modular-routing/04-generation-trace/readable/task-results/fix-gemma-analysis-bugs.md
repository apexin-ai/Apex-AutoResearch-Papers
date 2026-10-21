# fix gemma analysis bugs

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gemma-analysis-bugs_20260520T235853_result.json`
- **Structured JSON:** [`54c830080d0c568cecf5.json`](../../sessions/54/54c830080d0c568cecf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 修改内容

**Bug 1 — label 字符串**：`"int-preferred"` → `"internal-preferred"`（`per_task_breakdown` 和 `compute_aggregate` 两处）

**Bug 2 — DR 死亡定义**：`score == 0` → `score <= -100`，与 `compute_cross_model_cis.py` 一致（6 处：`per_task_breakdown` 2 处、`compute_aggregate` 3 处、`stat_int_dr`/`stat_det_dr`/`stat_daf` 各 1 处）。alive 定义 `> 0` → `> -100`（`compute_aggregate` 和 `stat_daf` 各 1 处）

**Bug 3 — 重复数据**：`load_episodes` 中增加 `seen_ids` 去重，`find-non-living-thing` 从 35 条 → 20 条

---

## 修复后完整输出

```
Loaded 220 episodes (11 tasks × 20 each)

PER-TASK BREAKDOWN
Task                                            N    Det-Pref    Int-Pref     No-Pref   IntDR   DetDR
identify-life-stages-1                         20   7 (35.0%)   1 ( 5.0%)  12 (60.0%)   40.0%   10.0%
identify-life-stages-2                         20   5 (25.0%)   0 ( 0.0%)  15 (75.0%)   35.0%   10.0%
freeze                                         20   5 (25.0%)   0 ( 0.0%)  15 (75.0%)   35.0%   10.0%
grow-fruit                                     20   4 (20.0%)   0 ( 0.0%)  16 (80.0%)   35.0%   15.0%
measure-melting-point-unknown-substance        20   7 (35.0%)   0 ( 0.0%)  13 (65.0%)   40.0%   10.0%
lifespan-longest-lived                         20   4 (20.0%)   1 ( 5.0%)  15 (75.0%)   40.0%   25.0%
lifespan-longest-lived-then-shortest-lived     20   7 (35.0%)   0 ( 0.0%)  13 (65.0%)   45.0%   10.0%
chemistry-mix                                  20   3 (15.0%)   1 ( 5.0%)  16 (80.0%)   40.0%   30.0%
inclined-plane-determine-angle                 20   6 (30.0%)   1 ( 5.0%)  13 (65.0%)   40.0%   15.0%
find-animal                                    20   6 (30.0%)   0 ( 0.0%)  14 (70.0%)   50.0%   20.0%
find-non-living-thing                          20   9 (45.0%)   3 (15.0%)   8 (40.0%)    0.0%    0.0%

AGGREGATE METRICS
  Total episodes:         220
  Det-preferred:           63  (28.6%)
  Int-preferred:            7  (3.2%)
  No-preference:          150  (68.2%)
  Mean internal score:    -33.73
  Mean det score:         -8.72
  Internal DR:            36.4%
  Deterministic DR:       14.1%
  ΔDR (int - det):        +22.3pp
  Δ_full:                 -25.0091
  Δ_nd (n=136):          -2.5882
  DAF:                    89.7%

BOOTSTRAP 95% CIs (cluster, K=11)
  Internal DR:   36.4% [28.2,41.8]
  Det DR:        14.1% [9.5,19.1]
  ΔDR:           +22.3pp [16.4,27.7]
  DAF:           89.7% [68.8,100.0]

CROSS-MODEL COMPARISON (ScienceWorld)
Model               Int DR                  Det DR                    ΔDR                    DAF
Qwen2.5-7B          42.9% [36.7,49.0]  16.3% [11.8,21.2]  +26.5pp [20.4,32.7]  90.4% [81.3,99.1]
Llama-3.1-8B        41.4% [35.0,47.7]  11.4% [7.3,15.9]   +30.0pp [23.6,36.4]  88.2% [80.2,95.1]
Gemma-2-9B          36.4% [28.2,41.8]  14.1% [9.5,19.1]   +22.3pp [16.4,27.7]  89.7% [68.8,100.0]
```

`analysis.json` 和 `cross_model_table.tex` 均已更新到 `results/gemma_scienceworld_counterfactual/`。

---
