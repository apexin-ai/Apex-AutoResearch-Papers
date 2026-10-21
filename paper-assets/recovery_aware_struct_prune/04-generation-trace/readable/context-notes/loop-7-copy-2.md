# agent / loop_7.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`d54f0893da215a8e88fc.json`](../../sessions/d5/d54f0893da215a8e88fc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-15T11:28:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- **D025 数据可信度挂起**：所有基于 "29% vs 1% (29x advantage)" 的结论暂停。westd α ablation 显示 Standard post-prune ~30%（非 1%），根因是 calibration samples 差异（westb=512, westd=256）。Worker `worker_code_westd-rasp-reeval-definitive` 正在做 definitive re-eval，出结果前**禁止在汇报/论文中引用 29x**。
- **sft_standard_20 checkpoint 已删除**：磁盘清理误删 81GB checkpoint，正在 cuda:1 重训（sft_standard_20_retrain, PENDING 状态等审批）。GRPO Standard 对照实验依赖此 checkpoint。
- **GPU 白名单**：westb-23072 cuda:0/cuda:1；westd-11672 可用但 GPU ID 需确认。
- **calibration 混淆未消除**：westd 上的 α ablation 用了 256 samples，与 westb 的 512 不一致，导致 ~5% MLP group 选择差异。正式结论必须用 512 samples 重算。

### 2. 🖥️ 基础设施快照
- **westb-23072**：工作目录 `/root/recovery_aware_struct_prune`，数据盘 `/root/autodl-tmp/`（141/250GB used）
  - Python：`/root/miniconda3/bin/python`，conda base env（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
  - 基础模型：`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`
  - 剪枝模型：`/root/autodl-tmp/pruned_rasp_20`, `/root/autodl-tmp/pruned_standard_20`
  - SFT checkpoint：`/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20`（有效），`sft_standard_20`（已删，重训中）
  - CKA 缓存：`results/cka_scores.pt`
  - W&B project: recovery_aware_struct_prune
- **westd-11672**：工作目录 `/root/recovery_aware_struct_prune`（同步代码），数据盘 178GB free
  - 同样 conda base env
- **活跃进程**：
  - `grpo_stage2_rasp_20_v5` — westb cuda:0, PID 498474, tmux session, cron 监控中
  - `sft_standard_20_retrain` — westb cuda:1, PID 239068, PENDING 等审批
- **活跃 Worker**：`worker_code_westd-rasp-reeval-definitive`（westd 上做 definitive re-eval）

### 3. 📊 当前状态
**刚完成**：GRPO v4 killed（29min/step 不可接受），启动 v5（max_completion_length 2048→512）。处理了 D023/D024 数据可信度危机（westd α ablation 暴露 calibration confound），派 Worker 做 definitive re-eval。

**Registry 活跃实验**：
| exp_id | 状态 | 摘要 |
|--------|------|------|
| grpo_stage2_rasp_20_v5 | RUNNING | 决定性 GRPO 实验，v4 速度修复版，cuda:0 |
| sft_standard_20_retrain | PENDING | 重训被删 checkpoint，cuda:1，等审批 |
| reeval_postprune_definitive | PREPARING | 验证 29% vs 1% 是否可复现 |
| alpha_ablation_westd_cal256 | PREPARING | westd 上 α ablation Phase A 完成，Phase B(SFT) 待推进 |

**等待中**：
- Worker `worker_code_westd-rasp-reeval-definitive` 回调 → definitive re-eval 结果
- `grpo_stage2_rasp_20_v5` cron 回调 → GRPO 决定性结果
- `sft_standard_20_retrain` 审批通过 → 启动重训 → 后续 GRPO Standard 对照

### 4. 📋 待办（条件触发式）
- **definitive re-eval Worker 完成** → 比对 westb/westd 的 RASP vs Standard post-prune accuracy。若 westb 1% 可复现 → D025 解除挂起，29x 结论恢复；若 Standard ~30% → 核心 narrative 需 reframe（差距从 29x 缩小到 <2x），**立即向 Director 汇报**
- **sft_standard_20_retrain 审批通过** → 确认训练启动，~37min 完成后可作为 GRPO Standard 对照的 checkpoint
- **grpo_stage2_rasp_20_v5 完成** → 这是整个项目的决定性实验。按 ROADMAP contingency 表判断：RASP>>Standard(>10pp) 全面推进；RASP≈Standard(<5pp) 转 training dynamics 分析；Standard>RASP 核心假设失败需 reframe
- **sft_standard_20_retrain 完成** → 立即启动 grpo_stage2_standard_20_v5（用 v5 同参数，作为 RASP 对照）
- **α ablation 推进** → 需在 westd 用 n_samples=512 重算 importance scores 消除 calibration 混淆，然后 Phase B(SFT) + Phase C(eval)

### 5. 🎯 战略上下文
- **目标**：EMNLP 2026 ARR May 25（距今 10 天）。核心 claim = CKA functional overlap 指导的 RASP 剪枝在 RLVR 恢复下优于 importance-only 剪枝。
- **决策链核心**：D025 挂起了所有基于 29x advantage 的结论 → D023 暴露 calibration confound → definitive re-eval 和 GRPO v5 是当前两个阻塞点。
- **GRPO 是生死线**：v1-v3 全部 sampling collapse（grad_norm=0），v4 速度不可接受（29min/step），v5 是最后的参数组合（temp=0.4, rep_penalty=1.15, beta=0.01 with monkey-patched ref_model, max_completion_length=512）。如果 v5 也 collapse，GRPO 路线宣告失败，需要 pivot。
- **最容易判断错的事**：(1) 不要假设 29% vs 1% 是确定事实——calibration sensitivity 说明 20% sparsity 是 fragile threshold，结果高度依赖 calibration 样本数；(2) GRPO 对剪枝模型极不稳定，即使 SFT 恢复了 greedy accuracy，sampling mode 仍可能 collapse；(3) sft_standard_20 checkpoint 不存在了，任何依赖它的实验需要等重训完成。
- **Dream 审稿模拟**：最佳 Weak Accept(4/6)，三档一致问题=α ablation 缺失(Critical)、single model、no inference speedup。这些是 GRPO 完成后必须补的实验。


---
