# reviewer / loop_5.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`c461cb8bfb04abeac9f1.json`](../../sessions/c4/c461cb8bfb04abeac9f1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-25T03:18:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-10894 gpu_ids 白名单需核实（之前 GPU 0/1/2/3 都在用，但未确认 constraints.yaml 是否存在）
- westd-34685 同上，4 张 GPU 都在用
- **ProcessGroupNCCL 误报**：所有用 torchrun 的实验完成时都会触发 `on_failed` cron（exit_code=1 from destroy_process_group warning）。**不要当真正失败处理**，检查日志确认 "Max step 50005 reached!" 即可
- checkpoint rotation 代码已部署到 finetune.py（save_total_limit=3），但**已启动的进程不会加载新代码**，仍会无限累积 checkpoint

### 2. 🖥️ 基础设施快照
- **westd-10894** (root): `/root/occsafe_vla`，conda env `occsafe`，Python `/root/miniconda3/envs/occsafe/bin/python`
  - Checkpoints: `/root/autodl-tmp/checkpoints/`，磁盘 250G（~50G 可用，81%已用）
  - 训练日志: `/root/runs/occsafe_vla/*.log` 和 `/root/autodl-tmp/logs/*.log`
  - Eval artifacts: `/root/occsafe_vla/artifacts/`
  - **所有 4 GPU 空闲**（3 个训练 + 1 个 eval 刚完成）
  - 已 SCP 到本机：vanilla_retrain_s0 + full_occ_retrain_s0 的 50K checkpoint（用于梯度分析）
  - 中间 checkpoint（full_occ_ln_s1/s2 + ablation_detach_retrain 各 20K/40K = 90G）**建议清理但尚未执行**

- **westd-34685** (root): `/root/occsafe_vla`，同上 conda env
  - Checkpoints: `/root/autodl-tmp/checkpoints/`，磁盘 350G（~91G 可用，74%已用）
  - 训练日志: `/root/occsafe_vla/logs/*.log` 和 `/root/runs/occsafe_vla/*.log`
  - cutoff_15k_s1 中间 checkpoint（10K/20K/30K/40K = 60G）**急需清理**
  - GPU 0: cutoff_45k_s1 (29%, ~9h)；GPU 1: 空闲；GPU 2: cutoff_25k_s2 (63%)；GPU 3: reverse_cutoff_s2 (63%)

### 3. 📊 当前状态
**刚完成的实验**（全部 false-positive "failed"，实际成功）：
- ablation_occ_detach_s0_retrain → eval 完成：TSR=0.944, CAR=0.754
- cutoff_15k_s1 → eval 待提交（50K checkpoint 已就绪）
- full_occ_ln_s1 → eval 完成：TSR=0.894, CAR=0.718
- full_occ_ln_s2 → eval 完成：TSR=0.866, CAR=0.744
- CKA full_occ_ln_s1 完成：DINOv2=0.965（s0 的 0.640 drift 未复现，是 outlier）

**仍在 RUNNING（westd-34685）**：
- cutoff_45k_s1_resume: step ~14.4K/50K (29%), GPU 0, ~9h
- cutoff_25k_s2: step ~31.4K/50K (63%), GPU 2, ~5h
- reverse_cutoff_s2: step ~31.3K/50K (63%), GPU 3, ~5h

**等待中**：
- cutoff_15k_s1 eval 需提交（已通知 Director）
- full_occ_ln_s2 CKA 分析（确认 s0 CKA outlier）
- 磁盘清理（两台服务器均已通知 Director，尚未执行）

### 4. 📋 待办（条件触发式）
- cutoff_15k_s1 eval 结果出来 → 核实 dose-response 数据点（15K cutoff CAR 对比 25K/45K）
- full_occ_ln_s2 CKA 结果出来 → 如 DINOv2 CKA ~0.96 则确认 s0 是 outlier；如 CKA 低则重新审视 crossover 假说
- cutoff_25k_s2 / reverse_cutoff_s2 完成 → 提交 eval，核实 3rd seed dose-response + withdrawal 效应
- cutoff_45k_s1 完成 → 提交 eval，完成 dose-response 曲线 s1 数据
- 磁盘清理未执行 → 再次催 Director，westd-34685 margin 仅 ~91G 且 3 个实验还在写 checkpoint

### 5. 🎯 战略上下文
- **Venue**: CoRL 2026，Abstract 5/26（明天），Paper 5/29
- **核心叙事**: Dual mechanism — BN interference (1.9pp) + gradient flow absence (1.5pp)
- **2×2 factorial 关键结果**: Full OCC+LN 3 种子 CAR 均值 0.743，比 Full OCC BN (~0.797) 低 5.4pp。BN 在 gradient flow 下优于 LN（行为层面一致）
- **CKA crossover 已被推翻**: s0 DINOv2 CKA=0.640 是 seed-specific outlier，s1 CKA=0.965 正常。我之前推荐的 "BN coupling context-dependent" 叙事调整**已撤回**
- **表征-行为解耦**: s1 CKA 最高(0.965)但 CAR 最低(0.718)；s0 CKA 最低(0.640)但 CAR 最高(0.766)。CKA 不预测 CAR
- **统计显著性**: 目前只有 Detach+BN (p=0.031) 和 Reverse Cutoff (p=0.031) 显著不同于 Vanilla。其他条件需 3 种子完整后重算
- **易错点**: (1) 不要把 ProcessGroupNCCL 的 on_failed cron 当真正失败 (2) 不要重新提出 CKA crossover 假说——已被 s1 数据否定 (3) westd-34685 磁盘随时可能再次爆满


---
