---
loop: 22
reason: max_wall_time
updated: '2026-05-25T19:12:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- **用户已于 2026-05-25 05:34 下令停止所有实验**。不得在任何 GPU 上启动新训练，不得准备新实验配置。项目处于等待 ARR 审稿结果阶段。
- bjb1-17606 cuda:0 是本项目唯一分配的 GPU，但当前处于停用状态。
- Worker `scienceworld_cell_d_episode` 已被 kill 并标记 `conclusion=killed`，不要尝试恢复。
- 已有 SFT checkpoint 和 hsweep 数据保留不动，禁止删除。

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，账号 root，工作目录 `/root/cost-verify-agent-rl`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型路径：`/root/autodl-tmp/checkpoints/` 下有各 SFT 和 GRPO checkpoint
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/`
- W&B project：`cost-verify-agent-rl`
- 活跃进程：**无**（全部已停止）
- Cron：可能有残留 cron 监控 `scienceworld_cell_d_episode`，BOOT 后 `reconcile_crons` 会清理

### 3. 📊 当前状态
刚完成论文提交前最后一轮修改，所有改动已编译确认：
- **P0 去 AI 风格**：全文 12 处 em-dash `---` 替换为逗号/括号/拆句
- **P1 叙事一致性**：Abstract "additionally removing"；experiments "suggest" 替代 "confirm"
- **P2 符号一致性**：window index $k$ → $w$（method.tex / theoretical_analysis.tex / appendix.tex，约 20 处）
- **Figure 2** Y 轴裁切修复（`pad_inches=0.3`）
- **Figure 7a** SFT baseline 改为虚线 + legend（`loc='lower right'`）
- **附录引用完整性**：补了 `app:method_selection` 和 `app:step5_unified` 的正文引用
- **ACL 模板对齐**：删除 3 行自定义浮动间距覆盖；`acl.sty` / `acl_natbib.bst` 与官方一致
- **匿名仓库链接**：已改为 `https://anonymous.4open.science/r/cost-verify-agent-rl-52D4/`
- **页数**：主正文恰好 8 页，Limitations 从 p8 底延续到 p9，References p9-10，Appendix p11-16，总 16 页

Registry 中无 RUNNING/PREPARING 实验。无等待中的 Worker 回调或 Cron。

### 4. 📋 待办
- ARR 审稿结果到达 → Read `rebuttal` skill → 按审稿意见逐条写 response
- Director 要求恢复实验 → 先确认 GPU 分配（当前 cuda:0 停用），再走正常审批流程
- Director 要求 Framing 调整 → Read `red-section` skill 产出提案

### 5. 🎯 战略上下文
- 论文核心 claim：step-independent training 的 dual mechanism（M1 信息损失 + M2 sign misattribution）导致 collapse；episode-level GRPO 结构性消除两者但 seed-dependent（36% 泛化）
- 11-seed mean OOD = 17.7%（非 17.2%），SFT baseline = 6.72%
- ScienceWorld Cell D 实验被 kill，registry 里 `conclusion=killed`。如果审稿要求补 ScienceWorld episode-level 结果，需要 Director 重新批准 GPU 使用
- 易错点：论文中 window index 现在是 $w$，rollout index 是 $k$，不要混淆。之前 session 已全文替换完成
