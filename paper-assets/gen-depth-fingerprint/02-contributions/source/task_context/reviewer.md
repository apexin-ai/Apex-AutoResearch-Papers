---
loop: 10
reason: idle_timeout
updated: '2026-05-24T21:50:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `bjb2-18868`，本项目代码根目录 `/root/gen-depth-fingerprint`
- 论文在**本地** `artifacts/_project/paper/`——审查论文内容用 `Read`，不是 `ssh_read_only`
- 实验数据 JSON 在**服务器** `/root/gen-depth-fingerprint/results/`——审查数值溯源必须 `ssh_read_only` 读服务器 JSON
- 服务器备份已拉到本地：`artifacts/server_backup/experiment_outputs.tar.gz`（209 JSON + 64 CSV），服务器到期后可用此核查
- QLoRA 实验实际协议是 **4-gen 5-fold stratified CV**（非 LOGO），baseline 来自 `plan012_xgboost_matched.json`

### 2. 🖥️ 基础设施快照
- 服务器：`bjb2-18868`，工作目录 `/root/gen-depth-fingerprint`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`
- 论文 tex：`artifacts/_project/paper/`（本地）
- 实验结果 JSON：`/root/gen-depth-fingerprint/results/`（服务器）
- 无活跃进程、无 tmux session、无 cron 任务（项目已完成实验阶段）
- 匿名 repo 已 push（commit `214304f` 含最终交叉引用修复）

### 3. 📊 当前状态
全部审查工作已完成。本轮（Loop #10）完成了：
- **3 CRITICAL 全部修复确认**：±3-4% batch estimation 删除 ✅、QLoRA 协议统一为 4-gen 5-fold CV ✅、instruct F1=0.487 删除 ✅
- **2 WARNING 全部修复确认**：η² 比较对象修正 ✅、QLoRA 表格协议混用修正 ✅
- **Abstract "6-gen LOGO" 修复确认** ✅
- **appendix cross-ref 新增验证通过**（human-edit 8pp 核实、downstream null-result 核实、LaTeX 无 undefined ref）
- Registry: 0 RUNNING / 0 PREPARING，68 total（48 success, 2 negative, 12 failed, 6 killed）
- 无等待中的 Worker / Cron / Director 决策

### 4. 📋 待办
- 论文提交后收到审稿意见 → 按 rebuttal skill 流程处理
- 若 Director 要求额外数据核查 → 服务器 JSON 或本地 `artifacts/server_backup/` 均可用
- 若发现新的数值不一致 → 优先核对服务器 JSON 原始数据，区分本地 tex 版本与服务器数据
- N/A（当前无 pending 条件触发项，项目处于提交等待状态）

### 5. 🎯 战略上下文
- 项目核心结论：递归生成产生可分解的 depth response（location drift + shape stationary），支持跨 generator 深度分类
- DDL: EMNLP 2026 ARR 2026-05-25，论文已完成最终修复，匿名 repo 已 push
- **最容易判断错的事**：论文中多个实验用不同协议（8-gen LOGO / 5-gen cross-model LOGO / 4-gen 5-fold CV / within-model 5-fold CV），不能跨协议比较 delta。核实数值时必须先确认对应 JSON 的 `cv_type` / `method` 字段
- **容易踩的坑**：`docs/paper/` 和 `artifacts/_project/paper/` 是两份拷贝，可能不同步——以 `artifacts/_project/paper/` 为准（编译源）
- discussion.tex 的 η² 数值来自两个不同 ANOVA：主 ANOVA（variance_decomposition，N=37058）vs cross-model ANOVA（appendix_cross_model_detail，N=3778），前者 η²_gen=0.017-0.024，后者 η²_gen<0.009
