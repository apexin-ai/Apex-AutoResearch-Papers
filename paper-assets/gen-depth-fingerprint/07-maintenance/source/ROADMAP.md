# gen-depth-fingerprint — Research Dashboard

> 最后更新: 2026-05-22 22:11 UTC | 更新原因: v55+ 全部改进完成，论文就绪等用户批准审稿轮

> 详见 paper_framing.md

## 核心方向
递归 LLM 生成链展现 **differential depth response (DDR)**：central-tendency/diversity 特征随深度漂移，shape 特征近稳态。7-feature ensemble 跨 8 generators / 5 families / 3 prompt types / 4 domains 验证。**Primary metric: LOGO binary F1=0.694 (leak-free); end-to-end QLoRA: 0.905。**

## 投稿目标
- **主投: EMNLP 2026 ARR (DDL: 2026-05-25)** — 3 天后
- **审稿评分轨迹**: R29=2.5 → R32=3.0 → R34=3.0 → R39=3.0 → R40=3.5 → R45=3.5 → R47=3.0 → R48 修复完成(v55+)
- **Reviewer 预估**: v55+ 应恢复 3.5 (Borderline Conference)

## 当前进展
- **阶段**: 论文就绪，等待用户批准最终审稿轮
- **48 个成功实验**（68 total, 77% success rate）
- **v55+ 改进（本 session）**:
  - R48 全部 4 critical + warnings resolved ✅
  - R44-N1 Two-way ANOVA (generator η²<1%) ✅
  - Figure 1 替换为 PaperBanana framework 图 ✅
  - Discussion 压缩为 1 段 + ANOVA ≥50× ratio 显式量化 ✅
  - §4.3 自贬表述修正 → cost-efficiency framing ✅
  - Conclusion 扩展为 2 句（+batch contamination utility）✅
  - Contribution 3 scope 扩展 + 14B exploratory evidence ✅
  - R48-W8 concurrent methods 不可直接对比说明 ✅
  - Granger causality appendix 引用补回 ✅
  - Camera-ready 审查: 数字全匹配、叙事一致、0 undefined refs ✅
- **review_issues.yaml**: 全部 closed

## 近期任务
- [ ] 最终审稿轮 — 已提交待用户批准 (continue mode)，催了 3 次
- [ ] 审稿反馈后最终修复
- [x] Framework 图 — PaperBanana 版已集成（默认方案）✅
- [x] R48-W8 concurrent methods 写作修复 ✅
- [x] Claim 强度最大化（≥50× ratio + cost-efficiency + Conclusion 扩展）✅
- [x] Camera-ready 完整审查 ✅
- [x] Writing polish（断链引用/hedge/overfull/未引用label）✅

## GPU 预算
- 分配: **4× RTX 5090** (bjb2-18868, cuda:0-3)
- 状态: 空闲 — Reviewer 审计确认无 <4h 实验值得跑，D043 维持
- 注意: 如审稿反馈需补实验，GPU 可立即响应

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D051 | 2026-05-23 | R50 Action Matrix 定稿：4 MF + 7 SF 全部 paper-side，MF4 | — |
| D050 | 2026-05-23 | R49 Action Matrix 定稿：4 MF + 7 SF + 4 MR 全部 paper-s | — |
| D049 | 2026-05-22 | R48 Action Matrix: 4 MF + 1 DIV + 11 SF, 两线并行执行 (A | — |
| D048 | 2026-05-22 | D048: 批准 CPU-only mechanistic analysis (ANOVA + 收敛 | — |
| D047 | 2026-05-22 | D047: Round 47 分数降至 3.0 — 核心修复：Discussion mechanis | exp_062_decoding_strategy_shape |
| D046 | 2026-05-22 | Round 40 达到 3.5 (Borderline Conference) 目标；剩余 3 个  | — |
| D045 | 2026-05-22 | R39 审稿报告处理: 全部 writing fixes, 无新实验, D043 遵守 | — |
| D044 | 2026-05-21 | D044: Dream full review 分析完成，8项写作修复已派Agent执行，不启新实验 | — |
| D043 | 2026-05-21 | DDL 前 72h 全投写作修复，不启动新 GPU 实验；DDR decoding-agnostic | exp_062 |
| D042 | 2026-05-21 | Qwen3-0.6B greedy marginal drift failure (hapax d= | exp_062_decoding_strategy_shape |

