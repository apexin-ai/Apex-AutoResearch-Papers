# agent / loop_15.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`9108698fa63c84ced5eb.json`](../../sessions/91/9108698fa63c84ced5eb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-16T21:04:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-23072 cuda:0/1, westd-11672 cuda:0/1/2/3（共 6 张）
- submit_training_job 注入 CUDA_VISIBLE_DEVICES 映射，脚本内 `--gpu` 始终从 0 开始
- sft_standard_25_westd 用了 `--gpu 1` 但 CUDA_VISIBLE_DEVICES=1 → 实际访问不到设备，这是本次失败的疑似根因，重试时改 `--gpu 0`
- Qwen Math calibration=256（不同于 westb 的 512），论文加 footnote 不重跑（D046）
- 磁盘：根分区小，模型/数据/cache 全部放 `/root/autodl-tmp/`，HF_HOME/HF_DATASETS_CACHE 必须重定向

### 2. 🖥️ 基础设施快照
- **westb-23072**: 2× ~98GB GPU | conda base `/root/miniconda3/bin/python` | 工作目录 `/root/recovery_aware_struct_prune` | 模型/数据 `/root/autodl-tmp/recovery_aware_struct_prune/`
- **westd-11672**: 4× ~95GB GPU | 同上 conda base | 同上路径结构
- W&B project: recovery_aware_struct_prune（多个 run_id 散落在 registry）
- HF_HOME: `/root/autodl-tmp/.hf_cache`
- 活跃进程（reconcile 确认）:
  - eval_sft_rasp_25: westb-23072 cuda:0, PID 602990
  - eval_sft_rasp_rlvr_20: westb-23072 cuda:1, PID 625453
  - grpo_rasp_25: westd-11672 cuda:0, PID 21408
  - eval_grpo_standard_25_qwen_math / eval_pass_k8_unpruned_qwen_math: westd-11672 cuda:1（无 PID/cron，可能是手动提交）
  - eval_pass_k8_rasp_20_sft_qwen_math: westd-11672 cuda:2
  - eval_pass_k8_rasp_20_grpo_qwen_math: westd-11672 cuda:3

### 3. 📊 当前状态
**刚发生**：sft_standard_25_westd 失败（process dead 5×, no W&B/sentinel）。已派 Worker `worker_diagnose_sft_standard_25_westd_20260516T164827` SSH 查日志诊断根因，**尚未回调**。

**RUNNING (7)**:
- eval_sft_rasp_25 — 25% RASP post-SFT GSM8K eval
- eval_sft_rasp_rlvr_20 — RLVR 20% eval
- grpo_rasp_25 — 25% RASP GRPO recovery（关键实验，验证 25% collapse 比 20% 更快）
- 4× Qwen Math pass@k8 evals（westd cuda:1/2/3）

**PREPARING (11)**: grpo_standard_25, eval_postprune_25, eval_sft_standard_20_n1319, eval_sft_grasp_20, eval_sft_alpha_0p5, eval_sft_rasp_20_full, grpo_standard_20_v8, grpo_rasp_20_v8, alpha_ablation_westd_cal256, grpo_stage2_standard_20_v5, grpo_stage2_rasp_20_v5（后两个是旧 v5 遗留）

**等待中**：
- Worker diagnose 回调 → 确定 sft_standard_25_westd 失败根因 → 修复重试
- grpo_rasp_25 完成回调 → 核心 25% collapse 数据点
- 4× Qwen Math eval 回调 → 填充 cross-model validation 数据

### 4. 📋 待办（条件触发式）
- Worker diagnose 回调到达 → 根据诊断结果修复命令（大概率 `--gpu 1` → `--gpu 0`）→ 重新提交 sft_standard_25_westd
- grpo_rasp_25 完成 → 对比 20% collapse timeline（RASP step~10 vs 25% 预期更早）→ 更新 paper_framing.md C2 证据
- eval_sft_rasp_25 完成 → 对比 sft_standard_25（一旦重跑成功）→ 25% 下 RASP vs Standard SFT gap
- sft_standard_25 重跑成功 → 立即提交 grpo_standard_25（cuda:1 空出后）→ 25% Standard GRPO negative control
- 4× Qwen Math eval 全部完成 → 汇总 cross-model 表格 → 更新 ROADMAP Phase 2 进度
- DDL 倒计时 9 天 → 25% GRPO + Qwen Math 必须并行，不能串行

### 5. 🎯 战略上下文
- **核心 narrative (D044/D045 pivot 后)**: GRPO alignment fundamentally fails on structurally pruned models — reward improves but accuracy never follows (universal decoupling). 不再是 "RASP enables better GRPO recovery"，而是 "所有剪枝模型 GRPO 都 collapse，RASP 的差异体现在 collapse 时间线和 SFT 恢复"
- **三大 Claims**: C1=Universal decoupling (unpruned reward↑ accuracy→), C2=Collapse gradient (RASP earliest → Standard later → Unpruned stable), C3=Functional redundancy plays opposite roles under SFT vs RLVR
- **D048**: C3 reframe 为 "RASP enables better GRPO recovery" 但这与 D044 有微妙冲突——实际上 RASP GRPO 也 collapse，只是时间线不同。下一个"你"注意不要把 C3 说成 "RASP GRPO works"
- **易错点**：
  - `--gpu` 参数：submit_training_job 已注入 CUDA_VISIBLE_DEVICES，脚本内必须 `--gpu 0`
  - westd cuda:1 当前有多个 eval 在跑，sft_standard_25 重试要等 eval 完成或确认不冲突
  - report.md 里"资源状态"显示"空闲"但实际有 7 个实验在跑——report 的资源段不可信，以 reconcile_crons 和 nvidia-smi 为准


---
