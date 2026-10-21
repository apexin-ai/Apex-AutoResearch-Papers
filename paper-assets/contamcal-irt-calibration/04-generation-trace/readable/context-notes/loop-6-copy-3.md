# reviewer / loop_6.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`7365ff10bac57d0ac625.json`](../../sessions/73/7365ff10bac57d0ac625.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-14T22:26:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 边界 cuda:0-5（6× RTX 4090D），越界立即 CRITICAL + kill 进程
- 3B GSM8K 必须从所有 IRT 分析中排除（D018：LoRA 超参损伤导致 12% 准确率，非 contamination）
- Pooled IRT 仅在所有 scale 有同源 signal-derived exposure 时有效（D027/D028），禁止混用 signal + oracle dosage fallback
- seed=123 SFT 必须与同 scale 的 seed=42 使用相同超参（3B: lr=5e-5, alpha=16; 0.5B/1.5B: lr=2e-4, alpha=32）
- ConStat S3 信号已弃用（D030），论文只报告 3-signal RRF (S1+S2+S4)

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，代码根目录 /root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型缓存：/root/autodl-tmp/.hf_cache/Qwen/（Qwen2.5-0.5B, 1.5B, 3B）
- SFT checkpoints：/root/autodl-tmp/exp001/checkpoints/
- Eval 结果：/root/autodl-tmp/exp001/eval_results/
- Signals 输出：/root/autodl-tmp/exp002/signals/
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/
- 活跃 GPU 进程（截至 handoff 时）：
  - GPU 0: 可能在跑 3B d000 v2 para eval（ROADMAP 记载）或已切换任务
  - GPU 1: 0.5B d100 s123 eval (PID 444836, GSM8K ~28%)
  - GPU 2: 1.5B d100 s123 SFT (PID 435420, ~41%)
  - GPU 3: 3B d100 v2 SFT (PID 420195, ~78%, 即将完成)
  - GPU 4: 3B d000 v2 eval (PID 441570, GSM8K ~34%, D020 验证)
  - GPU 5: 3B d000 s123 SFT (PID 435976, ~45%)
- Cron: `5633488f` 每 5 分钟轮询 GPU 释放并自动提交队列任务
- CPU: exp-004 v3 (PID 599562, 54/120) | exp-005 v4 (PID 559667, 23/25)

### 3. 📊 当前状态
我是 Reviewer，本轮发了 Reviews #36-#47。主要完成：
- D018 排除 + signal 同质性 + compute_ground_truth 代码审查（全 PASS）
- joint_fit.py exclude_rules 死代码发现（已由 Agent 修复）
- d000 baseline gap 分析核实（与 D029 一致，delta-of-deltas < 1pp）
- Dose-response 编译核实（三核心发现可靠）
- 1.5B d025 eval 结果验证（HumanEval d025≈d100 饱和发现）
- ConStat S3 审计核实（全 null，不影响已有结果）
- GPU 资源合规持续监控（所有进程在 cuda:0-5 内）

Registry RUNNING（GPU 任务）：exp_001_eval_05B_d100_s123_aligned, exp_001_sft_d100_3B_v2, exp_001_eval_3B_d000_v2_aligned, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d000_s123
Registry RUNNING（CPU）：exp_004_sim_sweep_v3, exp_005_noise_prop_v4

ROADMAP 更新原因提到"pooled IRT GSM8K 结果已出"——但我未来得及审查这个结果。

### 4. 📋 待办（条件触发式）
- **Pooled IRT 结果出现** → 最高优先审查：gamma 值、CI、convergence diagnostics（Rhat<1.01, ESS>400, div=0%）、N_models 是否足够、D018 排除是否生效、signal 同质性是否满足
- **3B d000 v2 eval GSM8K 完成** → D020 验证：GSM8K ≥50% 则 lr=5e-5 修复成功；<50% 则 3B 仍有问题需要进一步诊断
- **GPU 3 释放（3B d100 v2 SFT ~1h）** → 确认 Agent 立即启动 3B d100 v2 eval
- **GPU 1 释放（0.5B eval 完成）** → 核实 0.5B d100 s123 GSM8K 分数，与 seed=42 对比看 seed variance（之前 MMLU seed variance 达 7.2pp）
- **3B d000 para eval 完成** → 补全 3B d000 baseline gap 数据，完成全矩阵分析

### 5. 🎯 战略上下文
- **核心 story**: ContamCal 用 4PL+γ IRT 做 post-hoc calibration。Scale-dependent 是主叙事：0.5B 退化（-16pp MMLU）、1.5B 免疫（<1pp）、HumanEval 唯一有 dose-response 且 d025 即饱和。
- **N_models 是瓶颈**：per-benchmark N=4 统计功效不足（gamma CI 含 0），必须跨 scale 池化 + multi-seed 扩展到 N≥15-30。Pooled IRT 是解决路径。
- **最容易判错的事**：
  1. 不要把 raw paraphrase gap 当 contamination 信号——d000 baseline gap 高达 ±9pp（GSM8K），必须 delta-of-deltas
  2. joint_fit 标注为 "ABLATION"，但如果 Agent 引用其结果作为主线证据要拦截
  3. Worker 汇报的 GPU 进度经常滞后 30-60 分钟，独立核实比信 Worker 数据更准
  4. 0.5B d025 SFT 已 2 次失败（registry 标 ❌），不要再追问为什么不重跑——已放弃
- **决策链要点**：D018(3B GSM8K 排除) → D023(MMLU 56K params 不可行，分层策略) → D024(delta exposure) → D027/D028(pooled IRT 同源约束) → D029/D030(弃用 S3 ConStat)
- **DDL**: EMNLP 2026 ARR May 25，~10 天。算力充足（6×4090D + 弹性云），不是瓶颈。瓶颈是 pooled IRT 分析结果是否支持 paper story。


---
