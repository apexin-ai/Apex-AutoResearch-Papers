# Paper Update Checklist: n=50 → n=500

> 生成时间: 2026-05-15 | 适用实验: c2_n500_deepseek + c2_qw_n500 (C7)
> 约束: median + bootstrap CI 为主指标 (D054); d_z 分场景 (D059); Qwen imp-vs-rand 不claim显著直到n=500确认 (D058); C8=partially_confirmed (D060); C5b=future_work (D056)

---

## 优先级说明
- **P0**: 核心数字，读者第一眼看到，必须同步更新
- **P1**: 支撑性数字/表格，与 P0 有数据依赖
- **P2**: 条件性更新（取决于 n=500 结果）
- **P3**: 一致性检查，防止 n=50/n=500 混用

---

## P0: 核心数字更新

### 1. methodology.tex:10 — 样本量
```
当前: "We use 50 problems stratified from MATH-500"
更新: → 500 problems (n=500 的具体描述，包括 stratification 方式)
```

### 2. abstract.tex:6 — 样本量
```
当前: "using 50 MATH-500 problems"
更新: → 500 MATH-500 problems
```

### 3. abstract.tex:7 — DeepSeek 主指标
```
当前: "median Interaction Index difference...from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)"
更新: → 用 n=500 segment-level median diff + paired d_z 替换
注意: 0.39/14.59 是 segment-level medians；d_z 0.44/0.80 是 paired d_z。两组数据来源不同，都需更新。
```

### 4. introduction.tex:14 — DeepSeek 主指标（与 abstract 一致）
```
当前: "median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$)"
更新: → 同 abstract
```

### 5. results.tex:8,13,19-20 — Tab aggregate-ii（DeepSeek segment-level Δ）
```
当前 Importance: 0.39, 1.48, 7.16, 14.59
当前 Random: 0.01, -0.02, 0.54, 1.54
caption "$n{=}50$" → $n{=}500$ (或实际有效 n)
更新: → 全部替换为 n=500 值
```

### 6. results.tex:34,40-50 — Tab main-results（DeepSeek 全 per-phase 分解）
```
当前 (importance, 4 sparsity × 3 phases + Δ + G):
  s015: II_high=0.006, II_mid=0.081, II_low=0.398, Δ=0.39, G=69
  s020: II_high=0.015, II_mid=0.203, II_low=1.496, Δ=1.48, G=103
  s025: II_high=0.032, II_mid=1.118, II_low=7.196, Δ=7.16, G=222
  s030: II_high=0.053, II_mid=2.283, II_low=14.639, Δ=14.59, G=274
当前 (random, 4 sparsity × 3 phases + Δ + G):
  s015: 0.093, 0.097, 0.103, 0.01, 1.1
  s020: 0.292, 0.350, 0.276, -0.02, 0.9
  s025: 0.818, 0.932, 1.363, 0.54, 1.7
  s030: 2.503, 2.592, 4.041, 1.54, 1.6
caption "50 problems" → 500 problems
更新: → 全部替换为 n=500 值
```

### 7. results.tex:106,117-120 — Tab cohens-d（DS + QW paired d_z + Δ̃[CI]）
```
当前 DS: d_z 0.44/0.52/0.68/0.80; Δ̃ 0.32[0.20,0.47] / 1.15[0.66,1.26] / 3.97[2.83,5.29] / 9.94[8.39,16.65]
当前 QW: d_z 0.28/0.55/0.89/1.02; Δ̃ 0.05[-0.01,0.11] / 0.21[0.07,0.40] / 1.11[0.61,1.47] / 2.62[1.72,3.65]
更新: → 全部替换为 n=500 值
关键: QW s015 CI 当前包含零 → n=500 后检查是否仍包含零（影响 onset threshold 叙事）
```

### 8. conclusion.tex:4 — 核心数字复述
```
当前: "severity gradient grows from $69{\times}$ to $274{\times}$...($d_z$: $0.44 \to 0.80$)"
更新: → 与 results 一致
```

### 9. discussion.tex:5 — severity gradient + crossover 复述
```
当前: "severity gradient ($69$--$274{\times}$)"
当前: crossover 数字 "0.032 vs 0.818", "7.196 vs 1.363"
更新: → 与 results 一致
```

### 10. results.tex:29 + 58 — G 值 + fig1 caption
```
当前: G "from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$"
当前 fig1 caption: "$69{\times}$ to $274{\times}$"
更新: → n=500 G 值
```

---

## P1: 支撑性数字更新

### 11. results.tex:66 — Crossover 数字
```
当前: "importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363"
reversal "5.3×"
更新: → n=500 crossover 值
```

### 12. results.tex:71 — Qwen cross-model 段落
```
当前: "Δ increases from 0.04 at s=0.15 to 2.94 at s=0.30...d_z ≥ 0.55...d_z=0.28 CI includes zero"
更新: → n=500 Qwen 值
关键: 检查 s015 d_z 是否仍 marginal，onset threshold 是否仍 s≥0.20
```

