# pgpf-collapse-filter — Research Dashboard

> 最后更新: 2026-05-13 11:56 UTC | 更新原因: Phase 1 RUNNING，更新 ROADMAP 反映真实状态

## 核心方向
Property-Guided Post-training Filtering (PGPF)：用多属性（LC + SN + Confidence）过滤合成数据，缓解递归合成训练中的 model collapse。详见 paper_framing.md。

## 当前阶段
**MVP 验证** — Phase 0 正交性 PASS，Phase 1 核心对比实验 RUNNING。

## 当前进展
- Phase 0 正交性检验 PASS（D002）：4 属性 pairwise |r| < 0.7，LC vs Conf = 0.303。Quality ≈ Confidence（ρ=-0.998），有效属性空间 3 维（LC, SN, Confidence）
- Phase 1 代码经 3 轮 Reviewer 审查修复：retention rate 对等（rank-based top-k）、属性 key 匹配、LC 方向一致性
- Phase 1 (phase1_gate_check) 已 RUNNING：5 条件 × 3 代 × seed=42，Qwen2.5-1.5B + OpenHermes，autodl-pgpf cuda:0+cuda:1
- 预计 10-12h 墙钟时间完成（~15-20 GPU-hours）

## 近期任务
- [ ] 等待 Phase 1 完成，分析 gate check 结果（预计 ~2026-05-14 凌晨）
- [ ] Phase 1 PASS → complete_mvp() 进入 research 阶段，写 paper_framing.md + experiment_plan.yaml
- [ ] Phase 1 FAIL → 分析失败原因，评估是否调整属性权重/过滤策略/换模型
- [ ] LC TF-IDF 正交性验证脚本已写好未执行（不阻塞 Phase 1，结果出来后补跑）

## GPU 预算
- autodl-pgpf：2× RTX PRO 6000 96GB（cuda:0, cuda:1）
- 当前占用：2/2（phase1_gate_check RUNNING）

## MVP Gate 条件
1. ✅ Phase 0：属性正交性 |r| < 0.7 → PASS
2. ⏳ Phase 1：(a) NoFilter 退化 ≥ 5% (b) PGPF-S vs Conf-only 相对改善 ≥ 5% (c) PGPF-S < Random
3. Phase 1 PASS → MVP 完成，进入 research 阶段

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D001 | 2026-05-13 | 放弃 EMNLP 2026 ARR May 25，重定向至 AAAI 2027（abstract J | — |



