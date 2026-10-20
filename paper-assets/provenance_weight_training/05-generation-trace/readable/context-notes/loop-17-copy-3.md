# reviewer / loop_17.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`ecaf97cfe8a9b083984c.json`](../../sessions/ec/ecaf97cfe8a9b083984c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-17T22:17:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-30476 和 westd-41312 均为 cuda:0-3，越界即 CRITICAL
- eval 协议统一：eval_perplexity.py, max_docs=5000, stride=1024 (max_length//2), autocast fp16, eval_holdout.jsonl。任何偏离导致 PPL 不可比
- batchsize16 实验必须 per_device_train_batch_size=16 + gradient_accumulation_steps=1（不能 bs=4×accum=4，因为 ESS 按 micro-batch 算，micro_batch < n_min 会导致 b*=0 永远）
- 所有实验 WANDB_MODE=disabled，不查 W&B，只看 step_metrics.jsonl + eval_perplexity_results.json
- westd-41312 进度条显示 X/8477（含 eval forward passes），实际训练步数看 step_metrics.jsonl 最后 step 字段或 max_steps=6103

### 2. 🖥️ 基础设施快照
- **westd-30476** (root): 4× NVIDIA RTX PRO 6000 Blackwell 98GB
  - 代码：`/root/provenance_weight_training`
  - 模型输出：`/root/autodl-tmp/output/models/` 和 `/root/autodl-tmp/provenance_weight_training/output/models/`（两个路径都有实验）
  - 日志：`/root/runs/provenance_weight_training/*.log`
  - eval 脚本：`/root/provenance_weight_training/eval_perplexity.py`
  - conda: base env, HF_HOME=/root/autodl-tmp/.hf_cache
- **westd-41312** (root): 4× NVIDIA RTX PRO 6000 Blackwell 98GB
  - 代码：`/root/provenance_weight_training`
  - 模型输出：`/root/autodl-tmp/provenance_weight_training/output/models/`
  - lm-eval-harness v0.4.11 已安装：`/root/miniconda3/bin/lm_eval`
  - eval 结果目录：`/root/autodl-tmp/provenance_weight_training/output/eval/`

### 3. 📊 当前状态
**刚完成审查**：uniform_seed42_v2 PPL=17.6949（与历史 17.6939 差 0.001，可复现确认）。Llama-3B downstream eval 分析已报 Director（MMLU +1.57pp 显著但 HellaSwag -0.60pp，不支持升级 claim）。

**westd-30476 运行中**（截至 ~22:00 UTC）：
| GPU | 实验 | PID | 进度 | ETA |
|-----|------|-----|------|-----|
| 0 | grid_b0_3_seed456_r2 | 54784 | ~25% | ~3h |
| 1 | grid_b0_3_seed123 (resumed) | 53826 | ~41% | ~2h |
| 2 | rho02_adaptive_tau08_seed42 | 41387 | ~90% | ~25min |
| 3 | batchsize16_nmin8_r2 | 48891 | ~57% | ~2.5h |

**westd-41312 运行中**：
| GPU | 实验 | PID | 进度 | ETA |
|-----|------|-----|------|-----|
| 0 | **空闲** | — | — | — |
| 1 | ess_only_seed456_r2 | 133526 | ~72% | ~1h |
| 2 | ess_only_seed123_r2 | 133449 | ~63% | ~1.3h |
| 3 | random_reweight_seed456 | 136149 | ~33% | ~2.4h |

### 4. 📋 待办（条件触发式）
- rho02_adaptive_tau08_seed42 完成 → 验证 PPL（预期 ~17.3-17.5 范围），对比 rho02_tau09 的 17.45 确认 tau=0.8 是否更优
- ess_only_seed123_r2 / seed456_r2 完成 → eval PPL，对比旧 ess_only 结果（seed42 PPL=17.76），3-seed 一致性验证
- random_reweight_seed456 完成 → eval PPL，凑齐 2-3 seed（seed123 已有 PPL=17.8），确认 random baseline 与 uniform 持平
- batchsize16_nmin8_r2 完成 → eval PPL，验证 coupling rule n_min=bs//2 在 bs=16 下成立
- grid_b0_3_seed123/seed456_r2 完成 → eval PPL，验证 cross-seed 一致性（seed42=17.64）
- 41312 cuda:0 空闲 → Director 应已安排新任务（contamination_60 或其他）

### 5. 🎯 战略上下文
**三核心 Claim**：
- Claim 1（detector signal load-bearing）：需 random_reweight baseline PPL ≈ uniform >> adaptive。seed123 已有 17.8 ≈ uniform 17.34? 不对——需重新确认 random 是否真的和 uniform 持平
- Claim 2（adaptive ≈ grid-best）：adaptive PPL 17.336 vs grid-best b=0.3 PPL 17.64。**注意这里 adaptive 明显更好不是"≈"**，U-shape 存在但 grid-best 远不如 adaptive
- Claim 3（proportion-robust）：tau=0.9 在 ρ=0.2 时 PPL=17.45 > uniform 17.34 **失败**。现在跑 tau=0.8 在 ρ=0.2 验证修正

**易错点**：
- 8477 vs 6103 步数混淆：带 eval_data_path 的实验进度条显示 8477（含 eval），实际 optimizer steps = 6103
- output_dir 路径不统一：有些在 `/root/autodl-tmp/output/models/`，有些在 `/root/autodl-tmp/provenance_weight_training/output/models/`——按实际 checkpoint 路径为准
- save_only_model=True：checkpoint 无 optimizer state，resume 时 Adam momentum 从零重积累，前几百步可能有轻微 loss 波动
- 进程被 kill 的 pattern：Agent 会主动 kill 带 eval_data_path 的慢实验后重启无 eval 版本，这是正常操作不是故障，但 cron 会报 failed


---
