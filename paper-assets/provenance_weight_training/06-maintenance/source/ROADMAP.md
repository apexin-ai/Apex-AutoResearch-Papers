# provenance_weight_training — Research Dashboard

> 最后更新: 2026-05-25 UTC | 更新原因: 编译核实 + 未勾选项清理

## 核心方向
**Analysis paper**: "When, why, and how does detect-and-reweight work?"
贡献排序: (1) Epoch confound >95% (2) Detector requirements: calibration+discrimination (3) Mechanism decomposition: minimum intervention > maximization (4) Adaptive b* tool。详见 paper_framing.md (D115)。

## 当前阶段
**Round 13 响应中。** DDL: **EMNLP 2026 ARR May 25**。

Round 13 fresh review: **3.0 (Findings)**。核心瓶颈（N=3 BH 不显著）**已解决**。
N=5 seeds 完成：**p_BH = 0.011 < 0.05 ✓**。剩余：random-subset baseline + 论文更新。

## 近期任务
- [x] **N=5 seeds 训练** — 5 seeds × adaptive/uniform 全部 DONE
- [x] **N=5 统计量** — Δ=-0.023±0.006, t(4)=-8.21, p=0.0012, p_BH=0.011 ✓ (Reviewer 独立验证 PASS)
- [x] **Figure CRITICAL 修复** — Fig 2 + Fig 4 已完成并通过审查 (04:58 UTC)
- [x] **论文更新 N=5 统计量** — results.tex 已反映 5-seed 数据 (p_BH=0.011) ✓
- [x] **Random-subset multi-epoch baseline** — random_subset_epoch_seed42 DONE, holdout_ppl=17.694 = uniform ✓
- [x] OOD eval (OWT/Wiki) adaptive seeds — adaptive_ood_seed123/456 + uniform_ood_seed123/456 全部 DONE，results.tex 已写入 ✓
- [x] ρ=0.6 p 值标注 — 正文报 p_BH=0.064（BH 校正后），附录补 uncorrected p=0.010，呈现合理 ✓
- [x] 标题加 "Self-Contaminated" [Paper Agent ✅]
- [x] 删除 "practical corollary" → "engineering demonstration" [Paper Agent ✅]
- [x] 删除 B^0.89 power law → monotonic trend [Paper Agent ✅]
- [x] 补引用 RAID/M4/Phi/Owen [Paper Agent ✅]
- [x] §6 精简 + α_eff proxy theory gap [Paper Agent ✅]
- [x] B=4 SD ±0.008→±0.006 [Agent ✅]
- [x] appendix "~2%"→"~6%" 修正 [Agent ✅]
- [x] "variance"→"standard deviation" 修正 [Agent ✅]

## 关键数据速查
| 指标 | 值 |
|------|-----|
| **Δ(B=4, ρ=0.4, N=5)** | **−0.023±0.006 (p=0.0012, p_BH=0.011) ✓** |
| Δ(B=8, ρ=0.4, 3-seed) | −0.052±0.007 (p=0.006, 2.6×) |
| Δ(B=16, ρ=0.4, 3-seed) | −0.068±0.005 (p<0.01, 3.4×) |
| Δ(ρ=0.6, 3-seed) | −0.032 (p=0.010, uncorrected) |

## GPU 预算
4× RTX PRO 6000 96GB on westd-41312 — **0/4 在跑，4 空闲待分配**

## 审稿历史
Round 8: 2.5 → Round 9: 3.0 → Round 10: 3.0 → Round 12: 3.0 → **Round 13: 3.0** → 修复中

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D130 | 2026-05-24 | Round 13 响应：补 N=5 seeds + random-subset baseline + | — |
| D129 | 2026-05-24 | α_eff 定义从 binary indicator 改为 continuous (1-q_i)，对 | adaptive_fix_seed42 |
| D128 | 2026-05-23 | 保持 Bonferroni-Holm k=9 校正方法不变，BH k=5 作为 rebuttal 备 | bs8_nmin4_adaptive_seed456_r2 |
| D127 | 2026-05-23 | α_eff-only ablation 2-seed 数据写入论文，确认双约束交互效应 | aeff_only_nmin1_seed42, aeff_only_nmin1_seed123, nmin1_seed42 |
| D126 | 2026-05-23 | α_eff-only ablation 呈现策略：inline 扩展 results.tex:120 | — |
| D125 | 2026-05-23 | Claim 强度决策：维持 "majority" 不升级 "dominates"，数据修正后 sto | — |
| D124 | 2026-05-23 | R12 Action Matrix: P0 format fixes (abstract/pages | — |
| D123 | 2026-05-23 | R11 Action Matrix 定稿：P0 overclaim fix + P1 power a | — |
| D122 | 2026-05-23 | D122: 预跑 B=8 seed123 补强 batch-size amplification c | bs8_nmin4_adaptive_seed42, bs8_nmin4_uniform_seed42 |
| D121 | 2026-05-23 | D121: ρ=0.3 boundary check 确认 transition boundary  | rho03_adaptive_seed42, rho03_uniform_seed42, rho03_adaptive_seed123, rho03_uniform_seed123 |





