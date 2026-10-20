# analysis alternative ews v2 fix

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alternative-ews-v2-fix_20260518T112442_result.json`
- **Structured JSON:** [`a0562667d11f0fbd0eb5.json`](../../sessions/a0/a0562667d11f0fbd0eb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All artifacts registered. Here are the complete results.

---

## 对比表 1: exp_001 (r=0) 完整版（含新指标）

| Metric | Type | Gen 0 | Gen 1 | Gen 2 | Gen 3 | Gen 5 | Gen 10 | Mono post-G2? | Det lag | Rel chg | s/ckpt |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **RankMe (emb)** | emb-SVD | 707.1 | 738.7 | **745.1** | 744.6 | 735.5 | 709.9 | Yes (post-G2) | 3 | 4.7% | 0.3s |
| **SLV (log_det)** | emb-Gram | 2366.7 | 2464.8 | **2469.9** | 2440.6 | 2370.2 | 2179.0 | Yes | 3 | 11.8% | ~2s |
| Token entropy | logit-pred | 6.752 | 6.750 | 6.714 | 6.670 | 6.510 | 6.106 | Yes (mono DOWN) | N/A | 9.6% | 3.2s |
| Isotropy (cos) | emb-cos | 0.319 | 0.074 | 0.065 | 0.059 | 0.064 | 0.074 | No (4 viol) | 3 | 76.8% | 0.0s |
| Stable rank (attn) | weight | 33.83 | 33.88 | 33.72 | 33.51 | 32.83 | 29.09 | Yes (mono DOWN) | N/A | 14.0% | 0.2s |
| Spectral norm (attn) | weight | 2.447 | 2.444 | 2.450 | 2.457 | 2.483 | 2.642 | Yes (mono UP) | N/A | 7.9% | 0.2s |
| PPL growth rate | ppl-diff | 0.0 | 1.83 | 2.20 | 2.67 | 4.79 | 13.46 | No (peak G9) | N/A | N/A | 0s |
| Perplexity | loss | 9.55 | 11.38 | 13.58 | 16.25 | 24.59 | 76.78 | Yes (mono UP) | N/A | 703.7% | 0s |

## 对比表 2: r=0 vs r=0.5 方向对比

| Metric | r=0 方向 | r=0 G0→G10 | r=0.5(adap) 方向 | r=0.5 G0→G10 | Signal preserved? |
|---|---|---|---|---|---|
| **RankMe** | UP→DOWN (peak G2) | +0.4% net | UP (monotonic) | +14.8% | **YES** (opposite trajectory) |
| **SLV (log_det)** | UP→DOWN (peak G2) | -7.9% | UP (monotonic) | +8.7% | **YES** (opposite trajectory) |
| Token entropy | DOWN | -9.6% | UP | +2.4% | **YES** (opposite direction) |
| Isotropy (cos) | DOWN | -76.8% | DOWN | -89.7% | NO (same direction) |
| Stable rank (attn) | DOWN | -14.0% | UP | +3.7% | **YES** (opposite direction) |
| Spectral norm (attn) | UP | +7.9% | DOWN | -1.2% | **YES** (opposite direction) |
| PPL growth rate | Accelerating (1.8→14.0) | - | Slow (0.5→0.9) | - | **YES** (rate 15x difference) |
| Perplexity | UP +703.7% | 9.6→76.8 | UP +58.1% | 9.6→15.1 | Partial (both up, magnitude differs) |

exp_004 (fixed mix r=0.5) is nearly identical to exp_006 (adaptive r=0.5) in all metrics.

---

## 必须回答的问题

**1. RankMe 在 r=0 下是否也展示 decompression-then-collapse？**

**是。** RankMe 从 Gen 0 的 707 上升到 Gen 2 的 745 (peak)，然后单调下降到 Gen 10 的 710。这与 SLV (log_det) 的 decompression-then-collapse 模式完全匹配。**SLV 的独特性被削弱**：RankMe 作为更简单的 embedding-level 指标展现了相同的非单调轨迹。不过 SLV 的相对变化幅度更大 (11.8% vs 4.7%)，信噪比更高。

**2. RankMe 在 r=0.5 下方向如何？**

**单调上升**：706 → 811 (+14.8%)。没有任何 collapse 迹象。与 r=0 形成完美对比。

**3. Token entropy 在 r=0.5 下方向如何？**

**单调上升**：6.752 → 6.912 (+2.4%)。方向与 r=0 完全相反（r=0 为 6.752 → 6.106, -9.6%）。

**4. PPL growth rate 是否 monotonic？**

**r=0**: 几乎单调递增 (0 → 1.83 → 2.20 → 2.67 → 3.56 → 4.79 → 6.32 → 7.97 → 10.40 → 14.03)，但 Gen 10 (13.46) 略低于 Gen 9 (14.03)，有一个 violation。总体呈加速模式。
**r=0.5**: 非单调 (0 → 0.54 → 0.33 → 0.34 → 0.38 → 0.51 → 0.50 → 0.58 → 0.67 → 0.76 → 0.94)，Gen 1→2 有明显下降，但整体缓慢增长，且绝对值比 r=0 小 15 倍。

---

**结论**: RankMe 确实复现了 SLV 的 decompression-then-collapse，但 SLV 信噪比更高 (11.8% vs 4.7%)。论文中可以定位为：RankMe 提供独立验证，但 SLV 的 Gram matrix log-determinant 放大了同一信号。

---
