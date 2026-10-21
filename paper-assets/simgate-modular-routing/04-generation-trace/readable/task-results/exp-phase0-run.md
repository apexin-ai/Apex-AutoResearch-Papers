# exp phase0 run

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phase0-run_20260513T045900_result.json`
- **Structured JSON:** [`80e440c3f1db4494aeca.json`](../../sessions/80/80e440c3f1db4494aeca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 0 结果报告

### GATE 判定：**PASS**

### Fork 成功率
**10/10 = 100%**（门槛 ≥80%）

### Fork 延迟
| 指标 | 值 |
|------|------|
| avg | 1.67s |
| p50 | 1.53s |
| p95 | 2.37s |

p95 < 5s ✓

### 内存
最大 RSS: 20 MB

### 每个 task type 结果

| Task | 成功率 | 平均延迟 | obs_match | score_match |
|------|--------|----------|-----------|-------------|
| boil | 4/4 | 1.56s | 全部 True | 全部 True |
| melt | 3/3 | 1.77s | 全部 True | 全部 True |
| change-the-state-of-matter-of | 3/3 | 1.72s | 全部 True | 全部 True |

### ScienceWorld 实际 task type 名称（30 个）
关键名称与代码配置的对应：
- `boil` ✓ 精确匹配
- `melt` ✓ 精确匹配
- `change-the-state-of-matter-of` ✓ 精确匹配
- `chemistry-mix-paint-secondary-color`（注意：无尾 `s`，已在修复中更正）
- `grow-plant` ✓ 精确匹配

### 修复内容
运行前修复了 `scienceworld_utils.py`：
1. `get_score()` — ScienceWorld 1.2.3 无 `getScore()`/`get_score()` 方法，改用 `step()` 返回的 `info['score']` 缓存
2. `get_valid_actions()` — 改用 snake_case API `get_valid_action_object_combinations()`
3. `MEDIUM_TASKS` 名称 — `chemistry-mix-paint-secondary-colors` → `chemistry-mix-paint-secondary-color`

---
