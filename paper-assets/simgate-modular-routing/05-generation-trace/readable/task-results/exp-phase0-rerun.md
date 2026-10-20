# exp phase0 rerun

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phase0-rerun_20260513T052947_result.json`
- **Structured JSON:** [`e6a77952c4f404b72c1e.json`](../../sessions/e6/e6a77952c4f404b72c1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 0 结果报告

### 1. 代码部署状态
4 项修复全部已部署确认：`_last_score` 追踪、task name 修正、variation 越界修复、random.seed(42)。

### 2. PHASE 0 GATE: **PASS**

### 3. 各 task type 结果

| Task Type | Variations | 成功率 | 平均延迟 |
|-----------|-----------|--------|---------|
| boil | 4/4 | 100% | 1.64s |
| melt | 3/3 | 100% | 1.76s |
| change-the-state-of-matter-of | 3/3 | 100% | 1.76s |
| chemistry-mix-paint-secondary-color | 2/2 | 100% | 1.56s |
| grow-plant | 2/2 | 100% | 1.50s |

**总计**: 14/14 = 100% 成功率，p95 延迟 2.38s（gate <5s），所有 fork 的 obs_match 和 score_match 均为 True。

### 4. 输出文件
`/root/autodl-tmp/simgate-modular-routing/results/mvp/phase0_validation_v2.json`

### 5. 无失败项
全部通过，无异常。Phase 1 可以启动。

---
