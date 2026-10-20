# agent_progress_probe — Research Dashboard

> 最后更新: 2026-05-16 06:56 UTC | 更新原因: D079: Round 6 action plan — Findings track recommended, 5 supp experiments dispatched

## 核心方向
Structural features for real-time LLM agent stagnation monitoring: cross-agent transfer as unique contribution, deployment trade-off framework. 详见 paper_framing.md。

## 当前进展
- **阶段**: Round 6 complete → narrative rewrite pending user track confirmation
- **距 EMNLP ARR DDL**: 9 天 (2026-05-25)
- **评分趋势**: R5 2.75/5 → R6 2.75/5 (fresh, same score = structural ceiling)
- **D079**: Recommend Findings track + gold-centric narrative + 5 supp experiments
- **实验**: 86 DONE, 5 supplementary dispatched (pure computation, <4h)

## Round 6 Action Plan

**补实验（Agent 执行中）**:
- [ ] LF threshold baseline (silver/gold/cross-agent F1)
- [ ] Gold LLM vs GB bootstrap CI + McNemar
- [ ] Residual 19-feature gold eval
- [ ] Conf=1 isolated performance
- [ ] Silver→gold ranking reversal quantification table

**论文修改（待用户确认 track 后 Paper Agent 执行）**:
- [ ] Gold-centric narrative rewrite (abstract/intro)
- [ ] "agent-agnostic" → "SWE-Bench ecosystem transferability"
- [ ] 2-LF results promoted to main text
- [ ] Finding 3 scope limitation
- [ ] Contribution 2 → empirical observation
- [ ] Number repetition reduction
- [ ] "uniquely" → "robustly"
- [ ] Minor fixes (terminology, bib, footnote, quantification)

## 待定决策
- **用户确认 Findings track**（pending）— 确认后立即派 Paper Agent

## GPU 预算
bjb2-23165: cuda:0 + cuda:1（2x RTX 5090）— 空闲，补实验为纯计算不需 GPU

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D079 | 2026-05-16 | Round 6 weak reject 2.75/5: recommend Findings tra | llm-judge-gold-r5, e2-gb-matched-scope |
| D078 | 2026-05-16 | LLM gold 0.910 > GB gold 0.839 confirmed valid; pa | llm-judge-gold-r5, d073-cycle-oh |
| D077 | 2026-05-16 | Round 5 weak reject action plan: reframe headlines | e2-gb-matched-scope, e1-2lf-crossagent, d073-cycle-oh |
| D076 | 2026-05-16 | E5-large cross-agent 0.733 confirms structural adv | d073-probe-e5-large, d073-probe-bge-m3, cross-agent-structural |
| D075 | 2026-05-16 | E5-large multiseed JSON contains fabricated seed 4 | d073-probe-e5-large |
| D074 | 2026-05-16 | Cross-agent transfer confirmed as genuine contribu | d073-cycle-oh, d073-cycle-detector, structural-cross-agent |
| D073 | 2026-05-16 | C3 stays "negative with nuance", not upgrade to co | 6lf-tlm, d073-cycle-detector, gold-3annotator-eval |
| D072 | 2026-05-16 | D074: Dream 2 分析 — best 4/6, median 3.5/6, worst 3 | dream_20260516T021904 |
| D071 | 2026-05-15 | Gold set 使用 Set B (N=505, ≥2 annotators agreed) 作为 | gold-set-eval-v1, gold-3annotator-eval |
| D070 | 2026-05-15 | Gold set framing: dual-report silver+gold, reverse | gold-set-eval-v1 |


