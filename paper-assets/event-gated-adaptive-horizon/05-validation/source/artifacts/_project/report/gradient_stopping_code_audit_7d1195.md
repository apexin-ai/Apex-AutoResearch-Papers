# Selective Gradient Stopping — Code Audit

## 1. dt_embedding 数据流

### 创建
- **文件**: `networks.py:57`
- **定义**: `self._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)` (RSSM.__init__)
- **条件**: `max_dt > 1 and dt_embed_dim > 0`
- **初始化**: `nn.init.normal_(weight, std=0.01)`

### 注入 RSSM (img_step)
- **文件**: `networks.py:249-260` (RSSM.img_step)
- **方式**: **concat** — dt_emb 与 prev_stoch, prev_action 拼接后进入 `_img_in_layers`

```
dt_emb = self._dt_embedding(dt - 1)                    # (batch, dt_embed_dim)
x = torch.cat([prev_stoch, prev_action, dt_emb], -1)   # (batch, stoch*discrete + act + dt_embed_dim)
x = self._img_in_layers(x)                              # Linear → LayerNorm → SiLU → (batch, hidden)
x, deter = self._cell(x, [deter])                       # GRU: (batch, hidden) + (batch, deter) → (batch, deter)
```

### 融合路径
```
dt_emb → [concat] → _img_in_layers (Linear+LN+SiLU) → GRU Cell → deter
                                                                      ↓
                                                            _img_out_layers → prior stoch
                                                                      ↓
                                                            get_feat = cat(stoch, deter)
```

**关键**: dt_emb 在 GRU 中与 prev_stoch/prev_action 的信息不可逆地混合。GRU 输出的 `deter` 包含了来自三个源的混合信息，**无法在 get_feat 层面分离 dt_emb 分量**。

### RSSM State Dict
- **Keys**: `{stoch, deter, logit}` (discrete) 或 `{stoch, deter, mean, std}` (continuous)
- dt_emb **不是**独立 key，已融合到 `deter` 中
- `stoch` 也间接包含 dt_emb 信息（通过 prior 从 deter 计算而来）

### obs_step 路径
- `networks.py:207-240`: obs_step 内部调用 `self.img_step(prev_state, prev_action, dt=dt)` 计算 prior
- posterior 使用 prior 的 deter + embed 计算新 stoch
- **结论**: posterior state 的 `deter` 完全等于 prior 的 `deter`，包含 dt_emb 信息

---

## 2. Reward Head 数据流

### 定义
- **文件**: `models.py:~100-110` (WorldModel.__init__)
- **类型**: `networks.MLP(feat_size, (255,), ...)`
- **输入维度**: `feat_size = dyn_stoch * dyn_discrete + dyn_deter`（与 get_feat 输出维度一致）

### World Model 训练时的数据流
- **文件**: `models.py:~253` (WorldModel._train 的 head loop)

```python
for name, head in self.heads.items():
    grad_head = name in self._config.grad_heads  # reward 通常在 grad_heads 中
    feat = self.dynamics.get_feat(post)           # cat(stoch, deter)，包含 dt_emb 信息
    feat = feat if grad_head else feat.detach()
    pred = head(feat)
```

**梯度路径**: `reward_loss → reward_head → feat → {stoch, deter} → GRU → _img_in_layers → dt_emb.weight`

### Imagination 时的数据流
- **文件**: `dreamer.py:124-126`

```python
reward = lambda f, s, a: self._wm.heads["reward"](
    self._wm.dynamics.get_feat(s)
).mode()
```

- `s = imag_state`，由 `dynamics.img_step(state, action, dt=prev_dt)` 产生
- **但**：imagination 在 `RequiresGrad(self.actor)` 上下文中执行（`models.py:490`），world model 参数（含 dt_emb）的 `requires_grad=False`
- **结论**: imagination 期间 dt_emb **不会**收到梯度，此路径天然安全

### Value Head 数据流
- **文件**: `models.py:~443` (ImagBehavior.__init__)
- `self.value = networks.MLP(feat_size, (255,), ...)`
- Value loss: `value_loss = -value.log_prob(target.detach())` — target 被 detach
- Value optimizer 只更新 value 参数，不更新 world model 参数
- **结论**: value head 不会给 dt_emb 传梯度

