---
loop: 1
reason: max_wall_time
updated: '2026-05-25T19:27:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目当前无分配 GPU（gpu_ids=[]），所有实验已 DONE，不要尝试提交训练任务
- 论文正文严格 ≤ 8 页（EMNLP 2026）。Fig 5 必须保持 figure*（双栏宽），用户明确要求不能改回单栏
- fig2_pipeline.pdf 已用 ghostscript 压缩（3.1MB→302KB），不要再次替换为未压缩版本
- 匿名 URL `anonymous.4open.science/r/clkc_mech_interp-F894/` 含项目名，用户知情但未要求修改
- 论文数据已修正：probe peak = L15 (47% depth)，不是 L28。任何新文本引用 probe peak 必须用 L15

### 2. 🖥️ 基础设施快照
- 本地工作目录：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/`
- 论文目录：`docs/paper/`（main.tex + 分章节 .tex）
- 图片目录：`figures/paper/`（gen_fig1_hero.py, plot_fig3_layer_probe.py, plot_fig4_asymmetry_forest.py, plot_fig5_fig6.py 等）
- 论文编译：`cd docs/paper/ && pdflatex + bibtex × 3`，当前 main.pdf = 12 页 / 0 错误
- GOOGLE_API_KEY：`/tmp/.google_api_key`（PaperBanana 用）
- 无活跃 GPU 进程 / 无 tmux / 无 cron / 无运行中 Worker
- 全部 78 个实验 DONE（最后一批：steering_qwen_L13-L15, steering_gemma_v2_L17-L18）

### 3. 📊 当前状态
正在等 Worker `fix-fig4-fontcolor`（修复 Fig 4 文字颜色太浅→全部改黑色）完成回调。

刚完成的修复链：
- Fig 2：pdfcrop 无白边 → LaTeX vspace 进一步压缩（-8pt/-10pt/-18pt）
- Fig 4：sans-serif + 字体放大 + 图例 lower right frameon=False（颜色修复 Worker 进行中）
- Fig 5：figure* 双栏宽 + 字体放大至 8-9pt
- 审计修复：3 处 em-dash → 逗号/括号，related_work 引用堆砌拆分，0 占位符/0 泄露
- 页面溢出：多轮修复，当前 Conclusion 在第 8 页内结束

Director 最后指令是 Fig 2 白边 + Fig 4 字体颜色修复后提交 Reviewer 审查。

### 4. 📋 待办
- `fix-fig4-fontcolor` Worker DONE 回调到达 → 读结果 → 视觉确认 Fig 4 文字黑色 + 页数仍 ≤ 8 → 向 Director 汇报"两项修复完成，提交 Reviewer 审查"
- Director 说"提交 Reviewer 审查" → 等 Reviewer 反馈再处理
- 若 Reviewer 发现 Page 12 末页空白问题 → appendix 表格重排（之前标记为"等 Fig 5 双栏后再处理"）
- introduction.tex:27 还有一个 em-dash（`cross-model contrast---all three models`）审计 Worker 发现但未修，Director 未要求修 → 如果 Reviewer 提出再修

### 5. 🎯 战略上下文
- 核心结论：Detection ≠ Decision — 三个模型均线性检测到冲突（probe acc >70%），但只有 Llama 在 L13 有因果效应（p<0.001）。Gemma/Qwen 0/6 alphas 显著。
- 论文 framing：cross-model contrast 是主要证据（不是单模型 layer 对比），probe peak L15 vs causal node L13 的 dissociation 是辅助证据
- 易错点：之前多次因并行 Worker 编辑同一 .tex 文件导致页面重排回归超 8 页。每次编辑后必须编译确认页数。
- Fig 4 的 `inconsolata.sty` 缺失不影响图片生成（只影响 LaTeX 编译的 \texttt 字体），编译 warning 可忽略
- 匿名代码仓库 `artifacts/anonymous_repo/` 结构已完整（22 脚本 + README + LICENSE），但未确认是否已 push 到 anonymous.4open.science
