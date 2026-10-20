---
loop: 15
reason: max_wall_time
updated: '2026-05-25T05:27:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-11235 的 GPU 白名单需查 `execution.gpu_ids`（本项目实验已全部完成，当前无训练进程）
- 论文 PDF 编译必须在远程 `/root/trace-verdict-study/docs/paper/` 执行（本地 TeX Live 版本不同会产生 ~15KB PDF 差异）
- 本地 workspace 与远程存在双源架构：论文/文档在本地 `projects/trace-verdict-study/docs/paper/`，训练代码/checkpoint 在远程 `/root/trace-verdict-study/` 和 `/root/autodl-tmp/trace-verdict-study-checkpoints/`
- `check_figures_and_layout` 工具有已知 false positive：6 个 "missing_image" critical 是因为不识别 `\graphicspath`，PDF 实际编译 0 errors

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235(root)，工作目录 `/root/trace-verdict-study`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/`
- 论文源文件：`docs/paper/`（main.tex + 6 个 section tex + appendix.tex + references.bib）
- 图表：`figures/paper/`（fig1_trace_overview.pdf, fig2_calibration.pdf, fig3_cross_model_gap.pdf, budget_curve.pdf, training_dynamics.pdf）
- Checkpoints：`/root/autodl-tmp/trace-verdict-study-checkpoints/`（exception_only, full_trace, qwen7b_full_trace_seed{123,456} 等）
- 无活跃训练进程，无 cron 任务，无 wandb 活跃 run

### 3. 📊 当前状态
**阶段**：EMNLP 2026 ARR 投稿日（2026-05-25），论文处于最终修订状态。

**刚完成**：Round 18 reviewer response 全部修复的 claim-evidence 交叉验证。结果：7/8 项 PASS，1 项残留（experiments.tex:139 和 :144 两处 "attributes" 旧措辞需改为 "places an upper bound"）。已 post 给 Director。

**最新 PDF**：远程编译通过（21 页，正文 ≤8 页，0 errors）。fig1 刚由 worker_figure_fig1-final-v3 更新，远程已编译成功（473KB）。

**Registry**：全部实验 DONE。无 RUNNING/PREPARING。

**等待中**：Director 处理我上报的 experiments.tex 2 处残留旧措辞 + 触发最终编译验证。

### 4. 📋 待办
- Director 确认修复 experiments.tex:139/144 → 验证修改正确性（"places an upper bound" 替换 "attributes"）
- 最终编译 worker 完成 → pdf_to_images 验证 page 8-9 边界仍合规（≤8 页正文）
- 若 Director 要求 paper_provenance 审查 → `read_project_file("paper_provenance.yaml")` 检查覆盖率
- 若收到新 reviewer comments（Round 19+）→ 按审查模式 B 执行对抗审查

### 5. 🎯 战略上下文
**核心结论**：complete traces degrade SFT verdict prediction by 18-23pp vs exception events；gradient masking bounds gradient dilution to ≤4%（within-format upper bound）；real mechanism = low signal density → exceed context window → right-truncation discards diagnostic tail。

**Paper 叙事已稳定**：从 "information density effects" 角度讲 degradation story，不再讲 "why exceptions help"（那是 tautological）。

**易错点**：
1. 论文有两种 "truncation"——pre-processing truncation（外部 budget，已排除）vs context-window truncation（model max_length，真正的 proximate mechanism）。混用会被 reviewer 打回。
2. Registry 中 `full_trace_seed{123,456}` 的数字（79.58/80.50）与论文使用的 `qwen7b_full_trace_seed{123,456}`（80.17/82.35）不同——论文数字正确（对应磁盘 eval_results.json），registry 过时但未更新。不要误判为 paper error。
3. 上传飞书的 PDF 可能是本地编译版（~511KB），远程最新版（~473-527KB）因 TeX Live 版本差异大小不同，内容一致。
