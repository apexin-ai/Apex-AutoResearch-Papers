# Event-Gated Adaptive-Horizon RSSM: Implementation Design

**Codebase**: NM512/dreamerv3-torch (PyTorch)
**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.

---

## Architecture Overview (ASCII)

```
                          IMAGINATION LOOP
 ┌──────────────────────────────────────────────────────────────────────┐
 │                                                                      │
 │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │
 │  │ prev    │    │           │    │          │    │               │  │
 │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │
 │  │         │    │           │    │ layers   │    │               │  │
 │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │
 │                 │  + Dt_emb │                            │          │
 │                 └───────────┘                       deter_t         │
 │                       ▲                                 │          │
 │                       │                                 ▼          │
 │              ┌────────┴───────┐              ┌──────────────────┐  │
 │              │  Dt Embedding  │              │  img_out_layers  │  │
 │              │  (learned,     │              └────────┬─────────┘  │
 │              │   dim=32)      │                       │            │
 │              └────────┬───────┘                       ▼            │
 │                       │                      ┌──────────────────┐  │
 │                       │                      │  stats layer     │  │
 │                       │                      │  -> stoch_t      │  │
 │              ┌────────┴───────┐              └────────┬─────────┘  │
 │              │  EVENT GATE    │                       │            │
 │              │  MLP(h_t, z_t) │◀──────────────────────┤            │
 │              │                │                       │            │
 │              │  Gumbel-       │              ┌────────┴─────────┐  │
 │              │  Softmax       │              │  feat_t =        │  │
 │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │
 │              └────────────────┘              │   deter_t]       │  │
 │                                              └────────┬─────────┘  │
 │                                                       │            │
 │                                                       ▼            │
 │                                              ┌──────────────────┐  │
 │                                              │  Actor / Critic  │  │
 │                                              │  Reward / Cont   │  │
 │                                              └──────────────────┘  │
 │                                                                      │
 └──────────────────────────────────────────────────────────────────────┘

Gate supervision (training only):
  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)
  target: large delta -> small Dt, small delta -> large Dt
```

---

## Module A: Variable-Rate RSSM Modifications

### A.1 Core Change: Dt Embedding in GRU Input

The RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.

**File**: `networks.py`

**Constructor changes** (`RSSM.__init__`, lines 14-98):

```python
# New parameters in __init__ signature:
#   max_dt: int = 8          # K, maximum temporal stride
#   dt_embed_dim: int = 32   # dimensionality of Dt embedding

# After line 46 (self._device = device):
self._max_dt = max_dt
self._dt_embed_dim = dt_embed_dim
self._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)
nn.init.normal_(self._dt_embedding.weight, std=0.01)

# Modify inp_dim calculation (lines 49-52):
# Original:
#   if self._discrete:
#       inp_dim = self._stoch * self._discrete + num_actions
#   else:
#       inp_dim = self._stoch + num_actions
# New:
if self._discrete:
    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim
else:
    inp_dim = self._stoch + num_actions + dt_embed_dim
```

**`img_step` changes** (lines 208-233):

```python
def img_step(self, prev_state, prev_action, dt=None, sample=True):
    prev_stoch = prev_state["stoch"]
    if self._discrete:
        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]
        prev_stoch = prev_stoch.reshape(shape)

    # Dt embedding: default to dt=1 if not provided (backward compat)
    if dt is None:
        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,
                        device=prev_stoch.device)
    # dt is 1-indexed {1,...,K}, embedding is 0-indexed
    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)

    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)
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

**`obs_step` changes** (lines 174-206): Pass `dt=None` (defaults to 1) to `img_step` call at line 195. During world model training from replay, Dt is always 1 (we observe every real timestep); variable Dt only applies during imagination.

```python
# Line 195: prior = self.img_step(prev_state, prev_action)
# No change needed if dt defaults to None->1 inside img_step
```

**`observe` changes** (lines 127-143): No change. Training always uses Dt=1 on real data.

**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:

```python
def imagine_with_action(self, action, state, dt_sequence=None):
    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))
    action = swap(action)
    if dt_sequence is not None:
        dt_sequence = swap(dt_sequence)
        prior = tools.static_scan(
            lambda s, a, dt: self.img_step(s, a, dt=dt),
            [action, dt_sequence], state
        )
    else:
        prior = tools.static_scan(self.img_step, [action], state)
    prior = prior[0]
    prior = {k: swap(v) for k, v in prior.items()}
    return prior
