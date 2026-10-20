# analysis image mean rsa rise ci

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_image_mean_rsa_rise_ci_20260517T192104_result.json`
- **Structured JSON:** [`b4ea23fe8edefaf5d7bb.json`](../../sessions/b4/b4ea23fe8edefaf5d7bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
=== Image Mean RSA Rise Phase Bootstrap CI ===

Trained image_mean:
  L0:  ρ = 0.6118, L12: ρ = 0.6282
  Δρ = 0.0165, 95% CI [-0.0002, 0.0346], p = 0.0528

Untrained image_mean:
  L0:  ρ = 0.6118, L12: ρ = 0.5496
  Δρ = -0.0622, 95% CI [-0.0830, -0.0403], p < 0.0001

Trained vs Untrained rise difference:
  Trained rise:   +0.0165
  Untrained rise: -0.0622
  Difference:     +0.0787, 95% CI [0.0593, 0.0986], p < 0.0001
```

关键发现：

1. **Trained image_mean rise** 本身是边际显著（p=0.0528），CI 下界几乎触及 0。单独看 Δρ=+0.016 确实不算强。

2. **Untrained image_mean 显著下降**（Δρ=−0.062, p<0.0001），这是更重要的对比。

3. **Trained vs Untrained 差异高度显著**（Δ=+0.079, CI [0.059, 0.099], p<0.0001）。训练使 image_mean RSA 从"显著下降"变为"持平/微升"，这个效果是稳健的。

回应 N2 的策略：不应强调 trained 的绝对升幅（确实小），而应 frame 为"训练阻止了 untrained 中观察到的显著下降，两者差异 Δ=0.079 高度显著"。与 last_preaction 的大幅上升（Δρ=+0.074）形成互补——训练对不同 readout 的影响模式不同：last_preaction 上大幅增强 action-relevant coding，image_mean 上则是维持/保护了 visual representation 不被 deeper layers 破坏。

---
