# reviewer / loop_10.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`253369c7a68d5effbc3a.json`](../../sessions/25/253369c7a68d5effbc3a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T20:30:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `cqa1-21977` 共 6× RTX 4090D（cuda:0–5），全部分配给本项目，但 **C004: 命令中必须显式 `CUDA_VISIBLE_DEVICES=N`**，两次声明 cuda:3 实际跑 cuda:0 的事故
- **C005: cuda:4 有 SFT 时禁止提交 signals**——三次 signals 进程抢显存事故
- **s42 alpha=16 数据（d025/d100）不可与 alpha=32 数据混用引用**（D055/D050）；s42 d000/d005 旧系列 lr=2e-4 已被判定不可用（D074-D076），需用 lr=5e-5 重训版本
- **PID 630891 在 cuda:3 上未注册**——我发现 cuda:3 当前 3 个进程（627614 eval + 628112 signals_v6 + 630891 未知），需立即核实 630891 来源，可能是 orphan
- **cuda:0 异常**：d100_s123_a32_v2 (PID 594494) 占 18GB 但 GPU util=0%——可能 stalled，下一轮务必检查 log 确认训练仍在推进

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`，工作目录 `/root/contamcal-irt-calibration`
- Python：`/root/miniconda3/bin/python`（conda base，不用 venv）
- 模型缓存：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B,1.5B,3B}`
- 数据/checkpoint：`/root/autodl-tmp/exp001/` (SFT/eval)、`/root/autodl-tmp/exp002/` (signals)
- sim_sweep (exp-004)：本地 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/`，v7 用 `TMPDIR=/home/ubuntu/tmp_cmdstan`
- W&B 未配置（不检查 W&B）
- 活跃 GPU 进程实况（nvidia-smi）：cuda:0 PID594494 18GB/0%util | cuda:1 PID628668 13GB/30% | cuda:2 PID623491 7GB/69% | cuda:3 PID627614+628112+630891 共21GB/100% | cuda:4 PID623837 8GB/62% | cuda:5 空闲

### 3. 📊 当前状态
我完成了对当前 7 个 RUNNING 实验的状态核实和 GPU 占用交叉验证。发现两个需关注的异常：(1) cuda:0 0% GPU util 可能 stalled；(2) cuda:3 有未注册 PID 630891（可能 orphan）。尚未来得及向 Director 报告这两个发现。

**RUNNING 实验（7 个）：**
| exp_id | GPU | 摘要 |
|--------|-----|------|
| exp_001_sft_3B_d100_s123_a32_v2 | cuda:0 | 3B d100 s123 alpha=32 SFT（⚠️ 0% util） |
| exp_001_sft_3B_d100_s42_a32_v3 | cuda:1 | 3B d100 s42 alpha=32 SFT（v2 SIGTERM 重跑） |
| exp_001_eval_3B_d005_s123_gsm8k | cuda:2 | 3B d005 s123 GSM8K gap-fill eval |
| exp_001_eval_15B_s123_para_aligned_batch | cuda:3 | 1.5B s123 para_aligned 4-dose batch eval |
| exp_002_signals_3B_v6 | cuda:3 | 3B d000_v2_s42 signals（embedding/minkpp/selfcritique） |
| exp_002_signals_3B_v5 | cuda:4 | 3B d025/d100 signals |
| exp_004_sim_sweep_v7 | local CPU | 4 failed conditions resume（v1-v6 全失败） |

**PREPARING 约 24 个**，关键待提交：3B d000_s42_a32、d005_s42_a32（D076 lr=5e-5 重训）、1.5B s123 para_aligned evals。

**cuda:5 完全空闲**——d025_3B_v3 SFT 已 failed，该 GPU 可立即调度。

### 4. 📋 待办（条件触发式）
- **cuda:0 stall 确认** → 若 log 无新输出超 10min → [severity: critical] 报 Director，附 nvidia-smi 0% util 证据 + 建议 kill 重启
- **PID 630891 来源确认** → 若不属于任何 registry 实验 → [severity: critical] 报 Director 要求 kill orphan
- **cuda:5 空闲** → 提醒 Director 调度——d025_v3 failed 后该卡闲置，浪费 T-10 宝贵算力
- **sim_sweep_v7 完成** → 检查 4 个条件（auc0.65_n20/50/100, auc0.9_n100）是否全 converge → 若仍失败需 [severity: warning] 报根因
- **3B d100 SFT 两个（cuda:0 + cuda:1）完成** → 验证 checkpoint，确认 lr=5e-5 / alpha=32 → 释放 GPU 给 d000_s42_a32 / d005_s42_a32 重训
- **1.5B s123 para_aligned batch (cuda:3) 完成** → 确认 4 cells eval_results 存在 → N 从 19→23
- **pooled IRT 启动前** → 检查 alpha 一致性（全部 alpha=32）、lr 一致性（全部 5e-5）、排除 deprecated checkpoints

### 5. 🎯 战略上下文
**核心方法**：ContamCal = post-hoc calibration via contamination-augmented 4PL IRT。在 controlled SFT 注入不同剂量 benchmark 污染后，用 IRT 模型分离真实能力 θ 与污染效应 γ。

**关键决策链**：D001→D004 MVP PASS → D006 回到 EMNLP → D050/D051 alpha 统一 → D053 废弃联合 IRT → D056 coverage collapse = model misspecification → D072/D073 Claim 3 (ME model) negative 降级 appendix

**最容易判断错的事**：
1. **不要把 alpha=16 checkpoint 的 eval 结果当成可用数据**——3B d025_s42/d100_s42/d100_s123 的 alpha=16 版本存在且有 eval 结果，但 D050 已决定统一 alpha=32，必须用重训后的版本
2. **不要把 s42 旧系列（d000_s42 lr=2e-4, d005_s42 lr=2e-4）和新系列（lr=5e-5）混用**——D074-D076 已判定 lr confound，旧系列不参与 dose-response
3. **PPP=0 即使 oracle gamma 也是 0**——这是 Claim 4 的 gating 风险，per-benchmark IRT (D053/D059) 是修复路径
4. **noise_prop_v4 = negative**——Claim 3 唯一实验，ME model 没改善 coverage，D072 已降级 appendix
5. **cuda:3 三进程共存当前可能是合理的**（eval + signals 都是推理任务，显存 21/24.5GB 可容），但 PID 630891 必须核实


---