```

### A.2 Config Additions

**File**: `configs.yaml`, under `defaults`:

```yaml
# Event-Gated Adaptive Horizon
gate_max_dt: 8              # K: max temporal stride
gate_dt_embed_dim: 32       # Dt embedding dimension
gate_hidden_units: 256      # gate MLP hidden size
gate_hidden_layers: 2       # gate MLP depth
gate_tau_init: 1.0          # Gumbel-Softmax initial temperature
gate_tau_final: 0.5         # Gumbel-Softmax final temperature
gate_tau_anneal_steps: 200000  # linear anneal duration
gate_loss_weight: 1.0       # gate supervision loss coefficient
gate_entropy_bonus: 0.01    # entropy regularization weight
gate_curriculum_phase1: 50000   # forced Dt=1 phase
gate_curriculum_phase2: 150000  # linear ramp phase end
gate_enabled: false         # master switch
```

**Hyperparameter search ranges**:

| Parameter | Default | Search Range | Notes |
|---|---|---|---|
| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |
| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |
| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |
| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |
| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |
| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |
| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |

### A.3 WorldModel Constructor Wiring

**File**: `models.py`, `WorldModel.__init__` (lines 30-101)

```python
# After line 54 (self.dynamics = networks.RSSM(...)):
# Add max_dt and dt_embed_dim to RSSM constructor call:
self.dynamics = networks.RSSM(
    config.dyn_stoch,
    config.dyn_deter,
    config.dyn_hidden,
    config.dyn_rec_depth,
    config.dyn_discrete,
    config.act,
    config.norm,
    config.dyn_mean_act,
    config.dyn_std_act,
    config.dyn_min_std,
    config.unimix_ratio,
    config.initial,
    config.num_actions,
    self.embed_size,
    config.device,
    max_dt=config.gate_max_dt if config.gate_enabled else 1,
    dt_embed_dim=config.gate_dt_embed_dim,
)
```

---

## Module B: Event Gate Architecture

### B.1 Gate Network

**File**: `networks.py` (new class, insert after RSSM class ~line 291)

```python
class EventGate(nn.Module):
    def __init__(
        self,
        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)
        max_dt=8,
        hidden_units=256,
        hidden_layers=2,
        act="SiLU",
        norm=True,
        tau_init=1.0,
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
        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)
        return self._tau_init + frac * (self._tau_final - self._tau_init)

    def forward(self, feat, step, hard=False):
        """
        Args:
            feat: (batch, feat_size) - concatenated [stoch, deter]
            step: int - current training step for temperature annealing
            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)
        Returns:
            dt_onehot: (batch, max_dt) - one-hot or soft assignment
            dt_index:  (batch,) - integer Dt in {1,...,K}
            logits:    (batch, max_dt) - raw logits for entropy computation
        """
        x = self.mlp(feat)
        logits = self.logit_layer(x)  # (batch, max_dt)

        tau = self.get_tau(step)
        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)

        # Dt index: 1-indexed
        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)

        return dt_onehot, dt_index, logits

    def entropy(self, logits):
        """Categorical entropy of the gate distribution."""
        probs = F.softmax(logits, dim=-1)
        log_probs = F.log_softmax(logits, dim=-1)
        return -(probs * log_probs).sum(dim=-1)  # (batch,)
```

### B.2 Gate in Imagination Loop

**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)

The gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of "wall-clock" steps consumed varies, but the loop always runs `horizon` imagined transitions.

```python
def _imagine(self, start, policy, horizon):
    dynamics = self._world_model.dynamics
    gate = self._world_model.event_gate  # added to WorldModel
    config = self._config
    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))
    start = {k: flatten(v) for k, v in start.items()}
    step = self._world_model._step

    # Determine if gate is active based on curriculum
    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)

    def step_fn(prev, _):
        state, _, _, prev_dt = prev
        feat = dynamics.get_feat(state)
        inp = feat.detach()
        action = policy(inp).sample()

        # Use previous gate decision as Dt for this transition
        succ = dynamics.img_step(state, action, dt=prev_dt)
        succ_feat = dynamics.get_feat(succ)

        # Gate decides Dt for the NEXT step
        if gate_active:
            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)
        else:
            batch_size = succ_feat.shape[0]
            next_dt = torch.ones(batch_size, dtype=torch.long,
                                 device=succ_feat.device)
            gate_logits = None

        return succ, feat, action, next_dt

    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],
                         dtype=torch.long, device=config.device)

    succ, feats, actions, dts = tools.static_scan(
        step_fn, [torch.arange(horizon)],
        (start, None, None, init_dt)
    )
    states = {k: torch.cat([start[k][None], v[:-1]], 0)
              for k, v in succ.items()}

    return feats, states, actions, dts  # dts: (horizon, batch)
