# agent / loop_14.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`14da7d67410bc2ff8aa5.json`](../../sessions/14/14da7d67410bc2ff8aa5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-16T15:30:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-16980 cuda:0/1 + westd-21461 cuda:0/1，共 4 张，其他设备号禁用
- submit_on_allocated 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不能假设 .venv 存在
- GPU 编号脚本内始终写 `--gpu 0`（框架自动映射物理卡）
- 不加 NYT29 第三数据集（D031 决策）
- Qwen3-8B tokenizer regex warning 已确认为 transformers 4.57.6 false positive（Reviewer PASS），但 w8 DocRED 结果需注意 parse_fail_rate 偏高（Qwen DocRED ~8%）

### 2. 🖥️ 基础设施快照
- **westd-16980**: 工作目录 `/root/schema_semantic_constrained_ie`，Python `/root/miniconda3/bin/python`，conda base env
  - Qwen FT checkpoints: `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged`, `qwen_lora_docred_merged`
  - Llama FT checkpoints: `/root/autodl-tmp/checkpoints/llama3_8b_lora_scierc_merged`, `llama_lora_docred_merged`
  - 数据: SciERC `data/processed_data/test.json` (551), DocRED `data/docred/dev.json` (998)
  - 活跃: w8_llama_docred_ft_grammar_only on cuda:1（PID 未记录在 spec 中，用 CUDA_VISIBLE_DEVICES=1 手动提交，非 submit_training_job）
- **westd-21461**: 同结构工作目录，Mistral 模型在 `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3`
  - 活跃: w8_qwen_docred_ft_grammar_only PID=18555 cuda:0 (tmux), w8_qwen_docred_ft_semantic_only PID=20035 cuda:1 (tmux)
- **⚠️ 0 active crons**：3 个 RUNNING 实验无 cron 监控。已派 ops Worker `worker_ops_check_running_experiments_20260516_20260516T105323` SSH 检查进程实际状态，尚未回调

### 3. 📊 当前状态
Session #14 刚完成 session-start 初始化。已向 Director 汇报。

**RUNNING (3)**:
- `w8_qwen_docred_ft_grammar_only` — westd-21461:cuda:0, PID=18555, since 09:13 UTC
- `w8_qwen_docred_ft_semantic_only` — westd-21461:cuda:1, PID=20035, since 10:08 UTC
- `w8_llama_docred_ft_grammar_only` — westd-16980:cuda:1, since 06:34 UTC（无 PID 记录）

**PREPARING (1)**:
- `w8_llama_docred_ft_semantic_only` — 已创建 registry 条目，DocRED FT ablation 第 4 格。命令模板已知（参照 w8_qwen_docred_ft_semantic_only spec，改 model_path 为 llama_lora_docred_merged，改 output_path）。目标 GPU: westd-16980:cuda:0（空闲）

**等待回调**:
- ops Worker（进程状态检查）— 确认 3 个 RUNNING 实验实际在跑 + 空闲 GPU
- analysis Worker `worker_analysis_ft_ablation_summary_20260516_20260516T105606` — 整理 FT ablation 结果表

**关键进展（本 session 之前已完成）**:
- SciERC FT ablation 4 格全部完成（w7 系列）
- Composability 4 格全部完成（w5 系列）
- Mistral 3rd model SciERC+DocRED 全部完成（w6 系列）
- FT + ZS post-hoc baseline 完成（w8_ft_posthoc_baseline）
- 总计: 49 DONE (44 success / 1 negative / 4 killed) + 3 RUNNING + 1 PREPARING

### 4. 📋 待办（条件触发式）
- ops Worker 回调到达 → 读诊断结果 → 为 3 个 RUNNING 实验注册 crons → 确认 westd-16980:cuda:0 空闲 → 提交 w8_llama_docred_ft_semantic_only
- w8_llama_docred_ft_grammar_only 完成 → 分析结果 → 与 SciERC 模式对比（预期 grammar_only DR≈0.49% = unconstrained，不降）
- w8_qwen_docred_ft_grammar_only 完成 → 分析（预期 DR≈0.76%，grammar 不约束 DR）
- w8_qwen_docred_ft_semantic_only 完成 → 分析（预期 DR 从 0.76% 降至 ~0.3-0.5%）
- w8_llama_docred_ft_semantic_only 完成 → DocRED FT ablation 全部完成 → 汇总 2 模型 ×2 数据集 ×4 模式 ablation 表 → 汇报 Director
- 全部 w8 完成 → 排 latency profiling（Dream 审稿要求）→ 论文写作
- analysis Worker 回调 → 审查 ablation 分析质量 → 注册 artifact

### 5. 🎯 战略上下文
- **核心论点**: OntoCoDec 两层约束解码（grammar + semantic）自动编译 ontology schema 为 token constraints，消除 LLM IE 的 schema violations
- **投稿目标**: EMNLP 2026 ARR May 25（9 天后）
- **ablation 核心结论已确立**: grammar 层消除 RV/ET（→0%），semantic 层消除 DR（降 42-68%），两层互补缺一不可。FT regime 下 DR 残留 0.49-1.95%，full OntoCoDec 进一步降至 0-0.2%
- **post-hoc baseline 结论**: ZS 下 post-hoc F1 ≥ constrained F1（5/6 组），但极端 rejection 时（Mistral DocRED 73.7%）R_F1 反降。Constrained decoding ZS 价值在于"生成时 0% violations + composability"，不在 F1 保留
- **Mistral DocRED 残余 DR=33.2%**: 远高于 Qwen/Llama（10-13%），原因是 semantic constraint 未覆盖的 domain-range 组合。这不是 negative——是"复杂 schema 下 semantic 层覆盖度的上限"
- **易踩坑**:
  - w8_llama_docred_ft_grammar_only 是手动提交（非 submit_training_job），没有 PID 记录，没有 cron。下一个"你"必须先确认它的实际状态再做任何假设
  - westd-16980:cuda:0 理论上空闲但未经 SSH 验证。提交前必须确认
  - w8 系列是 eval-only（用已有 FT checkpoint），运行时间应为 1-6h（DocRED 998 samples），如果超长大概率是 bug


---