### 13. appendix_moved.tex:26 — Qwen/DS 有效 n
```
当前: "Four of the 50 problems...n=46 valid problems for Qwen (vs. n=49 for DeepSeek)"
更新: → n=500 的排除数和有效 n
```

### 14. appendix_moved.tex:59-60 — Tab cross-model Qwen Δ
```
当前 DS: 0.39, 1.48, 7.16, 14.59
当前 QW: 0.04, 0.23, 1.27, 2.94
更新: → n=500 值
```

### 15. appendix_moved.tex:88,93,99-102 — Tab permutation（DeepSeek permutation test）
```
当前: n=49; observed Δ̃ 0.37[0.19,0.62], 0.97[0.69,1.49], 3.34[1.66,6.64], 9.85[6.70,16.29]
caption "$n{=}49$"
更新: → n=500 permutation test 值
```

### 16. results.tex:104 — permutation test 段落引用
```
当前: "observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$"
更新: → 与 Tab permutation 一致
```

### 17. appendix_moved.tex:11 — crossover 详细数字
```
当前: "reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$"
更新: → n=500 reversal magnitudes
```

### 18. appendix_disc_analysis.tex:46-47 — permutation CI + skewness 统计
```
当前: "mean/median ratio ~1.6:1 at s=0.30"
当前: "permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]"
当前 (line 11): "high-phase II rises to 0.105 at s=0.35"
更新: → n=500 值 (s035 supplementary 是否也需更新取决于是否重跑)
```

### 19. abstract.tex:10 — LLaMA cross-arch 段落
```
当前: "Δ̃: 0.020→0.356; s=0.30 Wilcoxon p_Bonf=0.029"
注意: LLaMA 实验仍为 n=50，数字不变，但需检查措辞是否暗示与 DS/QW 同一 n
```

### 20. 图表重新生成
```
fig1_dose_response.pdf — G vs s 曲线（P0 依赖）
fig3_crossover.pdf — crossover bar chart
fig4_bootstrap.pdf — permutation forest plot
fig5_crossmodel.pdf — cross-model Δ comparison
所有图需用 n=500 数据重新生成
```

---

## P2: 条件性更新

### 21. D058: Qwen imp-vs-rand 显著性
```
当前状态: 论文未报告 Qwen imp-vs-rand permutation test（只报告了 DeepSeek）
约束: n=500 前不得 claim Qwen imp-vs-rand 显著
行动:
  - 若 n=500 Qwen imp-vs-rand 显著 → 可添加 Qwen permutation test 表格，strengthens C1
  - 若仍不显著 → 在 cross-model 段落加 caveat，或维持当前策略（只报 within-importance gradient）
检查文件: results.tex:71, appendix_results.tex:10
```

### 22. D059: d_z 报告策略
```
约束: within-importance d_z 保留; 涉及 random 只报方向
行动: 检查 n=500 后是否有新的 imp-vs-rand d_z 值需要报告，确保遵守"只报方向"规则
影响文件: results.tex, appendix_moved.tex
```

### 23. C2 预注册: Qwen s015 onset threshold
```
当前: paper_framing 预注册 "n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)'"
检查: results.tex:71 "marginal at s=0.15" + Tab cohens-d QW s015 行
行动:
  - 若 n=500 QW s015 CI 不跨零 → onset = s≥0.15，更新叙事
  - 若仍跨零 → 保持 "emerges above ~s020" 叙事
```

### 24. Placeholder 值填充
以下 \placeholder{} 标记需用实际数据填充:

| 文件:行 | Placeholder | 数据来源 | n=500影响? |
|---------|-------------|----------|-----------|
| abstract.tex:8 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |
| results.tex:71 | NULL_PCT | Qwen per-phase null rate | 是 |
| results.tex:81 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |
| results.tex:86 | N_LLAMA | c3_llama | 否(n=50) |
| results.tex:92-95 | 整个 LLaMA 表格 (12 cells) | c3_llama | 否(n=50) |
| discussion.tex:10 | ORACLE_PCT, ORACLE_P, HEUR_PCT, HEUR_P | c5b_pilot | 否 |
| discussion.tex:15 | LLaMA random Wilcoxon p | c3_llama | 否(n=50) |
| appendix_moved.tex:30 | NULL_PCT | Qwen null rate | 是 |
| appendix_moved.tex:35 | N_QW | Qwen valid n | 是 |
| appendix_moved.tex:41-43 | Qwen effective n 表格 (12 cells) | Qwen per-phase data | 是 |
| appendix_moved.tex:73 | ρ, p (per-problem concordance) | cross_model_analysis.json | 是 |
| appendix_moved.tex:76 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |
| appendix_results.tex:7 | 同 appendix_moved.tex:73 (重复!) | cross_model_analysis.json | 是 |
| appendix_results.tex:10 | 同 appendix_moved.tex:76 (重复!) | bf16_qw_rand_s030 | 是 |
| appendix_disc_analysis.tex:14 | Qwen rand s030 Δ̃ | bf16_qw_rand_s030 | 是 |
| appendix_disc_analysis.tex:49 | Qwen rand s030 Δ̃ | qw_rand_s030 | 是 |

