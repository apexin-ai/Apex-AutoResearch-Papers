# agent / loop_18.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`30a70d05f9041b58e1fb.json`](../../sessions/30/30a70d05f9041b58e1fb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-17T23:12:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-23072 cuda:0/1, westd-11672 cuda:0/1/2/3（ROADMAP 说 cuda:0/1 但 report.md 显示 6 张全分配）
- EMNLP 2026 ARR May 25 提交，距今 ~8 天
- eval_humaneval_grpo_standard_20_2048 当前 ANALYZING 状态，Worker 已派出但尚未回调——下一个"你"收到 Worker Done 后再推进到 DONE，不要重复派 Worker
- D052 决策：C3 降级为 observation，C2 collapse gradient 升为主力贡献；D053：CKA-only GRPO 最稳定，"Redundancy-Stability" 叙事
- MATH-500 GRPO 对比不可用于 C3 论证（D051，配置不公平）

### 2. 🖥️ 基础设施快照
- **westb-23072**: 2× ~98GB GPU, 工作目录 ~/runs/recovery_aware_struct_prune/
- **westd-11672**: 4× ~95GB GPU, 工作目录 ~/runs/recovery_aware_struct_prune/
- 项目本地路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/
- 活跃进程:
  - grpo_random_20: westb-23072 cuda:1, PID 719679
  - grpo_cka_only_20: westb-23072 cuda:0, PID 725227
  - eval_math500_grpo_rasp_20_v3: westd-11672 cuda:3, PID 31706
  - eval_math500_grpo_standard_20: westd-11672 cuda:1(?), PID 14556
- Cron 监控这 4 个实验（reconcile 确认 all running）
- 空闲 GPU: westd-11672 cuda:0, cuda:2（report.md 标注）

### 3. 📊 当前状态
收到 eval_humaneval_grpo_standard_20_2048 完成回调，已派 Worker (`worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T175504`) 去 SSH 读日志提取 pass@1 指标。Worker 尚未回调。

Registry 概况：165 实验，ANALYZING 1（eval_humaneval_grpo_standard_20_2048），RUNNING 4（上述），PREPARING 18。
DONE 142 中: success 92, negative 15, failed 24, killed 11。

已知 HumanEval@2048 矩阵：
- GRPO RASP 20%: success（具体数值待查）
- SFT RASP 20%: 10.37%
- SFT Standard 20%: negative
- GRPO Standard 20% @512: 1.83%（truncation artifact）
- GRPO Standard 20% @2048: 等 Worker 分析

### 4. 📋 待办
- Worker `worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T175504` 回调 → 读分析报告 → update_registry(conclusion=..., metrics=...) → 刷新 report.md → 汇报 Director
- eval_math500_grpo_rasp_20_v3 cron 回调 → 派 Worker 分析 → 与 sft_rasp_20 MATH-500 对比 → C1 验证
- eval_math500_grpo_standard_20 cron 回调 → 同上，与 sft_standard_20 对比
- grpo_random_20 / grpo_cka_only_20 完成 → D053 collapse gradient 对比分析（4-way: RASP/Standard/CKA-only/Random collapse 模式）
- 空闲 GPU (westd cuda:0, cuda:2) → 应提交 PREPARING 中的实验（eval_humaneval_sft_standard_20_2048 或 scoring_ablation_batch 等），向 Director 建议
- 25% GRPO 启动需 Director 分配 westb GPU（当前被 grpo_random_20 和 grpo_cka_only_20 占用）

### 5. 🎯 战略上下文
- 核心叙事 (D044/D045): GRPO alignment 在结构剪枝后 fundamentally fails — reward 提升但 accuracy 不跟随（universal decoupling）。剪枝引入 training collapse，severity 诊断 structural damage 类型。
- 三个 Claims: C1=reward-accuracy decoupling, C2=collapse gradient (主力), C3=降级为 observation
- 当前阶段: 20% 核心数据完成，正在补 HumanEval/MATH-500 cross-benchmark 验证 + scoring ablation (4-way collapse 对比)
- 25% sparsity expansion + Qwen2.5-Math-7B cross-model 验证是 scope expansion，时间紧
- 易错点: 不要把不同 max_new_tokens 的 HumanEval 结果直接对比（512 vs 2048 有 truncation artifact）；MATH-500 GRPO 对比配置不公平不能用于 C3


---
