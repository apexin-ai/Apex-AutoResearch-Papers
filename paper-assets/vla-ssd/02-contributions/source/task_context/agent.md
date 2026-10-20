---
loop: 15
reason: max_wall_time
updated: '2026-05-28T21:37:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 分配（纯分析/写作项目），不要尝试提交训练任务
- 论文正文严格 8 页（含 Limitations），References 从 p9 开始；p2-p8 每页必须有 ≥1 figure/table
- 所有 main-body float 只用 `[t]`，禁止 `[htbp]`/`[b]`/`[h]`/`[p]`（wrapfigure 豁免）
- `experiments.tex` 中 fig:result_matrix / fig:action_r2_threecond / fig:counterfactual_bar 三个 label 定义在 experiments.tex 开头的 3-panel composite figure 上（method.tex 不再有这个 figure），**不要在 experiments.tex 中再添加这三张图的 standalone 版本**——之前 Worker 误操作添加过导致 duplicate labels + 页数溢出
- counterfactual bar 图中 TraceVLA Spatial 和 Object 的 wrong/shuffled 条件值存在交换问题（已报告 Director，尚未修复）

### 2. 🖥️ 基础设施快照
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/`
- 论文源码：`docs/paper/`（main.tex 入口，pdflatex 编译）
- 绘图脚本：`scripts/`（plot_*.py, gen_fig_*.py）
- 实验产出：`artifacts/` 及 `artifacts/_project/data/`（JSON 格式原始数据）
- 无远程服务器、无 GPU、无活跃进程、无 cron 任务
- 编译命令：`cd docs/paper && pdflatex -interaction=nonstopmode main.tex`（需跑两遍）

### 3. 📊 当前状态
**刚完成**：
1. Figure 3 色系优化（学术蓝 + Tol orange 边框）、Figure 7 字体修正（Times New Roman）— 已重新生成 PDF
2. 排版修复：移除 3 个 duplicate figure、重建 3-panel composite、移动 synthesis_panels 到 FloatBarrier 后 → 8 页正文 + p2-p8 每页有 float ✓
3. DDL 前数据完整性抽检 — 已向 Director 汇报结果

**等待 Director 决策**：
- counterfactual bar wrong/shuffled 交换问题是否需要在 DDL 前修复（改脚本 2 行 + 重出图）
- plot_action_r2_threecond.py 数据源不一致是否需要调查（可能是不同 readout token 导致的合理差异）

**Registry**：无 RUNNING/PREPARING 实验（纯写作阶段）

### 4. 📋 待办
- Director 指示修 counterfactual bar → spawn Worker 改 `scripts/plot_counterfactual_bar.py` 中 TraceVLA Spatial/Object 的 wrong↔shuffled 值 → 重新生成 `fig_counterfactual_bar.pdf` → 编译验证排版不变
- Director 指示调查 threecond 数据源 → spawn Worker SSH 到实验服务器查原始 log，确认 readout token 类型
- Director 指示提交 → 编译最终 PDF → `register_artifact` + `backup_project_to_s3`
- 任何 tex 文件修改后 → 必须双遍 pdflatex + 验证：(a) 无 undefined/multiply-defined labels (b) p2-p8 每页有 float (c) 正文 ≤ 8 页

### 5. 🎯 战略上下文
- **论文核心结论**：VLA instruction routing 可分解为 training-associated effects（exit collapse, counterfactual sensitivity）和 inherited base-model priors（L1 attention routing）。跨 3 个架构一致。
- **DDL 2026-05-29**（明天），目标会议 CoRL 2026
- **数据完整性风险**：gen_fig_matrix_heatmap + Table 3 数据已验证 ✓；其余 3 个脚本存在不同程度的数据溯源问题（详见上一轮 Director 汇报）。最严重的是 counterfactual bar wrong/shuffled 交换——影响图中 2 个 bar 的标签，但不影响论文文字中的定量 claim（文字只报告 range 和 ranking，不引用单个条件的具体 d 值）
- **易错点**：experiments.tex 的 float 布局极度敏感——任何图片尺寸/位置变化都可能导致排版级联崩坏。修改后务必编译 + 逐页视觉检查（pdftoppm 渲染 PNG）
