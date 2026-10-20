# director / loop_1.md

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`863c71309e62c690d025.json`](../../sessions/86/863c71309e62c690d025.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-21T02:06:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验，全部是 API 调用实验（τ²-bench）。不涉及本地 GPU 分配。
- 5-model error analysis 需要 OpenRouter API（GPT-5.4 作为 coder），当前 402 余额不足，用户未充值前不要尝试运行 `artifacts/run_error_analysis_5model.py`
- 论文主体严格 8 页限制（EMNLP 2026 Long Paper）。Limitations + References 不计入。每次加文本后必须编译验证 Conclusion 仍在 page 8
- Cross-judge 设计不可改：GPT-5.4 judge Claude/Qwen3/DeepSeek，GPT-4.1 judge GPT-5.4。C3 layer effect 是 INCONCLUSIVE（p=0.017 但 within-judge 不显著），绝不能 claim 为 significant
- Realism validation 数据必须诚实报告 amb_vs_original 全部 4 项（包括 FK d=0.29 p=0.006），不能只挑有利的

### 2. 🖥️ 基础设施快照
- 无远程服务器。所有实验数据在本地 workspace。
- 论文源码：`projects/policy_ambiguity_safety/docs/paper/` (main.tex)
- 实验数据：`projects/policy_ambiguity_safety/artifacts/full_study/`
- 分析 JSON：`artifacts/full_study/analysis/` (clause_variance_decomposition.json, info_delta_analysis.json, realism_validation.json, severity_sensitivity.json, mcnemar_matched.json, within_judge_c2.json, tost_margin_sensitivity.json 等)
- Error analysis 脚本：`artifacts/run_error_analysis_5model.py`（支持断点续传）
- Plan_009 人工标注材料：`artifacts/plan_009/` (annotation_sheet.csv, annotator_instructions.md, calibration.py)
- 无活跃进程 / 无 tmux / 无 cron

### 3. 📊 当前状态
刚完成本轮全部零成本文本加固（7 项编辑 + Reviewer 叙事一致性验证）：
1. Limitations: realism FK 诚实报告（修正选择性报告问题）
2. Analysis §6.2: C3 inconclusive 限定句
3. Intro contribution 2: incompleteness confound caveat
4. Experiments C1: McNemar discordant breakdown (544 vs 36, 15.1:1)
5. Method §4.2: realism validation 前向引用
6. Experiments C1: variance decomposition (clause 22.4% vs model 1.0%)
7. Discussion: 压缩（Systematic Nocuity 合并入 Differential Nocuity）+ Conclusion 压缩
8. Analysis §6.3 Ambiguity Blindness 精简（省页面空间）

论文已提交 C 群审稿（continue 模式，apr_20260521T012024_19x0）。Registry 无 RUNNING 实验。

### 4. 📋 待办
- C 群审稿报告回来 → Read `skills/global/review-report-action.skill.md` → Holistic Pass + Per-Comment Action Matrix → 派 Agent/Paper Agent 执行
- 用户充值 OpenRouter → 立即派 Agent 运行 `run_error_analysis_5model.py`（369 traces × 2 coders = 738 API calls，Claude/Qwen3/DeepSeek 三模型）→ 结果写入论文 §6 扩展 error analysis 覆盖至 5 模型
- 用户设置 Google Sheets + 邀请标注者 → 等标注完成 → `calibration.py --human-csv` 算 human-LLM agreement → 结果写入论文 Limitations
- Reviewer 建议 optional：C4 加 variance decomposition 呼应句 + per-type ICC 放 Appendix（仅在页面有空间时考虑）

### 5. 🎯 战略上下文
- **核心论文 story**: Differential Nocuity — 所有 policy ambiguity 对 LLM agent 都是 nocuous (+34pp)，但 type 和 model 共同决定严重程度。Auth_scope 是 canary type (12-64%)，incompleteness 是 universal blind spot (46-62%)。
- **Claims**: C1 binary effect ✅ (OR=15.1), C2 type hierarchy ✅ (V=0.137, three-tier), C3 layer effect ❌ INCONCLUSIVE, C4 model×type ✅ (χ²=31.02)
- **最大 Soundness 缺口**: Error analysis 只覆盖 2/5 模型（GPT-5.4 + GPT-4.1）。5-model 扩展是 Soundness 3→3.5 的关键，但阻塞在 API 余额。
- **易错点**: (1) 编译工具报 "11 pages > 8" 是 false alarm（Limitations+References 不计入），但必须视觉确认 Conclusion 在 page 8 结束 (2) C3 绝不能升级为 significant claim (3) per-type ICC 有两种：reproducibility ICC (C3, 0.976-0.989) 和 cross-model clause-level ICC (variance decomposition, 0.29-0.49)，不要混淆 (4) incompleteness confound: 排除 incompleteness 后 five-type omnibus p=0.079 不显著，three-tier 退化为 two-tier


---
