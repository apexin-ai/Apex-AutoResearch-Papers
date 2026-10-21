# agent / loop_12.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`27bcbb5c753c3322d65d.json`](../../sessions/27/27bcbb5c753c3322d65d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-17T16:31:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19828 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- C003: 禁止引用 α≤0.50 TY Granger 显著率（seed 不稳定，已升级约束）
- C004: 禁止未确认状态下 kill 运行中进程或 rm -rf 实验目录
- 训练命令必须自带 `export HF_ENDPOINT=https://hf-mirror.com`（国内服务器，直连 HF 超时）
- 训练命令必须自带 `export HF_HUB_DISABLE_XET=1`（避免 xet 协议报错）

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`，conda env = base（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 数据：`data/c4_5k/`（C4）、`data/wikitext/`（WikiText）均在工作目录下
- 模型：通过 HF mirror 在线拉取（Pythia-1B、Pythia-410M、OPT-1.3B、GPT-2 medium）
- 磁盘：`/root/autodl-tmp` 约 817GB 可用（3% 使用率），空间充裕
- 活跃进程：generalize_opt1b_wiki_a100_s42（PID 249384，cuda:1，OPT-1.3B on WikiText）

### 3. 📊 当前状态
**刚做完**：收到 `generalize_pythia1b_c4_a100_s42` 失败 CRON 回调（Pythia-1B on C4, EXIT_CODE=1，跑了 0.65h）。已派诊断 Worker（`worker_diagnose_generalize_pythia1b_c4_a100_s42_20260517T122942`）SSH 读日志分析原因，已向 Director 汇报失败。

**Registry 状态**：
- RUNNING: `generalize_opt1b_wiki_a100_s42`（OPT-1.3B on WikiText, cuda:1）— 预计 17:00-22:00 UTC 完成
- DONE(failed): `generalize_pythia1b_c4_a100_s42` — 等诊断 Worker 回调
- 其余 38 个实验全部 DONE（success 21, failed 3, killed 14）

**等待中**：
- 诊断 Worker 回调 → 分析失败原因 → 修复后重新提交到 cuda:0
- OPT-1.3B 训练完成 cron 回调 → 5-method analysis

### 4. 📋 待办
- 诊断 Worker 回调到达 → 读报告确定失败原因 → 修复 → 重新提交 Pythia-1B C4 实验到 cuda:0（cuda:0 当前空闲，必须尽快恢复利用）
- `generalize_opt1b_wiki_a100_s42` cron 完成回调 → spawn Worker 做 5-method analysis（PermG + TY + ECE + ColS + MinK）→ 汇报 Director
- 两个泛化实验（Pythia-410M 已 success + OPT-1.3B + Pythia-1B C4）全部完成 → 泛化结果纳入论文 experiments.tex → 准备 Round 2 重新提交
- cuda:0 空闲是失职状态，诊断完成后必须立即重新利用

### 5. 🎯 战略上下文
- **核心方向**：D027 reframe — 方法论陷阱 + 多方法共识框架为主线，canary prediction 为 case study，目标 EMNLP 2026 main track
- **当前阶段**：泛化实验 Phase 2（证明 framework 跨架构/跨数据域的通用性）。Phase 2a Pythia-410M 已成功，Phase 2b OPT-1.3B 运行中，Phase 2c Pythia-1B+C4 刚失败待修复
- **Dose-Response 已完成**：α=0.00→1.00 五个点三 seed 全部跑完，α=0.50 确认为 seed-dependent boundary（D053）
- **Review issues 19/19 已全部关闭**，论文待泛化结果纳入后重新提交 Round 2
- **易错点**：Pythia-410M 泛化实验已成功（report 里有 analysis_report），下一个"你"不要重复提交这个实验。失败的是 Pythia-1B on C4（不同实验），等诊断结果修复后重提
- **易错点2**：论文唯一真源是 `docs/paper/`（D046 决策），不是 artifacts 下的副本


---
