# Post-exp_016 Integration Checklist

> exp_016 (r=0.3 seed44) 完成后，30 min 内完成以下全部操作。

## Step 1: 数据收集 (5 min)
- [ ] SSH 到 rtx6000-diagprobe，确认 exp_016 results JSON 完整 (Gen 0-10)
- [ ] 运行 `python scripts/collect_phase_table_stats.py --ratio 0.3 --seeds 42 43 44`
- [ ] 记录输出：SLV mean±sd, eff_rank mean±sd, PPL mean±sd, D-4 mean±sd, σ₁ mean±sd, CV, max_Δt, EMA violations

## Step 2: Table 3 更新 (5 min)
- [ ] `experiments.tex` L177: 替换 r=0.3 行数字（当前为 2-seed mean: 2509.7 / 521.2 / 13.34 / .232 / 0）
- [ ] `experiments.tex` L181 (caption): `$r{=}0.3$ the mean of two seeds` → `$r{=}0.3$ the mean of three seeds (42, 43, 44)`

## Step 3: 正文更新 (5 min)
- [ ] `experiments.tex` L148: `SLV expands monotonically from Gen~2 to 2509.7 at Gen~10 ($+$6.0\%)` — 更新 2509.7 和 6.0% 为 3-seed mean
- [ ] `experiments.tex` L150: `Under a second seed, the individual EMA-smoothed sequence shows a transient violation of 0.83~points at Gen~2` — 改为 "Under additional seeds" 或类似表述
- [ ] `experiments.tex` L161: `$r{=}0.3$ (s.d.\ $= 0.156$ vs.\ SLV s.d.\ $= 2.0$` — 更新为 3-seed s.d.

## Step 4: Abstract 更新 (2 min)
- [ ] `abstract.tex` L5: `across two random seeds` → `across three random seeds`

## Step 5: Limitations 更新 (2 min)
- [ ] `limitations.tex` L5: `$r{=}0.3$ (two seeds)` → `$r{=}0.3$ (three seeds)`

## Step 6: Response letter 更新 (3 min)
- [ ] R1-W2 表格: r=0.3 row — 填入 SLV CV
- [ ] R1-N2: 确认 3-seed 表述一致

## Step 7: 验证 (5 min)
- [ ] `cd paper && latexmk -pdf main.tex` — 编译通过
- [ ] 检查 PDF ≤ 8 页
- [ ] grep 残留 "two seeds" / "two random seeds" / "2-seed" 确认无遗漏
- [ ] commit + push

## Step 8: exp_018 启动 (5 min)
- [ ] cuda:0 释放后立即启动 exp_018 (r=0.5 seed43)

## 当前已知 2-seed 数据 (exp_008 + exp_012)
用于与 3-seed 结果交叉验证：
- SLV: 2509.7 ± 2.0 (seed42=2511.13, seed43=2508.33)
- eff_rank: 521.2 ± 0.0 (seed42=521.26, seed43=521.19)
- PPL: 13.34 ± 0.05 (seed42=13.377, seed43=13.306)
- D-4: 0.232 ± 0.156 (seed42=0.3422, seed43=0.1217)
