# agent / loop_14.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`50eb0b5c432ab5d9a531.json`](../../sessions/50/50eb0b5c432ab5d9a531.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-16T14:53:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 rtx5090-4x 的 cuda:0/1/2/3（无其他服务器分配）
- plan_016_llama_grpo_qlora 正在 cuda:2 跑（PID 346621），不要 kill 或抢占
- RSFT candidate generation 三个进程（1.7B/8B/LLaMA）分别占 GPU 0/3/1，完成前不可抢占
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`——服务器用 conda 不是 venv
- Evidence tax 的 1.7B 数据需用 442 docs 非截断子集（D083），不要用全集数据做对比
- C3 claim 已降级（D056 CED vs flat-NLI 统计不可区分），不要再为 C3 跑新实验

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x（4× RTX 5090 32GB）
- 工作目录：`/root/autodl-tmp`（代码在 `/root/autodl-tmp/freige/`）
- Python：`/root/miniconda3/bin/python`（conda base env）
- 模型路径：`/root/autodl-tmp/models/` (Qwen3-1.7B, Qwen3-8B, Meta-Llama-3.1-8B)
- HF cache：`/root/autodl-tmp/.hf_cache/`
- NLI 模型：`/root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7`
- RSFT 输出目录：`rsft_candidates_1_7b` / `rsft_candidates_8b` / `rsft_candidates_llama_3_1_8b`
- 活跃进程：
  - plan_016_llama_grpo_qlora: PID 346621, cuda:2, cron 监控中
  - plan_006_qwen3_8b_rsft_candidates: PID 349382, cron 监控中
  - plan_006_qwen3_1_7b_rsft_candidates: PID 349794, cron 监控中
  - plan_016_llama_rsft_candidates_r2: GPU 1, cron 未注册（需确认）
  - plan_014_no_evidence_eval_d076: 状态待确认（可能已完成未回调）

### 3. 📊 当前状态
上一轮完成了 D077 scope 扩展的大部分基础工作：模型下载、SFT 训练、evidence tax 评估（1.7B/4B/8B/LLaMA 全覆盖）、D076 paired t-test。现在处于 **RSFT candidate generation + GRPO QLoRA** 并行阶段。

**RUNNING (5):**
| exp_id | GPU | 说明 |
|--------|-----|------|
| plan_016_llama_grpo_qlora | cuda:2 | LLaMA GRPO QLoRA 训练（验证 decoupling 跨家族） |
| plan_006_qwen3_1_7b_rsft_candidates | cuda:0 | 1.7B RSFT 候选生成（~57/3053 docs as of 22:03） |
| plan_006_qwen3_8b_rsft_candidates | cuda:3 | 8B RSFT 候选生成（~47/3053 docs） |
| plan_016_llama_rsft_candidates_r2 | cuda:1 | LLaMA RSFT 候选生成 |
| plan_014_no_evidence_eval_d076 | ? | 4B no-evi eval（可能卡住或已完成） |

**等待中：**
- 3 个 cron 回调（RSFT gen 完成 → 触发 CED scoring）
- plan_014_no_evidence_eval_d076 状态不明（无 cron，需派 Worker 检查）

### 4. 📋 待办（条件触发式）
- plan_006_qwen3_1_7b_rsft_candidates 完成 → spawn Worker 执行 CED scoring（命令已在 memory.md） → 得分后 RSFT train
- plan_006_qwen3_8b_rsft_candidates 完成 → 同上 8B CED scoring → RSFT train
- plan_016_llama_rsft_candidates_r2 完成 → LLaMA CED scoring → RSFT train
- plan_016_llama_grpo_qlora 完成 → eval（验证 QLoRA decoupling 跨家族是否复现）
- plan_014_no_evidence_eval_d076 确认结果 → 更新 scaling comparison table
- 所有 RSFT train 完成 → RSFT eval → 与 SFT baseline 对比 → 更新 paper C1 evidence
- GRPO QLoRA eval 完成 → 与 4B QLoRA decoupling 对比 → 更新 C2 cross-family evidence

### 5. 🎯 战略上下文
**核心结论链：**
- D079: 8B evidence tax ≈ 0（大模型容量足以 absorb）
- D082: LLaMA-8B evidence tax = +0.68pp ≈ 0（跨家族确认）
- D083: 1.7B evidence tax 反转 +6.2pp（小模型 evidence 起正则化作用）
- D078: CED vs flat-NLI 统计不可区分（C3 降级）
- **Paper narrative**: evidence tax 呈非线性 U-shape（小模型正则化 → 中模型负担 → 大模型中性）

**易错点：**
- RSFT candidate generation 很慢（3053 docs × N=8），预计 10-13h。不要因为"慢"就 kill 重试
- `rsft_generate` 的参数是 `--base_model` 不是 `--model_path`，`--num_generations` 不是 `--n_candidates`
- plan_014_no_evidence_eval_d076 没有 cron 注册，需要手动检查是否完成
- 4 张 GPU 全在跑，当前无空闲卡。下一批实验（RSFT scoring/train）需等 candidate generation 完成释放 GPU
- report.md 显示 GPU "空闲"是过时信息，实际全满载


---
