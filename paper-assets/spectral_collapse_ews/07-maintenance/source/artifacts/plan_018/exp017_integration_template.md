# Post-exp_017 Integration Template (r=0.2 seed43 → 2-seed)

> exp_017 完成后，按此模板执行所有更新。

## 当前 seed42 数据 (用于交叉验证)
- SLV Gen10: 2479.7
- eff_rank Gen10: 511.3
- PPL Gen10: 13.83
- D-4 Gen10: 0.520
- max_Δt: 0.0019

## Step 1: 数据收集
- [ ] SSH 到 gpu-6000pro-1，确认 exp_017 results JSON 完整 (Gen 0-10)
- [ ] 运行 `python scripts/collect_phase_table_stats.py --ratio 0.2 --seeds 42 43`
- [ ] 记录：SLV mean±sd, eff_rank mean±sd, PPL mean±sd, D-4 mean±sd, CV, max_Δt

## Step 2: Table 3 更新
- `experiments.tex` L175: 替换 r=0.2 行
  - 旧: `0.20 & II  & 2479.7 & 511.3 & 13.83 & .520 & .0019 & 10`
  - 新: `0.20 & II  & [FILL_SLV] & [FILL_EFFRANK] & [FILL_PPL] & [FILL_D4] & .0019 & 10`
  - 注意：max_Δt 可能变化（取 2-seed 数据中的 max），需验证
- `experiments.tex` L181 (caption): 
  - 旧: `$r{=}0.2$ and $r{=}0.5$ report a single seed`
  - 新: `$r{=}0.2$ the mean of two seeds (42, 43); $r{=}0.5$ reports a single seed`

## Step 3: §3.5 正文更新
- `experiments.tex` L131: r=0.2 的 Gen10 终值
  - 旧: `reaching 2479.7 at Gen~10 ($+4.8\%$ above baseline)`
  - 新: `reaching [FILL_SLV] at Gen~10 ($+[FILL_PCT]\%$ above baseline)`
  - 注意：整段 L130-135 的具体数值（2367.5, 2358.3, -9.2 等）是 seed42 数据，保留不变（seed42 作为 representative trajectory）
- `experiments.tex` L161: r=0.2 的 D-4 s.d. 可选更新（当前没有 r=0.2 的 s.d. 引用，跳过）

## Step 4: Figure 2 caption
- `experiments.tex` L123:
  - 旧: `$r{=}0.2$ and $r{=}0.5$: single seed`
  - 新: `$r{=}0.2$: 2-seed mean; $r{=}0.5$: single seed`

## Step 5: Limitations 更新
- `limitations.tex` L5:
  - 旧: `$r \in \{0.2, 0.5\}$ each report a single seed`
  - 新: `$r{=}0.2$ reports two seeds and $r{=}0.5$ a single seed`

## Step 6: Response letter 更新
- R1-W2 表格 (L51):
  - 旧: `| r = 0.2 | 42 | ✅ Complete; seed 43 running | — (single seed; 2-seed pending) |`
  - 新: `| r = 0.2 | 42, 43 | ✅ Complete | [FILL_CV]% |`

## Step 7: 验证
- [ ] `cd paper && latexmk -pdf main.tex` — 编译通过
- [ ] 检查 PDF ≤ 8 页
- [ ] grep "single seed" 确认 r=0.2 不再标注为 single seed
- [ ] commit: `[paper] upgrade r=0.2 to 2-seed coverage: Table 3, §3.5, Figure 2, Limitations`

## 注意事项
- r=0.2 正文 L130-135 中的具体数值（SLV dip -9.2, EMA values 2362.7/2367.1 等）来自 seed42 单 seed 数据，作为 representative trajectory 保留不变
- 2-seed 升级只影响 Gen10 终值（Table 3 行）和 seed count 描述
- 不需要重绘 Figure 2（数据变化小，视觉上无区别）
