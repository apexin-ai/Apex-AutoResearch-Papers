# analysis exp004 cross model and permutation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004_cross_model_and_permutation_20260521T213143_result.json`
- **Structured JSON:** [`36f7da7abc12dab9b1d5.json`](../../sessions/36/36f7da7abc12dab9b1d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 数据概况
- 8 models 总计，但仅 **6 个模型** 覆盖全部 5 benchmarks（OLMo-2-7B / Yi-1.5-9B 仅在 GSM8K/MATH）
- B1/B2 用 6 common models 做 balanced comparison，B3/B4 同时报告 6-model balanced 和 full 两版

---

### B1: Permutation Test (6 common models × 5 benchmarks)

| Benchmark | item_id% | model:item% |
|-----------|----------|-------------|
| mmlu | 40.48 | 31.60 |
| arc | 42.46 | 38.05 |
| hellaswag | 32.20 | 37.14 |
| gsm8k | 14.58 | 13.48 |
| math | 20.49 | 17.69 |

- **item_id% decreasing**: ρ = 0.80, **p = 0.067** (n.s. at 0.05, marginal)
- **model:item% increasing**: ρ = −0.60, **p = 0.883** (n.s., **wrong direction**)

MC vs FF 二分明显（MC 组 32-42% vs FF 组 15-20%），但组内排序非单调（arc > mmlu; math > gsm8k），导致不显著。

---

### B2: LOBO Stability
- **0/5** drops preserve both monotonic gradients
- item_id 方向一致（所有 drops rho > 0），但都不显著（p ≥ 0.167）
- model:item 方向**一致反转**（rho < 0 in all drops）

---

### B3: D-study (6 models balanced)

| Benchmark | G_current | min(≥.80) | min(≥.90) | min(≥.95) |
|-----------|-----------|-----------|-----------|-----------|
| mmlu | 0.8705 | 119 | 268 | 566 |
| arc | 0.8623 | 128 | 288 | 607 |
| hellaswag | 0.8240 | 171 | 385 | 812 |
| gsm8k | 0.8111 | 187 | 420 | 885 |
| math | 0.8324 | 162 | 363 | 765 |

With full data (8 models for GSM8K/MATH): gsm8k G→0.863, math G→0.892（更多 model 增加 model:item 从而提高 G）

---

### B4: Cross-model G-study

**MMLU 6-model vs 4-model**:
| Metric | 6-model | 4-model | Δ |
|--------|---------|---------|---|
| item_id% | 40.48 | 41.55 | −1.07 |
| model:item% | 31.60 | 32.81 | −1.21 |
| model% | 3.05 | 0.75 | +2.30 |
| G_item | 0.8705 | 0.8159 | +0.055 |

添加 2 个 model 后 model 主效应大幅增加（0.75%→3.05%），item_id%/model:item% 略降，G_item 提升 0.055。

---

### 输出文件
```
results/exp004_8model_analysis/
  permutation_test_5bm.json
  lobo_stability.json
  dstudy_8model.json
  cross_model_gstudy_8model.json
```

**核心发现**：MC vs FF 的 format dichotomy 在 item_id% 上清晰（40% vs 17%），但 model:item% 不是假设的递增方向——MC 组反而更高。这意味着 model:item 交互更多受 format/item-type 复杂度驱动，而非简单的 "reasoning 越多 interaction 越大" 叙事。论文可以改 framing 为 "format-conditional variance structure" 而非 "monotonic gradient"。

---
