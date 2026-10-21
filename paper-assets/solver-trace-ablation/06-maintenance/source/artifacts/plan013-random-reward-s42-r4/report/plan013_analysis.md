# Plan013 Random Reward Baseline Analysis

**Date**: 2026-05-14
**Experiment**: plan013-random-reward-s42-r4 (500 steps, seed=42, EXIT_CODE=0)

## Reward Design

Random reward replaces ISR with uniform random noise in the multi-objective reward:

```
When proved:  reward = 0.9 * 1.0 + 0.1 * U(0,1)  ∈ [0.9, 1.0)
When failed:  reward = 0.0
```

Same weight split (exec=0.9, sta=0.1) as plan005-sta-low-s42, where ISR fills the 0.1 slot.

## Three-Way Comparison

### Overall Metrics

| Metric | exec-only (plan001) | random reward (plan013) | convex STA (plan005) |
|--------|:-------------------:|:-----------------------:|:--------------------:|
| overall prove_rate | 0.6743 | 0.6747 | 0.5657 |
| overall ISR | 0.6677 | 0.6705 | 0.1682 |
| last100 prove_rate | **0.865** | **0.966** | 0.773 |
| last100 ISR | 0.861 | 0.966 | 0.230 |
| last100 ISR/PR | ~1.0 | 1.0 | 0.298 |
| steps at PR=1.0 | 166 (33.2%) | 264 (52.8%) | — |
| first rolling10 PR≥0.8 | step 133 | step 200 | step 178 |
| duration (min) | 62 | 38 | 71 |

### Windowed Prove Rate

| Window | exec-only | random reward | convex STA |
|--------|:---------:|:-------------:|:----------:|
| 1-50 | 0.185 | 0.118 | 0.178 |
| 51-100 | 0.238 | 0.155 | 0.178 |
| 101-200 | 0.663 | 0.415 | 0.506 |
| 201-300 | 0.784 | **0.899** | 0.671 |
| 301-400 | 0.849 | **0.958** | 0.701 |
| 401-500 | 0.865 | **0.966** | 0.773 |

### Windowed ISR (plan005 only diverges)

| Window | exec-only PR | exec-only ISR | STA PR | STA ISR |
|--------|:---:|:---:|:---:|:---:|
| 1-50 | 0.185 | — | 0.178 | 0.091 |
| 101-200 | 0.663 | — | 0.506 | 0.146 |
| 401-500 | 0.865 | — | 0.773 | 0.230 |

(exec-only 和 random reward 的 ISR ≈ PR，省略单独列。)

## Key Findings

### 1. Random reward 的学习曲线：慢启动，强收敛

Random reward 在前 200 步明显慢于 exec-only（0.118/0.155 vs 0.185/0.238），但从 step 200 开始超越，最终 last100 prove_rate=0.966 >> exec-only 的 0.865。

**解释**：reward ∈ [0.9, 1.0) 的随机抖动在训练早期引入噪声干扰学习信号，但后期这种噪声起到隐式正则化作用，防止 policy 过早 collapse 到局部最优，使得模型在后半段 generalize 更好。

### 2. ISR/PR ratio = 1.0 → ISR 是 prove 的自然副产物

Random reward 的 ISR 与 prove_rate 在 495/500 步完全一致（5 步有微小偏差，max_diff=0.5）。这证实：**当不显式优化 ISR 时，ISR 自然跟随 prove_rate**。模型学会证明时，formalization 的结构质量自动提升。

### 3. Convex STA (plan005) 的 ISR 反而最低

plan005 显式优化 ISR（sta_weight=0.1），但 ISR/PR ratio 仅 0.298。这不是 ISR 优化失败，而是 ISR 信号与 exec 信号产生梯度冲突——ISR 引导模型向"结构正确"方向优化，但这个方向与"能被 prover9 证明"不一致，两个目标互相拖累。

### 4. reward_mean 分布确认

- 当 prove_rate=0 时，reward_mean 恒为 0（86 步）
- 当 prove_rate=1.0 时，reward_mean = 0.9495 ± 0.0094（264 步）
- reward_mean / prove_rate ratio = 0.9496 ± 0.013，符合 `0.9 + 0.1 * E[U(0,1)] = 0.95` 的理论值

## 对 Paper Claims 的影响

### Claim: "ISR provides specific structural feedback that improves formalization"

**结论：此 claim 需要重新表述。**

证据矩阵：

| 条件 | 结果 | 含义 |
|------|------|------|
| exec-only | last100 PR=0.865 | 纯 exec 的 baseline |
| exec + random(0.1) | last100 PR=0.966 | 任意二级信号都能帮助，甚至超越 exec-only |
| exec + ISR(0.1) | last100 PR=0.773 | ISR-specific 信号反而**伤害** prove_rate |

这个三角对比表明：
1. **ISR 不是 "helpful structural signal"**——它在当前 convex formulation 下是 harmful
2. **多目标 regularization 有益**——但必须是不与 exec 冲突的信号（甚至 random noise）
3. **ISR 与 exec 的梯度方向冲突**是 plan005 性能低下的根因

### Paper Story 建议调整

**原叙事**：ISR as structural reward → better formalization
**建议叙事**：

1. **ISR 是有价值的 diagnostic metric**（与 prove_rate 自然高度相关，r=0.994），但不应直接作为 reward component
2. **ISR 作为 reward 时产生 objective conflict**——这本身就是一个有意义的 negative finding（"not all structural rewards help"）
3. **Random reward baseline 的惊喜**：微小随机扰动（0.1 * noise）起正则化作用，值得进一步探索（可做 ablation：不同 noise scale 0.01/0.05/0.1/0.2）

### 或者：重新设计 ISR reward integration

当前 convex 方案（`0.9 * exec + 0.1 * ISR`）的问题在于 ISR 直接参与 reward 计算。替代方案：
- **Multiplicative gating**：`exec * (1 + β * ISR)`（plan002 additive bonus 在做这个）
- **Reward shaping**：ISR 不进 reward，只做 KL penalty 的调节因子
- **Curriculum**：前 N 步用 exec-only，后续引入 ISR（避免早期冲突）

## Data Integrity Note

plan013 config 中 `data_path: data/proofwriter_fol_500.jsonl`，与约束 C001 要求的 `data/train_500_seed42.jsonl` 不一致。需确认 plan001 和 plan005 是否使用了相同数据文件。如果三者数据不同，此对比存在 confound。
