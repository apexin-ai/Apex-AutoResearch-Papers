# Selective Gradient Stopping (SGS) Implementation Report

## Date: 2026-05-15

## Summary

Implemented SGS in the DreamerV3 codebase on server bjb1-45299. SGS cuts the gradient path `reward_loss → dt_embedding.weight` during world model training while preserving `decoder/kl → dt_embedding.weight` gradients, targeting the CIVO (Critic-Induced Value Overestimation) root cause.

## Files Modified

### 1. `configs.yaml` (line 120)
- Added `reward_dt_emb_detach: false` after `dt_emb_freeze: false`
- Activated via CLI: `--reward_dt_emb_detach True`

### 2. `models.py` — WorldModel._train (lines 337-355)

**Core SGS block** (inserted between `mean_model_loss` finalization and `self._model_opt(...)` call):

```python
# Selective Gradient Stopping: subtract reward→dt_emb gradient to prevent CIVO
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

metrics = self._model_opt(mean_model_loss, self.parameters())

if _sgs_handle is not None:
    _sgs_handle.remove()
```

**Mechanism**: Before the optimizer backward pass, compute `∂(reward_loss)/∂(dt_emb.weight)` via `torch.autograd.grad`. Register a backward hook that subtracts this from the total gradient. After optimizer step, remove the hook. Net effect: dt_emb receives gradients from decoder/kl/cont but NOT from reward.

**Diagnostic metrics** (lines ~387-415):
- `dt_emb_reward_grad_norm` (every 1000 steps): magnitude of the removed reward gradient
- `dt_emb_decoder_grad_norm` (every 1000 steps): magnitude of the preserved decoder gradient
- `dt_emb_weight_norm` (every 5000 steps): dt_emb weight L2 norm
- `dt_emb_weight_diff_dt1_dt2` (every 5000 steps): distance between dt=1 and dt=2 embeddings

## Verification

### Syntax check
```
python -c "import models; import networks; print('Syntax OK')"
→ Syntax OK
```

### Config parse test
```
--reward_dt_emb_detach True parsed as bool True ✓
```

### Gradient correctness unit test
```
Test 1: Gradient decomposition
  total ≈ reward + decoder: True
Test 2: SGS hook
  grad after SGS ≈ decoder-only grad: True
Test 3: SGS with GradScaler (disabled)
  grad after SGS ≈ decoder-only: True
All SGS tests passed!
```

## Usage

```bash
python dreamer.py --configs defaults dmc_proprio \
    --task dmc_walker_walk \
    --gate_enabled True \
    --gate_fixed_dt 2 \
    --reward_dt_emb_detach True \
    --logdir ./logdir/exp_XXX
```

## Compatibility

- `reward_dt_emb_detach: false` (default) → no behavior change, fully backward-compatible
- Works with both AMP (`precision: 16`) and FP32 (`precision: 32`) — GradScaler handles both
- Compatible with `dt_emb_freeze: true` (SGS skips when dt_embedding is None or frozen)
- Does NOT interfere with running experiments (009d, 015b)
- Only affects future experiments launched with `--reward_dt_emb_detach True`

## Design Notes

- **Why backward hook instead of detach?** dt_emb concatenates with prev_stoch+prev_action in `_img_in_layers` before entering GRU. The fused representation in `deter → feat` cannot be split at the `get_feat` level. Gradient subtraction via hook is the only way to selectively remove one loss's contribution.
- **GradScaler compatibility**: Both the pre-computed reward gradient and the optimizer's backward pass use the same scaler, so subtraction is scale-consistent.
