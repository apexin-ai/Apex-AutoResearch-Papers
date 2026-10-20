# agent / loop_4.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`b809e35eb6448ff9b04c.json`](../../sessions/b8/b809e35eb6448ff9b04c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T08:21:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-22162 的 cuda:0, cuda:1, cuda:2, cuda:3（config `gpu_ids`），禁止用其他设备
- 论文数字诚信：Cohen's d 实际值 0.44→0.52→0.68→0.80（旧 claim 0.60→1.12 已证伪，D035/D036），引用必须用 `/root/autodl-tmp/pacs/analysis_output/cohens_d_bf16.json` 的计算结果
- Mean-based II 全部弃用，论文统一 median + difference statistic（D032/D033），registry 中 `gradient_paired_aggregate` 字段 s015/s025 vs s020/s030 定义不一致，不可直接引用
- Bootstrap B=1000（fp16）vs B=10000（bf16），论文需标注差异
- Cross-model 不是 cross-architecture（DeepSeek/Qwen 同为 Qwen2ForCausalLM）

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162，4× RTX PRO 6000 Blackwell 96GB
- 工作目录：`/root/autodl-tmp/pacs`
- Python：`/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：DeepSeek-R1-Distill-Qwen-7B（默认 checkpoints/）+ Qwen2.5-7B-Instruct（`/root/autodl-tmp/models/Qwen2.5-7B-Instruct`）
- 数据：`/root/autodl-tmp/pacs/data/math500.json`（50 problems）
- 分析产出：`/root/autodl-tmp/pacs/analysis_output/`（permutation_test_results.json, cohens_d_bf16.json 等）
- 活跃进程：c4_entropy（PID 93190, cuda:1, cron 监控中，19/30 problems 进度）
- 活跃 Worker：`worker_analysis_bf16_qw_rand_s015_20260514T081651`（分析 Qwen random s015）

### 3. 📊 当前状态
**刚完成**：Qwen importance 4/4 PASS 确认（D034/D037/D038）；DeepSeek bf16 importance 全系列 Cohen's d 实际计算（D035/D036）；旧 bf16 DeepSeek random/importance/Qwen importance 实验批量 killed（已被 bf16_qw_*/bf16_ds_* 系列取代）

**Registry 状态**：71 实验 — RUNNING 1, ANALYZING 3, QUEUED 1, DONE 66
- RUNNING：`c4_entropy`（cuda:1, PID 93190, 19/30 problems）— C4 mechanism 验证
- ANALYZING：`bf16_qw_rand_s015/s020/s025` — Qwen random baseline，Worker 正在分析 s015
- QUEUED：`bf16_qw_rand_s030` — 等 GPU（cuda:0/2/3 空闲但需要启动）

**等待中**：
- Worker `worker_analysis_bf16_qw_rand_s015` 回调 → 处理 s015 结果
- bf16_qw_rand_s020/s025 待分析（需 spawn Worker）
- bf16_qw_rand_s030 待从 QUEUED 提交
- c4_entropy cron 回调 → 完成后分析

### 4. 📋 待办（条件触发式）
- `worker_analysis_bf16_qw_rand_s015` 回调到达 → 更新 registry + spawn s020/s025 分析 Worker
- bf16_qw_rand_s020/s025/s030 全部分析完 → 跑 cross-model permutation test（Qwen random 预期 4/4 FAIL）
- c4_entropy cron 回调（进程 93190 退出）→ spawn Worker 分析 entropy/Gini 结果，更新 C4 claim
- 全部 Qwen random + c4_entropy 完成 → 向 Director 汇报实验矩阵全部填满，请求启动 full paper review
- bf16_qw_rand_s030 仍 QUEUED → 需要提交到 cuda:0/2/3 之一（当前空闲）
- **截稿 2026-05-25（11 天）**：§5 Results 需要最终数字、§1/§7/§8/Abstract 未开始

### 5. 🎯 战略上下文
- **核心发现**：importance-based head pruning 的 compound interaction severity (II) 随 sparsity 单调递增（DeepSeek median diff: 0.39→1.48→7.16→14.59; Qwen: 0.039→0.235→1.268→2.943），random masking 三相 II 持平（全 FAIL）。这是论文的 central claim
- **决策链关键节点**：D029（random outlier 修正）→ D030（mean 污染）→ D031（bf16 importance PASS）→ D032（difference statistic）→ D033（弃 ratio）→ D034（C5 cross-model）→ D035/D036（Cohen's d 修正）→ D037/D038（Qwen Cohen's d）
- **易错点**：
  - Qwen s015 Cohen's d CI 含 0，不显著（D037/D038），论文 dose-response narrative 需要处理这个 gap
  - Qwen mid-phase 极小（4372 tokens, 26 segments），与 DeepSeek 不同，不可直接对比绝对值
  - bf16_qw_rand_s030 还在 QUEUED 没提交，cuda:0/2/3 空闲 = 失职状态，接手后立即提交
  - c4_entropy 是 C4 claim 的唯一验证实验，结果直接决定论文是否保留 mechanism 叙事


---
