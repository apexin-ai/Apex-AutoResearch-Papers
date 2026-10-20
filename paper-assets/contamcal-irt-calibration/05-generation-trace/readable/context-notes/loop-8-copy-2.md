# agent / loop_8.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`4ec0ced6ff97e2a2cc73.json`](../../sessions/4e/4ec0ced6ff97e2a2cc73.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T02:41:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0~5 (cqa1-21977)，全部已分配给本项目，但必须通过 `load_project_config` 确认再用
- Pooled IRT 禁止混用 signal-derived exposure 和 oracle dosage（D026 红线，违规案例 exp_006_pooled_gsm8k_v1）
- 3B d000 GSM8K=12% 是 LoRA 超参损伤，必须从所有 IRT 分析中排除（D018）
- seed=123 超参必须与同 scale 的 seed=42 完全一致（3B: lr=5e-5, alpha=16, r=16；0.5B/1.5B: lr=2e-4, alpha=32, r=16）
- per-model exposure 只用 S1-only 或 oracle dosage，禁止 RRF per-model mean（非单调，已审计确认）
- eval/训练提交命令前缀必须带 `source /etc/network_turbo`，否则 HF 数据加载超时
- CmdStan 在 cqa1-21977 有 nproc limit，parallel_chains 必须设为 1（不是默认 4）

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977, 6× RTX 4090D
- **工作目录**: /root/contamcal-irt-calibration
- **Python**: /root/miniconda3/bin/python（conda base 环境，非 venv）
- **激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型缓存**: /root/autodl-tmp/.hf_cache (Qwen2.5-0.5B, 1.5B, 3B)
- **SFT checkpoints**: /root/autodl-tmp/exp001/checkpoints/
- **Eval 结果**: /root/autodl-tmp/exp001/eval_results/
- **IRT 结果**: /root/autodl-tmp/exp006/
- **Signal 数据**: /root/autodl-tmp/exp002/signals
- **W&B**: 未配置（指标通过 log 文件和 registry 追踪）
- **活跃进程**:
  - PID 466755: exp_001_sft_d025_3B_v2 (SFT, GPU 3)
  - PID 471296: exp_001_sft_3B_d100_s123 (SFT, GPU 5)
  - PID 473954: exp_001_eval_15B_d100_s123_aligned (eval, GPU 2)
  - PID 475651: exp_001_eval_05B_d005_s123_aligned (eval, GPU 1)
  - PID 477489: exp_001_eval_3B_d100_v2_aligned_v2 (eval, GPU 0)
  - PID 481020: exp006-pooled-s1only-gsm8k-v2 (IRT CPU)
  - PID 481167: exp006-oracle-gsm8k-extended-v2 (IRT CPU)
  - PID 652931: exp_004_sim_sweep_v4 (simulation CPU)
- **Cron 监控**: 5 个活跃 cron（exp_001_sft_d025_3B_v2, exp_001_sft_3B_d100_s123, exp_001_eval_15B_d100_s123_aligned, exp_001_eval_05B_d005_s123_aligned, exp_001_eval_3B_d100_v2_aligned_v2）
- **活跃 Worker**: 1 个（worker_eval_exp_001_eval_05B_d005_s123_para_aligned）

### 3. 📊 当前状态
**刚做完**: D036 分析——ARC negative gamma 确认（4 条独立证据），coverage collapse 根因确认为 N 不足（N=16 时 C95=1.00）。论文 framing 调整方向已定：ARC 作为 discriminative validity case study，benchmark-dependent effects。

**正在跑 (8 RUNNING)**:
- 2 个 SFT: 3B d025 v2 (seed=42, GPU 3) + 3B d100 s123 (seed=123, GPU 5)
- 3 个 eval: 3B d100 v2 (GPU 0) + 0.5B d005 s123 (GPU 1) + 1.5B d100 s123 (GPU 2)
- 2 个 CPU IRT: pooled-s1only-gsm8k-v2 (已有 metrics: gamma=0.12, CI含0, PPP=0.334) + oracle-gsm8k-extended-v2
- 1 个 CPU sim: exp_004_sim_sweep_v4 (~45%)

