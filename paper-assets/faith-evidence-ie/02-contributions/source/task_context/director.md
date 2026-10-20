---
loop: 13
reason: max_messages
updated: '2026-05-23T22:48:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 匿名仓库 git author 泄漏尚未修复（committer 暴露 AWS ap-northeast-1），Agent 重置前队列里有修复指令但未执行，新 session 必须优先处理
- 14B 定位为 "validation scale"（n=2），论文中 14B 相关 claim 必须用 hedged 语言，CI 跨零时不能说 "substantial"
- EDCR 公式已改为 distractor citation rate（method.tex eq:edcr），与代码实现一致。不要回退到旧的 Evi-Recall_TP/Rel-Recall 定义
- 4B 主表用 n=3（去掉 s45），附录透明报告 n=4。不要把 s45 加回主表
- DPO 3ep 用旧协议（已 footnote 标注），不要重跑

### 2. 🖥️ 基础设施快照
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/`
- 论文目录：`docs/paper/`，主文件 `main.tex`，编译用 pdflatex
- 匿名 GitHub 仓库：需要 Agent 确认具体 URL（上轮 Agent push 过但 session 已重置）
- 4 张 GPU 空闲（具体 device id 需 `get_project_status` 确认）
- 远程服务器信息需重新通过 `list_ssh_hosts` 获取

### 3. 📊 当前状态
**刚做完**：
- 14B RSFT s43 eval 处理完毕，全表更新为 2-seed mean（experiments.tex + appendix.tex ~17处编辑）
- EDCR 公式从 recall ratio 改为 distractor citation rate（method.tex L63-72）
- 跨表一致性修复（tab:scaling, tab:test_results, tab:encoder_comparison, tab:cross_detail 全部对齐）
- Reviewer 完成 claim-evidence 覆盖率审查：3 个 contribution 覆盖充分，无 blocking gap
- Round 3 审稿已提交（`apr_20260523T222455_tbtd`），等待用户审批选择 continue/fresh 模式

**未执行的 Agent 任务**（队列里但 Agent 重置前未处理）：
1. 匿名仓库 git author 清洗（**最高优先级**）
2. 4B RSFT s44 no-evi test eval（~2h GPU）
3. Inference efficiency 对比表整理（artifacts/efficiency_comparison.md）

### 4. 📋 待办
- Agent 新 session 启动 → 立即重新派发：(1) git author 清洗 (2) 4B test eval (3) efficiency 表
- Round 3 审稿报告回来 → 按 `review-report-action.skill.md` 逐条处理，不要整体"已知悉"
- 4B test eval 完成 → 更新 test 表格数据
- 用户审批 Round 3 review mode → 等待审稿团队报告

### 5. 🎯 战略上下文
- 项目处于**审稿打磨阶段**，EMNLP 2026 ARR July cycle（DDL 2026-07-17）
- 三个核心 claim：(1) scale-dependent evidence tax (2) gradient pressure causes decoupling (GRPO→DPO→RSFT spectrum) (3) RSFT reduces variance via output filtering
- 覆盖率审查结论：22/30 实验完成，全部 P0 done，九维 7/9 达标
- 主要审稿风险点：数据集=2（CDR/GDA 无 evidence 标注不可行）、DPO 3ep 旧协议、EDCR 无人工验证——均有应对方案
- 易错点：review_issues.yaml 有 20+ 历史 issue，处理新审稿报告时必须先读它了解已解决/未解决状态，避免重复处理或遗漏
- 4B no-evi 3-seed tax 已确认：+1.65±0.29pp（matched@2048），evidence 在 4B 几乎 neutral
