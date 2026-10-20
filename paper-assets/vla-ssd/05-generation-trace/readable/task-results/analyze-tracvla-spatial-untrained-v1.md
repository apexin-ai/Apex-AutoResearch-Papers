# analyze tracvla spatial untrained v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_tracvla_spatial_untrained_v1_20260521T160910_result.json`
- **Structured JSON:** [`4a3776f82479aa187c04.json`](../../sessions/4a/4a3776f82479aa187c04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已获取。没有 RSA 或 counterfactual 结果（Phase 5 被跳过）。下面汇总。

## Metrics Summary

### Phase 2: R² Probing (Ridge, all 32 layers)

| Layer | Trained img_mean | Untrained img_mean | Trained last_pre | Untrained last_pre |
|-------|-----|------|------|------|
| L0 | 0.8059 | 0.7761 | 0.6656 | 0.5911 |
| L4 | 0.8091 | 0.7812 | 0.7954 | 0.7132 |
| L8 | 0.8134 | 0.7892 | 0.7908 | 0.6942 |
| L12 | 0.8231 | 0.7806 | 0.7980 | 0.7195 |
| L16 | 0.8311 | 0.7961 | 0.8035 | 0.7207 |
| **L17** | **0.8317** | 0.7919 | **0.8090** (peak) | 0.7156 |
| **L19** | **0.8347** (peak) | 0.7901 | 0.8051 | 0.7178 |
| L24 | 0.8169 | 0.7694 | 0.7463 | 0.7116 |
| L28 | 0.8223 | 0.7714 | **0.6150** | 0.7036 |
| L29 | 0.8136 | 0.7731 | **0.5040** | 0.7037 |
| L30 | 0.7970 | 0.7696 | **0.4472** | 0.6969 |
| **L31** | 0.7907 | 0.7589 | **0.6712** | **0.7065** |

### Phase 3: L1 Attention Profile

| Metric | Trained | Untrained |
|--------|---------|-----------|
| Instruction-dominant heads | 30/32 | 32/32 |
| Image-dominant heads | 2/32 | 0/32 |

### Phase 4: Cross-instruction Classification

| Layer | Trained img | Untrained img | Trained last_pre | Untrained last_pre |
|-------|-------------|---------------|-------------------|---------------------|
| L0 | 1.000 | 1.000 | 0.923 | 0.977 |
| L1+ | 1.000 | 1.000 | 1.000 | 1.000 |

### Phase 5: Counterfactual
- Trained: empty d=1.3268, shuffled d=1.2947
- Untrained: **skipped** (untrained model cannot generate meaningful actions)

---

## Trained vs Untrained Comparison

### 1. R² Collapse — **Training-induced (CONFIRMED)**

The defining finding. Trained last_preaction shows dramatic late-layer collapse; untrained is flat:

| Metric | Trained | Untrained |
|--------|---------|-----------|
| last_pre peak | 0.8090 (L17) | 0.7224 (L18) |
| last_pre @ L30 (nadir) | **0.4472** | 0.6969 |
| last_pre @ L31 (exit) | 0.6712 | 0.7065 |
| Peak→L30 drop | **-0.3618** | **-0.0255** |
| img_mean @ L31 | 0.7907 | 0.7589 |
| L31 gap (img - last_pre) | **0.1195** | 0.0524 |
| L30 gap (img - last_pre) | **0.3498** | 0.0727 |

Trained model develops a massive **routing divergence**: image tokens maintain R² while last_preaction collapses in layers 26–30, then partially recovers at L31. Untrained model has no such pattern — both modalities decline gently and in parallel.

### 2. L1 Instruction Dominance — **Pre-existing architectural property (NOT training-induced)**

Untrained: 32/32 instruction-dominant. Trained: 30/32. Training actually *reduces* instruction dominance slightly (introduces 2 image-dominant heads). This is an architectural bias of Phi-3-Vision, not an emergent training effect.

### 3. Cross-instruction Classification — **Pre-existing (NOT training-induced)**

Both conditions achieve near-perfect classification (1.0) at all layers. Task-discriminative representations exist in the pretrained model already.

### 4. Counterfactual — **No comparison possible**

Skipped for untrained (no meaningful action generation without fine-tuning).

---

## Conclusion

**success** — Hypothesis partially confirmed with one important nuance.

The core claim holds: the **R² collapse pattern is training-induced**. The trained model develops a dramatic routing divergence where last_preaction R² collapses by 0.36 (L17→L30) while image_mean stays elevated, creating a late-layer gap of up to 0.35. The untrained model shows no such pattern — both modalities follow a flat, parallel trajectory (max drop 0.026). This is the strongest evidence that VLA fine-tuning creates specialized information routing.

However, **L1 instruction dominance is NOT training-induced** — it's a pre-existing architectural property of Phi-3-Vision (32/32 untrained vs 30/32 trained). Similarly, cross-instruction classification is pre-existing. These should not be cited as training-induced effects.

The counterfactual comparison is unavailable (untrained cannot generate actions), but the R² probing contrast alone is decisive for the routing hypothesis.

---
