# cert_manip_resist_eval — Research Dashboard

> 最后更新: 2026-05-25 23:06 UTC | 更新原因: D048 R8 Action Matrix 派发 Paper Agent 执行，叙事从 predictor shift 重新定位为 η_max diminishing + K_eff stable

## 核心方向
Multi-judge LLM evaluation panels: diversity positively associated with vulnerability (K_eff pooled β̂_std 0.286–0.353, CI excludes zero), with η_max predictive power diminishing as panel size grows (WCB 5→0→1) while K_eff remains consistently strong (WCB 8→8→7). 详见 paper_framing.md v9.

## 当前阶段
**D048: R8 审稿报告 Action Matrix 执行中**。R8 Overall 3.0 (Findings)，目标 3.5+。Paper Agent 正在执行全套修改：MF1 Contribution 结构性重写 + MF2 pooled β̂_std 替代 vote counts + MF3 全文因果语言清理 + 9 项 Should-Fix + 6 篇缺失引用 + 页数压缩。叙事从 "predictor shift (4→7→8)" 重新定位为 "η_max diminishing + K_eff stable (8→8→7)"。

## V2 可审计数据定稿（D047 修正后）

| K | K_eff WCB (majority) | η_max WCB (majority) | Threshold R² | Bayesian R² | Majority R² |
|---|---|---|---|---|---|
| 3 | 8/12 | 5/12 | 0.745 | 0.136 | 0.349 |
| 5 | 8/12 | 0/12 | — | — | — |
| 7 | 7/12 | 1/12 | — | — | — |

- K_eff WCB: 8→8→7（高位稳定，K=7 轻微下降）
- η_max WCB: 5→0→1（K=5 处急剧衰减至零，K=7 微弱恢复）
- Position bias: 10/12 conditions positive（2 exceptions explained）

## 近期任务
- [x] D047: 全文数据修正 + 图表重画 + 一致性验证
- [x] fig_keff_eta_scatter 修复（caption 矛盾 + Pool A + log-space r）
- [ ] **D048: R8 Action Matrix（Paper Agent 执行中）**
  - [ ] Phase 1: 压缩腾空间（Prop 1 降级、§5.3/§5.4 移 appendix、Limitations 压缩）
  - [ ] Phase 2: MF1-3（Contribution 重写、pooled β̂_std、因果语言清理）
  - [ ] Phase 3: SF1-9（K_eff 改名、AWQ 讨论、fractional logit co-primary 等）
  - [ ] Phase 4-5: 补引用 + 编译验证 ≤8 页
- [ ] Reviewer 验证 MF1-3 修改
- [ ] 决定是否提交 R9 审稿 / 跑 Dream Review

## GPU 预算
seetacloud-rtx6000 (port 25392): 1x RTX PRO 6000 Blackwell 98GB。当前无 GPU 需求（论文修改阶段）。

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D048 | 2026-05-25 | D048: R8 审稿报告 Action Matrix——reframe predictor shi | plan001_step1_full_v4 |
| D047 | 2026-05-25 | D047: Position bias bug 修复后修订叙事——"12/12 uniformly  | plan001_step1_full_v4 |
| D046 | 2026-05-25 | 合成数据验证后修正 D045：predictor shift 从 CRITICAL artifact | synthetic_data_validation, kappa_diversity_replacement |
| D045 | 2026-05-25 | Predictor shift 确认为 metric-specific artifact，核心叙事从 | kappa_diversity_replacement |
| D044 | 2026-05-24 | MF1 策略转向：K_eff 从 "Gaussian copula 理论支撑" 改为 "操作性启发式 | r4-a2-gaussian-copula-gof, r4-a3-mi-plugin-vs-closedform |
| D043 | 2026-05-24 | D043: K=7 V2 bootstrap 确认 Majority K_eff=8/12。全量可审 | plan001_step1_full_v4 |
| D042 | 2026-05-24 | D042: K=7 K_eff=9/12 也来自被废弃的 regime_transition_cor | plan001_step1_full_v4 |
| D041 | 2026-05-24 | D041: 弃用 regime_transition_corrected.json (K_eff=1 | plan001_step1_full_v4 |
| D040 | 2026-05-24 | D040: 最终确认 V2 K=5 聚合为 uniform K_eff=7/12，撤销 D039 恢 | — |
| D039 | 2026-05-24 | D039: 撤回 D038——V2 确认 Bayesian K_eff=0/12，neutraliz | — |


