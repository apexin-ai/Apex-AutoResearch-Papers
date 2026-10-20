# agent / loop_2.md

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`dfa401a3669ede40f9e8.json`](../../sessions/df/dfa401a3669ede40f9e8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-13T21:35:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-11235 的 cuda:0 和 cuda:1，无其他可用
- rgds_seed456 在 registry 中误标为 RUNNING（实际未启动，等 ext_seed456 完成后 chain 自动启动），registry 不允许回退状态，已在 spec 字段加注释说明。不要尝试再次 submit 或改状态
- S3 claim（random pruning as regularizer）已由 D017 降级为 directional observation，p≈0.10，不做假设检验，只报 mean±SD。写论文时禁止用 "significantly" 描述 random vs uncurated 差异
- Selection algorithm 是 eigenvalue variance minimization + PCA 32d，不是 facility location / submodular。代码和论文中多次出现此区分，写错会被 Reviewer 抓

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235（2×RTX PRO 6000 48GB），工作目录 `/root/div_cal_verify/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 模型：gpt2-small 124M（HF cache）、gpt2-medium 355M（HF cache），均在线下载过
- 数据：WikiText-103，路径由 HF datasets 自动管理
- 活跃 tmux sessions：`chain_cuda0`（medium_uncurated → medium_rgds → medium_random50）、`chain_cuda1`（ext_seed456 → rgds_seed456 → medium_external → medium_random50）
- 脚本位置：`/root/div_cal_verify/run_medium_*.sh`、`/root/div_cal_verify/chain_cuda*.sh`、`/root/div_cal_verify/run_3seed_stats.py`
- 本地产出：`artifacts/figures/fig1_ppl_trends.{pdf,png}`、`artifacts/tables/table1_gen7_summary{.csv,_latex.tex}`
- GPU 已用 ~35 GPU-h，剩余预算充裕（~560h 可用）

### 3. 📊 当前状态
刚派出 3 个 Worker 等待回调：
1. `worker_ssh_check_gpu_status_20260513` — SSH 检查 GPU 实际进度
2. `worker_paper_experiments_results_draft` — 起草 experiments.tex + results.tex
3. `worker_paper_related_work_draft` — 起草 related_work.tex（36 篇文献已收集）

Registry RUNNING 实验：
- `medium_uncurated_seed42`（cuda:0, GPT2-medium 355M uncurated, 估计 Gen ~5/7）
- `ext_seed456`（cuda:1, GPT2-small external_only seed=456, 估计 Gen ~4/7）
- `rgds_seed456`（cuda:1 串行，registry 误标 RUNNING 但实际未启动，等 ext 完成）

已完成论文章节：introduction.tex、methodology.tex。experiments/results/related_work 正在由 Worker 起草。

### 4. 📋 待办（条件触发式）
- 3 个 Worker 回调到达 → 检查产出质量，GPU Worker 结果更新 ROADMAP 运行中实验表的进度
- ext_seed456 完成（chain_cuda1 cron 回调）→ update_registry DONE + 记录 metrics → rgds_seed456 由 chain 自动启动
- rgds_seed456 完成 → update_registry DONE → 运行 `run_3seed_stats.py` 产出全量 3-seed t-test（C1/C3 强检验，S3 只报描述统计）→ 更新 Table 1 为 n=3
- medium_uncurated_seed42 完成（chain_cuda0 cron 回调）→ update_registry DONE → chain 自动启动 medium_rgds_seed42
- medium 4 方法全部完成 → 产出 GPT2-medium 版 Table 和 Figure，补充 experiments.tex/results.tex 的 TODO 段
- 论文 3 个章节草稿完成后 → 还缺 abstract.tex、discussion.tex、conclusion.tex

### 5. 🎯 战略上下文
- **DDL**：EMNLP 2026 ARR 2026-05-25（还有 12 天）
- **核心发现**：Embedding Alignment Gap — 自训练中内部嵌入几何多样性与内容多样性失对齐，导致 RGDS（内部嵌入 diversity selection）灾难性加速 model collapse（+82% PPL vs random），而 external frozen embedding selection 免疫
- **决策链关键节点**：D009（采纳 Embedding Alignment Gap 叙事）→ D014（C2 从 "external 是方案" 修正为 "internal 是问题"）→ D017（S3 降级为 directional observation）
- **Claim 强度**：C1（ratio 退化 1.04→0.52）强 ✅ | C3（RGDS +74% PPL vs random）强 ✅ | C2-revised（问题特异于内部嵌入）定性强但定量待 3-seed 补全 | S3 方向性观察
- **易错点**：
  - External 和 RGDS 目前只有 2 seeds（42, 123），seed=456 在跑。汇报/写论文时必须标注 n=2†
  - rgds_seed456 的 registry 状态是 RUNNING 但实际没跑，不要被误导去分析它的"结果"
  - run_3seed_stats.py 中 S3 对比已按 D017 改为 descriptive only，不要再加 t-test
  - chain 脚本是 tmux 里的 bash 循环轮询，不是 cron 系统管理的——如果 tmux session 挂了需要手动重建


---
