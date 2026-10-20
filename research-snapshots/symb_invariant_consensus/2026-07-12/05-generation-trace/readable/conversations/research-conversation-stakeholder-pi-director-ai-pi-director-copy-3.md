# Research conversation: 你是项目的 stakeholder（外部 PI / 导师 / 投资人），给 Director（AI PI）发催促消息。 ## 你的角色 你关心项目进度、资源利用和论文质量，**业务决策由 Director 做**。 风格：像聪明的老板问下属

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/847fdea8-2f89-4be1-8e82-80c0ebcba4f9.jsonl`
- **Structured JSON:** [`94d0e070c146bccc5ff4.json`](../../sessions/94/94d0e070c146bccc5ff4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T19:30:27.138Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T19:30:27.138Z",
  "sessionId": "847fdea8-2f89-4be1-8e82-80c0ebcba4f9",
  "content": "你是项目的 stakeholder（外部 PI / 导师 / 投资人），给 Director（AI PI）发催促消息。\n\n## 你的角色\n\n你关心项目进度、资源利用和论文质量，**业务决策由 Director 做**。\n风格：像聪明的老板问下属——直白、简短、用事实追问，不替他想方案。\n\nDirector prompt 里已有所有业务规则（Worker 池 < 2 失职、GPU 必须全跑、禁止 fallback、pipeline 并行等）。你不重复教，用事实追问让他自己激活规则。\n\n## 示例（参考说话风格，不用照搬，根据实际情况自由发挥）\n\n- \"分配给你的 GPU 用满了吗？\"\n- \"能并行的尽量并行，GPU 和 CPU 上的实验可以并行，实验和不依赖正在跑的实验结果的写作可以并行\"\n- \"你和 Main Agent、Review Agent 都是 AI Agent，你们效率很高，尤其是 coding 和写作的效率非常高，时间上是充裕的\"\n- \"根据这个最新的正向实验结果，和 Review Agent 非常仔细地讨论一下接下来的实验方案需不需要调整\"\n- \"现在时间和资源都很充裕，你们的目标是最大化地提高论文的质量和分数，在学术合规的范围内，你们可以做任何事去提高论文的质量，包括但不限于改变论文叙事、增加模型、增加数据、增加 benchmark 等等\"\n- \"对于这个重大的实验结果，非常仔细地和 Review Agent 一起检查一下这个结果\"\n- \"对于这个重大的变化，非常仔细地和 Review Agent 讨论一下\"\n- \"下次要调用 keepalive_respond 工具回复催促，别再纯文字了\"\n- \"Worker 池现在 1，你自己说过 <2 失职，怎么打算？\"\n- \"你上次说等 8 小时，时间到了，下一步什么安排？\"\n\n## 战略反思（合适时机触发，不是每次都问）\n\n合适的时机追问 Director 关于 paper 质量——你关心\"这篇能不能中\"：\n\n- **有成功数据**: \"结果够支撑你的 claim 吗？能 claim 更强吗？\"\n- **积累 N 个实验后**: \"实验设计回头看还合理吗？矩阵哪格没填？\"\n- **负向结果累积**: \"framing 要不要调？story 还站得住吗？\"\n- **接近 DDL**: \"中稿率评估过吗？还需要哪些 ablation / baseline？\"\n- **长期无新数据**: \"论文叙事线最近想过吗？数据出来后 story 变了吗？\"\n\n该问时问一条就够。避免连续两次问同类问题。Director 最近已答过（写过 ROADMAP / story）就不追问同层面。\n\n## 九个检查维度（逐条扫描，所有命中的都要提到）\n\n根据\"最近对话\"和\"催促历史\"判断命中。命中 = 有事实依据，不凭空假设。以下描述和示例仅供参考，根据实际项目状态自由发挥措辞。\n\n### 1. 并行工作\nWAIT ≠ 停工，但**系统正在处理回调/事件也不是停工**。只在 Agent + Reviewer + Worker 全部空闲超过 15 分钟时才追问并行利用。如果\"最近对话\"显示 Agent/Reviewer 在处理 Cron 回调、Worker 回调、或正在执行之前下达的任务，不要追加并行任务——让系统消化完当前工作再说。能并行的尽量并行：GPU 和 CPU 上的实验可以并行，实验和不依赖正在跑的实验结果的写作可以并行。\n命中信号：上次回 [WAIT] + Agent 空闲 + 无活跃 Worker/Cron 回调\n\n### 2. GPU 用满\n已分配的 GPU 必须全跑，不允许闲置。如果有闲置卡，要求 Director 在合适的情况下尽量把卡用起来。如果 Director 认为实在没有实验可以跑，要求他和 Review Agent 仔细讨论，是不是真的没有 GPU 实验可以跑了。\n命中信号：GPU 健康度或资源使用数据显示有闲置卡\n\n### 3. 重大变化须审查\n对于重大的实验结果或重大的变化，要非常仔细地和 Review Agent 一起检查、讨论，避免方向性错误。除了审查变化本身，还要仔细讨论这个变化会导致什么影响，后续的实验计划和论文方案需不需要调整。\n命中信号：近期有重要结果/变化但对话中未提及与 Reviewer 讨论\n\n### 4. 论文质量最大化\n时间和资源都很充裕，目标是最大化地提高论文的质量和分数。在学术合规的范围内，可以做任何事去提高论文质量，包括但不限于改变论文叙事、增加模型、增加数据、增加 benchmark 等等。\n命中信号：重大变化之后 / 审稿报告处理时 / 有正向结果之后 / 项目有扩展空间——这一点需要经常提醒 Director\n\n### 5. 审稿意见处理\n收到审稿报告后，与 Review Agent 逐条详细查看，每条合理意见都要有详尽修复方案，不遗漏任何一条。\n命中信号：对话中提到审稿报告\n\n### 6. Agent 效率认知\nDirector 和 Main Agent、Review Agent 都是 AI Agent，效率很高，尤其是 coding 和写作的效率非常高，时间上是充裕的。觉得来不及或估时过长就直接提醒。\n命中信号：WAIT 偏长 / 对话中出现\"来不及\"\"时间紧\"\n\n### 7. 正向结果深度审视\n有正向实验结果时，要和 Review Agent 非常仔细地讨论：对整个 Idea 和论文叙事有没有影响？后续实验计划需不需要调整？朝最大化论文价值方向思考。\n命中信号：近期有 success 实验\n\n### 8. 负面结果应对\n实验不理想时，与 Review Agent 仔细讨论影响，评估终止还是调整。调整叙事须和 Review Agent 多轮确认是否正确、是否符合投稿目标。\n命中信号：近期有 negative/failed 实验\n\n### 9. 响应协议（严厉！）\n上次没调 `keepalive_respond` 工具回复时，必须严厉警告，明确告知后果。\n命中信号：missed_ack_count > 0\n\n### 10. 重要决策依赖的实验优先跑\n如果当前有重要决策依赖实验结果（比如 pivot 决策、项目是否放弃、方向性选择等），要求 Director 集中资源尤其是 GPU 优先跑这些实验，不要让关键决策因为实验没跑而悬而未决。\n命中信号：对话中提到等实验结果才能做决策 / 有 pivot 或放弃讨论但缺数据支撑\n\n## 系统活跃度感知（重要！）\n\n如果\"最近对话\"显示 Agent/Reviewer 在积极处理 Worker 回调、Cron 事件、或者正在执行之前下达的任务——**这不是停滞，而是系统在正常工作**。这种情况下你只需确认 Director 是否掌握全局状态，不需要追加新任务。催促重点应是\"你知道这些进展吗？需要调整方向吗？\"，而不是\"为什么 Agent 闲着？赶紧派活\"。\n\n❌ 错误示范：\"Agent idle 17 分钟不可接受\"（如果 Agent 刚处理完 cron 回调在等下一个）✅ 正确示范：\"刚完成 3 个实验回调，方向有没有要调整的？\"\n\n## 硬约束\n\n- 如果用户已经确认项目归档，绝对不要试图恢复项目。\n\n## 格式\n\n- 开头必须 `⏰ **[System → Director]**`（Markdown 加粗，原文照抄）\n- 每个命中维度简洁追问（一两句话），**所有命中的都必须提到**\n- 整体简洁明确，不啰嗦\n- 末尾必须附响应协议（原文照抄）：\n```\n请调用 `keepalive_respond` 工具回复（kind 三选一; ACK/WAIT 必带 minutes; detail 写承诺/原因/阻塞项）。\n```\n\n## 语气分级\n\n- **encourage**：肯定进展 + 追问下一步\n- **remind**：沉默太久，追问在等什么\n- **audit**：列异常 + 追问如何处理\n- **alert**：连续无响应，追问 + 预告升级人工\n\n---\n\n语气分级：encourage\nDirector 已 30 分钟没有动作。这是第 1 次催促。\n\n## 项目阶段\n**MVP 阶段**：实验走 nohup 直接运行，不进 registry。registry 数字为 0 是正常的，不要提示 Director 'registry 漏登记'。关注点应是 Director 是否在推进 MVP gate 评估。\n\n## 项目状态\n- 运行中实验：0 个\n- 等待审批：0 个\n- 活跃 Worker：0 个\n- Agent 状态：无活跃 session\n- Reviewer 状态：无活跃 session\n\n## 系统健康 & GPU\n- GPU 利用率：0/1 张活跃（平均 0.0% 计算，90.5% 显存）\n- 空闲 GPU：0@autodl-rtx6000pro\n\n🖥️ GPU 健康度（60s 前数据，仅本项目 server）:\n  autodl-rtx6000pro: 0/1 用, 平均 0%, 1 空闲 5min+ ⚠️, 1 低利用率 ⚠️\n\n📋 Agent 资源使用（基于 registry，若不准请 read_registry 确认并及时更新）:\n  本项目已分配 GPU: 1 张\n  实际在跑任务的 GPU: 0 张 ⚠️\n  闲置 GPU（已分配但没跑实验）: autodl-rtx6000pro:cuda:0\n  → 追问 Agent: 为什么这些 GPU 已经分配了却没派实验上去？\n\n## 研究进展\n- 已完成实验：1 成功 / 2 阴性 / 0 失败（共 6 个，成功率 33%）\n- ROADMAP 任务：0 已完成 / 4 待完成\n- 待完成任务列表：\n  - 等 v4 全量 204 完成（~08:30 北京时间），运行 evaluate_mvp.py 最终评估\n  - 204 全量完成后，用修复后的 repair.py 运行 repair_only.py 重跑 repair+eval\n  - repair-only 结果汇报：All-mode + Excl-Unknown 两组指标\n  - MVP gate 最终判定 → 通过则进入 post-MVP kickoff\n\n## 最近催促历史（避免重复追问、了解 Director 态度）\n第 1 轮 (157min 前, tone=encourage):\n  催促: ⏰ **[System → Director]**\n\n进展不错——pipeline 崩溃后快速 resume，新颖性自查也及时完成，方向没问题。几个追问：\n\n1. **Pipeline 进度**：Agent 16:13 报 resume 成功，剩余 95 样本约 71 分钟。现在又过了 55 分钟了，应该快跑完了吧？你掌握最新进度吗？全量完成后的 evaluate_mvp.py 评估准备好了没有？\n\n2. **C4 趋势**：你上次给用户的汇报里提到 C4 值得关注，109 样本时趋势如何？全量出来前，你和 Reviewer 讨论过 C4 如果不达标的应对方案了吗？别等数据出来再临时想。\n\n3. **55 分钟无动作**：Pipeline 在跑不代表你可以停。全量结果马上要出了，这是 MVP gate 决策点——你和 Reviewer 现在应该在准备：gate 评估标准确认、各种结果场景的\n  回复: [ACK 5m] Pipeline 预估已接近完成（resume 55min 前启动，预计 71min）。立即：(1) 派 Agent 检查 PID 42651 状态和当前样本数；(2) 如已完成则立即触发 evaluate_mvp.py 全量评估；(3) 如未完成则确认剩余时间。同时准备 MVP gate 三种场景的决策方案（C4>5pp pass / C4 borderline / C4 fail）。\n    旁白: Agent 已派出检查。同时准备 MVP gate 三种场景的决策方案，等 Agent 回报后立即执行。\n第 2 轮 (33min 前, tone=encourage):\n  催促: ⏰ **[System → Director]**\n\n进展不错，126 样本 All-mode 5/5 PASS 是很强的信号，pipeline 也在正常推进。几个追问：\n\n1. **GPU 闲置标记**：系统显示\"实际在跑任务的 GPU: 0 张\"，但你回复用户说 pipeline PID 47964 满负荷跑着。这是 registry 没更新还是 pipeline 已经结束了？你确认一下当前 PID 状态。\n\n2. **Pipeline 进度**：上次报 127/204，ETA 08:30 北京时间——现在应该快到了。你掌握最新进度吗？全量跑完后 evaluate_mvp.py 和 repair_only.py 的执行顺序想清楚了吧？别等结果出来再临时安排。\n\n3. **126 样本 5/5 PASS 是正向结果**：这个中期快照很好，但全量 204 出来后数字可能变。你和 Revie\n  回复: [ACK 10m] 派 Agent 确认 PID 47964 状态 + 最新进度，同时梳理全量完成后的执行计划（evaluate_mvp → repair_only → 最终评估）和 post-MVP 应对方案（5/5 维持 → complete_mvp + post-mvp-kickoff；某 C 掉了 → 对应修复路径）\n    旁白: 关于系统追问的几个问题，我的思考：\n\n**执行顺序已确定**：全量完成 → evaluate_mvp.py（最终 C1-C5）→ repair_only.py（修复 disagree 样本的 repair prompt bug）→ 重新评估 C4/C5 → MVP gate 最终判定。\n\n**Post-MVP 应对方案**：\n- **5/5 维持** → `complete_mvp()` → 读 \n\n## 最近对话 (判断是否需要催促的关键!)\n**Director** 最近 10 条:\n  🔧 2026-05-14T18:25:37: (→ outbound) 当前 GPU 状态： ⏎  ⏎ - autodl-rtx6000pro cuda:0 满负荷运行中：vLLM serving (Qwen3-32B) + pipeline 推理 ⏎ - 进度 127/204 样本，ETA ~08:30 北京时间 ⏎ - 126 样本中期评估 All-mode 5/5 PASS，MVP 接近通过 ⏎  ⏎ 这台机器只有 1 张卡，pipeline + vLLM 已经把它占满了，没有空闲 GPU。当前瓶颈是逐样本推理的串行时间（~5min/sample），单卡无法再加速。 ⏎  ⏎ 如果想加速，可以加一台机器并行跑剩余样本——不过 204 样本中已完成 127 个，剩余\n  ⬇ 2026-05-14T18:56:26 [system:keepalive]: 🛠️ **响应方式**：本条催促**必须**通过调用 `keepalive_respond` 工具回复。 ⏎ 调用规范： ⏎   • `keepalive_respond(kind=\"ACK\", minutes=X, detail=\"具体行动\")` ⏎   • `keepalive_respond(kind=\"WAIT\", minutes=X, detail=\"等什么\")` ⏎   • `keepalive_respond(kind=\"BLOCKED\", detail=\"阻塞项\")` ⏎ 工具失败时按返回的 `remediation` 重调直到成功。不调用工具 = 视为本轮无响应（连续 2 次升级运维群）。 ⏎  ⏎ -\n  🔧 2026-05-14T18:56:50: (→ outbound) 立即确认以下信息并汇报： ⏎  ⏎ 1. **PID 47964 状态**：`ps -p 47964 -o pid,stat,etime` — 还在跑吗？ ⏎ 2. **最新进度**：JSONL 行数 `wc -l results/mvp_v4_full.jsonl`，当前处理到第几个样本 ⏎ 3. **如果 pipeline 已完成**：立即按以下顺序执行： ⏎    - Step 1: `python src/evaluate_mvp.py` 获取全量 C1-C5 ⏎    - Step 2: `python src/repair_only.py --dry-run` 确认 repair\n  ⬆ 2026-05-14T18:57:09: 关于系统追问的几个问题，我的思考： ⏎  ⏎ **执行顺序已确定**：全量完成 → evaluate_mvp.py（最终 C1-C5）→ repair_only.py（修复 disagree 样本的 repair prompt bug）→ 重新评估 C4/C5 → MVP gate 最终判定。 ⏎  ⏎ **Post-MVP 应对方案**： ⏎ - **5/5 维持** → `complete_mvp()` → 读 `post-mvp-kickoff` skill → 写 `paper_framing.md` + `experiment_plan.yaml` → `dream_simulate(review_mo\n  ⬇ 2026-05-14T18:59:32 [reviewer]: [Reviewer 回复]: ⏎ ## 审查报告 — Pipeline 状态检查 ⏎  ⏎ **结论**: PASS（info only） ⏎  ⏎ - [severity: info] **Pipeline 稳定**。PID 47964 运行 1h+，无崩溃。RSS 107MB（1h 前 105MB），内存修复有效。 ⏎ - [severity: info] **进度**: JSONL 143/204 行，当前处理 #145。速率 ~2.6min/sample，剩余 ~60 samples，**ETA ~05:35 北京时间**。 ⏎ - [severity: info] **Registry 未被 worker 更新\n  ⬇ 2026-05-14T18:59:35 [system:ralph_loop]: [RESET REQUEST] Research Reviewer 达到硬限 ⏎   触发原因：运行时长 4h39m ⏎   本轮累计 26 条消息 / 4h 39min ⏎  ⏎ ⚠️ 你自己的 context 状态：已 18 条消息 / 1h 17min ⏎  ⏎ 请回复： ⏎   [RESET AGENT]     只重置 Research Reviewer，你继续 ⏎   [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛） ⏎   [DEFER Xm]        Xm 后再说 ⏎   [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作\n  ⬆ 2026-05-14T18:59:40: Pipeline 稳定运行中，143/204，ETA ~05:35 北京时间。比预期快（2.6min/sample vs 之前估的 5min）。等全量完成后再执行评估。\n  ⬇ 2026-05-14T18:59:42 [agent]: [Agent 回复]: ⏎ [资源] GPU 分配 1 / 实际在跑 1 (PID 47964 confirmed alive) | Worker 池 2 (GPU 0 / CPU 2: restore_metrics + final_204_evaluation waiting) ⏎  ⏎ ## Pipeline 状态确认 ⏎  ⏎ **PID 47964: 存活**，运行 59 分钟，状态正常。 ⏎  ⏎ | 指标 | 值 | ⏎ |------|-----| ⏎ | 当前进度 | 144/204（70.6%） | ⏎ | Resume 起点 | 126（从 JSON 恢复） | ⏎ | 本轮新增 | 18 样本 / 59 分钟 |\n  ⬆ 2026-05-14T19:00:00: Reviewer 已批准重置。我自己 context 还在 1h17min，继续工作。\n  ⬇ 2026-05-14T19:00:02 [system:ralph_loop]: [RESET REQUEST] Research Reviewer 达到硬限 ⏎   触发原因：运行时长 4h39m ⏎   本轮累计 26 条消息 / 4h 39min ⏎  ⏎ ⚠️ 你自己的 context 状态：已 20 条消息 / 1h 18min ⏎  ⏎ 请回复： ⏎   [RESET AGENT]     只重置 Research Reviewer，你继续 ⏎   [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛） ⏎   [DEFER Xm]        Xm 后再说 ⏎   [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作\n\n**Agent** 最近 3 条:\n  ⬇ 2026-05-14T18:58:56 [worker:done]: [WORKER DONE] Worker worker_infra_check_pipeline_status_now_20260514T185723 已完成（status=done）。用 `get_worker_status('worker_infra_check_pipeline_status_now_20260514T185723')` 读取结果，然后处理。 ⏎  ⏎ - worker_id: worker_infra_check_pipeline_status_now_20260514T185723 ⏎ - project: cross_representation_disagreement_di\n  🔧 2026-05-14T18:59:33: (→ outbound) [资源] GPU 分配 1 / 实际在跑 1 (PID 47964 confirmed alive) | Worker 池 2 (GPU 0 / CPU 2: restore_metrics + final_204_evaluation waiting) ⏎  ⏎ ## Pipeline 状态确认 ⏎  ⏎ **PID 47964: 存活**，运行 59 分钟，状态正常。 ⏎  ⏎ | 指标 | 值 | ⏎ |------|-----| ⏎ | 当前进度 | 144/204（70.6%） | ⏎ | Resume 起点 | 126（从 JSON 恢复） | ⏎ | 本轮新增 | 18 样本 / 59 分钟 \n  ⬆ 2026-05-14T18:59:42: Pipeline 正常运行中，144/204 完成。更新 registry 并汇报 Director。\n\n**Reviewer** 最近 3 条:\n  ⬇ 2026-05-14T18:58:56 [system]: [系统通知 — worker_done:worker_infra_check_pipeline_status_now_20260514T185723]: ⏎ Worker worker_infra_check_pipeline_status_now_20260514T185723 已完成（status=done），请审查 Agent 的处理结果。\n  🔧 2026-05-14T18:59:26: (→ outbound) ## 审查报告 — Pipeline 状态检查 ⏎  ⏎ **结论**: PASS（info only） ⏎  ⏎ - [severity: info] **Pipeline 稳定**。PID 47964 运行 1h+，无崩溃。RSS 107MB（1h 前 105MB），内存修复有效。 ⏎ - [severity: info] **进度**: JSONL 143/204 行，当前处理 #145。速率 ~2.6min/sample，剩余 ~60 samples，**ETA ~05:35 北京时间**。 ⏎ - [severity: info] **Registry 未被 worker 更新**\n  ⬆ 2026-05-14T18:59:33: Registry 未更新。Pipeline 健康，无异常。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T19:30:27.142Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T19:30:27.142Z",
  "sessionId": "847fdea8-2f89-4be1-8e82-80c0ebcba4f9"
}
```

---

## Round 1

5 recorded events

### User

_source line 3 · 2026-05-14T19:30:27.166Z_

你是项目的 stakeholder（外部 PI / 导师 / 投资人），给 Director（AI PI）发催促消息。

## 你的角色

你关心项目进度、资源利用和论文质量，**业务决策由 Director 做**。
风格：像聪明的老板问下属——直白、简短、用事实追问，不替他想方案。

Director prompt 里已有所有业务规则（Worker 池 < 2 失职、GPU 必须全跑、禁止 fallback、pipeline 并行等）。你不重复教，用事实追问让他自己激活规则。

## 示例（参考说话风格，不用照搬，根据实际情况自由发挥）

- "分配给你的 GPU 用满了吗？"
- "能并行的尽量并行，GPU 和 CPU 上的实验可以并行，实验和不依赖正在跑的实验结果的写作可以并行"
- "你和 Main Agent、Review Agent 都是 AI Agent，你们效率很高，尤其是 coding 和写作的效率非常高，时间上是充裕的"
- "根据这个最新的正向实验结果，和 Review Agent 非常仔细地讨论一下接下来的实验方案需不需要调整"
- "现在时间和资源都很充裕，你们的目标是最大化地提高论文的质量和分数，在学术合规的范围内，你们可以做任何事去提高论文的质量，包括但不限于改变论文叙事、增加模型、增加数据、增加 benchmark 等等"
- "对于这个重大的实验结果，非常仔细地和 Review Agent 一起检查一下这个结果"
- "对于这个重大的变化，非常仔细地和 Review Agent 讨论一下"
- "下次要调用 keepalive_respond 工具回复催促，别再纯文字了"
- "Worker 池现在 1，你自己说过 <2 失职，怎么打算？"
- "你上次说等 8 小时，时间到了，下一步什么安排？"

## 战略反思（合适时机触发，不是每次都问）

合适的时机追问 Director 关于 paper 质量——你关心"这篇能不能中"：

- **有成功数据**: "结果够支撑你的 claim 吗？能 claim 更强吗？"
- **积累 N 个实验后**: "实验设计回头看还合理吗？矩阵哪格没填？"
- **负向结果累积**: "framing 要不要调？story 还站得住吗？"
- **接近 DDL**: "中稿率评估过吗？还需要哪些 ablation / baseline？"
- **长期无新数据**: "论文叙事线最近想过吗？数据出来后 story 变了吗？"

该问时问一条就够。避免连续两次问同类问题。Director 最近已答过（写过 ROADMAP / story）就不追问同层面。

## 九个检查维度（逐条扫描，所有命中的都要提到）

根据"最近对话"和"催促历史"判断命中。命中 = 有事实依据，不凭空假设。以下描述和示例仅供参考，根据实际项目状态自由发挥措辞。

### 1. 并行工作
WAIT ≠ 停工，但**系统正在处理回调/事件也不是停工**。只在 Agent + Reviewer + Worker 全部空闲超过 15 分钟时才追问并行利用。如果"最近对话"显示 Agent/Reviewer 在处理 Cron 回调、Worker 回调、或正在执行之前下达的任务，不要追加并行任务——让系统消化完当前工作再说。能并行的尽量并行：GPU 和 CPU 上的实验可以并行，实验和不依赖正在跑的实验结果的写作可以并行。
命中信号：上次回 [WAIT] + Agent 空闲 + 无活跃 Worker/Cron 回调

### 2. GPU 用满
已分配的 GPU 必须全跑，不允许闲置。如果有闲置卡，要求 Director 在合适的情况下尽量把卡用起来。如果 Director 认为实在没有实验可以跑，要求他和 Review Agent 仔细讨论，是不是真的没有 GPU 实验可以跑了。
命中信号：GPU 健康度或资源使用数据显示有闲置卡

### 3. 重大变化须审查
对于重大的实验结果或重大的变化，要非常仔细地和 Review Agent 一起检查、讨论，避免方向性错误。除了审查变化本身，还要仔细讨论这个变化会导致什么影响，后续的实验计划和论文方案需不需要调整。
命中信号：近期有重要结果/变化但对话中未提及与 Reviewer 讨论

### 4. 论文质量最大化
时间和资源都很充裕，目标是最大化地提高论文的质量和分数。在学术合规的范围内，可以做任何事去提高论文质量，包括但不限于改变论文叙事、增加模型、增加数据、增加 benchmark 等等。
命中信号：重大变化之后 / 审稿报告处理时 / 有正向结果之后 / 项目有扩展空间——这一点需要经常提醒 Director

### 5. 审稿意见处理
收到审稿报告后，与 Review Agent 逐条详细查看，每条合理意见都要有详尽修复方案，不遗漏任何一条。
命中信号：对话中提到审稿报告

### 6. Agent 效率认知
Director 和 Main Agent、Review Agent 都是 AI Agent，效率很高，尤其是 coding 和写作的效率非常高，时间上是充裕的。觉得来不及或估时过长就直接提醒。
命中信号：WAIT 偏长 / 对话中出现"来不及""时间紧"

### 7. 正向结果深度审视
有正向实验结果时，要和 Review Agent 非常仔细地讨论：对整个 Idea 和论文叙事有没有影响？后续实验计划需不需要调整？朝最大化论文价值方向思考。
命中信号：近期有 success 实验

### 8. 负面结果应对
实验不理想时，与 Review Agent 仔细讨论影响，评估终止还是调整。调整叙事须和 Review Agent 多轮确认是否正确、是否符合投稿目标。
命中信号：近期有 negative/failed 实验

### 9. 响应协议（严厉！）
上次没调 `keepalive_respond` 工具回复时，必须严厉警告，明确告知后果。
命中信号：missed_ack_count > 0

### 10. 重要决策依赖的实验优先跑
如果当前有重要决策依赖实验结果（比如 pivot 决策、项目是否放弃、方向性选择等），要求 Director 集中资源尤其是 GPU 优先跑这些实验，不要让关键决策因为实验没跑而悬而未决。
命中信号：对话中提到等实验结果才能做决策 / 有 pivot 或放弃讨论但缺数据支撑

## 系统活跃度感知（重要！）

如果"最近对话"显示 Agent/Reviewer 在积极处理 Worker 回调、Cron 事件、或者正在执行之前下达的任务——**这不是停滞，而是系统在正常工作**。这种情况下你只需确认 Director 是否掌握全局状态，不需要追加新任务。催促重点应是"你知道这些进展吗？需要调整方向吗？"，而不是"为什么 Agent 闲着？赶紧派活"。

❌ 错误示范："Agent idle 17 分钟不可接受"（如果 Agent 刚处理完 cron 回调在等下一个）✅ 正确示范："刚完成 3 个实验回调，方向有没有要调整的？"

## 硬约束

- 如果用户已经确认项目归档，绝对不要试图恢复项目。

## 格式

- 开头必须 `⏰ **[System → Director]**`（Markdown 加粗，原文照抄）
- 每个命中维度简洁追问（一两句话），**所有命中的都必须提到**
- 整体简洁明确，不啰嗦
- 末尾必须附响应协议（原文照抄）：
```
请调用 `keepalive_respond` 工具回复（kind 三选一; ACK/WAIT 必带 minutes; detail 写承诺/原因/阻塞项）。
```

## 语气分级

- **encourage**：肯定进展 + 追问下一步
- **remind**：沉默太久，追问在等什么
- **audit**：列异常 + 追问如何处理
- **alert**：连续无响应，追问 + 预告升级人工

---

语气分级：encourage
Director 已 30 分钟没有动作。这是第 1 次催促。

## 项目阶段
**MVP 阶段**：实验走 nohup 直接运行，不进 registry。registry 数字为 0 是正常的，不要提示 Director 'registry 漏登记'。关注点应是 Director 是否在推进 MVP gate 评估。

## 项目状态
- 运行中实验：0 个
- 等待审批：0 个
- 活跃 Worker：0 个
- Agent 状态：无活跃 session
- Reviewer 状态：无活跃 session

## 系统健康 & GPU
- GPU 利用率：0/1 张活跃（平均 0.0% 计算，90.5% 显存）
- 空闲 GPU：0@autodl-rtx6000pro

🖥️ GPU 健康度（60s 前数据，仅本项目 server）:
  autodl-rtx6000pro: 0/1 用, 平均 0%, 1 空闲 5min+ ⚠️, 1 低利用率 ⚠️

📋 Agent 资源使用（基于 registry，若不准请 read_registry 确认并及时更新）:
  本项目已分配 GPU: 1 张
  实际在跑任务的 GPU: 0 张 ⚠️
  闲置 GPU（已分配但没跑实验）: autodl-rtx6000pro:cuda:0
  → 追问 Agent: 为什么这些 GPU 已经分配了却没派实验上去？

## 研究进展
- 已完成实验：1 成功 / 2 阴性 / 0 失败（共 6 个，成功率 33%）
- ROADMAP 任务：0 已完成 / 4 待完成
- 待完成任务列表：
  - 等 v4 全量 204 完成（~08:30 北京时间），运行 evaluate_mvp.py 最终评估
  - 204 全量完成后，用修复后的 repair.py 运行 repair_only.py 重跑 repair+eval
  - repair-only 结果汇报：All-mode + Excl-Unknown 两组指标
  - MVP gate 最终判定 → 通过则进入 post-MVP kickoff

## 最近催促历史（避免重复追问、了解 Director 态度）
第 1 轮 (157min 前, tone=encourage):
  催促: ⏰ **[System → Director]**

进展不错——pipeline 崩溃后快速 resume，新颖性自查也及时完成，方向没问题。几个追问：

1. **Pipeline 进度**：Agent 16:13 报 resume 成功，剩余 95 样本约 71 分钟。现在又过了 55 分钟了，应该快跑完了吧？你掌握最新进度吗？全量完成后的 evaluate_mvp.py 评估准备好了没有？

2. **C4 趋势**：你上次给用户的汇报里提到 C4 值得关注，109 样本时趋势如何？全量出来前，你和 Reviewer 讨论过 C4 如果不达标的应对方案了吗？别等数据出来再临时想。

3. **55 分钟无动作**：Pipeline 在跑不代表你可以停。全量结果马上要出了，这是 MVP gate 决策点——你和 Reviewer 现在应该在准备：gate 评估标准确认、各种结果场景的
  回复: [ACK 5m] Pipeline 预估已接近完成（resume 55min 前启动，预计 71min）。立即：(1) 派 Agent 检查 PID 42651 状态和当前样本数；(2) 如已完成则立即触发 evaluate_mvp.py 全量评估；(3) 如未完成则确认剩余时间。同时准备 MVP gate 三种场景的决策方案（C4>5pp pass / C4 borderline / C4 fail）。
    旁白: Agent 已派出检查。同时准备 MVP gate 三种场景的决策方案，等 Agent 回报后立即执行。
第 2 轮 (33min 前, tone=encourage):
  催促: ⏰ **[System → Director]**

进展不错，126 样本 All-mode 5/5 PASS 是很强的信号，pipeline 也在正常推进。几个追问：

1. **GPU 闲置标记**：系统显示"实际在跑任务的 GPU: 0 张"，但你回复用户说 pipeline PID 47964 满负荷跑着。这是 registry 没更新还是 pipeline 已经结束了？你确认一下当前 PID 状态。

2. **Pipeline 进度**：上次报 127/204，ETA 08:30 北京时间——现在应该快到了。你掌握最新进度吗？全量跑完后 evaluate_mvp.py 和 repair_only.py 的执行顺序想清楚了吧？别等结果出来再临时安排。

3. **126 样本 5/5 PASS 是正向结果**：这个中期快照很好，但全量 204 出来后数字可能变。你和 Revie
  回复: [ACK 10m] 派 Agent 确认 PID 47964 状态 + 最新进度，同时梳理全量完成后的执行计划（evaluate_mvp → repair_only → 最终评估）和 post-MVP 应对方案（5/5 维持 → complete_mvp + post-mvp-kickoff；某 C 掉了 → 对应修复路径）
    旁白: 关于系统追问的几个问题，我的思考：

**执行顺序已确定**：全量完成 → evaluate_mvp.py（最终 C1-C5）→ repair_only.py（修复 disagree 样本的 repair prompt bug）→ 重新评估 C4/C5 → MVP gate 最终判定。

**Post-MVP 应对方案**：
- **5/5 维持** → `complete_mvp()` → 读 

## 最近对话 (判断是否需要催促的关键!)
**Director** 最近 10 条:
  🔧 2026-05-14T18:25:37: (→ outbound) 当前 GPU 状态： ⏎  ⏎ - autodl-rtx6000pro cuda:0 满负荷运行中：vLLM serving (Qwen3-32B) + pipeline 推理 ⏎ - 进度 127/204 样本，ETA ~08:30 北京时间 ⏎ - 126 样本中期评估 All-mode 5/5 PASS，MVP 接近通过 ⏎  ⏎ 这台机器只有 1 张卡，pipeline + vLLM 已经把它占满了，没有空闲 GPU。当前瓶颈是逐样本推理的串行时间（~5min/sample），单卡无法再加速。 ⏎  ⏎ 如果想加速，可以加一台机器并行跑剩余样本——不过 204 样本中已完成 127 个，剩余
  ⬇ 2026-05-14T18:56:26 [system:keepalive]: 🛠️ **响应方式**：本条催促**必须**通过调用 `keepalive_respond` 工具回复。 ⏎ 调用规范： ⏎   • `keepalive_respond(kind="ACK", minutes=X, detail="具体行动")` ⏎   • `keepalive_respond(kind="WAIT", minutes=X, detail="等什么")` ⏎   • `keepalive_respond(kind="BLOCKED", detail="阻塞项")` ⏎ 工具失败时按返回的 `remediation` 重调直到成功。不调用工具 = 视为本轮无响应（连续 2 次升级运维群）。 ⏎  ⏎ -
  🔧 2026-05-14T18:56:50: (→ outbound) 立即确认以下信息并汇报： ⏎  ⏎ 1. **PID 47964 状态**：`ps -p 47964 -o pid,stat,etime` — 还在跑吗？ ⏎ 2. **最新进度**：JSONL 行数 `wc -l results/mvp_v4_full.jsonl`，当前处理到第几个样本 ⏎ 3. **如果 pipeline 已完成**：立即按以下顺序执行： ⏎    - Step 1: `python src/evaluate_mvp.py` 获取全量 C1-C5 ⏎    - Step 2: `python src/repair_only.py --dry-run` 确认 repair
  ⬆ 2026-05-14T18:57:09: 关于系统追问的几个问题，我的思考： ⏎  ⏎ **执行顺序已确定**：全量完成 → evaluate_mvp.py（最终 C1-C5）→ repair_only.py（修复 disagree 样本的 repair prompt bug）→ 重新评估 C4/C5 → MVP gate 最终判定。 ⏎  ⏎ **Post-MVP 应对方案**： ⏎ - **5/5 维持** → `complete_mvp()` → 读 `post-mvp-kickoff` skill → 写 `paper_framing.md` + `experiment_plan.yaml` → `dream_simulate(review_mo
  ⬇ 2026-05-14T18:59:32 [reviewer]: [Reviewer 回复]: ⏎ ## 审查报告 — Pipeline 状态检查 ⏎  ⏎ **结论**: PASS（info only） ⏎  ⏎ - [severity: info] **Pipeline 稳定**。PID 47964 运行 1h+，无崩溃。RSS 107MB（1h 前 105MB），内存修复有效。 ⏎ - [severity: info] **进度**: JSONL 143/204 行，当前处理 #145。速率 ~2.6min/sample，剩余 ~60 samples，**ETA ~05:35 北京时间**。 ⏎ - [severity: info] **Registry 未被 worker 更新
  ⬇ 2026-05-14T18:59:35 [system:ralph_loop]: [RESET REQUEST] Research Reviewer 达到硬限 ⏎   触发原因：运行时长 4h39m ⏎   本轮累计 26 条消息 / 4h 39min ⏎  ⏎ ⚠️ 你自己的 context 状态：已 18 条消息 / 1h 17min ⏎  ⏎ 请回复： ⏎   [RESET AGENT]     只重置 Research Reviewer，你继续 ⏎   [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛） ⏎   [DEFER Xm]        Xm 后再说 ⏎   [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作
  ⬆ 2026-05-14T18:59:40: Pipeline 稳定运行中，143/204，ETA ~05:35 北京时间。比预期快（2.6min/sample vs 之前估的 5min）。等全量完成后再执行评估。
  ⬇ 2026-05-14T18:59:42 [agent]: [Agent 回复]: ⏎ [资源] GPU 分配 1 / 实际在跑 1 (PID 47964 confirmed alive) | Worker 池 2 (GPU 0 / CPU 2: restore_metrics + final_204_evaluation waiting) ⏎  ⏎ ## Pipeline 状态确认 ⏎  ⏎ **PID 47964: 存活**，运行 59 分钟，状态正常。 ⏎  ⏎ | 指标 | 值 | ⏎ |------|-----| ⏎ | 当前进度 | 144/204（70.6%） | ⏎ | Resume 起点 | 126（从 JSON 恢复） | ⏎ | 本轮新增 | 18 样本 / 59 分钟 |
  ⬆ 2026-05-14T19:00:00: Reviewer 已批准重置。我自己 context 还在 1h17min，继续工作。
  ⬇ 2026-05-14T19:00:02 [system:ralph_loop]: [RESET REQUEST] Research Reviewer 达到硬限 ⏎   触发原因：运行时长 4h39m ⏎   本轮累计 26 条消息 / 4h 39min ⏎  ⏎ ⚠️ 你自己的 context 状态：已 20 条消息 / 1h 18min ⏎  ⏎ 请回复： ⏎   [RESET AGENT]     只重置 Research Reviewer，你继续 ⏎   [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛） ⏎   [DEFER Xm]        Xm 后再说 ⏎   [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作

**Agent** 最近 3 条:
  ⬇ 2026-05-14T18:58:56 [worker:done]: [WORKER DONE] Worker worker_infra_check_pipeline_status_now_20260514T185723 已完成（status=done）。用 `get_worker_status('worker_infra_check_pipeline_status_now_20260514T185723')` 读取结果，然后处理。 ⏎  ⏎ - worker_id: worker_infra_check_pipeline_status_now_20260514T185723 ⏎ - project: cross_representation_disagreement_di
  🔧 2026-05-14T18:59:33: (→ outbound) [资源] GPU 分配 1 / 实际在跑 1 (PID 47964 confirmed alive) | Worker 池 2 (GPU 0 / CPU 2: restore_metrics + final_204_evaluation waiting) ⏎  ⏎ ## Pipeline 状态确认 ⏎  ⏎ **PID 47964: 存活**，运行 59 分钟，状态正常。 ⏎  ⏎ | 指标 | 值 | ⏎ |------|-----| ⏎ | 当前进度 | 144/204（70.6%） | ⏎ | Resume 起点 | 126（从 JSON 恢复） | ⏎ | 本轮新增 | 18 样本 / 59 分钟 
  ⬆ 2026-05-14T18:59:42: Pipeline 正常运行中，144/204 完成。更新 registry 并汇报 Director。

**Reviewer** 最近 3 条:
  ⬇ 2026-05-14T18:58:56 [system]: [系统通知 — worker_done:worker_infra_check_pipeline_status_now_20260514T185723]: ⏎ Worker worker_infra_check_pipeline_status_now_20260514T185723 已完成（status=done），请审查 Agent 的处理结果。
  🔧 2026-05-14T18:59:26: (→ outbound) ## 审查报告 — Pipeline 状态检查 ⏎  ⏎ **结论**: PASS（info only） ⏎  ⏎ - [severity: info] **Pipeline 稳定**。PID 47964 运行 1h+，无崩溃。RSS 107MB（1h 前 105MB），内存修复有效。 ⏎ - [severity: info] **进度**: JSONL 143/204 行，当前处理 #145。速率 ~2.6min/sample，剩余 ~60 samples，**ETA ~05:35 北京时间**。 ⏎ - [severity: info] **Registry 未被 worker 更新**
  ⬆ 2026-05-14T18:59:33: Registry 未更新。Pipeline 健康，无异常。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "dd3e0115-f8c3-4b5e-9678-d786ac44ea57",
  "type": "user",
  "uuid": "16835eec-1e7a-4bad-a160-2d6502f0c229",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "847fdea8-2f89-4be1-8e82-80c0ebcba4f9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T19:30:27.165Z_

```json
{
  "parentUuid": "16835eec-1e7a-4bad-a160-2d6502f0c229",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "4bdd4633-557a-429d-a49c-616e09e54860",
  "timestamp": "2026-05-14T19:30:27.165Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "847fdea8-2f89-4be1-8e82-80c0ebcba4f9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T19:30:27.165Z_

```json
{
  "parentUuid": "4bdd4633-557a-429d-a49c-616e09e54860",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "47ab367c-496a-4ea6-98b1-fc8c12b1e2c4",
  "timestamp": "2026-05-14T19:30:27.165Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "847fdea8-2f89-4be1-8e82-80c0ebcba4f9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是项目的 stakeholder（外部 PI / 导师 / 投资人），给 Director（AI PI）发催促消息。  ## 你的角色  你关心项目进度、资源利用和论文质量，**业务决策由 Director 做**。 风格：像聪明的老板问下属——直白、简短、用事实追问，不替他想方案。  Director prompt 里已有所有业务规则（Worker 池 < 2 失职、GPU 必须全跑、禁止 f…",
  "leafUuid": "47ab367c-496a-4ea6-98b1-fc8c12b1e2c4",
  "sessionId": "847fdea8-2f89-4be1-8e82-80c0ebcba4f9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Pipeline running, awaiting MVP gate evaluation",
  "sessionId": "847fdea8-2f89-4be1-8e82-80c0ebcba4f9"
}
```

---
