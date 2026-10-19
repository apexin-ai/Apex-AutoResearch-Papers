# director / loop_6.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`3016018ee23e22b14782.json`](../../sessions/30/3016018ee23e22b14782.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-14T19:05:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 cuda:0 和 cuda:1（bjb1-42106），两卡都在跑 M2 full runs，**禁止 kill 正在运行的训练进程**
- BM25 Phase 2 有 tmux watcher 自动触发，**不要手动启动 BM25 训练**——等 watcher 检测到 M2 链完成后自行启动
- Claim 2 已降级为 "exploratory observation with testable prediction"（D035），**不要再用 "conditional benefit" 的强 claim**
- Dream median=WR 由不可修复因素驱动（novelty/effect-size/n=2），决策是继续推进而非换目标（D034），**不要因 median=WR 建议降级会议**
- plan_007-012, plan_014 已 defer 到 camera-ready，**不要审批这些实验**

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (connect.bjb1.seetacloud.com)，账号 root
- GPU：2× RTX PRO 6000 96GB（cuda:0, cuda:1）
- 工作目录：/root/structfuse
- Python：需探测（可能 conda 或 venv，aml-train 镜像用 /root/miniconda3/bin/python）
- 活跃进程：
  - cuda:0: Qwen M2 remaining runs (PID 337267)，sequential chain: random_s44 + embedding×3 + dataflow×3
  - cuda:1: StarCoder M2 8 runs (PID 519791)，sequential chain: random×2 + embedding×3 + dataflow×3
  - m1_reextract_v2: 后台运行（~80% done, ETA today）
- BM25 watcher: 两个 tmux session 分别监控 cuda:0/cuda:1 链 PID，完成后自动触发 plan_018 Phase 2 训练
- M2 ETA: ~May 17

### 3. 📊 当前状态
**刚做完的**：
- D035 post-M2 优先级排序：P0(plan_003 SWE-bench + plan_018 BM25) → P1(plan_004 + plan_019 + plan_005)
- plan_017 literature comparison 完成（8 papers, citations verified, Discussion v2 drafted）
- plan_018 BM25 Phase 1 完成（数据就绪，3 seeds aligned, overlap 分析完成）
- neg_difficulty 可视化完成（margin/similarity/heatmap 3 张图）
- Dream 两轮分析完成（D029 + D030），行动项已持久化
- Checkpoint selection criterion + K documentation 完成

**RUNNING**：
- m2_full_qwen_continued — Qwen 剩余 7 runs (random_s44 + embedding×3 + dataflow×3)
- m2_full_starcoder_resumed — StarCoder 全 8 runs (random×2 + embedding×3 + dataflow×3)
- m1_reextract_v2 — 恢复 28,276 failed instances (~80%)

**等待中**：
- plan_018 Phase 2: tmux watcher 自动触发，无需手动干预
- plan_003 SWE-bench: dry-run 通过，等 M2 best checkpoint
- plan_015 dynamic: 缩减为 1 seed (Qwen, s42, ~11h)，排队等 GPU

### 4. 📋 待办（条件触发式）
- M2 full runs 完成 (~May 17) → BM25 watcher 自动启动 Phase 2 训练 → 同时启动统计检验（bootstrap CI + paired t-test）
- M2 best checkpoint 出来 → 立即启动 plan_003 SWE-bench eval（需确认 LLM API key 是否就绪，可能需要 Qwen3.6-27B key）
- plan_003 完成 → 启动 plan_016 bootstrap CI + plan_011 failure analysis
- plan_018 Phase 2 完成 → 分析 BM25 vs embedding R@1 差异 → 决定叙事方向（harm→correction / neutral→systematic comparison）
- GPU 空出后（~May 19）→ 并行启动 plan_004 RepoBench-R + plan_019 pool size sensitivity
- plan_005 分层分析 0 GPU → 可在 M2 完成后立即做（需 M2 checkpoints re-eval）
- 所有 P0+P1 完成 (~May 19-20) → 启动论文写作（Paper Agent Full Draft）

### 5. 🎯 战略上下文
- **核心结论**：Embedding-distance mining consistently improves contrastive code retrieval (+1.6-2.0pp R@1)。BM25 baseline 将 empirically close CoCoHaNeRe correction argument。Structure-grounded negatives (dataflow) 效果 conditional on representation saturation（n=2, exploratory）
- **决策链关键**：D029/D030 Dream 分析 → D031-D033 BM25 overlap 分析 → D034 继续推进决策 → D035 post-M2 优先级 + Claim 2 降级
- **最易判断错的事**：
  1. m2_full_starcoder 之前标记为 failed（cron timeout），但实际 PID 519791 仍在运行——m2_full_starcoder_resumed 是其续接实验，**不要重复启动 StarCoder 训练**
  2. M2 Qwen 类似：cron 在 s42 退出时标记为 ANALYZING，但 chain 仍在运行——m2_full_qwen_continued 是续接
  3. BM25 Phase 1 overlap 数据：top-7 overlap 远低于 k=50 的 87%（D033 修正了 D031），大 repo overlap 更低——叙事要据此调整
- **ARR May 25 DDL**：时间线 M2(~May 17) → post-M2 experiments(~May 19) → writing(~May 20-24)。2 GPU 并行 post-M2 总 ~40h real ≈ 1.7 天，可行但紧
- **审稿进行中**：review_chat_id 已配置，Group C 独立处理。Research Director 专注实验推进
- **写作提分路径**（Best R1 目标 5/6）：checkpoint criterion + K documented ✅, Claim 2 降级 ✅, 剩余：both checkpoint criteria 结果 / 34% structural coverage 分层 / related work 25+ citations / CI + p-value / sub-group CI


---
