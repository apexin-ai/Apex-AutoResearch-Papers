# reviewer / loop_6.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`9c907fd5fc9545f60900.json`](../../sessions/9c/9c907fd5fc9545f60900.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T09:54:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb GPU 白名单：cuda:0, cuda:1。westd GPU 白名单：cuda:0, cuda:1。越界进程立即 CRITICAL + kill
- D021 re-eval（westd PID 18580）是关键数据点——它决定 Standard 20% 是真 1% 还是 eval bug。**在 N=100 结果出来前，不要对 "Standard vs RASP 29pp gap" 下最终结论**
- SFT Standard retrain 模型在 westb `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/`（刚完成，尚未 eval）——这个 eval 结果直接影响 paper claim，确保 Agent 不跳过
- westd α ablation 用了 n_samples=256（不是默认 512），这是已确认的混淆变量。Agent 报告中有内部矛盾（声称 "layer 级别完全一致" 但 L20/L26 count 不同）——已在 D022 验证报告中标记

### 2. 🖥️ 基础设施快照
- **westb-23072** (root)：`/root/recovery_aware_struct_prune`，conda base `/root/miniconda3/bin/python`
  - 模型：`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`（base），`/root/autodl-tmp/pruned_rasp_20/`（RASP），`/root/autodl-tmp/pruned_standard_20/`（Standard），`/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/`（SFT Standard retrain 刚完成），`/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20/`（SFT RASP）
  - W&B project: `recovery_aware_struct_prune`，user: `xiaoyucorynne`
  - 活跃进程：GRPO v5 PID 498479 (cuda:0, W&B run tgpr1zwo, 6/250 steps ~2min/step)
  - GPU 1：**空闲**（SFT Standard retrain 17:50 完成）

- **westd-11672** (root)：`/root/recovery_aware_struct_prune`，conda base `/root/miniconda3/bin/python`
  - 模型：`/root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_{0.0,0.5,1.0}/`，`/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20/`（从 westb sync 的副本）
  - 活跃进程：
    - SFT α=0.0 PID 16795 (gpu 0, 78%, ~12min 剩余)
    - SFT α=0.5 PID 16796 (gpu 1, 92%, ~3min 剩余)
    - D021 re-eval PID 18580 (CUDA_VISIBLE_DEVICES=1, 27/100, max_new_tokens=4096)
  - ablation 驱动脚本：`run_alpha_ablation_full.sh` (PID 7191)，后续会接 α=1.0 SFT + eval

### 3. 📊 当前状态
刚完成 D022 代码对比验证报告并提交给 Director（severity: warning）。核心发现：calibration 差异 512 vs 256 已确认，但 Agent 报告有内部矛盾，且 D021 N=20 re-eval=40% 动摇了 "1% 是真实退化" 的前提。

Registry RUNNING：`grpo_stage2_rasp_20_v5`（westb GPU 0，6/250 步）
等待：D021 N=100 re-eval 结果（westd，~45min），SFT ablation 三组完成后的 eval 结果，westb SFT Standard retrain 的 eval

### 4. 📋 待办（条件触发式）
- D021 N=100 re-eval 完成 → 读 `/tmp/reeval_standard_20_results.json`。若 acc ≥ 25% → 确认原始 1% 是 eval bug，"calibration 导致 catastrophic degeneration" 不成立，立即通知 Director 更新根因判断。若 acc < 5% → 原始 1% 可能真实，fragile threshold 理论仍需考虑
- SFT α=0.5 完成 → 检查 α=1.0 SFT 是否自动启动（由 `run_alpha_ablation_full.sh` 驱动）
- westb GPU 1 持续空闲 > 15min → 通知 Director，Agent 应在此启动 SFT Standard retrain eval
- GRPO v5 ~10 步后 → 检查 W&B loss 趋势，特别关注 reward desert（patience=50 events）
- SFT ablation 全部完成 + eval 完成 → 对比 α=0.0/0.5/1.0 三组 GSM8K accuracy，判断 α ablation 是否有统计显著差异（N=100 下 SE ≈ 4.5pp，需 ≥ 10pp 差距才有意义）
- `run_alpha_verify_512.sh` 若被执行 → 这会用 n_samples=512 重算 westd 的 scores 并重新 prune，是消除 calibration 混淆的关键实验

### 5. 🎯 战略上下文
- **核心决策链**：D021（数据可信度危机：Standard 1% vs α=0.0 30%）→ D022（GRPO v4 太慢 → v5 减 max_completion_length）→ 当前等待 D021 re-eval 定论
- **项目核心 claim**：RASP（CKA-aware pruning）优于 Standard pruning。westb 原始数据 Standard=1% vs RASP=29% 看起来惊人，但 D021 re-eval 暗示 1% 是 eval bug。如果 Standard 实际 ~30-40%，则 RASP vs Standard 的差距可能不显著——这将动摇论文核心 claim
- **EMNLP ARR deadline**：May 25（10 天）。GRPO v5 预计 ~8h 完成。时间仍充足但 RASP vs Standard 的 evidence 必须在此之前站稳
- **最容易判断错的事**：①不要因为 RASP 29% vs Standard "1%" 就认为 RASP 大幅优于 Standard——等 D021 N=100 re-eval 确认 Standard 真实水平。②α ablation 当前 N=100 下 0.0/0.5/1.0 无显著差异（25-30%），不支持也不否定 CKA 的价值——别过度解读。③Agent 报告有时自相矛盾（如 D022 报告的 "layer 级别完全一致" 与表格数据不符），需交叉验证而非直接采信


---
