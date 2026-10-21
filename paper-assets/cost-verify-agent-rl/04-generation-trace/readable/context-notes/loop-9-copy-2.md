# agent / loop_9.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`67a5c9a4f25bdc872f17.json`](../../sessions/67/67a5c9a4f25bdc872f17.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-15T13:55:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**bjb1-17606 cuda:0, cuda:1** 仅此两张，其他 GPU 编号绝对不碰
- **禁止 WANDB_MODE=disabled + cron 监控同时使用**（D029 事故：cron 5 次检测不到 W&B sentinel 后 auto-resolve 为 failed，实际进程还在跑）
- Cron 监控 PID 必须是 **Ray TaskRunner PID**（781795），不是 bash wrapper PID（778562）
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- exp026 训练 ~40min/step × 150 步 ≈ 100h，**不要因为看起来慢就 kill 它**——这是正常速度

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-17606，账号 root
- **工作目录**：/root/cost-verify-agent-rl
- **Python**：/root/miniconda3/bin/python（conda base 环境，非 venv）
- **模型**：Qwen3-1.7B，SFT checkpoint `/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/`
- **框架**：RAGEN + cherry-picked step-independent rollout（从 verl-agent 移植）
- **活跃进程**：exp026 PID=781795（Ray TaskRunner），tmux 管理，cuda:0+cuda:1
- **Cron**：exp026_step_independent_grpo 活跃（reconcile 确认 pid=781795 still running）
- **Log 路径**：`/root/autodl-tmp/tmp/ray/session_2026-05-15_18-38-45_487055_778562/logs/worker-f5a9c771de63c207b8db019edc7dedd89a425c2fe97314a2669cdd43-01000000-781795.out`
- **W&B**：WANDB_MODE=disabled（指标只能从 Ray worker stdout 解析）
- **Worker 池**：0（所有 Worker 已完成）

### 3. 📊 当前状态
**exp026_step_independent_grpo 是唯一 RUNNING 实验**，也是 MVP 的关键赌注。

前 3 步训练指标（从 Ray logs 解析）：
| Step | Success | Entropy | KL | Grad Norm | Reward Mean |
|------|---------|---------|-----|-----------|-------------|
| val_before | 6.25% | — | — | — | — |
| 1 | 21.88% | 0.267 | 0.180 | 14.43 | 1.218 |
| 2 | **32.81%** | 0.317 | 0.097 | 15.62 | 1.620 |
| 3 | **17.19%** | 0.387 | 0.262 | 15.65 | 1.079 |

Step 2 已超 MVP 20% 阈值，但 step 3 回落到 17.19%——可能是噪声（pass_at_16 从 1.0 降到 0.75，action_is_valid 仍~64%）。**Step 5 是首次正式 val eval，是判定 MVP 成败的关键点。**

已并行完成的 CPU 任务（不需要重做）：
- B-IAVR 核心机制代码已写好（action-change gating），Reviewer 审查通过（D031），Phase B 前需解决 2 个 warnings
- Related work survey 完成
- Literature map 更新完成
- exp026 standalone eval 脚本已写好

等待中：
- exp026 cron 回调（训练完成或失败时自动触发）
- 无等待中的 Worker 回调
- 无等待 Director 决策的事项

### 4. 📋 待办（条件触发式）
- **exp026 cron 回调到达（训练完成）** → spawn Worker 跑 standalone eval（脚本已就绪）→ 按 on-experiment-done skill 分叉处理
- **Step 5 val success ≥ 20%** → 确认 MVP Phase A 达标，汇报 Director，准备 Phase B（B-IAVR action-change gating，代码已就绪）
- **Step 5 val success < 20% 但训练未 collapse**（entropy 稳定） → 继续跑到 step 10-15 再判
- **训练 collapse**（entropy → 0 或 success → 0） → 早停，评估 GiGPO Phase 2（step-level advantage grouping）
- **exp026 最终 negative（150 步后 val < 20%）** → 按 red-section 产出 Framing 调整提案，禁止默默跑下一个实验
- **GPU 空闲（exp026 结束后）** → 立即铺下一个实验，不留 GPU 空窗

### 5. 🎯 战略上下文
**核心叙事**：B-IAVR（Behavior-Informed Agent Verification via RL）——训练 agent 基于 action change 信号选择性自我验证。基于 Self-Guide (arXiv 2604.03098) 框架。

**决策链精华**：
- D025/D026: RAGEN 原版 GRPO 3/3 失败，根因是 full-history context 爆炸 → pivot 到 step-independent rollout
- D028: verl-agent 因 AutoDL cgroup pids.max 限制无法运行 → cherry-pick 核心算法到 RAGEN
- D032: exp026 前 2 步 success 6.25%→32.81%，验证 step-independent + discounted returns 的方向正确
- D034: 两级阈值——MVP=20% val（训练可行性），论文 baseline 另算

**易判断错的事**：
1. Step 3 success 回落到 17.19% **不要恐慌**——GRPO 早期波动正常，pass_at_16=0.75 说明模型仍有探索能力。等 step 5 val 再判
2. **不要因为 WANDB_MODE=disabled 就想重启训练开 W&B**——重启 = 浪费已跑的 steps + GPU 时间。从 logs 解析指标即可
3. exp025c 状态是 PENDING/failed——这是 verl-agent 路线的残留，**不要尝试恢复它**，该路线已被 D028 终止
4. 大量 PREPARING 状态的旧实验（exp014a/b/c, exp018, exp019b/c, exp020c/d 等）都是历史遗留，**不要去清理或恢复它们**——它们属于已废弃的 RAGEN GRPO / dense reward 路线


---
