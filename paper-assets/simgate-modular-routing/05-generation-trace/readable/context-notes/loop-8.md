# director / loop_8.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`aa5a49cc9ce98964cc91.json`](../../sessions/aa/aa5a49cc9ce98964cc91.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-16T13:19:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13313 的 cuda:0 和 cuda:1，严禁使用其他设备
- 当前两块 GPU 均空闲，无活跃实验，无需担心冲突
- 论文源文件在**本地** `docs/paper/` 目录，不在远程服务器——改论文找本地，改训练代码找远程
- ARR/EMNLP 提交不强制行号，当前已用 `\nolinenumbers` 关闭行号（用户报告过行号重叠）
- review_issues.yaml 刚全量更新（28 items 全部 resolved），不要重复标记

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (connect.westb.seetacloud.com)，账号 root
- 远程工作目录：/root/autodl-tmp/simgate-modular-routing
- 本地论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/
- 本地 artifacts：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/
- 最新 PDF：artifacts/main_v122_r8fixed.pdf（14页，已上传给用户）
- Provenance version：123
- 活跃进程：无。87/87 实验全部 DONE。GPU0 和 GPU1 均空闲。无 tmux session。

### 3. 📊 当前状态
**刚完成**：Round 8 审稿全部 8 项修复（1 Must-Fix + 4 Should-Fix + 3 Minor），PDF 已编译上传给用户。关键新增内容：
- Llama cross-model 从 pilot (2 tasks/20 eps) 升级到完整验证 (7 tasks/70 eps, 7/7 方向一致)
- Capacity scaling episode-level eval: 4B=58.96% (p<0.005)，reframed 为 "capacity-dependent negative"
- "vanishes" → "not statistically detectable"，safety critic → conservative default policy

**Registry**：87 个实验全部 DONE（35 success / 20 negative / 14 failed / 其余 killed）。无 RUNNING/PREPARING。

**等待中**：用户 贾骁涵 的 A/B/C 方向决策（main track method innovation vs Findings track）。这是唯一 blocker。

### 4. 📋 待办
- 用户选 A/B/C 中任一 → 设计对应 method contribution 实验，分配 GPU0+GPU1 并行铺开
- 用户选 Findings track → 提交 Round 9 审稿（`submit_paper_to_review`, recommended_review_mode="continue"），目标修到 3.5+/5
- 用户无响应超过 24h → 主动 `director_reply_to_user` 再次提醒 DDL 5/25 倒计时
- 如果提交 Round 9，审稿报告回来后 → Read `review-report-action.skill.md`，走 Holistic Pass + Action Matrix 流程
- 如果用户说"提交" → 走 ARR 提交流程（确认 venue/track/DDL，准备 supplementary）

### 5. 🎯 战略上下文
**核心发现**：ScienceWorld 上 ~90% routing signal 来自 death avoidance（DAF=90.4%, 78.9% penalty-independent）。Router 在 episode-level 失败（47.1% < 50% baseline），data scaling 无效，4B capacity scaling 仅 59%（capacity-dependent negative）。

**论文定位冲突**：Round 8 评 borderline 3.25/5，推荐 Findings track。用户 贾骁涵 明确要求 main track + method 创新。我提了三个方向：
- A: Counterfactual Decomposition Framework 形式化（最安全，提升方法论贡献）
- B: Decomposition-Guided Routing（用分析 insight 设计 rule-based router）
- C: Death-Aware Architecture（最激进，修改 agent 架构）
**推荐 B**，但用户尚未选择。

**易错点**：
- 不要把 4B=59% 当成 "router works"——它仍然远不实用，论文 framing 是 "capacity-starved signal, validates analytical methodology"
- Llama 数据中 int-preferred=0（比 Qwen 更极端），但 det death rate 也不是 0%（Reviewer 核实是 24.3%）——Agent 之前报告过 "det death=0%" 是错的，以 Reviewer 数据为准
- 1.7B 和 0.6B/4B 使用不同训练配置，不能做公平三点比较——论文已加脚注
- bib 条目 toolkengpt/voyager/tot 不是 orphan（Agent 之前误判），已全部恢复
- DDL 5/25 剩 9 天，如果要加 method contribution，时间非常紧


---
