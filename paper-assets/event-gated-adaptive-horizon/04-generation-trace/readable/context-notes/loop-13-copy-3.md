# reviewer / loop_13.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`0a12f49b6971eab6d420.json`](../../sessions/0a/0a12f49b6971eab6d420.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-16T13:24:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 和 cuda:1（bjb1-45299 两张 RTX PRO 6000）
- 018 registry 的 NVE 是 0.72×（peak@75K），但 018_summary.json 脚本输出 1.0（疑似 self-comparison bug）——论文用 0.72，不要改
- Introduction 还有"representation-level phenomenon"与"gradient-level mechanism"的矛盾未修复（已报 Director WARNING），下次审 intro 时跟进
- causal_matrix table 中 008d NVE=2.09×与 Table 1 的 4.12× 不一致（已报 WARNING），等 Agent 修复

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299(root)，工作目录 /root/autodl-tmp/event-gated-adaptive-horizon
- Python：/root/miniconda3/bin/python（conda base）
- Logdir：/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_*
- 日志：~/runs/event-gated-adaptive-horizon/exp_*.log
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/
- 论文 tex：docs/paper/sections/{abstract,introduction,methodology,results,analysis,conclusion}.tex
- 活跃进程：**无**——两卡当前空闲（018 和 010a 已完成）

### 3. 📊 当前状态
刚完成 018 Full-SGS 结果审查——**CIVO 完全消除**（eval 915.7@105K, NVE≈1.0×），确认 Scenario A（gradient-level）。Version A 文本已插入 analysis.tex §5.3.5。

Registry RUNNING：无。QUEUED：019a (PickCube baseline), 019b (PickCube CIVO trigger), 010b 未注册。
**两卡空闲是紧急问题**——已报 Director 催 Agent 提交。

等待中：
- Agent 提交 019a/019b/010b/Pathway B 控制实验
- Agent 修复 intro "representation-level" 矛盾 + causal_matrix NVE 不一致

### 4. 📋 待办
- 019a 完成 → 审查 PickCube baseline 稳定性，确认可作 NVE 归一化参考
- 019b 完成 → 核心判断：NVE>1.5× = CIVO 跨环境成立（C1 大幅加强）；NVE<1.5× = environment-specific
- D6 Pathway B 控制实验完成 → 如果 vanilla DreamerV3 seed=2 也崩 → C6 需降级；如果稳定 → C6 confirmed
- 010b Cheetah CIVO trigger 完成 → 同 019b 逻辑，验证 Cheetah 环境 CIVO
- Agent 修 intro 后 → 重读 intro 确认"representation-level"已删除/改写
- Agent 修 causal_matrix NVE 后 → 确认 008d 改为 4.12× 或明确注明 range 定义

### 5. 🎯 战略上下文
- **核心结论链**：D057(016e 崩)→D058(reframe as diagnostic)→D061(reward grad=0)→D062(4-way classification)→D063(018 confirms gradient-level)→D064(Dream 审稿行动项)
- **018 是本论文最强结果**：016e removes 0%→CIVO; 018 removes 93%→no CIVO; 008f removes 100%→no CIVO. Causal chain closed.
- **D6 (Pathway B control) 是最大风险**：如果 vanilla DreamerV3 同 seed 也出 Pathway B 崩溃 → C6 ("trained dt_emb creates vulnerability through multiple mechanisms") 不成立。优先级高于 ManiSkill3。
- **易错点**：018_summary.json 的 NVE=1.0 是 script bug（可能 baseline logdir 指错），不要因此质疑论文中的 0.72×。Registry 里 nve_peak=0.72 是 Agent 手工计算的，更可信。
- **进程 hang 教训**（见 memory）：不要因为单次 nvidia-smi 快照 0% 就判断进程 hang，DreamerV3 在 env interaction 阶段 GPU 利用率可以为 0。需多次采样确认。


---
