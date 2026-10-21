# D103 Arbitration: DeepSeek VOTA Seed456 Analysis

## 1. Seed456 Core Metrics

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | **99.33%** | [98.8%, 99.7%] |
| Majority baseline | 71.5% (always "pass") | [69.2%, 73.9%] |
| Lift over majority | +27.8pp | [+25.4pp, +30.3pp] |

### Per-class Breakdown

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| pass | 0.9941 [0.988, 0.999] | 0.9965 [0.992, 1.000] | 0.9953 [0.992, 0.998] |
| fail | 0.9911 [0.979, 1.000] | 0.9853 [0.971, 0.997] | 0.9882 [0.980, 0.996] |

### Training Metrics

| Metric | Value |
|--------|-------|
| train_loss (final) | 0.062 |
| eval_loss (epoch 2) | 0.088 |
| eval_loss (epoch 3) | 0.109 |
| train_runtime | 2h 14m |
| epochs | 3 |
| total steps | 444 |
| n_train / n_eval | 4720 / 1190 |

Epoch 3 eval_loss > epoch 2 eval_loss，轻微过拟合但不影响最终 accuracy（99.33%）。

## 2. Three-Seed Comparison

| Seed | Accuracy | eval max_length | truncation_side | Eval Script |
|------|----------|-----------------|-----------------|-------------|
| 42 | 84.45% | 16384 (no truncation) | N/A | max_length=16384 确认 |
| 123 | 99.16% | 2048 | right (keep head) | fixed evaluate.py |
| 456 | 99.33% | 2048 | right (keep head) | fixed evaluate.py |

### Aggregate Stats

- **Mean**: 94.31%
- **Std (sample)**: 8.54%
- **Median**: 99.16%
- **seed123-seed456 gap**: 0.17pp（极其稳定）
- **seed42 vs mean(123,456)**: -14.80pp

## 3. Front-Truncation Bug Analysis

seed456 的 evaluate.py 使用当前版本，默认参数 `max_length=2048, truncation_side="right"`：
- **right truncation = 保留输入头部（包含 verdict 关键信息）**
- 不受原始 front-truncation bug（左截断砍掉头部）的影响
- seed123 和 seed456 使用相同 evaluate.py，结果一致性高（0.17pp）

**seed42 的 84.45% 存在 eval 条件差异**：
- 训练时 max_length=2048，eval 时 max_length=16384（约 8x 差距）
- 模型从未在 >2048 token 的输入上训练过
- 超长输入可能导致：positional embedding 外推失败、注意力稀释
- **84.45% 可能是 train/eval 长度不匹配导致的人为偏低，而非模型真实能力**

## 4. Arbitration Verdict

### 结论：seed42 是 outlier，DeepSeek VOTA 归 Tier 1

依据：
1. seed456 = 99.33% ≥ 95% 阈值 → 满足仲裁条件
2. seed123 (99.16%) 和 seed456 (99.33%) 高度一致（gap=0.17pp），互相验证
3. seed42 的 84.45% 使用了不同的 eval 条件（max_length=16384 vs 2048），不可直接对比

### 置信度：High（但有 caveat）

seed42 尚未用 fixed evaluate.py (max_length=2048, truncation_side=right) 重新评估。建议补跑以完全排除 seed42 模型本身质量差的可能性。

## 5. 论文影响建议

### 数据更新
- **DeepSeek VOTA 论文数据应报告 seed123/seed456 均值**：99.25% ± 0.09pp
- 或报告三 seed 均值 94.31% 并注明 seed42 eval 条件差异
- **推荐方案**：用 fixed evaluate.py 重评 seed42，然后报告三 seed 均值

### 具体操作
1. **立即可用**：用 99.25%（seed123/456 均值）作为 DeepSeek VOTA accuracy，附注脚说明 seed42 eval 条件差异
2. **DDL 前补跑**（推荐）：对 seed42 checkpoint 用 `evaluate.py --max_length 2048`（默认 right truncation）重新评估，获得公平对比值
3. 如果 seed42 重评后 ≥ 95%，则三 seed 全部一致，直接报告三 seed 均值
4. 如果 seed42 重评后仍 ~84%，则该 seed 训练本身有问题（非 eval 造成），报告 seed123/456 均值并在 appendix 讨论 seed42

### 时间考量
- EMNLP ARR DDL: 2026-05-25（5 天）
- seed42 重评仅需 ~3 分钟推理时间，建议尽快补跑
