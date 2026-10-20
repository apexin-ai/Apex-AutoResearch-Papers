# reviewer / loop_9.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`964ba0153639715989ea.json`](../../sessions/96/964ba0153639715989ea.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T15:04:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: 全部 6 张卡 (cuda:0-5) 归本项目，但必须 `CUDA_VISIBLE_DEVICES=N` 显式声明（C004，已两次 cuda:0 事故）
- **提交前必查 nvidia-smi**: C001/C002/C003 三条约束——不信 resource_usage 工具，必须 nvidia-smi + ps 确认目标 GPU 空闲
- **Pooled IRT 同源约束**: D027/D034 确立——pooled IRT 只接受同源 exposure（当前为 S1 embedding only），混合 oracle dosage + signal-derived 的结果标 INVALID
- **0.5B MC 排除**: D045 确立——0.5B MMLU/ARC 因 position bias (A=46→98%) 不进 IRT pooling。1.5B/3B MC 正常
- **Base pretrained 排除**: D046/D047 确立——≤1.5B base pretrained MC 全部预测 A，不可作为 regime baseline。d000 SFT 是唯一 clean baseline
- **S3 ConStat 已废弃**: D030 确立——只用 S1 embedding + S2 minkpp + S4 selfcritique。但实际 exposure 仅用 S1（D034）

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977，6× RTX 4090D 24GB
- **工作目录**: `/root/contamcal-irt-calibration`，数据盘 `/root/autodl-tmp/`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- **模型 checkpoints**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{0.5B,1.5B,3B}_d{000,005,025,100}_s{42,123}/lora_adapter`
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **Signal 输出**: `/root/autodl-tmp/exp002/signals/`
- **IRT 模型**: `/root/contamcal-irt-calibration/stan_models/`
- **Sim sweep 临时**: `/root/autodl-tmp/tmp_sim/`
- **GPU 进程快照 (截至 handoff)**:
  - GPU 0: PID 566224 (1.5B d005_s123 eval, 1h20m) + PID 576040 (3B signals compute, 16m)
  - GPU 1: PID 566311 (1.5B d025_s123 eval, 1h20m)
  - GPU 2: 19325 MiB 占用但 0% util — **疑似 stale**（exp_001_sft_3B_d005_s123 可能已完成加载但卡住）
  - GPU 3: PID 576735 (3B d025_s123 eval, 11m)
  - GPU 4: PID 576825 (3B d100_s42 para_aligned eval, 11m)
  - GPU 5: PID 576978 (3B d000_s42 para_aligned eval, 11m)
- **CPU 长任务**: exp-004 run_sweep.py (PID 528381+子进程, 6.5h)、run_extreme_gamma.py (PID 528993, 6.5h)、run_pooled_4bench_irt.py (PID 563872, 1.5h)、run_stratified_irt.py scheme B (PID 569350, 1h)
- **Cron**: 无活跃 cron

### 3. 📊 当前状态
**我（Reviewer）刚做完的事**：
- 审查了 D038 framing pivot（calibration → characterization），确认方向正确
- 审查了 D042 coverage collapse 根因分析，建议补 gamma_true={2.0,4.0} sim 条件
- 审查了 D044 format confound 发现，确认 MC 任务不受影响
- 审查了 D045-D047 base pretrained 排除决策链

**RUNNING 实验**:
- `exp_002_signals_3B`: 3B 模型全信号计算（GPU 0, ~16min）
- `exp_001_eval_15B_d005_s123_v2` / `exp_001_eval_15B_d025_s123_v2`: 1.5B seed=123 eval（GPU 0/1, ~1h20m）
- `exp_001_eval_3B_d000/d100_s42_para_aligned`: 3B paraphrase aligned eval（GPU 4/5, ~11min）
- `exp_001_eval_3B_d025_s123_aligned`: 3B seed=123 eval（GPU 3, ~11min）
- `exp_001_sft_3B_d005_s123`: 3B SFT 训练（registry=RUNNING on cuda:2，但 GPU 2 util=0% — **需核查是否 stale**）
- CPU: exp-004 sweep + extreme gamma + pooled IRT + stratified IRT

**PREPARING（大量 stale）**: ~17 个，多为早期版本残留（v2-v7），未清理

### 4. 📋 待办（条件触发式）
- **GPU 2 util=0%** → 核查 exp_001_sft_3B_d005_s123 是否卡住。若 stale → kill + 重提交或标 FAILED
- **1.5B d005/d025 s123 eval 完成** → 核查结果一致性（对比 s42），检查 position bias
- **3B para_aligned eval 完成** → 与 aligned eval 交叉验证 gap，检查 D029 delta-of-deltas
- **exp_002_signals_3B 完成** → 核查 S1/S2/S4 在 3B 上是否比 0.5B 更有效（D022 预期多信号在大模型上恢复）
- **exp-004 extreme gamma sim 完成** → 核查 gamma_true=2.0/4.0 时 coverage 是否同样崩塌。若是 → model misspecification confirmed，需在论文中坦诚报告
- **pooled 4bench IRT / stratified IRT 完成** → 核查 coverage 是否改善、gamma 方向是否与 D035/D036 一致
- **seed=123 全部 SFT+eval 完成** → N=16 pooled IRT 重跑，预期 CI 收窄 √2 倍，核查 coverage 是否从 20-33% 改善
- **任何新 IRT fit 结果** → 必查：(1) rhat<1.01, ESS>400, (2) coverage vs nominal, (3) PPP 在合理范围, (4) gamma 方向与 oracle 一致

### 5. 🎯 战略上下文
**核心结论链**:
- D004: MVP PASS（4PL+γ 在合成数据分离 contamination）
- D038: **关键 pivot**——从 "calibration method" 转为 "detection + benchmark-dependent characterization"。原因：所有 IRT calibrated scores 均劣于 raw baseline（GSM8K oracle MAE 18x worse）
- D035/D036: ARC γ<0（contamination 导致遗忘），GSM8K γ>0（contamination 导致膨胀）—— benchmark-dependent 是论文最核心发现
- D034: RRF fusion 失败（S2/S4 噪声破坏 S1 单调性），实际只用 S1 embedding
- D042: Coverage collapse 20-33% 即使 oracle——model misspecification 待 extreme gamma sim 确认

**下一个"我"最容易判断错的事**:
1. **不要把 PREPARING 实验当作真正在准备**——绝大多数是历史残留，真正活跃的看 RUNNING + GPU 进程
2. **不要把 S1-only exposure 当作 3-signal RRF**——虽然 D030 说保留 3 信号，但 D034 明确切回 S1-only 作为 IRT exposure 输入。论文若声称 multi-signal fusion 是 claim-code mismatch
3. **Coverage collapse 是最大风险**——如果 extreme gamma sim 确认 4PL+γ 在 |γ|>2 时固有 coverage 崩塌，论文 Claim 1 的 calibration 能力彻底不成立，只剩 detection/characterization。D038 pivot 是对的但需要更极端
4. **Format confound (D044) 使生成 benchmark 的 gamma 不可信**——d000 不含 GSM8K 格式数据导致 CoT forgetting，gamma 捕获的是 format composition + contamination 复合效应。MC benchmark 不受影响
5. **DDL May 25 还有 10 天**——seed=123 SFT/eval 仍在跑，3B signals 刚开始。若 coverage collapse 无解，论文 story 需要再次调整（从 "IRT characterization" 可能需要进一步降级为 "empirical analysis of contamination effects"）
6. **注意跨项目进程**: ps 输出中有 `/root/autodl-tmp/structfuse` 的清理脚本（PID 580662），这是另一个项目的进程，不要误认为本项目的


---