**ANALYZING**: exp_001_sft_3B_d000_s123 — 3B baseline seed=123 SFT 完成，需要 spawn Worker 验证 checkpoint 并启动 eval。

**等待中**:
- Worker 回调: worker_eval_exp_001_eval_05B_d005_s123_para_aligned（正在执行 0.5B d005 s123 paraphrase aligned eval）
- Cron 回调: 5 个实验的完成通知
- PREPARING 队列: 15 个实验（多数是历史重试残留，实际需要关注的: exp_008_instruct_rl_proxy, exp_003_mmlu_item_aligned_gap, exp_006_irt_05B_v2）

### 4. 📋 待办（条件触发式）
- exp_001_sft_3B_d000_s123 ANALYZING → spawn Worker 验证 checkpoint → 提交 eval（3B d000 s123 aligned，需 GPU，等当前 eval 完成释放）
- exp_001_eval_3B_d100_v2_aligned_v2 完成 → 收集 metrics → 更新 registry → 3B d100 加入 pooled IRT 分析
- exp_001_eval_05B_d005_s123_aligned 完成 → 收集 metrics → 与 seed=42 d005 对比 → 跨种子方差分析
- exp_001_eval_15B_d100_s123_aligned 完成 → 1.5B d100 s123 加入 cross-seed analysis
- exp_001_sft_d025_3B_v2 完成 → 提交 eval → 填充 SFT 矩阵 3B d025 格
- exp_001_sft_3B_d100_s123 完成 → 提交 eval → 3B d100 s123 → multi-seed pooling 关键数据点
- seed=123 所有 eval 完成 → N≥16 multi-seed pooled IRT 重跑 → 验证 coverage 改善
- exp006-pooled-s1only-gsm8k-v2 完成 → 已有初步 metrics (gamma=0.12)，需最终确认 convergence
- exp_004_sim_sweep_v4 完成 → coverage 诊断数据，对比 N=8 vs N=16 coverage
- GPU 空出后 → 优先: exp_001_sft_3B_d000_s123 的 eval、0.5B d025 SFT（矩阵缺失格）

### 5. 🎯 战略上下文
**投稿目标**: EMNLP 2026 ARR May 25，距今 10 天。

**核心结论链**:
- D035: Oracle baseline 确认 benchmark-dependent contamination effects（GSM8K gamma>0 正向，ARC gamma<0 负向）
- D036: ARC negative gamma 有 4 条独立证据，不再尝试翻转。Coverage collapse 根因是 N 不足，N=16 时恢复正常
- D034: Exposure 切回 S1-only，RRF fusion 废弃作为 per-model exposure
- D030: S3 ConStat 弃用，只报 3-signal（实际 S1 是核心）

**论文 story**: ContamCal 方法通过 4PL+gamma IRT 做 post-hoc calibration。GSM8K 检出正向 contamination effect，ARC 检出负向（discriminative validity）。Multi-seed pooling 解决小 N coverage 问题。

**易错点**:
1. **不要把 pooled-s1only-gsm8k-v2 的 gamma=0.12 当最终结论** — 它还在 RUNNING，且 CI 含 0，需要 N≥16 multi-seed 后才有统计功效
2. **PREPARING 队列有大量历史残留**（v2/v3/v4/v6 重试），不要盲目提交——先确认哪些已被更新版本替代
3. **exp_001_sft_3B_d000_s123 是 ANALYZING 不是 DONE** — 必须先验证 checkpoint 再标 DONE，上次有 Worker 误报 v1 结果为 v2 的事故（D036 教训）
4. **CmdStan parallel_chains 必须设 1** — cqa1-21977 有 nproc limit，parallel_chains=4 会在 55-65% 时被 kill
5. **3B 模型用保守超参**（lr=5e-5, alpha=16），不要用 0.5B/1.5B 的参数（lr=2e-4, alpha=32），否则 GSM8K 从 70% 暴跌到 30%
6. **时间紧迫但不要 fallback** — 10 天内需要完成: seed=123 SFT+eval → multi-seed pooled IRT → paper writing。关键路径是 seed=123 SFT 完成


---
