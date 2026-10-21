# agent / loop_17.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`550d0a735eddd4796c18.json`](../../sessions/55/550d0a735eddd4796c18.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-16T18:54:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0~cuda:5 on cqa1-21977，共 6 张 RTX 4090D，不可用其他服务器/卡
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...`
- 3B d000_s42 checkpoint 有命名不一致（`Qwen2.5-3B_d000_s42/` vs `_a32_`），必须 ls 确认实际路径再引用
- exp_002_signals_3B_d000_s123_cuda2 的 CRON 曾重复触发（D076 retrained checkpoint lr=5e-5 是唯一有效版本）
- 禁止在未分配 GPU 上启动实验——白名单 = cuda:0~5 on cqa1-21977

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，工作目录 `/root/contamcal-irt-calibration/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，激活用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型 checkpoints：`/root/autodl-tmp/exp001/checkpoints/` 下各 `Qwen2.5-{size}_{dosage}_{seed}/` 子目录
- Signals 输出：`/root/autodl-tmp/exp002/signals/` 下按 `{model}_{dosage}_{seed}/` 组织
- 日志：`~/runs/contamcal-irt-calibration/`（submit_training_job 写入）
- 活跃进程（reconcile_crons 确认）：
  - exp_001_eval_llama32_3B_d000_s42: cuda:4, PID 785949, cron 监控中
  - exp_001_eval_15B_instruct: cuda:5, PID 782625, cron 监控中
  - exp_006_mmlu_domain_gamma_n24_v4: CPU, PID 789935, 无 cron（Worker 2 在确认状态）

### 3. 📊 当前状态
- **刚做完**：session 初始化（read_registry + reconcile_crons + report.md + ROADMAP），修复了 signals_05B_s123_v2 过期 RUNNING 条目为 DONE/success，向 Director 汇报了 4 GPU 空闲问题
- **已派发 2 Worker**：
  1. `worker_signals_3B_s123_fill_gpus_20260516T143113`：填充 cuda:0/1/2（3B s123 d000 retry / d005 / d025 signals）+ cuda:3 任务选择
  2. `worker_analysis_rrf_aggregation_prep_20260516T143136`：盘点 signals 完整性 → 启动 RRF 聚合（CPU）→ 检查 mmlu_domain_gamma_n24_v4
- **RUNNING (registry)**：exp_001_eval_llama32_3B_d000_s42 (cuda:4), exp_001_eval_15B_instruct (cuda:5), exp_006_mmlu_domain_gamma_n24_v4 (CPU)
- **PREPARING (21)**：关键的有 exp_001_eval_3B_d000_s42_a32_aligned、exp_001_sft_3B_d000_v4/s42、exp006_pooled_rrf_irt_05b_15b_v2 等

### 4. 📋 待办
- Worker 1 回调 → 确认 cuda:0/1/2/3 已提交 → update report.md + 向 Director 汇报 6/6 GPU 满载
- Worker 2 回调 → 确认 RRF 已启动 → update registry（新 exp_003 条目）
- cuda:4 Llama eval 完成（cron 回调）→ on-experiment-done 流程 → 下一步 Llama d005 SFT 或 signals
- cuda:5 1.5B instruct eval 完成（cron 回调）→ on-experiment-done → 分配 0.5B instruct eval 或其他
- mmlu_domain_gamma_n24_v4 完成 → 分析 domain heterogeneity 是否 scale-dependent → update D108 措辞
- 3B s123 signals 全部完成 (d000+d005+d025+d100) → 全量 RRF 聚合 → pooled IRT 更新（N≥24+）
- RRF 完成 → pooled IRT fitting → 论文核心 γ_k 数字冻结 → paper draft

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25（距今 9 天），critical path = 3B s123 signals → RRF → pooled IRT → paper
- **3B s42 signals 全部完成** ✅ → RRF partial aggregation 可以先跑（0.5B + 1.5B + 3B s42），3B s123 补齐后再跑 full
- **Claim 1**（identifiability）升级为 domain-level γ（D108），N=24 MMLU domain gamma 正在 v4 重跑确认
- **Claim 2**（signal pipeline）依赖 3B signals 全覆盖
- **Claim 3**（noise propagation）sim_sweep_v7 支撑，D107 GO
- **D110**: scale-stratified IRT 为 negative，不影响主 claim（aggregate pooled IRT D109 为 success）
- **Llama-3.2-3B**（D106 scope expansion）：SFT d000 ✅, eval d000 running on cuda:4，P1 不阻塞 critical path
- **易错点**：exp_002_signals_3B_d000_s123 已失败 1 次（process dead），Worker 1 正在调查原因；不要假设 3B s123 checkpoint 路径和 s42 一样（可能无 `_a32_` 后缀）
- **PPP=0 in 4/5 MMLU domains**：paper claim 必须基于 pattern/ranking，不能基于绝对 γ 值


---
