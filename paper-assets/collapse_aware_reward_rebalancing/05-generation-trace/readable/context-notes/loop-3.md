# agent / loop_3.md

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`64838f9befc60ec463f1.json`](../../sessions/64/64838f9befc60ec463f1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-17T08:47:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb2-23165 的 cuda:0 和 cuda:1（2× RTX 5090 32GB）
- RTX 5090 必须用 bf16=True，不能用 fp16（GradScaler 会崩，carr_fullft_k4_probe_01 已验证）
- 训练命令必须带 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`（服务器网络受限）
- Full-FT 训练必须 gradient_checkpointing=True + per_device_train_batch_size=1 + grad_accum=8（否则 OOM）

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165，工作目录 `/root/autodl-tmp/carr/`
- Python：`/root/miniconda3/bin/python`，conda env=base
- 模型：Qwen3-0.6B（HF cache 已离线缓存）
- 数据集：openbmb/UltraFeedback（已离线缓存，2200 prompts）
- 输出目录模式：`/root/autodl-tmp/carr/outputs_*/{gen_N}/condition_0/merged`
- 活跃进程：carr_fullft_lr2e5_k16_probe_01（PID 534061，cuda:1，K=16 极端筛选实验）
- 磁盘：充裕（/autodl-pub 4.4T/14T 可用）

### 3. 📊 当前状态
**刚做完**：收到 `carr_fullft_lr2e5_nocuration_01` 完成回调，已 spawn Worker（worker_analysis_carr_fullft_lr2e5_nocuration_01_20260517T032939）去 SSH 提取指标，**尚未回调**。同时将 `carr_fullft_lr2e5_probe_01` 从 ANALYZING 推到 DONE(negative)。

**Registry 摘要**：
- RUNNING 1：`carr_fullft_lr2e5_k16_probe_01`（cuda:1，K=16 极端筛选，预计 8-12h）
- ANALYZING 1：`carr_fullft_lr2e5_nocuration_01`（cuda:0 已释放，等 Worker 提取指标后推 DONE）
- DONE 11：success 2 / negative 3 / failed 4 / killed 1

**等待中**：
1. Worker 回调：analysis_carr_fullft_lr2e5_nocuration_01（提取指标）
2. Cron：carr_fullft_lr2e5_k16_probe_01（K=16 实验完成回调）
3. cuda:0 当前空闲——nocuration 分析完成后应立即铺下一个任务或向 Director 汇报

### 4. 📋 待办
- Worker 回调到达 → 提取 metrics → update_registry(metrics+conclusion) → 推 DONE → 与 curation 版(lr2e5_probe_01)对比 → 汇报 Director
- K=16 cron 回调到达 → spawn Worker 提取指标 → 这是最关键的数据点：collapse 概率约 20%，成功则论文有 boundary finding，失败则全 negative
- cuda:0 空闲 → 向 Director 汇报空闲状态，建议铺论文准备 CPU 任务（outline、Table 1 数据整理、literature_map 补全）
- 所有 P1 实验完成后 → 整理完整实验数据表格（论文 Table 1）→ 启动 Paper Agent

### 5. 🎯 战略上下文
- **核心结论**：5/5 配置 curation 均不导致 diversity collapse，项目已从"验证 collapse 存在"pivot 到"Direction D: Negative Result Empirical Study"
- **论文 framing**：EMNLP 2026 ARR（DDL 2026-05-25，还剩 8 天），"Does reward-based curation cause diversity collapse? Systematic evidence of surprising resilience."
- **决策链**：D004(P1 FAIL) → D007(K=8 也 FAIL，LoRA=artifact) → D008(Full-FT FAIL) → D009(5/5 全 FAIL) → D011(Direction C FAIL，正式切 Direction D)
- **K=16 是最后一个实验数据点**：collapse → boundary finding 大幅加强论文；no collapse → 全 negative，需要更强的 framing 和 actionable takeaway
- **易错**：LoRA 实验的 3pp Vendi gap 是 LoRA capacity artifact（D007 已确认），不是 curation 因果效应——论文叙事中必须区分
- **已验证无效的路**：Direction C（CARR multi-reward rebalancing）干跑 99.3% overlap，proxy scores 太相关，路不通


---
