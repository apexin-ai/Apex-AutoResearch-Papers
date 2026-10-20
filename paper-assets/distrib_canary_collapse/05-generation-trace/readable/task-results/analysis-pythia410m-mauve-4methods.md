# analysis pythia410m mauve 4methods

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pythia410m_mauve_4methods_20260517T124235_result.json`
- **Structured JSON:** [`58c69358a76a232ca0fe.json`](../../sessions/58/58c69358a76a232ca0fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。整理如下：

---

## Mauve Supplement — 2 pairs × 4 methods

| Pair | Naive XCorr | Diff XCorr (FDR) | Threshold | TY Granger |
|------|-------------|------------------|-----------|------------|
| entropy→mauve | not sig (r=0.86, p=0.006, **lag=-3**) | not sig (p_adj=0.29) | not sig (canary onset=None) | not sig (F=1.18, p=0.47, d_max=2) |
| ece→mauve | **SIG** (r=0.86, p=0.007, lag=+3) | not sig (p_adj=0.29) | not sig (lead=-2) | not sig (F=0.08, p=0.83, d_max=2) |

**Per-method mauve sig count:** Naive 1/2, Diff 0/2, Threshold 0/2, TY 0/2

---

## Final Table 5 — Pythia-410M (8 pairs)

| Method | Sig Count |
|--------|-----------|
| Naive XCorr | 7/8 |
| Diff XCorr (FDR) | 6/8 |
| Threshold Onset | 6/8 |
| PermG forward | 6/8 |
| PermG reverse | 0/8 |
| TY Granger | 6/8 |
| Consensus ≥3 | 6/8 |
| Consensus ≥4 | 6/8 |

---

**解读：**

Mauve 漂移仅 ~10%（0.034→0.031），几乎是 flat noise。两个 mauve pair 基本不显著，符合预期：
- entropy→mauve 的 Naive XCorr 虽然 r=0.86 / p=0.006，但 peak lag = **-3**（mauve 反而领先 entropy），不满足因果方向条件，判定 not sig
- ece→mauve 的 Naive XCorr lag=+3 且 p<0.05，判定 sig（唯一一个）
- Threshold 失败因为 entropy 的 oriented series 没超过 3σ threshold（它本身是 decreasing 且初始方差大），mauve 也没有明显 onset
- TY 在 T=11, d_max=2 下 df_resid 很小，power 不足

结果已保存至 `results/generalize/pythia410m_wiki_a100_s42/analysis/mauve_supplement_4method.json`。

---
