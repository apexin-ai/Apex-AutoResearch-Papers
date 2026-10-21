# Post-exp_018 Integration Template v2 (r=0.5 seed43 → 2-seed)

> 更新于 2026-05-23。基于 Round 2 修订后的论文状态（commit e960458 之后），修正行号和遗漏引用。

## 当前 seed42 数据 (用于交叉验证)
- SLV Gen10: 2573.2
- eff_rank Gen10: 554.5
- PPL Gen10: 15.20
- D-4 Gen10: 0.095
- max_Δt: 0

## Step 1: 数据收集
- [ ] SSH 到 rtx6000-diagprobe，确认 exp_018 results JSON 完整 (Gen 0-10)
- [ ] 计算 2-seed mean±sd: SLV, eff_rank, PPL, D-4, CV
- [ ] 记录 max_Δt (应为 0，与 seed42 一致)

## Step 2: Table 3 更新 (experiments.tex L177-190)
- L185: 替换 r=0.5 行
  - 旧: `0.50 & III & 2573.2 & 554.5 & 15.20 & .095 & 0     & 10`
  - 新: `0.50 & III & [FILL_SLV] & [FILL_EFFRANK] & [FILL_PPL] & [FILL_D4] & 0     & 10`
- L188 (caption): 
  - 旧: `$r{=}0.2$ and $r{=}0.5$ report a single seed`
  - 新: `$r{=}0.2$ reports a single seed; $r{=}0.5$ the mean of two seeds (42, 43)`

## Step 3: §3.1 Adaptive Mixing (experiments.tex L66-77)
- L69: `SLV rises to 2573 at Gen~10`
  - 新: `SLV rises to [FILL_SLV_ROUNDED] at Gen~10` (if 2-seed mean differs from 2573)
  - 同行 `(105 points above the pure-collapse peak)` — 用 2-seed SLV mean - 2468 重算
- L75: `perplexity increases 59\% ($9.55 \to 15.20$) and distinct-4 falls 87\% ($.738 \to .095$)`
  - 重算: PPL_pct = (PPL_2seed - 9.55) / 9.55 * 100; D4_pct = (0.738 - D4_2seed) / 0.738 * 100
  - 如果变化 < 1pp，保留不变

## Step 4: §3.5 Phase Diagram Type III 段 (experiments.tex L147-157)
- L148: `reaching 2573 at Gen~10 ($+$8.7\% above baseline)`
  - 新: 用 2-seed mean 重算
- L149: `$\Delta_t \in [+11, +35]$ for $t \geq 2$; mean $+23.0$`
  - 需验证 2-seed mean 是否改变; 如果变化 <1，保留

## Step 5: Figure 1 caption (experiments.tex L43)
- 旧: `dashed: $r{=}0.5$, single seed`
- 如果图未重绘: 改为 `dashed: $r{=}0.5$, representative seed`
- 如果重绘为 2-seed mean: 改为 `dashed: $r{=}0.5$, 2-seed mean`

## Step 6: Figure 2 caption (experiments.tex L126)
- 旧: `$r{=}0.2$ and $r{=}0.5$: single seed`
- 新: `$r{=}0.2$: single seed; $r{=}0.5$: 2-seed mean` (或 representative seed 如果图未重绘)

## Step 7: Limitations (limitations.tex L5)
- 旧: `$r \in \{0.2, 0.5\}$ each report a single seed`
  (实际文本: `$r{=}0.2$ and $r{=}0.5$ report a single seed` — 需 grep 确认精确文本)
- 新: `$r{=}0.2$ reports a single seed and $r{=}0.5$ two seeds (42, 43)`

## Step 8: Conclusion (conclusion.tex L11)
- 旧: `even at $r = 0.5$, perplexity increases 59\% and D-4 drops 87\%`
- 用 2-seed mean 验证百分比; 如果变化 < 1pp 保留

## Step 9: Abstract (abstract.tex)
- 无直接 r=0.5 数值引用，无需改动

## Step 10: 验证
- [ ] `cd paper && latexmk -pdf main.tex` — 编译通过
- [ ] pdftotext 检查 ≤ 8 页
- [ ] `grep -n "single seed" paper/sections/*.tex` 确认 r=0.5 不再标注为 single seed
- [ ] commit: `[paper] upgrade r=0.5 to 2-seed coverage (exp_018)`

## 遗漏说明 (v1 未覆盖)
- v1 遗漏了 §3.1 (L69, L75) 中的 r=0.5 引用
- v1 遗漏了 §3.5 Type III 段 (L148-149)
- v1 行号全部过时（15+ edits 后偏移 10-20 行）
- 如果 exp_019 也在 exp_018 之前或同时完成，r=0.2 可能升级为 3-seed —— 需要 Director 决策
