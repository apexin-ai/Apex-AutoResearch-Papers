# causal_style_decomp_judge — Research Dashboard

> 最后更新: 2026-05-25 09:19 UTC | 更新原因: 匿名仓库 push 完成 (808123f)，数字修复+Table2+附录引用全部验证通过，进入等待审稿状态

> 核心方向: Likert Blindspot + Per-axis confound decomposition. 详见 paper_framing.md。

## Score Trajectory
R1: 2.5 → R2-R4: 3.0 → R5-R10: 3.5 → R11-R16: 3.5 → R17: 3.5 → Target: **4.0 (Conference)**

## 当前阶段：论文已提交（May 25 AoE），等待审稿

### 论文状态
- 正文 8 页合规，20 页总计（含 Appendix）
- 无 critical warnings，无 undefined references
- Table 1 全 14 行经可复现脚本验证（Reviewer 独立确认）
- Table 2 overfull hbox 已修复（resizebox）
- 附录 27/27 有正文引用（修复 app:nli_ablation）
- 数字一致性审计通过（5 处修正，Reviewer 独立验证 PASS）
- 匿名仓库已同步 push（commit 808123f, public）
- OpenReview 提交由运维人工完成

### Rebuttal 备弹（全部完成）
- [x] formality_scaled_n300: Llama-70B n=355, BT=72.5%, Likert d=0.048 p=.026。大样本下 Likert 终于 sig 但 d 极小 → 结构性 attenuation 确认
- [x] formality_llama_rewriter: Llama-70B rewriter, BT=71.1%, Blindspot YES。3 独立 rewriter 排除 rewriter artifact
- [x] llama70b_crossbench: AlpacaEval formality BT=95.7%, verbosity BT=97.0%; MT-Bench formality BT=91.7%。全部 Likert sig (d=0.21-0.30) → Blindspot 在大效应下消失，验证 effect-size gradient
- [x] GPT-5.4 NO-GO（D081）

### 待做
- [ ] 等待审稿结果（预计 4-6 周）
- [ ] 审稿回来后根据 reviewer concerns 制定 rebuttal 策略

## GPU 预算
westb-29275: 4×RTX PRO 6000 96GB。全部实验完成，已通知 Manager GPU 可供全局调度。

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D081 | 2026-05-23 | NO-GO: Keep GPT-4o, do not replace with GPT-5.4 | D080 |
| D080 | 2026-05-23 | GPT-5.4 替换 GPT-4o：T-20h go/no-go contingency plan  | — |
| D079 | 2026-05-23 | R17→R18 comprehensive patch：6 MF + 5 SF + 9 minor  | — |
| D078 | 2026-05-23 | D078: 用现有数据做 construct divergence adjudication（non | — |
| D077 | 2026-05-23 | R17 提交：100-pair 标注整合(precision=98.6%, AC₁=0.96) +  | — |
| D076 | 2026-05-23 | FK Sobel 数值修正：z=3.36/p<.001 改为 z=1.93/p=.053 + β r | — |
| D075 | 2026-05-23 | R15 Action Matrix 锁定：MF1 结构性修改 + MF2 convergent ev | — |
| D074 | 2026-05-23 | D074: Claude narrative 升级——formality negative cont | claude_crossbenchmark |
| D073 | 2026-05-23 | D073: Claude negative control 限定为 LLMBar only，cros | claude_crossbenchmark |
| D072 | 2026-05-22 | D072: R14 Action Matrix 定稿——MF1 "diagnostic method | all_54 |






