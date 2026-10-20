# MVP Gate Checklist — D025 CSS-Only 标准

> 适用于 mvp_arithmetic_gpt2_k3 结果判定
> 替代 D002/D024 标准（CIRCUS 已废弃 per D021）
> 代码输出的 gate_verdict 不可信，必须人工按以下标准判定

## 四条件（全部满足 = PASS）

| # | 条件 | 阈值 | IOI 参考值 | Arithmetic 结果 | 判定 |
|---|------|------|-----------|----------------|------|
| 1 | Pairwise Jaccard 任意方法对 < 0.70 | < 0.70 | [0.31, 0.10, 0.09] ✅ | _待填_ | _待判_ |
| 2 | CSS ≥2/3 edge count ≥ 10 | ≥ 10 | 52 ✅ | _待填_ | _待判_ |
| 3 | CSS = 1.0 edge count ≥ 3 | ≥ 3 | 7 ✅ | _待填_ | _待判_ |
| 4 | CSS faithfulness > single-method | CSS CPR > any single | CSS-1.0 CPR=0.11 > EP=-0.24 ✅ | _待填_ | _待判_ |

## 必查清单

| 项目 | 预期 | Arithmetic 结果 |
|------|------|----------------|
| ACDC binarization 方式 | `isinf` 或其他 | _待填_ |
| ACDC 边数 | IOI: 14 | _待填_ |
| CSS distribution (1/3, 2/3, 3/3) | 三级分布 | _待填_ |
| Pairwise Jaccard 三对 | 在 [0.05, 0.30]? | _待填_ |
| Phase D faithfulness 排序 | CSS > single-method | _待填_ |
| Mean ablation 对照 | CPR 非 ablation artifact | _待填_ |

## 判定结果

- 四条件全满足 → **PASS** → complete_mvp → post-mvp-kickoff
- 任一条件不满足 → 分析失败原因：
  - CSS 在 arithmetic 不泛化 → task-specific，评估 pivot
  - ACDC 极端稀疏导致 Jaccard 异常 → 考虑 ACDC binarization 调整
  - faithfulness 不满足 → 检查 ablation 方式（node-level zero ablation 破坏性大）

## IOI 完整参考数据（mvp_pilot_gpt2_ioi_v3）

- off_diagonal_pct: 13.3% [CI: 1.7%-40.5%]
- circus_core_edges: 15, css_2of3: 52, css_3of3: 7
- gate: PASS_MAIN (D002 标准)
- pairwise Jaccard: eapig×ep=0.31, eapig×acdc=0.10, ep×acdc=0.09
- three_way_ratio: 0.045
- circuit_sizes: eapig=100, ep=100, acdc=14
- Phase D faithfulness: CSS-1.0 CPR=0.11 > CSS-0.67=0.06 > ACDC=0.03 > CIRCUS=-0.11 > EAP-IG=-0.11 > EP=-0.24
