# agent / loop_13.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`81575b890363b9926090.json`](../../sessions/81/81575b890363b9926090.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-16T00:25:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0-5（6× RTX 4090D），服务器 cqa1-21977，无其他服务器
- **alpha 混用禁令（D050/D055）**：s42 系列必须 alpha=32，s123 alpha=16 的旧数据不可与 alpha=32 混合引用。d025_s42 和 d100_s42 旧 checkpoint 是 alpha=16，不可用
- **lr confound（D074-D076）**：s42 的 d000/d005 旧 checkpoint 用了 lr=2e-4（默认值），与全系列 lr=5e-5 不一致。这些 checkpoint 及其下游 signals 全部不可用于 IRT pool，必须用重训后的 checkpoint
- **投稿死线：EMNLP 2026 ARR May 25，距今 9 天**
- sim_sweep（exp-004）跑在本地 CPU，不在 cqa1-21977 上

### 2. 🖥️ 基础设施快照
- **服务器**：cqa1-21977（AutoDL），6× RTX 4090D
- **工作目录**：`/root/contamcal-irt-calibration`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **激活命令**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型缓存**：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B,1.5B,3B}`
- **Checkpoint 目录**：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{size}_{dose}_{seed}/lora_adapter`
- **Eval 结果**：`/root/autodl-tmp/exp001/eval_results/`
- **Signals 输出**：`/root/autodl-tmp/exp002/signals/`
- **SFT 数据**：`/root/autodl-tmp/exp001/sft_data/sft_dosage_{000,005,025,100}.jsonl`
- **Paraphrases**：`/root/autodl-tmp/exp001/paraphrases/`
- **活跃进程（cron 监控中）**：
  - `exp_001_sft_3B_d100_s42_a32_v3` — PID 628663, cuda:1, tmux
  - `exp_001_sft_3B_d005_s42_a32` — PID 643696, cuda:0, tmux（Session #13 提交）
  - `exp_001_eval_3B_d100_s123_a32_batch` — PID 642752, cuda:0, tmux
  - `exp_002_signals_3B_v7` — PID 652247, cuda:2, tmux（d005_s123 三 benchmark signals）
  - `exp_002_signals_3B_v8` — PID 659053, cuda:4, tmux（d025_s123 + d100_a32_s123 signals）
  - `exp_002_signals_3B_d025_v3_s42` — PID 663047, cuda:5, tmux（d025_v3_s42 self-critique signal）
  - `exp_001_eval_3B_d025_v3_s42_batch` — PID unknown, cuda:3, tmux（d025_v3_s42 aligned+para eval）
  - `exp_004_sim_sweep_v7` — 本地 CPU（7/12 条件完成，auc0.65×3 全失败，auc0.9_n100 在跑）
- **无 running Worker**（全部已 done）

### 3. 📊 当前状态
**刚做完**：Session #12/#13 连续处理了 D076 lr confound 重训、orphan 进程清理（D078-D084）、signals v5/v6 失败重提交、1.5B/3B eval matrix 推进。

**RUNNING 实验（8 个，6 GPU 100% 饱和 + 1 CPU）**：
| GPU | 实验 | 内容 | 预计剩余 |
|-----|------|------|----------|
| cuda:0 | exp_001_sft_3B_d005_s42_a32 | D076 重训 d005 s42 lr=5e-5 α=32 | ~数小时（SFT） |
| cuda:0 | exp_001_eval_3B_d100_s123_a32_batch | d100 s123 α=32 aligned+para eval | 可能快完（共享 cuda:0） |
| cuda:1 | exp_001_sft_3B_d100_s42_a32_v3 | d100 s42 α=32 SFT（v2 被 SIGTERM 后重跑） | ~数小时 |
| cuda:2 | exp_002_signals_3B_v7 | d005_s123 三 benchmark 全 signals | 数小时 |
| cuda:3 | exp_001_eval_3B_d025_v3_s42_batch | d025_v3_s42 eval (aligned+para) | 数小时 |
| cuda:4 | exp_002_signals_3B_v8 | d025_s123 + d100_a32_s123 signals | 数小时 |
| cuda:5 | exp_002_signals_3B_d025_v3_s42 | d025_v3_s42 self-critique signal | 数小时 |
| CPU | exp_004_sim_sweep_v7 | IRT simulation sweep（9/12 可用） | auc0.9_n100 ~15h |

