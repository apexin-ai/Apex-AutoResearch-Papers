# reviewer / loop_9.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`8f8f6b8be127ab69e214.json`](../../sessions/8f/8f8f6b8be127ab69e214.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T14:21:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 bjb1-45299 只有 2 张 GPU 被项目使用（cuda:0, cuda:1），但 `execution.gpu_ids` 未在 constraints.yaml 中明确定义（文件未创建）——以 registry 中历史实验使用的 cuda:0/cuda:1 为准
- ManiSkill3/SAPIEN 在 CUDA_VISIBLE_DEVICES 限制下会 segfault——如果启动 ManiSkill3 实验，必须先验证 state-based 模式兼容性，否则违反 GPU 隔离
- exp_015b_frozen_dt_emb 和 exp_009d_baseline_walker_s0 正在 RUNNING，不要 kill 它们

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (root)，4× RTX PRO 6000 Blackwell 98GB
- 工作目录：`/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base，不是 venv）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 分析脚本：`/root/autodl-tmp/event-gated-adaptive-horizon/analysis/` 下有 imagination_reward_analysis{_v2}.py, signed_reward_error.py
- ManiSkill3 wrapper：`/root/autodl-tmp/event-gated-adaptive-horizon/envs/maniskill.py`（已通过集成测试）
- 代码审计产出：`artifacts/gradient_stopping_code_audit.md`（SGS 方案，待实验验证）
- 无 W&B 配置（项目不用 W&B）

### 3. 📊 当前状态
**刚完成的审查**（本轮）：
1. **Imagination Reward Analysis v1** → WARNING（样本量小、actor-in-the-loop 混淆）→ Worker 做了 v2
2. **Imagination Reward Analysis v2** → PASS。Random policy 对照确认纯 dynamics bias = 1.68x，trained actor 放大至 2.90x。CIVO 因果链彻底闭合。建议论文分层报告（dynamics bias → actor exploitation → collapse）
3. **Gradient Stopping Code Audit** → INFO。方案技术可行（hook-based gradient subtraction），只需切断 reward_loss → dt_emb 一条路径。待实验验证
4. **ManiSkill3 Integration** → INFO + WARNING（CUDA_VISIBLE_DEVICES 冲突）

**Registry RUNNING**：
- exp_009d_baseline_walker_s0：baseline seed 0（第三 seed）
- exp_015b_frozen_dt_emb：frozen dt_emb 消融（D041 关键实验——隔离 dt_emb 训练 vs 存在的因果效应）

**QUEUED**：exp_017, exp_010a_cheetah, exp_009f

### 4. 📋 待办
- exp_015b_frozen_dt_emb 完成 → 审查结论：如果 freeze 后不崩 → CIVO 根因确认为 dt_emb 训练（strongest evidence）；如果仍崩 → dt_emb 存在本身就有害，需修改 C2 narrative
- exp_009d_baseline_walker_s0 完成 → 核实 3-seed baseline 一致性，更新 v/e 校准参考
- SGS 实验提交后 → 核对代码是否正确实现 hook-based gradient subtraction（审计报告 Section 7.1 的梯度检查），核对 `dt_emb_reward_grad_norm` 接近 0
- dt=3 vs dt=4 非单调性 → 论文中不要声称严格排序（gap 仅 0.038，N=20 统计不可靠），只声称 dt=2 >> dt=1 和 dt=2 > dt=3,4（方向）
- 中间 checkpoint 时序分析（25K/35K/45K 上重复 imagination analysis）→ 优先级低，非 blocking，但如果 GPU 空闲可安排

### 5. 🎯 战略上下文
- **项目定位**：诊断分析论文，非方法论文。CoRL 2026 DDL 2026-05-29（14 天后）
- **核心因果链已闭合**：trained dt_emb → prior dynamics 在 imagination 中产生乐观 latent trajectory (dynamics bias 1.68x) → trained actor 放大 (total 2.90x) → value inflation → stochastic collapse (50%)。008f (no dt_emb) 完美对照
- **CIVO 术语**：不叫"delusional critic"（与 Lu et al. 2018 冲突），叫 Conditioning-Induced Value Overestimation (D037)
- **C6 已 partially falsified**：dt=1 imagination 不阻止崩溃（008e_v3_s2 崩了），但崩溃机制与经典 CIVO 不同（eval-driven vs value-driven）。Trained dt_emb 通过多条路径创造脆弱性
- **易错点**：(1) 009e 和 008d 是同一 seed=1 的延续运行，独立崩溃率是 1/2 不是 2/3；(2) 008c vs 008d 同时改变了 dt_emb 训练状态和 RSSM 训练数据，不是纯 dt_emb 对照——008f 才是（D023/D024）；(3) v/e ratio 在 25K 前不可靠（baseline v/e 仅 0.087，微小差异被放大）；(4) 远程代码和本地 artifacts 可能不同步——审查"未修改"类结论前必须双边核对
- **关键决策链**：D020(delusional critic 机制定位) → D021(008c vs 008d 闭合) → D023/D024(008f confound control) → D032(nve>1.5x threshold) → D037(CIVO 术语) → D038(C6 falsified) → D041(015b frozen dt_emb 消融)


---
