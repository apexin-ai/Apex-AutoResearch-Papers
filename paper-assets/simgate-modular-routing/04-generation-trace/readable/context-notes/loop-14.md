# director / loop_14.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`e7d8e78a81e620ce4452.json`](../../sessions/e7/e7d8e78a81e620ce4452.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-22T18:40:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 按用户指令保留 westd-18266 备用，**不要再请求 Manager 回收**（用户 05-22 明确说"不要再请求回收了，你留着备用"）
- D131/D132：DDL 前不开新 GPU 实验（Reviewer 两次独立评估确认无高 ROI 实验）
- 用户说"论文提交的事你不用管，我们会手动去做的"——不要代替用户操作 ARR 提交
- 论文 8 页限制 margin 为 0-1 行，任何正文增删都可能导致 Conclusion 溢出到 page 9

### 2. 🖥️ 基础设施快照
- 服务器：westd-18266 (connect.westd.seetacloud.com:18266, root)，4× RTX PRO 6000，0% 利用率
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- autodl-simgate (westb, 端口 13313)：SSH 未注册，连接失败，大概率已释放或端口过期
- 论文目录：projects/simgate-modular-routing/docs/paper/（本地 workspace）
- 活跃进程：无。0 RUNNING 实验，0 Worker，Agent/Reviewer 均空闲（Reviewer 刚批准 RESET_BOTH）
- Cron：无活跃 cron 任务

### 3. 📊 当前状态
刚完成：
- R28 fresh review 全部修复（12/15 PASS，3 wont_fix 因页数约束）+ Reviewer 验收 10/10 PASS
- W4 64.7% task-type classifier 写入 §3.6（D133）
- Conclusion future work 具体化（写作微调 B）
- 最终 proofread：修复 2 个数字一致性 bug（WCB p 值 + K≥20-50 统一）
- review_issues.yaml R28 状态全部更新
- 文献蒸馏 v2 完成（9 篇论文，literature_map.yaml 格式已修复为 `papers` dict 格式）
- 叙事完整性审计：Reviewer 确认 53 成功实验全部引用，29/30 阴性纳入叙事，无遗漏

Registry：121 实验全部 DONE（53 成功 / 30 阴性 / 17 失败 / 21 killed），2 个标记"分析中"但实际无活跃工作。

等待中：用户回复提交 checklist（匿名代码仓库 + supplementary data 决策）。Plan B：若 05-23 18:00 前无回复，默认不提交，论文 as-is 可提交。

### 4. 📋 待办
- 用户回复 checklist → 按用户决定处理（"都不做"则无动作，"我来处理"则无动作）
- 用户要求再次审稿 → submit_paper_to_review（recommended_review_mode="continue"）
- DDL 05-25 过后 → 蒸馏待办可进一步完善（当前 v2 已有 9 篇，可扩充）
- 收到 ARR reviewer comments（数周后）→ 读 rebuttal_prep.md（精简版 ~670 词 + 详细版 ~1200 词，6 个 Attack 已备好）

### 5. 🎯 战略上下文
- **核心结论**：Death avoidance 占 ~79% routing signal（penalty-independent label fraction），跨 3 个 7-9B 模型家族复现（spread 2.2pp），router step-level learning 收敛失败
- **论文定位**：Framework-centric diagnostic（D126/D127 pivot），目标 Findings ≥3.0
- **R28 评分**：Overall 3.0，R1/R2 独立均 3.5 Borderline Conference。Excitement 3/5。差距是结构性的（单环境 scope + diagnostic 非 prescriptive 贡献），非写作/实验可解决
- **关键决策链**：D126/D127 framework pivot → D129 GPU 释放 → D130 接受 Findings → D131/D132 实验冻结 → D133 W4 写入正文
- **易错点**：(1) 页数 margin 极紧（0-1 行），任何正文改动必须编译验证；(2) 不要主动建议降级会议或放弃投稿；(3) GPU 用户说保留备用，不要再催回收；(4) `add_to_literature_map` 工具不存在，蒸馏靠手动编辑 literature_map.yaml 的 `papers` dict 键


---
