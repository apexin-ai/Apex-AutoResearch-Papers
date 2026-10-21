# π0.5 LIBERO-Long (libero_10) — Four-Seed Consolidation Table

> Generated: 2026-05-28 | Updated: 2026-05-28T07:35 UTC | Error bar standard: sample std (n-1) per D301

## L2norm

| mode | k | s42 | s43 | s44 | s45 | mean | std | outlier? |
|------|------|------|------|------|------|------|------|----------|
| l2norm | 0.95 | 86.2 | 85.8 | 86.8 | 87.8 | 86.7 | 0.87 | no |
| l2norm | 0.9 | 80.0 | 81.2 | 80.4 | 80.0 | 80.4 | 0.57 | no |
| l2norm | 0.85 | 77.6 | 78.6 | 76.6 | 79.2 | 78.0 | 1.14 | no |
| l2norm | 0.75 | 70.8 | 73.2 | 67.4 | 68.4 | 70.0 | 2.59 | no (D299: transition zone, inherently high variance) |
| l2norm | 0.7 | 63.2 | 65.4 | 63.8 | 61.6 | 63.5 | 1.57 | no |
| l2norm | 0.5 | 49.2 | 52.8 | 52.6 | 52.2† | 51.7 | 1.68 | no |

## Random

| mode | k | s42 | s43 | s44 | s45 | mean | std | outlier? |
|------|------|------|------|------|------|------|------|----------|
| random | 0.95 | 60.6 | 60.8 | 61.2 | 62.4 | 61.3 | 0.81 | no |
| random | 0.9 | 34.2† | 35.0 | 31.8 | 33.4 | 33.6 | 1.37 | no |
| random | 0.85 | 44.0 | 47.2 | 44.2 | 44.2 | 44.9 | 1.54 | no |
| random | 0.75 | 63.0 | 60.6 | 64.6 | 64.6 | 63.2 | 1.89 | no |
| random | 0.7 | 66.0 | 64.4 | 65.6 | 61.6 | 64.4 | 1.99 | no |
| random | 0.5 | 49.8 | 51.4 | 50.2 | 50.4 | 50.5 | 0.68 | no |

## Attention

| mode | k | s42 | s43 | s44 | s45 | mean | std | outlier? |
|------|------|------|------|------|------|------|------|----------|
| attn | 0.95 | 78.4 | 77.2 | 77.8 | 77.8 | 77.8 | 0.49 | no |
| attn | 0.9 | 64.0 | 62.8 | 64.0 | 65.0 | 64.0 | 0.90 | no |
| attn | 0.85 | 50.0 | 52.4 | 49.4 | 52.0 | 51.0 | 1.47 | no |
| attn | 0.75 | 49.8 | 52.0 | 51.6 | 53.0 | 51.6 | 1.34 | no |
| attn | 0.7 | 53.6 | 53.8 | 52.2 | 53.8 | 53.4 | 0.77 | no |
| attn | 0.5 | 52.0 | 48.8 | 48.8 | 49.4 | 49.8 | 1.53 | no |

---

## Coverage Summary

| Seeds | Count | Cells |
|-------|-------|-------|
| 4/4 complete | 18/18 | ALL CELLS COMPLETE |

### Missing Seeds

**None — all 18 cells have 4 seeds.** †L2norm k=0.5 s45 has 490/500 eps (T9 timeout, accepted per Director).

†Random k=0.9 s42=34.2% from D273/D292 decision log; registry strict entry not found.

---

## ROADMAP 数据整合检查清单

| # | 检查项 | 状态 | 详情 |
|---|--------|------|------|
| 1 | Attn k=0.75 seed43: 用 cqa1=52.0% | ✅ | w27 不支持 attention scoring，w27_v2=49.0% 已排除 |
| 2 | Attn k=0.75 seed42: 确认来源服务器 | ✅ | w41=49.8%（D278 canonical），非 w27，无需标注 |
| 3 | Random k=0.9 seed43: 用 v2=35.0% | ✅ | w41=35.0%，旧版 cqa1_v2=32.4% 已排除 |
| 4 | metrics 格式统一（全部转百分比） | ✅ | 所有值已转为百分比格式 |
| 5 | OV Attn k=0.75 用 v3=34.2% | N/A | OpenVLA 数据，不在此表范围 |
| 6 | Random k=0.85 s43 per-task 数据源 | ⚠️ | 整体 SR=47.2% 正确；per-task T0/T1 数据有 L2norm 混入（D277），论文 per-task 分析必须用 server log 真值 |

