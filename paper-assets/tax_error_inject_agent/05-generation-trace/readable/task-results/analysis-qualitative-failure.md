# analysis qualitative failure

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qualitative-failure_20260515T130130_result.json`
- **Structured JSON:** [`e7b341a7a7e6c8e29e38.json`](../../sessions/e7/e7b341a7a7e6c8e29e38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `eval_results/failure_analysis.json`。

## 关键发现

### 失败模式分布

| Mode | Vanilla | TaxEI | Random |
|------|---------|-------|--------|
| max_steps_exhaustion | 50 (51.0%) | 61 (49.6%) | 53 (76.8%) |
| **loop_repetition** | **22 (22.4%)** | **49 (39.8%)** | **6 (8.7%)** |
| exploration_wandering | 13 (13.3%) | 7 (5.7%) | 6 (8.7%) |
| object_not_found | 13 (13.3%) | 6 (4.9%) | 4 (5.8%) |

### TaxEI 独特模式

**TaxEI 的 loop_repetition 显著高于其他两个条件**（49 vs 22 vs 6）。这意味着 TaxEI 训练出的 agent 在遇到错误注入后，更容易陷入重复动作循环（如反复 take/put 同一物品），而非探索新策略。

loop_repetition 在 TaxEI 中分布于所有 4 种注入算子：P1_step_order_swap (15), P2_sub_goal_deletion (14), C1_context_truncation (11), C4_observation_masking (9)。

### 注意事项

- `missing_subgoal` 未被触发 — agent 在 clean/heat/cool 任务中的失败更多表现为探索失败或循环，而非跳过子目标后直接放置。
- Random 只有 1 个 recovery eval 文件（seed 42），vanilla/taxei 各有 3 个，total 不完全对齐。
- clean eval 文件无 trajectory，其中的失败只能按 steps 数粗分类（大部分归入 max_steps_exhaustion）。

---
