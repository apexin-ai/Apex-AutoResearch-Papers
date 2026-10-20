# 标签编码核查报告

**日期**: 2026-05-14
**目的**: 核实 OpenHands 与 SWE-agent 的标签编码是否一致，排除编码反转导致 cross-agent 零样本迁移 macro-F1=0.528 的可能性。

## 1. SWE-agent 标签编码定义

**代码位置**: `labeling_functions.py:18-20`

```python
PROGRESS = 1
STAGNATION = 0
ABSTAIN = -1
```

标签流转路径：
1. `window_extractor.py` 调用 `labeling_functions.ALL_LFS`（3 个 LF）对每个窗口打标
2. 多数投票 → `majority_label`（0 或 1）
3. `generate_embeddings.py` 将 `majority_label` 存入 `embeddings.pt["labels"]`
4. `train_probe.py` 直接使用 `data["labels"]` 训练，probe 输出 `sigmoid ≥ 0.5 → 1(progress)`, `< 0.5 → 0(stagnation)`

## 2. OpenHands 标签编码定义

**代码位置**: `prepare_openhands_data.py` → 调用 `window_extractor.process_trajectory()` → 同一套 `labeling_functions.py`

OpenHands 数据处理复用 SWE-agent 的完整标签管线：
- `openhands_adapter.py` 将 OpenHands 轨迹转为项目统一的 `Trajectory/Step` 格式
- `prepare_openhands_data.py:62` 调用 `process_trajectory(traj)` → 与 SWE-agent 相同的窗口提取 + LF 标注
- `generate_embeddings.py` 同样将 `majority_label` 存入 `embeddings.pt`

**编码完全一致：`PROGRESS=1, STAGNATION=0`。无任何反转或重映射。**

## 3. cross_agent_eval.py 的标签处理

`cross_agent_eval.py:142-146` 直接加载 OpenHands `embeddings.pt`，使用 `data["labels"]` 作为 ground truth，无任何标签变换：

```python
data = torch.load(emb_path, weights_only=False, map_location="cpu")
labels = data["labels"]
ds = WindowDataset(embeddings, labels)
```

评估时 probe 预测也用同一编码：`(sigmoid(logits) >= 0.5).long()` → 1=progress, 0=stagnation。

## 4. 标签分布对比

| 数据集 | Progress (1) | Stagnation (0) | Stagnation 占比 |
|--------|-------------|----------------|-----------------|
| SWE-agent (全量) | 39,209 | 15,600 | 28.5% |
| SWE-agent (高置信过滤后) | 9,555 | 5,846 | 38.0% |
| SWE-agent (训练集) | 6,740 | 3,894 | 36.6% |
| OpenHands (嵌入后) | 133,667 | 9,390 | 6.6% |

OpenHands stagnation 比例（6.6%）远低于 SWE-agent（36.6%）。若编码反转，OpenHands 的 stagnation 应为 ~93.4%，明显不合理。

## 5. 抽样人工验证（5 个窗口）

### 窗口 1: sunpy__sunpy-5915 win=0, majority_label=1 (PROGRESS)
- **LF**: command_repetition=1(progress), file_diff_delta=-1, outcome_backprop=-1
- **内容**: agent 使用多样化命令探索代码库（think → ls → view README → find tests），每条命令不同
- **判定**: ✅ 确实是进展

### 窗口 2: spacetx__starfish-1525 win=0, majority_label=1 (PROGRESS)
- **LF**: command_repetition=1(progress), file_diff_delta=-1, outcome_backprop=-1
- **内容**: agent 做系统性探索（think → view README → find tests → pytest --help），命令均不同
- **判定**: ✅ 确实是进展

### 窗口 3: tobymao__sqlglot-2295 win=0, majority_label=0 (STAGNATION)
- **LF**: file_diff_delta=0(stagnation), command_repetition=1(progress), outcome_backprop=-1
- **内容**: agent 反复 view README 不同行范围，出 ERROR（无效 view_range），无文件编辑
- **判定**: ✅ 确实是停滞

### 窗口 4: tobymao__sqlglot-4516 win=0, majority_label=0 (STAGNATION)
- **LF**: file_diff_delta=0(stagnation), command_repetition=1(progress), outcome_backprop=-1
- **内容**: cd、pwd、view README（出错），无文件修改
- **判定**: ✅ 确实是停滞

### 窗口 5: reframe-hpc__reframe-2533 win=0, majority_label=0 (STAGNATION)
- **LF**: file_diff_delta=0(stagnation), command_repetition=1(progress), outcome_backprop=0(stagnation)
- **内容**: view README + 运行 pytest，无文件编辑，虽最终 resolved 但此窗口无实质操作
- **判定**: ✅ 确实是停滞

**5/5 样本标签与实际行为一致。**

## 6. 结论

**编码一致，无反转。**

SWE-agent 和 OpenHands 使用完全相同的标签管线（`labeling_functions.py` → `window_extractor.py` → `generate_embeddings.py`），编码定义一致：`PROGRESS=1, STAGNATION=0`。5 个抽样窗口的人工验证全部通过。

Cross-agent 零样本迁移 macro-F1=0.528 的原因不是标签反转，而是：
1. **类别分布偏移**: OpenHands stagnation 仅 6.6% vs SWE-agent 36.6%，极度不平衡
2. **行为模式差异**: OpenHands agent 的交互格式（tool_calls JSON）和探索策略与 SWE-agent 不同
3. **单类失败**: probe 在 progress 上 F1=0.908 正常，但 stagnation F1=0.151（严重漏检稀有的 stagnation 样本）
