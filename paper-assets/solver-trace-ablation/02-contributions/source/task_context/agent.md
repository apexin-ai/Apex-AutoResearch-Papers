---
loop: 26
reason: idle_timeout
updated: '2026-05-25T12:26:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- 匿名仓库 push 必须读 `_anonymous_repo.json` 的 `push_url`，不要硬编码 URL（含 token，会过期）
- push 命令：`git push "$PUSH_URL" master:main`（本地 master → 远程 main）
- 论文正文严格 8 页限制（EMNLP 2026 ARR），Limitations + References 不计入
- Abstract 不超 200 words
- Ethics section 已删除（EMNLP 2026 不要求），不要加回来
- `paper/` 目录是 `docs/paper/` 的镜像提交副本，每次改 docs/paper/ 后必须 cp 同步到 paper/ 再 commit

### 2. 🖥️ 基础设施快照
- 服务器：本地 EC2 (ip-172-31-5-208)，无远程 GPU 服务器活跃
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/`
- 论文源码：`docs/paper/` (主编辑目录) + `paper/` (提交镜像)
- Python：系统 python3.14，PEP 668 受保护；PaperBanana 装在 `/tmp/pb_venv/`
- 无活跃训练进程、无 tmux session、无 cron 任务
- 无活跃 Worker

### 3. 📊 当前状态
本 session 全部在做论文排版冲刺（DDL 2026-05-25）。完成的工作：
- 数据审计：Table 1/2 所有百分比与 per-seed appendix 数据交叉验证并修复
- 新增 premise-bins figure (Fig 4)，Table 2 移入 appendix
- PaperBanana 重绘 STA overview (Fig 2) — 三栏概念图
- Introduction 重写（去掉 \paragraph 分隔，改为流畅叙事）
- Related Work 精简（reward hacking 段从 10 行压到 5 句）
- Limitations 精简（6 点→3 点）
- Ethics section 删除
- 12 个缩写首次使用展开
- 全部 5 张统计图配色统一（blue/red/lightblue 学术色系）
- 每轮都 compile + commit + push 到匿名仓库

最新 commit: `3a7afb5` (master)，已 push 到匿名仓库 main。
编译状态：23 页，正文 8 页以内，无 warning。
Registry: 无 RUNNING/PREPARING 实验。

### 4. 📋 待办
- 用户要求最终提交前检查 → pdf_to_images 全页视觉审查，确认无排版溢出
- Director 要求 reference audit → Read reference-audit skill，检查 bib 条目真实性
- Director 要求 checklist → 确认 ARR Responsible NLP Checklist 在 OpenReview form（不在 PDF 里）
- 如需进一步压缩页面 → 优先继续压 Related Work

### 5. 🎯 战略上下文
- 项目核心结论：ISR 作为诊断工具有效（检测 CE/TS 等 hacking modes），但作为训练 reward 触发 Goodhart effect（TS gaming 达 ISR=1）。Observe-optimize asymmetry 是论文主线。
- 已完成全部实验，当前纯论文写作阶段，无需跑新实验
- 易错点：`docs/paper/` 和 `paper/` 必须保持同步，忘记 cp 会导致提交版本与编辑版本不一致
- 易错点：latexmk 经常报 "up-to-date" 即使图片内容变了，需用 `pdflatex` 直接编译强制刷新
- 易错点：PaperBanana 生成的图是 JPEG 格式但扩展名为 .png，需用 PIL 先转换
- χ² 值保持 174.8 不动（Director 决策，p<10^-36 定性结论不变）
