# Consistency Fixes Report

## 修复 1: CI 区间 [0.786, 0.799]

已从所有 6-gen 上下文中删除该 CI（该 CI 实为 5-gen 数据，与 6-gen point estimate 0.79 混用造成歧义）。保留在 5-gen baselines 表格中（results.tex Table 3, caption 已标注 "5-gen LOGO"）。

- **main.tex**, line 26: `macro-F1 of 0.79 (95\% CI: [0.786, 0.799]; $p < 0.001$ ...)` → `macro-F1 of 0.79 ($p < 0.001$ ...)`
- **abstract.tex**, line 8: 同上
- **abstract_014854.tex**, line 8: 同上
- **introduction.tex**, line 23: `macro-F1 of 0.79 (95\% CI [0.786, 0.799]; \textit{plan-014})` → `macro-F1 of 0.79`
- **introduction.tex**, line 34: `F1\,=\,0.79 [0.786, 0.799] ... (\textit{plan-014, plan-015})` → `F1\,=\,0.79 ... consistency.`
- **introduction_4bbcfd.tex**, lines 23, 34: 同上
- **results.tex**, line 11: `F1\,=\,0.790 (95\% bootstrap CI [0.786, 0.799])` → `F1\,=\,0.789`
- **results.tex**, line 47 (caption): `(0.790, 95\% CI [0.786, 0.799])` → `(0.789)`
- **results_b30771.tex**, lines 11, 47: 同上
- **conclusion.tex**, line 6: `macro-F1 of 0.79 (95\% CI [0.786, 0.799])` → `macro-F1 of 0.79`
- **conclusion_b5f10d.tex**, line 6: 同上
- **conclusion_70534e.tex**, line 6: `macro-F1 of 0.79 (95\% CI [0.786, 0.799]) ... (\textit{plan-014, plan-015})` → `macro-F1 of 0.79 ... 0.86.`
- **main_53f11a.tex**, line 24: `macro-F1 of 0.79 (95\% CI [0.786, 0.799]) with a CI width` → `macro-F1 of 0.79 with a CI width`

**保留**: results.tex / results_b30771.tex 的 baselines 表格（Table 3, line 103/117），因为该表 caption 已明确标注 "5-gen LOGO"。

## 修复 2: 内部实验 ID

所有 `plan-` 引用已删除。

- **introduction.tex**, line 23: 删除 `; \textit{plan-014}`
- **introduction.tex**, line 24: 删除 `(\textit{plan-015})`
- **introduction.tex**, line 28: 删除 `; \textit{plan-004-v2}`
- **introduction.tex**, line 34: 删除 `(\textit{plan-014, plan-015})`
- **introduction.tex**, line 35: 删除 `; \textit{plan-004-v2}`
- **introduction_4bbcfd.tex**: 同上 5 处
- **conclusion_70534e.tex**, line 6: 删除 `(\textit{plan-014, plan-015})`
- **conclusion_70534e.tex**, line 7: 删除 `(\textit{plan-004-v2})`
- **discussion_c98572.tex**, line 14: 删除 `; \textit{plan-015}`
- **discussion_c98572.tex**, line 17: 删除 `(\textit{plan-004-v2})`
- **limitations_69ebec.tex**, line 5: 删除 `; \textit{plan-014}`

## 修复 3: Binoculars 数字 (0.59 → 0.41)

单检测器 CI 下界应为 0.41（Binoculars CI 下界 0.405 四舍五入），非 0.59。

- **introduction.tex**, line 16: `0.59--0.82` → `0.41--0.82`
- **introduction_4bbcfd.tex**, line 16: 同上
- **related_work.tex**, line 11: `0.59--0.82` → `0.41--0.82`
- **related_work_2ce9dd.tex**, line 24: `0.59--0.82` → `0.41--0.82`
- **method_e59d28.tex**, line 58: `0.59--0.82` → `0.41--0.82`

main.tex / abstract.tex / abstract_014854.tex 已正确使用 `0.41--0.82`，无需修改。

## 修复 4: 统一 6-gen 主线数字

将 5-gen 数字 (F1=0.80) 替换为 6-gen 数字 (F1=0.79)。

- **main.tex**, line 25: `macro-F1\,=\,0.80` → `macro-F1\,=\,0.79`（ablation 对比句）
- **abstract.tex**, line 7: `macro-F1\,=\,0.80` → `macro-F1\,=\,0.79`
- **abstract_014854.tex**, line 7: 同上
- **introduction.tex**, line 23: `0.69 to 0.85` → `0.68 to 0.86`（与 abstract/conclusion 统一）
- **introduction_4bbcfd.tex**, line 23: 同上
- **conclusion_70534e.tex**, line 6: `0.69 to 0.86` → `0.68 to 0.86`

results.tex 中 "All three achieve LOGO F1 between 0.80 and 0.82"（line 70/77）保留，因为这是跨 reference model 的消融实验范围，非主线数字。