---

## 3. 唯一需要修复的梯度路径

只有 **一条** 路径需要切断：

```
WorldModel._train:
  reward_loss → reward_head(feat) → feat = get_feat(post) → post["deter"] → GRU → _img_in_layers → dt_emb.weight
```

Imagination 和 value training 已通过 `RequiresGrad` 和 `target.detach()` 机制自然隔离。

---

## 4. 具体修改方案

### 方案: Backward Hook + Gradient Subtraction

**原理**: 在 optimizer backward 过程中，用 hook 将 dt_emb.weight 的梯度中 reward 贡献减去。

**文件**: `models.py`, WorldModel._train 方法

**位置**: 在 `mean_model_loss` 计算完成后、`self._model_opt(...)` 调用前

**代码** (约15行):

```python
# ======== Selective Gradient Stopping (reward → dt_emb) ========
_sgs_handle = None
if getattr(self._config, 'reward_dt_emb_detach', False) and self.dynamics._dt_embedding is not None:
    _scaler = self._model_opt._scaler
    _reward_grad = torch.autograd.grad(
        _scaler.scale(torch.mean(scaled['reward'])),
        self.dynamics._dt_embedding.weight,
        retain_graph=True,
        allow_unused=True,
    )[0]
    if _reward_grad is not None:
        _sgs_handle = self.dynamics._dt_embedding.weight.register_hook(
            lambda grad, _rg=_reward_grad: grad - _rg
        )
# ===============================================================

metrics.update(self._model_opt(mean_model_loss, self.parameters()))

# ======== Cleanup ========
if _sgs_handle is not None:
    _sgs_handle.remove()
# =========================
```

### 工作原理
1. `torch.autograd.grad(scaled_reward_loss, dt_emb.weight)` — 预计算 reward loss 对 dt_emb 的**scaled**梯度（与 optimizer backward 使用相同 scale）
2. `register_hook(lambda grad, _rg: grad - _rg)` — 在 optimizer 的 backward 过程中，hook 将 dt_emb 的全梯度减去 reward 贡献
3. 最终 dt_emb.weight.grad = 全梯度 - reward 梯度 = decoder + kl + cont 梯度
4. optimizer.step() 使用修正后的梯度更新 dt_emb

### 插入位置

需要在 `mean_model_loss` 最终确定之后、`self._model_opt(...)` 之前。注意 gate_loss 可能在 model_loss 之后追加到 mean_model_loss：

```python
# models.py 中的结构:
model_loss = sum(scaled.values()) + kl_loss
mean_model_loss = torch.mean(model_loss)

if self._config.gate_enabled and ...:
    # gate_loss computation...
    mean_model_loss = mean_model_loss + gate_loss_weight * gate_loss

# >>> INSERT SGS CODE HERE <<<

metrics.update(self._model_opt(mean_model_loss, self.parameters()))
```

---

## 5. Config Flag

```yaml
reward_dt_emb_detach: False  # 默认关闭，兼容已有实验
```

- `True`: 切断 reward_loss → dt_emb 梯度
- `False`: 保持原有行为
- 与 `dt_emb_freeze: True` 的区别: freeze 完全冻结 dt_emb（所有梯度），detach 只切断 reward 路径，保留 decoder/kl 梯度

---

## 6. 潜在风险和注意事项

### 6.1 AMP/GradScaler 一致性
`autograd.grad` 必须使用 `_scaler.scale(loss)` 作为输入，确保与 optimizer backward 的 scaling 一致。如果 scale factor 在两次调用之间变化（不会，因为 `scaler.update()` 在 optimizer step 之后），会有不一致。**当前实现是安全的。**

### 6.2 cont head 梯度泄漏
`cont_loss → feat → deter → dt_emb` 路径未被切断。cont head 预测 episode 是否继续，与 reward 相关性较弱。如果需要更彻底的隔离，可扩展 config 为 `dt_emb_detach_heads: [reward, cont]`。

