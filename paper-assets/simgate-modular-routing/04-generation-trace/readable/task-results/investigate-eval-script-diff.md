# investigate eval script diff

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_eval-script-diff_20260515T225403_result.json`
- **Structured JSON:** [`5d956d6392b07d65653f.json`](../../sessions/5d/5d956d6392b07d65653f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有现有报告都是 n_val=300（原始 split）。分析完成，下面是汇报。

---

```
=== 两个 eval 脚本 Diff 汇报 ===

### 脚本对比
| 维度 | routing_eval_sft.py (原始) | corrected_eval.py (修正) |
|------|--------------------------|--------------------------|
| 路径 | src/evaluation/routing_eval_sft.py | corrected_eval.py (项目根) |
| Split 函数 | load_val_split() | load_implicit_sft_data()（训练函数完整复制） |
| 分组键 | (task_type, variation) = episode | task_type（不含 variation） |
| Split 算法 | sklearn train_test_split on episode keys, stratify=majority_label | 手动 per-task_type: rng.shuffle → int(len*0.15) |
| Split seed | random_state=42 (sklearn) | random.Random(42) (stdlib) |
| n_val | 300 | 305 |
| 是否调用训练的 split 函数 | 否，自己实现 | 是，EXACT copy of training's load_implicit_sft_data |

### eval_routing_metrics.py 归属
src/eval_routing_metrics.py 用的是和 routing_eval_sft.py **相同**的 episode-level sklearn split（load_val_split），
属于原始 eval 阵营，n_val=300。

### n_val 差异根因

两个差异叠加导致 300 vs 305：

1. **分组粒度不同**：原始按 (task_type, variation) 分 episode 后整 episode 划入 val；
   训练按 task_type 分组后逐条划入 val。不同粒度下 15% 切分的 rounding 行为不同。

2. **Split 算法不同**：
   - sklearn `train_test_split(test_size=0.15)` 作用于 episode 数量，
     val episodes 展开后的 step 总数取决于各 episode 长度，无法精确控制 step 数
   - 训练函数对每个 task_type 内部做 `int(len(items) * 0.15)`，
     逐 task 累加，更精确地控制 step 级别的比例

3. **RNG 不同**：sklearn 用 numpy RandomState(42)，训练用 stdlib random.Random(42)，
   即使粒度相同，选出的样本也不同。

### 权威标准判定

**corrected_eval.py 是权威标准。**

训练脚本 `implicit_router_sft.py:138` 的 `load_implicit_sft_data` 定义了训练/验证 split。
corrected_eval.py 完整复制了这个函数（docstring 明确写 "EXACT copy of training's split function"），
因此它产出的 val set = 训练 held-out set，是唯一能保证 eval 不泄露训练数据的方式。

routing_eval_sft.py / eval_routing_metrics.py 的 val set 与训练 held-out set **不一致**：
- 有训练样本被错误纳入 eval（乐观偏差）
- 有 held-out 样本未被 eval 覆盖

### 已有报告受影响情况

所有 checkpoints/plan-004-v5/ 下的现有报告均使用原始 split（n_val=300）：
- routing_eval_report.json → n_val=300
- routing_eval_thinking_off.json → n_val=300
- routing_eval_thinking_on.json → n_val=300

corrected_eval.py 尚无产出的 JSON 报告文件（未找到对应结果文件）。

### 影响范围
论文中所有引用自 routing_eval_sft.py 或 eval_routing_metrics.py 的数字需要用
corrected_eval.py 重跑：
- plan-004-v5 的 routing accuracy / balanced accuracy / confusion matrix
- 任何 thinking_on vs thinking_off 对比数字
- 其他 checkpoint 的 eval_report.json（如用了同一 split 逻辑）
```

---
