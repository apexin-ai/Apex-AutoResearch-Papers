# director / loop_4.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`75330bfb952fb66afdbc.json`](../../sessions/75/75330bfb952fb66afdbc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-14T21:47:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 + cuda:1（westb-23072），约束 C001
- 数据盘 89%（剩 29GB）——启动新实验前必须先清理旧 checkpoint（killed GRPO runs: grpo_rasp_20/grpo_standard_20 output dirs）
- grpo_rasp_20_fast / grpo_standard_20_fast 状态是 **inconclusive (truncation artifact)**，不是 negative——不要基于这两个实验做任何 pivot 决策
- run_grasp_prune.sh MODEL_PATH 仍然错误（报告 3 次未修）：当前 `/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B` → 正确 `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (connect.westb.seetacloud.com)，2× RTX PRO 6000 94G
- 工作目录：/root/recovery_aware_struct_prune
- 模型：/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B
- Eval 脚本：src/run_full_eval_all.sh（并行双 GPU 5 模型）、src/run_full_eval_d008_parallel.sh
- GRPO 脚本：src/run_grpo_multiseed.sh（参数化 method/sparsity/gpu/seed）
- W&B / Git：未配置
- 活跃进程（截至 ~22:00 UTC）：GPU0 baseline eval (PID 239932)、GPU1 pruned_standard eval (PID 239929)——日志断流（tee 进程死了），需通过 results/ 目录 JSON 或 ps 监控

### 3. 📊 当前状态
**刚做完**：D008 更新 MVP 标准（model-level significance）、D009 判定 GRPO 截断伪阴性、D010 审批 max_completion=4096 重跑。
**正在进行**：full eval（baseline + pruned 模型 × 1319 samples）在双 GPU 跑。recovered 模型 eval 无价值（应跳过/kill）。
**等待中**：eval 完成后立即启动 D010 GRPO 4096 重跑（grpo_rasp_20_4k + grpo_standard_20_4k）。Agent 队列深度 6，已发 urgent + replace 指令要求 eval 完有价值部分后切 GRPO。

### 4. 📋 待办
- baseline + pruned_rasp + pruned_standard eval 完成 → 记录 1319-sample accuracy（D008 要求）→ kill recovered eval → 清理旧 checkpoint → 启动 D010 GRPO 4096 双卡（nohup）
- D010 GRPO 完成（~7h from start）→ full eval 1319 samples（5 模型）→ 按场景判定 MVP：A（50%+）= pass、B（35%）= 看显著性、C（≤30%）= 追加 epochs+lr 不急 pivot
- MVP pass → complete_mvp → post-mvp-kickoff（framing → plan → dream → roadmap）
- GraSP 路径 bug 修复 → Phase 2 P2 就绪

### 5. 🎯 战略上下文
- **核心发现**：20% sparsity 下 RASP 29% vs Standard 1%（matched params, p<0.0001）——这是 RASP 的硬证据，不依赖 recovery
- **MVP claim 分层（D008）**：MVP 只证 "RASP preserves reasoning better"（model-level），"CKA predicts recoverability"（per-group ρ）留 Phase 2 P4
- **1024 截断教训（D009）**：DeepSeek-R1 在 sampling+temp=0.7 下推理链远长于 greedy，剪枝后更冗长。后续所有 GRPO 默认 max_completion=4096
- **RewardDesertCallback 不会触发**：patience×logging_steps=500=total_steps，不能作为 early stopping evidence
- **易错点**：不要把截断 GRPO 的结果当真实 negative；不要在 MVP 前启动论文写作；Phase 2 P1 是多 seed 重复（效应<10pp 时必须）
- **决策链**：D001(MLP-only ok) → D005(20%/25% sparsity) → D006(Scenario B confirmed) → D007(快速 GRPO) → D008(MVP 标准更新) → D009(截断伪阴性) → D010(4096 重跑)
- **EMNLP ARR May 25，距今 10 天**


---
