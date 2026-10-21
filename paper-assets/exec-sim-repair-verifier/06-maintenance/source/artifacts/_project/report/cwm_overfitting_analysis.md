# CWM Repo-level Overfitting Analysis

## Available Data Points

### DeepSeek CWM Repo-level (Reliable Data Only)

| Seed | Epoch/Checkpoint | Accuracy | Unparseable | eval_loss | exp_id | Notes |
|------|------------------|----------|-------------|-----------|--------|-------|
| 42 | 3-epoch final (ckpt-13266) | 61.49% | 62.5% | NaN (known bug) | deepseek-cwm-repo-s42-seq4096-eval | @seq4096, DONE |
| 42 | epoch 2 (partial) | 66.85% | 65.5% | N/A | deepseek-cwm-repo-s42-epoch2-eval | **Only 31.2% coverage (3050/9784)** |
| 123-v2 | 1-epoch (ckpt-4209) | 75.45% | 66.4% | N/A | deepseek-cwm-repo-s123-eval-1epoch | Cross-seed |
| 456-v2 | epoch 2 (training) | N/A | N/A | **4.727** | deepseek-cwm-repo-s456-train-v2 | RUNNING |

**Discarded data (data bug):** `deepseek-cwm-repo-s123-train` 训练加载了错误数据（可能是 func-level），其衍生 eval（s123-eval 86.05%/0% unparseable, s123 ckpt-8844 61.9%）均不可靠。`deepseek-cwm-repo-s123-train-v2` 修正了此 bug。

### DeepSeek CLS Repo-level (Overfitting Comparison)

| Metric | Epoch 1 | Epoch 2 | Epoch 3 |
|--------|---------|---------|---------|
| eval_loss | 0.0886 | 0.1587 | 0.1975 |
| accuracy (best ckpt vs final) | 82.61% (ckpt-2105) | — | 82.51% (ckpt-6315) |

CLS eval_loss 也明显上升（+123%），但 **accuracy 几乎不变**（-0.1pp）。

### Qwen CWM Function-level (No Overfitting Baseline)

| Metric | Epoch 1 | Epoch 2 | Epoch 3 |
|--------|---------|---------|---------|
| eval_loss (8B s42) | 0.0554 | 0.0512 (best) | 0.0564 |
| eval_loss (4B s456) | — | — | best=0.0551, final=0.0635 |

Function-level CWM eval_loss 稳定，无过拟合。

### Qwen CWM Repo-level

| Model | Seed | Checkpoint | Accuracy | Unparseable | exp_id |
|-------|------|------------|----------|-------------|--------|
| 4B | 42 | ckpt-500 (v12) | 58.04% | 53.7% | repo-level-cwm-v12 |
| 4B | 123 | ckpt-500 (conda) | 59.09% | 67.2% | repo-level-cwm-seed123-conda |
| 8B | 42 | ckpt-400 @seq4096 | 64.36% | 63.74% | qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval |

Qwen repo-level CWM 只有单一 checkpoint eval，无法构建 epoch 曲线。

## Evidence Assessment

### 过拟合证据强度：中等偏弱（需更多 same-seed 数据确认）

**支持过拟合的证据：**

1. **s42 within-seed 下降（弱）**：epoch 2 partial (66.85%) → epoch 3 final (61.49%) = **-5.36pp**
   - 限制：epoch 2 只有 31.2% coverage，可能不具代表性
   - 如果 partial 样本偏向 easy instances，真实 gap 可能更小

2. **s123-v2 epoch 1 vs s42 epoch 3（间接）**：75.45% vs 61.49% = **+14pp**
   - 限制：跨 seed 对比，seed variance 可能是主因之一
   - 但 14pp 差异远超 function-level seed variance（4B 5-seed range: 86.67-87.57%, <1pp）

3. **s456-v2 eval_loss 异常高（警示）**：epoch 2 eval_loss = 4.727
   - 对比 function-level eval_loss 量级（0.04-0.07），高出两个数量级
   - 但 repo-level 输出更长，eval_loss 量级本身会更高，缺乏正常 baseline 参照

4. **CLS 对照**：CLS repo 也过拟合（eval_loss +123%），但 accuracy 仅下降 0.1pp
   - 这暗示：对于 classification，eval_loss overfitting 不伤 accuracy
   - 而 CWM generation 可能对 overfitting 更敏感（长序列生成累积误差）

**反对过拟合结论的因素：**

