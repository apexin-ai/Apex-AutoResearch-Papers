# director / loop_7.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`48e47b62b3aaa1a6fcbc.json`](../../sessions/48/48e47b62b3aaa1a6fcbc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-17T16:44:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：rtx5090-4x 的 cuda:0/1/2/3，不可用其他服务器的卡
- LLaMA base_model 路径：`/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B`（注意 `meta-llama/` 子目录，之前因缺少此前缀导致 eval 崩溃，M002 记录）
- 4B RSFT gain 已修正为 **+5.5pp**（非 +6.1pp），之前 Agent 报告的 0.4655 无法从 registry 复现，Reviewer 核实最高 +5.72pp (best seed s44)，M002 已记录
- 3-parameter model loading：`--model_path=RSFT_checkpoint --base_model=原始模型 --sft_adapter=sft_output`。当 model_path 是 full model（无 adapter_config.json）时 base_model 被忽略
- CED filter 脚本参数是 `--predictions`（不是 `--predictions_path`），之前两次犯错

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (connect.bjb2.seetacloud.com)，工作目录 `/root/autodl-tmp/freige`
- 模型路径：Qwen3-1.7B `/root/autodl-tmp/models/Qwen/Qwen3-1.7B`，Qwen3-4B `/root/autodl-tmp/models/Qwen3-4B`，Qwen3-8B `/root/autodl-tmp/models/Qwen/Qwen3-8B`，LLaMA `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B`
- RSFT checkpoints：4B `rsft_output_ced_s43/checkpoint-510`，1.7B `rsft_output_qwen3_1_7b/checkpoint-1698`，8B `rsft_output_qwen3_8b/checkpoint-3393`，LLaMA `rsft_output_llama_3_1_8b_r3/checkpoint-3312`
- Seed 43 outputs：1.7B `rsft_output_qwen3_1_7b_seed43/checkpoint-1698`，LLaMA `rsft_output_llama_3_1_8b_seed43/`（training completed）
- 活跃进程（截至 handoff 时刻）：
  - cuda:0: plan_006_llama_rsft_seed43_eval_r2 (PID 463080) — LLaMA seed43 eval（刚启动）
  - cuda:1: plan_006_qwen3_8b_rsft_test (PID 460585) — 8B test predictions
  - cuda:2: plan_006_qwen3_1_7b_rsft_seed43_eval (PID 455632) — 1.7B seed43 eval (~20%)
  - cuda:3: plan_006_llama_rsft_test (PID 460159) — LLaMA test predictions

### 3. 📊 当前状态
**刚做完**：
- D094: Scaling Study 4/4 闭合（8B RSFT rel_f1=0.5606, +3.4pp）
- D095: Lead 2 RSFT→GRPO ckpt-20 结论（pipeline 可行但 +0.16pp 噪声，定位 future work）
- 4B gain +6.1pp→+5.5pp 数据修正（M002）
- Paper Agent 启动并完成 Step 2 (figures) + Step 3 文献验证（4/6 clusters done），进入 Step 4 Section Writing：experiments.tex ✅，method.tex ✅，introduction 写作中

**正在运行**：
- 4 GPU 满载（见上），预计完成：test predictions ~1-2h，1.7B eval ~1.5h，LLaMA eval ~2h
- Paper Agent：Step 4 writing（experiments/method done，intro in progress，then related_work → conclusion → limitations → abstract → appendix）
- Review Director（Group C）审稿同步进行中

**等待**：
- 4 个 GPU 任务完成的 cron 回调
- Paper Agent 后续写作进展汇报

### 4. 📋 待办（条件触发式）
- 1.7B seed43 eval 完成 → 对比 seed42 rel_f1=0.5219（±2pp 阈值判断 seed 鲁棒性）
- LLaMA seed43 eval 完成 → 对比 seed42 rel_f1=0.5674，两组 seed variance 齐全后 log decision
- 8B/LLaMA test predictions 完成 → 通知用户 CodaLab 可提交（4B s43/s44 predictions 已就绪）
- Paper Agent 完成 intro → 发文献修正（DREEAM=Ma et al. 2023，LMRC=2024，DocKS-RAG=ICML 2025，DPO=NeurIPS 2023）
- Paper Agent 报告 "建议提交审稿" → 评估是否调 submit_paper_to_review
- Seed variance > 2pp → 需增加 seed 数量或调整 claim 强度

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 Main（ARR July cycle, ~July 15-25, ~59 天）
- **核心 claims 全部有数据支撑**：C1 RSFT 有效（4/4 models），C2 decoupling spectrum（GRPO/DPO/RSFT），C3 CED≈flat-NLI（p=0.44），C4 EDCR 双层诊断（ρ=-0.96），C5 non-monotonic evidence tax
- **关键叙事点**：1.7B RSFT ign_f1 (50.50) ≈ 8B SFT ign_f1 (50.51)——RSFT 弥合 scale gap，有部署价值
- **Reviewer 已核实的完整 Scaling Study 数据**（以此为准，不用 Agent 原始报告）：1.7B +2.74pp, 4B +5.52pp, 8B +3.44pp, LLaMA +1.60pp (rel_f1)
- **易错点**：(1) evi_f1 有 TP-only (~0.80+) 和 joint (~0.37-0.44) 两个版本，论文必须标明用的是哪个 (2) DREEAM 作者是 Ma et al. 不是 Tan et al. (3) Paper Agent queue 容易堆积，发消息前检查 depth (4) fig_scaling 中 1.7B evidence tax +8.0pp（全 dev set）vs paper_framing +6.2pp（D083 fair subset），论文需说明差异来源
- **不要做的事**：不要追加 RSFT→GRPO 实验（D095 已定 future work），不要建议降级到非 A 类会议


---
