# code implement tcn rave

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_implement-tcn-rave_20260520T024538_result.json`
- **Structured JSON:** [`af7fdfb5dec5bae6bbcf.json`](../../sessions/af/af7fdfb5dec5bae6bbcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 实现 Diff

### configs.yaml (line 129-131)
```yaml
  # CIVO intervention methods
  tcn_sigma: 0.0
  rave_ceiling: 0.0
```

### networks.py — TCN (img_step, line 241/256-258)
```python
def img_step(self, prev_state, prev_action, dt=None, sample=True, tcn_sigma=0.0):
    ...
    dt_emb = self._dt_embedding(dt - 1)
    # TCN: temporal conditioning noise on dt embedding during imagination
    if tcn_sigma > 0:
        dt_emb = dt_emb + tcn_sigma * dt_emb.detach().std() * torch.randn_like(dt_emb)
```

### models.py — TCN wiring (_imagine, line 691)
```python
succ = dynamics.img_step(state, action, dt=prev_dt, tcn_sigma=getattr(config, "tcn_sigma", 0.0))
```

### models.py — RAVE (_compute_target, line 745-751)
```python
# RAVE: cap imagination values relative to real-state EMA anchor
if getattr(self._config, 'rave_ceiling', 0) > 0:
    if not hasattr(self, '_rave_anchor'):
        self._rave_anchor = value[0].mean().detach()
    else:
        self._rave_anchor = 0.99 * self._rave_anchor + 0.01 * value[0].mean().detach()
    ceiling = self._rave_anchor * self._config.rave_ceiling
    value = torch.min(value, ceiling)
```

## Dry-run 结果
- **TCN** (tcn_sigma=0.5): 通过，100 pretrain steps 完成，无报错
- **RAVE** (rave_ceiling=2.0): 通过，100 pretrain steps 完成，无报错

## 实验提交
| 实验 | GPU | PID | tmux session |
|------|-----|-----|-------------|
| exp_027_tcn_walker_s0 | cuda:0 | 879355 | exp_027_tcn_walker_s0 |
| exp_028_rave_walker_s0 | cuda:1 | 879636 | exp_028_rave_walker_s0 |

---
