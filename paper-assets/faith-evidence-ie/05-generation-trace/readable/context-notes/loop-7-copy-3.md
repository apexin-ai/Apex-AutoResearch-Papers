# reviewer / loop_7.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`1d9a430433fcff8cba87.json`](../../sessions/1d/1d9a430433fcff8cba87.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T14:33:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目 GPU 白名单：rtx5090-4x 的 cuda:0-3 全部可用，但必须核对实际 CUDA_VISIBLE_DEVICES 与 registry GPU 字段一致（本 session 已发生 3 次 registry 标 cuda:2 实际跑 cuda:0 的事故）
- DREEAM baseline 必须在 cuda:2 运行（刚完成迁移，PID 213006 确认在 cuda:2）
- submit_training_job 的 GPU 参数传递有 bug：注册 cuda:2 但命令里写 CUDA_VISIBLE_DEVICES=0——每次新实验提交后必须用 `/proc/&lt;PID>/environ` 核实实际 GPU
- registry 更新不可信：本 session 多次出现 DONE 实验仍标 RUNNING、RUNNING 实验仍标 QUEUED、metrics 被覆盖等问题——每次审查必须独立读服务器验证

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root)，4× RTX 5090 32GB；bjb2-12179 (root) 备用
- 代码根目录：`/root/autodl-tmp/freige`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型：`/root/autodl-tmp/models/Qwen3-4B`，SFT adapter `/root/autodl-tmp/sft_output`
- 数据集：`/root/autodl-tmp/data/docred`（train_annotated/dev/test）
- HF cache：`/root/autodl-tmp/.hf_cache`
- GRPO G=8 checkpoint：`/root/autodl-tmp/grpo_ced_g8_bf16/`（已完成，含 checkpoint-10 到 checkpoint-100）
- DREEAM baseline：`/root/autodl-tmp/baselines/dreeam/`（evaluation.py 4 处 `!= []` bug 已全部修复为 `len(...) > 0`）
- RSFT 数据集：topk3 `/root/autodl-tmp/rsft_filtered_topk3/`(8037), CED-filtered `/root/autodl-tmp/rsft_filtered_topk3_ced_filtered/`(7942), random `/root/autodl-tmp/rsft_filtered_topk3_random/`(8037)
- flat-NLI 输出：`/root/autodl-tmp/rsft_filtered_flat_nli/`（仍空，进程运行中）

### 3. 📊 当前状态
**活跃进程**：
| GPU | PID | 实验 | 进度 | 预计完成 |
|-----|-----|------|------|---------|
| cuda:0 | 178055 | CED reranker scoring | 498/985 (50%) | ~30 min |
| cuda:1 | 197386 | maxtok1536_r2 eval | 92/124 (74%) | ~40 min |
| cuda:2 | 213006 | DREEAM teacher training | epoch 0/30 (刚重启) | ~1.8h |
| cuda:3 | 208155 | flat-NLI scoring | 运行中(35min)，无进度条 | ~2h? |

**Registry RUNNING**：plan_004_dreeam_baseline, plan_011_grpo_g8_bf16（实际已完成！）, mvp2_eval_rsft_r2b_maxtok1536_r2, mvp2_ced_reranker_poc

**已发送但未解决**：
- plan_011_grpo_g8_bf16 registry 仍标 RUNNING（实际 22:09:52 UTC+8 完成，EXIT_CODE=0），需 Agent 更新为 DONE + 跑 dev eval
- plan_004 registry status 已改为 RUNNING（14:32 更新）✓

### 4. 📋 待办（条件触发式）
- **GRPO G=8 eval 完成** → 审查 dev set rel_f1/evi_f1_joint/EDCR，对比 SFT baseline。重点：是否出现 catastrophic forgetting（rel_f1 崩塌）？三变量混淆（bf16+kl_coef=0.01+G=8）无法归因，若结果好需建议 controlled ablation
- **maxtok1536_r2 完成** → 审查 EDCR 是否从 0.6609 改善。如显著改善→截断是真因；如不变→distractor citation 是 RSFT 行为
- **CED reranker 完成** → 审查 rel_f1 是否 > 0.4057 (SFT greedy)。如是→CED reranker 有价值；审查 oracle reranker 上界
- **flat-NLI scoring 完成** → 验证输出样本数和质量指标（mean_f1/mean_ced）vs CED topk1，确保 C3 ablation 公平性
- **DREEAM teacher 完成** → 审查 dev set evi_f1（应达 ~50+ joint），对比 FREIGE 的 evi_f1_joint=0.3711
- **plan_008 random baseline RSFT 训练启动** → 审查 per-doc 分布混淆：random 是全池随机抽样（非 per-doc balanced），若 topk3 vs random 差异显著需追加 doc-balanced random

### 5. 🎯 战略上下文
- **项目**：FREIGE — 用 CED 作为离线质量信号，通过 RSFT 训练 Qwen3-4B 做 document-level RE (DocRED)
- **目标**：EMNLP 2026 Main (ARR July cycle)
- **Dream v1 reframe (D044)**：CED 降级为"一种可能的 scoring function"；4 Core Claims：C1=feasibility, C2=GRPO decoupling, C3=NLI ablation, C4=EDCR
- **Publishability gates**：RSFT > SFT on test + DREEAM Evi-F1 对标 + GRPO G=8 decoupling 复现
- **s43_r2 registry 事故**（已修复）：joint backfill 覆盖了原始 metrics + delta 算错（用 conditional 当 baseline 而非 joint baseline），escalate 4 次才修
- **最易判断错的事**：(1) 不要把 conditional evi_f1 (~82%) 和 joint evi_f1 (~37%) 混淆——评估协议完全不同；(2) GRPO G=8 训练 reward 不等于 eval metrics，必须等 dev eval 才能判断 C2；(3) registry 数据经常不可信（metrics 被覆盖、GPU 错标、status 不更新），始终独立验证；(4) DREEAM evaluation.py 已修好但如果 Agent 更新代码可能覆盖——新 epoch eval 时注意 crash 信号


---
