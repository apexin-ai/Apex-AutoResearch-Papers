---
loop: 3
reason: max_messages
updated: '2026-05-17T11:32:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文核心 Vendi/Quality 指标必须用原始 C1 (carr_quick_probe_03) registry 数据，**不能用** c1-regen-v2 数据。Regen 仅用于 format 分析
- C7 (carr_fullft_lr2e5_nocuration_01) Vendi 真值是 108.08/107.85/108.13（已从 JSON 校正，registry 已更新）
- C8 (K=16) Vendi 用 registry 值 107.32/106.73/107.11，Director 确认无需改
- Format collapse 因果归因：**iterative self-training 固有属性，不是 curation 导致**。论文任何位置不能暗示 curation 导致 format collapse（D013 决策）
- GPU 分配：cuda:0 和 cuda:1 均空闲，Director 指示暂不安排新实验
- 论文只改根目录 tex 文件（`docs/paper/*.tex`），不改 `sections/` 子目录

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165，用户 root，2× RTX 5090 (32GB each)
- 工作目录：`/root/autodl-tmp/carr/`
- Python：`/root/miniconda3/bin/python`（conda base env）
- 模型：`/root/autodl-tmp/carr/outputs_*/gen_*/condition_0/merged`（各实验 checkpoints）
- 数据集：openbmb/UltraFeedback (HF cache, offline mode)
- Format metrics JSON：`/root/autodl-tmp/carr/analysis/c1_c5_format_diversity.json`
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/`
- 活跃进程：无（所有实验已完成）
- 活跃 cron：无（reconcile 已清理）

### 3. 📊 当前状态
**刚做完**：D013 format collapse 因果归因修正 Step 1+2（analysis.tex Table 4 替换 + 5 个 tex 文件叙事更新 + Reviewer 3C5W 全部修复）

**正在等**：
- `worker_paper_figure_fig4_format_collapse_v2_20260517T111150` — Fig 4 三线图重新生成（C1 K=4 curated, C5 K=4 random, C2 K=8 curated），应该即将完成

**Registry**：15 个实验全部 DONE（4 success, 5 negative, 6 failed），无 RUNNING/PREPARING

**已完成的论文工作清单**：
- 8/8 sections 初稿 + Reviewer 审查通过
- K=16 data patched into results.tex + analysis.tex
- AI 风格检查（18 处 -ing phrase 修复）
- 引用审计通过（15/15 key）
- Reviewer 3 CRITICAL + 5 WARNING 全部修复
- D013 因果归因修正（abstract/intro/analysis/discussion/conclusion 全部更新）
- Fig 2 (Vendi trajectories v2 含 K=16) + Fig 3 (direction reversal) 已完成
- Appendix per-gen metrics table 完整（8 条件）

### 4. 📋 待办
- Fig 4 v2 Worker 回调 → 验证图表质量（C1/C5 重叠 + C2 更陡）→ register artifact → 报告 Director Step 3 完成
- Director 确认 D013 全部完成 → 进入最终 proofread + LaTeX 编译阶段
- W5 (analysis.tex Table 4 format metrics K mismatch)：Director 说等 format_metrics_unified 完成后处理，现在 Table 4 已用 C1/C5 同 K 数据替换，W5 应已自动解决——但需要 Director 确认
- DDL 2026-05-25（8 天后）：剩余工作 = Fig 4 落地 + 最终 proofread + 编译 + 提交

### 5. 🎯 战略上下文
**核心结论（Direction D）**：Reward curation 不导致任何形式的 collapse。Semantic diversity 在所有 8 条件下保持 ±1%。Format collapse 是 iterative self-training 固有属性（C1≈C5 同 K=4 证明），K 是放大因子。LoRA 下的表观 diversity suppression 是 capacity artifact（direction reversal +0.63pp under Full-FT）。

**决策链**：D004(P1 FAIL) → D009(5/5 FAIL 证伪核心假设) → D011(Direction C FAIL) → D012(K=16 NEGATIVE, Outline A 确认) → D013(format collapse 因果归因修正：不是 curation 的错)

**易错点**：
- 论文中 format metrics 有两套数据：candidates pool（论文主要使用，opening_unique_ratio 0.757→0.477）和 selected responses（format_metrics_unified.md, 0.980→0.976）。不要混用
- C2 (K=8) 的 format 数据（0.701→0.367, 1.13 bits drop）仍在论文中作为 K amplification 的证据使用，但不再作为 curation 导致 collapse 的证据
- Abstract 已更新但 word count 需要检查（新句子比旧句子长）
