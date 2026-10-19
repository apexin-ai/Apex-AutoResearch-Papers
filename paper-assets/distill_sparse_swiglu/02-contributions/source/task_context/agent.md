---
loop: 17
reason: idle_timeout
updated: '2026-05-25T05:40:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34887 cuda:0, cuda:1（2× RTX PRO 6000 Blackwell 96GB）。不可用其他 GPU/服务器
- 匿名仓库 push 必须读 `_anonymous_repo.json` 获取 token URL，不可硬编码。工作目录 `/tmp/anon_repo`
- 匿名仓库 push 时排除：`paper/_pdf_images/`、`paper/_figure_backups/`、`figures/paper/run_*/`（PaperBanana 临时目录）
- Registry 中 `model_level_sparsity` 字段可能是 target 而非 actual（ste_30_s42 教训：标 0.30 实际 0.208）
- 论文 8 页硬限（EMNLP 2026），limitations/references/appendix 不计入

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887，工作目录 `/root/distill_sparse_swiglu/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型：LLaMA-3.1-8B `/root/autodl-tmp/models/llama-3.1-8b`，Qwen-2.5-14B `/root/autodl-tmp/models/qwen2.5-14b/`
- 数据盘：`/root/autodl-tmp/` (250GB, 28% used, 181GB free)
- 网络：HuggingFace 需 `source /etc/network_turbo` 才可达
- wandb：服务器无 API key，实验用 offline 模式
- 活跃进程：无（全部 GPU 空闲）
- Cron：无活跃监控任务

### 3. 📊 当前状态
论文处于最终提交状态。DDL 2026-05-25（EMNLP ARR May cycle），待运维手动提交。

刚完成的工作：
- Fig 1 v5 简化版 commit (ae2fa73) + push 到匿名仓库 (8a12e6b)
- 此前完成：typo/caption 扫描 → P0 factual fix → overfull hbox fix → legend overlap fix → Fig 1 多轮迭代
- MSE LR sweep 完成（mse30_lr2e4_s42 Lagrangian 发散，mse30_lr1e4_s42 PPL=17.50，仍 2× 差于 KL 8.81）——rebuttal 备用数据
- STE 调查结论：ste_30_s42 PPL 8.41 是在 20.8% 实际稀疏度下取得，不可与 KL 30% 比较，论文现有处理正确

Registry：408 实验，0 RUNNING，257 success。全部 GPU 空闲。

### 4. 📋 待办
- 运维提交 ARR → 无需 Agent 动作，等审稿
- Reviewer 质疑 MSE baseline LR 公平性 → 引用 mse30_lr1e4_s42 (PPL 17.50) 和 mse30_lr2e4_s42 (Lagrangian 发散) 作为 evidence
- Reviewer 质疑 STE/Gumbel claim → 引用 STE 调查结论（实际稀疏度 20.8% vs target 30%）
- 收到审稿意见 → Read rebuttal skill，逐条回应
- 论文数据审计发现但未修的 minor issues（P2/P3 级）：tab:c1 caption metric 歧义、BoolQ 未在 eval 段声明、多个 appendix orphan labels——Director 决定不改

### 5. 🎯 战略上下文
- 核心 claim：KL output-distribution alignment > per-neuron BCE for sparsity prediction（PPL 14.5% improvement at 30%）
- 已知弱点：knowledge-intensive tasks regression（MMLU -5.2pp 8B, GSM8K -19.9pp 14B），论文已 honest 报告
- 内部评分 R29 = 3.0 Findings，目标 ≥3.5 Conference
- 易错点 1：匿名仓库 push 前必须 `git pull origin main`，否则 reject（之前踩过）
- 易错点 2：论文数字修改后必须同步 abstract/intro/experiments/conclusion/appendix 全部出现位置
- 易错点 3：MSE baseline 主表用 LR=1e-3（PPL 18.52±1.68），消融表用不同 run（15.71 s42），两表 BCE 值也不同（15.09 vs 15.71）——这是已知 issue，Director 决定不改
