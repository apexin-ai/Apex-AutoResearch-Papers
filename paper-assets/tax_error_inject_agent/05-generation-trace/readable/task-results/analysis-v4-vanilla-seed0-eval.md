# analysis v4 vanilla seed0 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-vanilla-seed0-eval_20260514T190222_result.json`
- **Structured JSON:** [`fcc49eda746e6837c97b.json`](../../sessions/fc/fcc49eda746e6837c97b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v4-vanilla-seed0-eval 结果

### 总体

| 指标 | 值 |
|------|-----|
| 成功率 | **68.1% (32/47)** |
| 平均步数（全部） | 26.04 |
| 平均步数（成功） | 14.81 |
| 平均步数（失败） | 50.0（全部触顶） |

### 按任务类型

| Task Type | Seed=0 | Seed=42 | Delta |
|-----------|--------|---------|-------|
| look_at_obj_in_light | 5/6 (83.3%) | 5/6 (83.3%) | 0 |
| pick_and_place_simple | 5/8 (62.5%) | 5/8 (62.5%) | 0 |
| pick_clean_then_place | 6/11 (54.5%) | 5/11 (45.5%) | +1 |
| pick_cool_then_place | 4/7 (57.1%) | 4/7 (57.1%) | 0 |
| pick_heat_then_place | **7/8 (87.5%)** | 6/8 (75.0%) | +1 |
| pick_two_obj_and_place | 5/7 (71.4%) | 4/7 (57.1%) | +1 |

### Baseline 对比

| 实验 | 成功率 | vs seed0 |
|------|--------|----------|
| **v4-vanilla seed=0** | **68.1% (32/47)** | — |
| v4-vanilla seed=42 | 61.7% (29/47) | -6.4pp |
| v4-taxei seed=42 | 61.7% (29/47) | -6.4pp |
| v4-random seed=42 | 66.0% (31/47) | -2.1pp |
| zero-shot | 42.6% (20/47) | -25.5pp |

### McNemar Test (seed=0 vs seed=42)

| | seed42 OK | seed42 FAIL |
|---|-----------|-------------|
| **seed0 OK** | 28 | 4 |
| **seed0 FAIL** | 1 | 14 |

- 不一致对 (discordant pairs): b=4, c=1
- seed0 独赢任务: Spatula-Drawer, Bread-CounterTop, Egg-GarbageCan, KeyChain-Safe
- seed42 独赢任务: Pan-CounterTop
- **Exact binomial p = 0.375 (双侧)**, 差异不显著
- 结论：seed=0 多赢 3 个任务，但仅 5 个不一致对，在正常 seed 方差范围内

产出文件: `artifacts/eval/v4_vanilla_seed0_eval_analysis.json`（含完整 47 个 episode 的逐任务对比数据）

---
