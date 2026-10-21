# ops check eval level config

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_eval_level_config_20260522T032617_result.json`
- **Structured JSON:** [`d201460eb435bc5c550f.json`](../../sessions/d2/d201460eb435bc5c550f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰，汇总如下：

---

## 1. 当前 eval v10 跑的是 Level II

Log 中明确输出：
- `Setting up SafeLIBERO benchmark: safelibero_object (level II)`
- `Safety level: II`

eval_safelibero.py 第 17 行启动参数为 `--safety_level II`，第 355 行 argparse default 也是 `"II"`。

## 2. Level I vs Level II 在代码中的区分

**同一套 BDDL 文件**（相同 task/obstacle 定义），区别在于 **init_states 文件不同**：

```python
# benchmark/__init__.py, get_task_init_states()
init_states_path = init_states_path.replace(
    ".pruned_init", f"_level_{self.safety_level}.pruned_init"
)
```

例如同一个 task 有两个 init 文件：
- `pick_up_the_orange_juice_..._level_I.pruned_init`
- `pick_up_the_orange_juice_..._level_II.pruned_init`

Level I 和 II 共享相同的 BDDL（相同的 6 个 obstacle 对象：moka_pot, storage_box, milk, wine_bottle, red_mug, yellow_book + box_base），**区别是 obstacle 的初始位置/姿态不同**（Level II 的 obstacle 更靠近操作路径，更难避开）。

另外 `safelibero_goal` suite 在 Level II 时还会替换 task 顺序（第 4 个 task 换成第 5 个）。

## 3. `--suite safelibero_object` 对应哪个 level？

suite 和 level 是独立参数。`safelibero_object` 是 suite（4 个 pick-and-place 任务），level 由 `--safety_level` 控制。当前跑的是 `safelibero_object` + `Level II`。

## 4. 关于 TSR=0% 的判断

**当前确实跑的是 Level II，不是 Level I。** TSR=0% 不是因为跑错了 level。

从 log 看，前 30 个 episode 全部 `success=False, collided=False, steps=300`——机械臂跑满 300 步既没有完成任务也没有碰撞。这说明 **baseline 模型根本没有有效执行任务**（不是被 obstacle 碰撞导致失败，而是压根没抓到东西）。

如果 AEGIS 论文报告 Level II baseline TSR 为 40-78%，需要检查：
- checkpoint 是否正确（当前用的 `baseline_object_pudding_eval/best`）
- 这个 checkpoint 是否在 safelibero_object 上训练/验证过
- norm_stats 是否匹配

---
