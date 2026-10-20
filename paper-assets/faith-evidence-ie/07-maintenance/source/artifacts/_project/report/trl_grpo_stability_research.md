# TRL 1.1.0 GRPO 训练稳定性调研报告

## 1. clip_ratio=0.0 的根因：设计如此，非 bug

**结论：当 `num_iterations=1`（默认值）时，clip_ratio 恒为 0.0，这是预期行为。**

原理：
- GRPOTrainer 默认 `num_iterations=1`，即纯 on-policy 训练
- On-policy 下 `per_token_logps == old_per_token_logps`，importance sampling ratio = exp(logp - old_logp) = 1.0
- ratio=1.0 永远在 [1-ε, 1+ε] 范围内，clipping 永远不触发
- 只有 `num_iterations > 1` 时，模型在同一批数据上多次更新，ratio 才会偏离 1.0，clipping 才生效

参考：[GitHub Discussion #3548](https://github.com/huggingface/trl/discussions/3548)、[Issue #3757](https://github.com/huggingface/trl/issues/3757)

## 2. TRL GRPO 的策略约束参数全景

| 参数 | 默认值 | 作用 | 备注 |
|------|--------|------|------|
| `epsilon` | 0.2 | clipping 下界 (1-ε) | 仅 num_iterations>1 时生效 |
| `epsilon_high` | None (=epsilon) | clipping 上界 (1+ε_high) | DAPO 推荐 0.28 |
| `num_iterations` | 1 | 每批数据的梯度更新次数 (μ) | =1 时无 clipping |
| `beta` / `kl_coef` | 0.0 | KL 散度惩罚系数 | =0 时不加载 ref model |
| `max_grad_norm` | None | 梯度裁剪 | 建议设 0.1-1.0 |
| `mask_truncated_completions` | False | 屏蔽被截断的 completion | DAPO overlong filtering |
| `use_bias_correction_kl` | False | 无偏 KL 估计（importance sampling 修正） | 启用 beta 时建议开启 |
| `off_policy_mask_threshold` | None | 离策略序列掩码阈值 | 过滤 KL 过高的序列 |
| `loss_type` | "grpo" | 损失函数变体 | 可选 "bnpo", "dr_grpo" 等 |

**关键发现：默认配置下（num_iterations=1, beta=0.0），TRL GRPO 没有任何显式的 policy drift 约束机制。** 唯一的约束来自学习率和梯度裁剪。

## 3. Collapse 诊断

结合你的症状分析：

| 症状 | 诊断 |
|------|------|
| step 35 达峰后退化 | 典型 policy drift — 无约束的策略更新越过最优区域 |
| clip_ratio=0.0 | 正常（num_iterations=1），但说明**无 clipping 保护** |
| truncation 40% | 截断 completion 参与 loss 计算，引入大量噪声梯度 |
| f1 从 0.098 降到 0.012 | 模型输出退化为固定模式（mode collapse / entropy collapse） |
| total_reward 从 1.79 降到 1.1 | reward hacking 或 entropy 崩塌 |

**根因排序**：
1. **无 policy drift 约束**（num_iterations=1 + beta=0.0）→ 策略可以一步跳很远
2. **截断噪声**（40% truncation 的 completion 贡献了错误梯度）
3. **可能的学习率过高**（在无约束情况下放大了 drift）

## 4. 修复方案清单（按优先级排序）

### P0：mask_truncated_completions=True
```python
GRPOConfig(mask_truncated_completions=True)
```
- **原理**：40% 截断率意味着大量不完整 completion 参与 loss。截断的 completion 没有 EOS token，reward 信号不完整，会引导模型走向错误方向。DAPO 论文证明 overlong filtering 显著稳定训练。
- **风险**：低。可能减少有效训练样本量，但 40% 截断率下收益远大于代价。
- **预期效果**：消除截断噪声，是最直接的单一改进。

### P0：启用 KL 惩罚 beta=0.001~0.04
```python
GRPOConfig(beta=0.04)  # 保守起步，DeepSeek-R1 用 0.001
```
- **原理**：beta>0 会加载 reference model 并在 loss 中加入 KL(π_θ || π_ref) 惩罚项，直接阻止策略偏离初始模型太远。这是 GRPO 在 num_iterations=1 时唯一的显式 drift 约束。
- **风险**：增加显存（需加载 ref model）。beta 过大会限制学习能力。QLoRA + ZeRO-2 下 ref model 显存开销需评估。
- **建议值**：0.01~0.04 起步，观察 KL divergence 指标。DeepSeek-R1 用 0.001 但他们 num_generations 很大。

### P1：增大 num_iterations=2
```python
GRPOConfig(num_iterations=2, epsilon=0.2)
```
- **原理**：num_iterations>1 时 clipping 机制激活，每次更新受 [1-ε, 1+ε] 约束，防止单步过大更新。相当于在同一批数据上做 2 次更新，第 2 次有 clipping 保护。
- **风险**：轻微增加训练时间。数值过大（>4）可能导致 off-policy 问题。
- **配合**：设为 2 后 clip_ratio 应不再为 0.0，可用此指标监控策略偏移程度。

### P1：DAPO 风格非对称 clipping
```python
GRPOConfig(
    num_iterations=2,
    epsilon=0.2,        # 下界
    epsilon_high=0.28,  # 上界（DAPO 推荐）
)
```
- **原理**：对称 clipping 会压制低概率 token 的探索（它们难以突破上界），导致 entropy collapse。非对称上界 0.28 > 下界 0.2 允许模型更自由地探索新 token，缓解 mode collapse。
- **风险**：低。DAPO 论文已验证有效性。
- **前提**：需 num_iterations>1 才有意义。

### P1：降低学习率 + 余弦调度
```python
GRPOConfig(
    learning_rate=5e-6,      # 从当前值下调（如果当前是 1e-5+）
    lr_scheduler_type="cosine",
    warmup_ratio=0.1,
)
```
- **原理**：在无 clipping / 无 KL 约束时，学习率是唯一的隐式约束。降低学习率减缓策略更新速度，延迟或避免越过最优区域。
- **风险**：训练变慢，可能需要更多 step 收敛。
- **建议**：QLoRA + GRPO 建议 5e-6 ~ 1e-5。

### P2：增加 num_generations
```python
GRPOConfig(num_generations=8)  # 从 4 增加到 8 或 16
```
- **原理**：GRPO 的 advantage 估计基于 group 内 reward 的均值和标准差。group 越小，advantage 估计方差越大，梯度越嘈杂。num_generations=4 时方差显著高于 16。
- **风险**：线性增加生成时间和显存。4x RTX5090 应能支撑 8-16。
- **权衡**：生成开销 vs 训练稳定性。如果生成瓶颈严重，优先用其他方法。

### P2：max_grad_norm 梯度裁剪
```python
GRPOConfig(max_grad_norm=0.1)
```
- **原理**：限制梯度范数防止单步过大更新。作为额外安全网。
- **风险**：设太小会减慢收敛。0.1 是实践中常用的保守值。

### P3：提高采样温度
```python
GRPOConfig(temperature=0.9)  # 默认通常 1.0
```
- **原理**：低温度导致生成多样性不足，advantage 估计退化（group 内 reward 方差趋零），加速 entropy collapse。
- **风险**：温度过高会降低 completion 质量。
- **建议**：0.8~1.0 范围。

## 5. 推荐实验方案

### 第一轮：最小改动验证
```python
grpo_config = GRPOConfig(
    mask_truncated_completions=True,  # P0: 消除截断噪声
    beta=0.04,                         # P0: KL 约束
    max_grad_norm=0.1,                 # P2: 梯度安全网
    # 其他参数保持不变
)
```
这三个改动风险最低、实现最简单，且直接针对两个根因（无约束 + 截断噪声）。

### 第二轮：如果仍不稳定
```python
grpo_config = GRPOConfig(
    mask_truncated_completions=True,
    beta=0.01,                         # 降低 KL 权重（有 clipping 兜底）
    num_iterations=2,                  # 启用 clipping
    epsilon=0.2,
    epsilon_high=0.28,                 # DAPO 非对称
    max_grad_norm=0.1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
    warmup_ratio=0.1,
)
```

### 监控指标
- `clip_ratio`：num_iterations>1 后应非零；持续接近 1.0 说明 clipping 过于激进
- `kl`：启用 beta 后观察，正常范围 0.01~0.5；>1.0 说明策略偏移严重
- `entropy`：0.05~0.5 正常；<0.01 说明 mode collapse
- `grad_norm`：0.001~1.0 正常；>10 不稳定
- `truncation_rate`：mask_truncated 后此指标应稳定或下降

## 6. 参考来源

- [TRL GRPOConfig 源码](https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_config.py)
- [TRL GRPOTrainer 源码](https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_trainer.py)
- [TRL GRPO Trainer 文档](https://huggingface.co/docs/trl/main/en/grpo_trainer)
- [num_iterations 默认值讨论](https://github.com/huggingface/trl/discussions/3548)
- [advantage clipping Issue #3757](https://github.com/huggingface/trl/issues/3757)
- [GRPO++ Tricks for Making RL Work](https://cameronrwolfe.substack.com/p/grpo-tricks)
- [MAD GRPO: 修复 GRPO 不稳定性](https://huggingface.co/blog/telcom/mad-grpo)
- [DAPO 论文](https://arxiv.org/pdf/2503.14476)
- [From GRPO to DAPO and GSPO](https://huggingface.co/blog/NormalUhr/grpo-to-dapo-and-gspo)
- [GRPO Loss Variants (DeepWiki)](https://deepwiki.com/huggingface/trl/5.2-grpo-loss-variants-and-clipping)
- [The Illustrated GRPO](https://abderrahmanskiredj.github.io/the-illustrated-grpo/)
