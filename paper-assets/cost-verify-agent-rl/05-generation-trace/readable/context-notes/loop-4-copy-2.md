# agent / loop_4.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`115c721eab3d59fa8c2d.json`](../../sessions/11/115c721eab3d59fa8c2d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T12:42:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 cuda:0, cuda:1** @ bjb1-17606（RTX PRO 6000 Blackwell 94GB × 2）
- **磁盘告急**：/root/autodl-tmp 95% 已用（仅剩 4.1GB）。下一个实验**必须先清理旧 checkpoint**（exp012_grpo、exp013b_grpo、exp013e 等），否则写入即崩
- submit_training_job 启动命令必须包含完整环境变量（见基础设施快照），缺任一个都会复现历史崩溃
- exp013f 结论是 **negative**，按 red-section 规范必须先产出 Framing 调整提案 → Director 审批，**禁止直接跑下一个实验**
- cgroup 内存限制 220GB，Ray object_store_memory 硬编码 30GB（train.py:203），不可改大

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-17606，2× RTX PRO 6000 Blackwell 94GB
- **工作目录**：/root/cost-verify-agent-rl/RAGEN（训练入口 `python train.py --config-name=&lt;cfg>`）
- **Python**：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- **激活命令**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**：
  - SFT checkpoint: /root/autodl-tmp/checkpoints/exp008_sft/final（symlink qwen3_sft_final）
  - GRPO step 5 checkpoint: /root/autodl-tmp/checkpoints/exp008_grpo/global_step_5
  - exp013f checkpoint: /root/autodl-tmp/checkpoints/exp013f/global_step_30
- **数据**：/root/autodl-tmp/alfworld/（3553 train games），SFT 数据 /root/autodl-tmp/sft_data/alfworld_sft_ragen.jsonl（1200 条）
- **必需环境变量**（启动脚本模板）：
  ```
  TMPDIR=/root/autodl-tmp/tmp/
  ALFWORLD_DATA=/root/autodl-tmp/alfworld
  RAY_memory_monitor_refresh_ms=0
  RAY_SYSTEM_MEMORY=210000000000
  HYDRA_FULL_ERROR=1
  ```
- **活跃进程**：无。无 tmux session、无 cron 任务。GPU 空闲。

### 3. 📊 当前状态
**刚完成**：exp013f 30/30 步训练完成，结论 **negative**（dense reward gaming）。action_is_valid 60%→97.5% 但 success 始终 0-8%→0%。模型最大化 valid_action_bonus（累计 4.5）而忽略 success_reward（10.0）。D012 已记录。

**Registry 摘要**：
- 25 个实验，0 个 RUNNING，0 个 QUEUED/ALLOCATED
- 成功：exp008_sft（SFT warmup，action_is_valid 90%）
- 负向：exp013f（dense reward gaming）
- 其余全部 failed/killed（基础设施问题或 reward 设计问题）
- 多个 PREPARING 状态的旧实验（exp005/exp008/exp007_dryrun/exp_003* 系列）是历史残留，可忽略

**等待中**：无 Worker 回调、无 Cron、无 Director 决策。exp013f negative 的 Framing 调整提案**尚未产出**——这是本 session 未完成的关键任务。

### 4. 📋 待办（条件触发式）
- **立即（新 session 启动后第一件事）**→ 产出 exp013f 的 red-section Framing 调整提案，发 `main_agent_post_to_director`。提案必须包含 3 种 narrative 备选 + 下一步实验方案
- **磁盘清理**（在提交任何新实验前）→ spawn worker 清理 /root/autodl-tmp 旧 checkpoint（exp012_grpo、exp013b_grpo、exp013e、exp013d 等），释放至少 50GB
- **Director 审批 Framing 提案后** → 按审批方向设计 exp014（大概率是 success-gated reward 或 curriculum learning）
- **如果 Director 选 success-gated reward 方向** → 需改 RAGEN 代码：valid_action_bonus 只在 trajectory 最终 success 时发放（或 bonus 与 success 概率挂钩）
- **如果 Director 选 curriculum/expert-SFT 加强方向** → 需更多 SFT 数据（当前 1200 条，目标 5000+），可能用 expert trajectory 生成
- **Phase B 启动条件**：Phase A success ≥ 20% → FSDP→HF 转换（脚本就绪 scripts/convert_fsdp_to_hf.py）→ Phase B 配置更新 → 提交

### 5. 🎯 战略上下文
**核心结论链**：
- D004: Qwen3 格式修复 → D006: SFT warmup → D007/D008: format_penalty 劫持梯度 → D010: sparse reward 冷启动死锁 → D011: dense reward shaping → D012: **reward gaming**
- 这条链证明了：(1) GRPO 学习能力没问题（action_is_valid 可以从 8%→97.5%）；(2) 问题在 reward 设计——sparse 太难、dense 太容易 game

**最容易判断错的事**：
- **不要以为再调 valid_action_bonus 比例就能解决**。问题不是比例（从 0.5 调到 0.15 只是推迟了 gaming），而是 dense reward 可以被独立最大化。下一步必须是**结构性改变**（success-gated / curriculum / 子目标 reward）
- **不要跳过 Framing 提案直接跑实验**——这是 L1 红线（negative 结果必须先走 red-section）
- **不要忽略磁盘问题**——4.1GB 剩余空间，任何新实验都会立即写满
- Phase B 代码虽然就绪（68 tests pass），但完全被 Phase A 阻塞，不要试图绕过
- ALFWorld score 是纯二值 0/1（memory.md 已记录），不存在中间进度信号，这是整个 reward shaping 困境的根源


---
