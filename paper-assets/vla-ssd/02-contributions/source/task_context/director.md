---
loop: 15
reason: max_messages
updated: '2026-05-28T21:37:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目分配的 2 张 GPU 一直空闲，已连续 8 轮被 System 催促。用户未确认释放，不要擅自归还，但也不要启动新实验——等用户回复
- 论文 PDF 中的数据必须与 Appendix Table 5 (tab:counterfactual) 一致——刚修过 Figure 5 的 wrong/shuffled 交换错误，任何重新生成 figure 都要交叉验证
- CoRL 2026 DDL 是 2026-05-29，提交需要用户本人在 OpenReview 操作，我们无法代替
- `\enlargethispage` 和全局 `\setlength` 间距 hack 禁止使用（R15-N4/R17-N4 反复被 Reviewer 打回）

### 2. 🖥️ 基础设施快照
- 本地工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/`
- 论文源码：`docs/paper/`（main.tex 入口），PDF：`docs/paper/main.pdf`（39 页，已编译）
- 绘图脚本：`scripts/plot_*.py` 和 `scripts/gen_fig_*.py`，输出到 `docs/paper/figures/` + `artifacts/figures/paper/`
- 提交材料：`docs/paper/submission_fields.md`（title/abstract/keywords/TL;DR 全部就绪）
- 无活跃远程服务器进程、无 tmux session、无 cron 实验任务
- Python 路径：`python3`（系统无 `python` 命令）

### 3. 📊 当前状态
**论文终稿已就绪，等待用户提交。**

刚完成的工作：
- 正文压页（Conclusion 6→5 句，Limitations 4→3 句，Synthesis 末句精简）→ 恰好 8 页
- Figure 5 数据修正（TV-S/TV-O wrong/shuffled 交换 + OV-S/OV-L 四舍五入）
- Figure 7 L1 head count 25→24（与论文正文一致）
- 补了 tab:cf_summary 孤儿表引用
- Reviewer 终稿审查 PASS（0 critical / 0 warning after fix）
- Agent 做了全部 figure 数据完整性抽检，Table 1 全部匹配，Figure 4 R² 偏移确认为不同 readout token 的合理差异

Registry：无 RUNNING/PREPARING 实验。107 个实验全部完成。
等待中：用户回复（OpenReview 提交确认 + GPU 释放确认）。

### 4. 📋 待办
- 用户回复确认提交 → 如需要，用 `feishu_upload_file` 上传 PDF 到飞书方便用户下载
- 用户确认 GPU 释放 → `director_post_to_manager` 正式请求释放 2 张卡
- 用户要求修改论文内容 → 改完后必须 `paper_compile_and_check` + 验证仍 ≤8 页
- 如果审稿卡片被用户批准（apr_20260528T185407_eln2）→ Review Director 会启动新一轮审稿，但论文已 PASS，这轮审稿结果仅供参考

### 5. 🎯 战略上下文
- 项目核心结论：VLA fine-tuning 产生两种可分离模式——exit collapse + counterfactual sensitivity 是训练关联的（VLM→VLA 显著，VLA→VLA 不显著），L1 attention routing 继承自预训练 backbone
- 论文 17 轮审稿迭代，关键决策链：R12 标题从 declarative→descriptive、R14 N=2 overclaim 降格、R15 统计框架从 sign test→effect-size+CI、R16 setlength 全部移除+Discussion/Conclusion 合并、R17 enlargethispage 移除+动态语言清理
- 结构性局限（open issues，wont_fix）：scope fit（纯 representational，无物理机器人）、LIBERO-only、open-loop only——这些在 Limitations 已充分承认，由 AC 判断
- 易错点：不要重新引入 `\enlargethispage` 或间距 hack 来"修复"页面布局——这是 Reviewer 反复打回的红线
- Figure 数据一致性刚修过，任何 figure 重生成后必须与 Appendix 表格交叉验证
