# agent / loop_6.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`5f0e65f68cfa1f3bbfad.json`](../../sessions/5f/5f0e65f68cfa1f3bbfad.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-15T00:54:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-17606 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- exp008_sft checkpoint 路径 `/root/autodl-tmp/checkpoints/exp008_sft/final/` 是后续所有 SFT/GRPO 的基础，不可覆盖
- expert data 中 `move X to Y` 是正确命令（ALFWorld admissible_commands 包含 move），之前 exp019_v2 错误地用 put 替换 move 导致 kill，不要重蹈

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，工作目录 /root/cost-verify-agent-rl
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型 base：Qwen3-1.7B；SFT checkpoint：/root/autodl-tmp/checkpoints/exp008_sft/final/（format 知识）、/root/autodl-tmp/checkpoints/exp017_expert_sft/final/（expert 知识但 format 退化）
- 数据：/root/autodl-tmp/expert_sft_v3/expert_sft_train.jsonl（2546 条，exp019b_v3 用）
- 活跃进程：无（两张 GPU 都空闲）
- Cron：无活跃 cron（reconcile 返回 0）

### 3. 📊 当前状态
exp019b_expert_sft_v3 刚失败（EXIT_CODE=1，只跑了 13 秒，启动即崩溃）。我已派 Worker `worker_diagnose_exp019b_v3_failed_20260514T205709` 去 SSH 读日志诊断根因，**该 Worker 尚未回调**。

Registry 关键状态：
- exp019b_expert_sft_v3: DONE/failed — 启动即崩，等 Worker 诊断结果
- exp019b_expert_sft_v2: PREPARING — 旧版，已被 exp019b_v3 取代，可忽略
- exp018_sft_grpo: PREPARING/killed — 等 SFT 成功后再启动
- 两张 GPU (cuda:0, cuda:1) 均空闲

### 4. 📋 待办
- Worker 诊断回调到达 → 读诊断报告，确定错误类型（数据格式/脚本bug/环境问题），修复后重新提交 exp019b_v3
- exp019b_v3 修复并成功 → 跑 20-episode eval（success ≥ 10% 且 format_ok ≥ 90% 且 action_is_valid ≥ 85%）
- eval 通过 → 启动 exp018/020 sparse GRPO（从 SFT checkpoint 开始，LR=5e-7, 30 steps，目标 success ≥ 20%）
- eval 未通过 → 向 Director 汇报，分析是数据问题还是方法问题，提出调整方案

### 5. 🎯 战略上下文
**核心研究方向**：B-IAVR（行为改变信号驱动的选择性自我验证），Qwen3-1.7B + ALFWorld + RAGEN/verl GRPO。当前卡在 MVP Phase A：ALFWorld success ≥ 20%。

**决策链关键节点**：
- GRPO 冷启动问题已确认（exp012b/015/016 三种 LR 全失败，base success ~1-2% 太稀疏）→ D016 pivot 到 Expert SFT warmup
- Dense reward shaping 也失败（exp013f reward gaming）→ 纯 sparse reward 是正确路线，但需要 SFT 先把 success 提上去
- exp017 第一轮 Expert SFT：5% success 但 format_ok 从 100%→75%（数据格式不匹配）→ D018 决定从 exp008_sft checkpoint 出发保留 format 知识
- Reward pipeline 确认正常（D017 纠正 D015 误诊）：raw_reward=0 是日志 artifact，不是 bug

**易错点**：
- exp019b_v3 是"两阶段 SFT"的关键——从 exp008_sft checkpoint（有 format 知识）出发用 expert data 微调，不是从 base model 从头 SFT
- 不要把 exp017 的 format 退化归因于 expert data 质量问题——根因是没有从 exp008_sft checkpoint 出发
- 两张 GPU 都空闲是失职状态，诊断 + 修复 + 重提交应在分钟级完成


---
