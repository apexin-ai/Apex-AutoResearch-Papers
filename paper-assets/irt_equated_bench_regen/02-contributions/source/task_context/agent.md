---
loop: 1
reason: idle_timeout
updated: '2026-05-25T06:10:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 分配，所有分析为纯 CPU 统计计算（response matrix 操作）
- 匿名仓库 token `[REDACTED_GITHUB_TOKEN]` 绝不能提交到任何文件中
- 论文分支是 `rebuttal-b1-b7`，不要在 main 上改 paper/
- 数据源 truth: `artifacts/` 下的 CSV/JSON，不是论文 .tex 中的数字

### 2. 🖥️ 基础设施快照
- 服务器：本地 Ubuntu (ip-172-31-8-29, ap-northeast-1)，无远程 GPU 服务器
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen`
- Python：系统 python3（无 conda/venv，纯 numpy/scipy/pandas 分析）
- 匿名仓库：`https://github.com/anonymous-nlp-2026-2/irt_equated_bench_regen`（public，3 commits by Anonymous）
- 活跃进程：无（全部实验已完成）
- Crons：无活跃

### 3. 📊 当前状态
论文技术侧 100% 就绪，DDL 2026-05-25 AoE。最终数据自查已通过（无需修正）。

已完成的 rebuttal 任务：
- B1-B9 should-fix commits（rebuttal-b1-b7 分支）
- E1-E3 Tier 1 实验（K=3 power, interaction regression, mixed-mechanism）
- R15/R16/R17/R22 审稿分析（temporal DIF, threshold calibration, DEFF downstream, score inflation）
- W2 k=30,40,50 multi-subject injection 扩展
- 匿名仓库 push（code + paper source）
- 数据正确性审计 2 轮（130+ 数字核查，6 处已修正，最终确认 0 问题）

Registry: 所有实验 DONE（成功 14 / 负向 6 / 失败 0）。无 RUNNING/PREPARING。

等待：用户完成 ARR OpenReview 提交（匿名仓库已 public，论文已编译）。

### 4. 📋 待办
- Director 说 "提交完成" → standby 结束，进入 post-submission 阶段
- 如果 Director 发现任何 last-minute 数字问题 → 改 .tex → 编译 → commit rebuttal-b1-b7 + push 匿名仓库
- Camera-ready 阶段需修正 2 处低风险：§5.1 AUC "0.93-0.94"→"0.92-0.93"，Table 5 一个 cell 0.915→0.914

### 5. 🎯 战略上下文
这是 EMNLP 2026 ARR 投稿（MH-DIF psychometric audit of LLM benchmarks）。核心 claim：temporal DIF C%=31.3%（DEFF-adjusted 13.5-29.2%），50× above random null，ranks preserved (ρ=0.997)，orthogonal to web-overlap (Jaccard=0.206)。

易错点：
- "≥22×" enrichment 精确值是 21.8×（13.5%/0.62%），Director 已知并接受
- Table 1 Ability quintile N 是 ~2,090 不是 ~2,600（已修正，别改回去）
- summary_by_k_full.csv 包含 k=1,2,3,5,10,20,30,40,50（不只是原始的 1-20）
- 匿名仓库 git author 必须是 "Anonymous <anonymous@example.com>"，不要用真实身份 push
