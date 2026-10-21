# agent / loop_15.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`b3a0e9ee31149d32203c.json`](../../sessions/b3/b3a0e9ee31149d32203c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-16T10:13:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-21977 的 cuda:0~5（共 6 张 RTX 4090D），不得用其他设备
- 3B d000_s42 checkpoint 路径有命名不一致问题：`Qwen2.5-3B_d000_s42/` vs `_a32_`，ROADMAP 提到需 symlink 但尚未完成，eval 时注意指向正确路径
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python ...`
- s4_selfcritique 在 3B MMLU 上 OOM（D091），已降级 P1 不阻塞 critical path，论文用 S1/S2/S3 三信号融合（D098）
- 投稿目标 EMNLP 2026 ARR May 25（距今 9 天），不允许 fallback 思维

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，6× RTX 4090D
- Python：/root/miniconda3/bin/python（conda base 环境）
- 工作目录：/root/autodl-tmp/exp001/（SFT+eval）、/root/autodl-tmp/exp002/signals/（信号计算）
- Checkpoints：/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_{dose}_{seed}/lora_adapter
- Eval 结果：/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_{dose}_{seed}_a32_{format}/
- Logs：~/runs/contamcal-irt-calibration/
- 活跃进程（reconcile 时刻）：
  - exp_001_eval_3B_d005_s42_a32_batch: PID 679180, cuda:2
  - exp_001_eval_3B_d100_s42_a32_batch: PID 687347, GPU 未知
  - exp_002_signals_05B_s123_v2: cuda:5
  - exp_002_signals_15B_s123_batch: PID 691872, cuda:0
  - exp_002_signals_3B_d100_s123_v9: cuda:4, 进程已消失（miss 1/5）

### 3. 📊 当前状态
刚收到 exp_001_eval_3B_d000_s42_a32_batch（3B 0% baseline aligned eval）完成回调，已派 Worker 分析结果（worker_analysis_..._20260516T060402）。
同时 reconcile 发现 exp_002_signals_3B_d100_s123_v9 进程消失，已派诊断 Worker（worker_diagnose_..._20260516T060411）。

**等待中**：
- Worker 回调：analysis worker → 确认 d000_s42 eval metrics，更新 registry 到 DONE
- Worker 回调：diagnose worker → 确认 signals v9 是否需要重跑
- RUNNING：d005_s42_a32_batch eval (cuda:2)、d100_s42_a32_batch eval、signals_05B_s123_v2 (cuda:5)、signals_15B_s123_batch (cuda:0)
- 空闲 GPU：cuda:1、cuda:3（report.md 显示），d000_s42 eval 完成后 cuda:1 释放

### 4. 📋 待办
- analysis worker 回调 success → update report.md + 向 Director 汇报 d000 baseline metrics + 立即提交 exp_001_eval_3B_d000_s42_a32_para_aligned（para eval，填 s42 矩阵下一格）到 cuda:1
- diagnose worker 回调确认 v9 失败 → 在 cuda:4 重跑 exp_002_signals_3B_d100_s123（v10），或修 OOM 后重跑
- cuda:3 空闲 → 提交 exp_001_eval_3B_d005_s42_para_aligned（待 d005 aligned eval 完成后）
- d005_s42 eval (cuda:2) 完成 → 分析 + 提交 d005 para_aligned eval
- d100_s42 eval 完成 → 分析 + 提交 d100 para_aligned eval
- 所有 3B s42 eval+signals 完成 → RRF 聚合（exp-003, CPU）→ pooled IRT fitting（exp-006）
- 0.5B/1.5B s123 signals 完成 → 补全 IRT pool 跨种子数据

### 5. 🎯 战略上下文
- 项目核心：ContamCal = post-hoc 4PL IRT 校准，通过污染增强训练构建 dose-response 曲线
- Critical path：3B s42 eval 矩阵（7/16 cells 完成）→ signals → RRF 聚合 → pooled IRT fitting → paper
- Claim 1（identifiability）已有 sim_sweep_v7 支撑（D090）；Claim 2=60%；Claim 3 靠间接支撑
- 3B 是瓶颈：0.5B/1.5B 矩阵已满，3B s42 矩阵缺大量格子
- d000_s42 是 0% contamination baseline，是所有信号计算的参照点——metrics 异常则整条 s42 链条受影响
- 易踩坑：d000 checkpoint 命名不一致（有/无 _a32_），路径引用时仔细确认；signals v9 连续失败多版本（v3-v8 全挂），可能是 3B d100 s123 信号计算本身有系统性问题（OOM 或数据路径错误）


---
