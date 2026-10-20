# director / loop_4.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`8726c6fac8f137221346.json`](../../sessions/87/8726c6fac8f137221346.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-14T18:27:02+00:00'
---

# Director Handoff — agent_progress_probe — 2026-05-14

## 刚做完什么

今天是密集决策日。一系列重大发现导致论文 framing 经历多次 pivot：

1. **non-nlp-baseline 实验（D031-D032）**：structural features（step count, action diversity 等）在跨 agent 场景下 F1=0.9951，碾压 probe。这暴露了 MV 标签可被非 NLP 特征近完美预测的问题。
2. **TWV ablation（D037-D038）**：temporal weighted voting 实验 negative——temporal alignment 在 circular eval 中梯度反转。TLM 从 core claim 降级为 "promising direction"。
3. **Framing pivot（D029-D036）**：论文从"提出 TLM 方法"pivot 到以 LF framework 分析 + ProgressProbe 实证为主。Claim 结构：C1 LF framework（时序分析+OB 贡献）、C2 Probe practical（encoder-agnostic, +24pp vs LLM）、C3 Cross-impl（LF 可迁移但 probe 需适配）。
4. **ablation-window-size 完成**：k=5 最优 0.9309，写入 ROADMAP。
5. **D033 全面优先级重排**：gold set 人工标注确认为唯一关键路径，暂停 circular eval 框架内的进一步 ablation。

## 当前状态

- **投稿目标**：EMNLP 2026 ARR 5/25 cycle，剩 11 天
- **实验**：41 个，27 成功，7 negative，7 待处理（PREPARING/QUEUED）
- **GPU**：bjb2-23165 RTX 5090 ×2，当前两张都空闲——**必须立即派活**
- **Agent 队列**：有积压（depth~5），包括 data-scaling fix、F1_stag 溯源、OH 实验等
- **审稿阶段**：Group C 已启动并行审稿

## 关键路径 & 阻塞项

1. **🔴 人工标注（最大阻塞）**：650 窗口标注材料就绪，但用户尚未确认标注人力。GO/NO-GO gate 在 5/16-17。没有人类标注就没有 gold set，没有 gold set 则 TLM 的 GO/NO-GO 无法执行。**必须持续追用户**。
2. **data-scaling FAILED**：FileNotFoundError 路径 bug，Agent 队列中等修复。
3. **F1_stag 数字闭环**：论文用 0.641（3-seed），但 per-class breakdown 和 0.000 来源未溯源。Agent 已排队。
4. **OH 补充实验**（Reviewer P0）：OH 100% fine-tuning + OH cmd_rep LF 消融，需 Agent 执行。

## 下一个"我"接手要做的

1. **检查 Agent 队列执行情况**：`get_agent_queue_status` 看 Agent 是否在消化积压。GPU 空闲就派活。
2. **催用户标注确认**：如果用户没回应，`director_reply_to_user` 再催一次。
3. **监控 data-scaling 修复进展**：Agent 修完路径 bug 后需要重跑，分配 GPU。
4. **OH 实验审批**：Agent 提交 OH fine-tuning / cmd_rep 消融时及时审批+分配 GPU。
5. **Plan B 准备**：如果 5/16-17 标注没完成或 κ<0.6，需要果断切 Plan B（Claim 1 降级 + TWV 替代 TLM + 强化 C3）。

## 教训 & 禁区

- **不要在 circular eval 框架下继续追 TLM**——TWV negative（D037-D038）已证明 temporal alignment 在这个框架下不 work。TLM 只在有 gold label 时才有意义。
- **non-nlp-baseline 0.9951 不是威胁而是 insight**——论文 framing 已 pivot 为"LF 信号分析"视角，structural features 的强表现支持 Claim 1（LF 有效性）。
- **不要建议降级到 Findings 或换会议**——保持 EMNLP main conference 目标，时间紧就加并行。


---
