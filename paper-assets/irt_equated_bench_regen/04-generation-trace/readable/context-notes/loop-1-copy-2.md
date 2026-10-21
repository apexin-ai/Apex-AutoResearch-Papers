# reviewer / loop_1.md

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`9feab7ec3d5da2a5ef0f.json`](../../sessions/9f/9feab7ec3d5da2a5ef0f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-22T19:16:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目是纯分析项目（METABENCH response matrix），无 GPU 训练、无远程服务器。所有实验在本地 Python 运行。不要 SSH 任何服务器。
- 论文 DDL: **2026-05-25 AoE**（EMNLP 2026 via ARR），8 页正文限制。
- Discussion.tex:15 "ruling out ceiling effects" 已被我标 WARNING 但截至 handoff 时**尚未修正**——下一个"你"必须追踪这个修正是否落地。
- Semi-synthetic gradient 实验的 Scheme A 将 "capability" 建模为 "easy items improve"，但 real data 显示 hard items improve。**不要**在审查中说 "real data rules out capability evolution"——只能说 "ρ 符号 alone 不具区分力"。

### 2. 🖥️ 基础设施快照
- 无远程服务器、无 GPU、无 wandb、无活跃进程/cron
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`
- 论文: `paper/sections/{introduction,experiments,discussion,method,limitations,appendix,abstract}.tex`
- 实验产出: `artifacts/r17_*/`, `artifacts/r18_*/`, `artifacts/r19_*/`
- Registry: `registry.yaml`; Roadmap: `ROADMAP.md`; Decisions: `decisions.yaml`

### 3. 📊 当前状态
**刚完成**：R19 全部实验审查 + 论文修正验证。已发两条 `reviewer_post_to_director`:
1. R19 论文修正验证报告（6 项修正全部 ✅，1 个 WARNING 残留："ruling out ceiling effects"）
2. Exp 4 Semi-Synthetic Gradient 解释正确性深度审查（回答 Director 4 个问题，结论 WARNING）

**Registry 状态**：所有实验 DONE，无 RUNNING/PREPARING。

**等待中**：
- Director 对 "ruling out ceiling effects" 修正的决策
- 可能的 R20 论文提交前终审请求
- Paper Agent 可能的 Step 5 写作评审请求（需用维度评分模板）

### 4. 📋 待办
- Director 转发论文修正稿 → 验证 discussion.tex:15 是否删除 "ruling out ceiling effects"，是否增加 ceiling effect caveat 连接 §4.5→§5.1
- Paper Agent 提交 Step 5 评审 → 使用 §5.3 评分模板（Originality/Clarity/Soundness/Significance/Presentation + Overall 1-10）
- 论文提交前终审 → 逐项检查：de-dup 19.7%（3处）、rank-bucket 15.1%、contribution "orthogonal constructs"、base-vs-instruct 数据一致性、limitations 长度合规（EMNLP: 一小段 3 点）、页数 ≤8
- Director 转发 Framing 调整提案 → 必须先 Read `negative-framing-review` skill，按四维度审

### 5. 🎯 战略上下文
**论文核心论点**：MH-DIF 审计发现 MMLU 31% items 存在 temporal measurement instability（校正后 ~27-29%），DIF flags 与 web-overlap labels 正交（Jaccard=0.206），base/instruct 模型展现不同 DIF 机制（χ²=562.7）。

**审稿分数轨迹**：R17=3.0 → R18=3.5 → R19=3.0（回落）。目标 4.0（Conference），现实天花板 3.5（Findings）。R19 回落可能因 de-dup 数据 credibility + causal framing tension。

**最易判断错的事**：
1. **ρ 符号的因果推断**：negative ρ 同时 consistent with contamination（ceiling effect）和 capability evolution（hard items improve）。不要在审查中偏向任一解释。Base-vs-instruct 分解才是 mechanism separation 的主论据。
2. **De-dup K=20 的 19.7% vs 旧 29.1%**：19.7% 是 random selection（正确），29.1% 是 plan_022 biased "most representative" selection（已废弃）。如果论文任何位置还残留 29.1%，立即 CRITICAL。
3. **ICC 混淆**：item-level ICC=0.047（DEFF 用）vs model-level pairwise r≈0.47（ICC-by-family-size 用），10× 差异。appendix "ICC by Family Size" section 内容正确（说 pairwise r）但标题有歧义。
4. **Scheme A 建模假设**：它定义 "capability = easy items improve"，但这只是一种可能的 capability model。审稿人可能质疑"为什么不建模 hard items improve"——论文需要 acknowledge 这个局限。


---
