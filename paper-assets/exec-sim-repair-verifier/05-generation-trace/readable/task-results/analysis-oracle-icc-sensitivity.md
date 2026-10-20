# analysis oracle icc sensitivity

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oracle-icc-sensitivity_20260516T043503_result.json`
- **Structured JSON:** [`70b274667bb5510184fb.json`](../../sessions/70/70b274667bb5510184fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D107 sensitivity analysis 完成。

**关键数字：**

| ICC | 70-85% Advantage | 说明 |
|-----|-----------------|------|
| 0.000 | 0.64 pp | i.i.d. baseline |
| 0.191 | **2.38 pp** | function-level (论文现用) |
| 0.3146 | **3.80 pp** | repo-level |
| 0.500 | 5.78 pp | |

- Advantage 随 ICC **单调递增**，确认 function-level ICC=0.191 是保守估计
- Repo-level (ICC=0.3146) advantage 是 function-level 的 **1.60x** (+1.42pp)
- ICC=0.50 时 advantage 达 5.78pp，是 function-level 的 2.43x

**产出文件：**
- 脚本：`oracle_icc_sensitivity.py`
- 图表：`artifacts/oracle_icc_sensitivity.pdf` + `.png`
- 数据：`artifacts/oracle_icc_sensitivity.json`

注意：这些 advantage 数值比原始 `mvp_a_total_sim.py` 的 ~10.93pp 小，因为原始用的是 all-or-nothing block noise (ICC≈1 within blocks)，而 Beta-Binomial 模型在 ICC=0.191 时给出更温和的相关性。两组数字不矛盾——原始模型是另一种极端情形，sensitivity analysis 展示的是 ICC 连续变化下的趋势。

---
