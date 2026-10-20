---
loop: 27
reason: max_wall_time
updated: '2026-05-25T20:16:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目当前 **无分配 GPU**（纯论文写作阶段），不要尝试提交训练实验
- TOST sensitivity 数据有两个易混淆的源文件：`tost_sensitivity.json`（CLS-CWM, seed-level paired）和 `tost_margin_sweep_v2_results.json`（CLS-TRAJ, clustered bootstrap）。**两个文件的 header 都标注了错误的 comparison 名称**，必须以 mean_diff 值区分（1.24=CLS-CWM, -0.45=CLS-TRAJ）
- `tost_sensitivity_full.json` header 写 "CLS vs TRAJ" 但 mean_diff=1.24，实际是 CLS-CWM 数据，不要被 header 误导
- Figure 3 已用正确数据重新生成，画图脚本在 `artifacts/figures/paper/plot_tost_sensitivity.py`，PDF 同时存在于 `artifacts/` 和 `docs/paper/figures/paper/` 两处，改图需同步更新两处

### 2. 🖥️ 基础设施快照
- 本地工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/`
- Python（画图/分析）：`.venv/bin/python`（Python 3.14，含 matplotlib/scipy/numpy）
- 论文源码：`docs/paper/`，用 `pdflatex` 编译，ACL review 模板
- LaTeX 依赖已装齐（含 texlive-fonts-extra for inconsolata.sty）
- 无活跃 GPU 进程 / Worker / Cron
- Registry: 267 个实验，全部 DONE

### 3. 📊 当前状态
**刚完成**：全文数据真实性审计 + 3 个修复 + Figure 3 重新生成

修复清单（已完成）：
1. ±1.52pp → ±1.63pp（CLS-CWM 最小等价 margin）：experiments.tex 3 处 + appendix.tex 3 处 + Figure 3 图内标注
2. CWM 8B std 1.15 → 1.14（Table 3）
3. unparseable 范围 51-74% → 53-74%（§4.5 taxonomy 段）

编译验证通过：22 页（主文 8 + 参考 2 + appendix 12）。

**等待**：Director 确认审计报告 + 修复结果。无 pending Worker/Cron 回调。

### 4. 📋 待办
- Director 确认修复无误 → 无进一步动作（审计任务闭环）
- Director 要求提交前其他检查（reference audit / visual review 等）→ 派 Worker 执行
- Director 指示新实验方向 → 读 ROADMAP.md 了解当前短期计划，申请 GPU

### 5. 🎯 战略上下文
- 项目处于 **论文投稿准备阶段**（EMNLP 2026 ARR），核心实验全部完成（267 runs），当前焦点是论文质量
- 核心结论：function-level CLS≈CWM（TOST p=0.007, ±2pp），repo-level CLS>>CWM（18-26pp gap），TRAJ 等价性 Holm 校正后 inconclusive
- 审计中 5 个无法独立验证的数字（2 个 DeepSeek prompting baseline、CLS 4B seed 456 隐含值、mixed-effects 系数、compute budget）均非核心 claim，已向 Director 报告保留理由
- **易踩坑**：论文中 CLS-CWM 和 CLS-TRAJ 的 TOST 分析使用不同统计方法（seed-level paired vs clustered bootstrap），不要混用。Appendix J 表格已改为 seed-level paired (df=4)，与 §4.4 主文一致
- ACL 模板已对齐官方版本（上一轮 session 完成），8 页限制满足
