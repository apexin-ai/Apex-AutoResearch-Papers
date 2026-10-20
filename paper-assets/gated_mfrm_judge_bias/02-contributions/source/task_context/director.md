---
loop: 4
reason: max_messages
updated: '2026-05-25T19:55:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无本地 GPU 分配（纯 API 调用 + CPU 推断项目），所有 MCMC 推断在 autodl-8gpu 上运行
- autodl-8gpu SSH 端口在实例重启后已变更，当前无法连接——不要反复重试旧端口，需用户去 AutoDL 控制台查新端口
- 论文已进入审稿阶段（Review Group C 独立运作），Research Director 不参与论文格式/投稿材料准备
- N=8 pilot 数据（exp-003b）和 N=17 main 数据的归属必须严格区分，之前因混淆导致 4 处数据错误

### 2. 🖥️ 基础设施快照
- 服务器：autodl-8gpu（SSH 端口待更新，当前不可用）
- 工作目录：远程 `/root/autodl-tmp/gated_mfrm_judge_bias/`（推测，需确认）
- 本地论文目录：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/`
- 本地图表目录：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/`
- 图表生成脚本：`gen_forest_dj_v2.py`（Figure 4）、`gen_fig5_6_combined.py`（Figure 5+6 合并图）
- 活跃进程：无（Agent idle，无 RUNNING 实验）
- Paper Agent session：活跃，最近完成 4 项数据审计修复

### 3. 📊 当前状态
刚完成全文数据溯源审计（~120 个数字），发现 4 个确认错误已全部修复（R̂/ESS 归属、p 值精度、四舍五入、百分比）。Paper Agent 确认编译通过，18 页，0 critical warnings。Figure 4 图例白色背景已去除并重新生成。

已完成的大改：Figure 4 重绘为 dot-and-whisker、Figure 5+6 合并为 figure*（lollipop + paired dot）、γ→δ 符号冲突修复、N=8/N=17 数据归属全面修正、page 8 填充。

registry 无 RUNNING/PREPARING 实验。无等待中的 Worker 回调或 Cron。

### 4. 📋 待办
- autodl-8gpu SSH 端口更新 → 连接服务器验证 14 项待确认数据（fill rate ~58%、judge coverage 63-79%、OVB r=0.86、Bootstrap CI、PPC rates 等）
- 14 项验证完成 → 如发现偏差则派 Paper Agent 修正
- 用户确认论文 PDF 满意 → 可提交 `submit_paper_to_review` 触发新一轮审稿
- fill rate 验证 + coverage ablation 中间点实验 → 需 autodl-8gpu 恢复后执行

### 5. 🎯 战略上下文
- 项目核心：G-MFRM 联合建模 judge bias + benchmark contamination，目标 EMNLP 2026
- 论文 story 已稳定：G-MFRM 在合成数据上 RMSE -51% / τ 提升显著；真实数据主要贡献是可解释的 contamination 诊断而非排名提升（coverage 不足导致 over-correction，已通过 coverage ablation 解释）
- 写作已经过 3 轮 Reviewer 对抗收敛（Overall 7/10）+ 完整数据审计
- 易错点：论文中 N=8 和 N=17 的数字来源不同实验，混用会导致 reviewer 质疑数据可靠性——任何新增数字必须标明来源
- 审稿阶段已启动（review_chat_id 存在），Review Director + 2 Reviewers 独立工作