```

### B.3 Registering Gate in WorldModel

**File**: `models.py`, `WorldModel.__init__` (after line 86):

```python
if config.gate_enabled:
    self.event_gate = networks.EventGate(
        feat_size=feat_size,
        max_dt=config.gate_max_dt,
        hidden_units=config.gate_hidden_units,
        hidden_layers=config.gate_hidden_layers,
        act=config.act,
        norm=config.norm,
        tau_init=config.gate_tau_init,
        tau_final=config.gate_tau_final,
        tau_anneal_steps=config.gate_tau_anneal_steps,
    )
else:
    self.event_gate = None
```

---

## Module C: Gate Supervision

### C.1 Supervision Signal

The gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).

**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.

```python
def compute_gate_targets(feats, max_dt):
    """
    Args:
        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features
    Returns:
        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt
    """
    feats = feats.detach()  # stop gradient

    # L2 delta between consecutive states
    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)

    # Normalize deltas to [0, 1] within each batch
    delta_min = deltas.min(dim=0, keepdim=True).values
    delta_max = deltas.max(dim=0, keepdim=True).values
    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)

    # Large delta -> small Dt (index 0 = Dt=1)
    # Small delta -> large Dt (index K-1 = Dt=K)
    # Map normalized delta to a "preferred Dt" float in [1, K]
    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)

    # Create soft target via Gaussian kernel around preferred_dt
    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,
                              device=feats.device)  # (max_dt,)
    # (time-1, batch, 1) vs (max_dt,)
    sigma = 1.0
    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2
    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)

    return target_dist
```

### C.2 Gate Loss

```python
def gate_loss(gate_logits, target_dist):
    """
    Cross-entropy between gate's predicted distribution and supervision target.

    Args:
        gate_logits: (time-1, batch, max_dt) - raw gate logits
        target_dist: (time-1, batch, max_dt) - soft target from state deltas
    Returns:
        loss: (time-1, batch) - per-step per-batch loss
    """
    log_probs = F.log_softmax(gate_logits, dim=-1)
    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy
    return loss
```

### C.3 Integration in WorldModel._train

**File**: `models.py`, `WorldModel._train` (lines 108-174)

The gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).

```python
# After line 147 (model_loss = sum(scaled.values()) + kl_loss):

if self._config.gate_enabled and self.event_gate is not None:
    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM
    # Run gate on each timestep's features
    # feat shape: (batch, time, feat_dim)
    B, T, D = feat.shape
    feat_flat = feat.reshape(B * T, D)
    _, _, gate_logits_flat = self.event_gate(
        feat_flat, self._step, hard=False
    )
    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)

    # Supervision target from state deltas (time dim = axis 1)
    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)
    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)
    # target_dist: (time-1, batch, max_dt)

    # Gate logits for steps 1..T-1 (we need t and t-1)
    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)

    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)

    # Entropy bonus
    g_entropy = self.event_gate.entropy(
        g_logits.reshape(-1, self._config.gate_max_dt)
    ).reshape(g_loss.shape)

    # Curriculum: scale gate loss
    step = self._step
    if step < self._config.gate_curriculum_phase1:
        gate_scale = 0.0  # Phase 1: no gate training
    elif step < self._config.gate_curriculum_phase2:
        # Phase 2: linear ramp
        progress = (step - self._config.gate_curriculum_phase1) / (
            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1
        )
        gate_scale = progress
    else:
        gate_scale = 1.0  # Phase 3: full gate

    total_gate_loss = gate_scale * (
        self._config.gate_loss_weight * g_loss.mean()
        - self._config.gate_entropy_bonus * g_entropy.mean()
    )
    model_loss = model_loss + total_gate_loss
