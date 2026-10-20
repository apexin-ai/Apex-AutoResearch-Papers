# analysis grow plant fix and planc verify

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grow-plant-fix-and-planc-verify_20260513T195156_result.json`
- **Structured JSON:** [`2e30606e2ebe53886f4c.json`](../../sessions/2e/2e30606e2ebe53886f4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

### 任务 A: grow-plant 分类修正

**根因**：旧 `classify_signal(delta, delta_no_death)` 不考虑 death rate，当 `delta=0, delta_nd=0` 时走进 `delta_no_death <= 0` 分支 → 错误输出 "death-dominated"。

**修复**：新 `classify_signal(delta, delta_no_death, i_death_pct, d_death_pct)` 按六条规则分类，新增 "no-effect" 类别。同时添加了 `--data_dir` / `--output` CLI 参数支持。

**MVP 结果**：

| Task | Signal_type |
|------|------------|
| boil | death-dominated |
| change-the-state-of-matter-of | death-dominated |
| chemistry-mix-paint-secondary-color | death-dominated |
| **grow-plant** | **no-effect** ✓ |
| melt | death-dominated |

**Prescreening 结果**：5 death-dominated, 6 mixed, 1 internal-preferred, 0 no-effect（符合预期，prescreening 没有零死亡+零差异的 task）

---

### 任务 B: Plan C 代码文件状态

| 文件 | 大小 | 最后修改 |
|------|------|---------|
| `src/episode_level_collection.py` | 13,874 B | May 14 01:40 |
| `src/death_aware_labeling.py` | 6,936 B | May 14 03:12 |
| `src/router_sft_train.py` | 12,752 B | May 14 02:33 |
| `src/rule_based_routing.py` | 11,559 B | May 14 02:33 |

四个文件全部就绪。

---