1. s42 epoch 2 数据只有 31.2% coverage，统计不充分
2. 14pp gap 中 seed variance 的贡献未知
3. DeepSeek s42 训练 eval_loss=NaN，无法直接观察 loss 曲线
4. s456-v2 的 eval_loss=4.727 缺乏 epoch 1 参照（无法判断是上升还是本来就高）

## Impact on Paper Story

### 方向 A：加强 "CWM at repo-level fundamentally fails"（推荐）

如果 s123-v3 训练完成后确认 epoch 3 << epoch 1：

- **核心论点强化**：CWM 不仅 accuracy 低于 majority baseline，而且训练不稳定——更多 epoch 反而更差
- **机制解释**：CWM 需要生成完整执行轨迹，repo-level 轨迹过长 → 训练后期模型 overfit 噪声而非学到有用信号 → unparseable rate 不随训练改善（始终 ~63-66%）
- **与 CLS 对比**：CLS 在相同数据上也有 eval_loss 上升，但 accuracy 几乎不变（-0.1pp），证明 classification formulation 对 overfitting 天然鲁棒
- **Paper 写法**：在 §5 或 §6 加一句 "Moreover, CWM accuracy degrades with continued training (75.5% at epoch 1 → 61.5% at epoch 3 for DeepSeek s42), while CLS accuracy remains stable (82.6% → 82.5%), suggesting that generation-based formulations are more susceptible to overfitting on long repo-level sequences."

### 方向 B："Early stopping 能救 CWM"（需防御）

如果 Reviewer 提出：

- "CWM 只需要 early stopping 就能获得 75.45% accuracy，远超 majority baseline (72.96%)"
- **防御**：
  1. 75.45% 仍显著低于 CLS 的 82.6%（same data, same model family）
  2. 66.4% unparseable rate 说明生成质量仍然很差——多数 predictions 无法 parse
  3. 实际可用 accuracy = parseable_rate × parseable_accuracy，effective accuracy 更低
  4. CLS 不需要 early stopping、不需要 tuning generation length——开箱即用
  5. Frame: "Even with oracle early stopping, CWM remains 7pp below CLS and produces unparseable outputs for 66% of instances"

### 方向 C：跨 seed 差异（诚实披露）

- 14pp gap 中，seed variance 贡献未知
- 论文中应注明 epoch 1 和 epoch 3 数据来自不同 seed
- 等 s123-v3 完成后可以做 same-seed 对比
- 如果 same-seed gap < 14pp 但 > 5pp，仍然有意义

## Recommendations

### 立即可做

1. **论文中加入 s42 epoch 2 partial 数据作为脚注**：虽然 coverage 低，但 66.85% vs 61.49% 的方向性证据是有价值的
2. **在 Limitations 中提及**：CWM repo-level 结果来自 3-epoch final checkpoint，未做 early stopping 优化；epoch 1 checkpoint 表现可能更好但跨 seed 不可直接对比

### 等待 RUNNING 实验完成后

3. **s123-v3 完成后**（epoch 3 eval）：same-seed 3-epoch curve（epoch 1: 75.45% → epoch 2: ? → epoch 3: ?）→ 确认/否定过拟合
4. **s456-v2 完成后**（epoch 3 eval）：第三个 seed 提供额外 data point

### 如果过拟合被确认

5. **主表格不变**（仍报 3-epoch final results，这是公平比较因为 CLS 也用 3-epoch）
6. **加一个 supplementary 分析**：epoch-by-epoch accuracy 曲线，展示 CWM overfitting vs CLS stability
7. **将 CWM overfitting 作为 CWM 方法的额外缺陷写入 Discussion**

### 不建议做

8. ~~用 epoch 1 的 75.45% 替换主表格中的 61.49%~~：这会引入 cherry-picking 嫌疑，且跨 seed
9. ~~大篇幅讨论过拟合~~：当前证据不够强，过度讨论反而给 Reviewer 留攻击面

## Missing Data（按优先级）

| 优先级 | 数据 | 用途 | 状态 |
|--------|------|------|------|
| P0 | s123-v2 epoch 2 & 3 eval | Same-seed overfitting 曲线 | s123-v3 RUNNING |
| P0 | s456-v2 epoch 1/2/3 eval | 第三 seed overfitting 曲线 | s456-v2 RUNNING |
| P1 | s42 epoch 1 eval | 补全 s42 epoch 曲线 | 需要 ckpt-4422 |
| P2 | s42 epoch 2 full eval | 补全 31.2% partial → full | 需要重跑 |
| P2 | Qwen CWM repo multi-epoch eval | 跨模型家族 overfitting 证据 | 未规划 |
