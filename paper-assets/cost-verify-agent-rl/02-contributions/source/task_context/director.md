---
loop: 19
reason: max_messages
updated: '2026-05-25T14:55:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-17606 cuda:0（唯一分配的 GPU，之前误记为 2 张）
- 用户已在 2026-05-25 05:34 明确下令停止所有实验，包括 Cell B 多种子——不要重启任何训练
- 匿名仓库推送用 GitHub PAT（secret vault: `github_anon_pat`，username: `caoxiaoyu001`），论文中链接必须用 `https://anonymous.4open.science/r/cost-verify-agent-rl-52D4/`，不能用 GitHub 链接
- DDL 2026-05-25 AoE 已过，当前处于等待 ARR 提交/审稿结果阶段

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606 (connect.bjb1.seetacloud.com)，用户 root
- 工作目录：`/root/cost-verify-agent-rl`
- GPU：1× NVIDIA RTX PRO 6000 (96GB)，cuda:0，当前空闲
- 论文源码：`projects/cost-verify-agent-rl/docs/paper/`（本地 workspace）
- 图表生成脚本：`docs/paper/gen_fig_*.py`（在 bjb1 上运行生成 PDF/PNG）
- 活跃进程：无（全部 kill + tmux 清理完成）
- W&B：未配置；Git：未配置

### 3. 📊 当前状态
DDL 当天完成了大量论文排版和数据修复工作：
- **数据一致性审计**：修复 3 处（Abstract 17.2→17.7%、Figure 5 seed100 11.19→12.69%、Figure 6a 1.5→1.6%）
- **去 AI 风格**：12 处 em-dash 全部清除
- **符号一致性**：window index k→w，约 20 处替换
- **叙事一致性**：Abstract "additionally removing"、experiments "suggest" vs "confirm"
- **Figure 修复**：3b 双 seed 黑点+图例、4 移到 P7 右栏、6 配色+标签、7a SFT→legend、2 Y轴裁切
- **匿名仓库**：推送完成，论文脚注改为 anonymous.4open.science 链接
- **附录引用**：补了 Appendix E/G 的正文引用
- Registry 无 RUNNING 实验，36 个 PREPARING 状态实验已全部取消

### 4. 📋 待办
- 用户要求编译最新 PDF → `/paper-pdf` 生成并发群
- 收到 ARR 审稿结果 → 按 `review-report-action` skill 处理
- 用户要求继续实验（如 rebuttal 阶段补实验）→ 重新分配 GPU、参考 36 个 pending 实验优先级
- Round 6 审稿 Overall 3.0 (Findings)，若需提分 → Cell B 多种子 + ternary corollary 是最高杠杆

### 5. 🎯 战略上下文
- 论文定位：diagnostic paper（非 method paper），核心贡献是 M1/M2 双机制理论框架 + partial factorial 实验
- 结构性天花板（Round 6 审稿共识）：solution 无新颖性（episode-level GRPO = 原版回退）、Cell C 永久缺失（NaN 崩溃）、无同期方法实验对比——这些无法通过 rebuttal 解决
- 可改善项：Cell B 多种子（N2 Critical，用户叫停前只跑了 seed100 部分）、ternary corollary（W1）、Eq.6 多时间点（W2 已部分修复为 break-even 分析）
- 易错点：不要主动建议降级到 workshop/低级别会议（硬约束 L1）；不要在用户未授权时重启实验；Figure 修改后必须在 bjb1 上重新运行生成脚本再编译，本地 workspace 没有 Python 环境
