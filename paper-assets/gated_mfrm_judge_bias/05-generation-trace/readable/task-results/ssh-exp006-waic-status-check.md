# ssh exp006 waic status check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp006_waic_status_check_20260523T013012_result.json`
- **Structured JSON:** [`27eb071332ba216a2298.json`](../../sessions/27/27eb071332ba216a2298.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

---

**exp-006: RUNNING** — k=6 进度 9/10（s0-s8 done，s9 正在 warmup 25%，~6.5min 剩余）

完成情况：
| k | sequential | joint |
|---|-----------|-------|
| 2 | 9/9 (s1-s9) | 9/9 (s1-s9) |
| 4 | 10/10 (s0-s9) | 10/10 (s0-s9) |
| 6 | 9/10 (s0-s8) | 9/10 (s0-s8) |

当前 tmux `exp006_full` 正在跑 k6_s9 的某个 model，warmup 758/3000 (25%)，5.65 it/s。sampling 阶段还要跟在后面。预计 k6_s9 全部完成还需 ~20-30min（warmup + sampling × 2 models）。

---

**WAIC/LOO-CV: DONE**

| Metric | G-MFRM | MFRM |
|--------|--------|------|
| ELPD (LOO) | -2270.0 | -2330.0 |
| ELPD (WAIC) | -2272.3 | -2327.8 |
| p_eff | 128.6 | 125.6 |
| Stacking weight | **1.0** | 0.0 |

- **ΔELPD_LOO = -60.0** (dSE = 9.4) → G-MFRM 显著优于 MFRM（差值 > 6×dSE）
- **ΔWAIC = 111.1**（MFRM 4655.6 vs G-MFRM 4544.5）
- Pareto k 诊断良好：所有 k < 0.5（max 0.28 G-MFRM, 0.36 MFRM），LOO 估计可靠
- MFRM baseline: 0 divergences, R̂ max 1.01, ESS min 265 — 收敛正常
- 已生成 `model_comparison.png/pdf` 和 `pareto_k_plot.png/pdf`

---