```

### C.4 Stop-Gradient Design

Critical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.

- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input
- `target_dist` uses `feats.detach()` internally
- Only `self.event_gate` parameters receive gradients from gate loss
- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads

---

## Module D: Adapted Lambda-Returns

### D.1 Standard vs. Adapted Lambda-Return

**Standard** (from `tools.py:691-717`):

$$V_t^\lambda = r_{t+1} + \gamma \left[(1-\lambda) V(s_{t+1}) + \lambda V_{t+1}^\lambda\right]$$

**Adapted for variable Dt**:

$$V_t^\lambda = r_{t:t+\Delta t}^{\text{cum}} + \gamma^{\Delta t} \left[(1-\lambda) V(s_{t+\Delta t}) + \lambda V_{t+\Delta t}^\lambda\right]$$

where:
- $r_{t:t+\Delta t}^{\text{cum}}$: cumulated reward over Dt skipped steps (in imagination, the reward head predicts a single reward for the jumped state; we scale it by Dt as an approximation)
- $\gamma^{\Delta t}$: discount raised to the power of the stride

### D.2 Modified lambda_return

**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):

```python
def lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):
    """
    Lambda-return with variable temporal strides.

    Args:
        reward: (time, batch, 1) - per-step imagined reward
        value:  (time, batch, 1) - value estimates
        pcont:  (time, batch, 1) - continuation probability * base discount
        dt:     (time, batch) or (time, batch, 1) - temporal stride per step
        bootstrap: (batch, 1) - terminal value
        lambda_: float
        axis: int
    Returns:
        returns: list of (batch, 1) tensors
    """
    assert len(reward.shape) == len(value.shape)
    if isinstance(pcont, (int, float)):
        pcont = pcont * torch.ones_like(reward)
    if dt.dim() == 2:
        dt = dt.unsqueeze(-1)  # (time, batch, 1)
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

    # Adjust reward and discount for variable Dt:
    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)
    reward_adj = reward * dt
    # gamma^Dt
    pcont_adj = pcont ** dt

    next_values = torch.cat([value[1:], bootstrap[None]], 0)
    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)

    returns = static_scan_for_lambda_return(
        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,
        (inputs, pcont_adj), bootstrap
    )
    if axis != 0:
        returns = returns.permute(dims)
    return returns
```

### D.3 Integration in ImagBehavior._compute_target

**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):

```python
def _compute_target(self, imag_feat, imag_state, reward, dts=None):
    if "cont" in self._world_model.heads:
        inp = self._world_model.dynamics.get_feat(imag_state)
        discount = self._config.discount * self._world_model.heads["cont"](inp).mean
    else:
        discount = self._config.discount * torch.ones_like(reward)
    value = self.value(imag_feat).mode()

    if dts is not None and self._config.gate_enabled:
        target = tools.lambda_return_variable_dt(
            reward[1:],
            value[:-1],
            discount[1:],
            dts[1:],  # Dt for each imagined step
            bootstrap=value[-1],
            lambda_=self._config.discount_lambda,
            axis=0,
        )
    else:
        target = tools.lambda_return(
            reward[1:],
            value[:-1],
            discount[1:],
            bootstrap=value[-1],
            lambda_=self._config.discount_lambda,
            axis=0,
        )

    # Adjusted weights: cumulative discount accounts for variable Dt
    if dts is not None and self._config.gate_enabled:
        pcont_adj = discount ** dts.unsqueeze(-1).float()
        weights = torch.cumprod(
            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0
        ).detach()
    else:
        weights = torch.cumprod(
            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0
        ).detach()

    return target, weights, value[:-1]
```

### D.4 Reward Accumulation Approximation

In imagination, we don't have access to intermediate rewards between skipped steps. Two options:

1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.

2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.

We use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).

---

## Module E: Gate Collapse Prevention

### E.1 Failure Modes

Gate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.

### E.2 Entropy Regularization

Already included in Module C's loss:

```python
total_gate_loss = gate_scale * (
    config.gate_loss_weight * g_loss.mean()
    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy
)
```

The entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.

### E.3 Gating Curriculum (Three Phases)

| Phase | Steps | Behavior | Rationale |
|---|---|---|---|
| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |
| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |
| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |

Implementation (already shown in Module C.3):

```python
if step < config.gate_curriculum_phase1:
    gate_scale = 0.0
elif step < config.gate_curriculum_phase2:
    progress = (step - config.gate_curriculum_phase1) / (
        config.gate_curriculum_phase2 - config.gate_curriculum_phase1
    )
    gate_scale = progress
else:
    gate_scale = 1.0
```

In `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.

### E.4 Collapse Detection Metrics

**File**: `models.py`, add to metrics in `ImagBehavior._train`:

```python
if self._config.gate_enabled and dts is not None:
    dts_float = dts.float()
    metrics["gate_dt_mean"] = to_np(torch.mean(dts_float))
    metrics["gate_dt_std"] = to_np(torch.std(dts_float))
    metrics["gate_dt_min"] = to_np(torch.min(dts_float))
    metrics["gate_dt_max"] = to_np(torch.max(dts_float))

    # Distribution over K bins
    dt_counts = torch.bincount(
        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1
    )[1:]  # skip bin 0
    dt_dist = dt_counts.float() / dt_counts.sum()
    for k in range(self._config.gate_max_dt):
        metrics[f"gate_dt_{k+1}_frac"] = to_np(dt_dist[k])

    # Entropy of empirical Dt distribution (collapse indicator)
    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()
    metrics["gate_empirical_entropy"] = to_np(emp_entropy)
    max_entropy = np.log(self._config.gate_max_dt)
    metrics["gate_entropy_ratio"] = to_np(emp_entropy) / max_entropy
```

