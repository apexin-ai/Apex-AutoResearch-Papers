# agent / loop_7.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`3c1af588988f67bc17c5.json`](../../sessions/3c/3c1af588988f67bc17c5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-14T23:12:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0-5 on cqa1-21977，无其他服务器/GPU 可用
- Pooled IRT 只能用同源 signal-derived delta exposure（D027/D028）。**绝对不能**混 signal-derived exposure 和 oracle dosage fallback 到同一 IRT fit
- 3B GSM8K 必须从所有 IRT 分析中排除（D018）——theta=-4.98 是 LoRA 超参损伤，不是 contamination
- 3B SFT 必须用 D020 保守超参: lr=5e-5, lora_alpha=16, r=16。0.5B/1.5B 用 lr=2e-4, alpha=32, r=16。seed=123 同 scale 必须与 seed=42 超参一致
- S3 ConStat 已废弃（D030），论文只报 3-signal RRF（S1 embedding + S2 Min-K++ + S4 SelfCritique）
- 所有 eval/训练提交命令必须带 `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...`
- Signal-derived exposure 必须 baseline-subtract（减 d000 baseline signal 并 clip≥0），否则 gamma 不可识别

### 2. 🖥️ 基础设施快照
- 服务器: **cqa1-21977**, 6× RTX 4090D
- 工作目录: `/root/contamcal-irt-calibration`
- Python: `/root/miniconda3/bin/python`（conda base 环境，**不是 venv**）
- HF cache: `/root/autodl-tmp/.hf_cache`
- SFT checkpoints: `/root/autodl-tmp/exp001/checkpoints/`
- 活跃 GPU 进程:
  - GPU 0: exp_001_eval_3B_d000_v2_para_aligned (PID 450055, tmux: eval_3B_d000_v2_para)
  - GPU 1: exp_001_eval_05B_d100_s123_aligned (PID 444836)
  - GPU 2: exp_001_sft_15B_d100_s123 (PID 435415)
  - GPU 3: exp_001_sft_d100_3B_v2 (PID 420195)
  - GPU 4: exp_001_eval_3B_d000_v2_aligned (PID 441570)
  - GPU 5: exp_001_sft_3B_d000_s123 (PID 435971)
- CPU 进程（local）:
  - exp_004_sim_sweep_v3: PID 599562, 54/120 IRT parameter recovery fits
  - exp_005_noise_prop_v4: PID 617670, 23/25 noise propagation fits
- 本 session 无 active crons（reconcile 返回 0）

### 3. 📊 当前状态
**刚做完**: D033 pooled IRT 审计（发现 6 个严重问题），joint_fit.py exclude_rules 死代码修复（方案A），exp-004/005 registry 清理，pooled IRT GSM8K/ARC/MMLU v2 结果出炉。

**正在做（6 个 running workers）**:
1. `worker_fix_exp006_rrf_exposure` + `worker_code_exp_006_rrf_fix` — 修复 exp006 RRF exposure 代码（D033 审计发现的问题）
2. `worker_analysis_exp005-v4-wrapup` — exp005 noise propagation 分析收尾
3. `worker_diag_gsm8k-v2-v3-rootcause` — GSM8K pooled IRT v2/v3 差异根因诊断
4. `worker_diag_coverage-wider-priors` — coverage wider priors 诊断
5. `worker_ops_cpu_exp005_v4_restart` — exp005 v4 CPU 进程跟踪

**RUNNING 实验 8 个**（6 GPU 满载 + 2 CPU），详见 §2。

**等待中**: 上述 6 个 worker 回调；GPU 训练完成的 cron 回调（SFT runs 预计数小时）。

### 4. 📋 待办（条件触发式）
- exp006 RRF fix workers 完成 → 用修复后的代码重跑 0.5B+1.5B pooled IRT（3-signal RRF exposure, delta-subtracted）→ 这是 Paper Table 1 的关键数据
- 3B d100 v2 SFT (GPU 3) 完成 → 提交 3B d100 eval（aligned + para_aligned）→ 填补 3B dose-response 曲线
- 3B d000 v2 aligned eval (GPU 4) 完成 → 检查 GSM8K 是否恢复（target ≥50%，v1 仅 11.7%）→ 若恢复则 D018 排除规则仅限 v1
- 3B d000 v2 para_aligned eval (GPU 0) 完成 → 计算 3B d000 baseline gap → 完成 delta-of-deltas 分析
- 1.5B d100 s123 SFT (GPU 2) 完成 → 提交 s123 eval → 增加 pooled IRT N_models
- 3B d000 s123 SFT (GPU 5) 完成 → 提交 s123 eval
- 0.5B d100 s123 eval (GPU 1) 完成 → 收集 signals → 加入 multi-seed pool
- exp_004 sim sweep (54/120) 完成 → 汇总 parameter recovery 结果，确认 4PL+γ 可识别性
- exp_005 noise prop (23/25) 完成 → 汇总 noise propagation 结果，量化 signal uncertainty 对 gamma 的影响
- 所有 seed=123 eval 完成 → 重跑 pooled IRT with N≥20 models → gamma 显著性检验

### 5. 🎯 战略上下文
**投稿目标**: EMNLP 2026 ARR May 25（距今 11 天）。MVP 已通过。

**核心 narrative**: ContamCal = post-hoc statistical calibration via contamination-augmented 4PL IRT。
- 关键发现: contamination effects are scale-dependent（0.5B 退化, 1.5B 免疫）→ standard accuracy metrics blind at ≥1.5B → IRT gamma 能捕捉 accuracy 看不到的 contamination signal
- ARC 0.5B gamma=-1.87（负方向，显著）= 小模型被 contamination SFT 伤害
- GSM8K gamma=0.508 但 CI 含 0（N=4 不够）→ multi-seed + cross-scale pooling 是提升功效的唯一路径

**最容易判断错的事**:
1. **Pooled IRT exposure 来源**: 必须全部用 signal-derived delta exposure，不能有任何 oracle dosage fallback。上一轮 exp_006_pooled_gsm8k_v1 就是混了 fallback 导致 gamma=2.14 无效（D027）
2. **S2 Min-K++ 极性反转**: higher = less memorized，RRF 融合时需 flip。忘了 flip 会反转 exposure 方向
3. **3B 超参不能用 0.5B/1.5B 的**: 3B 用 lr=5e-5/alpha=16 是因为旧参数导致 GSM8K catastrophic forgetting。新 session 容易想当然用统一超参
4. **PREPARING 实验大部分是历史残留**: exp_001_eval_05B_d000_s42_v2/v3/v4/v6 等都是早期失败版本，不要试图重提交这些。关注当前 RUNNING 的 8 个实验和它们的后续
5. **D033 审计的 6 个问题还在修中**: worker_fix_exp006_rrf_exposure 和 worker_code_exp_006_rrf_fix 正在修。修完前不要跑新的 pooled IRT


---
