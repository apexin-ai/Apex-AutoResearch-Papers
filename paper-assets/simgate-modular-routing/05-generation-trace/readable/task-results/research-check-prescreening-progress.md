# research check prescreening progress

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check-prescreening-progress_20260513T214841_result.json`
- **Structured JSON:** [`9708c45654a36fc174b8.json`](../../sessions/97/9708c45654a36fc174b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在有完整的信息了。

---

## GPU0 (pid=649681) — 25 tasks 总计

### 已完成 (16/25)
| # | Task Type | 完成时间 |
|---|-----------|---------|
| 1 | chemistry-mix | 00:42 |
| 2 | chemistry-mix-paint-tertiary-color | 01:02 |
| 3 | find-animal | 01:23 |
| 4 | find-living-thing | 01:42 |
| 5 | find-non-living-thing | 02:02 |
| 6 | find-plant | 02:22 |
| 7 | freeze | 02:42 |
| 8 | grow-fruit | 03:02 |
| 9 | identify-life-stages-1 | 03:21 |
| 10 | identify-life-stages-2 | 03:44 |
| 11 | inclined-plane-determine-angle | 04:03 |
| 12 | inclined-plane-friction-named-surfaces | 04:21 |
| 13 | inclined-plane-friction-unnamed-surfaces | 04:41 |
| 14 | lifespan-longest-lived | 04:59 |
| 15 | lifespan-longest-lived-then-shortest-lived | 05:19 |
| 16 | lifespan-shortest-lived | 05:36 |

### 正在运行
- **measure-melting-point-known-substance** — 已跑 ~13 分钟 (05:36 开始)

### 剩余 (8 tasks，但与 GPU1 重叠)
`measure-melting-point-unknown-substance` → `mendelian-genetics-known-plant` → `mendelian-genetics-unknown-plant` → `power-component` → `power-component-renewable-vs-nonrenewable-energy` → `test-conductivity` → `test-conductivity-of-unknown-substances` → `use-thermometer`

**注意：GPU0 脚本没有 "skip if directory exists" 逻辑，会重跑 GPU1 已完成的这 8 个 task。**

---

## GPU1 (pid=265929) — 8 tasks 总计

### 已完成 (7/8)
| # | Task Type | 完成时间 |
|---|-----------|---------|
| 1 | measure-melting-point-unknown-substance | 03:53 |
| 2 | mendelian-genetics-known-plant | 04:12 |
| 3 | mendelian-genetics-unknown-plant | 04:30 |
| 4 | power-component | 04:48 |
| 5 | power-component-renewable-vs-nonrenewable-energy | 05:07 |
| 6 | test-conductivity | 05:26 |
| 7 | test-conductivity-of-unknown-substances | 05:45 |

### 正在运行
- **use-thermometer** — 已跑 ~1 分钟 (05:48 开始)

### 剩余
无。use-thermometer 是最后一个。

---

## 耗时估算
- **每 task 约 18-20 分钟**（GPU0 平均 ~19.6 min，GPU1 平均 ~19 min）
- GPU0 剩余 8+1(当前)=9 tasks → 预计还需 **~2.8 小时**
- GPU1 剩余 1 task (当前) → 预计 **~18 分钟后完成**

---

## 数据格式兼容性

### episode_level_collection.py 输出
- `{task_type}/episodes.jsonl` — 每行一个 JSON：
  ```
  {episode_idx, variation_idx, always_internal: {final_score, steps: [{step, action, modality, observation, score_before, score_after, ...}]}, always_deterministic: {同结构}}
  ```

### death_aware_labeling.py 期望输入
- `--input_dirs` 指向含 `episodes.jsonl` 的 task 目录
- 读取 `always_internal.final_score` / `always_deterministic.final_score` 做 3-label 分类 (internal-preferred / det-preferred / no-preference)
- 读取 winner 方的 `steps` 提取 SFT 训练三元组

### 格式兼容吗？
**兼容。** 预筛产出的 `episodes.jsonl`（如 `chemistry-mix/episodes.jsonl`）结构与 `death_aware_labeling.py` 期望的完全一致：有 `always_internal` / `always_deterministic` 两个 key，各含 `final_score` 和 `steps` 数组。预筛数据可以直接喂给 `death_aware_labeling.py`，无格式断裂。

---
