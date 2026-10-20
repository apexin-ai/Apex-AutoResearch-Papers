# infra model check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_model-check_20260513T045724_result.json`
- **Structured JSON:** [`00afc2f8db35e83d3fc3.json`](../../sessions/00/00afc2f8db35e83d3fc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. 模型下载状态：进行中

- PID 1869 仍在运行，已下载约 8 分钟
- 4 个 shard 并行下载，当前进度 ~21-22%，速度 ~1.7-2.4 MB/s
- 每 shard ~3.6GB，预计总剩余时间 **~25-30 分钟**
- 路径：`/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct/`

### 2. ScienceWorld 全部 30 个 Task Names

| # | Task Name | Max Variations |
|---|-----------|---------------|
| 0 | boil | 30 |
| 1 | change-the-state-of-matter-of | 30 |
| 2 | chemistry-mix | 32 |
| 3 | chemistry-mix-paint-secondary-color | 36 |
| 4 | chemistry-mix-paint-tertiary-color | 36 |
| 5 | find-animal | 300 |
| 6 | find-living-thing | 300 |
| 7 | find-non-living-thing | 300 |
| 8 | find-plant | 300 |
| 9 | freeze | 30 |
| 10 | grow-fruit | 126 |
| 11 | grow-plant | 126 |
| 12 | identify-life-stages-1 | 14 |
| 13 | identify-life-stages-2 | 10 |
| 14 | inclined-plane-determine-angle | 168 |
| 15 | inclined-plane-friction-named-surfaces | 1386 |
| 16 | inclined-plane-friction-unnamed-surfaces | 162 |
| 17 | lifespan-longest-lived | 125 |
| 18 | lifespan-longest-lived-then-shortest-lived | 125 |
| 19 | lifespan-shortest-lived | 125 |
| 20 | measure-melting-point-known-substance | 436 |
| 21 | measure-melting-point-unknown-substance | 300 |
| 22 | melt | 30 |
| 23 | mendelian-genetics-known-plant | 120 |
| 24 | mendelian-genetics-unknown-plant | 480 |
| 25 | power-component | 20 |
| 26 | power-component-renewable-vs-nonrenewable-energy | 20 |
| 27 | test-conductivity | 900 |
| 28 | test-conductivity-of-unknown-substances | 600 |
| 29 | use-thermometer | 540 |

### 3. 目标 Task 精确名称与 Variation 分布

| Task | Max | Train | Dev | Test |
|------|-----|-------|-----|------|
| **boil** | 30 | 14 (0-13) | 7 (14-20) | 9 (21-29) |
| **melt** | 30 | 14 (0-13) | 7 (14-20) | 9 (21-29) |
| **change-the-state-of-matter-of** | 30 | 14 (0-13) | 7 (14-20) | 9 (21-29) |
| **chemistry-mix-paint-secondary-color** | 36 | 18 (0-17) | 9 (18-26) | 9 (27-35) |
| **grow-plant** | 126 | 62 (0-61) | 31 (62-92) | 33 (93-125) |

### 4. ScienceWorld API 用法

**核心方法签名：**

```python
env = scienceworld.ScienceWorldEnv("")

# 加载任务
env.load(taskName: str, variationIdx: int = 0, simplificationStr: str = '', generateGoldPath: bool = False) -> None

# 重置
obs, info = env.reset()  # -> Tuple[str, Dict[str, Any]]

# 执行动作
obs, reward, done, info = env.step(input_str: str)  # -> Tuple[str, int, bool, Dict]

# info dict 包含:
#   moves: int, score: int, reward: int,
#   look: str, inv: str, taskDesc: str,
#   valid: list[str], variationIdx: int, taskName: str, simplificationStr: str

# 其他方法
env.get_valid_action_object_combinations() -> list[str]  # 当前可用动作列表（~400个）
env.get_task_description() -> str
env.get_goal_progress() -> str                           # 子目标完成状态
env.get_gold_action_sequence() -> list[str]              # 需 load 时 generateGoldPath=True
env.get_max_variations(task_name: str) -> int
env.get_variations_train() -> list[int]                  # 需先 load
env.get_variations_dev() -> list[int]
env.get_variations_test() -> list[int]
env.look() -> str
env.inventory() -> str
env.get_possible_simplifications() -> list[str]
env.close()
```

**Step limit**: 100 步/episode

**Simplification options**: `noElectricalAction`, `openContainers`, `openDoors`, `selfWateringFlowerPots`, `teleportAction`

### 5. 与文档不一致之处

- **没有 `get_num_variations()`** — 应使用 `get_max_variations(task_name)`
- **没有 `get_score()`** — score 在 `info['score']` 中返回
- **`get_variations_train/dev/test()` 不接受 task name 参数** — 必须先 `load()` 再调用
- **Gold path 需要显式启用** — `load(..., generateGoldPath=True)`，否则返回错误字符串
- **`step()` 的 reward 类型是 `int` 而非 `float`**
- **CamelCase API 已废弃** — 应使用 snake_case 版本（如 `get_valid_action_object_combinations` 而非 `getValidActionObjectCombinations`）

---
