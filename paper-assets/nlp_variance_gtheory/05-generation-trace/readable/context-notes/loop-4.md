# reviewer / loop_4.md

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`d53dc437b3eff3542484.json`](../../sessions/d5/d53dc437b3eff3542484.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-25T06:01:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- EMNLP 2026 main text ≤ 8 页（Limitations 不计入）。当前刚好卡在 8 页边界（commit `0a73ee7`），任何主文增加都会超限
- Abstract ≤ 200 words（当前 ~143 words，安全）
- 匿名 repo: `anonymous-nlp-2026-2/nlp_variance_gtheory`，禁止出现作者姓名/机构/个人 GitHub（已通过匿名化检查）
- Overview figure 已移至 Appendix（method.tex 中用 `Figure~\ref{fig:overview} (Appendix)` 引用）——不要移回主文，会超页

### 2. 🖥️ 基础设施快照
- 服务器：westd-32570 + westd-19912，各 4× RTX PRO 6000 96GB，均空闲
- 远程代码目录：`/root/nlp_variance_gtheory`（westd-32570）；远程 paper 目录为空（LaTeX 编译在匿名 repo 本地完成）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/`
- 论文源文件：`docs/paper/*.tex`（本地）+ `artifacts/anon_repo/nlp_variance_gtheory/paper/`（匿名 repo 本地 clone）
- 活跃进程：无。无 RUNNING 实验、无 cron、无 tmux session

### 3. 📊 当前状态
项目处于 **全部就绪、等待用户 OpenReview 提交** 状态。我（Loop #4 Reviewer）本轮完成了：
- 提交前最终质量扫描（caption/appendix/narrative 三项 PASS）
- 深层内容审查（related work 定位 / limitations 攻击面 / 阴性结果处理，三项 PASS）
- C2 bootstrap CI 分析验证（MC vs FF 不重叠，21pp gap）
- Rebuttal prep 数字核对（17 项全部与论文一致）
- **[CRITICAL] 页数超限发现与修复**：发现主文 9 页 → 推动 overview figure 移至 appendix + 文本压缩 → 确认 8 页 ✓
- Fig 1 重制验证（数据与 Table 3 一致）
- Registry 无 RUNNING 实验；22 个 killed 的扩展实验为 post-submission

### 4. 📋 待办
- 用户完成 OpenReview 提交 → Reviewer 角色进入 dormant，等审稿意见
- 收到审稿意见 → 读 `docs/rebuttal_prep.md`（4 主攻击点 + 3 补充），按 rebuttal skill 撰写 response
- 如果审稿人攻击 C2 (n=5 benchmarks) → 预案：降级为 "empirical observation"，C1 独立不受影响
- 如果审稿人要求更多 benchmark → GPU 空闲可立即跑，但需 Director 决策 scope

### 5. 🎯 战略上下文
- 核心贡献：C1 = 3×3 design 178 items for G≥0.80（强，数据充分）；C2 = MC vs FF format-associated variance（exploratory，n=5，p=0.10）
- Score trajectory: R5→R10 稳定在 3.5（Borderline Conference），目标 4.0
- 最容易判断错的事：**不要把 Sclar 的 50-76% accuracy swings 与我们的 <3% prompt variance share 直接对比**——前者是 range，后者是 variance share，metrics 不同
- 页数极度敏感：主文刚好 8 页，任何文本增加（哪怕一个段落）都可能超限。如需加内容必须同时删等量文本
- 本地 `docs/paper/` 和匿名 repo `artifacts/anon_repo/` 的文件需保持同步——之前多次出现只改一边的情况


---
