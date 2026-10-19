---
loop: 30
reason: max_messages
updated: '2026-05-29T13:20:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- 全面停机指令（用户 05-28 下达）仍然有效，未被撤销。不要在用户明确恢复前启动实验
- 论文数据锁定（D184）：Table 1 / Table 3 数据不可修改
- GPU 白名单以 `get_project_status` 返回的 gpu_ids 为准，4 台服务器全部不可达（截至 05-29）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-18228 / bjb1-32546 / bjb2-28827 / cqa1-32758 — **全部不可达**（SSH 连接失败，AutoDL 实例可能已关机/端口变更）
- 本地论文路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/`
- 远程代码路径：`/root/acr-vla-conformal-refinement`（各服务器，当前均不可达）
- 活跃进程：无。0 个 Worker，0 个实验 RUNNING

### 3. 📊 当前状态
- 刚完成：Limitations section 修改（删 seed limitation → 换 fixed gating threshold τ）+ 附录 `\clearpage` 分页。Reviewer PASS
- 修改在本地文件，未同步到远程（服务器不可达）
- 飞书 API 配额耗尽（本月），无法向用户发消息
- **三个问题悬而未决**（用户未回复）：
  1. Title 用哪个版本？（main.tex "Calibrated Uncertainty Gating..." vs D184 "Adaptive Test-Time Refinement..."）
  2. 投稿目标：CoRL 已提交？还是转投其他会议？
  3. 服务器状态：用户是否已释放？
- Registry: 1423 实验全部 DONE/killed/cancelled，无 RUNNING/PREPARING

### 4. 📋 待办
- 飞书 API 恢复（月初配额刷新）或用户主动来消息 → 立即确认 title / 投稿目标 / 服务器状态
- 用户确认转投其他会议 → 评估是否需要补实验，恢复服务器，更新 ROADMAP DDL
- 用户确认 CoRL 已提交 → 项目进入等待审稿阶段，考虑 archive 或准备 rebuttal 材料
- 服务器恢复可达 → sync_code 推送本地论文修改到远程

### 5. 🎯 战略上下文
- 项目核心结论：CRM always-on 4/4 suites 有害（K-matched controlled），Adaptive gating 恢复性能。跨模型验证（SmolVLA 0.4B + π₀.₅ 3.6B）
- CoRL DDL 05-28 20:00 已过。用户在 DDL 后仍在改论文细节（limitation、keyword、abstract 字数），行为模式像在填投稿系统，但始终未明确回答是否已提交
- Reviewer 遗留 warning：4 个图表问题未修（fig_method_bar τ 标注歧义、配色不一致、Object τ=0.10 trigger rate "---"、fig1_pipeline trigger rate 范围）+ Spatial τ=0.25 SR 0.8pp 差异
- 易错点：不要假设"用户在改论文 = 还没提交"，也不要假设"DDL 过了 = 已提交"。必须等用户明确回答
