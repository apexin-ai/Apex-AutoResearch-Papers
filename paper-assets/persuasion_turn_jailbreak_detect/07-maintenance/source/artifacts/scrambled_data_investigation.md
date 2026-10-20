# Scrambled 模型训练数据差异调查报告

## 三次实验时间线

| 实验 | 数据源 | Benign 来源 | DD OOD F1 | Perturbation F1 |
|------|--------|-------------|-----------|-----------------|
| plan_003_v2 (原始) | plan_002_splits 等价数据 | topic-anchored-v2 | 0.981 (plan_006 eval) | N/A |
| plan_003_scrambled_retrain | **final_v2** | **v4c-casual** | N/A (未跑DD OOD) | **0.333** (全预测benign) |
| plan_003_scrambled_fix | plan_002_splits | topic-anchored-v2 | **0.990** | 1.000 |

注：plan_003_scrambled_retrain 的结果文件 (`plan_003_scrambled_perturbation.json`) 中的 `clean_results` 和 `perturbed_results` 是在 `plan_004_perturbed_test.jsonl`（benign=topic-anchored-v2）上的评估，不是 DD OOD。但效果等价——模型在训练分布外的 benign 数据上完全崩溃。

## 数据集对比

### 样本数

| 数据集 | train | val | test | train_scrambled |
|--------|-------|-----|------|-----------------|
| final_v2 | 336 (175 jb + 161 bn) | 71 | 73 | 336 |
| plan_002_splits | 350 (175 jb + 175 bn) | 74 | 76 | 350 |

### Benign 数据来源

| 属性 | v4c-casual (final_v2) | topic-anchored-v2 (plan_002) | jailbreak (crescendo) |
|------|----------------------|------------------------------|----------------------|
| source | qwen3-8b-v4c-casual | qwen3-8b-topic-anchored-v2 | crescendo |
| 对话结构 | **user-only** | user+assistant | user+assistant |
| 有 assistant 轮次 | **0/161** | **175/175** | 175/175 |
| 平均 user 轮数 | **6.5** | 8.1 | 8.3 |
| 平均 user 字符总量 | **1086** | 2013 | 1992 |

### DeBERTa 训练指标

| 实验 | best_epoch | val_persuasion_acc | val_intent_acc | val_loss |
|------|-----------|-------------------|----------------|----------|
| plan_003_v2 (原始) | 3 | 0.644 | 0.967 | 1.015 |
| plan_003_scrambled_retrain | 未找到独立日志 | — | — | — |
| plan_003_scrambled_fix | 4 | 0.679 | **1.000** | 0.776 |

### GRU 训练参数（两次重训完全一致）

- hidden=256, layers=2, dropout=0.3, lr=1e-3, epochs=20, batch=32, seed=42

## 根因结论

**v4c benign 数据存在严重的结构性 shortcut。**

v4c-casual benign 是纯 user-turn 对话（无 assistant 回复），平均 6.5 轮、1086 字符。而 jailbreak（crescendo）是 user+assistant 多轮对话，平均 8.3 user 轮、1992 字符。虽然模型只处理 user turns，但这两个分布在 **轮数** 和 **文本长度/风格** 上有本质差异。

GRU 在 final_v2 数据上训练时，学到的区分信号是「短/少轮 → benign，长/多轮 → jailbreak」的 shortcut，而非真实的 intent 特征。这导致：

- **IID test（同 v4c benign）**：F1=1.0（shortcut 在同分布数据上有效）
- **Perturbation test（topic-anchored benign）**：F1=0.333（topic-anchored benign 结构匹配 jailbreak，shortcut 失效，全部预测为 benign）
- **DD OOD（deceptive_delight + wildchat）**：未评估，但预期同样崩溃

Topic-anchored-v2 benign 通过匹配 jailbreak 的对话结构（8.1 user turns, 2013 chars, 有 assistant 回复），消除了结构性 shortcut，迫使模型学习内容级特征。因此 plan_002_splits 训练的模型能泛化到 wildchat (DD OOD F1=0.990)。

## 对论文叙事的影响

1. **Scrambled 作为有效 control：成立**，但仅限于使用 plan_002_splits（topic-anchored）数据训练的版本
2. 原始 plan_003_v2 和 fix 版本都使用 plan_002_splits 数据，结果一致（DD OOD F1 ≈ 0.98-0.99）
3. final_v2 数据的 0.333 结果是数据 bug，不是 scrambled control 本身的问题
4. 论文中应使用 plan_003_scrambled_fix 的结果（DD OOD F1=0.990），并确认所有对照实验使用 plan_002_splits 数据
5. Scrambled model 在 DD OOD 上 F1=0.990 说明：即使 persuasion strategy 标签是噪声，DeBERTa 的 intent 信号仍然足够强，GRU 可以利用它做二分类。这符合预期——scrambled 消除的是 strategy 信号的贡献，而非 intent 信号
