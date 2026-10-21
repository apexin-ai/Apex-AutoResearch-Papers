# code intervention mode

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_intervention_mode_20260518T095757_result.json`
- **Structured JSON:** [`539f5520412813dc8559.json`](../../sessions/53/539f5520412813dc8559.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Diff 总结：

**4 处修改，共增加 ~40 行：**

1. **`parse_args()`** (L75-83): 添加 `--intervention_mode`, `--intervention_metric`, `--intervention_threshold`, `--intervention_alpha` 四个参数

2. **`main()` 初始化** (L229-235): 在 gen 循环前初始化 `intervention_triggered=False`, `trigger_gen=None`，并从已有 metrics 恢复干预状态（支持 `--start_gen` 断点续跑）

3. **Gen 0 metrics** (L249-251): 写入 `intervention_triggered`, `trigger_gen`, `effective_alpha` 字段

4. **Gen 1..N 循环** (L269, L285, L288, L314-331):
   - 每个 gen 开始时根据干预状态选择 `current_alpha`
   - `mix_datasets` 和 print 使用 `current_alpha` 替代 `args.synthetic_ratio`
   - metrics 计算后检查 gen-over-gen 相对下降是否超过 threshold，超过则触发干预
   - 将干预状态写入 metrics.json

**`--intervention_mode none` 不改变任何现有行为**——`current_alpha` 始终等于 `args.synthetic_ratio`，trigger check 被跳过。

语法检查 + 参数解析验证均通过。备份已保存为 `iterative_train.py.bak`。

---
