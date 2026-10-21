# investigate bjb1 32546 r4 goal files

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_bjb1-32546-r4-goal-files_20260523T102706_result.json`
- **Structured JSON:** [`ca3f469b65056f078a77.json`](../../sessions/ca/ca3f469b65056f078a77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是结论：

---

## 文件配置详情

### `eval_goal_vla_only_seed43_r4.json`
| 字段 | 值 |
|------|-----|
| mode | `vla_only` |
| baseline_mode | `single` |
| benchmark | `goal` |
| n_rollouts | **20** |
| overall_success_rate | **0.98 (98%)** |
| 创建时间 | May 23 00:15 |

### `eval_goal_vla_only_seed44_r4.json`
| 字段 | 值 |
|------|-----|
| mode | `vla_only` |
| baseline_mode | `single` |
| benchmark | `goal` |
| n_rollouts | **20** |
| overall_success_rate | **0.975 (97.5%)** |
| 创建时间 | May 23 00:16 |

两个文件均**没有** `model`、`seed`、`K` 字段。`_r4` 后缀不是 evaluate.py 自动生成的（代码中无此逻辑），是通过 `--output_file` 手动指定的路径。

---

## 结论：这是 Pi0.5 的结果，被错误命名

证据链：

1. **SR 对比**：同服务器上 SmolVLA goal vla_only 的结果（`eval_goal_vla_only_seed43.json`，n_rollouts=10）SR = **69%**；而 Pi0.5 goal vla_only（`eval_goal_vla_only_pi05_seed42.json`，n_rollouts=20）SR = **98%**。r4 文件的 97.5-98% SR 与 Pi0.5 完全吻合，与 SmolVLA 差距巨大。

2. **文件命名逻辑**：evaluate.py 第 826 行 `model_tag = f"_{args.model}" if args.model != "smolvla" else ""`。Pi0.5 应产生 `_pi05` 后缀（如 `eval_goal_vla_only_pi05_seed42.json`），但 r4 文件缺少此标记。原因：使用了 `--output_file` 手动指定路径（第 794-798 行），绕过了自动命名。

3. **per_task 对比**：r4 文件中 8/10 任务 SR=100%，与 Pi0.5 seed42 的模式一致（也是多数 100%）。SmolVLA 的 per_task 最高才 90-100%，多数在 40-90%。

4. **r4 文件唯一性**：整个 logs 目录只有这两个 r4 文件，无其他 r4 数据。

**判定：这两个文件是 Pi0.5 模型 + n_rollouts=20 + goal benchmark + vla_only mode 的结果，不是 SmolVLA baseline。不应用于 SmolVLA baseline 统计。**

---
