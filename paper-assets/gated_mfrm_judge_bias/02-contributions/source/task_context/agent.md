---
loop: 3
reason: max_wall_time
updated: '2026-05-25T19:55:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- **AutoDL SSH 端口已变**，当前 ~/.ssh/config 连不上 autodl-8gpu。需用户查 AutoDL 控制台获取新端口后更新配置，否则所有 SSH Worker 会失败
- 论文数据归属：N=8 pilot 数据来自 exp-003b（9 judges），N=17 数据来自 exp-020（6 judges）。**不要混用**——上一轮审计发现 R̂/ESS 值被错误归属到 N=8（实际来自 N=17）
- 论文 c_n 值在正文/Table 8 用 1dp 精度（5.6, 4.2），在 Table 9 bias absorption 用 4dp 精度（5.587, 4.168）。**两套精度是一致的格式选择**，不要"修正"为不统一的精度
- Figure 5+6 已合并为 figure*（fig5_6_combined），label 是 `fig:contamination_and_bias`，旧 label `fig:contamination_bars` 和 `fig:bias_absorption` 已不存在

### 2. 🖥️ 基础设施快照
- **服务器**: autodl-8gpu（SSH 端口已失效，需更新）；rtx6000-4x（状态未知）
- **本地工作目录**: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/`
- **论文目录**: `docs/paper/`，编译命令 `pdflatex -interaction=nonstopmode main.tex`（需两遍解决引用）
- **图表脚本**: `figures/paper/gen_fig5_6_combined.py`（合并图），`gen_forest_dj_v2.py`（judge severity），`gen_fig6.py`（旧两面板，已废弃）
- **活跃进程**: 无。PID 29577（exp-009 zombie）已 kill，194GB GPU 内存已释放
- **Cron**: 无活跃 cron（上次 reconcile 时全部完成）
- **Registry**: 22 个实验，全部 DONE/ALLOCATED/killed/failed，无 RUNNING

### 3. 📊 当前状态
**刚完成**: 全文数据真实性审计（~120 个数字逐一对账），发现 4 个确定性错误已汇报 Director，等待修复指令。Figure 5+6 合并为 figure* 并经过两轮 Director 反馈修改（width_ratios 和 panel label 位置），已编译验证。

**等待中**:
- Director 决策：4 个审计错误的修复方案（特别是 #1 R̂/ESS 归属）
- Director 决策：数据归属问题（N=8 vs N=17 混用、sequential vs staged 数字）的全局修复方案
- Director 决策：diagnostic framing pivot（exp-020 所有变体 Δτ≤0，方法改进空间耗尽）
- 用户操作：AutoDL SSH 端口更新（阻塞所有服务器端验证任务）

### 4. 📋 待办
- Director 批准审计修复 → 修改 experiments.tex 4 处：(1) R̂/ESS 归属改为 N=17，(2) p<10^{-6} 改为 p<10^{-5}，(3) "within 0.014" 改为 "within 0.015"，(4) appendix θ-RMSE +2.4% 改为 +1.9%
- SSH 端口恢复 → 验证 ~58% fill rate、63-79% judge coverage、r=0.86 等 14 个待验证数字
- Director 决定 framing pivot 方向 → 按 red-section skill 产出提案或维持 diagnostic framing
- ACL 官方模板对齐 → 尚未启动，等 Director 排期

### 5. 🎯 战略上下文
- **核心结论**: G-MFRM 在合成数据上显著优于 sequential（RMSE -51%, p<10^{-5}），但在真实数据上 Δτ=-0.044（负向）。根因是 53.8% items 缺少 exposure 估计，gating 机制"半盲"。已通过 coverage ablation 证明 Δτ 随 coverage 单调趋近 0
- **决策链**: exp-020 negative → 7 个诊断变体全部 Δτ≤0 → 方法改进空间耗尽 → 推荐 diagnostic framing（G-MFRM 的价值是 contamination diagnostics，不是 ranking improvement）→ 等 Director 决策
- **易错点**: (1) 不要尝试再跑更多 MCMC 变体——已穷尽，都不 work。(2) exp-004 中 N=8 raw_average=0.8095 ≠ exp-003b 的 0.786，因为前者用不同 judge 子集计算。(3) 论文中"51% RMSE reduction"来自 exp-w7-ablation staged vs full (0.2539→0.1243)，不是 exp-015 或 exp-018
- **DDL**: EMNLP 2026 ARR 提交截止 2026-05-26（明天），所有修改必须今天完成