**等待中**：
- 无 running Worker，所有回调由 cron 系统触发
- Director 无未决决策请求

### 4. 📋 待办（条件触发式）
- **d100_s123_a32_batch eval 完成** → 更新 3B eval matrix（s123 aligned+para d100 两格）→ 若 cuda:0 释放且 d005_s42 SFT 仍在跑，提交 d005_s42_para_aligned eval 到 cuda:0
- **d005_s42 SFT 完成（cuda:0）** → spawn worker 跑 aligned + para_aligned eval → 之后跑 signals
- **d100_s42_a32_v3 SFT 完成（cuda:1）** → spawn worker 跑 aligned + para_aligned eval → 之后跑 signals → 完成后提交 exp_001_sft_3B_d025_s42_a32_v3（PREPARING，最后一个 s42 SFT）
- **signals v7 完成（cuda:2）** → d005_s123 signals 入库 → 释放 cuda:2 给下一个 signals 或 eval
- **signals v8 完成（cuda:4）** → d025_s123 + d100_a32_s123 signals 入库
- **d025_v3_s42 eval + signals 完成（cuda:3/5）** → d025_v3_s42 数据点完整
- **3B signals 全部完成** → exp-003 RRF 聚合（CPU）→ per-benchmark exposure scores
- **N ≥ 16 alpha=32 eval 数据齐备** → exp-006 pooled IRT fitting（per-benchmark γ_k, Stan NUTS）+ 7 baselines 对比。当前 N=19（strict α=32），RUNNING 完成后 N≥24
- **sim_sweep_v7 完成** → 9/12 条件足够写 identifiability boundary section；auc0.65 失败不阻塞
- **所有 exp-001/002/003/004/006 完成** → paper writing pipeline 启动（5 步，预计 4-7 天）

### 5. 🎯 战略上下文
**核心 story**：ContamCal = post-hoc statistical calibration via contamination-augmented 4PL IRT。3 个 Claims：
- **Claim 1**（Identifiability, 28.6%）：4PL+γ 模型在 simulation 中可识别 γ → sim_sweep_v7 提供证据
- **Claim 2**（Signal Pipeline, 60%）：multi-signal exposure detection → 3B signals 是 critical path 瓶颈
- **Claim 3**（0%）：noise_prop_v4 negative，measurement error model 无效 → D056 降级为 future work / appendix

**关键决策链**：
- D050: alpha=32 统一标准
- D055: s123 alpha=16 历史数据可接受但不与 alpha=32 混用
- D056: coverage collapse = model misspecification（不是 γ 值问题）
- D076: lr confound 发现，s42 d000/d005 重训

**最易判断错的事**：
1. **不要混用 alpha=16 和 alpha=32 数据做 IRT pooling**——memory.md 有 alpha 实际分布表，严格按此判断
2. **d000_s42 旧 checkpoint（lr=2e-4）的 signals 不可用**——即使文件存在于 exp002/signals/ 目录下也不行，必须等重训 checkpoint 重算
3. **cuda:0 上同时跑了 SFT 和 eval**（d005_s42 SFT + d100_s123_a32 eval），注意 eval 先完成后 SFT 仍在占 GPU，不要误判 cuda:0 空闲
4. **sim_sweep 在本地 CPU 跑**，不是远程服务器，不要 SSH 去查
5. **Claim 3 已经 negative**——不要投入 GPU 做 noise_prop 相关实验，除非 Director 明确指示
6. **auc0.65 sim_sweep 条件持续失败**——这是 CmdStan 数值问题，不是代码 bug，不要反复重试


---
