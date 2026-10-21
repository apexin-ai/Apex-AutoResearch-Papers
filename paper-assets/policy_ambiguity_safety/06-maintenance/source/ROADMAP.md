# policy_ambiguity_safety — Research Dashboard

> 最后更新: 2026-05-24 00:04 UTC | 更新原因: Fix Fisher p-value (10⁻⁷→10⁻⁶) and timeline (~44h→~24h) per Reviewer audit

> 核心方向详见 paper_framing.md

## 核心方向
首个因果性、type-granular 研究，证明 policy ambiguity 导致 LLM agent 安全违规。Matched-pair 设计 + perturbation control + 7 模型 × 6 type taxonomy。

## 当前进展
- **阶段**: Pre-submission — acceptance-readiness 修复全部完成，等 κ 重标注
- **DDL**: EMNLP 2026 ARR May cycle — **2026-05-25**（~24h）
- **目标**: 4.0 Conference（Reviewer 评估：稳固 3.5，κ 解决后有 4.0 潜力）
- **页面**: 8 页正文 verified（25 pages total with appendix）
- **编译**: PASS，无 critical warnings
- **注意**: κ 未完成也可以当前状态提交（3.5 水平）——κ 改善是提分机会，不是 blocker

## 已完成的提分工作
1. R28 全部 16 issue resolved
2. Pre-submission hardening: appendix 术语、limitations 补充、discussion v2 worsening
3. Writing quality pass: convergent nocuity 命名、"initial evidence" 升级、Discussion 深度
4. 温度 pilot: GPT-4.1 × 50 pairs, temp=0.7 robust (+27.6pp vs +28.0pp, mod+crit threshold)
5. AI 辅助披露 Appendix AH
6. Discussion sycophancy 对比锐化
7. κ contingency 预案预写（3 scenario × 7 positions）
8. Acceptance-readiness fixes (243ff7c): B1 coreferential 措辞统一 + confound-minimized + B2 SOPBench Fisher combined test (p<10⁻⁶)

## 剩余工作
- [ ] κ 重标注：用户 5/24 找标注者，目标 κ 0.15 → 0.4+
- [ ] κ 成功后更新 7 处数据 + B3 bridge sentence
- [ ] 最终 compile + push to anonymous repo（需用户提供 credentials）

## GPU 预算
本项目 0 GPU（全 API 实验）。实验阶段已结束。

## 关键发现
1. C1: +34.0pp binary effect (OR=15.1), excluding-incompleteness +31.0pp [27.9, 34.1]
2. C2: Type→mechanism NMI=0.23 vs type→rate NMI=0.01
3. SOPBench 跨 benchmark +12.7pp (all 5 Δ>0, 3/5 significant, Fisher combined p<10⁻⁶)
4. Convergent Nocuity: 41.3% convergent, cross-family Jaccard 0.46 vs within-family 0.54
5. Disambiguation Neglect: 4.6% awareness, 95.4% neglect
6. v2 mitigation worsens incompleteness +14pp
7. Temperature robustness: +27.6pp at t=0.7 (SD=3.3) vs +28.0pp at t=0, 89% unanimous, 97% agreement

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D027 | 2026-05-22 | Round 14: Taxonomy repositioned as intervention de | plan_004, plan_005, dream_20260522T111643 |
| D026 | 2026-05-22 | 启动 plan_016 type-specific mitigation 实验 + inter-mo | plan_016, inter_model_nocuity |
| D025 | 2026-05-20 | C群审稿3.0处理: C2 robustness analyses dispatched, C3 → | — |
| D024 | 2026-05-20 | 5-model analysis complete: C3 downgraded (Δ=6.08pp | plan_002, plan_002c, plan_003a, plan_003b, plan_004 |
| D023 | 2026-05-20 | τ²-bench 还原 + GPU 消除 + 5 模型 API-only 方案确定 | plan_003, plan_002 |
| D022 | 2026-05-20 | Round 1 审稿报告 3.5 Action Matrix 定稿 + Paper Agent Fu | plan_002, plan_005, plan_006, plan_010 |
| D021 | 2026-05-20 | Dream review 3.5 analyzed: 3 systemic issues ident | plan_002, plan_005, plan_006 |
| D020 | 2026-05-20 | Major framing pivot: "Uniform Nocuity" → "Differen | plan_002, mvp_001 |
| D019 | 2026-05-20 | plan_010 v2 PASS (real data): Δ_perturb=3.33pp, CI | plan_010, plan_002 |
| D018 | 2026-05-20 | plan_010 PASS (Δ_perturb=0pp, verdict=PASS), plan_ | plan_010, plan_002 |











