---
loop: 1
reason: max_wall_time
updated: '2026-05-25T19:29:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 分配（gpu_ids=[]），所有实验均为 CPU 模拟（Monte Carlo），不要尝试提交 GPU 训练任务
- 论文源码路径：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/`，远程服务器 `local-cpu` 上有实验脚本和结果 CSV，但本地无 Python 实验脚本
- PaperBanana 必须用 `--vlm-model gemini-2.5-pro`（默认 gemini-2.0-flash 已废弃会崩溃），venv 在 `/home/ubuntu/.paperbanana_venv/`
- 论文 EMNLP 2026 ARR：正文 8 页硬限，abstract ≤ 200 words，limitations 放正文不放 appendix，"8 LLMs"（不是 11），"Prop. 5"（不是 Prop. 2）
- AUC 数字已从 0.66 修正为 0.96（scalar diagnostic under asymmetric errors），三个文件已同步（theory.tex, experiments.tex, appendix.tex）

### 2. 🖥️ 基础设施快照
- 本机 EC2（ap-northeast-1），工作目录 `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/`
- 远程 `local-cpu`：实验数据在 `results/` 目录（exp_fl_comparison_summary.csv 等），无 GPU
- PaperBanana venv：`/home/ubuntu/.paperbanana_venv/`（pip install paperbanana）
- 论文 figures 目录：`docs/paper/figures/`
- 无活跃进程、无 tmux、无 cron 任务
- GOOGLE_API_KEY 需每次通过 `request_secret` 审批获取

### 3. 📊 当前状态
**刚完成**：fig_combined_overview v3（PaperBanana 分段生成：上半 Panel a+b + 下半 Panel c+d → PIL 拼接）。本次成功用 PaperBanana 出图（前两次都回退 matplotlib）。

**等待 Director 决策**：fig_combined_overview v3 有两个小偏差：
1. Row 3 结果卡片是深 teal 而非指定的 dark navy (#2C3E50)
2. Panel (b) 公式分母 "1−2π" 缺 overbar（应为 π̄）

Director 选项：A. 接受当前版本 / B. PIL 后处理换卡片颜色 / C. 重新迭代下半部分

**本 session 已完成的其他任务**：
- fig_overview.pdf（4-panel overview，PaperBanana V4）
- fig_method_overview.pdf（双行流程图，PaperBanana 1 轮通过）
- tab:fl_comparison 3 处文字修复（signed vs unsigned bias 叙述问题）
- R22 reviewer 修复（Fix 5 PPCI, Fix 7 A3 relaxation, Task 8 AUC 0.96, Task 9 Corollary 4）

**Registry**：无 RUNNING/PREPARING 实验。成功 34 / 负向 6 / 失败 0。

### 4. 📋 待办
- Director 回复 fig_combined_overview 决策 → 按指示执行修复或接受
- Director 决定如何在 LaTeX 中替换 Figure 引用（fig_overview + fig_method_overview → fig_combined_overview）→ 派 Worker 改 .tex
- 编译论文 PDF 验证所有图表修改无报错 → 可能需要 Worker SSH 到有 LaTeX 的环境
- exp-027b（CausalForest coverage gap 诊断）仍在 PREPARING 但无 GPU 分配，等 Director 决定是否推进

### 5. 🎯 战略上下文
- **论文核心 story**：LLM annotation 的 misclassification error 在 subgroup 间异质 → global correction 引入 bias 甚至 sign reversal → EC-HTE 用 per-subgroup HB confusion matrix inversion 消除 → 7.4× bias reduction, 0% sign reversal, ≥93% coverage
- **PaperBanana 使用经验**：复杂图（≥3 panel）一次生成大概率失败。分段策略有效：分成 2-3 个子图各自生成再拼接。gemini-2.5-pro 的 VLM critic 有时返回 None 导致 JSON 解析错误，重试通常能解决。PaperBanana 对精确颜色控制有限（如 navy vs teal），需要后处理或多轮迭代
- **易错点**：fig_overview（4-panel 概览）和 fig_method_overview（双行流程图）和 fig_combined_overview（合并版）是三个不同文件，Director 最终决定用哪个替换 Figure 2。不要混淆
- **fl_comparison 不是 bug**：0.064 vs 0.008 来自不同 DGP（Δτ=0.3 vs ≈1.0），"near-zero bias" 指 signed bias 而非 unsigned |Bias|。已修复叙述但数据本身正确
