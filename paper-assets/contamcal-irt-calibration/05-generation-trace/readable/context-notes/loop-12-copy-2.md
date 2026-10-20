# agent / loop_12.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`88cccf8708e56bbd9c39.json`](../../sessions/88/88cccf8708e56bbd9c39.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-15T21:19:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0-5 on cqa1-21977，共 6× RTX 4090D，全项目独占
- **Alpha 混用禁令（D055）**：s42 alpha=32 与 s123 alpha=16 数据**不可混用引用**。IRT pooling 只纳入 alpha=32 checkpoint
- **lr confound（D074-D076）**：旧 s42 系列 d000+d005 用了 lr=2e-4（其他全 lr=5e-5），已废弃，d000_s42_a32 正在重训
- **0.5B 已从 IRT pooling 排除**——不参与 N 计数，仅记录
- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，**不存在 .venv**
- AutoDL 必须 `source /etc/network_turbo` 开代理，`HF_HOME=/root/autodl-tmp/.hf_cache`

### 2. 🖥️ 基础设施快照
- **服务器**：cqa1-21977（AutoDL），工作目录 `/root/contamcal-irt-calibration`
- **Python**：`/root/miniconda3/bin/python`（conda base env）
- **模型**：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B,1.5B,3B}`
- **数据**：`/root/autodl-tmp/exp001/sft_data/sft_dosage_{000,005,025,100}.jsonl`
- **Checkpoints**：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{size}_{dose}_{seed}/lora_adapter`
- **Eval results**：`/root/autodl-tmp/exp001/eval_results/`
- **Signals**：`/root/autodl-tmp/exp002/signals/`
- **W&B**：未配置（metrics 从 SSH 日志和 eval_results.json 读取）
- **活跃进程**：
  - PID 594489 — `exp_001_sft_3B_d100_s123_a32_v2` (cuda:0, tmux)
  - PID 628663 — `exp_001_sft_3B_d100_s42_a32_v3` (cuda:1, tmux)
  - PID 623480 — `exp_001_eval_3B_d005_s123_gsm8k` (cuda:2, tmux)
  - PID 627600 — `exp_001_eval_15B_s123_para_aligned_batch` (cuda:3, tmux)
  - PID 623826 — `exp_002_signals_3B_v5` (cuda:4, tmux) — d025+d100 signals
  - PID 633036 — `exp_001_sft_3B_d000_s42_a32` (cuda:5, tmux)
  - sim_sweep_v7 — CPU/local，补跑 4 failed conditions
- **活跃 Workers**：
  - `worker_code_d081-fix-lora-alpha-bug` — 修 train_sft.py lora_alpha bug
  - `worker_run_d025_v3_signals_all` — d025 v3 signals 全量计算
- **Cron 监控**：5 个 cron 跟踪上述 5 个 GPU 实验（reconcile 确认全部 still running）

### 3. 📊 当前状态
**刚做完**：D074-D082 一系列决策——发现 s42 lr confound + alpha 混用问题，废弃旧数据，启动 alpha=32 统一重训。d025_v3 SFT 刚完成（success），正在跑其 signals。

**7 个实验 RUNNING**（6 GPU + 1 CPU）：
1. `exp_001_sft_3B_d100_s123_a32_v2` — cuda:0, 3B d100 s123 SFT（最早启动，可能接近完成）
2. `exp_001_sft_3B_d100_s42_a32_v3` — cuda:1, 3B d100 s42 SFT v3（v2 被 SIGTERM@73%）
3. `exp_001_eval_3B_d005_s123_gsm8k` — cuda:2, GSM8K 单 benchmark 补跑
4. `exp_001_eval_15B_s123_para_aligned_batch` — cuda:3, 1.5B s123 para_aligned 4-dose batch eval
5. `exp_002_signals_3B_v5` — cuda:4, 3B d025+d100 signals
6. `exp_001_sft_3B_d000_s42_a32` — cuda:5, 3B d000 s42 重训
7. `exp_004_sim_sweep_v7` — CPU, simulation sweep 补跑

