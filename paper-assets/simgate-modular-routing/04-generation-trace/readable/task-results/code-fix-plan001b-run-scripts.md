# code fix plan001b run scripts

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-plan001b-run-scripts_20260513T221012_result.json`
- **Structured JSON:** [`bb645483bf8b4c81344c.json`](../../sessions/bb/bb645483bf8b4c81344c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 修复结果

**run_plan001b_gpu0.sh** — 已修复：
- `collect_trajectories.py` → `episode_level_collection.py`
- 任务更新为 7 tasks: find-animal, identify-life-stages-1, lifespan-longest-lived-then-shortest-lived, lifespan-longest-lived, measure-melting-point-unknown-substance, freeze, chemistry-mix
- 添加 `--reuse_dirs results/prescreening,results/mvp,results/research`
- 输出改为 `results/plan_c/`

**run_plan001b_gpu1.sh** — 已修复：
- `collect_trajectories.py` → `episode_level_collection.py`
- 任务更新为 4 tasks: find-non-living-thing, grow-fruit, inclined-plane-determine-angle, identify-life-stages-2
- 同样添加 `--reuse_dirs` 和 `results/plan_c/` 输出

## Dry-run 验证结果

| 验证项 | 状态 |
|--------|------|
| `episode_level_collection.py --dry_run` | 通过 — reuse adapter 正确识别 prescreening 中已有 episodes |
| `death_decomposition.py --data_dirs results/prescreening` | 通过 — 正确读取 episodes.jsonl 并输出分解表 |
| `death_aware_labeling.py --input_dirs results/prescreening/find-animal` | 通过 — 三标签输出正常 (det-preferred: 3, no-preference: 2, 150 SFT steps) |

Pipeline 格式兼容性确认，可以启动数据收集。

---
