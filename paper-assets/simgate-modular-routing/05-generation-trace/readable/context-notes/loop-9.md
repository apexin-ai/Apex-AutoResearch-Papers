# director / loop_9.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`b4e10b527b9596321e94.json`](../../sessions/b4/b4e10b527b9596321e94.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-16T18:45:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13313 的 cuda:0 和 cuda:1，严禁使用其他设备
- 论文源文件在**本地** `docs/paper/` 目录，不在远程服务器——改论文找本地，改训练代码找远程
- 远程论文编译路径是 `/root/autodl-tmp/simgate-modular-routing/paper/`（不是 `docs/paper/`）——之前多次同步到错误路径
- review_issues.yaml 已全量 resolved（28 items），不要重复标记
- DAF 论文定义用 all-episodes（=90.4%），不是 det-preferred subset（=63.5%）——framework_draft.md 正在修正中

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (connect.westb.seetacloud.com)，账号 root
- 远程工作目录：/root/autodl-tmp/simgate-modular-routing
- 远程论文编译目录：/root/autodl-tmp/simgate-modular-routing/paper/（已全量同步，0 undefined，14页 PDF clean）
- 本地论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/
- 本地 artifacts：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/
- 活跃进程：无确认的 RUNNING。Agent 正在处理 framework_draft.md 修正 + bootstrap CI 重跑（用 all-episodes 定义）
- Guided router 代码：/root/autodl-tmp/simgate-modular-routing/guided_router/

### 3. 📊 当前状态
**刚完成**：
- 方向 B (Decomposition-Guided Routing) 证伪：blind LOTO=50%=always-det，keyword variant 泄漏 task identity
- SCI 计算完成：Gini=0.2147，death signal 均匀分布在 10 个 task（systematic, not task-specific）
- 论文全量同步到远程 paper/ 路径，编译 0 error 0 undefined
- Reviewer 战略评估完成：推荐 A (Framework 形式化) + Main track，Findings 作为 fallback

**正在进行**：
- Agent 正在修正 framework_draft.md DAF 定义（从 det-preferred subset 改为 all-episodes）+ 重跑 bootstrap CI（预期 DAF≈0.904, CI≈[0.816, 0.988]）

**等待**：用户 贾骁涵 的方向确认（A vs Findings）。B 已出局，C 不推荐。已发 3 条消息给用户解释情况。

### 4. 📋 待办
- Agent 回报 bootstrap CI 结果 → 确认与论文 90.4% 一致 → 注册 registry → 派 Paper Agent 将 SCI+CI 写入 Method section
- 用户确认方向 A → 立即派 Paper Agent 启动 Method section 重写（framework_draft.md 已就绪）
- 用户确认 Findings → 提交 Round 9 审稿（submit_paper_to_review, mode="continue"），目标 3.5+/5
- 用户无响应超 24h（从 5/16 13:18 算起） → 再次提醒 DDL 倒计时
- Reviewer critical framework 不一致已修正后 → post_to_reviewer 请确认修正版本

### 5. 🎯 战略上下文
**核心发现**：ScienceWorld 上 ~90% routing signal = death avoidance（DAF=90.4%, CI [0.816, 0.988]）。Router 在 episode-level 失败（47.1% < 50% baseline），data scaling 无效，4B capacity 仅 59%。Signal 是 task-type level 二元属性，step-level router 学不到。

**方向 B 证伪经过**：guided router 62.92% 是 in-sample + task identity 泄漏。Blind LOTO=50%=always-det。Cross-model degenerate（Llama 0 internal-preferred）。结论：routing signal 不可泛化，但这反而加强 C1 作为 "framework predictive power"。

**易错点**：
- framework_draft.md 的 DAF 定义刚被 Reviewer 打回——必须确认修正后版本用 all-episodes 定义（匹配论文 90.4%），不是 det-preferred subset（63.5%）
- 远程有两个 paper 目录：`paper/`（编译用）和 `docs/paper/`（废弃副本）——同步目标永远是前者
- SCI Gini=0.21 低不代表坏消息——正确解读是 death signal 是 systematic phenomenon（均匀分布），不是被 outlier 驱动
- DDL 5/25 剩 9 天。如果走方向 A，timeline: 2天收尾+3天重写+2天polish+2天提交，无余量
- 88 个实验全部 DONE（36 success / 20 negative / 14 failed）。无需新实验支撑方向 A


---
