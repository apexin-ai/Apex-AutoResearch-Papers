# investigate table7 trainer eval

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_table7-trainer-eval_20260515T230556_result.json`
- **Structured JSON:** [`6609b92b456c1f9f409a.json`](../../sessions/66/6609b92b456c1f9f409a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整报告。

---

## Part 1: Table 7 seeds 123/456/789 eval 来源

| Seed | 论文数字 | 来自 Trainer eval? | 来自 generation eval? | 结果文件 |
|------|---------|:-:|:-:|---------|
| 123 | 57.36% | 否 | **是** | `results/ablation_b_seed123_gen.json` |
| 456 | 57.48% | 否 | **是** | `results/ablation_b_seed456_gen.json` |
| 789 | 58.31% | 否 | **是** | `results/ablation_b_seed789_gen.json` |

**关键证据：**
- `implicit_router_sft.py` 中无 `compute_metrics`，Trainer eval 只产出 `eval_loss`（trainer_state.json 确认，最后一步仅有 `eval_loss: 0.3172`）
- Gen eval 文件的 `balanced_accuracy` 精确匹配论文数字（0.5736, 0.5748, 0.5831）

**Split 算法问题：**

Gen eval 使用 **flat step-level split**（`plan013_eval.py` 风格）：
```python
random.seed(42); random.shuffle(records); val = records[int(N*0.85):]  # n_val=306
```
训练使用 **per-task step-level split**（`load_implicit_sft_data`，seed=123/456/789）：n_val=305

这两个 split 算法不同，导致 **eval val 集与训练 train 集大量重叠**：

| Seed | Eval val steps | 被训练 train 集见过 | 泄露率 |
|------|:-:|:-:|:-:|
| 123 | 302 | 254 | **84.1%** |
| 456 | 302 | 256 | **84.8%** |
| 789 | 302 | 260 | **86.1%** |

**结论：这 3 个数字不可信，需要用一致的 split 重跑。** corrected seed-robustness 文件（seeds 42-49）已修正为使用 `training_load_implicit_sft_data` split，n_val=305。

---

## Part 2: Data Split 粒度确认

**Split 粒度：step-level（非 episode-level）**

| 维度 | 实际情况 |
|------|---------|
| 总 records | 2040 |
| Unique episodes (task_type, variation) | **66** |
| Unique task_types | 11 |
| 论文写的 "81 train, 14 val episodes" | **与 66 total 不符** |

**训练 split (`load_implicit_sft_data`)**：按 `task_type` 分组，每组内 step 级别 shuffle + 15% 切分。**无 episode 分组**——同一 episode 的 steps 被拆到 train 和 val 两侧。

验证（seed=123）：
- 66 episodes 中有 **65 个** 同时出现在 train 和 val（只有 1 个 episode 完全在 train 侧，因为某 task_type 仅 2 episodes、n_val=1）

**Gen eval split**：flat random shuffle（无任何分组），更严重的 contamination——全部 66 episodes 被拆分。

**注意**：`data_loader.py:stratified_split()` 有正确的 episode-level split（按 `(task_type, episode_id, variation)` 分组、注释写 "no episode leakage"），但这是给 **explicit router** 用的，implicit router 的训练和 eval 都没用它。

**准确描述（供论文修正）：**
> "We split the 2040 labeled steps from 66 episodes into ~85/15 train/val sets, stratified by task type at the step level, yielding ~1735 training steps and ~305 validation steps. Note: steps from the same episode may appear in both splits."

或者，如果要改为 episode-level split（推荐），需要用 `data_loader.py` 的 `stratified_split()` 逻辑重新训练和评估。66 episodes × 15% ≈ 10 val episodes（~300 steps），56 train episodes（~1740 steps）。

---
