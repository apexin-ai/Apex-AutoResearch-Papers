# contamcal-irt-calibration — Research Dashboard

> 最后更新: 2026-05-23 15:00 UTC | 更新原因: 清理 4 个过时任务，更新为 pre-submission 等待状态

## 核心方向
Controlled SFT injection reveals a spectrum of dose-response patterns (Benefit/Immune/Collapse/V-recovery), not uniform inflation. ContamCal combines multi-signal RRF fusion with contamination-augmented IRT (2PL+γ) for domain-level diagnosis. 详见 paper_framing.md。

## 当前阶段
**Pre-submission → 等待用户 OpenReview 提交**

论文已完成全部技术内容和格式审查，PDF 已生成。提交清单已发送给用户。

### 论文状态
- 21 页（8 页正文 + Limitations + References + Appendix）
- 6 figures, 3 tables, 1 algorithm
- 所有格式检查通过（页数、字体 Type 42、匿名性、abstract ≤200 words）
- AI 写作模式已修复（trailing participial clauses）
- MDES 数值统一为 1.25--2.05pp
- 匿名仓库已推送 (43 files, verified accessible)

### 已完成
- [x] 6 模型 × 5 dosage SFT injection + 3-seed cross-seed evaluation
- [x] Volume control (Falcon3 non-benchmark MCQ)
- [x] DiD item-level memorization test
- [x] Within-family IRT (Qwen2.5, J=16) + domain-level γ_d
- [x] Cross-benchmark transfer (GSM8K, ARC)
- [x] Out-of-sample validation (LLaMA-3.1-8B)
- [x] Signal failure characterization (Min-K\%++ reversal at 0.5B)
- [x] 2-panel Fig 1 (inline annotations) + cross-seed CI forest plot (Fig 5)
- [x] 全部 11 个图表脚本 Type 3→42 字体修复
- [x] 美学升级（统一色板、rcParams、去冗余标注）
- [x] Round 12 内审通过（Reviewer full audit: 1 warning fixed, rest PASS）
- [x] 匿名仓库推送 + 验证

### 待办
- [ ] ⏳ 用户在 OpenReview 提交（DDL 2026-05-25）
- [ ] ⏳ 用户手动填写 ARR Responsible NLP Checklist

## GPU 预算
当前无 GPU 分配（实验全部完成）。

## 投稿信息
- **目标**: EMNLP 2026 via ARR
- **DDL**: 2026-05-25
- **格式**: Long paper, 8-page main text limit

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D220 | 2026-05-23 | Round 13 Action Matrix: 系统性 framing 重写 + S2-remova | — |
| D219 | 2026-05-23 | Volume control Scenario C confirmed: 45% volume /  | sft_falcon3_7b_volume_control |
| D218 | 2026-05-23 | D218: Falcon3 d000 s123 降级为可选；Yi 正式 defer 到 camera | sft_falcon3_7b_d000_s123, sft_yi_1.5_9b |
| D217 | 2026-05-22 | Round 11 审稿响应策略：data quantity control 实验 + 全面文本修复  | sft_falcon3_7b_d100_s123_v2, data_quantity_control_falcon3 |
| D216 | 2026-05-22 | 最终冲刺策略：Tier 1 补全 + Yi gate check + 条件分支 | signals_falcon3_d100_s42_v2 |
| D215 | 2026-05-22 | Falcon3 结果判断标准：任何结果均直接提交 ARR，不再加内审轮次 | sft_falcon3_7b_d000_s42, sft_falcon3_7b_d100_s42 |
| D214 | 2026-05-21 | D214: P(γ<0) 差异根因=不同模型池。Option A: j16_qwen 池重跑 pri | — |
| D213 | 2026-05-21 | D213: Round 10 (3.0 Findings) Action Matrix — P(γ< | — |
| D212 | 2026-05-21 | D212: 参数化 DR 拟合 1/5 一致——framing 为 n=3 统计力限制而非 Algo | — |
| D211 | 2026-05-21 | D211: Round 9 (3.5 Borderline Conference) Action M | — |


