# agent / loop_11.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`512c47aeaa4aef76263e.json`](../../sessions/51/512c47aeaa4aef76263e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-16T00:10:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 rtx5090-4x 的 cuda:0/1/2/3，bjb2-12179 是备用服务器但当前无 GPU 分配
- **--sft_adapter 必须传**：D064 教训，所有 eval 命令必须带 `--sft_adapter /root/autodl-tmp/sft_output`，否则 rel_f1 崩到 0.002 级别（已因此 kill 重跑 3 个实验）
- **EDCR by-construction 混淆**（D071）：方法级 EDCR ≈ f(1/rel_f1)，论文中不能声称 EDCR 独立于 rel_f1，只能在 per-relation 级声称独立于 evi_f1
- **CED 补种受阻**：rsft_ced_s43_train FAILED (EXIT_CODE=1)，rsft_ced_s45_train KILLED——paired t-test 需要 matched pairs，目前 CED 只有 s42/s44 两个 3ep seeds，不够做统计检验。下一个"你"需要先诊断 s43 失败原因再重跑
- eval 必须加 `--no-quantize`（inference 不做量化，与训练时一致）

### 2. 🖥️ 基础设施快照
- **服务器**: rtx5090-4x（4× RTX 5090 32GB）
- **工作目录**: `/root/autodl-tmp/freige`（代码仓库）
- **Python**: `/root/miniconda3/bin/python`，conda base 环境（不是 venv）
- **激活命令**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型**: `/root/autodl-tmp/models/Qwen3-4B`（base model），SFT adapter `/root/autodl-tmp/sft_output`
- **RSFT checkpoints**: `/root/autodl-tmp/rsft_output_flat_nli_s{42,43,44,45}/`（flat-NLI），`/root/autodl-tmp/rsft_output_s{42,44}/`（CED）
- **数据**: `/root/autodl-tmp/data/docred`，RSFT 训练数据 `/root/autodl-tmp/rsft_filtered/rsft_train.jsonl`（2718 samples）
- **HF cache**: `/root/autodl-tmp/.hf_cache`（必须设 HF_HOME + HF_HUB_OFFLINE=1）
- **Eval 产出**: `/root/autodl-tmp/eval_results/`
- **Logs**: `~/runs/faith-evidence-ie/*.log`
- **活跃进程**:
  - eval_flat_nli_s44: PID 270462, cuda:0
  - reeval_rsft_topk3: PID 268485, cuda:2
  - eval_flat_nli_seed45: PID 272164, cuda:3
- **活跃 Crons**: 3 个（分别监控上述 3 个 RUNNING 实验）
- **活跃 Worker**: 1 个（worker_analysis_ced_s43_directory_check，在跑 CED s43 目录检查）

### 3. 📊 当前状态
**刚做完**: reeval_flat_nli_s43 成功（D064 bug fix 重跑），plan_003_edcr_diagnostic 成功（EDCR 双层诊断完成）。rsft_ced_s43_train 失败、rsft_ced_s45_train 被 kill——CED 补种受阻。

**RUNNING (3)**:
| exp_id | GPU | 目的 |
|--------|-----|------|
| eval_flat_nli_s44 | cuda:0 | flat-NLI s44 全量 dev eval（C3 统计数据点）|
| reeval_rsft_topk3 | cuda:2 | RSFT top_k=3 重跑 eval（D064 fix，对比 top_k=1）|
| eval_flat_nli_seed45 | cuda:3 | flat-NLI s45 全量 dev eval（C3 统计数据点）|

**QUEUED (1)**: eval_plan_014_no_evidence（SFT-no-evidence dev eval，等 GPU 空闲）

**空闲 GPU**: cuda:1 分配了没跑——这是失职状态，需要立即安排任务（CED 补种诊断/重跑 或 eval_plan_014_no_evidence）

**等待中**:
- 3 个 RUNNING 实验的 cron 回调
- worker_analysis_ced_s43_directory_check 的 Worker 回调（检查 CED s43 训练失败原因）

### 4. 📋 待办（条件触发式）
- **eval_flat_nli_s44 完成** → 记录 rel_f1，与 s42(0.4539)/s43(待确认)/s45(中间 0.4876) 对比
- **eval_flat_nli_seed45 完成** → 记录 rel_f1，flat-NLI 4-seed 收齐后运行 `/root/autodl-tmp/scripts/seed_comparison.py` 做 CED vs flat-NLI paired t-test
- **reeval_rsft_topk3 完成** → 对比 top_k=1 (rel_f1≈0.46) 和 SFT baseline (0.4057)，决定 top_k=3 是否写入论文
- **CED s43 Worker 回调** → 诊断失败原因，修复后在 cuda:1 重跑 rsft_ced_s43_train
- **cuda:1 立即** → 要么提交 eval_plan_014_no_evidence，要么诊断+重跑 CED s43 训练——不能空着
- **flat-NLI 4-seed + CED 4-seed 全齐** → 跑 paired t-test，结果决定 C3 是否完全降级：p<0.05 保留 CED 优势声称，p≥0.05 则 CED 降级为 "one possible scoring function"
- **所有 eval 收齐** → 提交 plan_002 test set eval（D057 之前失败需重试）
- **plan_003 EDCR diagnostic** → 已完成数据分析，需要写入论文 Results section

### 5. 🎯 战略上下文
**项目**: FREIGE — LLM evidence-grounded DocRE 系统性研究，目标 EMNLP 2026 Main (ARR July, ~7月15-25)

**4 个 Core Claims**:
1. Evidence-grounded DocRE 可行（evidence tax ~8pp，CED reranker 恢复 97%）✅ 数据充足
2. RL optimization pressure ∝ decoupling severity（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）✅ 数据充足
3. NLI-based scoring 提升 RSFT（CED vs flat-NLI 统计不显著，已降级）⚠️ 等 4-seed 结果
4. EDCR 双层诊断（方法级 + per-relation）✅ plan_003 完成

**关键决策链**: D064（--sft_adapter bug）→ D065/D066（decoupling 是 QLoRA-specific）→ D067/D068/D069（DPO 中性，decoupling spectrum 修正）→ D070/D071/D072/D073（EDCR 双层诊断定位 + 定义规范）

**最容易判断错的事**:
- 不要把 GRPO bf16 baseline ckpt-100 (rel_f1=0.4549) 当成 GRPO 训练结果——那是训练前起点，实际 GRPO bf16 训练后 ~0.434
- CED 补种是 **paired t-test 的硬依赖**——没有 CED s43/s45 seeds，C3 的统计检验做不了。当前 CED 只有 s42/s44，flat-NLI 将有 s42-s45 四个
- eval_plan_014_no_evidence 其实已经跑过一次成功（rel_f1=0.4893），QUEUED 的这个可能是重跑或者遗留——先查 registry 确认再决定是否还要跑
- cuda:1 空闲是当前最紧急的资源浪费，必须立即填上


---