**等待中**：
- 2 个 Worker 回调（d081 lora fix + d025_v3 signals）
- 5 个 Cron 回调（上述 GPU 实验完成时触发）
- ~13 个 PREPARING 实验排队等 GPU 释放

### 4. 📋 待办（条件触发式）
- **d100_s123_a32_v2 完成 → cuda:0 释放** → 提交 `exp_001_sft_3B_d100_s123_a32`（注意：这个已经是 v2，完成后 cuda:0 给 3B d005_s42 a32 SFT 或 3B signals）
- **d100_s42_a32_v3 完成 → cuda:1 释放** → 提交 `exp_001_sft_3B_d005_s42_a32`（D076 retrain）
- **d005_s123_gsm8k eval 完成 → cuda:2 释放** → 提交 exp-002 3B d005 signals（critical path for Claim 2）
- **15B s123 para_aligned batch 完成 → cuda:3 释放** → N 从 19→23，提交 3B d005/d100 signals 或 eval
- **signals_3B_v5 完成 → cuda:4 释放** → 继续 3B d005/d100 signals（剩余 dosage levels）
- **d000_s42_a32 SFT 完成 → cuda:5 释放** → 跑 d000_s42 eval（aligned + para_aligned）
- **sim_sweep_v7 完成** → 若 success，identifiability boundary 确认，入 paper；若 fail，需根因分析（v1-v6 连续失败）
- **Worker d081 lora fix 完成** → 验证 train_sft.py 修复，确认后续 SFT 不受影响
- **所有 3B alpha=32 SFT + eval 完成** → 编译 N≥16 pooled IRT 输入 → 启动 exp-006 pooled IRT fitting
- **3B signals 全完成** → RRF 聚合 (exp-003) → per-benchmark exposure scores
- **noise_prop_v4 negative 已确认** → Claim 3 需 Director 决策（降级 future work or 换路径），**不要自行重试 ME model**

### 5. 🎯 战略上下文
**项目**：ContamCal——用 contamination-augmented 4PL IRT 做 post-hoc statistical calibration，检测和校正 benchmark contamination。

**投稿目标**：EMNLP 2026 ARR May 25（T-10 天），时间极紧。

**核心决策链**：
- D050: alpha=32 统一 | D051: s123 alpha=16 可接受（历史数据，不重跑）
- D053: 废弃联合 IRT，改 per-benchmark IRT
- D055: alpha 重跑（d025_s42, d100_s42, d100_s123 必须 alpha=32）
- D056: coverage collapse = model misspecification（4PL+γ additive 模型的 fundamental 问题）
- D073: Claim 3 ME model negative，降级为 appendix
- D074-D076: s42 lr confound，废弃旧 d000_s42/d005_s42

**Critical Path**：3B signals（Claim 2 瓶颈）→ RRF 聚合 → pooled IRT fitting → paper writing

**易错点**：
1. **不要把 alpha=16 的 eval 结果纳入 IRT pooling**——memory.md 有完整 alpha 分布表，严格按 alpha=32 筛选
2. **d000_s42 有两个版本**：原始 d000（alpha=32✅）和 d000_v2（alpha=16❌弃用），注意区分 checkpoint 路径
3. **GSM8K anomaly**：3B d000 s42 para_aligned GSM8K=4.8%（aligned ~18%），疑 CoT 提取 bug，不阻塞但需标注
4. **PPP=0 风险**：即使 oracle 数据 PPP 仍为 0，per-benchmark IRT 是修复路径，若仍为 0 则 Claim 4 需降级
5. **sim_sweep v1-v6 连续失败**：v7 用了 per-worker tmpdir 隔离修复 pymp race condition，如果还失败就不是 tmpdir 问题了
6. **1.5B 对 contamination 几乎不敏感**（仅 HumanEval 有反应），3B 才有明显 dose-response——论文应强调 scale-dependent effects


---
