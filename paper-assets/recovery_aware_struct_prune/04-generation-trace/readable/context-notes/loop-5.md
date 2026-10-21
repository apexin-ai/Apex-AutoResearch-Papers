# director / loop_5.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`57b266a017fe84ef92c7.json`](../../sessions/57/57b266a017fe84ef92c7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T01:48:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-23072 的 cuda:0 和 cuda:1（约束 C001）
- 两卡当前跑 GRPO Stage 2（grpo_stage2_rasp_20 / grpo_stage2_standard_20），不得中断
- SFT checkpoint 是 GRPO 的输入，不能删除或覆盖
- registry 中 sft_rasp_20 / sft_standard_20 的 conclusion=success 是基于 EOS 修复目标，不代表 RASP 在 SFT 阶段优于 Standard（实际 Standard 64% > RASP 57%）

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (connect.westb.seetacloud.com)，账号 root
- 工作目录：/root/recovery_aware_struct_prune
- 模型：DeepSeek-R1-Distill-Qwen-7B（路径需向 Agent 确认）
- SFT checkpoint 路径：Agent 侧管理，在 /root/recovery_aware_struct_prune/ 下
- 活跃进程：grpo_stage2_rasp_20 (PID 263888, cuda:0) + grpo_stage2_standard_20 (PID 263966, cuda:1)
- Cron：两个 GRPO 实验各有 120s 间隔的训练监控 cron
- 评估脚本：/tmp/quick_eval.py（100 greedy + 5 sampling，seed=42）

### 3. 📊 当前状态
- **GRPO Stage 2 双卡并行运行中** — 这是项目的决定性实验（D015）
- 已派 Agent 做 GRASPrune 代码准备（plan_005 前置）和 full GSM8K eval 脚本准备（plan_001 前置），均不占 GPU
- Reviewer 刚完成 Claim 3 叙事逻辑审查（warning 级别），结论：排序反转叙事有结构性弱点，SFT 57% vs 64% 在 N=100 下不显著（p≈0.32），需 full eval 确认
- Agent 队列：正在处理 GRASPrune/full eval 准备指令 + 若干 worker:done 回调
- Dream simulate 已 launch 但未收到完成回调

### 4. 📋 待办
- GRPO Stage 2 cron 回调显示训练完成 → 立即跑 100 样本 eval（或 full 1319 样本）对比 RASP vs Standard
- GRPO RASP >> Standard (>10pp) → 全面推进 plan_001-014，Claim 1+3 成立
- GRPO RASP > Standard (5-10pp) → 优先 plan_001 (full eval) + plan_006 (multi-seed) 确认显著性
- GRPO RASP ≈ Standard (<5pp) → Claim 3 死亡，降级到 Claim 1 主线，考虑 25% sparsity 探索
- GRPO Standard > RASP → 核心假设失败，pivot 到负向发现论文或 CKA-as-predictor 分析论文
- Dream 回调到达 → Read dream-report-action skill 按流程处理
- Reviewer Claim 3 审查建议：GRPO 期间做 full GSM8K eval on SFT models 确认 SFT 差异显著性 — **已派 Agent 准备脚本，GRPO 完成后立即执行**

### 5. 🎯 战略上下文
- 核心决策链：D006(post-prune 29% vs 1%) → D014(MVP PASS) → D015(SFT Standard>RASP 不改方向，GRPO 是生死局)
- **最容易判断错的事**：看到 SFT Standard>RASP 就恐慌 pivot。SFT 不是核心测试，Claim 3 本来就预测 SFT 和 GRPO 偏好不同。只有 GRPO 也失败才需要 pivot
- **Reviewer 的关键警告**：即使 GRPO RASP>Standard，Claim 3 的"排序反转"叙事仍需加固——SFT 差异在 N=100 下不显著，需要 full eval + 至少 1 个额外 sparsity level + 多 seed。不要在 GRPO 成功后就觉得万事大吉
- 实验成功率低（2/11 success），大量早期失败源于 sampling 无 EOS 问题，SFT warmup 已修复此问题
- 目标 EMNLP 2026 ARR May 25（距今 10 天），时间紧但双卡 480 GPU-hours 预算充足


---
