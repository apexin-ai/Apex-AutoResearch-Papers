# reviewer / loop_7.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`3ad8f901ce511c548e79.json`](../../sessions/3a/3ad8f901ce511c548e79.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-16T11:08:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-11235 的 cuda:0 和 cuda:1，越界立即 CRITICAL
- ae_only_seed123/seed456 的 registry 曾被监控系统误标为 failed（"process dead 5× with no sentinel/W&B"），实际成功。已修复为 success。如果再出现类似误判，先检查 eval_results.json 再信 registry
- deepseek_full_trace 在 cluster_robust_ci.json 中曾有 v1（10.59%）残留，已修复为 v3（79.16%）。论文引用必须确认指向 v3 数据
- 论文中 "≥99.8%" claim 出现在 discussion.tex 和 conclusion.tex 两处，ae_only seed123=99.08% 违反此阈值，必须改为 "≥99%" 或类似表述

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (root)，代码根目录 /root/trace-verdict-study
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型路径：
  - Qwen-7B: /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct
  - Qwen-1.5B: /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct（symlink→ModelScope）
  - DeepSeek-6.7B: /root/autodl-tmp/models/deepseek-coder-6.7b-instruct
  - CodeLlama-13B: /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf（3 shards 完整，24.4GB）
- 数据：/root/autodl-tmp/trace-verdict-study-data/
- Checkpoints：/root/autodl-tmp/trace-verdict-study-checkpoints/
- HF_HOME：/root/autodl-tmp/.hf_cache
- W&B project：trace-verdict-study
- 论文：/root/trace-verdict-study/docs/paper/*.tex
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/

### 3. 📊 当前状态
刚完成 qwen15b_vota_seed42 审查（99.58%）。1.5B 多规模验证 3/4 条件完成（exception_only=99.83%, VOTA=99.58%, no_trace=67.31%），等 full_trace。

Registry 活跃实验（截至 handoff）：
- qwen15b_full_trace_seed42: 应在运行中，最后一个 1.5B 条件
- codellama13b_exception_only/vota/no_trace_seed42: QUEUED，模型已下载完整可启动
- exception_only_nomarker_seed42/123/456: PREPARING（Task G format marker ablation）
- loop_only_seed123/456: QUEUED（Task H seed robustness）
- label_only_seed123: DONE (87.06%), label_only_seed456: 刚完成 (85.88%)，Agent 可能还在 ANALYZING

总数 ~63 实验，DONE ~48。

### 4. 📋 待办（条件触发式）
- qwen15b_full_trace on_complete → 验证 eval_results.json，完成 1.5B 四条件全景表，发 Director
- codellama13b_* 开始运行 → GPU 合规检查（必须在 cuda:0/1），核对模型加载是否正常（13B 首次训练）
- exception_only_nomarker 实验完成 → 关键审查：对比有/无 format marker 的 accuracy 差异，直接回应 C1 reviewer concern（B5=99.33% 靠 marker，SFT 去掉 marker 后还能多高？）
- loop_only seed123/456 完成 → 计算 3-seed mean 和 σ，验证 Tier 2 (85.63%) 稳定性
- 任何论文修改 worker 完成 → 检查 "≥99.8%" 是否已改为 "≥99%"，ae_only 是否更新为 3-seed mean (99.64%)
- conclusion.tex 修改 → 确认 DebugBench 不再出现在 future work（此 bug 已修复但需持续监控）

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 Main（ARR May 25 deadline，~9 天）
- 核心发现：exception events 单独达 99.83%，是 verdict prediction 最有效组件。Two-tier hierarchy: Tier 1 (exception/ae) ≥99% >> Tier 2 (loop) ~86%
- 1.5B 实验揭示最强新证据：Tier 1 scale-invariant（1.5B=7B=99.83%），no_trace scale-sensitive（-7.82pp）→ task is signal-limited not capacity-limited
- ae_only 3-seed 数据改变了排序：exception_only (99.83%±0) > ae_only (99.64%±0.49)。论文 Table 2 和 "≥99.8%" claim 需同步更新
- DeepSeek 有两个已知 confound：(1) tokenizer 导致 VOTA 91.7% 样本被截断；(2) seed123 LoRA outlier (91.09%)。论文已诚实讨论
- 易踩坑：监控系统的 on_failed cron 会误判已完成但无 W&B sentinel 的实验——先查 eval_results.json 再信 registry 状态
- 本地 artifacts/analysis/cluster_robust_ci.json 是旧版（12 条件），服务器端是新版。引用数据以服务器端为准


---
