# director / loop_13.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`d85c653e0664e15eedea.json`](../../sessions/d8/d85c653e0664e15eedea.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-25T22:56:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1 只能用 cuda:0 / cuda:1（项目配置 gpu_ids）
- westd 只能用 cuda:0 / cuda:1（项目配置 gpu_ids）
- 两台服务器各 2 卡，总共 4 张卡，不可越界使用其他项目的卡
- exp_089/090 已 FAILED（参数名错误 `--dt_embed_dim` → `--gate_dt_embed_dim`），不要重复犯
- 本项目处于审稿阶段，Review Director 在 Group C 独立审稿，Research Director 不参与论文格式/投稿材料准备

### 2. 🖥️ 基础设施快照
- **bjb1**: 工作目录 `/root/event-gated-adaptive-horizon`，2x GPU（RTX 系列）
  - exp_092: PID 313538, GPU 0, 3255 MiB — Mamba dt_embed 相关实验
  - exp_093: PID 313815, GPU 1, 2740 MiB — Mamba dt_embed 相关实验
- **westd**: 工作目录应在 `/root/` 下，2x GPU
  - westd cuda:1 刚分配给 Cheetah trained dt_emb s3 (seed=3) 实验，指令已在 Agent 队列中
- 具体 Python 路径/conda env/模型路径/数据集路径：需接手后 `get_project_status` + `load_project_config` 确认，本轮未在 context 中留存完整快照

### 3. 📊 当前状态
- **刚做完**：处理 exp_089/090 崩溃（参数名 bug），Agent 已修复并重提交为 exp_092/093
- **正在进行**：
  - exp_092 (bjb1 GPU0) RUNNING — 需 Agent 更新 registry 状态从 PREPARING→RUNNING 并补全 spec 追溯字段
  - exp_093 (bjb1 GPU1) RUNNING — 同上
  - Agent 队列中有 2 条待处理消息：(1) westd cuda:1 Cheetah 实验分配指令 (2) registry 修复指令（exp_092/093 状态+追溯字段）
- **Reviewer**：刚批准 RESET_BOTH，Reviewer 会重启新 session
- **审稿阶段**：论文已提交 Review Director 审稿（review_chat_id: `oc_dd4a07a509df7e5f9a31d65f776059bc`）

### 4. 📋 待办
- Agent 处理完 registry 修复消息 → 确认 exp_092/093 状态已更新为 RUNNING + spec 字段完整
- exp_092/093 训练完成 → 走 on-experiment-done 流程，分析结果
- westd cuda:1 Cheetah 实验提交成功 → 确认 RUNNING
- 审稿报告回传 `[审稿报告]` → Read `review-report-action.skill.md`，走 Holistic Pass + Action Matrix 流程
- 所有 GPU 空闲时 → 立即派下一批实验，不允许空卡 >10min

### 5. 🎯 战略上下文
- 项目核心：Event-Gated Adaptive Horizon — Mamba/SSM 类模型的事件门控自适应时间步长方法
- 当前处于 research + 审稿并行阶段：实验继续推进（补 ablation/seed），同时 Review Director 独立审稿
- **易错点**：
  - 参数名必须是 `--gate_dt_embed_dim` 不是 `--dt_embed_dim`（exp_089/090 教训）
  - Reviewer 报告"未修改"时先确认真源位置（论文在本地 workspace，代码在远程服务器）
  - Agent 队列深度 >0 时不要重复发同类指令
  - 审稿报告到达后禁止整体性"已知悉"，必须逐条处理


---
