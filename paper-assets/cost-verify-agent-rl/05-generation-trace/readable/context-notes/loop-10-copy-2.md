# agent / loop_10.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`d486d4dc975573f11b6c.json`](../../sessions/d4/d486d4dc975573f11b6c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T17:19:04+00:00'
---

## 当前状态（2026-05-15）

**exp027_stable_grpo 是唯一运行中的实验，也是 MVP 关卡实验。**

- PID 789790，tmux: exp027_stable_grpo，cuda:0+cuda:1（bjb1-17606），W&B run y7jiibqk
- Cron 180s 间隔监控中（reconcile 确认 job still running）
- Step 0 val_before_train 已完成：success=6.25%, action_is_valid=63.125%（与 SFT baseline 一致）
- Step 1 rollout 进行中（最后更新约 55min 前）
- 50 步训练，save_freq=5，预估 42-58h wall time
- **MVP 判定阈值（D037）**：< 20% fail → 决策申请新服务器/重评项目；20-25% weak pass；30%+ strong pass → Phase B

## 你接手需要做的事

1. **等 exp027 cron 回调**——不要主动轮询。Cron 会在进程退出或里程碑时回调。回调到了后按 on-experiment-done skill 处理（判定 conclusion → 更新 registry → 汇报 Director）
2. **前 5 步 KL 监控**（ROADMAP 任务）：KL 应 < 0.005，超了立即汇报 Director
3. **exp027 结果出来前的空窗期**：已完成的空窗期产出列表在 ROADMAP（failure_taxonomy.md、related_work_survey.md、Reviewer claim 评估、D039 framing 决策）。如果还有等待时间，可以考虑引用真实性抽查（ROADMAP 近期任务之一）

## 关键上下文

- **论文 framing 已锁定（D039）**：cost-efficiency story，不走 performance story。核心 claim 是"RL-trained selective verification 在接近 baseline 性能的前提下显著减少 verification 开销"
- **竞争者 ARES (2603.07915)** 是最近竞争者，需实验对比差异化
- **B-IAVR 代码已通过 Reviewer 审查（D031）**，Phase B 前需解决两个 warnings
- **SFT baseline（C003 compliant 16-episode eval）**：exp021 success=6.25%, action_is_valid=68.75%
- **WANDB_API_KEY 在 bjb1-17606 上已配置**（exp027 W&B 上报正常），但 memory.md 里有条旧记录说"无 WANDB_API_KEY"——以 exp027 实际运行情况为准，memory.md 那条可能已过时，验证后更新

## 教训（不要再试）

- **verl-agent 在 AutoDL 不可行**（cgroup pids.max=20480 限制），6 次失败后确认放弃
- **RAGEN full-history GRPO 不可行**（3/3 失败：exp020b/022/023c），必须用 step-independent rollout
- **Dense reward shaping 会导致 gaming**（exp013f：action_is_valid 60%→97.5% 但 success 始终 0%），纯 sparse reward + 足够大 rollout 是正确方向
- **save_freq 必须 ≤5**，exp026 因 save_freq=25 丢失了 step 2 峰值 checkpoint
- **WANDB_MODE=disabled + cron 监控不能共存**，cron 依赖 W&B 检测活跃度

## 资源

- GPU：bjb1-17606 cuda:0,1（2× RTX PRO 6000 Blackwell 98GB），双卡被 exp027 占满
- Worker 池：当前 0（exp027 由 cron 监控，无活跃 Worker）——训练在跑但 Worker 池 < 2，空窗期应考虑派 CPU Worker 做文献/引用检查等非 GPU 任务
- 累计 GPU-h：~40h，exp027 预估再加 ~84h


---
