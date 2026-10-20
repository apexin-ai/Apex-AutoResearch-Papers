# agent / loop_9.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`6ae3516a5bfa0e37022a.json`](../../sessions/6a/6ae3516a5bfa0e37022a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-15T17:42:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: rtx5090-4x 的 cuda:0/1/2/3，无其他服务器 GPU 可用
- bf16 GRPO 实验 (plan_011) 用 `--no-quantize`，eval 也必须 `--no-quantize`，不能混用 QLoRA 加载
- GRPO eval 必须加载 Base + SFT adapter + GRPO adapter 三层，漏掉 `--sft_adapter` 会得到错误结果（之前 maxtok1536 eval 因此被 kill 重试过）
- submit_training_job 命令必须用 `bash -c "..."` 包裹（裸 source 会被 sh 执行失败，已踩坑 3 次）
- HF 相关环境变量必须带: `HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`（服务器无外网）

### 2. 🖥️ 基础设施快照
- **服务器**: rtx5090-4x (4× RTX 5090 32GB)
- **工作目录**: /root/autodl-tmp/freige
- **Python**: /root/miniconda3/bin/python（conda base 环境，不是 venv）
- **环境激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型**: /root/autodl-tmp/models/Qwen3-4B (base), /root/autodl-tmp/sft_output (SFT adapter)
- **GRPO checkpoints**: /root/autodl-tmp/grpo_ced_g8_bf16/ (10 checkpoints, step 10-100)
- **RSFT checkpoints**: /root/autodl-tmp/rsft_ced_r1/ (s42/s43/s44 seeds)
- **数据**: /root/autodl-tmp/data/docred, RSFT 数据 /root/autodl-tmp/rsft_filtered/ 和 /root/autodl-tmp/rsft_filtered_topk3/
- **W&B**: 未配置 entity/project（fetch_wandb_metrics 会失败，需从 SSH 拉 W&B 或读日志）
- **活跃进程** (截至 handoff):
  - cuda:0: mvp2_ced_reranker_poc (PID 178050) — CED 推理时重排
  - cuda:1: mvp2_eval_rsft_r2b_maxtok1536_r2 (PID 197381) — truncation 诊断
  - cuda:2: plan_004_dreeam_baseline (PID 213006) — DREEAM 复现
  - cuda:3: plan_011 eval Worker 刚派发 (worker_eval_plan_011_grpo_g8_bf16_eval_20260515T143923)

### 3. 📊 当前状态
**刚做完**: plan_011_grpo_g8_bf16 训练完成回调分析。训练 100 steps/554s，**无 mode collapse** (frac_zero_std=0)，best_reward=2.858 (step 85)，f1_reward=1.85。与 QLoRA 实验的灾难性遗忘形成根本对比。已更新 registry notes，已向 Director 汇报初步分析和决策请求。

**正在等待**:
- Worker `worker_eval_plan_011_grpo_g8_bf16_eval_20260515T143923` 回调 — eval checkpoint-85/100 on cuda:3
- mvp2_ced_reranker_poc (cuda:0) cron 回调
- mvp2_eval_rsft_r2b_maxtok1536_r2 (cuda:1) cron 回调
- plan_004_dreeam_baseline (cuda:2) cron 回调
- Director 对 plan_011 初步分析的回复（决策请求：C2 reframe 方向、是否补 QLoRA G=8 实验）

**Registry PREPARING**: mvp2_eval_rsft_s44（低优先级，s44 eval 已在其他条目完成）

### 4. 📋 待办（条件触发式）
- plan_011 eval Worker 回调 → 读 metrics。rel_f1>0.30 → 更新 registry conclusion=success + notes "decoupling is QLoRA-specific" + 向 Director 汇报确认 + 触发 on-experiment-done 完整流程（文献联动、反思实验计划）。rel_f1<0.05 → conclusion=negative + C2 原始 framing 加强
- Director 回复 C2 reframe 决策 → 更新 paper_framing.md + 可能需要补 QLoRA G=8 实验（控制变量隔离 G vs quantization）
- mvp2_ced_reranker_poc 完成 → 读结果判断 CED-as-reranker 是否 > SFT greedy。如是 → C1 补充 evidence
- mvp2_eval_rsft_r2b_maxtok1536_r2 完成 → 判断 EDCR gap 是 truncation artifact 还是 genuine RSFT behavior
- plan_004_dreeam_baseline 完成 → 对比 DREEAM Evi-F1 protocol，为 C1 建立 encoder baseline
- GPU 释放后 → 优先提交 plan_008 topk3 双变体训练 (cuda:2 全量 / cuda:3 过滤 CED=0)，然后 plan_001 flat-NLI RSFT ablation、plan_012 DPO+CED

### 5. 🎯 战略上下文
- **核心决策链**: D031(GRPO判死) → D040(MVP通过) → D044(Dream v1 reframe: CED降级/claims重构) → D045(DPO升P0) → D046(GRPO G=8首批)
- **publishability 三必要条件**: (1) RSFT test set rel_f1 > SFT ✅训练完成待test (2) DREEAM-protocol Evi-F1 可报告 ⏳plan_004 (3) GRPO decoupling G=8 复现 ⚠️ plan_011 训练指标暗示**不复现**
- **plan_011 大概率改变 paper framing**: bf16 G=8 训练完全稳定 → decoupling 是 QLoRA-specific → C2 需 reframe 为 "quantization+RL interaction causes decoupling"。这可能是**更 interesting** 的发现（量化噪声如何破坏 RL 信号），但 claim 边界更窄
- **易错点**: (1) plan_011 改了两个变量 (G=4→8 + QLoRA→bf16)，如果 eval 确认不 collapse，可能需要补 QLoRA G=8 实验隔离变量 (2) TaskEvalCallback 的 rel_f1 是已知 bug（D038），**不要**用训练时的 F1 metric 作为最终结论，必须等全量 eval (3) W&B fetch 会失败（未配置），用 SSH 读日志或 eval output 的 metrics.json
- **Dream v1 不达标** (best=2.5)，re-dream 正在跑验证 reframe 效果。如果 re-dream 也不过 → 可能需要更大 scope 调整


---
