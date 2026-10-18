# research dataset scope audit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dataset_scope_audit_20260519T154143_result.json`
- **Structured JSON:** [`55115ff032fdb94c4779.json`](../../sessions/55/55115ff032fdb94c4779.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 1. 训练集包含 40 个唯一 task，1693 个 episode

### 2. 覆盖全部 4 个 LIBERO suite，每个 suite 恰好 10 个 task

### 3. 训练代码无 suite 过滤

`train_smart_compress.py` 直接加载 `HuggingFaceVLA/libero` 全量数据，未做任何 task/suite 筛选。

### 4. 各 suite 的 task 列表

**LIBERO-Spatial (10 tasks, ~430 episodes)** — "pick up the black bowl [位置] and place it on the plate"：
| # | Task | Episodes |
|---|------|----------|
| 30 | pick up the black bowl next to the cookie box and place it on the plate | 46 |
| 31 | pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate | 42 |
| 32 | pick up the black bowl on the ramekin and place it on the plate | 39 |
| 33 | pick up the black bowl on the stove and place it on the plate | 35 |
| 34 | pick up the black bowl between the plate and the ramekin and place it on the plate | 45 |
| 35 | pick up the black bowl on the cookie box and place it on the plate | 43 |
| 36 | pick up the black bowl next to the plate and place it on the plate | 47 |
| 37 | pick up the black bowl next to the ramekin and place it on the plate | 45 |
| 38 | pick up the black bowl from table center and place it on the plate | 46 |
| 39 | pick up the black bowl on the wooden cabinet and place it on the plate | 44 |

**LIBERO-Object (10 tasks, ~455 episodes)** — "pick up the [物品] and place it in the basket"：
| # | Task | Episodes |
|---|------|----------|
| 20 | pick up the orange juice and place it in the basket | 45 |
| 21 | pick up the ketchup and place it in the basket | 45 |
| 22 | pick up the cream cheese and place it in the basket | 45 |
| 23 | pick up the bbq sauce and place it in the basket | 46 |
| 24 | pick up the alphabet soup and place it in the basket | 44 |
| 25 | pick up the milk and place it in the basket | 45 |
| 26 | pick up the salad dressing and place it in the basket | 47 |
| 27 | pick up the butter and place it in the basket | 45 |
| 28 | pick up the tomato sauce and place it in the basket | 42 |
| 29 | pick up the chocolate pudding and place it in the basket | 50 |

**LIBERO-Goal (10 tasks, ~426 episodes)** — 同一场景不同目标：
| # | Task | Episodes |
|---|------|----------|
| 10 | put the bowl on the plate | 49 |
| 11 | put the wine bottle on the rack | 36 |
| 12 | open the top drawer and put the bowl inside | 36 |
| 13 | put the cream cheese in the bowl | 40 |
| 14 | put the wine bottle on top of the cabinet | 47 |
| 15 | push the plate to the front of the stove | 33 |
| 16 | turn on the stove | 50 |
| 17 | put the bowl on the stove | 48 |
| 18 | put the bowl on top of the cabinet | 46 |
| 19 | open the middle drawer of the cabinet | 43 |

**LIBERO-Long (10 tasks, ~382 episodes)** — 多步长任务：
| # | Task | Episodes |
|---|------|----------|
| 0 | put the white mug on the left plate and put the yellow and white mug on the right plate | 38 |
| 1 | put the white mug on the plate and put the chocolate pudding to the right of the plate | 36 |
| 2 | put the yellow and white mug in the microwave and close it | 34 |
| 3 | turn on the stove and put the moka pot on it | 41 |
| 4 | put both the alphabet soup and the cream cheese box in the basket | 43 |
| 5 | put both the alphabet soup and the tomato sauce in the basket | 33 |
| 6 | put both moka pots on the stove | 29 |
| 7 | put both the cream cheese box and the butter in the basket | 49 |
| 8 | put the black bowl in the bottom drawer of the cabinet and close it | 35 |
| 9 | pick up the book and place it in the back compartment of the caddy | 41 |

### 对论文的影响

**`HuggingFaceVLA/libero` 训练集包含全部 4 个 LIBERO suite 的 demo。** 不能声称 Spatial/Goal/Long 上的 eval 是 "unseen cross-suite transfer"——模型在训练时已经见过这些 suite 的 demonstration。

---
