# agent / loop_14.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`c77412ad20007c64773d.json`](../../sessions/c7/c77412ad20007c64773d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-16T03:35:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: cuda:0~5 on cqa1-21977，共 6× RTX 4090D。无其他服务器/GPU 可用
- **Alpha 必须 32**: 所有 checkpoint 必须 alpha=32 + lr=5e-5。alpha=16 或 lr=2e-4 的 checkpoint 及其下游 eval/signals **全部作废**（D074-D076 教训）
- **投稿死线 EMNLP 2026 ARR May 25**（距今 9 天），所有调度决策以此为锚
- **D034**: Signal pipeline 用 S1-only 即可（S4 selfcritique 3B MMLU OOM 降级 P1，不阻塞 critical path）
- **D098**: 论文采用 s1+s2+s4 three-signal fusion，s3_constat 不批
- **D095**: Claim 3 降级为 Claim 1 Discussion 中的 honest negative（noise_prop negative），不单独撑 claim
- **cuda:0 历史违规**: 曾双进程冲突（C001），释放后严禁再同时跑两个 GPU 密集任务

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977，6× RTX 4090D (24GB each)
- **工作目录**: `/root/contamcal-irt-calibration`
- **Python**: `/root/miniconda3/bin/python`，环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型基座**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B,1.5B,3B}`
- **Checkpoints**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{size}_{dose}_{seed}/lora_adapter`
- **Eval 结果**: `/root/autodl-tmp/exp001/eval_results/`
- **Signals 输出**: `/root/autodl-tmp/exp002/signals/`
- **Paraphrases**: `/root/autodl-tmp/exp001/paraphrases/`
- **活跃进程（reconcile 确认）**:
  - `exp_001_eval_3B_d000_s42_a32_batch` — PID 676487, cuda:1, tmux session, cron 监控中
  - `exp_001_eval_3B_d005_s42_a32_batch` — PID 679180, cuda:2, tmux session, cron 监控中
  - `exp_001_eval_3B_d100_s42_a32_batch` — cuda:3（registry RUNNING，cron 未覆盖，需确认进程状态）
  - `exp_002_signals_05B_s123_v2` — cuda:5, tmux=exp002_05B_s123_v2（registry RUNNING，cron 未覆盖，需确认）

### 3. 📊 当前状态

**刚完成的关键事项**:
- sim_sweep_v7 完成 9/12 条件，Claim 1 identifiability 充分支撑（D090）
- D076 lr confound 修复：d000_s42 重训完成，d005_s42/d025_s42_v3/d100_s42_a32_v3 在跑
- exp_001_eval_3B_d100_s123_a32_batch 成功完成（s123 aligned + para_aligned）
- 1.5B 双种子矩阵 16/16 全部就绪

**RUNNING (4)**:
| exp_id | GPU | 内容 |
|--------|-----|------|
| exp_001_eval_3B_d000_s42_a32_batch | cuda:1 | d000 s42 aligned+para eval（填 3B s42 矩阵 2 格）|
| exp_001_eval_3B_d005_s42_a32_batch | cuda:2 | d005 s42 aligned+para eval（填 3B s42 矩阵 2 格）|
| exp_001_eval_3B_d100_s42_a32_batch | cuda:3 | d100 s42 aligned+para eval（填 3B s42 矩阵 2 格）|
| exp_002_signals_05B_s123_v2 | cuda:5 | 0.5B s123 全部 signals (s1+s2+s4) |

**IRT Pool 现状**: N=35（含 0.5B）/ N=23（不含 0.5B）。3B 是瓶颈：aligned 4/8, para_aligned 3/8。上述 3 个 eval 完成后可推至 aligned 7/8, para_aligned 6/8。

**⚠️ 注意**: cuda:0 和 cuda:4 当前状态不明——ROADMAP 记录 cuda:0 跑 SFT d005_s42 + eval d100_s123，cuda:4 跑 d000_s42 eval，但 reconcile 只返回了 2 个 cron。新 session 应 SSH 确认 cuda:0/4 实际进程。

**PREPARING (24)**: 大量 eval/SFT 排队等 GPU 释放。

### 4. 📋 待办（条件触发式）
- **d000_s42 eval (cuda:1) 完成** → 更新 registry + 3B aligned 矩阵新增 1 格。立即提交下一优先任务（d025_s42 para_aligned 或 signals）
- **d005_s42 eval (cuda:2) 完成** → 同上。若 SFT d005_s42 已完成，此 eval 填 2 格（aligned + para）
- **d100_s42 eval (cuda:3) 完成** → 3B s42 d100 填满。GPU 释放后优先 signals 计算
- **0.5B s123 signals (cuda:5) 完成** → 检查 12 个 signal 文件完整性，更新 signal pipeline 状态
- **3B s42 eval 全部完成（7-8/8 aligned）** → 立即启动 3B signals 计算（前置条件满足）
- **3B signals 全完成** → RRF 聚合 (exp-003, CPU)，然后 pooled IRT fitting (exp-006)
- **IRT fitting 完成** → 7 baselines 对比 + ablation，Paper Agent 启动写作 pipeline
- **cuda:0/4 空闲确认** → 按优先级分配：3B s42 缺失 eval > signals > 1.5B s123 signals
- **任何 GPU 释放** → 检查 PREPARING 队列，按 critical path 优先级提交下一任务

### 5. 🎯 战略上下文

**项目核心**: ContamCal — 通过 contamination-augmented 4PL IRT 做 post-hoc 统计校准。3 个 Claims：
- **Claim 1** (identifiability): sim_sweep_v7 已充分支撑（gamma bias <0.03, CI95 coverage ≥0.8）
- **Claim 2** (calibration quality): 60% coverage，需更多 3B eval 数据点
- **Claim 3** (noise robustness): **降级为 Discussion honest negative**（D095），noise_prop_v4 negative，sim_sweep 提供间接支撑

**Critical path 瓶颈**: 3B s42 eval 矩阵。当前 4 个 RUNNING 实验全部是填这个矩阵。完成后才能做 3B signals → RRF → IRT fitting → paper。

**易踩的坑**:
- **Checkpoint 命名不一致**: d000_s42 路径是 `Qwen2.5-3B_d000_s42/` 但有的地方带 `_a32_`，ROADMAP 提到需 symlink 统一（指令已发但未确认执行）
- **不要用旧 checkpoint**: 任何没有 alpha=32 + lr=5e-5 的 3B checkpoint 都是废的（D076）
- **sim_sweep auc0.65 ×3 永远失败**: CmdStan 在低 signal quality 下有文件竞态问题，已放弃不重试（9/12 足够）
- **s4 selfcritique 3B MMLU OOM**: 已降级 P1（D091），论文用 0.5B/1.5B 完整 s4 + 3B S1/S2/S3
- **coverage collapse 是 model misspecification**: 不是 γ 值大导致，是 additive 4PL+γ 与真实 contamination 机制的 mismatch。论文应强调 benchmark-dependent effects
- **Dose-response 分层**: GSM8K 对 contamination 极敏感（3B +34pp@25%），MMLU/ARC 几乎不敏感——这支持 per-benchmark γ_k 参数化


---
