# ops verify audit and exp020 metrics

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-audit-and-exp020-metrics_20260523T220148_result.json`
- **Structured JSON:** [`d7caa9133855bfb26a52.json`](../../sessions/d7/d7caa9133855bfb26a52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected and verified. Here are the results:

---

## 任务 A：数据审计验证

### A1: r=0.25 SLV dip = −2.1

原始 log_det (SLV) 值 (Gen 0 → Gen 1):
| Seed | Gen 0 | Gen 1 | Gen 2 |
|------|-------|-------|-------|
| 42 (exp_004) | 2366.683 | 2362.135 | 2363.102 |
| 43 (exp_012) | 2366.683 | 2365.352 | 2362.542 |
| 44 (exp_016) | 2366.683 | 2366.125 | 2364.587 |

3-seed mean:
- Gen 0: 2366.683
- Gen 1: (2362.135 + 2365.352 + 2366.125) / 3 = **2364.537**
- Gen 2: (2363.102 + 2362.542 + 2364.587) / 3 = **2363.410**

Mean trajectory deltas:
- Δ₁ = 2364.537 − 2366.683 = **−2.146**
- Δ₂ = 2363.410 − 2364.537 = −1.127

Max dip = −2.146 ≈ **−2.1** → **MATCH** ✅

### A2: r=0.3 SLV dip = −1.5

原始 log_det 值:
| Seed | Gen 0 | Gen 1 |
|------|-------|-------|
| 42 (exp_006) | 2366.683 | 2366.134 |
| 43 (exp_009) | 2366.683 | 2363.895 |
| 44 (exp_015) | 2366.683 | 2365.486 |

3-seed mean Gen 1: (2366.134 + 2363.895 + 2365.486) / 3 = **2365.172**

Δ₁ = 2365.172 − 2366.683 = **−1.511** ≈ **−1.5** → **MATCH** ✅

### A3: Signal ratio ~3.5×

Table 2 (paper line 160-161):
- r=0.2: max Δₜ = 0.0017
- r=0.25: max Δₜ = 0.0005

0.0017 / 0.0005 = **3.4**

论文写 ~3.5×。精确值 3.4，~ 前缀表示近似值，在 3% 误差范围内。 → **MATCH (within ~ approximation)** ✅

### A4: Figure 1 caption "SLV falls 12% from peak"

原始 log_det (r=0, pure collapse):
| Seed | Gen 2 (peak) | Gen 10 (final) |
|------|-------------|---------------|
| 42 (exp_001/phase0) | 2469.928 | 2178.949 |
| 43 (exp_010) | 2466.626 | 2210.766 |
| 44 (exp_013) | 2467.384 | 2154.336 |

3-seed mean:
- Peak (Gen 2): **2467.979**
- Final (Gen 10): **2181.350**

(2467.979 − 2181.350) / 2467.979 × 100% = **11.61%** → 四舍五入 **12%** → **MATCH** ✅

---

## 任务 B：exp_020 Gen 0-3 metrics

JSON 已保存至:
`artifacts/exp_020/gen0_3_metrics.json`

数据来自 `phase1_gpt2m_pure_collapse_seed42_results.json`，使用 `slv`/`ppl`/`r_eff` 字段命名。Gen 2 SLV peak (924.39) 与 Gen 3 reversal (889.70) 确认。

---
