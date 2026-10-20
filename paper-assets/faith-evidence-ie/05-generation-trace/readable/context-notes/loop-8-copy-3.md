# reviewer / loop_8.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`3d03a8f585ba67c937c4.json`](../../sessions/3d/3d03a8f585ba67c937c4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T18:39:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配：rtx5090-4x 的 cuda:0/1/2/3 全部属于本项目，但必须核对每个实验 spec 中 CUDA_VISIBLE_DEVICES 与 registry gpu 字段一致
- plan_014 registry spec 标注 model_name 为 "QLoRA 4-bit" 但实际 adapter_config.json 显示标准 LoRA (use_qalora=false)——元数据不准，对比 SFT baseline 时需确认 baseline 也是相同 LoRA 配置，否则单变量控制不成立
- eval_plan_014_sft_no_evidence 有 298/985 (30.3%) truncated at max_new_tokens=1024，rel_f1=0.4893 是下限而非真值——论文引用此数字时必须注明 truncation caveat

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root) + bjb2-12179 (root)
- 代码根目录：/root/autodl-tmp/freige
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：/root/autodl-tmp/models/Qwen3-4B
- SFT baseline adapter：/root/autodl-tmp/sft_output（推测，需确认）
- SFT-no-evidence adapter：/root/autodl-tmp/sft_no_evidence_output（LoRA r=64, alpha=128, bf16）
- 数据集：/root/autodl-tmp/data/docred
- HF cache：/root/autodl-tmp/.hf_cache
- 活跃进程（截至 handoff）：plan_008_rsft_topk3 (PID 234489, cuda:3, RUNNING)；cuda:0/1/2 空闲

### 3. 📊 当前状态
刚完成 eval_plan_014_sft_no_evidence 审查并 post 给 Director。核心结论：
- rel_f1=0.4893（项目最高），evidence generation cost = 8.36pp
- CED-reranker (0.4864) 几乎消除 evidence 代价同时保有 evi_f1=0.8188——论文亮点
- eval registry 仍 ANALYZING，Worker done 但未补录 metrics，需 Agent 补全

Registry 活跃状态：
- plan_008_rsft_topk3: RUNNING (cuda:3, top_k=3 CED RSFT ablation)
- plan_012_dpo_ced: ANALYZING（DPO 训练已完成，等分析）
- plan_001_flat_nli_seed43: QUEUED
- eval_plan_014_sft_no_evidence: ANALYZING（eval 完成但 registry 未更新）

### 4. 📋 待办
- plan_008_rsft_topk3 完成 → 审查 top_k=3 vs top_k=1 RSFT 对比，关注 sample 数量差异对 rel_f1 的影响
- plan_012_dpo_ced 分析结果出来 → 重点审查：DPO 是否避免 GRPO 的 catastrophic forgetting（Claim 2 关键数据点，Dream v2 三档要求）
- Agent 补录 eval_plan_014 metrics 后 → 确认 registry 数据与日志一致
- 如 Director 要求 max_new_tokens=2048 复跑 plan_014 eval → 审查新结果与 1024 的差异

### 5. 🎯 战略上下文
项目处于 Research 阶段后期，核心实验矩阵正在补全。关键决策链：
- GRPO catastrophic forgetting 在 bf16 G=8 下**不复现**（rel_f1=0.4549 > SFT baseline）→ decoupling 是 QLoRA-specific，Claim 2 需 re-scope 为 "QLoRA GRPO fails" 而非 "online RL fails"
- flat-NLI vs CED RSFT 差异 <1pp (0.4539 vs 0.4596)，CED contrastive margin 增益不显著 → Claim 3 (CED 优势) 弱化
- DPO (plan_012) 是 RL spectrum 最后一个关键数据点——如 DPO 也 fail → 支撑 "structured IE + RL 困难" narrative；如 DPO work → 仅 on-policy (GRPO) 特有问题

**最容易判错的事**：
1. GRPO bf16 G=8 rel_f1=0.4549 不是"GRPO 成功"——它是 SFT merged 基础上训 100 步 GRPO，与 QLoRA GRPO 从零训完全不同。对比时注意训练起点和步数差异
2. SFT-no-evidence 的 0.4893 是 truncated 下限，不要直接用来算精确的 "evidence generation = X pp"——论文需注明
3. CED-reranker 的 0.4864 用了 8x 生成（20872s inference），与 single-pass 方法不可直接比推理效率


---
