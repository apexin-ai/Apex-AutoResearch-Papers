# director / loop_4.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`b8651b1dd16096963338.json`](../../sessions/b8/b8651b1dd16096963338.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-14T13:08:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-5（6 张卡），严禁使用白名单外 GPU
- 服务器 cqa1-21977 (connect.cqa1.seetacloud.com)，AutoDL 实例，重启后端口会变
- exp-002 selfcritique 崩溃根因未明确，不要盲目重启——需完整 traceback + 内存快照后再决定方案
- exp-002 cron 多次 false positive（读旧 batch_report dry_run=true 误判），诊断时必须区分新旧日志版本

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，工作目录 /root/contamcal-irt-calibration
- Python：aml-train 镜像，conda 环境 `/root/miniconda3/bin/python`（不用 venv）
- 模型 checkpoints：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{0.5B,1.5B,3B}_d{000,005,025,100}_s42/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- exp-002 信号输出：`~/runs/contamcal-irt-calibration/exp002/` 下各 dosage/benchmark 子目录
- exp-004 sim sweep + exp-005 noise prop：CPU 任务，跑在同一服务器

### 3. 📊 当前状态
本轮处理了 exp-002 多次失败重启（v4→v5）、exp_001_sft_d005_3B 完成确认、GPU 4 分配决策。

RUNNING 实验：
- **exp_002_signals_05B** (GPU 0)：v5 运行中，PID 370957/370959，信号完成度 6/27，selfcritique 是瓶颈，预估 ~15:00 UTC 完成（如不再崩）
- **exp_001_eval_15B_aligned_batch** (GPU 1)
- **exp_001_eval_05B_aligned_batch** (GPU 2)
- **exp_001_eval_3B_d100_aligned** (GPU 3)
- **exp_001_eval_3B_d000_aligned** (GPU 5)
- **GPU 4**：已指令 Agent 先跑 eval_3B_d005_aligned，完成后跑 0.5B d025 SFT
- **exp_004_sim_sweep_v2** (CPU)：48/120 runs，ETA May 16-17
- **exp_005_noise_prop_v3** (CPU)：ETA ~14:30 UTC today

SFT 训练完成度：0.5B/1.5B/3B × d000/d005/d100 全部 ✅。缺 d025/d050（P2-P4）。

### 4. 📋 待办
- exp-002 v5 selfcritique task 完成 → 确认修复有效，继续；崩溃 → 不重启，要求 Agent 提供完整 traceback + GPU 内存快照，考虑拆分 selfcritique 为独立脚本
- exp-002 全部 27 信号完成 → 核实文件齐全 → 推进 exp-003 RRF（P0 critical path）
- eval batch 全部完成 → 汇总 dose-response 表（目前 4/24 cells done）
- GPU 4 eval_3B_d005 完成 → 启动 0.5B d025 SFT
- exp-004 sim sweep 完成 → 与 v1 对比核心结论是否持续成立（1/√N scaling、100% power、multiplicative 无交互）
- exp-005 noise prop v3 完成 → 评估 measurement error model 是否 close coverage gap

### 5. 🎯 战略上下文
- 项目核心：用 IRT 4PL+γ 模型校准 LLM benchmark 污染，critical path 是 exp-002 signals → exp-003 RRF → exp-006 IRT calibration
- exp-002 是当前最大瓶颈，已失败多次。GPU 0 内存 13.4GB 异常（0.5B 模型理论 ≤5GB），可能 target+reference 同时加载或内存泄漏
- exp-004 增量结果持续支撑核心结论（AUC≥0.70 阈值、1/√N scaling），但 v1 标记 failed（sweep 未跑完），v2 在补
- Eval 结果初步：1.5B d000→d100 MMLU 仅 +0.80pp（MC benchmark 变化极小），HumanEval +17.7pp 显著但 appendix-only。dose-response 效应可能比预期弱——这是后续 IRT 分析需要关注的
- 易错点：(1) cron 读旧日志/旧 batch_report 产生 false positive，诊断时先确认读的是最新文件；(2) registry 状态可能与实际进程不同步（auto-facts 生成时间差）；(3) d025 全线缺失是 dose-response 曲线的关键 gap，需尽快补


---
