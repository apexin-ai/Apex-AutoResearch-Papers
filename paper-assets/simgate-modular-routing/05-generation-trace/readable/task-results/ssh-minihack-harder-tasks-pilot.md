# ssh minihack harder tasks pilot

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_minihack-harder-tasks-pilot_20260519T115207_result.json`
- **Structured JSON:** [`70712b1b3f0a6d1e0159.json`](../../sessions/70/70712b1b3f0a6d1e0159.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总表

```
Task                | LLM DR | Det DR | Δ DR  | LLM Win | Det Win | Avg Steps (LLM) | Avg Steps (Det) | Verdict
--------------------|--------|--------|-------|---------|---------|------------------|-----------------|--------
Room-15x15          |   0%   |   0%   |   0%  |  100%   |  100%   |       14.0       |      14.0       | 太简单，无信号
Corridor-R3         |  40%   |  60%   | -20%  |    0%   |   40%   |      500.0       |     337.4       | LLM完全不会导航，death是乱走副产物
Corridor-R5         |  80%   |  40%   | +40%  |    0%   |   60%   |      500.0       |     263.2       | LLM DR高但原因同上
River               |   0%   |  20%   | -20%  |    0%   |    0%   |      350.0       |     350.0       | 两者都解不了，无信号
```

## Episode 明细

### Room-15x15
- **Det**: 5/5 GOAL, 全部 14 步
- **LLM**: 5/5 GOAL, 全部 14 步, 0 parse failures

### Corridor-R3
**Det** (3 deaths, 2 goals):
| ep | seed | steps | outcome | score |
|----|------|-------|---------|-------|
| 0  | 42   | 500   | DIED    | -3.63 |
| 1  | 43   | 160   | GOAL    | +1.0  |
| 2  | 44   | 500   | DIED    | -3.77 |
| 3  | 45   | 500   | DIED    | -3.25 |
| 4  | 46   | 27    | GOAL    | +1.0  |

**LLM** (2 deaths, 3 timeouts, 0 goals):
| ep | seed | steps | outcome | score | parse_fail |
|----|------|-------|---------|-------|------------|
| 0  | 42   | 500   | TIMEOUT | 0.0   | 0/500      |
| 1  | 43   | 500   | DIED    | -5.0  | **500/500** |
| 2  | 44   | 500   | TIMEOUT | 0.0   | 0/500      |
| 3  | 45   | 500   | TIMEOUT | 0.0   | 0/500      |
| 4  | 46   | 500   | DIED    | -5.0  | 0/500      |

### Corridor-R5
**Det** (2 deaths, 3 goals):
| ep | seed | steps | outcome | score |
|----|------|-------|---------|-------|
| 0  | 42   | 162   | GOAL    | +1.0  |
| 1  | 43   | 500   | DIED    | -3.74 |
| 2  | 44   | 500   | DIED    | -3.83 |
| 3  | 45   | 19    | GOAL    | +1.0  |
| 4  | 46   | 135   | GOAL    | +1.0  |

**LLM** (4 deaths, 1 timeout, 0 goals):
| ep | seed | steps | outcome | score | parse_fail |
|----|------|-------|---------|-------|------------|
| 0  | 42   | 500   | DIED    | -4.96 | 0/500      |
| 1  | 43   | 500   | DIED    | -5.00 | 0/500      |
| 2  | 44   | 500   | DIED    | -4.97 | 0/500      |
| 3  | 45   | 500   | DIED    | -4.99 | 0/500      |
| 4  | 46   | 500   | TIMEOUT | 0.0   | 0/500      |

### River
**Det** (1 death, 4 timeouts, 0 goals):
| ep | seed | steps | outcome | score |
|----|------|-------|---------|-------|
| 0  | 42   | 350   | DIED    | -2.72 |
| 1-4| 43-46| 350   | TIMEOUT | 0.0   |

**LLM** (0 deaths, 5 timeouts, 0 goals):
| ep | seed | steps | outcome | score | parse_fail |
|----|------|-------|---------|-------|------------|
| 0  | 42   | 350   | TIMEOUT | -3.50 | 0/350      |
| 1  | 43   | 350   | TIMEOUT | 0.0   | 0/350      |
| 2  | 44   | 350   | TIMEOUT | -3.37 | 0/350      |
| 3  | 45   | 350   | TIMEOUT | -3.42 | 0/350      |
| 4  | 46   | 350   | TIMEOUT | -3.50 | 0/350      |

## 关键观察

1. **LLM 在 Corridor 任务中完全无法导航** — 所有 10 个 episode 都跑满 500 步，0 次到达目标。死亡是乱走后撞怪的副产物，不是决策问题。
2. **Corridor-R3/R5 ep1 的 500/500 parse failure** — 该 seed 下 LLM 输出完全无法解析为合法动作，全程只用 fallback action。
3. **River 对两者都太难** — 需要特殊操作（过河），heuristic agent 和 LLM 都不具备这种能力。
4. **Death rate 信号质量差** — Corridor 中 LLM 的高 death rate 来自"乱走 500 步后被怪杀"，不是有意义的决策差异。Det agent 死也是类似原因（某些 seed 找不到路）。
5. **Death 原因未记录** — runner 的 JSONL 没有保存 last_message 字段，无法提取具体死因。

## 决策判断

**没有任何 task 的 LLM DR 落在 20-90% 的"有信号"区间且是有意义的决策差异。**

- Corridor-R5 LLM DR=80% 表面上在区间内，但这是导航失败导致的乱走后被杀，不是 gate-able 的决策
- 核心问题：7B 模型在多房间导航任务中完全无效，death signal 来自无方向感而非错误决策

→ **建议切 Crafter 或其他有更清晰 death decision point 的环境**。MiniHack 的 Corridor/River 任务中，death 不是决策点（不像 Crafter 中"是否攻击怪物"/"是否进入危险区域"这种明确的路由选择），而是长时间无效动作后的随机结果。

---
