# agent / loop_5.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`8036fb5751d7834e7159.json`](../../sessions/80/8036fb5751d7834e7159.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-16T05:01:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 **cuda:0 和 cuda:1**（westd-34887），绝不碰其他卡
- **D032 数据污染**：mistral_kl_s42 的 PPL 指标疑似与 Llama 30% 交叉污染，暂停引用该实验 PPL 数据，需重新验证原始日志
- **DDL 2026-05-25**（EMNLP ARR May），剩 9 天，所有实验决策必须以此为锚
- BCE iso-compute 已被 kill 两次（v1 tmux 被杀、v2 tmux 被杀），v3 用 nohup 启动——**不要再用 tmux 跑 BCE**
- 论文中 KL PPL 统一引用 **4-seed mean 12.00±0.07**，禁止用单 seed 最佳值 11.91
- SPON framing 禁止说 "KL subsumes SPON"，必须用 "marginal complement"
- BCE framing 禁止说 "anti-learning"，必须用 "objective mismatch"

### 2. 🖥️ 基础设施快照
- **服务器**：westd-34887，账号 root
- **工作目录**：/root/distill_sparse_swiglu/
- **Python**：/root/miniconda3/bin/python（conda base 环境，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型路径**：Llama-3.1-8B → /root/autodl-tmp/models/llama-3.1-8b；Mistral-7B → /root/autodl-tmp/models/mistral-7b
- **HF cache**：/root/autodl-tmp/.hf_cache
- **Checkpoints**：/root/distill_sparse_swiglu/checkpoints/（KL s42, SPON, BCE+comp, STE, Mistral KL, 30%/70% 等均在此）
- **活跃进程**：
  - bce_isocompute_v3_s42: wrapper PID 205597, train PID 205598, cuda:1, nohup, log=/root/distill_sparse_swiglu/logs/bce_isocompute_v3_s42.log
  - d030_kl50_uniform: PID 203702, cuda:0, tmux session, log=~/runs/distill_sparse_swiglu/d030_kl50_uniform.log
- **活跃 Cron**：2 个（分别监控上述两个 RUNNING 实验）

### 3. 📊 当前状态
上一轮 session 完成了 D030/D031 优先级重排、BCE v3 nohup 启动、d030_kl50_uniform 提交。两个 P0 实验正在跑：

| exp_id | GPU | 内容 | 状态 |
|--------|-----|------|------|
| bce_isocompute_v3_s42 | cuda:1 | BCE 2700步 iso-compute（D031, Reviewer Concern #2 defense） | RUNNING |
| d030_kl50_uniform | cuda:0 | KL 50% uniform per-layer allocation eval（D030, Claim 3 验证） | RUNNING |

**等待中**：
- bench_mistral_kl50_s42 (PENDING/killed)：Mistral 统一 few-shot eval，被 BCE v3 插队 kill，待 BCE 完成后重跑
- PREPARING 中 7 个实验全部是历史 killed 状态，无需处理

**Registry 总览**：52 registered, 19 success, 12 negative, 8 failed。plan_001-006 全部完成，plan_008 部分完成（d030 系列），plan_007/009 部分完成。

### 4. 📋 待办（条件触发式）
- **bce_isocompute_v3_s42 完成回调** → spawn Worker 分析 TEAL PPL（对比 KL 1000步 teal_sparse_ppl=12.00）。若 BCE 2700步 TEAL PPL >> 12.00 → 确认 KL loss function 优势（非计算量差异），更新 registry + report.md，汇报 Director。然后 cuda:1 释放 → 提交 bench_mistral_kl50_s42 重跑（D029）
- **d030_kl50_uniform 完成回调** → spawn Worker 提取 MMLU/GSM8K 结果。对比 30% uniform（MMLU 40.61%, GSM8K 7.35%）和 50% global top-k。若 50% uniform MMLU 仍有提升 → Narrative A 确认（allocation-sensitive vs allocation-invariant）；若 MMLU 也崩 → 高 sparsity 下 uniform 无法修复，需更保守的 Claim 3
- **两个实验都完成后** → 审视 Claim 3 framing：uniform 成功 → "per-layer allocation matters, uniform recovers knowledge tasks"；uniform 失败 → pivot 为 "PPL-downstream disconnect" discovery paper（contingency 路线已在 ROADMAP 中）
- **bench_mistral_kl50_s42 重跑完成** → 与 Mistral dense baseline 和 0-shot 旧结果对比，确认 D029 benchmark 一致性

### 5. 🎯 战略上下文
**核心论点**：KL distillation 使 SwiGLU LLM 的 contextual sparsity prediction 无需 error compensation，实现最简推理管线。

**决策链关键节点**：
- D028: 50% downstream collapse 是 universal（Llama + Mistral 都崩）
- D030: Global top-k 的 per-layer 不均匀是知识类任务崩溃的重要因素，uniform 30% 修复 MMLU +12pp 但 GSM8K 不动
- D031: BCE iso-compute 是 Reviewer Concern #2 的唯一 defense——如果 BCE 2700步仍然 PPL >> KL 1000步，则 KL 优势确认来自 loss function 而非计算量

**最容易判断错的事**：
1. **D032 数据污染**——mistral_kl_s42 的 teal_sparse_ppl 与 kl_sparsity30_s42_v3 完全相同（8.98），实际 30% v3 的正确值是 13.63。引用 Mistral PPL 时必须查原始日志，不能信 registry 历史值
2. **PREPARING 状态的 7 个实验都是 killed**——不要误以为它们需要处理，它们是历史遗留
3. **d030_kl50_uniform 用的是 50% KL predictor（mvp_kl_norm_v2_s42）做 uniform allocation eval**——不是重新训练，是推理时改 allocation 策略
4. **Paper framing 未锁定**——Narrative A 被 Director 选定但条件是 D030 50% uniform 结果确认后才更新 paper_framing.md，在此之前不动论文


---
