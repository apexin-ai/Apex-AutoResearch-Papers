# code plan001 step4 5 regression sim

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-step4-5-regression-sim_20260522T075710_result.json`
- **Structured JSON:** [`e17fc126011d5cf2f131.json`](../../sessions/e1/e17fc126011d5cf2f131.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已部署到服务器并通过验证：

- `/root/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py` — 455 panels × 12 conditions 全套回归（OLS + VIF + partial corr + residualized K_eff + Bonferroni/FDR + beta regression）
- `/root/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py` — 1000 sims × 300 samples 随机故障模拟 + adaptive 对比回归 + high-K_eff/low-η_max 受益分析

依赖状态：numpy 2.3.2, scipy 1.17.1, statsmodels 0.14.6, pingouin 0.6.1 均就绪。Step 3 产出 MI 矩阵后可直接运行。

---
