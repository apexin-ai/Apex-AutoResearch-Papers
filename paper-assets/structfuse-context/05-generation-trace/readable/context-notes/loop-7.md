# director / loop_7.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`f0cbba53f8eb12dd8d78.json`](../../sessions/f0/f0cbba53f8eb12dd8d78.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-14T23:54:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 仅限 cuda:0, cuda:1（bjb1-42106 上分配的两张 RTX PRO 6000 96GB）。D005 教训：曾越界用了 GPU 5 被 CRITICAL
- M2 训练链正在跑（cuda:0 Qwen PID 337267, cuda:1 StarCoder PID 519791），**不得 kill**——每条链包含多个 sequential runs，cron watcher 监控中
- BM25 Phase 2 有 tmux watcher 自动触发，M2 跑完会自动开始，不要手动抢占
- Claim 2（dataflow negatives）已降级为 exploratory observation（D035），不要按 established finding 措辞
- 审稿由 Group C 独立负责（review_chat_id: oc_2a0777e0289fb54872621f6b14e6e4ee），你不参与格式/投稿材料

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (connect.bjb1.seetacloud.com)，账号 root
- 工作目录：/root/structfuse
- GPU：2× RTX PRO 6000 96GB (cuda:0, cuda:1)，满载 M2 训练
- 活跃进程：
  - cuda:0: m2_full_qwen_continued (PID 337267) — random_s44 + embedding×3 + dataflow×3 sequential chain
  - cuda:1: m2_full_starcoder_resumed (PID 519791) — 8 sequential runs (random×2 + embedding×3 + dataflow×3)
  - 后台: m1_reextract_v2 (~80% done, CPU only, 修复 28,276 失败 instances)
- tmux: 两个 BM25 Phase 2 watcher session，监控链 PID 完成后自动触发 BM25 训练
- Cron: m2_full_qwen_continued + m2_full_starcoder_resumed 状态 cron 已注册
- 弹性 GPU：未启用
- W&B：未配置

### 3. 📊 当前状态
- **M2 全量训练进行中**：两卡满载，ETA ~May 17。Qwen 在跑 random_s44（链中第一个），StarCoder 在跑 random_s43
- **plan_017 (literature comparison) DONE**：8 papers surveyed, discussion v2 drafted, citations verified
- **plan_018 Phase 1 DONE**：BM25 数据准备完成，3 seeds aligned，stratified overlap 分析完成
- **neg_difficulty 可视化 DONE**：3 张图表（margin/similarity/heatmap）
- **K/checkpoint 文档已更新**：Qwen 4/5 same, StarCoder 0/3 same
- **plan_003 (SWE-bench dry-run)**：worker 验证中，可能需要 LLM API key (Qwen3.6-27B)
- Agent 队列空闲，无 pending 消息
- 审稿阶段进行中（Group C 并行处理）

### 4. 📋 待办（条件触发式）
- M2 两链全部完成 (~May 17) → BM25 watcher 自动启动 plan_018 Phase 2 训练 → 完成后分析 BM25 narrative 方向（D033: harm→correction 或 neutral→systematic comparison）
- M2 完成 → 立即执行统计检验（CI + p-value for all claims）
- M2 best checkpoint 出后 → 启动 plan_003 SWE-bench 正式 eval (40h GPU)
- plan_003 dry-run 报告需要 LLM API key → 用 feishu_send_tum_key_request_card 向用户申请
- Post-M2 第二批：plan_004 (RepoBench-R) + plan_019 (pool size sensitivity) + plan_005 (分层分析, 0 GPU 可提前做)
- m1_reextract_v2 完成 → 确认训练数据量提升（15,897 → ~44,173）
- 所有 post-M2 实验完成 (~May 19) → 启动论文写作 (~May 20-24)，deadline ARR May 25

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 Main, ARR May 25 deadline
- **核心 story**：systematic analysis of hard negative mining for code retrieval。Claim 1（embedding-distance mining suffices, +1.6-2.0pp R@1）是 headline，直接回应 CoCoHaNeRe (TOSEM 2025) 的 gradient-based assumption
- **Dream 评估 (D034)**：re-dream gate 未通过但决定继续——median=WR 由不可修复因素驱动（novelty/effect-size/n=2），目标最大化 Best case（当前 Best=5/6）
- **写作提分路径**：related work 25+ citations、每个 claim 附 CI+p-value、checkpoint criterion+K documented、sub-group 分析标注 underpowered
- **D035 关键决策**：Claim 2 从 "conditional benefit beyond embedding" 降级为 "exploratory observation with testable prediction"（n=2 不足以支撑 established finding）
- **D033 BM25 发现**：top-7 overlap 远低于 k=50 的 87%，大 repo overlap 更低——Phase 2 结果将决定 BM25 叙事方向
- **易错点**：
  - 不要把分层分析 R@1 数据当真实结果（D039：之前 dry-run 用的 mock predictions）
  - M2 checkpoint 选择用 R@1 不是 val_loss（D036）
  - M2 checkpoint 只存 LoRA adapter weights（D037）
  - 40 条决策记录在 decisions.yaml，重大决策链：D001→D008(MVP)→D009(Dream)→D011(Z%=74%)→D035(Claim2降级)→D034(re-dream继续)


---
