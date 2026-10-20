# director / loop_6.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`8935fb8b4af886eead3f.json`](../../sessions/89/8935fb8b4af886eead3f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-14T20:03:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0-5 全部属于本项目（cqa1-21977），无越界风险但**禁止空闲 >10min**
- 3B d100 v2 SFT (PID 420195) output-dir 与 v1 相同（`Qwen2.5-3B_d100_s42`），会覆写 v1 checkpoint。D020 决策意图是弃用旧超参 v1，但如果 v1 eval 还在引用需先备份
- ADVI 已被 D003 证明失败（bad local mode on 4PL），禁止作为 fallback
- GSM8K 是**负对照**（D024），不是主结果。γ≈0 是期望值，不要把 3B GSM8K 灾难性退化（d000→12%）当 contamination 效应
- d100 AUC=0.5 是 labeling artifact（所有 item 都被污染 → label 无判别力），不是信号失效
- Delta exposure 修复已验证 — per-benchmark 路径**必须**减去 d000 baseline signal 再 clip≥0

### 2. 🖥️ 基础设施快照
- 服务器: cqa1-21977 (connect.cqa1.seetacloud.com), 6×RTX 4090D
- 工作目录: `/root/contamcal-irt-calibration`
- Python/conda: aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型 checkpoints: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{size}_d{dosage}_s42/`
- Signal 数据: `/root/contamcal-irt-calibration/exp002/signals/`
- IRT 代码: `exp006/run_exp006.py`, `exp006/run_irt_calibration.py`, `exp006/joint_fit.py`
- Stan model: `exp006/contamination_4pl.stan`
- 活跃进程 (上次核实): GPU 3 PID 420195 (3B d100 v2 SFT, 34%), GPU 4 PID 420910 (1.5B d025 eval)
- GPU 5 已释放 (3B d000 v2 SFT 完成 3125/3125, registry 仍标 RUNNING)
- CPU 实验: exp-004 sim_sweep (60/120 checkpoint), exp-005 noise_prop (17/25 checkpoint) — 均被系统 kill 过，重启 worker 可能也死了（90min 无更新告警）

### 3. 📊 当前状态
**刚完成**: P0 delta exposure bug 修复验证通过（Rhat 1.53→1.0096, ESS 7→522）。paper_framing.md 重新平衡（D025 基于 Dream full-mode 分析）。

**RUNNING/待处理**:
- exp_001_sft_d100_3B_v2: GPU 3, 34%, D020 超参 (lr=5e-5, alpha=16)
- 1.5B d025 aligned eval: GPU 4
- 1.5B exp-002 signals: 可能在 GPU 0（与 3B eval 共享，Reviewer 标记效率低）
- GPU 1/2/5: 空闲 — Agent 被 reset 前收到了 seed=123 SFT 指令但未执行
- Re-dream (dream_20260514T185145): reviewing 阶段，full mode，测试 D025 更新后 framing

**等待中**: 
- Dream 完成回调 → 按 dream-report-action skill 处理
- Agent reset 后需要重新下达: cross-scale pooling 代码 + seed=123 SFT + GPU 填充

### 4. 📋 待办（条件触发式）
- Agent BOOT 完成 → **立即下达**: (1) cross-scale pooling 代码（`--pool-scales`，最高优先级）, (2) seed=123 SFT 在空闲 GPU 上启动（0.5B d005/d025/d100）, (3) 3B d000 v2 eval（GPU 5 释放后）, (4) GPU 0 进程解冲突（1.5B signals 搬到独立 GPU）, (5) registry 状态清理（3B d000 v2→DONE, exp002 d025→DONE）
- Dream done 回调 → 读 3 份 review_report.md，跨档对比，执行 dream-report-action protocol。目标: best≥weak accept 且 median≥borderline 才能批准 P0 实验大规模投入
- Cross-scale pooling 代码完成 → 用 0.5B(4)+1.5B(3)+3B(1-2) ≈ 8-10 models 做首次 pooled IRT on ARC/MMLU(1000)
- 1.5B signals 完成 → C2 "scale-dependent" 验证：S2/S4 在 1.5B 是否恢复？如果不恢复 → 触发 C2 contingency（降为 "method-specific"，drop "scale-dependent"）
- Seed=123 SFT + eval 完成 → N_models 从 ~10 提升到 ~20-30，重跑 pooled IRT
- 3B d100 v2 SFT 完成 → eval all benchmarks，加入 pooling

### 5. 🎯 战略上下文
**决策链**: D016(Min-K++ ref model) → D018(3B GSM8K collapse) → D020(3B LoRA fix) → D021(d100 labeling) → D022(C2 radical reframing) → D023(NUTS stratified) → D024(GSM8K negative control + cross-scale pooling) → D025(Dream analysis: N_models + novelty rebalance)

**Dream D025 核心结论**: Best 4/6, Median 3/6, Worst 3/6。结构性问题: N_models 不足(全档)、novelty ceiling(全档)、coverage gap(全档)。积极信号: Min-K++ reversal = 最强贡献(全档)、Fisher Info = 最强理论贡献(全档)。Framing 已重新平衡: Fisher Info 升 Core #3, contribution hierarchy 调整。

**最容易判断错的事**:
1. 不要把 d000→d100 delta 当 contamination 效应 — 在 3B GSM8K 这是灾难性退化恢复(48pp)
2. 1.5B MC benchmark 污染效应极小(MMLU +0.8pp at d100) — 这不是 bug，是 SFT 方式在该 scale 确实效果弱
3. 0.5B d025 SFT 之前标 "2x fail" 但 checkpoint 实际存在（Reviewer #15 确认）
4. exp002 d025 signals 之前说不完整（只有 MMLU embedding），但后来确认完整（3 benchmarks × 4 signals）— 以最新 Reviewer 报告为准
5. GPU 预算是 1584h（6卡×11天×24h），不是 200h。瓶颈是调度效率不是总量。不需要申请扩容
6. Per-benchmark vs joint-fit 的区别: per-benchmark 用 signal-derived exposure（已修复 delta），joint-fit 用 oracle dosages。两者都可以跑，per-benchmark 是论文 primary（盲检测），joint-fit 是 oracle upper bound


---
