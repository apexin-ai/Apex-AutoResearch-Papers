# reviewer / loop_5.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`ced39ae2101bcee245bb.json`](../../sessions/ce/ced39ae2101bcee245bb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T00:54:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1 only（C001 约束，bjb1-17606）
- exp020b GRPO 正在跑（PID 389434/389435 Ray workers，双卡各 40GB）——不要 `ray stop --force` 或启动新 GPU 任务
- Cron 误报模式：SFT 实验用 `report_to="none"`，cron 无法区分正常退出与崩溃，已连续 4 次误报（exp017/019/019b×2）——收到 cron on_failed 先 tail log 确认再下结论
- ALFWorld 动作格式："move X to Y" 是唯一合法 placement action，"put X in/on Y" 不合法（exp019 踩过坑）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606(root)，工作目录 `/root/cost-verify-agent-rl`
- Python：`/root/miniconda3/bin/python`（conda base env）
- 模型 checkpoint：`/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final/`（Qwen3-1.7B，3.4GB）
- Symlink：`/root/autodl-tmp/checkpoints/qwen3_exp019b_sft` → 上述 final/（RAGEN 用）
- 数据：`/root/autodl-tmp/expert_sft_v3/`（train 2546, val 133）
- RAGEN config：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp018_sft_grpo.yaml`
- 活跃进程：exp020b Ray workers PID 389434, 389435（双卡各 ~40GB，step 3/30）
- 无 W&B（SFT/GRPO 都用 `logger: ['console']`）
- Eval 结果：`/root/cost-verify-agent-rl/artifacts/eval_exp019b_fast.json`

### 3. 📊 当前状态
**刚做完**：确认 exp019b SFT 成功（20% success, 100% format, 85.3% valid），修正 exp020b initial val 0% 为样本量问题（4 episodes），确认 exp020b GRPO step 1 train success=18.75% 与 eval_sft_fast 一致。

**Registry 活跃实验**：
- `exp020b_grpo_from_sft`: PREPARING（实际 RUNNING，step 3/30，~274s/step，ETA ~2h from step 3）
- `exp020d_grpo_from_sft`: PREPARING（exp020d 命令含 `ray stop --force`，未实际运行——被 cleanup worker 处理）
- `exp021_sft_ragen_format`: PREPARING（计划用 v4 RAGEN 格式数据重做 SFT，尚未启动）

**等待**：exp020b 完成后需审查 val success 是否 ≥20%。exp021 启动时需审查数据格式。

### 4. 📋 待办
- exp020b step 20 val 结果出来 → 检查 success 是否提升（pass@1 > 0%），action_is_valid 趋势
- exp020b 完成（30 steps） → 审查最终 val metrics，对比 baseline 20%，判断 GRPO 是否有效
- exp021 启动 → 审查 v4 数据格式（RAGEN Turn/State/Reward 结构）是否正确，system prompt 是否与 RAGEN agent_proxy 一致
- 任何新实验启动 → 检查 GPU 合规（cuda:0,1）+ 不与 exp020b 冲突
- cron on_failed 通知 → 先 `tail log` + `nvidia-smi` 确认，不盲信

### 5. 🎯 战略上下文
**核心进展链**：base 4.7% → exp008_sft format only → exp017 expert SFT 5%（无 admissible actions）→ **exp019b expert SFT + admissible actions 20%** → exp020b GRPO（进行中）

**关键发现**：admissible actions 在 observation 中是 success rate 从 5%→20% 的关键因素。

**易判断错的事**：
1. RAGEN initial val 只有 4 episodes（`env_groups=4, group_size=1`），0% success 不代表模型退化——看 train rollout（64 episodes）才准
2. action_is_valid 在 RAGEN train（temp=1.0）vs eval_sft_fast（temp=0.4）会有大差异（58% vs 85%），这是温度导致的，不是 bug
3. `enable_response_mask=True` 在 exp020b 中生效（通过 symlink 路径含 "qwen" 绕过 assertion），如果后续要禁用，正确 hydra override 是顶层 `enable_response_mask=false`，不是 `actor_rollout_ref.model.enable_response_mask`
4. Registry 状态可能不准——exp020b 显示 PREPARING 但实际 RUNNING，以 GPU 进程为准


---