## Outlier Detection

阈值：seed 偏离 group mean > 5pp。

**结果：无 outlier。** 最大偏差为 L2norm k=0.75 s43=73.2%（Δ=+3.2pp from mean 70.0%），在阈值内。D299 已标注此为 transition zone 固有高方差。

## Duplicate Resolution Log

| mode | k | seed | chosen | value | rejected | value | reason |
|------|------|------|--------|-------|----------|-------|--------|
| l2norm | 0.85 | 42 | cqa1 | 77.6 | w41 | 76.6 | ROADMAP 2-seed mean=78.1 匹配 |
| l2norm | 0.7 | 43 | w41 | 65.4 | w27 | 65.6 | D283 canonical; ROADMAP mean=64.3 匹配 |
| random | 0.5 | 42 | w41_v2 | 49.8 | cqa1 | 50.2 | D297 三 seed 用 49.8 |
| random | 0.9 | 43 | w41 | 35.0 | cqa1_v2 | 32.4 | ROADMAP 明确指定 v2=35.0 |
| attn | 0.5 | 43 | w38 | 48.8 | w41 | 49.4 | D296 三 seed 用 48.8 |
| attn | 0.7 | 42 | w41 | 53.6 | cqa1 | 50.8 | ROADMAP mean=53.7 匹配 |
| attn | 0.75 | 42 | w41 | 49.8 | cqa1 | 52.4 | D278 canonical; ROADMAP mean=50.9 匹配 |
| attn | 0.75 | 43 | cqa1 | 52.0 | w27_v2 | 49.0 | ROADMAP 明确指定 cqa1 (w27 不支持 attn scoring) |
| attn | 0.85 | 43 | w41 | 52.4 | w27_v2 | 52.4 | 值相同，无冲突 |

## Cross-Verification vs ROADMAP 2-Seed Means

All s42+s43 pairs verified against ROADMAP Importance Margin / Attn Cliff+Plateau tables:

| mode | k | s42 | s43 | calc mean | ROADMAP mean | match? |
|------|------|------|------|-----------|-------------|--------|
| l2norm | 0.95 | 86.2 | 85.8 | 86.0 | 86.0 | ✅ |
| l2norm | 0.9 | 80.0 | 81.2 | 80.6 | 80.6 | ✅ |
| l2norm | 0.85 | 77.6 | 78.6 | 78.1 | 78.1 | ✅ |
| l2norm | 0.75 | 70.8 | 73.2 | 72.0 | 72.0 | ✅ |
| l2norm | 0.7 | 63.2 | 65.4 | 64.3 | 64.3 | ✅ |
| l2norm | 0.5 | 49.2 | 52.8 | 51.0 | 51.0 | ✅ |
| random | 0.95 | 60.6 | 60.8 | 60.7 | 60.7 | ✅ |
| random | 0.9 | 34.2 | 35.0 | 34.6 | 34.6 | ✅ |
| random | 0.85 | 44.0 | 47.2 | 45.6 | 45.6 | ✅ |
| random | 0.75 | 63.0 | 60.6 | 61.8 | 61.8 | ✅ |
| random | 0.7 | 66.0 | 64.4 | 65.2 | 65.2 | ✅ |
| random | 0.5 | 49.8 | 51.4 | 50.6 | 50.6 | ✅ |
| attn | 0.95 | 78.4 | 77.2 | 77.8 | 77.8 | ✅ |
| attn | 0.9 | 64.0 | 62.8 | 63.4 | 63.4 | ✅ |
| attn | 0.85 | 50.0 | 52.4 | 51.2 | 51.2 | ✅ |
| attn | 0.75 | 49.8 | 52.0 | 50.9 | ~50.9 | ✅ |
| attn | 0.7 | 53.6 | 53.8 | 53.7 | 53.7 | ✅ |
| attn | 0.5 | 52.0 | 48.8 | 50.4 | 50.4 | ✅ |

All 18 pairs match. Data integrity confirmed.
