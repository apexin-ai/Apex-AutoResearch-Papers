# director / loop_2.md

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`5ea6af1aa84a509212a7.json`](../../sessions/5e/5ea6af1aa84a509212a7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-22T18:29:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验（纯 LLM API 调用 + 论文写作），无设备号限制
- 标注数据路径：A1 `data/annotation_sheet_1.csv`（latin-1 编码），A2 `data/annotation_sheet_2.csv.xlsx`（Excel 格式，需 openpyxl，venv 在 `/tmp/xlsx_env/`）
- 论文真源在本地 `projects/causal_style_decomp_judge/docs/paper/`，不在远程服务器
- R12 审稿报告已收到但 Action Matrix 尚未定稿——**禁止在 Reviewer 回复前派 Paper Agent 执行修改**

### 2. 🖥️ 基础设施快照
- 无远程服务器/GPU——本项目是纯论文写作+分析项目
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/`
- 编译：`paper_compile_and_check(project="causal_style_decomp_judge", max_pages=8)`，17 页总计（主文 8 + Limitations + Appendix + Refs）
- Excel 解析 venv：`/tmp/xlsx_env/bin/python3`（openpyxl 已装）——可能被清理，需要时重建
- 无活跃进程/cron/训练任务

### 3. 📊 当前状态
**刚做完**：
- D069: R11 审稿报告全部修复（P0-P5: novelty reframe + amplification hedging + 因果 disclaimer + recall 补报 + TOST 修复 + 批量修复）
- D070: 双标注员数据整合（A1 100% + A2 84% pass precision，majority 100%，κ=0.44/AC1=0.65）
- R12 审稿提交并完成——**评分 3.0 (Findings)**，比 R11 的 3.5 下降

**正在做**：
- R12 Action Matrix 已构建并发给 Reviewer（`post_to_reviewer`），等 Reviewer 回复后综合定稿
- 已向用户报告 R12 结果 + 询问标题改动确认（"Detecting Hidden Style Bias" → "Format-Dependent Style Sensitivity"）

**等待中**：
- Reviewer 对 R12 Action Matrix 的独立审阅回复
- 用户对标题改动的确认

### 4. 📋 待办
- Reviewer 回复 → 综合定稿 Action Matrix → 更新 review_issues.yaml → 派 Paper Agent 执行
- 用户确认标题改动 → 纳入 Paper Agent patch 指令
- Paper Agent 完成修改 → 编译 → 提交 R13 审稿（continue mode）
- SF1 multi-Δ TOST：可能需要 Agent 跑 Δ=5/10/15/20pp sensitivity 分析（取决于 Reviewer 判断）
- SF6 d=-0.23：可能需要 Agent 在 GEE 中加 word count covariate（取决于 Reviewer 判断）
- DDL: **2026-05-25 AoE**，剩余约 3 天

### 5. 🎯 战略上下文
**评分轨迹**：R1:2.5 → R2-R4:3.0 → R5-R10:3.5 → R11:3.5 → R12:3.0（回落）

**R12 下降核心原因**（4 个 MF）：
1. MF1: 标题 "Detecting Hidden Style Bias" 预设 pairwise 为 ground truth——连续多轮未解决，这次两位共识 critical
2. MF2: Formality 轴 quality confound 严重（Orig OR ≥ Style OR 多配置）——新问题，削弱统一 "style bias" 叙事
3. MF3: Novelty 是 Thurstone 领域迁移——R1 excitement 3.5 vs R2 2.5，最大分歧，从 R1 追到 R12
4. MF4: Bootstrap CI vs GEE sandwich SE 分工不清——纯技术清晰性，简单修复

**易错点**：
- 不要低估 MF1+MF2 的联合影响——标题+formality 双重问题意味着论文 narrative 需要实质性调整，不是微调措辞能解决的
- Novelty (MF3) 已经追了 12 轮，可能已到 writing 能做到的天花板——不要花太多精力在这里，聚焦 MF1+MF2
- R12 是 fresh review 3.0，不代表论文质量倒退——fresh reviewers 视角不同。但说明之前的修复未能从根本上解决 framing 问题
- review_issues.yaml 需要在 Action Matrix 定稿后更新（R12 新增 MF2 formality confound、MF4 CI 方法、SF6 cross-axis d=-0.23）
- 之前 Reviewer #114 反对改标题（辨识度），但 R12 两位共识 critical——这次可能必须改


---
