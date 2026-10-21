# verify figure2 caption

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_figure2_caption_20260523T201508_result.json`
- **Structured JSON:** [`ce847d3102b80f120cbc.json`](../../sessions/ce/ce847d3102b80f120cbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed. Here's the analysis:

---

## 问题1: ESS-only b* "3.5--5.9" 范围

**实际数据：**
- ESS-only seed123: mean b = 3.552 (n=28,362 batches)
- ESS-only seed456: mean b = 3.541 (n=25,992 batches)
- ESS-only seed42 (report): b_star_mean = 3.506
- 所有 seed 的 overall mean 都在 3.50–3.55 范围内，**没有任何 seed 给出 mean ≈ 5.9**

**"5.9" 来源：** `artifacts/mechanism_decomposition_stats.json` 第 39 行：
```json
"ess_only_bstar_approx_upper": 5.88
```
这是一个**反事实计算**——对 adaptive 运行中 α_eff-binding batches 的 q-score 分布，如果用 ESS-only solver 求解，得到的 b* ≈ 5.88。与 `adaptive_bstar_mean: 1.19` 的比值 = 4.9×（文件中标记为 `overweight_ratio`）。

**Caption 的问题：**
- "3.5" = ESS-only 整体训练 mean b* ✓
- "5.9" = ESS-only solver 在特定 batch 子集上的反事实 b*，不是实际训练 mean
- "mean 3.5--5.9 across batches" 混合了两个不同计算的结果，读者会理解为 ESS-only mean b* 跨 batch 变化范围是 3.5–5.9，但实际上两个 endpoint 来自不同的量
- 另外，图上箭头从 x=3.5 到 x=5.5（`generate_paper_figures.py` line 64），与 caption 的 "5.9" 也不一致

**建议：** Caption 改为 "ESS-only $b^*$ (overall mean $\approx 3.5$)" 更准确。如果要保留范围表述，应明确说明含义，例如 "ESS-only $b^*$ (per-batch mean 3.5, with $>$42\% of batches exceeding $b=2$)"。

---

## 问题2: "5.8×" 比率

**来源：** Introduction line 22:
> "An α_eff quality constraint binds in 50.9% of batches at 5.8× lower sharpening exponents than an ESS-only alternative"

**计算验证（tau07 runs, τ=0.7）：**

| Seed | α_eff-binding % | α_eff-binding mean b | ESS-only mean / α_eff mean |
|------|-----------------|---------------------|---------------------------|
| 42   | 49.7%           | 0.597               | 5.95×                     |
| 123  | 50.8%           | 0.609               | 5.83×                     |
| 456  | 49.6%           | 0.605               | 5.87×                     |
| **Mean** | **50.0%**    | **0.604**           | **5.88×**                 |

ESS-only mean b = 3.552, α_eff-binding conditional mean b ≈ 0.604 → ratio ≈ 5.9×

**结论：** "5.8×" **近似正确**（实际 5.9×，四舍五入）。但注意：
1. 论文写 "50.9%"，实际数据 seed42 给出 49.7%（seed123 = 50.8% 更接近）。论文引用 "seed 42" 但数字更像 seed 123。
2. Regime 分类结果对阈值定义敏感（clean/aeff/ess 边界），可能使用了稍不同的分类逻辑得到 50.9/43.3/5.8%。

---
