# ops kill and audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-and-audit_20260513T095620_result.json`
- **Structured JSON:** [`40422cd5bb3dacb4e88b.json`](../../sessions/40/40422cd5bb3dacb4e88b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有代码段已收集完毕。以下是完整输出：

---

## 任务 1: Kill exp_003

**PID 27009 已终止**（SIGTERM 成功，未需 SIGKILL）。

---

## 任务 2: 代码段

### 2a. `ImagBehavior._imagine` (models.py:519-580)

```python
def _imagine(self, start, policy, horizon):
    dynamics = self._world_model.dynamics
    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))
    start = {k: flatten(v) for k, v in start.items()}

    if self._config.gate_enabled:
        gate = self._world_model.event_gate
        config = self._config
        step = self._world_model._step

        gate_active = (
            gate is not None and step > 25000
        )

        def step_fn(prev, _):
            state, _, _, prev_dt = prev
            feat = dynamics.get_feat(state)
            inp = feat.detach()
            action = policy(inp).sample()
            succ = dynamics.img_step(state, action, dt=prev_dt)
            succ_feat = dynamics.get_feat(succ)
            if gate_active:
                _, next_dt, _ = gate(succ_feat.detach(), step, hard=True)
            else:
                batch_size = succ_feat.shape[0]
                next_dt = torch.ones(
                    batch_size, dtype=torch.long, device=succ_feat.device
                )
            return succ, feat, action, next_dt

        init_dt = torch.ones(
            start[list(start.keys())[0]].shape[0],
            dtype=torch.long, device=config.device,
        )
        succ, feats, actions, dts = tools.static_scan(
            step_fn, [torch.arange(horizon)],
            (start, None, None, init_dt),
        )
        states = {
            k: torch.cat([start[k][None], v[:-1]], 0)
            for k, v in succ.items()
        }
        return feats, states, actions, dts
    else:
        def step(prev, _):
            state, _, _ = prev
            feat = dynamics.get_feat(state)
            inp = feat.detach()
            action = policy(inp).sample()
            succ = dynamics.img_step(state, action)
            return succ, feat, action

        succ, feats, actions = tools.static_scan(
            step, [torch.arange(horizon)], (start, None, None)
        )
        states = {
            k: torch.cat([start[k][None], v[:-1]], 0)
            for k, v in succ.items()
        }
        return feats, states, actions
```

### 2b. `WorldModel._train` 中 gate 相关代码 (models.py:162-300)

```python
def _train(self, data):
    # action (batch_size, batch_length, act_dim)
    # image (batch_size, batch_length, h, w, ch)
    # reward (batch_size, batch_length)
    # discount (batch_size, batch_length)
    data = self.preprocess(data)

    if self._config.gate_enabled:
        self.gate_step += 1
        step = self._step
        if step < 25000:
            gate_scale = 0.0
        elif step < 75000:
            progress = (step - 25000) / (
                75000
                - 25000
            )
            gate_scale = progress
        else:
            gate_scale = 1.0

        effective_max_dt = 1 + gate_scale * (self._config.gate_max_dt - 1)
        data, dt_labels = tools.subsample_variable_dt(
            data, self._config.gate_max_dt, self._config.discount,
            effective_max_dt=effective_max_dt,
        )
    else:
        dt_labels = None

    with tools.RequiresGrad(self):
        with torch.cuda.amp.autocast(self._use_amp):
            embed = self.encoder(data)
            if dt_labels is not None:
                post, prior = self.dynamics.observe(
                    embed, data["action"], data["is_first"],
                    dt_labels=dt_labels,
                )
            else:
                post, prior = self.dynamics.observe(
                    embed, data["action"], data["is_first"]
                )
            kl_free = self._config.kl_free
            dyn_scale = self._config.dyn_scale
            rep_scale = self._config.rep_scale
            kl_loss, kl_value, dyn_loss, rep_loss = self.dynamics.kl_loss(
                post, prior, kl_free, dyn_scale, rep_scale
            )
            assert kl_loss.shape == embed.shape[:2], kl_loss.shape
            preds = {}
            for name, head in self.heads.items():
                grad_head = name in self._config.grad_heads
                feat = self.dynamics.get_feat(post)
                feat = feat if grad_head else feat.detach()
                pred = head(feat)
                if type(pred) is dict:
                    preds.update(pred)
                else:
                    preds[name] = pred
            losses = {}
            for name, pred in preds.items():
                loss = -pred.log_prob(data[name])
                assert loss.shape == embed.shape[:2], (name, loss.shape)
                losses[name] = loss
            scaled = {
                key: value * self._scales.get(key, 1.0)
                for key, value in losses.items()
            }
            model_loss = sum(scaled.values()) + kl_loss
            mean_model_loss = torch.mean(model_loss)

            if self._config.gate_enabled and self.event_gate is not None:
                gate_feat = self.dynamics.get_feat(post).detach()
                B_g, T_g, D_g = gate_feat.shape
                gate_feat_flat = gate_feat.reshape(B_g * T_g, D_g)
                step = self._step
                _, _, gate_logits_flat = self.event_gate(
                    gate_feat_flat, step, hard=False
                )
                gate_logits = gate_logits_flat.reshape(
                    B_g, T_g, self._config.gate_max_dt
                )

                feat_time = gate_feat.permute(1, 0, 2)
                target_dist = compute_gate_targets(
                    feat_time, self._config.gate_max_dt
                )

                g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)
                g_loss = gate_loss_fn(g_logits, target_dist)

                g_entropy = self.event_gate.entropy(
                    g_logits.reshape(-1, self._config.gate_max_dt)
                ).reshape(g_loss.shape)

                if step < 25000:
                    gate_scale = 0.0
                elif step < 75000:
                    progress = (step - 25000) / (
                        75000
                        - 25000
                    )
                    gate_scale = progress
                else:
                    gate_scale = 1.0

                entropy_frac = min(
                    step / max(self._config.gate_tau_anneal_steps, 1), 1.0
                )
                effective_entropy_bonus = (
                    self._config.gate_entropy_bonus_init
                    + entropy_frac
                    * (
                        self._config.gate_entropy_bonus_final
                        - self._config.gate_entropy_bonus_init
                    )
                )

                total_gate_loss = gate_scale * (
                    self._config.gate_loss_weight * g_loss.mean()
                    - effective_entropy_bonus * g_entropy.mean()
                )
                mean_model_loss = mean_model_loss + total_gate_loss

        metrics = self._model_opt(mean_model_loss, self.parameters())

    metrics.update(
        {f"{name}_loss": to_np(torch.mean(loss)) for name, loss in losses.items()}
    )
    metrics["kl_free"] = kl_free
    metrics["dyn_scale"] = dyn_scale
    metrics["rep_scale"] = rep_scale
    metrics["dyn_loss"] = to_np(torch.mean(dyn_loss))
    metrics["rep_loss"] = to_np(torch.mean(rep_loss))
    metrics["kl"] = to_np(torch.mean(kl_value))
    with torch.cuda.amp.autocast(self._use_amp):
        metrics["prior_ent"] = to_np(
            torch.mean(self.dynamics.get_dist(prior).entropy())
        )
        metrics["post_ent"] = to_np(
            torch.mean(self.dynamics.get_dist(post).entropy())
        )
        context = dict(
            embed=embed,
            feat=self.dynamics.get_feat(post),
            kl=kl_value,
            postent=self.dynamics.get_dist(post).entropy(),
        )

    if self._config.gate_enabled and self.event_gate is not None:
        metrics["gate_loss"] = to_np(total_gate_loss)
        metrics["gate_scale"] = gate_scale
        metrics["gate_entropy_bonus"] = effective_entropy_bonus

    post = {k: v.detach() for k, v in post.items()}
    return post, context, metrics
```

### 2c. `lambda_return_variable_dt` (tools.py:725-759)

```python
def lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):
    """Lambda-return with variable temporal strides.

    Reward is assumed to be cumulative-discounted (pre-computed during sub-sampling).
    Discount is raised to the power of dt: gamma^dt.
    """
    assert len(reward.shape) == len(value.shape), (reward.shape, value.shape)
    if isinstance(pcont, (int, float)):
        pcont = pcont * torch.ones_like(reward)
    if dt.dim() == 2:
        dt = dt.unsqueeze(-1)
    dt = dt.float()

    dims = list(range(len(reward.shape)))
    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]
    if axis != 0:
        reward = reward.permute(dims)
        value = value.permute(dims)
        pcont = pcont.permute(dims)
        dt = dt.permute(dims)

    if bootstrap is None:
        bootstrap = torch.zeros_like(value[-1])

    pcont_adj = pcont ** dt

    next_values = torch.cat([value[1:], bootstrap[None]], 0)
    inputs = reward + pcont_adj * next_values * (1 - lambda_)

    returns = static_scan_for_lambda_return(
        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,
        (inputs, pcont_adj), bootstrap
    )
    if axis != 0:
        returns = returns.permute(dims)
    return returns
```

### 2d. `EventGate` 类 (networks.py:336-410)

```python
class EventGate(nn.Module):
    """Learned event gate that decides per-step temporal stride dt in {1,...,K}."""

    def __init__(
        self,
        feat_size,
        max_dt=8,
        hidden_units=256,
        hidden_layers=2,
        act="SiLU",
        norm=True,
        tau_init=5.0,
        tau_final=0.5,
        tau_anneal_steps=200000,
    ):
        super(EventGate, self).__init__()
        self._max_dt = max_dt
        self._tau_init = tau_init
        self._tau_final = tau_final
        self._tau_anneal_steps = tau_anneal_steps

        act_fn = getattr(torch.nn, act)
        layers = []
        inp_dim = feat_size
        for i in range(hidden_layers):
            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))
            if norm:
                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))
            layers.append(act_fn())
            inp_dim = hidden_units
        self.mlp = nn.Sequential(*layers)
        self.mlp.apply(tools.weight_init)

        self.logit_layer = nn.Linear(hidden_units, max_dt)
        self.logit_layer.apply(tools.uniform_weight_init(0.01))

    def get_tau(self, step):
        """Linear temperature annealing from tau_init to tau_final."""
        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)
        return self._tau_init + frac * (self._tau_final - self._tau_init)

    def forward(self, feat, step, hard=False):
        """
        Args:
            feat: (batch, feat_size) — concatenated [stoch, deter]
            step: int — current training step for temperature annealing
            hard: bool — if True, use hard Gumbel-Softmax
        Returns:
            dt_onehot: (batch, max_dt) — one-hot or soft assignment
            dt_index:  (batch,) — integer dt in {1,...,K}
            logits:    (batch, max_dt) — raw logits for entropy computation
        """
        x = self.mlp(feat)
        logits = self.logit_layer(x)
        tau = self.get_tau(step)
        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)
        dt_index = torch.argmax(dt_onehot, dim=-1) + 1
        return dt_onehot, dt_index, logits

    def entropy(self, logits):
        """Categorical entropy of the gate distribution."""
        probs = F.softmax(logits, dim=-1)
        log_probs = F.log_softmax(logits, dim=-1)
        return -(probs * log_probs).sum(dim=-1)
```

### 2e. RSSM.img_step 中 dt 处理 (networks.py:241-278)

```python
def img_step(self, prev_state, prev_action, dt=None, sample=True):
    # (batch, stoch, discrete_num)
    prev_stoch = prev_state["stoch"]
    if self._discrete:
        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]
        # (batch, stoch, discrete_num) -> (batch, stoch * discrete_num)
        prev_stoch = prev_stoch.reshape(shape)

    if self._dt_embedding is not None:
        if dt is None:
            dt = torch.ones(
                prev_stoch.shape[0], dtype=torch.long,
                device=prev_stoch.device
            )
        dt_emb = self._dt_embedding(dt - 1)   # dt ∈ {1,...,K} → index {0,...,K-1}
        x = torch.cat([prev_stoch, prev_action, dt_emb], -1)
    else:
        x = torch.cat([prev_stoch, prev_action], -1)

    # (batch, stoch * discrete_num + action [+ dt_emb]) -> (batch, hidden)
    x = self._img_in_layers(x)
    for _ in range(self._rec_depth):
        deter = prev_state["deter"]
        x, deter = self._cell(x, [deter])
        deter = deter[0]
    x = self._img_out_layers(x)
    stats = self._suff_stats_layer("ims", x)
    if sample:
        stoch = self.get_dist(stats).sample()
    else:
        stoch = self.get_dist(stats).mode()
    prior = {"stoch": stoch, "deter": deter, **stats}
    return prior
```

### 补充: `subsample_variable_dt` (tools.py:762-830)

```python
def subsample_variable_dt(data, max_dt, discount, effective_max_dt=None):
    """Variable-dt sub-sampling of replay trajectories.

    Samples per-element dt from log-uniform over [1, effective_max_dt].
    Computes cumulative discounted reward and minimum continuation for each gap.

    Args:
        data: dict of tensors, each (B, T, ...).
        max_dt: config maximum dt (used as upper bound clamp).
        discount: scalar discount factor for cumulative reward.
        effective_max_dt: curriculum-controlled max dt.
            None or <=1 means no subsampling (pure dt=1, vanilla DreamerV3).
    """
    B, T = data["action"].shape[:2]
    device = data["action"].device

    if effective_max_dt is None:
        effective_max_dt = max_dt

    effective_max_dt = max(1, min(int(round(effective_max_dt)), max_dt))

    if effective_max_dt <= 1:
        dt_labels = torch.ones(B, T, dtype=torch.long, device=device)
        return data, dt_labels

    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(effective_max_dt))
    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, effective_max_dt)

    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()
    T_sub = sub_len.max().item()

    data_sub = {}
    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)
    reward_cum = torch.zeros(B, T_sub, *data["reward"].shape[2:], device=device)
    cont_min = torch.ones(B, T_sub, *data["cont"].shape[2:], device=device)

    for b in range(B):
        dt_b = dt_per_elem[b].item()
        indices = list(range(0, T, dt_b))
        L = len(indices)

        for key in data:
            if key not in data_sub:
                data_sub[key] = torch.zeros(
                    B, T_sub, *data[key].shape[2:],
                    dtype=data[key].dtype, device=device,
                )
            data_sub[key][b, :L] = data[key][b, indices]

        for i, t_start in enumerate(indices[:-1]):
            t_end = min(t_start + dt_b, T)
            span = t_end - t_start
            gamma_powers = discount ** torch.arange(
                span, dtype=torch.float, device=device
            )
            r_slice = data["reward"][b, t_start:t_end]
            reward_cum[b, i] = (gamma_powers * r_slice).sum(dim=0)
            cont_min[b, i] = data["cont"][b, t_start:t_end].min(dim=0).values

        dt_labels[b, :L] = dt_b

    data_sub["reward"] = reward_cum
    data_sub["cont"] = cont_min
    return data_sub, dt_labels
```

### 补充: `ImagBehavior._train` + `_compute_target` (models.py:433-615)

```python
def _train(self, start, objective):
    self._update_slow_target()
    metrics = {}

    with tools.RequiresGrad(self.actor):
        with torch.cuda.amp.autocast(self._use_amp):
            if self._config.gate_enabled:
                imag_feat, imag_state, imag_action, dts = self._imagine(
                    start, self.actor, self._config.imag_horizon
                )
            else:
                imag_feat, imag_state, imag_action = self._imagine(
                    start, self.actor, self._config.imag_horizon
                )
                dts = None
            reward = objective(imag_feat, imag_state, imag_action)
            actor_ent = self.actor(imag_feat).entropy()
            state_ent = self._world_model.dynamics.get_dist(imag_state).entropy()
            target, weights, base = self._compute_target(
                imag_feat, imag_state, reward, dts=dts
            )
            actor_loss, mets = self._compute_actor_loss(
                imag_feat, imag_action, target, weights, base,
            )
            actor_loss -= self._config.actor["entropy"] * actor_ent[:-1, ..., None]
            actor_loss = torch.mean(actor_loss)
            metrics.update(mets)
            value_input = imag_feat

    with tools.RequiresGrad(self.value):
        with torch.cuda.amp.autocast(self._use_amp):
            value = self.value(value_input[:-1].detach())
            target = torch.stack(target, dim=1)
            value_loss = -value.log_prob(target.detach())
            slow_target = self._slow_value(value_input[:-1].detach())
            if self._config.critic["slow_target"]:
                value_loss -= value.log_prob(slow_target.mode().detach())
            value_loss = torch.mean(weights[:-1] * value_loss[:, :, None])

    # ... metrics logging + gate dt stats ...

def _compute_target(self, imag_feat, imag_state, reward, dts=None):
    if "cont" in self._world_model.heads:
        inp = self._world_model.dynamics.get_feat(imag_state)
        discount = self._config.discount * self._world_model.heads["cont"](inp).mean
    else:
        discount = self._config.discount * torch.ones_like(reward)
    value = self.value(imag_feat).mode()

    if dts is not None and self._config.gate_enabled:
        target = tools.lambda_return_variable_dt(
            reward[1:], value[:-1], discount[1:], dts[1:],
            bootstrap=value[-1],
            lambda_=self._config.discount_lambda, axis=0,
        )
        pcont_adj = discount ** dts.unsqueeze(-1).float()
        weights = torch.cumprod(
            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0
        ).detach()
    else:
        target = tools.lambda_return(
            reward[1:], value[:-1], discount[1:],
            bootstrap=value[-1],
            lambda_=self._config.discount_lambda, axis=0,
        )
        weights = torch.cumprod(
            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0
        ).detach()
    return target, weights, value[:-1]
```

---

**dt 数据类型总结**：`dt` 全程为 `torch.long`（整数），取值 `{1,...,K}`。`EventGate.forward` 用 `argmax + 1` 产生 `dt_index`；`RSSM.img_step` 用 `dt - 1` 索引 embedding；`lambda_return_variable_dt` 中 `dt.float()` 转浮点后做 `pcont ** dt` 幂运算。Gumbel-Softmax 的 `hard=True` 用于 imagination，`hard=False` 用于训练 gate loss。

---
