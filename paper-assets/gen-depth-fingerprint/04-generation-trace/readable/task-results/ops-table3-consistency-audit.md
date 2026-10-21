# ops table3 consistency audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_table3-consistency-audit_20260516T173901_result.json`
- **Structured JSON:** [`721acfc45bf01b519d44.json`](../../sessions/72/721acfc45bf01b519d44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data needed. Here are the answers to the four core questions:

---

## 回答

### Q1: Table 3 的 7 行数字是否来自同一脚本的同一次运行？

**否。Table 3 混合了至少两个不同脚本的产出。**

证据：
- **7-feature 行** (3class=0.762, binary=0.694)：完全匹配 `results/8gen_logo_unfiltered.json`，由 `fix_tail_decay_and_eval.py` 产出
  - XGB: n_estimators=200, max_depth=6, random_state=**42**
  - 数据：**unfiltered** (`generations_shard0.jsonl` for llama/mistral)
  - **无 downsampling**
  - 不含 baselines，只评估 7-feature

- **Baseline 行** (avg_logprob, fastdetectgpt, binoculars, ld_score, 4det_ensemble, 4det_surface)：接近 `eval_8gen_logo_baselines.py` 的产出 (`8gen_logo_baselines.json`)，但不完全匹配（差 0.001–0.01），可能来自该脚本的较早运行版本
  - XGB baseline: n_estimators=100, max_depth=3, random_state=**789**
  - 数据：**filtered** (`generations_filtered.jsonl` for llama/mistral)
  - **有 downsample**（训练集类别平衡）

关键差异总结：

| 设置 | 7-feature 行 | Baseline 行 |
|------|-------------|------------|
| 脚本 | `fix_tail_decay_and_eval.py` | `eval_8gen_logo_baselines.py`（或类似） |
| random_state | 42 | 789 |
| 数据 | unfiltered | filtered |
| Downsampling | 否 | 是 |
| XGB 超参 | 200/6 | 100/3 (baselines), 200/6 (7-feature) |

---

### Q2: 0.694 是 pooled 还是 per-gen average？

**Pooled。**

证据：`fix_tail_decay_and_eval.py` 的 `logo_predictions` 函数（line 200-206）收集所有 fold 的预测到 `preds` 数组，然后 `run_logo_eval`（line 222-223）用全部预测计算一�� F1：

```python
preds = logo_predictions(X, y, groups)
f1_obs = round(f1_score(y, preds, average="macro"), 4)
```

`8gen_logo_unfiltered.json` 确认：`n_samples=29,095`（全部 binary 样本的数量），`f1_observed=0.6944`。

验证：per-gen F1 平均值 = (0.6968+0.6327+0.6954+0.7175+0.7243+0.6911+0.7093+0.6918)/8 = 0.6949 ≠ 0.6944，进一步证实是 pooled 而非 per-gen average。

---

### Q3: 4det_surface 在同一评估框架下的 binary F1 是多少？是否 > 0.694？

**在统一评估框架下，4det_surface pooled binary F1 = 0.7044，> 7feature_ours = 0.6935。**

来源：`eval_8gen_baselines_pooled.py` → `results/8gen_baselines.json`（May 16 22:53）

这是唯一一个在**同一脚本、同一数据、同一 LOGO fold** 中评估所有 7 种方法的脚本。结果：

| Method | Pooled Binary F1 | CI |
|--------|---------|------|
| **4det_surface** | **0.7044** | [0.6979, 0.7106] |
| 4det_ensemble | 0.6993 | [0.6928, 0.7054] |
| 7feature_ours | 0.6935 | [0.6867, 0.7000] |
| avg_logprob | 0.6785 | [0.6717, 0.6854] |
| ld_score | 0.6788 | [0.6717, 0.6851] |
| fastdetectgpt | 0.5805 | [0.5741, 0.5875] |
| binoculars | 0.5327 | [0.5268, 0.5392] |

注意：4det_surface CI [0.6979, 0.7106] 与 7feature_ours CI [0.6867, 0.7000] **不重叠**。这意味着在公平对比下，**4det_surface 显著优于 7-feature**，论文 claim "highest binary F1" 不成立。

超参差异：4det_surface 用 XGB_BASE (100/3)，7feature_ours 用 XGB_OURS (200/6)。即使给 7-feature 更强的模型容量优势，4det_surface 仍然赢。

---

### Q4: Llama/Mistral 是否有 baseline detection scores？如果没有，Table 3 baselines 的实际 generator 覆盖范围是多少？

**有。`data/detector_scores_8gen.csv` 包含全部 8 个 generator 的 detection scores（Llama 2937 行, Mistral 3665 行）。**

该文件由 `eval_8gen_baselines.py` 生成（如果不存在则现场计算 FDG/logprob/binoculars for llama/mistral，再合并 6-gen scores）。列：`model_name, seed_id, depth, label, avg_logprob, fastdetectgpt, binoculars`。

因此 Table 3 所有行覆盖的是 **相同的 8 个 generator**，不存在 6-gen vs 8-gen 覆盖差异问题。

但注意：`features_pythia410m.jsonl` for llama/mistral 只有 7-feature（entropy + surface），**不含** detection scores。Detection scores 单独存储在 `detector_scores_8gen.csv` 中，需要通过 merge 获取——这也是为什么需要 `eval_8gen_baselines_pooled.py` 这样的脚本来做合并。

---

## 总结

**Table 3 存在严重一致性问题：7-feature 行和 baseline 行来自不同脚本、不同设置、不同数据预处理。在唯一一个统一评估脚本（`eval_8gen_baselines_pooled.py`）的输出中，4det_surface (0.7044) 显著优于 7feature_ours (0.6935)，CI 不重叠。论文 "highest binary F1" 的 claim 是混合来源数字的假象。**

---
