# agent / loop_12.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`d9983413e86db89a0e6d.json`](../../sessions/d9/d9983413e86db89a0e6d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-16T05:06:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd-47453 cuda:0/1/2/3，其他设备号禁止使用
- GPU 预算极度紧张（剩余 ~26h），新实验必须精打细算
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（服务器用 conda，无 .venv）
- WANDB_MODE=disabled（本项目全部实验禁用 W&B online，cron 靠日志解析判断完成）
- n_min=2 是论文主结果（D043 决策），n_min=3 降为 sensitivity analysis
- grid_b_low 系列已连续失败 4 次（D041），Director 要求先诊断根因再重启

### 2. 🖥️ 基础设施快照
- 服务器: westd-47453，工作目录 /root/provenance_weight_training
- Python: /root/miniconda3/bin/python（conda base env）
- 模型: /root/provenance_weight_training/models/Qwen/Qwen3-0.6B
- 数据: /root/provenance_weight_training/data/scored_data.jsonl (ρ=0.4), scored_data_60.jsonl (ρ=0.6, 371K行)
- 输出: /root/provenance_weight_training/output/models/{exp_id}/
- 日志: ~/runs/provenance_weight_training/{exp_id}.log
- 活跃进程:
  - contamination_60_seed42_r2 (PID 257977, cuda:0) — ρ=0.6 adaptive
  - contamination_60_ess_only_seed42 (PID 265012, cuda:2) — ρ=0.6 ESS-only
  - grid_b0_3_seed42 (PID 274304, cuda:1) — b=0.3 sweep

### 3. 📊 当前状态
**刚发生**: `contamination_60_grid_b0_5_seed42` (cuda:3) 失败，EXIT_CODE=129 (SIGHUP)，运行了 3.65h。已派 Worker `worker_diagnose_contamination_60_grid_b0_5_seed42_20260516T013019` SSH 诊断日志——**回调尚未返回**。

**注意**: 同批次 `contamination_60_uniform_seed42` 也是 EXIT_CODE=129 但被标记 success，可能是 tmux 退出码误报模式（训练实际完成但 tmux 返回 129）。诊断 Worker 需要确认训练是否跑完。

**RUNNING**: 3 实验（见上），cuda:3 空闲待重新分配。

**PREPARING**: 10 实验（tau_05/06/07/09/095_nmin2_seed42, grid_b0_1/0_2_seed42, adaptive_v2_seed123/456, detect_remove_baseline_seed42）

### 4. 📋 待办
- Worker 诊断回调到达 → 如果训练实际完成：update_registry conclusion=success + 提取 final PPL → 汇报 Director
- Worker 诊断回调到达 → 如果训练未完成：update_registry failure_reason 详细原因 → 在 cuda:3 重跑 → 汇报 Director
- contamination_60_seed42_r2 完成 → 三组 ρ=0.6 结果齐全（adaptive/uniform/grid_b0.5）→ 分析 Claim 3
- contamination_60_ess_only_seed42 完成 → 补全 Claim 3 第四组对照
- grid_b0_3_seed42 完成 → b* curve 又多一个点，更新 Claim 2 证据
- 全部 contamination_60 完成 → 向 Director 汇报 Claim 3 验证结果 + 建议下一步（paper experiments section）
- cuda:3 空闲 → 重跑失败实验或从 PREPARING 队列挑优先级最高的提交（需 Director 审批）

### 5. 🎯 战略上下文
- 投稿目标: EMNLP 2026 ARR May 25（还剩 9 天）
- 核心框架: Dual-constrained adaptive b*（α_eff 下界 + ESS 上界），替代 Drayson validation-based grid search
- Claim 1 (dual > ESS-only): ✅ 3 seeds 验证完成
- Claim 2 (adaptive ≈ grid-best): ✅ 3 seeds MVP PASS
- Claim 3 (proportion-free，ρ 变化不影响): 🔄 正在验证，contamination_60 是关键
- τ sweep: ✅ 完成，safe range [0.5, 0.8]，τ=0.8 optimal
- bs8_nmin2 negative: Director 决策写入 limitation section（D042）
- EXIT_CODE=129 模式: 本项目多次出现（uniform 成功但也是 129），很可能是 tmux session 清理导致的 SIGHUP 而非真实 crash——诊断时优先检查训练是否跑完而不是死扣退出码
- 易踩坑: n_min confound（早期实验用 n_min=3，D043 后统一为 n_min=2 重跑）；不要混淆新旧 tau sweep 结果


---
