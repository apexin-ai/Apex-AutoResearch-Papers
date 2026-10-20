# solver-trace-ablation — Research Dashboard

> 最后更新: 2026-05-23 02:13 UTC | 更新原因: R33 完成，三轮均 3.0，更新终态评估

## 核心方向
STA (Solver Trace Ablation) 作为 LOO 诊断工具揭示 GRPO 训练的 FOL reasoner 中的结构退化和 seed-dependent Goodhart 效应。详见 paper_framing.md。

## 当前进展
- **阶段**: 论文修复完成，三轮审稿均 3.0 (Findings)，DDL 2026-05-25
- **论文状态**: R31/R32/R33 三轮均 3.0。所有可修改项已完成。结构性限制（单模型 Qwen3-4B / N=3-5 seeds / LOO novelty / taxonomy recall）标记 wont_fix 并附 rebuttal 论点。
- **Review issues**: 21 项中 17 resolved / 4 wont_fix / 0 open
- **Reviewer 评估**: 纯 framing 修改天花板 3.0-3.25；3.5 需新模型实验，DDL 前不可行
- **结论**: 论文已达当前数据下的最优状态，进一步审稿迭代边际收益递减

## R33 修复摘要（commit e7509b6）
- C2 改为 "seed-dependent Goodhart effect"
- "model-agnostic" → "applicable to any solver-verified reasoning system"
- Bimodal 讨论 front-loaded 到 §4.3
- "converts" → "systematically selects for"
- §3.3 加 taxonomy 互斥性规则 + N-H upper bound caveat

## 近期任务
- [ ] 决定是否提交 R34 或视为最终版
- [ ] GPU 释放 westd-39279:cuda:0（已请用户手动处理）

## 已完成
- [x] R31 Must-Fix/Should-Fix/Minor 全部修复
- [x] R32 Action Matrix 6 项完成
- [x] R33 Action Matrix 5 项完成
- [x] C3 conclusion 回响补充
- [x] 全文破折号一致性修复
- [x] Review issues 终态确认（21 项：17 resolved + 4 wont_fix）

## GPU 预算
westd-39279: cuda:0（空闲，已请用户手动释放）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D164 | 2026-05-23 | 跳过 R34 审稿，当前版本视为最终定稿 | — |
| D163 | 2026-05-22 | D169: 停止 8B 系列——K=8 s42 未收敛 (PR=15.9%)，不继续 s43/ISR | d154-8b-exec-s42-k8, d154-8b-exec-s42-k4v2 |
| D162 | 2026-05-22 | D168: 8B 实验序列确定——exec s42→s43→ISR s42（串行+决策门），跳过 K | d154-8b-exec-s42-k8, d154-8b-exec-s43-k8, d154-8b-isr-s42-k8 |
| D161 | 2026-05-22 | D167: 采纳 Reviewer 8B 时间修正 (12-13h/seed) + non-conv | d154-8b-exec-s42-k4v2, d154-8b-exec-s42-k8 |
| D160 | 2026-05-22 | D166: 8B GRPO 改用 K=8 — K=4 已证明 cold-start stagnati | d154-8b-exec-s42-k4v2 |
| D159 | 2026-05-20 | D159: D157 framing 决策——C2 不升级 "mechanistic"，§4.3 加 | d157-shuffled-isr-s42-r3 |
| D158 | 2026-05-20 | D158 终止：LLaMA SFT PR=0%，gate 未通过，不修复。GPU 全给 D157。 | d158-llama-sft-s42, d158-llama-grpo-s42 |
| D157 | 2026-05-20 | D157: R19 Action Matrix — 统计叙事重构 + ISR post-hoc fi | — |
| D156 | 2026-05-20 | R18 Action Matrix: ISR概念修复+component count论证+措辞收紧为 | — |
| D155 | 2026-05-20 | R17 策略：写作修改优先，8B 降为 background。目标 3.5 via W1 scope | — |

