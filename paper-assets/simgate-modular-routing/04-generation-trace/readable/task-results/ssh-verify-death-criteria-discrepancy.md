# ssh verify death criteria discrepancy

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-death-criteria-discrepancy_20260519T104723_result.json`
- **Structured JSON:** [`3cb9f97ede90cc55a5ee.json`](../../sessions/3c/3cb9f97ede90cc55a5ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整分析结果如下。

---

## 核查结论

**两种方法的数字都是"正确"的，差异来源于统计口径不同：**

| 方法 | 定义 | find-animal | lifespan-longest-lived |
|------|------|:-----------:|:----------------------:|
| Method A | `always_internal` 的 death 数 | **8** | **7** |
| Method B | 有任意 mode 死亡的 **episode 数** | **10** | **8** |

---

## find-animal 详细 (20 episodes)

| ep | int_score | int_dead | det_score | det_dead |
|----|-----------|----------|-----------|----------|
| 0  | -100      | **T**    | 8         | F        |
| 1  | 0         | F        | 0         | F        |
| 2  | 8         | F        | 8         | F        |
| 3  | 0         | F        | **-100**  | **T**    |
| 4  | -100      | **T**    | 0         | F        |
| 5  | -100      | **T**    | -100      | **T**    |
| 6  | 0         | F        | 0         | F        |
| 7  | -100      | **T**    | -100      | **T**    |
| 8  | 8         | F        | 8         | F        |
| 9  | -100      | **T**    | 0         | F        |
| 10 | 0         | F        | 0         | F        |
| 11 | 0         | F        | 0         | F        |
| 12 | -100      | **T**    | -100      | **T**    |
| 13 | 0         | F        | 0         | F        |
| 14 | 0         | F        | 0         | F        |
| 15 | -100      | **T**    | 0         | F        |
| 16 | 0         | F        | **-100**  | **T**    |
| 17 | 0         | F        | 17        | F        |
| 18 | -100      | **T**    | 0         | F        |
| 19 | 0         | F        | 0         | F        |

- Internal deaths: **8** (ep 0,4,5,7,9,12,15,18)
- Det deaths: **5** (ep 3,5,7,12,16)
- Both-dead episodes: **3** (ep 5,7,12)
- **Det-only deaths (int alive, det dead): ep 3, 16** → 这 2 个 episode 造成 8→10 的差异

## lifespan-longest-lived 详细 (20 episodes)

| ep | int_score | int_dead | det_score | det_dead |
|----|-----------|----------|-----------|----------|
| 0  | -100      | **T**    | 0         | F        |
| 1  | 0         | F        | 0         | F        |
| 2  | 0         | F        | 0         | F        |
| 3  | -100      | **T**    | 50        | F        |
| 4  | -100      | **T**    | 0         | F        |
| 5  | 0         | F        | **-100**  | **T**    |
| 6  | 0         | F        | 0         | F        |
| 7  | -100      | **T**    | 0         | F        |
| 8  | 0         | F        | 0         | F        |
| 9  | -100      | **T**    | 0         | F        |
| 10-14 | 0     | F        | 0         | F        |
| 15 | -100      | **T**    | 0         | F        |
| 16 | 50        | F        | 50        | F        |
| 17 | 50        | F        | 50        | F        |
| 18 | -100      | **T**    | 0         | F        |
| 19 | 0         | F        | 0         | F        |

- Internal deaths: **7** (ep 0,3,4,7,9,15,18)
- Det deaths: **1** (ep 5)
- **Det-only death: ep 5** → 这 1 个 episode 造成 7→8 的差异

## 全 11 task 汇总

| Task | int_dead | det_dead | total_events | ep_with_any_death | int==ep_any? |
|------|:--------:|:--------:|:------------:|:-----------------:|:------------:|
| chemistry-mix | 9 | 4 | 13 | 9 | YES |
| **find-animal** | **8** | **5** | **13** | **10** | **NO** |
| find-non-living-thing | 0 | 0 | 0 | 0 | YES |
| freeze | 9 | 0 | 9 | 9 | YES |
| grow-fruit | 9 | 1 | 10 | 9 | YES |
| identify-life-stages-1 | 11 | 2 | 13 | 11 | YES |
| identify-life-stages-2 | 9 | 1 | 10 | 9 | YES |
| inclined-plane-determine-angle | 9 | 4 | 13 | 9 | YES |
| **lifespan-longest-lived** | **7** | **1** | **8** | **8** | **NO** |
| lifespan-longest-lived-then-shortest | 10 | 4 | 14 | 10 | YES |
| measure-melting-point-unknown | 10 | 3 | 13 | 10 | YES |

只有 find-animal 和 lifespan-longest-lived 两个 task 出现不一致（NO），因为这两个 task 存在 **det-only death episodes**（internal 存活但 det 死亡）。其余 9 个 task 的 det deaths 全部发生在 internal 也死亡的 episode 中，所以两种统计口径结果相同。

## is_dead vs score==-100 一致性

额外验证：在 `episodes.jsonl` 中，`final_score==-100` 和最后一步 `is_dead==true` 在所有 episode 的所有 mode 中**完全一致**，没有 mismatch。两种判断死亡的方式等价。

---
