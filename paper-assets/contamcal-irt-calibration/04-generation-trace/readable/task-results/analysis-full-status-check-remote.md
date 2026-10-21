# analysis full status check remote

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_full-status-check-remote_20260515T044627_result.json`
- **Structured JSON:** [`ae322ff41ea26a5fd0ab.json`](../../sessions/ae/ae322ff41ea26a5fd0ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整状态报告

### 进程状态表

| exp_id | PID | 状态 | GPU | 运行时长 | 进度/结果摘要 |
|--------|-----|------|-----|---------|-------------|
| exp_001_eval_3B_d100_v2_aligned_v2 | 477489 | running | cuda:0 | 3h45m | eval 进行中（mmlu/gsm8k/arc/humaneval） |
| exp_008_instruct_05B_eval | 493617 | running | cuda:4 | 1h21m | eval 进行中 |
| exp_001_eval_05B_d000_s42_v7 | 494109 | running | cuda:4 | 1h19m | eval 进行中 |
| exp_001_eval_3B_d000_v2_s123_aligned | 492660 | running | cuda:1 | 1h25m | eval 进行中 |
| exp_001_eval_3B_d025_v2_para_aligned | 499610 | running | cuda:2 | 0h31m | eval 进行中（含 paraphrase） |
| exp006-oracle-arc-2pl | 496697 | **exited** | CPU | 完成 | **已完成**，3402s，结果已保存 |
| exp006-s1only-gsm8k-2pl | 496852 | running | CPU | 0h59m | IRT+baselines 已完成，正在跑 B3_vanilla_4pl baseline（chain1 ~60%） |
| exp006-oracle-arc-4pl-pooled | tmux | running | CPU | ~54m | chain4 warmup 28%（1700/6000），仍在 warmup 阶段 |
| exp_001_sft_05B_d025_s123_v2 | 498153 | running | cuda:3 | 0h46m | **45% (1534/3384)**，epoch 0.35，loss 1.51，ETA ~55min |
| exp_001_sft_3B_d100_s123 | 471296 | running | cuda:5 | 4h35m | **90% (3764/4159)**，epoch 0.86，loss 1.14，ETA ~32min |

### GPU 使用情况

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 21268/24564 MiB | 74% |
| 1 | 8985/24564 MiB | 60% |
| 2 | 9017/24564 MiB | 59% |
| 3 | 0/24564 MiB | 0% |
| 4 | 7254/24564 MiB | 31% |
| 5 | 17981/24564 MiB | 21% |

---

### 已完成实验结果

#### exp006-oracle-arc-2pl（arc_challenge，oracle exposure，2pl_gamma）

**诊断指标**：max_rhat=1.006, min_ess=1512, divergences=0, **all OK**

| Method | MAE | ECE | Brier | C50 | C80 | C95 | S95 | tau | gamma>0 |
|--------|-----|-----|-------|-----|-----|-----|-----|-----|---------|
| **IRT_2pl_gamma** | 0.0759 | 0.0759 | 0.0088 | 0.18 | 0.18 | 0.18 | 0.07 | 0.739 | **-0.618** |
| B0_raw | 0.0685 | 0.0668 | 0.0101 | 0.45 | 0.55 | 0.55 | 0.05 | 0.760 | --- |
| B1_remove_rescore | 0.0685 | 0.0668 | 0.0101 | 0.45 | 0.55 | 0.55 | 0.05 | 0.760 | --- |
| B2_2pl_gamma | 0.0758 | 0.0758 | 0.0088 | 0.18 | 0.18 | 0.18 | 0.07 | 0.739 | --- |
| B3_vanilla_4pl | 0.0754 | 0.0754 | 0.0073 | 0.09 | 0.09 | 0.09 | 0.04 | 0.739 | --- |
| B4_linear_regression | 0.0752 | 0.0752 | 0.0114 | 0.55 | 0.73 | 0.73 | 0.27 | 0.739 | --- |
| B5_emperor_mitigation | 0.0685 | 0.0668 | 0.0101 | 0.45 | 0.55 | 0.55 | 0.05 | 0.760 | --- |
| B6_dcr_fuzzy | 0.2631 | 0.2631 | 0.1104 | 0.27 | 0.27 | 0.27 | 0.03 | 0.394 | --- |

**gamma 参数**：mean=-0.618, 95% CI=[-1.042, -0.202], **CI excludes zero (负方向)**
- Ground truth: 0.5B d0 mean=0.469, 1.5B d0 mean=0.772

---

#### exp006-s1only-gsm8k-2pl（gsm8k，s1_embedding 信号，2pl_gamma，中间结果）

2pl_gamma 主 IRT 和大部分 baselines 已完成，B3_vanilla_4pl 仍在拟合中。

| Method | MAE | ECE | Brier | C50 | C80 | C95 | S95 | tau | gamma>0 |
|--------|-----|-----|-------|-----|-----|-----|-----|-----|---------|
| **IRT_2pl_gamma** | 0.0131 | 0.0130 | 0.0003 | 0.50 | 1.00 | 1.00 | 0.08 | 0.756 | **0.167** |
| B0_raw | 0.0031 | 0.0031 | 0.0000 | 1.00 | 1.00 | 1.00 | 0.05 | 0.756 | --- |
| B1_remove_rescore | 0.0031 | 0.0031 | 0.0000 | 1.00 | 1.00 | 1.00 | 0.05 | 0.756 | --- |
| B4_linear_regression | 0.0026 | 0.0026 | 0.0000 | 1.00 | 1.00 | 1.00 | 0.23 | 0.756 | --- |
| B5_emperor_mitigation | 0.0031 | 0.0031 | 0.0000 | 1.00 | 1.00 | 1.00 | 0.05 | 0.756 | --- |
| B6_dcr_fuzzy | 0.1793 | 0.1793 | 0.0682 | 0.50 | 0.50 | 0.50 | 0.03 | 0.378 | --- |

**gamma 参数**：mean=0.167, 95% CI=[-0.306, 0.636], **CI does NOT exclude zero**

---

### 关键发现

1. **arc_challenge oracle 2pl**：gamma 显著为负（-0.618），方向与预期相反。B0_raw 在 MAE/ECE 上反而优于 IRT。IRT 的 coverage 极低（C95=0.18），说明不确定性估计不够宽。
2. **gsm8k s1only 2pl**：gamma 很小且 CI 包含零（0.167, [-0.306, 0.636]），无法检测到污染信号。B0_raw 基线 MAE=0.003 已非常好。
3. **SFT 3B d100 s123** 即将完成（90%，~32min），**SFT 0.5B d025 s123** 约 45% 还需 ~55min。
4. **5 个 eval 进程**全部仍在运行，暂无结果。

---
