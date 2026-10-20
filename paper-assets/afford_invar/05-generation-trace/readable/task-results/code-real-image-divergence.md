# code real image divergence

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_real-image-divergence_20260519T201328_result.json`
- **Structured JSON:** [`62e0d336bc591716347e.json`](../../sessions/62/62e0d336bc591716347e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果如下：

## Layer-18 Divergence 结果（20 tasks, 100 pairs）

| 指标 | Mean | Std | Min | Max |
|------|------|-----|-----|-----|
| **Attention KL (真实图片)** | 0.000191 | 0.000086 | 0.000064 | 0.000468 |
| **Attention KL (dummy 图片)** | 0.000070 | 0.000026 | 0.000027 | 0.000151 |
| **Cosine dist (all tokens)** | 0.027682 | 0.009644 | 0.008112 | 0.050834 |
| **Cosine dist (image tokens only)** | 0.000035 | 0.000014 | 0.000000 | 0.000048 |
| **L2 dist (normalized)** | 2.026012 | 0.853548 | 0.144562 | 2.641152 |
| **Per-position variance** | 280.820155 | 57.237740 | 146.755219 | 372.425964 |

### 关键发现

1. **Attention KL — 真实图片 vs dummy**: 真实图片 KL mean=1.91e-4，dummy mean=7.0e-5。真实图片下 KL 约为 dummy 的 **2.7x**，说明图文交互下 paraphrase 对 attention 的影响确实更大，但绝对值仍然很小。

2. **Cosine distance — all tokens vs image tokens**: all tokens cosine dist mean=0.0277 (sim≈0.972), 说明文本 token 的 hidden state 有明显差异。但 **image tokens cosine dist 接近 0** (mean=3.5e-5, sim≈0.99997)，意味着 paraphrase 几乎不影响 image token 的 layer-18 表征。

3. **L2 dist (normalized)** mean=2.03，表面看不小，但这包含了 text token 的差异。

4. **Per-position variance** mean=280.8，主要来自 text token 位置的方差。

结果保存在 `/root/afford_invar/results/phase0/real_image_divergence.json`。

---
