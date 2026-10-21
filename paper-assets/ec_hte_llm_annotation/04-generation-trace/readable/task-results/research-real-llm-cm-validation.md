# research real llm cm validation

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_real-llm-cm-validation_20260523T071518_result.json`
- **Structured JSON:** [`d94a562724dd592d4236.json`](../../sessions/d9/d94a562724dd592d4236.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

100-MC 实验完成。总耗时 4121s（~69 分钟），124,800 raw rows。

---

## 最终结果汇总

### EC-HTE vs Global 胜率

| n_expert | HB EC-HTE 赢 (|bias|) | HB EC-HTE 赢 (RMSE) | Oracle EC-HTE 赢 (|bias|) | Oracle EC-HTE 赢 (RMSE) |
|----------|----------------------|---------------------|--------------------------|------------------------|
| 100 | **0/13** | **0/13** | **13/13** | **13/13** |
| 250 | **0/13** | **0/13** | **11/13** | **12/13** |
| 500 | **5/13** | **0/13** | **10/13** | **10/13** |

### 全局均值

| n_expert | Method | Mean|Bias| | RMSE | Coverage |
|----------|--------|-----------|------|----------|
| any | naive | 0.1019 | 0.1209 | **0.783** |
| 100 | global_corrected | 0.1298 | 0.1653 | 0.937 |
| 250 | global_corrected | 0.1198 | 0.1514 | 0.944 |
| 500 | global_corrected | 0.1172 | 0.1470 | 0.947 |
| 100 | hb_ec_hte | 0.2286 | 0.4050 | 0.906 |
| 250 | hb_ec_hte | 0.1460 | 0.2059 | 0.938 |
| 500 | hb_ec_hte | 0.1270 | 0.1730 | 0.947 |
| any | oracle_ec_hte | 0.1112 | 0.1395 | **0.951** |

### 核心发现

1. **Oracle EC-HTE 全面优于 Global**（10–13/13），证明 per-subgroup 校正在真实 CM 下理论上成立
2. **HB EC-HTE 受限于估计方差**：HB Gibbs 从有限 expert labels 估计 K=4 个 per-subgroup CM，方差代价高于 bias 收益。RMSE gap 从 n=100 时 +145% 收窄到 n=500 时 +17.6%，趋势正确但收敛慢
3. **Coverage 是最大亮点**：Naive 覆盖率仅 78.3%（严重不足），所有校正方法 ≥ 90.6%，接近名义 95%
4. **收敛趋势清晰**：HB EC-HTE 的 |bias| 从 0.2286→0.1460→0.1270 单调下降，approaching Oracle (0.1112)

### 产出文件

- `results/exp_real_cm_validation_raw.csv` — 124,800 rows（per-MC, per-subgroup, per-method）
- `results/exp_real_cm_validation.csv` — 156 rows（汇总统计）
- `results/exp_real_cm_validation.log` — 运行日志

---