**Collapse alert thresholds**:
- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values
- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed
- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating
- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates

### E.5 Automatic Recovery (Optional)

If collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:

```python
if gate_entropy_ratio < 0.2:
    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost
else:
    effective_entropy_bonus = config.gate_entropy_bonus
```

This is optional and aggressive. Prefer tuning the base entropy bonus instead.

---

## Module F: Replay Buffer Subsampling Strategy

### F.1 Problem Statement

The world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.

However, to train the RSSM to understand what "Dt=3" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.

### F.2 Strategy 1: Post-Sampling Temporal Skip

After sampling a standard `(batch_size, batch_length)` sequence from replay:
1. For a fraction of batch elements, randomly select skip patterns
2. Index into the sequence to create variable-rate subsequences
3. Train RSSM with corresponding Dt labels

```python
def apply_temporal_skip(data, max_dt, skip_prob=0.3):
    """
    Args:
        data: dict of (batch, time, ...) tensors from replay
        max_dt: int
        skip_prob: probability of applying skip to each batch element
    Returns:
        data_skipped: dict with same batch dim but potentially shorter time dim
        dt_labels: (batch, time') tensor of Dt values used
    """
    B, T = data["action"].shape[:2]
    dt_labels = torch.ones(B, T, dtype=torch.long)

    for b in range(B):
        if random.random() < skip_prob:
            t = 0
            indices = [0]
            while t < T - 1:
                dt = random.randint(1, min(max_dt, T - 1 - t))
                t += dt
                indices.append(t)
                dt_labels[b, len(indices) - 1] = dt
            # Subsample this batch element
            for key in data:
                data[key][b] = data[key][b, indices]
    return data, dt_labels
```

**Pros**: Simple, no replay buffer changes.
**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.

### F.3 Strategy 2: Precomputed Variable-Rate Subsequences

At episode storage time, precompute and store multiple temporal resolutions:
- For each episode, generate several subsampled versions with different skip patterns
- Store cumulated rewards for skipped intervals
- Sample from this augmented dataset

**Pros**: Efficient at training time; exact reward cumulation.
**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.

### F.4 Recommended Approach: Strategy 1 with Modifications

Strategy 1, but only applied to a separate "gate training" phase within each world model update:

```python
# In WorldModel._train, after standard RSSM training:
if self._config.gate_enabled:
    # Sample a separate batch for gate-aware RSSM fine-tuning
    # Standard RSSM loss on full-rate data (as before)
    # Gate supervision on the same full-rate data (state deltas)
    # No need to actually skip in replay -- the gate learns from
    # observing which states are "skippable" in the full-rate stream
```

**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means "predict what happens if I advance 3 steps." The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.

The RSSM can generalize to larger Dt because:
1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)
2. The GRU learns to scale its update magnitude based on Dt_emb
3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable

**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.

---

## File Modification Summary

| File | Function/Class | Lines | Change Type |
|---|---|---|---|
| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |
| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |
| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |
| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |
| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |
| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |
| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |
| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |
| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |
| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |
| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |
| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |

---

## Risks and Mitigations

### R1: Training Instability

**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.

**Mitigation**:
- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible
- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate
- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences

### R2: Gate Collapse

**Risk**: Gate degenerates to constant Dt, losing adaptivity.

**Mitigation**:
- Entropy regularization in gate loss
- Curriculum prevents premature commitment
- Monitoring metrics with alert thresholds (Section E.4)
- Gumbel-Softmax temperature annealing ensures exploration early on

### R3: Reward Approximation Error

**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.

**Mitigation**:
- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance
- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small
- Monitor `imag_reward` statistics for anomalies

### R4: Compatibility with Original DreamerV3

**Risk**: Modified code breaks when `gate_enabled=false`.

**Mitigation**:
- All gate logic is guarded by `config.gate_enabled`
- `img_step` defaults `dt=None` which maps to Dt=1
- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)
- `_compute_target` falls back to standard `lambda_return`
- Net-zero change to behavior when `gate_enabled=false`

### R5: Computational Overhead

**Risk**: Gate MLP adds forward-pass cost in imagination.

**Mitigation**:
- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)
- Gate is only called during imagination (not observation/training unroll)
- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute

### R6: Replay Buffer Efficiency

**Risk**: Strategy 1 subsampling wastes loaded data.

**Mitigation**:
- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.
- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the "wasted" frames still contributed to the standard RSSM loss before subsampling.
