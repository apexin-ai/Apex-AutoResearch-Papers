# importance_margin_vla_compress — Research Dashboard

> 最后更新: 2026-05-28 14:44 UTC | 更新原因: 数据验证通过，ROADMAP 精简为 submission-ready 状态

> 详见 paper_framing.md。

## 核心方向
VLA vision token compressibility: **scoring method × connector × task 三维交互**。5+ 模型 × 4 LIBERO suites。

## 当前阶段
✅ **π0.5 Cliff Curve 18/18 完成**
✅ **OpenVLA Long Curve 18/18 完成** (D288)
✅ **Crossover table 16/16 完成**
✅ **Abstract 已提交** (May 26)
✅ **Narrative 定稿** (D276)
✅ **Importance Margin Inverted-U 6/6 全闭合** (D291)
✅ **Attn cliff+plateau 全 6 点闭合** (D290)
✅ **5-seed 90/90 cell 零缺失，数据验证通过** (May 28)
✅ **Figures 已在前序轮次生成完毕**

## Deadlines
- **CoRL 2026 Paper**: May 29

## 🏁 π0.5 LIBERO-Long 最终汇总表 (5-seed, sample std n-1)

| k | L2norm (mean±std) | n | Random (mean±std) | n | Attn (mean±std) | n | Margin L2-Rand |
|---|-------------------|---|-------------------|---|-----------------|---|----------------|
| 0.95 | **86.8±0.8** | 5 | **61.2±0.7** | 5 | **77.3±1.2** | 5 | **+25.6pp** |
| 0.9 | **80.4±0.5** | 5 | **33.6±1.2** | 5 | **64.2±1.0** | 5 | **+46.9pp** ⭐peak |
| 0.85 | **78.1±1.0** | 5 | **44.9±1.3** | 5 | **50.8±1.3** | 5 | **+33.2pp** |
| 0.75 | **70.6±2.7** | 5 | **63.0±1.7** | 5 | **51.4±1.2** | 5 | **+7.6pp** |
| 0.7 | **63.2±1.5** | 5 | **64.6±1.8** | 5 | **53.0±1.1** | 5 | **-1.4pp** 🔄cross |
| 0.5 | **51.7±1.5** | 5 | **50.4±0.6** | 5 | **49.4±1.5** | 5 | **+1.3pp** ≈0 |

数据来源: s42-s43 硬编码验证值(42cell) + s44-s46 registry提取(47cell) + build_5seed_tables.py 交叉验证。

## 待处理
- [x] 5-seed 数据验证 (build_5seed_tables.py) — ✅ 90/90 一致
- [x] Figures 生成 — ✅ 前序轮次已完成
- [x] Paper Agent submission 准备 — ✅ 已完成

## GPU 分配
14 张 GPU (4 servers)。实验硬截止已过，仅 w38 跑 s47 bonus seeds（revision 备用）。

## 数据整合注意事项（全部已处理）
- [x] Attn k=0.75 seed43: cqa1=52.0%
- [x] Attn k=0.75 seed42: w41 strict=49.8%
- [x] Random k=0.9 seed43: w41 strict=35.0% (D292)
- [x] metrics格式: 统一百分比
- [x] OV Attn k=0.75: v3=34.2%
- [x] Random k=0.85 s43: strict_w27=47.2%
- [x] Attn k=0.7 seed42: w41=53.6%

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D302 | 2026-05-29 | attn k=0.95 s47 放弃，不再重试。5-seed mean=77.3±1.2 已足够 | eval_pi05_attn_k095_long_seed47_cqa1 |
| D301 | 2026-05-28 | 论文 error bar 标准确定：统一用 sample std (n-1)。L2norm k=0. | eval_pi05_l2norm_k075_long_seed45_strict |
| D300 | 2026-05-28 | Attn k=0.7 s44 溯源完成：数据有效，keep=179/256 确认 k=0.7。SR  | eval_pi05_attn_k07_long_seed44_strict_cqa1 |
| D299 | 2026-05-28 | L2norm k=0.75 四 seed: 70.8/73.2/67.4/68.4%, mean=7 | eval_pi05_l2norm_k075_long_seed45_strict |
| D298 | 2026-05-28 | ⚠️ k=0.7 量化异常：Attn k=0.7 s44 日志显示 keep=192(=k=0.75 | eval_pi05_attn_k07_long_seed44_strict |
| D297 | 2026-05-28 | Random k=0.5 三 seed: 49.8/51.4/50.2%, mean=50.5%±0 | eval_pi05_random_k05_long_seed44_strict_cqa1 |
| D296 | 2026-05-28 | Attn k=0.5 三 seed 完成: 52.0/48.8/48.8%, mean=49.9%± | eval_pi05_attn_k05_long_seed44_strict |
| D295 | 2026-05-28 | L2norm k=0.95 三 seed 完成: 85.8/86.2/86.8%, mean=86. | eval_pi05_l2norm_k095_long_seed44_strict_cqa1 |
| D294 | 2026-05-27 | L2norm k=0.9 三 seed: 80.0/81.2/80.4%, mean=80.5%±0 | eval_pi05_l2norm_k09_long_seed44_strict_cqa1 |
| D293 | 2026-05-27 | Attn k=0.75 s43 跨服务器：w27v2=49.0% vs cqa1=52.0%（Δ=3 | eval_pi05_attn_k075_long_seed43_strict_cqa1 |