### 6.3 KL loss 路径
`kl_loss → prior → deter → dt_emb` 路径保持完整。KL loss 训练 dynamics 的预测准确性，不涉及 reward 偏差，应当保留。

### 6.4 Computational overhead
每个 WM training step 额外一次 `autograd.grad` 调用。这需要从 `scaled['reward']` 反向传播到 `dt_emb.weight`，经过 reward_head → feat → deter → GRU → _img_in_layers → dt_emb。开销约等于一次额外的 partial backward。dt_emb 参数量很小 (max_dt × dt_embed_dim ≈ 4×32=128)，但中间路径涉及 GRU 和整个 dynamics。预估增加 ~5-10% 训练时间。

### 6.5 `retain_graph` 内存
`autograd.grad(..., retain_graph=True)` 保留计算图。Optimizer 的 backward 也使用 `retain_graph=True`（默认）。图在第二次 `zero_grad()` 后释放。内存占用不变。

---

## 7. 验证方法

### 7.1 梯度检查 (训练时 hook)

在 WM training 中添加诊断代码：

```python
# 验证 dt_emb 是否收到 reward 梯度
if step % 1000 == 0 and self.dynamics._dt_embedding is not None:
    # 计算 reward 对 dt_emb 的梯度
    rg = torch.autograd.grad(
        torch.mean(scaled['reward']),
        self.dynamics._dt_embedding.weight,
        retain_graph=True, allow_unused=True
    )[0]
    if rg is not None:
        metrics['dt_emb_reward_grad_norm'] = to_np(rg.norm())
    
    # 计算 decoder 对 dt_emb 的梯度
    dg = torch.autograd.grad(
        torch.mean(scaled.get('image', scaled.get('decoder', torch.tensor(0.0)))),
        self.dynamics._dt_embedding.weight,
        retain_graph=True, allow_unused=True
    )[0]
    if dg is not None:
        metrics['dt_emb_decoder_grad_norm'] = to_np(dg.norm())
```

当 `reward_dt_emb_detach=True` 时：
- `dt_emb_reward_grad_norm` 应接近 0（hook 减去后）
- `dt_emb_decoder_grad_norm` 应非零（保留）

### 7.2 CIVO 消融实验

| 实验 | dt_emb_freeze | reward_dt_emb_detach | 预期 CIVO |
|------|--------------|---------------------|-----------|
| baseline (gate_enabled) | False | False | 有 (2.90x) |
| 015B (完全冻结) | True | False | 消失/减弱 |
| **SGS** | False | **True** | **应消失** |

如果 SGS 实验 CIVO 消失，但性能优于 015B（因为 dt_emb 仍能学习有用的 dynamics 表示），则验证了方案的正确性。

### 7.3 dt_emb weight 变化监控

```python
# 记录 dt_emb 权重在 reward-correlated 维度上的漂移
if step % 5000 == 0:
    w = self.dynamics._dt_embedding.weight.detach()
    metrics['dt_emb_weight_norm'] = to_np(w.norm())
    metrics['dt_emb_weight_diff_dt1_dt2'] = to_np((w[0] - w[1]).norm())
```

---

## 8. 与现有 dt_emb_freeze 的关系

当前已有 `dt_emb_freeze` flag (models.py:~97):
```python
if getattr(config, 'dt_emb_freeze', False) and self.dynamics._dt_embedding is not None:
    self.dynamics._dt_embedding.weight.requires_grad_(False)
```

| Flag | 效果 | decoder→dt_emb 梯度 | reward→dt_emb 梯度 | kl→dt_emb 梯度 |
|------|------|---------------------|-------------------|----------------|
| dt_emb_freeze=False, reward_dt_emb_detach=False | 原始 | ✓ | ✓ | ✓ |
| dt_emb_freeze=True | 完全冻结 | ✗ | ✗ | ✗ |
| **reward_dt_emb_detach=True** | **选择性停止** | **✓** | **✗** | **✓** |

`reward_dt_emb_detach` 是更精确的外科手术——保留 dt_emb 学习 dynamics 的能力，只切断 reward 偏差源。
