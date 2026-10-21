# agent / loop_11.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`9b781ba60fc16e7a6477.json`](../../sessions/9b/9b781ba60fc16e7a6477.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-15T18:10:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器只有 **cqa1-21977**，GPU 白名单 **cuda:0–5**（6× RTX 4090D）
- LoRA **alpha=32** 是全项目标准（D050/D055）。d000_v2 checkpoint（alpha=16）已弃用，禁止引用
- 3B d025_s42 / d100_s42 / d100_s123 的旧 alpha=16 SFT 结果**不可用于论文**，必须等 v3/a32 版本完成
- exp_001_sft_3B_d100_s42_a32（PID 593745）在 cron 中显示 running 但 registry 标记 failed——下一个 session **必须先诊断这个矛盾**，可能是僵尸进程占 GPU
- 投稿目标 **EMNLP 2026 ARR May 25**，距今 10 天

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977 | 工作目录 `/root/contamcal-irt-calibration` | 数据盘 `/root/autodl-tmp/`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- **激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型缓存**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B,1.5B,3B}`
- **SFT checkpoints**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{SIZE}_{DOSE}_{SEED}/lora_adapter`
- **Eval 结果**: `/root/autodl-tmp/exp001/eval_results/`
- **W&B**: 未在 config 中看到专门配置，需要 Worker 确认
- **活跃进程**:
  - PID 594489 — exp_001_sft_3B_d100_s123_a32_v2 (cuda:0)
  - PID 593740 — exp_001_sft_3B_d100_s42_a32_v2 (cuda:1)
  - PID 580693 — exp_001_eval_3B_d005_s123_aligned (cuda:2)
  - PID 597174 — exp_001_sft_3B_d000_v3 (cuda:4)
  - PID 589763 — exp_001_sft_d025_3B_v3 (cuda:5)
  - PID 593745 — exp_001_sft_3B_d100_s42_a32 (⚠️ 见红线，registry=failed 但 cron=running)
  - PID 528993 — exp_004_sim_sweep_extreme_gamma (CPU, simulation)
- **空闲 GPU**: cuda:3（确认空闲），cuda:5 可能被 d025_v3 占用（report 显示 "?" 但 memory.md 说 cuda:5）

### 3. 📊 当前状态
**刚做完**: D055 alpha=32 重跑批次提交（3 个 3B SFT），d000_v3 已提交 cuda:4。exp_005_noise_prop_v4 完成（negative，降级 appendix）。exp_002_signals_3B_v2 被 kill（D057 GPU 冲突）。

**Registry 概览**: 167 实验 — RUNNING 6, ANALYZING 1, PREPARING 20, DONE 140（success 100, failed 34, negative 2, killed 4）

**RUNNING GPU 实验**:
| Exp | GPU | 说明 |
|-----|-----|------|
| exp_001_sft_3B_d100_s123_a32_v2 | cuda:0 | D055 alpha=32 重跑 |
| exp_001_sft_3B_d100_s42_a32_v2 | cuda:1 | D055 alpha=32 重跑 |
| exp_001_eval_3B_d005_s123_aligned | cuda:2 | 3B d005 s123 aligned eval |
| exp_001_sft_3B_d000_v3 | cuda:4 | 3B d000 s42 alpha=32 baseline |
| exp_001_sft_d025_3B_v3 | cuda:5 | D055 alpha=32 重跑 |

**CPU**: exp_004_sim_sweep_extreme_gamma（simulation，验证 extreme γ 下 coverage）

**等待中**: 0 个 Worker 在跑。无 pending Director 决策。20 个 PREPARING 实验排队。

### 4. 📋 待办（条件触发式）
- **exp_001_sft_3B_d100_s42_a32 状态矛盾** → 立即 SSH 检查 PID 593745 存活状态；如已死则确认 registry failed + 清理 cron；如活着则更新 registry 为 RUNNING
- **任一 3B SFT（d025_v3 / d100_s42_v2 / d100_s123_v2 / d000_v3）完成** → spawn worker 提交对应 eval（aligned + para_aligned 两轮），命令模板见 memory.md
- **exp_001_eval_3B_d005_s123_aligned 完成** → 接着提交 para_aligned eval（同 checkpoint，加 --paraphrase-dir）
- **d025_v3 eval 完成** → 提交 exp_001_sft_3B_d025_s42_a32 的排队 eval
- **所有 3B alpha=32 SFT+eval 完成** → spawn worker 跑 exp_002_signals_3B_v3（信号计算），然后 multi-seed pooled IRT（exp_006）检查 coverage 是否改善
- **exp_004_sim_sweep_extreme_gamma 完成** → 分析 extreme γ 下 coverage，更新 D056 结论
- **GPU 空出** → 优先级：(1) exp_001_sft_3B_d025_s42_a32 (2) exp_001_sft_3B_d100_s123_a32 (3) exp_008_instruct_rl_proxy (4) 15B experiments
- **Worker 池 = 0 → 失职** → 立即 spawn ≥2 个 Worker 做非 GPU 任务（代码审查、文献联动、paper 准备）

### 5. 🎯 战略上下文
**核心 story**: ContamCal — post-hoc IRT calibration for contamination detection. 4PL+γ additive model 在真实数据上 coverage collapse（20-33%），已确认为 model misspecification（D056），framing 调整为 "benchmark-dependent contamination effects"。

**决策链**:
- D056: Coverage collapse = model misspecification（不是 γ 值问题）
- D055: 3B 只需重跑 3 个 SFT（d025_s42, d100_s42, d100_s123），其余已 alpha=32
- D053: 废弃联合/Stratified IRT，论文只引用 per-benchmark 独立 IRT
- D052: Gamma 方向不稳定，不 pivot，等更多数据

**易错点**:
1. **不要混用 alpha=16 和 alpha=32 的 checkpoint 做对比**——memory.md 有完整表格，每次引用 checkpoint 前核对
2. **d000 有两个 checkpoint**: 原版（alpha=32，保留）和 v2（alpha=16，弃用）。eval 必须用原版
3. **Oracle vs RRF 比较需匹配 N=8**——当前 oracle N=15，RRF N=8，直接对比不公平
4. **GSM8K oracle 拟合需要 warmup=2000/samples=2000**——默认参数 rhat 不合格
5. **exp_004 sim sweep 和真实 IRT 的 N_models 不同**——sim 用固定 N，真实数据 N 随 benchmark 变化
6. **距 EMNLP ARR 只有 10 天**——所有非 critical path 任务（如 15B 扩展、新 benchmark）都应降优先级，聚焦 3B alpha=32 完整矩阵 + pooled IRT + paper 写作


---
