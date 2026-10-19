# Adaptive Epsilon — Manual Implementation Guide

If the automated patch fails due to code structure changes, apply these 3 changes manually.

## Change 1: Add CLI argument

In the argparser section of evaluate.py, after `--conformal_threshold`:

```python
p.add_argument("--adaptive_epsilon", action="store_true", default=False,
               help="Scale CRM correction proportionally to d2/tau instead of binary gating")
```

## Change 2: Modify select_action_conformal_crm function

Add `adaptive_epsilon=False` parameter to the function signature.

Replace the binary gate:
```python
# BEFORE (binary gate):
if uncertainty > threshold:
    # apply CRM
    refined_pose = crm(base_action_pose, uf, obs_feat)
    # ... assemble action ...
else:
    # skip CRM, use raw selected action
    # ... return unrefined ...
```

With soft gate:
```python
# AFTER (adaptive epsilon):
if adaptive_epsilon or uncertainty > threshold:
    refined_pose = crm(base_action_pose, uf, obs_feat)
    if adaptive_epsilon:
        correction = refined_pose - base_action_pose
        scale = min(uncertainty / threshold, 1.0)
        refined_pose = base_action_pose + correction * scale
    # ... assemble action ...
else:
    # skip CRM, use raw selected action
    # ... return unrefined ...
```

## Change 3: Pass flag at call site

Where `select_action_conformal_crm(...)` is called in the mode dispatch, add `adaptive_epsilon=args.adaptive_epsilon`.

## Verification

```bash
# Quick smoke test — should run without errors:
python src/evaluate.py --mode adaptive_conformal_crm --adaptive_epsilon \
    --benchmark spatial --seed 42 --n_rollouts 1 --max_steps 10 \
    --conformal_threshold 0.25 --max_correction_norm 0.2
```

## Semantics

`ε_adaptive = ε_max × min(d₂ / τ, 1.0)`

| d₂ | scale | ε_effective | Behavior |
|----|-------|-------------|----------|
| 0 | 0.0 | 0 | No correction (confident) |
| τ/4 | 0.25 | ε_max/4 | Minimal correction |
| τ/2 | 0.50 | ε_max/2 | Half correction |
| τ | 1.00 | ε_max | Full correction |
| 2τ | 1.00 | ε_max | Full correction (capped) |
