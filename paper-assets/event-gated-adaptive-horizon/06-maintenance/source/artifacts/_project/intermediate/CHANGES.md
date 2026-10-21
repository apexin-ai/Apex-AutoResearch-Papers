# Event-Gated Adaptive-Horizon RSSM — Change Summary

Base: NM512/dreamerv3-torch (commit at 2026-05-13)

## configs.yaml

| Lines | Change |
|-------|--------|
| 1–3 | Added file header comment |
| 96–109 | Added `gate_*` hyperparameters under `defaults` section (14 new keys) |

New parameters: `gate_max_dt`, `gate_dt_embed_dim`, `gate_hidden_units`, `gate_hidden_layers`, `gate_tau_init` (5.0), `gate_tau_final` (0.5), `gate_tau_anneal_steps`, `gate_loss_weight`, `gate_entropy_bonus_init` (0.1), `gate_entropy_bonus_final` (0.01), `gate_curriculum_phase1`, `gate_curriculum_phase2`, `gate_enabled` (false).

## networks.py

| Lines | Function/Class | Change |
|-------|---------------|--------|
| 1–3 | — | File header comment |
| 34–35 | `RSSM.__init__` | Added `max_dt`, `dt_embed_dim` parameters to constructor signature |
| 50–56 | `RSSM.__init__` | Created `nn.Embedding(max_dt, dt_embed_dim)` when `max_dt > 1`, initialized with `std=0.01` |
| 62–64 | `RSSM.__init__` | Expanded `inp_dim` by `dt_embed_dim` when dt embedding exists |
| 131–143 | `RSSM.observe` | Added `dt_labels` parameter; when provided, passes per-step dt through `static_scan` to `obs_step` |
| 145–158 | `RSSM.imagine_with_action` | Added `dt_sequence` parameter; when provided, passes dt to `img_step` via lambda in `static_scan` |
| 174 | `RSSM.obs_step` | Added `dt=None` parameter, forwards to `img_step` |
| 195 | `RSSM.obs_step` | Changed `self.img_step(prev_state, prev_action)` → `self.img_step(prev_state, prev_action, dt=dt)` |
| 208 | `RSSM.img_step` | Added `dt=None` parameter |
| 215–224 | `RSSM.img_step` | When dt_embedding exists: default dt=1, embed dt, concat to GRU input. When no dt_embedding: original behavior. |
| 292–345 | `EventGate` (new) | MLP → Gumbel-Softmax gate. τ anneals from 5.0→0.5 over 200K steps. Methods: `forward(feat, step, hard)`, `entropy(logits)`, `get_tau(step)`. |

## tools.py

| Lines | Function | Change |
|-------|----------|--------|
| 1–3 | — | File header comment |
| 8 | — | Added `import math` |
| 721–763 | `lambda_return_variable_dt` (new) | Lambda-return adapted for variable temporal strides. Discount raised to `γ^dt`. Reward assumed pre-accumulated. Same scan-based implementation as `lambda_return`. |
| 766–815 | `subsample_variable_dt` (new) | Log-uniform sampling of per-element Δt∈{1,...,K}. Computes cumulative discounted reward `Σ γ^k r_{t+k}` and minimum continuation for each gap. Returns sub-sampled data dict + dt_labels. |

## models.py

| Lines | Function/Class | Change |
|-------|---------------|--------|
| 1–5 | — | File header comment |
| 8 | — | Added `import math` |
| 11 | — | Added `from torch.nn import functional as F` |
| 17–38 | `compute_gate_targets` (new) | Derives soft supervision targets from state deltas. Large delta → prefer small dt. Uses Gaussian kernel σ=1.0 around preferred dt. |
| 41–44 | `gate_loss_fn` (new) | Cross-entropy between gate logits and soft targets. |
| 72–73 | `WorldModel.__init__` | RSSM constructor now receives `max_dt` (gate_max_dt if enabled, else 1) and `dt_embed_dim` |
| 99–112 | `WorldModel.__init__` | Creates `EventGate` instance when `gate_enabled`. Registers `gate_step` buffer for curriculum tracking. |
| 123 | `WorldModel._train` | Gate step counter increment |
| 124–128 | `WorldModel._train` | Calls `subsample_variable_dt` when gate enabled |
| 134–140 | `WorldModel._train` | Passes `dt_labels` to `dynamics.observe` when available |
| 157 | `WorldModel._train` | Uses `mean_model_loss` variable to cleanly add gate loss |
| 159–196 | `WorldModel._train` | Gate loss computation: supervision from state deltas + entropy bonus (λ_H annealing 0.1→0.01) + 3-phase curriculum scaling. Stop-gradient on RSSM features. |
| 206–210 | `WorldModel._train` | Gate-specific scalar metrics (gate_loss, gate_scale, gate_entropy_bonus) |
| 279–283 | `ImagBehavior._train` | Unpacks 4 values from `_imagine` when gate enabled |
| 288–289 | `ImagBehavior._train` | Passes `dts` to `_compute_target` |
| 310–326 | `ImagBehavior._train` | Gate monitoring metrics: dt_mean, dt_std, dt_min, dt_max, per-bin fractions, empirical entropy, entropy ratio |
| 332–381 | `ImagBehavior._imagine` | Gate-enabled path: calls gate after each img_step to decide next dt. Respects curriculum (phase1 forces dt=1). Returns (feats, states, actions, dts). |
| 382–395 | `ImagBehavior._imagine` | Original path preserved when gate disabled. Returns (feats, states, actions). |
| 397–429 | `ImagBehavior._compute_target` | Added `dts` parameter. When gate enabled: uses `lambda_return_variable_dt` with γ^dt discount. Weights use cumulative adjusted discount. Falls back to standard `lambda_return` otherwise. |

## Key design decisions

1. **Backward compatibility**: All gate code guarded by `config.gate_enabled`. When false, RSSM has `max_dt=1` → no dt_embedding → `inp_dim` unchanged → identical to original.
2. **Stop-gradient**: Gate supervision uses `feat.detach()` — gate learns to read latent dynamics, not shape them.
3. **Gate step counter**: `gate_step` registered as buffer for checkpoint persistence. Incremented per `_train` call.
4. **Temperature annealing**: τ = 5.0 → 0.5 linearly over 200K steps (not 1.0).
5. **Entropy bonus annealing**: λ_H = 0.1 → 0.01, same schedule as τ.
6. **Replay sub-sampling**: Log-uniform dt distribution ensures balanced coverage across stride values.
7. **Cumulative reward**: Exact `r_cum = Σ γ^k r_{t+k}`, not the `r×Δt` approximation.
