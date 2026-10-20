# ssh crafter seed patch demo

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_crafter-seed-patch-demo_20260518T042352_result.json`
- **Structured JSON:** [`02086bb976aa323ea443.json`](../../sessions/02/02086bb976aa323ea443.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 5 Episode 基础统计（seed=42, random agent）

| Episode | Steps | Reward | Death | Final Health | Achievements |
|---------|-------|--------|-------|--------------|-------------|
| 0 | 180 | 3.10 | Yes | 0 | collect_sapling, collect_wood, place_plant, place_table, wake_up |
| 1 | 40 | -0.90 | Yes | 0 | (none) |
| 2 | 135 | 2.10 | Yes | 0 | collect_sapling, place_plant, wake_up |
| 3 | 254 | 2.10 | Yes | 0 | collect_sapling, place_plant, wake_up |
| 4 | 148 | 0.10 | Yes | 0 | wake_up |

### 确定性验证：**通过**
两次 `PYTHONHASHSEED=0 python episode_runner.py --seed 42` 的 JSON 输出完全一致（`diff` 为空）。

### 修改内容
1. **seed_patch.py** — 创建完成，替换 `World._chunks` 的 `set` 为 `OrderedSet`
2. **episode_runner.py** — 三处修改：
   - 导入并调用 `apply_determinism_patch()`
   - 添加 `random.seed()` + `np.random.seed()` 全局 RNG seeding
   - 添加 `--output` 参数支持

### 注意
运行时需要 `PYTHONHASHSEED=0`，因为 crafter 的 `Env.reset()` 用 `hash((seed, episode))` 计算 per-episode seed，Python 3 的 `hash()` 默认随机化。

---
