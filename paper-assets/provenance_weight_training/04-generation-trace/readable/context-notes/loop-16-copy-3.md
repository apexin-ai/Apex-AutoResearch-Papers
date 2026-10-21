# reviewer / loop_16.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`f3c9aa76c1bb534f94e0.json`](../../sessions/f3/f3c9aa76c1bb534f94e0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-17T16:55:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-47453 永久宕机，不要尝试 SSH 连接或在其上调度任务
- ess_only_seed123/seed456 的 registry 指标（PPL 17.72/17.719）来源不明——registry 标 DONE 但实际训练仅 16%，原始 eval 文件未找到。引用这些数字前必须等当前重跑完成后重新验证
- llama3b_uniform_seed42 的 registry PPL=10.38 是错的（eval 只用了 1.5M tokens），正确值是 10.53（max_docs=5000, 4M tokens），证据在 westd-41312:/tmp/reeval_both.json
- random_reweight_seed123 checkpoint 在非标准路径 `/root/autodl-tmp/output/models/random_reweight_seed123/`（westd-30476），不在 `provenance_weight_training/output/` 下

### 2. 🖥️ 基础设施快照
- **westd-30476**（root）：工作目录 `/root/provenance_weight_training`，conda base，4× RTX PRO 6000 Blackwell 97887 MiB
  - GPU 0: eval 进程 PID 32393+32718（random_reweight PPL eval，可能已完成）
  - GPU 1: bs8_auto_nmin_r5（PID 22478, 81678 MiB）
  - GPU 2: batch_adaptive_tau_rho06_r5（PID 22917, 46496 MiB）
  - GPU 3: rho02_adaptive_tau09_r5（PID 22108, 46496 MiB）
- **westd-41312**（root）：同配置
  - GPU 0: uniform_seed42 retrain（PID 109024, 75014 MiB）
  - GPU 1: ess_only_seed456 重跑（PID 115525, 75014 MiB, step ~987/6103）
  - GPU 2: ess_only_seed123 重跑（PID 115021, 75014 MiB, step ~987/6103）
  - GPU 3: **空闲**（grid_b0_3_seed456 已完成）
- 统一 eval 命令：`python eval_perplexity.py --max_docs 5000 --data_path data/human/eval_holdout.jsonl`（产出 4,077,068 tokens）
- Llama 模型路径：`models/unsloth/Llama-3.2-3B`；Qwen：`models/Qwen/Qwen3-0.6B`

### 3. 📊 当前状态
刚完成 random_reweight_seed123_r5 PPL 审查（17.801，支持 Claim 1）并汇报 Director。

Registry 关键状态：
- `random_reweight_seed123_r5`: ANALYZING（eval 已出但 registry 未更新到 DONE）
- `bs8_auto_nmin_r5` / `batch_adaptive_tau_rho06_r5` / `rho02_adaptive_tau09_r5`: RUNNING（westd-30476）
- `grid_b0_3_seed456`: registry 仍 RUNNING 但实际已完成（final/ 存在），需更新
- `ess_only_seed123/456`: registry 标 DONE 但实际在重跑中（~16%）
- `qwen06b_uniform_seed42`: PREPARING（未启动）

未修正 registry 问题（已提醒三次）：
- llama3b_uniform_seed42 PPL 10.38→10.53
- llama3b_adaptive_seed42 conclusion "negative"→"neutral"
- batchsize16_nmin8_seed42 conclusion "failed"→"success"（PPL=17.653）

### 4. 📋 待办（条件触发式）
- bs8_auto_nmin_r5 / batch_adaptive_tau_rho06_r5 / rho02_adaptive_tau09_r5 完成 → 核实 checkpoint + eval，对比 uniform baseline，检查 registry 更新
- ess_only_seed123/456 重跑完成（~3h 后）→ 独立跑 eval，与 registry 现有指标交叉验证。若差异 >0.05 PPL → CRITICAL
- grid_b0_3_seed456 eval 结果出现 → 对比 grid_b0_2（17.64），验证 b=0.3 vs b=0.2 排序
- uniform_seed42 retrain 完成 → 核实 PPL 与原值（10.53 for Llama / ~17.69 for Qwen）一致
- Director 转发 Framing 提案 → 先 Read `negative-framing-review.skill.md` 再审

### 5. 🎯 战略上下文
**核心结论链**：
- Claim 1（detector 信号 load-bearing）：random(17.801) > uniform(~17.69) > adaptive(17.65) ✅ 已有数据支撑
- Claim 2（adaptive ≈ grid-best）：adaptive_fix(17.6527) ≈ grid_b0.2(17.640) ✅ 差距仅 0.013
- Claim 3（unknown contamination）：待更多 ρ 变体实验（rho02 等正在跑）
- Cross-model（Llama-3B）：PPL parity（Δ=0.048），MMLU +1.57pp，不够升级 claim，建议 Discussion 中保守提及
- ESS-only baseline：比 adaptive 差（17.72 vs 17.65），验证 min-intervention 原则——但当前 PPL 数据来源存疑，需重跑验证

**易错点**：
- 不同实验的 eval 用了不同 max_docs（历史遗留），比较 PPL 前必须确认 token 数一致（应为 4,077,068）。registry 里 llama3b_uniform 的 1,526,195 tokens 就是这个坑
- ess_only registry 数据可能不可靠（来源不明），不要直接引用写论文
- Cron on_complete 经常误报"failed"（进程正常结束但无 sentinel/W&B），要 SSH 核实再判断


---
