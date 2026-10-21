# STORM DMC Walker Walk Adaptation

Adapts STORM (NeurIPS 2023, Atari-only) to DMC Walker Walk proprioceptive control.
This is the Phase 1 baseline — no dt-conditioning (that's Phase 2).

## Changed Files

| File | Purpose | Key changes |
|------|---------|-------------|
| `envs/dmc_env.py` | **NEW** — DMC gymnasium wrapper | 24-dim proprioceptive obs, 6-dim continuous action, compatible with gymnasium vectorization |
| `sub_models/mlp_encoder.py` | **NEW** — MLP encoder/decoder | Replaces CNN EncoderBN/DecoderBN; 24→256→256 encoder, 1024→256→24 decoder |
| `sub_models/transformer_model.py` | **MODIFIED** — Continuous action transformer | Removed `F.one_hot()` discrete encoding; continuous action vectors concatenated directly with latent |
| `sub_models/world_models.py` | **MODIFIED** — WorldModel for DMC | MLP encoder/decoder, VectorMSELoss instead of image MSE, 3D action buffer for imagination |
| `agents.py` | **MODIFIED** — Continuous actor-critic | TanhGaussian actor (mean+log_std), tanh-corrected log_prob, Gaussian entropy |
| `replay_buffer.py` | **MODIFIED** — Continuous obs/action buffer | float32 obs (not uint8), 3D action buffer `(T, num_envs, action_dim)`, no /255 or rearrange |
| `config/dmc_walker.yaml` | **NEW** — DMC Walker Walk config | 500K steps, gamma=0.997, WM lr=3e-4, agent lr=3e-5 |
| `train_dmc.py` | **MODIFIED** — Training entry point | DMC env build, continuous obs/action handling, extended yacs config loader |

## Unchanged Files (use from original STORM repo)

- `sub_models/functions_losses.py` — SymLogTwoHotLoss, symlog/symexp
- `sub_models/attention_blocks.py` — MultiHeadAttention, PositionalEncoding1D, masks
- `utils.py` — seed, Logger, EMAScalar

## Dimension Chain

```
Env → obs (24,)
      ↓
MLPEncoder → (B, L, 256)
      ↓
DistHead.post → (B, L, 32, 32) categorical logits
      ↓ straight-through sample + flatten
Stochastic latent → (B, L, 1024)
      ↓                              ↓
MLPDecoder → (B, L, 24) obs_hat    Transformer stem: cat(1024, 6) → 512
                                          ↓
                                    Transformer → dist_feat (B, L, 512)
                                          ↓                ↓
                                    DistHead.prior    RewardDecoder → scalar
                                          ↓                ↓
                                    Prior latent     TerminationDecoder → bool
                                     (B, L, 1024)

Agent input: cat(latent, dist_feat) = (B, L, 1536)
      ↓                    ↓
Actor body → mean (B,L,6) + log_std (B,L,6) → tanh(Normal.sample) → action (B,L,6)
Critic → (B,L,255) two-hot → symexp decode → scalar value
```

## Diff Summary vs Original STORM

### Observation pipeline
- **Before**: 64×64 RGB image → CNN (stride-2 conv ×4) → 4096-dim flat feature → DistHead
- **After**: 24-dim vector → MLP (24→256→256→256) → 256-dim embedding → DistHead
- DistHead post_head input changes from 4096 to 256; prior_head unchanged (512→1024)

### Action pipeline
- **Before**: Discrete index → `F.one_hot(action, N)` → concat with latent → transformer stem
- **After**: Continuous 6-dim vector → directly concat with latent → transformer stem
- Stem input: `stoch_dim + action_dim` = 1024+6=1030 (was 1024+18 for Atari)

### Actor
- **Before**: MLP → logits (N,) → Categorical → sample index
- **After**: MLP → mean (6,) + log_std (6,) → Normal → tanh → action ∈ [-1,1]
- Log-prob: Gaussian log_prob + tanh squashing correction
- Entropy: Gaussian entropy (approximation, ignoring tanh)

### Replay buffer
- **Before**: obs as uint8 `(T, envs, H, W, C)`, action as float `(T, envs)` scalar
- **After**: obs as float32 `(T, envs, 24)`, action as float32 `(T, envs, 6)`
- No /255 normalization, no `rearrange("B T H W C -> B T C H W")`

### Reconstruction loss
- **Before**: `MSELoss` reducing over `(C, H, W)` → per-frame scalar
- **After**: `VectorMSELoss` reducing over obs_dim → per-step scalar

## Post-Review Fixes (2026-05-29)

### Fix 1: terminated/truncated separation (dmc_env.py + train_dmc.py)
DMC Walker Walk has a 1000-step time limit. Original code treated all `time_step.last()` as `terminated=True`, which zeroed bootstrap values at truncation boundaries — systematically underestimating values.
- `dmc_env.py`: `terminated` now checks `discount == 0.0` (true task failure); `truncated` is time-limit only
- `train_dmc.py`: replay buffer stores `terminated` (not `done`), so `calc_lambda_return` correctly bootstraps at truncation

### Fix 2: Deterministic evaluation loop (train_dmc.py)
- `evaluate()` function: greedy policy (mean action, no sampling noise), 10 episodes per eval
- Runs every 10K env steps, prints `[Eval @ N] return = X ± Y` for comparison with DreamerV3 baseline (915.7)
- Final eval after training completes

### Fix 3: wandb integration (train_dmc.py)
- Optional wandb logging (`--no-wandb` to disable)
- Logs `train/episode_return`, `eval/return_mean`, `eval/return_std` with `env_steps` as x-axis
- Project name: `storm-dmc-civo`

## Execution Steps (on GPU server)

```bash
# 1. Clone STORM and overlay DMC files
cd /root/autodl-tmp
git clone https://github.com/weipu-zhang/STORM storm_dmc
cp -r <artifacts/storm_dmc>/* storm_dmc/

# 2. Install dependencies
source /etc/network_turbo  # AutoDL proxy
pip install dm-control gymnasium[mujoco] mujoco \
    torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install einops tensorboardX yacs colorama tqdm wandb

# 3. Verify environment
python -c "
from envs.dmc_env import DMCWalkerWalkEnv
env = DMCWalkerWalkEnv()
obs, _ = env.reset()
print(f'obs_dim={obs.shape[0]}, action_dim={env.action_space.shape[0]}')
action = env.action_space.sample()
obs2, r, d, t, info = env.step(action)
print(f'step ok: obs={obs2.shape}, reward={r:.3f}, done={d}')
"

# 4. Train baseline (dt=1)
cd storm_dmc
python train_dmc.py -n walker_walk_baseline -seed 0 \
    -config_path config/dmc_walker.yaml

# 5. Monitor
tensorboard --logdir runs/
```

## GPU-Hours Estimate

| Setting | Estimate | Notes |
|---------|----------|-------|
| Walker Walk 500K steps, single A100 | ~5-8h | STORM transformer imagination is sequential (slower than RSSM) |
| Walker Walk 500K steps, single A6000 | ~8-12h | ~60% A100 speed |
| Walker Walk 500K steps, single RTX 4090 | ~6-10h | Good FP16 throughput |

Reference: DreamerV3 does Walker Walk 500K in ~3h on A100. STORM's autoregressive imagination adds ~2-3× overhead.

## Python Dependencies

```
torch >= 2.0
dm-control >= 1.0.14
mujoco >= 3.0
gymnasium >= 0.29
einops
tensorboardX
yacs
colorama
tqdm
wandb
numpy
```
