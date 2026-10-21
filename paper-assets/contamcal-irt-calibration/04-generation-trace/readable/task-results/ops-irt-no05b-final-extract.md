# ops irt no05b final extract

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_irt_no05b_final_extract_20260517T081434_result.json`
- **Structured JSON:** [`7e80a95a563b3a4b2118.json`](../../sessions/7e/7e80a95a563b3a4b2118.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型列表: 8 个 1.5B + 5 个 3B = 13 个模型。theta 没有保存在输出中。

以下是完整结果汇总。所有 9 个域的 IRT 拟合成功完成（脚本仅在最后的 `generate_summary` 阶段因 bug 崩溃，不影响单域结果）。

---

## 完整结果

| Domain | γ_mean | γ_2.5% | γ_97.5% | CI excludes 0? | PPP | MAE | Rhat OK |
|--------|--------|--------|---------|----------------|-----|-----|---------|
| STEM_Math | 0.499 | -0.213 | 1.203 | NO | 0.206 | 0.017 | YES |
| STEM_Science | 0.504 | -0.189 | 1.202 | NO | 0.149 | 0.014 | YES |
| STEM_CS_Eng | 0.497 | -0.425 | 1.397 | NO | 0.392 | 0.005 | YES |
| Medical | 0.235 | -0.421 | 0.879 | NO | 0.124 | 0.013 | YES |
| Humanities | -0.309 | -0.852 | 0.257 | NO | 0.530 | 0.002 | YES |
| Social_Sciences | **-0.571** | **-1.054** | **-0.103** | **YES (neg)** | 0.570 | 0.013 | YES |
| Business_Law | 0.044 | -0.497 | 0.579 | NO | 0.299 | 0.012 | YES |
| Other | 0.127 | -0.612 | 0.885 | NO | 0.096 | 0.014 | NO (rhat=1.010) |
| **pooled** | 0.107 | -0.401 | 0.625 | NO | 0.208 | 0.011 | YES |

## 关键发现

1. **仅 Social_Sciences 的 95% CI 排除零**（γ 为负值，CI 完全 < 0）。这意味着在该域中，exposure/contamination 与 performance 之间的关联为负方向（1.5B 高 exposure 模型反而表现相对更好，或 3B 低 exposure 模型表现不如预期）。

2. **STEM 域 γ 点估计最高**（~0.50），方向正确但 CI 宽，均包含零。

3. **Pooled 结果 γ=0.107，CI 包含零**，整体未检测到显著 contamination 效应。

4. **θ 参数未保存**：`fit_domain` 函数只提取了 gamma 到 JSON，没有保存 theta draws 或 summary。如需 θ_3B - θ_1.5B 差异，需修改脚本加入 theta 提取后重跑。

5. **崩溃原因**：`generate_summary` 中 `round(r["ppp"], 4)` 失败，因为 `ppp` 是 dict（含 overall_ppp/obs_mean_acc 等字段）而非 float。所有单域 fit 已完成，仅最终汇总未生成。

6. **Other 域 rhat=1.010** 略高于 1.01 阈值（但 divergences=0，ESS 充足，实际影响可忽略）。

---
