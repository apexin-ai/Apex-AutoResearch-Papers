# exp_008e Code Readiness Check: gate_dt_embed_dim=0

**Date**: 2026-05-14  
**Ready for dryrun**: True (with caveat)

## Parameter Definition

| Location | Line | Content |
|----------|------|---------|
| `configs.yaml` | 102 | `gate_dt_embed_dim: 32` (default) |
| `models.py` | 94 | `dt_embed_dim=config.gate_dt_embed_dim` (passed to RSSM) |
| `networks.py` | 36 | RSSM constructor parameter `dt_embed_dim=32` |
| `networks.py` | 55-68 | Embedding creation and inp_dim calculation |

Command-line override `--gate_dt_embed_dim 0` works correctly: `dreamer.py` uses `tools.args_type(32)` → `int` type → `int("0") = 0`.

## dim=0 Processing Logic Analysis

### RSSM.__init__ (networks.py:55-68)

```python
self._dt_embed_dim = dt_embed_dim  # = 0
if self._max_dt > 1:  # True (gate_max_dt=8 when gate_enabled)
    self._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)  # nn.Embedding(8, 0)
    nn.init.normal_(self._dt_embedding.weight, std=0.01)  # no-op (empty tensor)
# ...
if self._dt_embedding is not None:  # True — object exists
    inp_dim += dt_embed_dim  # inp_dim += 0 → no change
```

### img_step (networks.py:249-257)

```python
if self._dt_embedding is not None:  # True
    dt_emb = self._dt_embedding(dt - 1)  # shape (batch, 0)
    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)  # cat with 0-dim = no-op
```

### Imagination path (models.py:619)

```python
succ = dynamics.img_step(state, action, dt=prev_dt)  # dt passed but embedding contributes nothing
```

## Correctness Analysis

1. **nn.Embedding(n, 0)** — valid in PyTorch 2.x. Creates weight of shape (n, 0). Forward returns (*, 0).
2. **nn.init.normal_ on (n, 0)** — no-op, no elements to initialize.
3. **torch.cat with (batch, 0) tensor** — effectively no-op, output size unchanged.
4. **Linear layer input dim** — `stoch*discrete + num_actions + 0` matches exactly.
5. **Imagination loop** — dt values are still computed by EventGate, passed to img_step, but embedding lookup produces nothing. No crash path.

## Conclusion

The code handles `gate_dt_embed_dim=0` correctly through PyTorch's native support for 0-sized tensor dimensions. The dt_embedding object is created but contributes zero information — functionally equivalent to removing it entirely.

**No code modification required.** Ready for dryrun.

### Minor Suggestion (non-blocking)

For readability, an explicit guard `if self._max_dt > 1 and dt_embed_dim > 0:` would make the intent clearer. But this is cosmetic — current code is functionally correct.
