# director / loop_5.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`39b1a881e77a88219a75.json`](../../sessions/39/39b1a881e77a88219a75.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T10:40:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配：westc-26893 cuda:0 是本项目唯一分配的卡，不要用其他 GPU
- Reviewer pp 换算反复出错（10× 放大）：收到含 pp 数字的报告时必须手动验证（raw_diff ÷ 0.01 = pp）。已存 memory
- Citation 验证：不要从单次 web search 就判定引用为 hallucinated，必须交叉验证（arXiv/institution/proceedings）。已存 memory
- paper_framing.md 已更新为 Version B（binary > graduated），不要引用旧 Version A 语言
- discussion.tex 已压缩为 18 行，Reviewer 反复标记"L169-170/L206 stale"是引用旧行号，实际已修复——不要再派 Agent 修

### 2. 🖥️ 基础设施快照
- 服务器：westc-26893，项目目录 `/root/gen-depth-contamination/`（推测，需 Agent 确认）
- GPU：1× A6000 48GB，cuda:0
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/`
- 活跃实验：exp-015 v4 neural probe 已完成（3 模型 K*=[2,2,3]）；GPU 当前应空闲
- exp-006 filtering 51/51 DONE；exp-015 DONE
- Agent 正在处理 5 组 rebuttal 实验（EXP-A 到 EXP-E），queue depth=3

### 3. 📊 当前状态
**审稿报告处理中**：Round 1 审稿 weak reject / borderline，3 Critical + 11 Warning。

**已完成**：
- Paper Agent 完成 10 项论文修订（θ justification、neural probe 措辞、Limitations 独立、Ethics Statement、3 篇新引用、12 orphan bib 清理、Abstract 压缩至 170 词等）
- K*(θ) 曲线图 placeholder 已在 experiments_c1.tex，等 Agent 画 `figures/fig_kstar_theta.pdf`
- review_issues.yaml 已更新所有 FR-1 到 FR-16 为 in_progress

**Agent 正在处理的 5 组实验**：
- EXP-A [Critical]: 替代 Scorer（Pythia + OLMo 作为 surprisal scorer，重算特征+重训分类器）~1h GPU
- EXP-B [Critical]: 14D ablation（去 self_BLEU）→ Reviewer 已 PASS，K*=2 全部成立，但 OLMo CI 极边缘（0.6034，距 θ 仅 0.0034），建议补 bootstrap CI
- EXP-C [Warning]: 10K permutation → Reviewer 已 PASS，p 从 0.002 改善到 <0.0001，Qwen-cont CI lower 更紧（0.6003）
- EXP-D [Warning]: OBD N=500 → **已作废**，urgent message 已发，要求用 exp_011 已有 OBD predictions 做 bootstrap 而非重训分类器
- EXP-E [Warning]: Paired t-tests + Holm-Bonferroni + Cohen's d

**等待中**：
- Agent 回复 5 组实验汇总结果
- 用户回复是否补 7B 实验（FR-4，Reviewer 强烈建议，~2 天可完成）
- Paper Agent 等 Agent 画 K*(θ) 曲线图

### 4. 📋 待办（条件触发式）
- Agent 汇报 EXP-A（替代 scorer）结果 → 如 K*=2 stable：恢复 "text-intrinsic" 为更强措辞并派 Paper Agent 更新；如 K*≠2：重大叙事调整
- Agent 汇报全部实验完成 → 派 Agent 画 K*(θ) 曲线图（matplotlib，4 条线 × θ 从 0.55 到 0.70）→ Paper Agent 填入
- 用户确认 7B 实验 → 派 Agent 生成 7B 数据 + 全套 K* 实验（~2 天），可用 Qwen2.5-7B
- 用户拒绝 7B → Title 加 "at the ≤1.5B Parameter Scale"，rebuttal 用 DPI + 3 架构族论证
- 全部实验 + 论文修订完成 → submit_paper_to_review（推荐 continue 模式验证修复）
- 14D ablation OLMo margin 极紧 → 论文中如实报告 "point estimate above θ but CI may overlap"
- EXP-C 10K permutation 的 Qwen-cont CI lower=0.6003 → 论文更新为此更精确值

### 5. 🎯 战略上下文
- **核心结论**：K*=2 universal（15D features, 8/8 conditions）。Neural probe K*=[2,2,3] model-dependent，加强 model-free 方案定位（D027）
- **C3 Version B 确认**（D026）：binary-ours > all alternatives。DSIR 垫底。效果量小（sub-1pp），framing 改为 "K*=2 correctly predicts strategy ordering" + "damage minimization"
- **审稿三大攻击面**：(1) θ=0.60 缺 justification → Cohen's h + task-based 双论证已写入；(2) scorer-generator confound → EXP-A 结果决定论文能用多强的 claim；(3) self_BLEU leakage → 14D ablation 已 PASS
- **最容易判断错的事**：discussion.tex 看起来只有 18 行，Reviewer 反复标记旧行号——实际已修复，不要浪费时间重查。paper_framing.md 的 C3 已是 Version B。
- **DDL**：ARR May 25, 2026（10 天）。如果补 7B 实验需要立即启动，时间刚好够
- **决策链**：D012（2+1 claim 结构）→ D017（措辞策略）→ D025（C3 数据修正）→ D026（Version B 确认）→ D027（neural probe model-dependent reframe）


---
