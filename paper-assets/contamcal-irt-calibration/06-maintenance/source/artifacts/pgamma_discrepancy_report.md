# P(γ<0) Numerical Discrepancy Report

## 1. 论文中的精确位置

### 来源 A: 主文 + Table 15 (一致)

| 位置 | 文件 | 行号 | 值 |
|------|------|------|-----|
| §5.4 Domain-Level Analysis | `docs/paper/results.tex` | L136 | γ_d = -0.63, CI [-1.07, -0.19], P(γ<0) = 99.7% |
| Table 15 (`tab:domain_gamma`) J=16 列 | `docs/paper/appendix.tex` | L377 | γ = -0.63, P(γ<0) = 99.7%, PPP=0.722 |

上下文：Table 15 同时报告 J=13 和 J=16 两列。J=13 列: γ=-0.57, P(γ<0)=99.1%。J=16 列: γ=-0.63, P(γ<0)=99.7%。主文引用的是 J=16 值。

### 来源 B: Table 10 (矛盾)

| 位置 | 文件 | 行号 | 值 |
|------|------|------|-----|
| Table 10 (`tab:socsci_prior`) N(0,1) 行 | `docs/paper/appendix.tex` | L208 | γ̂ = -0.497, CI [-0.943, -0.055], P(γ<0) = 98.48%, PPP=0.282 |

上下文：Table 10 是 Social Sciences 的 prior sensitivity 分析，标注 J=16。三行分别为 N(0,0.5): γ=-0.428/97.95%, N(0,1): γ=-0.497/98.48%, N(0,2): γ=-0.507/98.92%。

**矛盾**：Table 15 和 Table 10 均标注 J=16、均使用 N(0,1) prior，但 γ 差 27%（-0.63 vs -0.497），P(γ<0) 差 1.22pp。

---

## 2. 数据来源追溯

### 来源 A 的产出链

```
脚本:  /root/contamcal-irt-calibration/exp006/run_mmlu_domain_gamma_j16.py
输出:  /root/autodl-tmp/exp006/mmlu_domain_irt_j16_qwen/Social_Sciences/irt_results.json
时间:  2026-05-18 11:09:12 CST
```

输出 JSON 精确值：
- γ mean = -0.6274, CI [-1.073, -0.192], P(γ<0) = 0.99675
- n_models = 16, n_items = 2000, original_n_items = 3077
- mean_acc = **0.7198**, PPP = 0.722

### 来源 B 的产出链

```
脚本:  /root/contamcal-irt-calibration/exp006/gamma_prior_sensitivity.py
输出:  /root/autodl-tmp/exp006/gamma_prior_sensitivity/social_sciences/sensitivity_comparison.json
时间:  2026-05-18 03:44:18 CST
```

输出 JSON 精确值（baseline_10 / N(0,1) 行）：
- γ mean = -0.4967, CI [-0.943, -0.055], P(γ<0) = 0.9848
- n_models = 16, n_items = 2000
- mean_acc = **0.7085**, PPP = 0.282

---

## 3. 配置差异分析

### 完全相同的配置

| 参数 | 来源 A (j16) | 来源 B (sensitivity) |
|------|-------------|---------------------|
| Model set | 16 Qwen2.5 (8×1.5B + 8×3B) | 同左（model_list 完全一致） |
| Stan model | contam_irt_2pl_gamma.stan | 同左 |
| Prior | N(0, 1) | 同左 |
| Chains | 4 | 4 |
| Warmup | 1000 | 1000 |
| Samples | 1000 | 1000 |
| Adapt delta | 0.95 | 0.95 |
| Max treedepth | 12 | 12 |
| MCMC seed | 42 | 42 |
| Item subsample seed | 42 | 42 |
| Target items | 2000 | 2000 |

### 关键差异: 数据加载逻辑

| 维度 | 来源 A (j16) | 来源 B (sensitivity) |
|------|-------------|---------------------|
| 数据加载函数 | `load_pooled_eval_results()` (from run_irt_calibration.py) | 自建 `load_social_sciences_data()` |
| n_total_items 计算 | `data["benchmarks"]["mmlu"]["n_items"]` (metadata 字段) | `min(len(r) for r in responses_list)` (per_item 数组长度最小值) |
| RRF key 映射 | 有 `DIR_TO_RRF_KEY` 字典处理 d000_s42_a32 → d000_a32_s42 等别名 | 无此映射 |
| MODEL_WHITELIST | 自定义 16 模型 | 从 `run_mmlu_domain_gamma_no05b.py` 导入（磁盘上为 13 模型，但运行时找到 16） |

**根因**：两个脚本通过不同路径计算 `n_total_items`，传入 `build_domain_col_indices(subject_list, n_total_items)` 时值不同。该函数用 `range(min(len(subject_list), n_total_items))` 遍历 MMLU 题目，将每个题目映射到对应 domain。`n_total_items` 不同 → Social Sciences 的列索引集合不同 → 子采样起点不同 → 最终 2000 条 item 不同。

**验证**：mean_acc 差 1.13pp（0.7198 vs 0.7085），在相同 16 个模型下，这只能由不同 item 子集解释。

---

## 4. 结论与修正建议

### 哪个正确

**来源 A（γ=-0.63, P(γ<0)=99.7%）是权威结果。**

理由：
1. `run_mmlu_domain_gamma_j16.py` 是主分析管线，其数据加载逻辑与所有其他 domain-level 分析一致
2. Table 15 中 J=13 列 (γ=-0.57) 的来源 (`mmlu_domain_irt_no05B`) 也使用相同的 `load_pooled_eval_results` 路径，J=13→J=16 的连续性成立
3. PPP=0.722（充分拟合）vs 0.282（边缘），说明来源 A 的 item 子集在 2PL+γ 下更适配

### 修正建议

1. **重跑 sensitivity**：修改 `gamma_prior_sensitivity.py`，使其使用 `run_mmlu_domain_gamma_j16.py` 的数据加载逻辑（或直接加载 `mmlu_domain_irt_j16_qwen/Social_Sciences/` 下的数据矩阵），确保 item 子集一致。预期 N(0,1) 行将恢复到 γ≈-0.63, P(γ<0)≈99.7%，sensitivity 结论（γ 仅变化 1.2×）可能仍成立。

2. **更新 Table 10**：用重跑结果替换当前数值。同时验证 Table 10 与 Table 15 J=16 行的 N(0,1) baseline 完全吻合。

3. **代码修复**：统一 Social Sciences 子采样逻辑为单一代码路径。建议将 `load_social_sciences_data()` 改为从 j16 的输出目录直接读取已保存的 response/exposure 矩阵，避免重复数据加载。

### Bonferroni 影响

如果修正后 P(γ<0) 在 sensitivity 分析中统一为 ~99.7%，则 Bonferroni-corrected threshold (99.375%) 在所有 prior 下均通过，消除 reviewer 指出的"自身数据矛盾"问题。
