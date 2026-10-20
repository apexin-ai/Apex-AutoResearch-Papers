# reviewer / loop_3.md

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`37309292d1a790a3634b.json`](../../sessions/37/37309292d1a790a3634b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-23T20:11:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-32570:0-3 + westd-19912:0-3，共 8 张。TP=4 推理用 westd-32570 全部 4 卡，合规。
- Llama-70B 模型路径是 symlink：`/root/autodl-tmp/models/Llama-3.1-70B-Instruct` → `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-70B-Instruct`。不要删 symlink target。
- 推理脚本有空文件跳过 bug：`if Path(output_path).exists(): skip`，不检查行数。如果推理失败留下空文件，下次重跑会跳过。务必删空文件再重跑。
- EMNLP 2026 DDL 5/25，Abstract ≤200 words，main text ≤8 pages，Limitations 在正文不在 appendix。

### 2. 🖥️ 基础设施快照
- 服务器：westd-32570（主）+ westd-19912（备），工作目录 `/root/nlp_variance_gtheory`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- Llama-70B：`/root/autodl-tmp/models/Llama-3.1-70B-Instruct`（128GB safetensors, 30 shards）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 磁盘：westd-32570 148/350GB used（213GB free）
- 活跃进程：无推理/训练进程运行，4 GPU 全部空闲
- 本地论文：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/`
- Llama-70B MMLU 产出：`/root/nlp_variance_gtheory/data/exp_llama70b/llama70b_mmlu.jsonl`（57,600 行）
- G-study 结果：`/root/nlp_variance_gtheory/data/exp_llama70b/llama70b_mmlu_gstudy.json`

### 3. 📊 当前状态
**阶段**：论文定稿完成，等待匿名 repo 最终推送 + ARR 提交。

我刚完成的审查：
- Llama-70B MMLU 推理完整性（57,600 records ✓）+ Henderson G-study 验算（G_item=0.9566 ✓）
- 全量数据正确性审计（105 项，102 PASS，2 已修复，1 UNVERIFIED: §4.1 text-exact-match 79.7% 无源 JSON）
- 论文修复验证：Table 1 温度注释、CI 标注、硬编码章节号、术语统一、BibTeX key——全部确认
- Reference 审计、caption 一致性、拼写语法——全部 PASS
- ROADMAP 审查——方向有数据支撑，无 GPU 缺口，DDL 可行
- 服务器审计 + 76 个分析 JSON 本地备份

Registry：`exp_llama70b_mmlu` 仍为 PREPARING（Agent 未更新为 DONE），其余实验全 DONE 或 killed。

### 4. 📋 待办
- 匿名 repo 推送完成通知 → 核查 repo 不含服务器路径/作者信息/API key
- ARR 提交前 → 最终确认 Abstract ≤200 words（当前 155 ✓）、main text ≤8 pages（当前 8 ✓）
- 如果 Agent 更新 registry exp_llama70b_mmlu → 核实 conclusion/metrics 与 G-study JSON 一致
- 如果 Director 要求跑剩余 4 benchmarks（GSM8K/ARC/HellaSwag/MATH）→ 提醒先删之前的空/部分文件，监控空文件跳过 bug
- §4.1 text-exact-match 79.7% → 如果 Agent 被要求溯源，源头可能在 `worker_analysis_dual_metric_deep_20260520T215443` 或服务器 `/root/nlp_variance_gtheory/results/analysis/` 中的早期分析

### 5. 🎯 战略上下文
- **核心结论**：G-theory 方差分解显示 item difficulty 主导 LLM 评测方差（MC 68-72%，FF 31-41%），D-study 3×3 设计（178 items）比 single-condition（552 items）节省 3.1× items，G≥0.80。
- **Llama-70B 验证**（D029）：item_id=74.5%, G_item=0.957，core structure 跨架构一致，但 seed:item 敏感性高于 Qwen-72B（5.0% vs 0.93%）——"部分一致"结论是诚实的，不要改成"完全一致"。
- **易错点 1**：Table 3 的 prompt† 行之前有系统性错误（10 cells），已修复并验证。如果有人再改 Table 3，必须重新对照 `bootstrap_ci_*.json` 源数据。
- **易错点 2**：per_benchmark_gstudy_hellaswag.json（服务器）用 3 温度（691,200 records），bootstrap_ci_hellaswag.json 用 2 温度（460,800 records），论文用后者。不要混淆。
- **评分轨迹**：R5(3.5)→R6(3.0)→R7(3.5)→R8(3.5)→R9(3.5)→R10(3.5)，目标 4.0 Conference。


---
