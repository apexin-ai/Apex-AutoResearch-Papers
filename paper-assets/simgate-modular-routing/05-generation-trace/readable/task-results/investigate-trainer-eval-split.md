# investigate trainer eval split

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_trainer-eval-split_20260515T225009_result.json`
- **Structured JSON:** [`0b67e849acf06fc1cb21.json`](../../sessions/0b/0b67e849acf06fc1cb21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在可以做完整对比了。两个 split 函数的算法完全不同。

---

## === Trainer eval split 验证 ===

### 1. Trainer eval_dataset 来源
`load_implicit_sft_data`（L201-204）。`train` 函数调用：
```python
train_records, val_records = load_implicit_sft_data(path, eval_split=args.eval_split, seed=args.seed)
```
然后 `val_dataset = ImplicitSFTDataset(val_records, ...)` 传给 `Trainer(eval_dataset=val_dataset)`。

**Trainer eval 确实使用训练脚本内部的 split，与训练数据不重叠。** 但 Trainer eval **只报告 `eval_loss`**，没有 `compute_metrics`，不产生 `balanced_acc`。

### 2. summary.json 中的 balanced_acc 并非来自 Trainer eval
`seed_robustness.py` 的 `eval_router_metrics` 函数导入了 `eval_routing_metrics.load_val_split`，用 **generation-based eval** 计算 balanced_acc。

### 3. 两个 split 算法不同

| | 训练 `load_implicit_sft_data` | Eval `load_val_split` |
|---|---|---|
| 分组粒度 | `task_type` | `(task_type, variation)` |
| 算法 | 手动 shuffle + 前15%切片 | `sklearn.train_test_split` |
| Stratify | 按 task_type 隐式均分 | 按 episode 多数 route_label |
| RNG | `random.Random(seed)` | `sklearn random_state` + `random.Random` |

**相同 seed 下，两个函数产生的 val set 不同。** eval 的 "val" 集可能包含训练时的 train 样本 → data leakage。

### 4. Split seed
都来自 `--seed` 参数（seed-robustness 中 42/43/44/45），但由于算法不同，相同 seed 不保证相同划分。

### 5. 结论

```
=== Trainer eval split 验证 ===

1. Trainer eval_dataset 来源：load_implicit_sft_data ✓（与训练同源）
2. Split 算法：per-task_type stratified（手动 shuffle + 切片）
3. Split seed：来自 --seed 参数
4. Trainer eval 只报告 eval_loss，不报告 balanced_acc
5. summary.json 的 balanced_acc 来自 eval_routing_metrics.load_val_split
   — 这是 generation-based eval，使用不同的 split 算法
   — 分组粒度不同（task_type vs task_type+variation）
   — 算法不同（手动切片 vs sklearn.train_test_split）
   — 存在 data leakage 风险：eval "val" 集可能包含训练集样本
6. 4-seed 55.4±5.2% 数据【需要修正】— 不是来自 Trainer eval，
   而是来自与训练 split 不一致的 generation-based eval
```

**影响范围**: `seed_robustness.py` 中每个 seed 的 balanced_acc 和 internal_recall 都受影响。eval_loss 不受影响（来自 Trainer eval，使用正确的 split）。修正方案：让 `eval_router_metrics.load_val_split` 直接复用 `load_implicit_sft_data` 的 split 逻辑，或在 `seed_robustness.py` 中直接调用 `load_implicit_sft_data` 获取 val_records。

---
