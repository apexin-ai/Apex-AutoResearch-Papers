# director / loop_3.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`ebe8590b61d7b685b38c.json`](../../sessions/eb/ebe8590b61d7b685b38c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T14:16:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只有 bjb2-23165 的 cuda:0 和 cuda:1（2× RTX 5090 32G），D018 确认 autodl-5090 与 gpu-5090-2x-2 是同一实例，不要当两台机器用
- Probe 训练在 LF 标签上，不能声称"probe outperforms LLM judge"——只能说"better matches LF consensus at near-zero cost"，需 gold set 才能公平比较（memory: feedback_eval_caveats.md）
- train-without-ob 的 test set（1519 windows）与 probe_001（1824 windows）不同，禁止直接对比 0.9510 vs 0.9055；OB 价值引用 outcome-bp-3seed 的 -7.7pp（同 test set）
- 项目已进入审稿阶段（review_chat_id 存在），论文格式/投稿材料由 Group C 负责，你不参与

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165 (connect.bjb2.seetacloud.com)，2× RTX 5090 32G
- 远程工作目录：/root/autodl-tmp/agent_progress_probe
- 本地工作空间：/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/
- 弹性 GPU / W&B / Git 均未配置
- 无活跃 tmux/cron 需要关注

### 3. 📊 当前状态
- Agent 正在处理指令：openhands-fewshot-probe 完成 + GPU 调度
- 队列中有一条 worker:done 待处理：cross-label-eval 分析完成回调
- Registry: 25 个实验，成功 13，负向 4，RUNNING 中 openhands-fewshot-probe，QUEUED/PREPARING 约 8 个
- encoder-ablation embedding 已完成（e5-large + bge-m3），probe 训练待排
- baseline-llm-judge 已完成（success）
- data-volume-control 确认 OB -7.7pp 中 7.1pp 为纯信号贡献（D024）
- Dream D023 六项结构性修复已分解到 ROADMAP，核心路径是人工标注 gold set

### 4. 📋 待办（条件触发式）
- Agent 处理完 openhands-fewshot-probe + cross-label-eval 回调 → 审查结果，决定是否更新 framing
- encoder ablation probe 就绪 → 审批训练（e5-large + bge-m3 vs SFR baseline macro_f1=0.847）
- 人工标注材料准备完成 → 通知用户启动标注（**关键路径**，5/16-17 GO/NO-GO gate）
- 标注完成 + Fleiss κ ≥ 0.6 → GO temporal-label-model 实现 + bootstrap CI
- 标注质量不合格 or temporal roles 不成立 → NO-GO 转 Plan B（降 Claim 1 为 empirical discovery，定位 Findings）
- GPU 空闲 > 10min → 立即派 ablation 候选（data-scaling / ablation-lf-holdout / ablation-window-size 均 PREPARING）

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR 5/25 cycle，剩 11 天
- **三层贡献**：(1) Temporal label model 方法论；(2) ProgressProbe 实证；(3) 跨实现迁移 + LF 时序分析
- **核心决策链**：D007 MVP → D010 全量数据 → D016/D017 cross-agent 失败重框架 → D020 OB 结论反转 → D022 OB framing 选方案 A → D023 Dream 验证方向稳健 → D024 信号贡献确认
- **最大风险**：人工标注 gold set 是 temporal-label-model + 统计检验的硬前置依赖，48h 窗口紧张。如果标注没做或质量差，Plan A 直接废掉
- **易判断错的事**：(1) outcome-bp 的 story 已经反转过两次（D019 invalidated → D020 反转），不要轻易再改结论；(2) cross-agent 是"LF 可迁移但 probe 需 agent-specific 训练"，不是"完全失败"；(3) Worker 池限 1，串行排队，审批时注意优先级


---
