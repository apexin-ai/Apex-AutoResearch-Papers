# agent / loop_8.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`b68d4a426d7f26e6e78c.json`](../../sessions/b6/b68d4a426d7f26e6e78c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T01:06:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `cuda:0` 和 `cuda:1`（bjb1-42106），之前在 cqa1 犯过 cuda:0 越界（D005），绝不能用白名单外 GPU
- M2 checkpoint 选择用 **R@1** 而非 val_loss 作为 primary criterion（D036）；checkpoint 只存 LoRA adapter weights，不存 merged model（D037）
- m1_reextract_v2 数据（~44K）**不重跑 M2**——ARR May 25 DDL 不允许再加 4-5 天重训（Director Session 8 决策）
- Claim 2 已降级为 "exploratory observation with testable prediction"（D035），不可在论文中按 hard claim 写
- BM25 Phase 2 watcher 启动的训练不经过 submit_training_job，链完成回调中必须补注册 cron

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-42106，2× RTX PRO 6000 96GB
- **工作目录**: /root/structfuse
- **Python**: /root/miniconda3/bin/python（conda base 环境，不是 venv）
- **数据**: /root/autodl-tmp/structfuse/full_m2_training_data/（11,308 train records/seed）
- **M1 产出**: /root/autodl-tmp/structfuse/full_m1_data/（reextract v2 追加中，已有 44,173 行 all.jsonl）
- **BM25 数据**: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl（Phase 1 已就绪）
- **Log 目录**: /root/runs/structfuse-context/
- **活跃进程**:
  - PID 337267: Qwen M2 chain（cuda:0），tmux session，cron 监控 m2_full_qwen_continued
  - PID 519791: StarCoder M2 chain（cuda:1），tmux session，cron 监控 m2_full_starcoder_resumed
  - m1_reextract_v2: 4 CPU workers（无 GPU），cron 监控
  - tmux `bm25_qwen_watcher` / `bm25_starcoder_watcher`: 每 5min 检查链 PID 存活，退出后自动触发 BM25 Phase 2 训练

### 3. 📊 当前状态
**RUNNING (3)**:
- **m2_full_qwen_continued** (cuda:0): random_s44 进行中 step 1500/2810 (~53%)。s42 best R@1=0.5527, s43 best R@1=0.5554。2/10 runs done。
- **m2_full_starcoder_resumed** (cuda:1): random_s43 进行中 step 1050/2810 (~37%)。s42 best R@1=0.4604（严重过拟合 3 epochs）。1/8 subruns done。ETA 整体 ~60-65h (~May 17)。
- **m1_reextract_v2** (CPU): ~80% done (22,842/28,276)，ETA ~May 15 18:00-23:00 CST。产出为独立 .json 文件，尚未合并 all.jsonl。

**QUEUED (2)**: plan_018_bm25 (BM25 Phase 2), plan_015_dynamic (dynamic negative mining)
**PREPARING (1)**: plan_005_stratified（脚本就绪，等 M2 checkpoint）

**Worker 池**: 0 running（当前无 CPU 任务需要 Worker，GPU 满载链式训练中）
**等待中**: 无 pending Worker 回调。3 个 cron 正常运行。

### 4. 📋 待办（条件触发式）
- **m2_full_qwen_continued 链完成 (cron 回调)** → spawn worker 做统计检验 (paired t-test across 3 seeds × 3 strategies) → 更新 registry metrics → 汇报 Director
- **m2_full_starcoder_resumed 链完成 (cron 回调)** → 同上，cross-encoder 对比 Qwen 结果（embedding > random 是否 encoder-agnostic）
- **BM25 tmux watcher 触发 Phase 2 训练** → 检测到训练启动后，补注册 cron（watcher 绕过 submit_training_job），更新 registry plan_018_bm25 → RUNNING
- **m1_reextract_v2 完成 (cron 回调)** → 合并 .json → 统计最终数据量 → 更新 registry → 汇报 Director（不重跑 M2，留 camera-ready）
- **M2 全部完成 (~May 17)** → plan_003 SWE-bench eval (P0, 40h) + plan_018 Phase 2 BM25 (P0, 15h) 双卡并行启动。需要 LLM API key (Qwen3.6-27B) for plan_003，dry-run 确认中
- **plan_005_stratified 可提前做 (0 GPU)** → M2 best checkpoints 出后立即用 analyze_stratified.py 跑分层分析，脚本已就绪

### 5. 🎯 战略上下文
- **核心结论**: embedding-distance mining consistently improves R@1 (+1.6-2.0pp)，跨 Qwen/StarCoder 两编码器。Dataflow 效果 encoder-dependent（Qwen +0.8pp, StarCoder -0.5pp），D035 降级为 exploratory。
- **决策链**: D035 Claim 2 降级 → D036 R@1 为 primary criterion → D037 只存 LoRA adapter → D038 plan_005 需控制 pool_size → D039 分层 R@1 mock 数据无效 → D040 Claim 1 framing 微调
- **易错点**:
  1. 不要把 plan_005 dry-run 的 mock R@1 当真实数据引用（D039 已标记无效）
  2. StarCoder s42 用了 3 epochs（过拟合），s43+ 改为 2 epochs（D026）——对比时注意 epoch 差异
  3. BM25 k=50 全候选重叠 87% ≠ top-7 训练 Jaccard 30-38%（memory.md D033 修正），不要用 87% 预测 Phase 2 结果
  4. Bash 预读陷阱：运行中的 bash chain 脚本修改磁盘文件无效，已在链外部署 tmux watcher 作为 workaround
  5. 时间线：M2 ~May 17 → post-M2 实验 ~May 19 → 写作 May 20-24 → **ARR May 25**，每一天都是关键路径


---
