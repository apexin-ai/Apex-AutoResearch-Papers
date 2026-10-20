# Falcon3 论文整合清单

## 必须更新（结果出来后）

| # | 文件:行号 | 当前文本 | 更新内容 |
|---|----------|---------|---------|
| 1 | abstract.tex:1 | "five models spanning four independent families" | → "six models spanning five independent families" |
| 2 | abstract.tex:1 | "five-family sample" (×3处) | → "six-family sample" |
| 3 | abstract.tex:1 | "Out-of-sample validation on a held-out fifth family" | → "held-out sixth family" |
| 4 | abstract.tex:1 | "Two patterns...attested in two or more; Collapse and V-recovery each in one" | → 按 Falcon3 pattern 更新 |
| 5 | introduction.tex:5 | "five models spanning four independent families from four labs" | → "six...five...five labs (...TII)" |
| 6 | introduction.tex:10 | "five-family sample" (Figure 1 caption) | → "six-family sample" |
| 7 | introduction.tex:14 | "In our five-family sample, contamination vulnerability..." | → "six-family sample" |
| 8 | introduction.tex:18 | "four families reveals qualitatively different..." | → "five families" |
| 9 | results.tex:4 | "five models from four independent families" | → "six models from five independent families" |
| 10 | results.tex:11 | Table 1 caption: "5/5 families" | → "6/6 families" |
| 11 | results.tex:16-23 | Table 1 (tab:taxonomy) data | 新增 Falcon3 行 |
| 12 | results.tex:28 | "$N=5$ families" | → "$N=6$" |
| 13 | results.tex:31 | "In our five-family sample..." baseline gradient | 加入 Falcon3, 更新 vulnerable band |
| 14 | results.tex:34 | "Two of four patterns...attested in ≥2 families" | → 按实际更新 |
| 15 | results.tex:48 | Table 2 caption: "2/5...4/5...2/5" | → x/6 |
| 16 | results.tex:51-64 | Table 2 (tab:cross_seed) data | 新增 Falcon3 行 |
| 17 | results.tex:67 | "Strict sign consistency holds for 2/5...4/5" | → x/6 |
| 18 | conclusion.tex:3 | "five-family sample" | → "six-family sample" |
| 19 | experimental_setup.tex:7 | "four independent model families from four labs" | 加 Falcon3 + TII |
| 20 | experimental_setup.tex:9 | "yields over 50 checkpoints" | 更新总数 |
| 21 | appendix.tex:42 | Fig caption "4/5 models" | → "x/6 models" |
| 22 | appendix.tex:346 | Fig 7 caption "four independent families" | → "five independent families" |
| 23 | appendix.tex:307-327 | Table 14 (classification sensitivity) | 新增 Falcon3 行 |

## 图表重生成
- fig_dose_response.pdf — 加 Falcon3 曲线
- fig_baseline_vs_effect.pdf — 加 Falcon3 数据点
- fig_arc_dose_response.pdf — 加 Falcon3 曲线（如有 ARC eval）
- Table 1, 2, 5, 6, 14

## 条件更新

### Falcon3 = Benefit
- Benefit 从 2→3 family, strengthen replication
- Limitations: Benefit replication caveat 可删

### Falcon3 = Collapse
- **最大影响**: Collapse 不再 single-family
- abstract/results/limitations: 删除 "Collapse requires additional replication"
- 两独立 family 在 vulnerable band Collapse → 极大强化结论

### Falcon3 = Immune
- 67.4% 出现 Immune 削弱 baseline gradient 叙事
- 需修改 "above 76%, immune" 表述

### Falcon3 = V-recovery
- V-recovery 不再 single-family
- 删除 replication caveat

## 不需要更新
- IRT calibration (§5.5-5.7): 基于 Qwen2.5 within-family
- Signal failure (§5.6): Min-K++ 不涉及 Falcon3
- DiD memorization (§5.4, Table 3): 除非另做
- Domain-level analysis (§5.7): 基于 Qwen2.5
- Prior sensitivity (appendix): 基于 Qwen2.5

## Algorithm 1 d100 依赖
Algorithm 1 显式要求全 5 dosage 包括 d100。d000-d050 可提供早期信号但不能正式分类。
