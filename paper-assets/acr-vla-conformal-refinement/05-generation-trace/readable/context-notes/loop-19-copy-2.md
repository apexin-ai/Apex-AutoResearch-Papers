# agent / loop_19.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`7dc37e5a550c4f859a32.json`](../../sessions/7d/7dc37e5a550c4f859a32.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-17T17:57:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5（共 17 张）。白名单外的 GPU 即使 Director 指令也必须 push back
- K=1 和 K=10 结果不得混比。K=10 作 supplementary evidence，K=1 是正文主线
- CRM checkpoint 路径固定：`/root/autodl-tmp/checkpoints/crm_v3_norm/{perdof,obs_only,scalar_unc}/crm_best.pt`
- 所有 eval 命令必须带 `HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl`
- eval-perdof-object-norm02-seed45 这个数据点已有 2 个运行副本，不要再提交第 3 个

### 2. 🖥️ 基础设施快照
- **bjb2-40593**: 工作目录 `/root/acr-vla-conformal-refinement`, Python via `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **bjb1-18228**: 同上路径和环境。磁盘 400G/438G 可用（4%）
- **bjb1-32546**: 同上。磁盘 400G/438G 可用（4%）
- **bjb2-28827**: 同上。磁盘 399G/439G 可用（5%）
- HF cache: `/root/autodl-tmp/.hf_cache`（所有服务器）
- W&B: 未配置（实验用 JSON output_file 而非 W&B 追踪）
- **活跃 cron 监控 17 个实验**（全部 eval 类型，reconcile_crons 已确认 running）
- **Worker**: `worker_diag_eval-perdof-object-norm02-seed45-deploy_20260517T134920` 正在诊断失败实验（SSH 查日志中），尚未回调

### 3. 📊 当前状态
刚处理 `eval-perdof-object-norm02-seed45-deploy` 失败回调（bjb1-18228, process dead 5× no metrics）。已更新 registry 为 DONE/failed，派 Worker 诊断根因，已汇报 Director。该数据点有 2 个运行副本覆盖，无需重跑。

**RUNNING 实验（17 个，按服务器分组）：**
- bjb2-28827 (5 GPU): eval-scalar-object-seed45, eval-obs-only-object-default-seed45, eval-perdof-object-norm02-seed{44,46,47}, eval-perdof-object-norm02-seed45（原版）
- bjb1-32546 (6 GPU): eval-perdof-object-norm01-seed{46-r2,47-bjb1}, eval-obs-only-object-norm03-seed46, eval-obs-only-object-default-seed46, eval-perdof-object-default-seed46, eval-obs-only-object-norm005-seed43-r2
- bjb1-18228 (~4 GPU): eval-perdof-object-norm02-seed45-r2, eval-obs-only-object-norm005-seed43-r3, eval-obs-only-object-norm02-k5-seed42, eval-obs-only-object-norm02-k20-seed42
- bjb2-40593 (1 GPU): eval-random-selection-object-seed42

**等待中：** Worker 诊断回调；无 Director 决策待回复

### 4. 📋 待办
- Worker 诊断回调到达 → 读结果，更新 failure_reason 到 registry，如发现系统性问题（如 GPU 硬件故障/驱动问题）则汇报 Director
- 任一 eval 实验完成回调 → 按 on-experiment-done 流程处理：提取 success_rate，更新 registry metrics，刷新 report.md，汇报 Director（带 magnitude curve 数据对比）
- bjb2-28827 cuda:1 空闲 → 检查 PREPARING 队列中是否有待跑实验可填入
- 所有 magnitude sweep 数据收齐后 → 汇总 Figure 2 数据（obs_only vs perdof across ε），生成对比表
- K sweep (K=5/K=20) 完成 → 与 K=10 (22%) 对比，验证 sample count 效应
- random-selection baseline 完成 → 与 obs_only/argmin 对比，验证 CRM selection 价值
- D049 MUST-DO plan_700/800 尚未启动 → 当前 eval sweep 有足够数据后应提醒 Director 推进 K=1 CRM 设计和 OpenVLA 适配

### 5. 🎯 战略上下文
- **核心方向 (D049)**：Narrative B+ — obs_only CRM 单步纠正 frozen VLA。三个贡献：K=1 单采样纠正、conditioning-magnitude interaction insight、跨 VLA 验证
- **已锁定结论**：K=10 obs_only 17.5% vs argmin 12.3%, Fisher p=0.0074。Magnitude sweep 显示 obs_only 在各 ε 稳定，perdof 在高 norm 崩塌
- **投稿目标**：CoRL 2026，abstract DDL ~May 26（~9 天），full paper DDL ~Jun 2
- **当前阶段**：仍在收集 magnitude curve 多 seed 数据 + baseline ablation。plan_700 (K=1 CRM) 和 plan_800 (OpenVLA) 是 MUST-DO 但未启动
- **易错点**：
  1. 很多实验 status 停在 PREPARING 但实际已通过 submit_training_job 在跑（cron 能监控但 registry status 不一致）——不要因为 status=PREPARING 就重复提交
  2. bjb1-18228 上同一 GPU 曾发生多实验冲突导致崩溃（本次 deploy 失败可能就是这个原因）——提交前务必确认目标 GPU 无其他进程
  3. 失败实验数量大（29 failed + 59 killed），大部分是早期迭代遗留，不代表当前代码有问题
  4. eval 实验不产 W&B metrics（用 JSON output），cron 检测到 "no W&B" 不一定是真失败，可能只是进程还没写出结果就被 kill 了


---
