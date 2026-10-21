# director / loop_5.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`06b472c387903beffe49.json`](../../sessions/06/06b472c387903beffe49.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T05:20:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-17606 的 cuda:0, cuda:1（2 张 RTX PRO 6000 Blackwell 94GB）
- SFT baseline 数据必须引用 **16-episode eval 的 6.25%**，早期 4ep eval 的 25% 是小样本噪声，不能作为决策依据（D024/Reviewer 纠正）
- SFT 数据必须用 RAGEN 精确格式（v4+），否则 val 0%（exp019b→exp021 教训）
- Worker 诊断结论必须 Reviewer 交叉验证再信——本项目两次 Worker 误诊（exp021 OOD 源、exp016 reward bug）
- submit_training_job 提交训练（不用 nohup），否则 cron 误报
- Checkpoint 路径必须含 "qwen" 字符串（train.py:137 断言），用 symlink 解决

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606 (connect.bjb1.seetacloud.com)，账号 root
- 工作目录：/root/cost-verify-agent-rl
- Python：conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- GPU：2× RTX PRO 6000 Blackwell 94GB (cuda:0, cuda:1)
- SFT checkpoint：/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/（symlink: qwen3_exp021_ragen_sft_v4）
- 模型：Qwen3-1.7B (Instruct 版本，无 -Instruct 后缀)
- TMPDIR=/root/autodl-tmp/tmp/（/tmp 只 30GB）
- W&B：未配置，实验通过 cron + 日志监控
- 活跃进程：无（GPU 空闲，等 verl-agent 代码就绪）

### 3. 📊 当前状态
**刚完成**：D025/D026 决策——RAGEN GRPO 路线终止（exp020b/exp022/exp023c 三次一致退化），pivot 到 verl-agent GiGPO。

**Agent 队列**：正在处理 D025 pivot 指令，队列中还有 D026 verl-agent 指令 + 一条 worker_done 回调（exp024-success-gated-reward 已完成）。Agent 忙，idle 330s。

**Registry 关键状态**：
- 无 RUNNING 实验
- exp021_ragen_sft_v4: DONE (success) — RAGEN 格式 SFT baseline，6.25% success (16ep)
- exp023c_grpo_serial: DONE (failed) — 最后一次 RAGEN GRPO，8 步后退化 + 磁盘满
- exp024_success_gated_reward: Worker 刚完成，尚未处理回调
- 17 个 PREPARING 状态的历史实验（已废弃的旧路线残留）

**等待中**：Agent 处理完 D025/D026 后应开始 verl-agent GiGPO cherry-pick 工作（Plan C，预估 3-5 天代码整合）。

### 4. 📋 待办（条件触发式）
- Agent 处理完 D025/D026 → 确认 Agent 理解 verl-agent pivot 方案，开始 cherry-pick GiGPO + step-independent rollout 代码
- exp024 worker_done 回调被 Agent 处理 → 审查 exp024 结果（success-gated reward 实验），判断是否有增量价值
- verl-agent GiGPO 代码就绪 → 审批 dry-run 实验，确认 SFT checkpoint 兼容性
- dry-run 通过 → 审批首次 verl-agent 风格 GRPO 实验（从 exp021 checkpoint 出发）
- verl-agent GRPO success ≥ 20% → MVP pass，调 complete_mvp()，启动 post-mvp-kickoff
- verl-agent GRPO 也退化 → 评估 SPEAR 算法（artifacts/grpo_alternatives_survey.md 已有调研），或考虑换更大模型

### 5. 🎯 战略上下文
**核心研究方向**：B-IAVR——训练 interactive agent 选择性自我验证，用 action change 作为 verification informativeness 的 reward。基于 Self-Guide (arXiv 2604.03098)。

**关键决策链**：
- D017-D018: 发现 sparse GRPO 冷启动问题（base success ~4.7%，几乎全零 reward）
- D020-D021: 两阶段 Expert SFT 路线验证，SFT→RAGEN 格式对齐是关键
- D025: Sparse GRPO 路线终止（3/3 退化），dense reward gaming 也失败
- D026: Pivot 到 verl-agent GiGPO（Self-Guide 论文用的框架，达 72.7%）

**最容易判断错的事**：
1. 不要把 exp021 的 25% success 当 baseline——那是 4ep 噪声，16ep 可靠数据是 6.25%
2. GPU 当前空闲但这是合理的——等 verl-agent 代码整合，不是怠工。代码就绪后立即派实验
3. RAGEN GRPO 路线已终止，不要再尝试调参救活（3 次一致退化，根因是框架层面差异）
4. verl-agent 72.7% 是论文数字，复现可能有差距，MVP 目标保持 ≥20% 即可
5. exp024 是 D025 之前派出的 success-gated reward 实验，可能已属废弃路线，需看结果再判断


---
