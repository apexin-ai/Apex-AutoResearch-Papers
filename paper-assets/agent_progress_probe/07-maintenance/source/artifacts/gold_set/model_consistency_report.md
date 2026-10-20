# Gold Set Bootstrap 模型一致性排查报告

**日期**: 2026-05-15

## 问题

| 来源 | GB macro-F1 | 脚本 |
|------|-------------|------|
| Bootstrap CI | **0.802** | `gold_bootstrap_ci.py` |
| eval_full | **0.760** | `evaluate_gold_set.py` |

两个脚本对同一 gold set (199 windows, 195 matched) 的 Structural GB 给出不同的 macro-F1。

---

## 1. 两个脚本的模型来源

**两个脚本都没有使用预训练 checkpoint，都是 on-the-fly 重新训练。**

`checkpoints/` 目录只有 GRU probe 的 `best_model.pt` 和 `split_info.json`，没有任何 structural GB/RF checkpoint。

### gold_bootstrap_ci.py (`get_structural_predictions`)

```python
# line 364
GradientBoostingClassifier,
{"n_estimators": 200, "learning_rate": 0.1, "max_depth": 5, "random_state": 42},
```

- 训练数据: `split_info.json` 的 `keep_indices` → `train_indices`，**不排除 gold windows**
- 特征来源: 仅 SWE-agent trajectories (`data/swe_agent_trajectories_5000.jsonl`)
- OH windows 的特征: 从 SWE-agent traj_index 用错误的 row_idx 查找，产生垃圾特征

### evaluate_gold_set.py (`evaluate_structural`)

```python
# line 660-661
GradientBoostingClassifier,
{"n_estimators": 200, "learning_rate": 0.1, "max_depth": 5, "random_state": 42},
```

- 训练数据: 同一 `split_info.json`，但 **排除 gold windows** (`train_idx = [i for i in orig_train if i not in gold_keep_set]`)
- 特征来源: SWE-agent + OpenHands trajectories（OH 单独索引）
- OH windows 的特征: 正确从 `oh_traj_index` 提取

---

## 2. 论文原始模型

论文中 cross-agent GB 模型定义在 `src/analysis/bootstrap_ci_crossagent.py`:

```python
# line 100
hp_full = dict(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
```

原始训练脚本 `non_nlp_baseline.py` 从 `[0.01, 0.05, 0.1, 0.2]` 中 CV 选择最优 lr。论文的 cross-agent 实验确定使用 **lr=0.05**。

**没有保存的 checkpoint。**

---

## 3. 差异根因

### 主因: 训练数据泄露 (leakage)

`gold_bootstrap_ci.py` 的 `get_structural_predictions()` 直接用 `split_info["train_indices"]` 训练，不排除 gold windows。

`evaluate_gold_set.py` 的 `evaluate_structural()` 有 leakage-fix:
```python
orig_train = split_info["train_indices"]
train_idx = [i for i in orig_train if i not in gold_keep_set]
```

Gold set 中部分 windows 落在训练集中（GRU Probe 的 `gold_in_train` 有 39 个），模型在训练时见过这些样本的特征和标签（MV 标签），导致预测偏高。

### 次因: OH trajectory 缺失

Gold set 中 63/199 windows 来自 OpenHands。

- `gold_bootstrap_ci.py`: 所有特征均从 SWE-agent trajectory index 提取，OH windows 的 `row_idx` 映射到错误的 SWE trajectory（或空），特征是垃圾值
- `evaluate_gold_set.py`: OH windows 正确使用 `oh_traj_index`

这个因素对分数的影响方向不确定（垃圾特征可能碰巧在部分 OH windows 上给出正确预测），但整体上不如 leakage 的影响大。

### 第三因: 超参数错配

两个脚本都使用 `learning_rate=0.1`，但论文的 cross-agent GB 使用 `learning_rate=0.05`。两个数字 **都不是论文原始模型的正确评估结果。**

---

## 4. 结论

| 问题 | 状态 |
|------|------|
| Bootstrap 0.802 可信吗？ | **不可信** — 有训练数据泄露 + OH 特征错误 |
| eval_full 0.760 可信吗？ | **较可信** — 已修复泄露 + 正确 OH 特征，但 lr=0.1 不是论文模型 |
| 论文原始模型的 gold macro-F1？ | **未知** — 没有 lr=0.05 的 checkpoint，也没有用 lr=0.05 在 gold set 上跑过 |

### 论文原始模型在 gold set 上的正确 macro-F1

**尚无法确定。** 需要以下步骤才能得到正确数字:

1. 在 `evaluate_gold_set.py` 中将 GB 的 `learning_rate` 从 0.1 改为 **0.05**（匹配论文模型）
2. 确保 leakage-fix 生效（已有）
3. 确保 OH trajectories 正确索引（已有）
4. 重新运行 eval_full

**预期**: 0.760 附近（lr 变化对 GB 影响有限，0.05 和 0.1 在 CV 中通常接近），但必须实际运行才能确认。

---

## 5. 修复建议

1. **`gold_bootstrap_ci.py`**: 将 `get_structural_predictions` 替换为 `evaluate_gold_set.py` 的 `evaluate_structural` 逻辑（含 leakage-fix），并添加 OH trajectory 索引
2. **两个脚本**: 将 GB 的 `learning_rate` 改为 0.05 以匹配论文模型
3. **长期**: 保存论文模型的 checkpoint（joblib/pickle），避免每次重新训练导致参数漂移
