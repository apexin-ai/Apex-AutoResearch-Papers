# agent / loop_13.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`2afd959e2158a9776777.json`](../../sessions/2a/2afd959e2158a9776777.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-16T02:31:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0, cuda:1（bjb1-17606），不可用其他设备
- exp028c 是 MVP 判定实验（D037）：success <20% = fail，20-25% = weak pass，30%+ = strong pass。**不得在 MVP 判定前启动 Phase B 实验**
- SFT checkpoint 来源：exp021_ragen_sft_v4（6.25% success baseline），路径在 bjb1-17606 上
- submit_training_job 命令必须自带环境激活（服务器用 conda：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- exp028c step_2_train 数据曾被标记为"脏数据"（success=6.25% 与 step_0 val 完全一致，疑为混淆）——已清除，等待真实数据替换，**不可引用旧 step_2 数据做判断**

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，账户 root
- 工作目录：/root/cost-verify-agent-rl
- Python：/root/miniconda3/bin/python（conda base 环境）
- GPU：2× RTX PRO 6000 Blackwell 98GB（cuda:0, cuda:1）
- 活跃进程：exp028c PID 824675，W&B run 4yu6qz1m
- Cron：exp028c_selfguide_recipe 活跃（reconcile 确认 pid=824675 仍在跑）
- 模型路径：qwen3_exp021_ragen_sft_v4（SFT checkpoint，具体路径在服务器上）
- 数据：AlfworldSG env_configs，128 条

### 3. 📊 当前状态
**exp028c_selfguide_recipe RUNNING**（Self-Guide recipe 全面对齐，9 项参数改动 vs exp027）。

已确认指标：
- step_0_val: success=6.25%（与 SFT baseline 一致，正确）
- step_1_train: success=13.28%, pass_at_8=37.5%, action_is_valid=76.43%（三方交叉验证通过）
- step_2_train: PENDING（旧数据已清除，等真实完成）

**Worker 运行中**：`worker_check_exp028c_step5_review`（turn 11，正在 SSH 读日志 + 拉 W&B 指标，检查 step 5 进度）

**等待中**：
- Worker 回调：step5 review 结果
- Cron 回调：exp028c 训练完成（100 steps，当前已过 step 5+）
- 无待处理 Director 决策

### 4. 📋 待办（条件触发式）
- Worker `check_exp028c_step5_review` 返回 → 读取 step 2-5 真实指标，更新 registry metrics，判断趋势
- exp028c cron 回调（训练完成）→ 按 D037 三层阈值判定 MVP：≥30% strong pass → complete_mvp() + 汇报 Director 启动 Phase B；20-25% weak pass → 汇报 Director 决策；<20% fail → 产出 Framing 调整提案（red-section），汇报 Director 评估项目可行性
- exp028c success ≥20% → 并行启动：(1) Phase B 前置实现（&lt;VERIFY> token + selective verification reward 设计）(2) ARES 对比实验设计
- exp028c fail → 考虑方向：换更大模型 / 换框架 / 终止项目，提交 Director 决策

### 5. 🎯 战略上下文
**核心判断链**：
- D050: 全面对齐 Self-Guide recipe 是"最后一搏"——如果完全对齐参考实现仍 <20%，说明 1.7B 模型 + ALFWorld 组合有根本问题
- D044: 之前失败的三大根因（SFT 起点差 + binary reward 零梯度 + 参数未对齐），exp028c 仅解决第三点（参数对齐），前两点仍存在
- D039: 论文 framing 是 cost-efficiency story，不是 performance story。即使 success 只到 30%，只要能证明 selective verification 减少开销就有故事
- 项目历史：35 个实验中成功仅 3 个，失败/负向 23 个。exp028c 是 MVP 最终验证

**易错点**：
- step_1_train success=13.28% 是 TRAINING metrics（pass_at_8=37.5%），不是 eval metrics。MVP 判定用 eval success
- 不要把 training success 和 eval success 混淆——之前 exp027 train 也有 13.28% peak 但 eval 很低
- exp025c 标记"等待人工审批"但实际是历史遗留，不需要主动推进
- 累计 GPU 时间 ~120h，post-MVP 预算需 600-2000h，需要 Director 提前规划资源


---
