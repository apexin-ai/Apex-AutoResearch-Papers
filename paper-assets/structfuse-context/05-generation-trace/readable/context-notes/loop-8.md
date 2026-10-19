# director / loop_8.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`07dca190b8452217a141.json`](../../sessions/07/07dca190b8452217a141.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-15T04:11:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0, cuda:1**（bjb1-42106 分配），D005 记录过 GPU 越界事故
- M2 训练链是 sequential runs（一个跑完自动接下一个），**不要 kill 任何 PID** 除非确认整条链已完成
- BM25 Phase 2 有 tmux watcher 监控链 PID 完成后自动触发，**不要手动启动 BM25 训练**——watcher 会做
- Dataflow-aware 策略论文描述改为 **BM25 排序**（D041），不要按旧描述写 "embedding similarity 排序"
- pool=50 独立评估已替代 pool=8（D042/D043），评估脚本已实现，**不要报告 pool=8 的旧数据**
- 删除了 R@10 报告（D042），只报 R@1

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-42106 (connect.bjb1.seetacloud.com), root
- **工作目录**: /root/structfuse
- **GPU**: 2× RTX PRO 6000 96GB (cuda:0, cuda:1)
- **活跃进程**:
  - M2 Qwen 链: PID 337267, cuda:0 (random_s44 + embedding×3 + dataflow×3 sequential)
  - M2 StarCoder 链: PID 519791, cuda:1 (random×2 + embedding×3 + dataflow×3 sequential)
  - m1_reextract_v2: 后台运行，~80% done (截至 May 14)
  - BM25 Phase 2 watcher: 2 个 tmux session 分别监控两条链 PID
- **Cron**: m2_full_qwen_continued + m2_full_starcoder_resumed 均有 cron 注册
- **审稿群**: review_chat_id = oc_2a0777e0289fb54872621f6b14e6e4ee (Group C 独立运作)

### 3. 📊 当前状态
上一轮主要工作：D035 将 Claim 2 降级为 exploratory observation，D041-D043 修正 dataflow 描述+实现 pool=50 评估+清理 R@10。plan_017 文献调研完成（8 papers, citations verified）。neg_difficulty 可视化完成（3 张图）。

**RUNNING**: m2_full_qwen_continued (cuda:0), m2_full_starcoder_resumed (cuda:1), m1_reextract_v2 (CPU background)
**PENDING**: plan_018_bm25 (Phase 2, 等 M2 完成 watcher 自动触发), plan_015_dynamic (排队), plan_005_stratified (准备中)

**ETA**: M2 两条链预计 ~May 17 完成。M2 完成后 BM25 watcher 自动接管 GPU。

### 4. 📋 待办（条件触发式）
- M2 全部完成 → 统计检验 (paired bootstrap CI, p-value) + pool=50 重评估所有 best checkpoints
- BM25 watcher 自动触发 Phase 2 训练 → 完成后对比 R@1，决定叙事方向 (harm→correction / neutral→systematic)
- plan_003 SWE-bench dry-run 完成 → 确认是否需要 LLM API key (Qwen3.6-27B) → 正式 eval 用 M2 best checkpoint
- M2 + BM25 完成后 → plan_004 (RepoBench) + plan_019 (pool size sensitivity) 并行铺
- plan_005 分层分析 → 0 GPU 可提前做，但需额外控制 pool_size (D038)
- 全部 post-M2 实验完成 (~May 19) → 启动 Paper Agent 写初稿 (目标 ~May 24)
- m1_reextract_v2 完成 → 数据管道数字更新（D043: 等 M1v2 再更新论文中数据量）

### 5. 🎯 战略上下文
- **投稿目标**: ARR May 25，时间线紧凑但可行 (M2~17 → post-M2~19 → 写作~20-24)
- **核心结论**: True embedding-distance mining consistently improves contrastive code retrieval (+1.6–2.0pp R@1)。Z%=74% 确认 Best Framing (D011)
- **Claim 2 已降级** (D035): "dataflow > embedding" 从 core claim 降为 "exploratory observation with testable prediction"，因为 n=2 encoder 不足以支撑强 claim，且 StarCoder pilot 显示 dataflow 效果 encoder-dependent
- **Dream 审稿 median=WR 是固有的** (D034): 由 novelty/effect-size/n=2 驱动，不可修复，目标是最大化 Best case
- **易错点**: (1) 不要把 Claim 2 当 headline——它是 exploratory；(2) BM25 结果决定 Claim 1 的叙事角度，结果出来前不要定 framing；(3) M2 链是 sequential 的，一个 seed 跑完才接下一个，不要因为某个 PID 退出就认为整条链结束；(4) checkpoint 选择用 R@1 不是 val_loss (D036)


---
