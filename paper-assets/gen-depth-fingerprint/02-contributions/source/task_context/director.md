---
loop: 8
reason: max_messages
updated: '2026-05-25T19:55:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验（纯论文写作项目），所有实验数据已固定在 `artifacts/_project/` 下
- 论文正文严格 8 页限制（EMNLP 2026 ARR），Limitations/refs 不计入
- 每次论文编辑+编译后必须上传 PDF 给用户（feedback_upload_pdf.md）
- 数据来源：`artifacts/_project/supplement/data/features_all_models.csv` (37,058 rows, 8 models) 是唯一真源，论文数字必须可追溯到此

### 2. 🖥️ 基础设施快照
- 无远程服务器，纯本地论文编译
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/`
- 编译命令：`cd docs/paper && pdflatex -interaction=nonstopmode main.tex`（bibtex 需单独跑）
- 数据目录：`artifacts/_project/supplement/data/`（CSV）、`artifacts/_project/analysis/`（JSON）、`artifacts/_project/results/`（JSON）
- 图表源码：`artifacts/_project/chart/`
- 无活跃进程、无 tmux、无 cron

### 3. 📊 当前状态
刚完成全文数据真实性审计 + 修复唯一不一致项（results.tex F1 0.773→0.771）。编译验证通过，8页正文。

之前完成的工作链：
1. Audit #2 fixes（macro vs pooled F1、VERSION C comment、CV protocol、gen-0 exclusion）
2. Figure 1 缩小 + Discussion 压缩解决超页
3. Audit #3 fixes（de-AI patterns、5-gen qualifier、ethics.tex）
4. ACL 官方模板对齐（去掉 float spacing hacks、raggedbottom、inconsolata）
5. 全文数据真实性审计（0 fabrications，1 minor fix done）

Registry: 无 RUNNING 实验。项目处于审稿阶段（review_chat_id 已配置）。

### 4. 📋 待办
- 用户确认审计报告 → 如有后续指令照办
- 用户说"进入审稿"/"重新审稿" → 调 `submit_paper_to_review` 提交
- 若需要 re-run eval scripts（eval_8gen_logo.py 等）生成本地 JSON → 需要用户提供 GPU 服务器（脚本需要 Pythia-410M inference）
- Paper Agent 如有写作任务回调 → 按正常流程处理

### 5. 🎯 战略上下文
- 项目核心贡献：DDR（Differential Depth Response）——递归生成的 location features 单调漂移而 shape features 近稳态，支持跨生成器深度分类
- 关键数字锚点：LOGO 3-class F1=0.762（8-gen）、binary F1=0.694（macro）/0.705（pooled）、cross-model 5-gen F1=0.830、LOFO binary F1=0.686
- 易错点：cross-model chains 用 5 generators（不是8），η²_gen≤0.009 来自 cross_model_anova.csv（不是主 ANOVA 表），10-fold CV 和 LOGO 是不同协议不要混
- 论文已基本定稿，主要风险是审稿阶段被 reviewer 挑战 instruct model 适用性（已有 QLoRA recovery 实验 F1=0.89-0.91 作为回应）
