# reviewer / loop_12.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`237baa65aebb21121596.json`](../../sessions/23/237baa65aebb21121596.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-16T10:31:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-47453 的 4 张 GPU (0-3) 全部归本项目使用，无跨项目 gpu_ids 白名单限制
- `--use_wandb` flag 与 `WANDB_MODE=offline` 冲突——脚本里两者只能留一个，否则 wandb.init() 报 API key 错误（已导致 random_reweight 3 次失败）
- detect_remove PPL=17.29 不可直接与 adaptive PPL=17.65 对比——eval confound（filtered data distribution match human-only eval）。阈值敏感性实验 (q03/q07) 是正确的分析框架
- `--n_min` 如果显式传入会覆盖自动计算逻辑 `max(2, batch_size//2)`。之前 bs8 negative result 就是因为脚本硬传了 `--n_min 2`

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453 (root)，工作目录 `/root/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`（conda base，不用 venv）
- 模型：`/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`（主模型）；`models/meta-llama/Llama-3.2-3B/`（跨架构验证，已下载 6.4GB）
- 数据：`data/scored_data.jsonl`(371K, ρ=0.4), `data/scored_data_rho06.jsonl`(371K, ρ=0.6), `data/scored_data_rho02.jsonl`(206K, ρ=0.2), `data/scored_data_hybrid.jsonl`/`_rho06.jsonl`(q≤0.95 filtered)
- Eval holdout：`data/human/eval_holdout.jsonl`
- WANDB_MODE=offline（所有新实验）；HF_HOME=/root/autodl-tmp/.hf_cache
- 截至 handoff：**仅 GPU 1 有活跃进程**（PID 316988, rho02_uniform_seed42）。GPU 0/2/3 全空闲——3 实验同时被系统 kill

### 3. 📊 当前状态
**刚做完**：
- 发现并报告 GPU 0/2/3 三个实验同时崩溃（系统级事件，非个别故障）
- 完成方法改进深度分析（理论+实验），提交给 Director：方案 A(n_min scaling) 确认代码已有、方案 B(batch-adaptive-τ) 代码已写好、方案 C(hybrid filter+reweight) 脚本已就绪
- grid_b0_1 eval 核实通过（PPL=17.657，确认 U-shape，b=0.3 为 grid-best）

**Registry RUNNING**：
- `rho02_uniform_seed42`：GPU 1，唯一存活实验（~3.6h 训练）
- `random_reweight_seed42`：Registry 仍标 RUNNING 但实际第 3 次 fail（step 499, 无 checkpoint）
- `threshold_q03_seed42`：Registry 仍标 RUNNING 但已死（step 2499, checkpoint-2000 可 resume）
- `threshold_q07_seed42`：已更新为 FAILED（step 2235, checkpoint-2000 可 resume）

**等待中**：Director 响应 GPU 崩溃报告 → 决定重启优先级

### 4. 📋 待办（条件触发式）
- threshold_q03/q07 重启并完成 eval → 三点阈值敏感性对比 (q=0.3/0.5/0.7)；若 PPL 变化 >0.1 → detect_remove "需精确校准" narrative 成立；若 <0.1 → reweighting 优势 narrative 需调整
- random_reweight 完成 eval → 若 PPL ≈ uniform (17.69) → detector signal load-bearing confirmed (Table 1 必需)
- rho02_uniform 完成 → 启动 rho02_adaptive_tau09 (脚本已就绪 `scripts/run_rho02_adaptive_tau09_seed42.sh`)；若 adaptive PPL < uniform 且 τ=0.9=1-0.2/2 → 公式第三验证点
- Plan B (batch-adaptive-τ) 实验完成 → 审查 ρ=0.6 capture ratio 是否从 58% 提升；若 >70% → 方法改进实质成立
- Llama-3B 实验启动 → 审查是否保持 Qwen 上的 relative ordering（adaptive ≈ grid-best > uniform）

### 5. 🎯 战略上下文
- **投稿**：EMNLP 2026 ARR May 25（剩 9 天）
- **核心方法**：dual-constrained adaptive b* = inf{b: α_eff(b)≥τ} s.t. ESS≥n_min，weight w=(1-q)^b
- **三大 Claims**：(1) 最小干预原则 (2) 免 grid-search 匹配 grid-best (3) τ=1-ρ/2 启发式（2 点验证，第 3 点 ρ=0.2 pending）
- **关键决策链**：D045(ρ=0.6 underperform)→D050(grid-best shift to b=0.3)→D051(detect_remove confound→threshold sensitivity)
- **最易判断错的事**：
  - detect_remove PPL=17.29 看起来远优于 adaptive，但这是 eval confound 不是真实优势——**不要建议放弃 reweighting 转 filtering**
  - adaptive vs grid-best gap=0.004 统计不显著(p=0.30)，Claim 2 的 framing 是"comparable without search"不是"better than"
  - ESS-only PPL=17.73 比 uniform 更差——这证明 max-intervention harmful，是核心 narrative 支柱
  - 60% reweighted batches 是 ESS-binding（α_eff 目标未达成），方法在这些 batch 上退化为 ESS-only——这是方法的真实弱点但目前 paper 没显式承认
  - ρ=0.6 实验用 contamination_60_* 前缀，ρ=0.4 用无前缀——注意区分


---
