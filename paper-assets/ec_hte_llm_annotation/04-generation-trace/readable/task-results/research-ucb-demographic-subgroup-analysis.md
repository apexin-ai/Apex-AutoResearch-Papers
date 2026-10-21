# research ucb demographic subgroup analysis

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ucb-demographic-subgroup-analysis_20260524T045225_result.json`
- **Structured JSON:** [`ebdd7bd87dee8fcac891.json`](../../sessions/eb/ebdd7bd87dee8fcac891.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

### Max Δπ = 0.117（race × ideology），低于 0.15 阈值

**单一 demographic features 的 Δπ：**
| Feature | Δπ |
|---|---|
| education | 0.084 |
| race | 0.080 |
| ideology | 0.077 |
| ideology (grouped) | 0.049 |
| income | 0.045 |
| age_group | 0.040 |
| gender | 0.017 |

**交互特征：**
- race × ideology: Δπ = 0.117（最高，但仍 < 0.15）
- gender × ideology: Δπ = 0.092（排除 N=36 的 non-binary_liberal 后）

### 为什么 Δπ 不够大

1. **高度不对称 CM**：FPR ≈ 0.17, FNR ≈ 0.55。LLM 的主要问题是漏检 hate speech（高 FNR），这在所有 demographic 组中都很一致
2. **Demographic 效应方向一致**：保守派 annotators 的 π 更高（~0.39），自由派更低（~0.35），但差异不够大
3. **Annotator-level 分组 ≠ observation-level 分组**：每条评论有多个不同 demographic 的标注者，无法干净地将 comments 分配到 demographic subgroups

### Semi-synthetic 验证（即使用虚高的 Δπ=0.23）

用包含 outlier 的 gender×ideology 分组跑了 100 MC runs，correction 方法全部比 naive 更差：
- Naive RMSE = 0.104
- HB EC-HTE RMSE = 0.174–0.212
- Global RMSE = 0.412–0.664

原因：1-FPR-FNR ≈ 0.28（分母太小），correction 放大了估计噪声。

### 产出文件
- `results/ucb_demographic_delta_pi.csv` — Δπ 汇总
- `results/ucb_demographic_delta_pi_summary.md` — 完整分析
- `results/ucb_demographic_cm_detail.csv` — 每组 CM 细节
- `results/ucb_demographic_echte_results.csv` — semi-synthetic 原始结果
- `exp_ucb_demographic.py` — 完整代码

---
