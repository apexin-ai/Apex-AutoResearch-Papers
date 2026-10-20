# agent / loop_16.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`bce89e794dc5b643ee2e.json`](../../sessions/bc/bce89e794dc5b643ee2e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-17T18:07:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-41312 GPU 白名单：cuda:0/1/2/3。westd-30476 GPU 白名单：cuda:0/1/2/3。两台服务器互不通用
- westd-30476 实验 output_dir 必须用 `/root/autodl-tmp/` 持久卷（非持久卷重启后数据丢失）
- 所有实验 WANDB_MODE=disabled（当前脚本不配 W&B），cron 监控依赖进程存活 + log sentinel，不依赖 W&B metrics
- llama3b 实验用 `unsloth/Llama-3.2-3B`，其余实验用 `Qwen/Qwen3-0.6B`——不要混
- submit_training_job 的命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && ...`

### 2. 🖥️ 基础设施快照
- **westd-30476**: 工作目录 `/root/provenance_weight_training`，Python `/root/miniconda3/bin/python`，conda env=base
- **westd-41312**: 同上路径结构
- 数据集：`/root/provenance_weight_training/data/scored_data.jsonl`（ρ=0.4, 371499 条），rho02/rho06 变体同目录
- HF cache：默认 `~/.cache/huggingface/`
- 活跃进程（westd-30476）：
  - random_reweight_seed123_r5: PID 20073, cuda:0, cron 已注册
  - bs8_auto_nmin_r5: PID 22466, cuda:1, cron 已注册
  - batch_adaptive_tau_rho06_r5: PID 22904, cuda:2, cron 已注册
  - rho02_adaptive_tau09_r5: PID 22095, cuda:3, cron 已注册
- 活跃进程（westd-41312）：
  - batchsize16_nmin8_seed42: PID 50284, cuda:2, cron 已注册
  - grid_b0_3_seed456: PID 88491, cuda:3, cron 已注册
- westd-41312:cuda:0 和 cuda:1 **空闲**

### 3. 📊 当前状态
**刚做完**：
- 处理 llama3b_adaptive_seed42 失败 cron 回调
- 发现 westd-30476 四个实验卡在 PREPARING 无 cron，已全部修复为 RUNNING + 注册 cron
- 向 Director 汇报了失败 + 空闲 GPU 情况

**等待中**：
- **诊断 Worker** `worker_diagnose_llama3b_adaptive_seed42_20260517T140045` 正在 SSH 到 westd-41312 检查训练是否实际完成。registry 中已有 metrics（PPL=10.58, eval_loss=2.359, conclusion 被之前 session 改成了 success），但 failure_reason 仍写着 "process dead 5×"。需要 Worker 确认 checkpoint 是否存在、PPL 是否准确。注意 metrics 中有 note "eval token count 不一致(4.0M vs uniform 1.5M)，待重新 eval"——这是关键问题
- **Eval Worker** `worker_eval_llama3b_uniform_lm_eval_20260517T134622` 在跑 llama3b_uniform 的 lm-eval
- **Director 决策**：westd-41312:cuda:0/1 空闲该跑什么？已向 Director 请示

**RUNNING 实验汇总**（6 个）：
| exp_id | 服务器:GPU | 用途 | 预估剩余 |
|--------|-----------|------|---------|
| random_reweight_seed123_r5 | 30476:0 | Claim 1 跨 seed random degradation | ~2h |
| bs8_auto_nmin_r5 | 30476:1 | D062 coupling rule bs=8 | ~3h |
| batch_adaptive_tau_rho06_r5 | 30476:2 | D063 batch-adaptive τ ρ=0.6 | ~3h |
| rho02_adaptive_tau09_r5 | 30476:3 | Claim 3 ρ=0.2 proportion-robust | ~3.5h |
| batchsize16_nmin8_seed42 | 41312:2 | D062 coupling rule bs=16 | 未知 |
| grid_b0_3_seed456 | 41312:3 | Claim 2 grid-best 跨 seed | 未知 |

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调 → 确认 llama3b_adaptive 是否真完成。若完成：conclusion 改 negative，发飞书结果卡，更新 report.md。若未完成：需重跑，加 W&B/log 配置
- eval Worker (llama3b_uniform lm-eval) 回调 → 记录 benchmark 分数到 registry
- Director 回复 westd-41312:cuda:0/1 安排 → 立即提交实验，不留空闲
- random_reweight_seed123_r5 最先完成（~2h）→ 按 on-experiment-done 分叉：PPL > uniform(17.688) 确认 Claim 1 跨 seed
- grid_b0_3_seed456 可能也接近完成 → 若 b=0.3 在 seed456 也是 grid-best，Claim 2 跨 seed 确认
- llama3b_adaptive metrics 有 "eval token count 不一致" 问题 → 可能需要重新 eval 才能公平比较

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25，**还剩 8 天**
- **核心方法**：Dual-constrained adaptive b*（α_eff 质量下界 + ESS 稳定上界）
- **三个 Claim**：
  - Claim 1 (dual > ESS-only): ★★★★★ 证据充足，random baseline 跨 seed 进行中
  - Claim 2 (adaptive ≈ grid): ★★★ grid-best=b=0.3，grid_b0_3_seed456 在跑
  - Claim 3 (proportion-robust): ★★ rho02_adaptive_tau09_r5 在跑，此前多次失败（transformers 版本 bug，已修）
- **关键决策**：D062 n_min coupling rule（n_min=⌊B/2⌋）已提升为方法正式设计原则；D063 hybrid pre-filter 暂 defer；D064/D065 Claim 1 叙事升级为 "both signal and principle"
- **跨模型泛化是 NEGATIVE**：Llama-3.2-3B adaptive PPL 退化，Core Claims 不受影响（全基于 Qwen3-0.6B），需在 Discussion 报告 limitation
- **易错**：
  - westd-30476 实验之前反复因 transformers 版本 bug 失败（`tokenizer=` → `processing_class=`），当前 r5 批次已修复，但如果 30476 环境被动过可能复发
  - llama3b_adaptive 的 eval token count 不一致问题——不能直接拿 PPL=10.58 和 uniform PPL=10.38 比较，可能需要统一 eval 后再下结论
  - 30476 上的实验 tmux_session_alive=false，进程是直接运行而非在 tmux 中——cron 通过 PID 监控，但如果 PID wrap 可能误判


---
