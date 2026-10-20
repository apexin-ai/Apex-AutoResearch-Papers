# TRL GRPOTrainer KL 计算路径分析

**实验**: mvp2_grpo_ced_r2 | **TRL**: 1.1.0 | **配置**: QLoRA + num_iterations=2 + beta(kl_coef)=0.05

---

## 1. KL 在 loss 中的角色：LOSS-COMPONENT（非 metric-only）

```python
# grpo_trainer.py:2601-2605
per_token_kl = (
    torch.exp(ref_per_token_logps - per_token_logps)
    - (ref_per_token_logps - per_token_logps)
    - 1
)

# grpo_trainer.py:2653  ← 关键行
per_token_loss = per_token_loss + self.beta * per_token_kl
```

KL 使用 **Schulman non-negative estimator**（`exp(r) - r - 1`，其中 `r = log(π_ref/π_θ)`），直接以 `beta * per_token_kl` 加入 per_token_loss，参与反向传播。梯度链完整：

```
loss → per_token_loss → per_token_kl → per_token_logps → model params
```

KL 同时作为 metric 记录（line 2689-2690），但主要角色是 **loss component**。

项目代码 `/root/autodl-tmp/freige/training/grpo_trainer.py` 直接使用 `trl.GRPOTrainer`，无自定义 KL 逻辑。`beta = args.kl_coef = 0.05`，`use_bias_correction_kl=False`（默认），`loss_type="grpo"`（默认）。

---

## 2. Clamp/Clip 保护：per_token_kl 无任何数值保护

| 组件 | 有无 clamp | 说明 |
|------|-----------|------|
| Policy loss (coef_1) | ✅ `clamp(1-ε, 1+ε)` | PPO-style clipping |
| **per_token_kl** | **❌ 无** | `exp(r)` 可产生任意大值 |
| use_bias_correction_kl | N/A | 默认 False，未开启 |
| VESPO/off-policy 的 log_ratio | ✅ `clamp(-20, 20)` | 仅限 VESPO 路径，KL 路径无 |
| max_grad_norm | ✅ 1.0（默认） | 梯度裁剪，最后防线 |

**核心问题**：当 `ref_logps - model_logps` 较大时，`exp()` 无上界保护。差值为 22 时 `exp(22) ≈ 3.6×10⁹`，恰好对应 step 5 的观测值 3.8×10⁹。

---

## 3. num_iterations=2 + QLoRA 数值稳定性

### 3.1 num_iterations=2 的放大效应

```
Generation → old_per_token_logps (固定), ref_per_token_logps (固定)
  ├─ Iteration 1: model_logps_1 → gradient step → 模型更新
  └─ Iteration 2: model_logps_2 → gradient step → 模型更新（ref_logps 未刷新）
```

- ref_per_token_logps 在 generation 时计算一次，两轮迭代不刷新
- 第一轮梯度更新后模型进一步偏离 reference → 第二轮 `|ref_logps - model_logps|` 更大 → KL 更高
- Policy loss 有 PPO clipping 保护，**但 KL 项无此保护**，成为 num_iterations>1 时的数值风险点

### 3.2 QLoRA 量化影响

- Reference = base model（adapter disabled），本身 4-bit 量化
- 量化噪声使 ref_logps 与真实 base model 存在偏差，被 `exp()` 指数放大
- 但这是常数偏差，不随训练步数恶化，非主因

### 3.3 KL 爆炸根因

观测：step 5 KL ≈ 3.8×10⁹ (r≈22)，step 15 KL ≈ 3.4×10¹¹ (r≈26.5)

公式中 `r = ref_logps - model_logps`：
- `r > 0`（model 概率低于 reference）→ `exp(r)` 爆炸
- `r < 0`（model 概率高于 reference）→ `exp(r) < 1`，KL 小

KL 爆炸说明存在 token 的 **model logprob 远低于 reference**。最可能的场景：
1. Reward 信号惩罚了某些 base model 常用 token → 概率被压低 → 与 reference 差距拉大
2. IE 任务的 JSON 格式训练使 token 分布大幅偏移
3. 长 completion 中某些位置出现 logprob 崩塌

---

## 4. 结论与风险评估

### 当前状态：⚠️ 危险但尚未致命

| 指标 | 状态 | 解读 |
|------|------|------|
| KL | 10⁹→10¹¹，持续恶化 | 严重溢出 |
| grad_norm | 稳定 0.02 | 梯度链路未崩溃 |
| rewards | 缓慢上升 | 训练信号仍有效 |

### KL 溢出的实际影响

**1. KL 已主导 loss**：`beta * per_token_kl = 0.05 × 10⁹ = 5×10⁷`，正常 policy loss 为 O(1)。KL 项的贡献高出 7 个数量级。

**2. grad_norm 为何稳定**：KL 梯度 `d(KL)/d(logp) = 1 - exp(r)` 虽大，但经 softmax Jacobian（元素 O(1/V)）和多层反向传播后被大幅衰减。QLoRA 低秩进一步限制有效梯度维度。

**3. 训练质量**：KL penalty 正在过度拉回模型向 reference 靠拢（远超设计意图）。当前 reward 上升速度很可能比无 KL 溢出时慢得多——**KL 在拖慢学习**。

**4. 崩溃风险**：bfloat16 max ≈ 3.4×10³⁸。当 `r ≈ 88` 时 `exp(r)` 溢出 inf → loss=NaN → 训练崩溃。以当前恶化速度（10 步 ~100x），约 50-100 步后可能触发。

### 建议（按优先级）

1. **治本**：在 TRL 源码 line 2605 后加 `per_token_kl = per_token_kl.clamp(max=100.0)`
2. **简单**：降 `beta` 到 0.01 或 0（设 `kl_coef=0` 则 TRL 跳过整个 KL 路径）
3. **缓解**：改 `num_iterations=1`，减少每轮 KL 放大
4. **监控**：在 wandb 中追踪 `loss` 曲线，若 loss 也指数增长则立即干预
