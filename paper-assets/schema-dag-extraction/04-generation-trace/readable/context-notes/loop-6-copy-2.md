# agent / loop_6.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`210de9937ea52fe1819a.json`](../../sessions/21/210de9937ea52fe1819a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-16T01:58:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单只有 **cuda:0**（cqa1-38874 单卡 RTX PRO 6000 Blackwell），不得用其他设备号
- **C001**: count_40 子集来自 80-type pool 采样，论文必须写 "40-rel subsets sampled from the 80-relation pool"
- **C002**: BCS amplification 3.4× 仅基于 16-type vs 80-type 两个 pool size，不得泛化表述
- submit_training_job 命令必须自带环境激活（`source /root/miniconda3/bin/activate && python3 ...`），不能假设 .venv
- flashinfer 已修到 0.6.11.post2 + nvidia-cuda-nvcc 13.2.78，需设 `CUDA_HOME=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13`，不要动这个配置

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-38874，RTX PRO 6000 Blackwell 98GB，CUDA 13.1
- **工作目录**: `/root/schema-dag-extraction`
- **Python**: `/root/miniconda3/bin/python`（conda base, Python 3.12.3）
- **Qwen3-32B-FP8**: `/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`
- **LLaMA-3.1-8B-Instruct**: `/root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct`
- **vLLM**: 0.20.2, torch 2.10.0+cu128
- **活跃进程**: exp_fewrel_16rel_bootstrap 已出结果（status=RUNNING 但 conclusion=success，需转 DONE）
- **Cron**: reconcile 返回 0 条活跃 cron

### 3. 📊 当前状态
**刚完成**: exp_fewrel_16rel_bootstrap 实际已跑完并出结果——16-rel pool BCS effect Δ(Q4-Q1)=-7.42pp, 95% CI [-9.45, -4.49], r=-0.637, bootstrap 1000 resamples。conclusion=success 但 status 卡在 RUNNING，需要转 DONE。

**正在进行**:
- `worker_submit_exp_fewrel_80pool_16sub_bootstrap`（running）— 正在提交 80-pool 采样 16 types 实验，消除跨 pool 混淆（审稿人 MW1 concern）
- `worker_analysis_d033_regression_slope`（running）— 分析 D033 回归斜率

**Registry 汇总**: RUNNING 1（exp_fewrel_16rel_bootstrap，实际已完成待转状态）、PREPARING 1（exp_fewrel_80pool_16sub_bootstrap，Worker 正在提交）、DONE 31（success 15 / negative 5 / failed 10 / killed 3）

**等待中**: 两个 running Worker 的回调；exp_fewrel_80pool_16sub_bootstrap 提交后的 cron 监控回调

### 4. 📋 待办（条件触发式）
- `worker_submit_exp_fewrel_80pool_16sub_bootstrap` 回调 → 确认实验已提交并注册 cron 监控，update_registry(status=RUNNING)
- `worker_analysis_d033_regression_slope` 回调 → 整合回归斜率分析到 report.md，向 Director 汇报 D033/D034 完整结果
- exp_fewrel_16rel_bootstrap → 立即 update_registry(status=DONE)，它已有 conclusion=success + metrics
- exp_fewrel_80pool_16sub_bootstrap cron 回调（完成）→ 与 16-rel 独立 pool 和 80-rel 做三方比较，计算 amplification ratio 正式 CI，更新论文 tab:bcs_controlled
- 三方比较结果出齐 → 向 Director 汇报完整 soundness 补强证据，确认 Soundness 3→4 是否达成
- ARR May 25 提交前（距今 9 天）→ 论文最终版编译 + 提交工程链

### 5. 🎯 战略上下文
- **核心结论**: type confusability（BCS）独立于 type count 驱动 training-free LLM IE 质量下降。双通道模型：count→recall 退化，confusability→type confusion。跨 3 任务（NER/ED/RE）+ 双模型（Qwen3-32B/LLaMA-8B）验证。
- **当前阶段**: Writing 冲刺 + Soundness 补强。写作对抗循环已收敛 8/10，正式预审已提交。D033 是最后一块 soundness 拼图——16-rel bootstrap CI 已出（success），80-pool 16-sub 正在提交。
- **决策链**: D031（跨模型复现成功升级 claim）→ D032（聚焦写作不追加模型）→ D033（16-rel bootstrap CI 填空白）→ D034（同时报告 quartile Δ 和 BCS-accuracy）
- **易错点**:
  - exp_fewrel_16rel_bootstrap status=RUNNING 但 conclusion=success——这不是还在跑，是状态转换遗漏，直接转 DONE
  - 16-rel 独立 pool 和 80-rel pool 的 BCS range 不同（16-rel [0.65, 0.90] vs 80-rel 更宽），三方比较时不能直接对比绝对值，要用 quartile-based Δ
  - SDGD（exp-008）已正式放弃（D014/D019），Claim 3 改为 negative result + future work，不要重开
  - MAVEN per-type BCS 正相关是 centrality artifact（exp_maven_residualized_bcs 已确认），不要在论文中 claim MAVEN 支持 per-type BCS effect


---
