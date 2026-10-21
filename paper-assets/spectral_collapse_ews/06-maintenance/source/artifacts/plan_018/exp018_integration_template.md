# Post-exp_018 Integration Template (r=0.5 seed43 → 2-seed)

> exp_018 完成后，按此模板执行所有更新。

## 当前 seed42 数据 (用于交叉验证)
- SLV Gen10: 2573.2
- eff_rank Gen10: 554.5
- PPL Gen10: 15.20
- D-4 Gen10: 0.095
- max_Δt: 0

## Step 1: 数据收集
- [ ] SSH 到 gpu-6000pro-1，确认 exp_018 results JSON 完整 (Gen 0-10)
- [ ] 运行 `python scripts/collect_phase_table_stats.py --ratio 0.5 --seeds 42 43`
- [ ] 记录：SLV mean±sd, eff_rank mean±sd, PPL mean±sd, D-4 mean±sd, CV, max_Δt

## Step 2: Table 3 更新
- `experiments.tex` L178: 替换 r=0.5 行
  - 旧: `0.50 & III & 2573.2 & 554.5 & 15.20 & .095 & 0     & 10`
  - 新: `0.50 & III & [FILL_SLV] & [FILL_EFFRANK] & [FILL_PPL] & [FILL_D4] & 0     & 10`
- `experiments.tex` L181 (caption):
  - 如果 exp_017 已完成: 旧 `$r{=}0.2$ the mean of two seeds (42, 43); $r{=}0.5$ reports a single seed`
  - 新: `$r{=}0.2$ the mean of two seeds (42, 43); $r{=}0.5$ the mean of two seeds (42, 43)`
  - 如果 exp_017 未完成: 旧 `$r{=}0.2$ and $r{=}0.5$ report a single seed`
  - 新: `$r{=}0.2$ reports a single seed; $r{=}0.5$ the mean of two seeds (42, 43)`

## Step 3: §3.5 正文更新
- `experiments.tex` L143: r=0.5 的 Gen10 终值
  - 旧: `reaching 2573 at Gen~10 ($+$8.7\% above baseline)`
  - 新: `reaching [FILL_SLV_ROUNDED] at Gen~10 ($+[FILL_PCT]\%$ above baseline)`
  - 注意：2573 是 seed42 单 seed 值的整数截断，2-seed mean 可能略有变化
- `experiments.tex` L144: Per-gen gains range
  - 旧: `$\Delta_t \in [+11, +35]$ for $t \geq 2$; mean $+23.0$`
  - 需验证 2-seed mean 是否改变这些值；如果变化 <1，保留不变

## Step 4: Figure 1 caption
- `experiments.tex` L42: Figure 1 uses r=0.5 as dashed line
  - 旧: `dashed: $r{=}0.5$, single seed`
  - 新: `dashed: $r{=}0.5$, 2-seed mean`
  - 注意：Figure 1 可能仍然画的是 seed42 单条线。如果图未重绘，caption 应保留 "single seed" 或注明 "representative seed"

## Step 5: Figure 2 caption
- `experiments.tex` L123:
  - 旧（取决于 exp_017 状态）: `$r{=}0.2$ and $r{=}0.5$: single seed` 或 `$r{=}0.2$: 2-seed mean; $r{=}0.5$: single seed`
  - 新: 将 `$r{=}0.5$: single seed` → `$r{=}0.5$: 2-seed mean`

## Step 6: Limitations 更新
- `limitations.tex` L5:
  - 如果 exp_017 已完成: 旧 `$r{=}0.2$ reports two seeds and $r{=}0.5$ a single seed`
  - 新: `$r{=}0.2$ and $r{=}0.5$ each report two seeds`
  - 如果 exp_017 未完成: 旧 `$r \in \{0.2, 0.5\}$ each report a single seed`
  - 新: `$r{=}0.2$ reports a single seed and $r{=}0.5$ two seeds`

## Step 7: Response letter 更新
- R1-W2 表格 (L52):
  - 旧: `| r = 0.5 | 42 | ✅ Complete; seed 43 pending | — (single seed; 2-seed pending) |`
  - 新: `| r = 0.5 | 42, 43 | ✅ Complete | [FILL_CV]% |`

## Step 8: Conclusion 更新
- `conclusion.tex` L10: r=0.5 downstream metrics
  - 旧: `even at $r = 0.5$, perplexity increases 59\% and D-4 drops 87\%`
  - 需验证 2-seed mean 是否改变百分比；如果变化 <1pp，保留不变
  - PPL baseline=9.55; 如果 2-seed PPL ≈ 15.20，则 59% 不变
  - D-4 baseline=0.738; 如果 2-seed D-4 ≈ 0.095，则 87% 不变

## Step 9: 验证
- [ ] `cd paper && latexmk -pdf main.tex` — 编译通过
- [ ] 检查 PDF ≤ 8 页
- [ ] grep "single seed" 确认 r=0.5 不再标注为 single seed（除非 Figure 1 未重绘）
- [ ] commit: `[paper] upgrade r=0.5 to 2-seed coverage: Table 3, §3.5, Figure 1/2, Limitations`

## 注意事项
- r=0.5 正文 L143-144 中的具体数值可能基于 seed42 单 seed
- Figure 1 的 dashed line 可能是 seed42 单条轨迹——如果不重绘图，caption 应标注 "representative seed" 而非 "2-seed mean"
- Conclusion L10 的百分比需要用 2-seed mean 重算验证
