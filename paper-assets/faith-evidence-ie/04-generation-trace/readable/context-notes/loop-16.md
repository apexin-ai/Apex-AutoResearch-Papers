# agent / loop_16.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`05ff554be4b25af7cefa.json`](../../sessions/05/05ff554be4b25af7cefa.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-17T23:20:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx5090-4x 的 cuda:0/1/2/3（4× RTX 5090）。无其他服务器。
- LLaMA base_model 路径必须是 `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B`（注意 `meta-llama/` 子目录），之前用 `/root/autodl-tmp/models/Meta-Llama-3.1-8B` 导致 eval 崩溃。
- RSFT eval 三层加载：base_model → merge SFT adapter → load RSFT LoRA。1.7B/8B Qwen 和 LLaMA 的 SFT adapter 路径不同，不可混用。
- 论文术语统一：EDCR = "Evidence-Decoupling Ratio"，禁止用 "Evidence-Distractor Citation Ratio" 或 "Distractor Citation Rate"。已因此修过两次图。

### 2. 🖥️ 基础设施快照
- **服务器**：rtx5090-4x，工作目录 `/root/autodl-tmp`，代码 `/root/autodl-tmp/freige`
- **Python**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **HF cache**：`HF_HOME=/root/autodl-tmp/.hf_cache`，离线模式 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`
- **模型路径**：
  - Qwen3-1.7B: `/root/autodl-tmp/models/Qwen/Qwen3-1.7B`，SFT: `sft_output_qwen3_1_7b_bf16`，RSFT: `rsft_output_qwen3_1_7b/checkpoint-1698`
  - Qwen3-4B: `/root/autodl-tmp/models/Qwen3-4B`，SFT: `sft_output`，RSFT: `rsft_output_ced_s43/checkpoint-510`
  - Qwen3-8B: `/root/autodl-tmp/models/Qwen3-8B`（注意无 Qwen/ 前缀），SFT: `sft_output_qwen3_8b_bf16`，RSFT: `rsft_output_qwen3_8b/checkpoint-3393`
  - LLaMA-8B: `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B`，SFT: `sft_output_llama_3_1_8b`，RSFT: `rsft_output_llama_3_1_8b_r3/checkpoint-3312`
- **数据**：DocRED `/root/autodl-tmp/data/docred`，Re-DocRED `/root/autodl-tmp/data/re-docred`
- **活跃进程**：无。全部 GPU 空闲，无 cron，无 running worker。
- **论文目录**：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/`
- **图表目录**：`artifacts/` 和 `figures/paper/`（两处均有副本）

### 3. 📊 当前状态
**刚做完**：Registry 最终清理——将 4 个 ANALYZING 实验推进到 DONE/success，2 个 PREPARING 过期条目推进到 killed。正在等 Director 确认 LaTeX 编译检查任务（尚未派 Worker）。

**Registry 状态**：0 个 RUNNING，2 个 QUEUED（过期条目正在清理中：`plan006_1_7b_rsft_eval` 和 `seed_comparison_prep`，均 conclusion=killed，需继续推到 DONE）。其余全部 DONE。

**论文写作进度**：所有章节草稿已完成（abstract, introduction, method, experiments, related_work, analysis, conclusion, limitations, appendix）。references.bib 有 20 条。5 张图已生成（fig_spectrum, fig_scaling, fig_overview, fig_grpo_dynamics, fig_edcr_relations）。Round 3 审查通过 7/10。

**CodaLab test predictions**：4/4 模型全部就绪，等用户手动提交：
- 4B: `/root/autodl-tmp/eval_results/` 下已有（s43+s44）
- 1.7B: `plan_006_qwen3_1_7b_rsft_test/codalab_submission.json`
- 8B: `plan_006_qwen3_8b_rsft_test/codalab_submission.json`
- LLaMA: `plan_006_llama_rsft_test/codalab_submission.json`

### 4. 📋 待办
- Registry 清理未完成 → `plan006_1_7b_rsft_eval` 和 `seed_comparison_prep` 仍在 QUEUED/conclusion=killed，需步进到 RUNNING → DONE
- Director 要求 LaTeX 编译检查 → 派 Worker 编译论文，确认 0 errors/0 undefined refs，报告总页数
- Director 要求确认 `figures/paper/` 下图表是术语修正后的最新版 → 派 Worker 检查 fig_grpo_dynamics.pdf 和 fig_edcr_relations.pdf 中无 "Distractor Citation"
- experiments.tex Table 3 有 SFT evi_f1 数据可填（1.7B SFT: 83.16/39.58, 8B SFT: 81.88/41.39）→ 等 Director 确认是否需要 Worker 填入
- CodaLab 提交后如拿到 test F1 → 更新 experiments.tex 中 TBD 占位符

### 5. 🎯 战略上下文
**核心结论**：FREIGE 证明 LLM-based DocRE 可以同时生成 relations 和 evidence，关键发现：
1. **Decoupling spectrum**：GRPO QLoRA 导致 catastrophic decoupling（EDCR→1.0），bf16 温和，DPO 渐进退化，RSFT 无 decoupling
2. **Evidence tax 非单调**：1.7B 受益（+6.2pp），4B 受损（-7.9pp），8B 吸收（≈0）
3. **RSFT+CED 全尺度有效**：1.7B→4B→8B→LLaMA 全部 +1.6~+6.1pp over SFT
4. **种子稳定**：1.7B Δ=0.39pp，LLaMA Δ=0.55pp

**易错点**：
- evi_f1 有两个版本：TP-only（~0.80，膨胀）和 joint/DREEAM（~0.37-0.44，真实）。论文中与 DREEAM 54.01% 对比必须用 evi_f1_joint
- 8B no-evidence eval 的 metrics.json 中 `base_model` 字段记录了传入的 args，但代码实际上忽略了它（当 model_path 无 adapter_config.json 时直接用 model_path 作为 base）
- post_hoc_bm25_baseline 证明 joint generation EDCR 优于 post-hoc 11.2pp，但 evi_f1_joint 差距小——论文中 claim 要精确


---