⚠️ appendix_results.tex 未被 main.tex \input，内容与 appendix_moved.tex §Cross-Model 重复。建议删除或统一。

---

## P3: 一致性与混用风险

### 25. n=50 / n=500 混用风险矩阵

| 数据源 | 当前 n | 更新后 n | 混用风险 |
|--------|--------|---------|---------|
| DeepSeek importance/random (c2) | 50 | **500** | 主表全部替换 |
| Qwen importance/random (c2) | 50 | **500** | 主表全部替换 |
| LLaMA cross-arch (c3_llama) | 50 | **50 不变** | ⚠️ 高风险 |
| Entropy/discrimination (c4) | 30 | **30 不变** | ⚠️ 中风险 |
| c5b_pilot | ~50 | **不变** | 低风险 |
| Permutation test | 49(DS)/46(QW) | **~490/~460** | 替换 |
| Cross-model comparison | 50 | **500** | 替换 |

### 26. 需要显式声明不同 n 的位置
```
- abstract.tex: "50 MATH-500 problems" → 改为区分 DS/QW (n=500) vs LLaMA (n=50)
  建议: "500 MATH-500 problems (50 for cross-architecture validation)"
- results.tex §5.5 (cross-arch): 已有 "n=\placeholder{N_LLAMA}" → 填入 49 或 50，确保读者知道这不是 500
- analysis.tex §6: 当前未提及 c4 的样本量 → 建议添加脚注 "(30 problems per model)"
- discussion.tex §7 (pilot): 当前未提及 pilot 样本量 → 建议添加
- methodology.tex: 需说明 "500 problems for primary experiments; 50 for cross-architecture (LLaMA)"
- limitations.tex: 添加 "LLaMA 和 mechanism 分析基于 n=50/30 子集"
```

### 27. C8 partially_confirmed 限定语检查 ✅
已确认以下位置使用了合格限定语:
- abstract.tex:10 — "mixed but directionally consistent evidence"
- results.tex:79 — "partially confirming the cross-architecture hypothesis"
- discussion.tex:14-15 — "partial support...substantially weaker"
- conclusion.tex:4 — "partially extends cross-architecture"
- limitations.tex:1-2 — "partially confirms...substantially weaker"
- appendix_disc_analysis.tex:33 — "partial confirmation"
**状态: 合格，无需修改（除非 n=500 改变了 DS/QW 数据使 LLaMA 对比幅度比例变化）**

### 28. C5b future_work 标注检查 ✅
已确认:
- discussion.tex:10 — pilot 结果 + "promising direction for future work"
- appendix_disc_analysis.tex:57,62 — REBUTTAL comments 标注 future work
**状态: 合格，但 discussion.tex:10 的 \placeholder{} 值需填充**

### 29. Qwen random s030 caveat 检查
当前标注为 negligible/no meaningful modulation 的位置:
- abstract.tex:8 — "negligible median difference" ✅
- appendix_moved.tex:76 — "negligible median difference, CI spans zero" ✅
- appendix_results.tex:10 — 同上 ✅
- appendix_disc_analysis.tex:14 — "negligible effect size" ✅
- appendix_disc_analysis.tex:49 — "negligible effect size, bootstrap CI spanning zero" ✅
**n=500 后需重新检查: Qwen rand s030 是否仍为 borderline/negligible → 若变显著且效应量非 negligible，需修改 "7/8 FAIL" 叙事**

---

## 执行顺序建议

```
Phase 1: 数据准备
  1.1 等 n=500 数据完成
  1.2 运行统计分析脚本 → experiment_summary_table.json, cohens_d, permutation_test 等
  1.3 提取所有新数值到一个汇总表

Phase 2: P0 核心更新 (同步进行，确保一致)
  2.1 更新 results.tex 三张主表 (Tab 1/2/3)
  2.2 更新 abstract.tex 数字
  2.3 更新 introduction.tex 数字
  2.4 更新 conclusion.tex 数字
  2.5 更新 discussion.tex 数字
  2.6 更新 methodology.tex 样本量

Phase 3: P1 支撑更新
  3.1 更新 appendix_moved.tex 所有表格和数字
  3.2 更新 appendix_disc_analysis.tex 数字
  3.3 重新生成 4 张图 (fig1-fig5)

Phase 4: P2 条件分支
  4.1 检查 QW s015 CI → 决定 onset threshold 叙事
  4.2 检查 QW imp-vs-rand → 决定是否添加 Qwen permutation test
  4.3 检查 QW rand s030 → 决定 "7/8 FAIL" 叙事是否需调整
  4.4 填充所有 \placeholder{}

Phase 5: P3 一致性扫描
  5.1 全文搜索 "n=50" / "50 problems" / "n=49" / "n=46" → 确保无残留
  5.2 添加 LLaMA n=50 / c4 n=30 的显式声明
  5.3 清理 appendix_results.tex（重复文件）

Phase 6: 验证
  6.1 LaTeX 编译 → 确保无 red placeholder 残留
  6.2 数字交叉检查: 每个数字在所有出现位置一致
  6.3 paper_framing.md 同步更新
```
