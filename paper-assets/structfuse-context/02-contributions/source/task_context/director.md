---
loop: 12
reason: max_messages
updated: '2026-05-16T11:03:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0, cuda:1（bjb1-42106 项目配置白名单）
- UniXcoder 用 conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不是 venv
- BM25 checkpoint 输出路径 `/root/autodl-tmp/structfuse/full_m2_outputs/bm25_s42/` 与 Qwen 主路径 `checkpoints/m2_full_qwen/` ��同，评估脚本需显式传入或建 symlink
- D061 (统一 val_loss 选 checkpoint) 已被 D062 supersede，禁止引用 D061 作为 checkpoint 选择依据
- pool=8 R@1 数据不可靠（D060 确认 ±0.5pp 噪声），所有 claim 对比必须用 pool=50 数据

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (connect.bjb1.seetacloud.com), 用户 root
- 工作目录：`/root/structfuse`（代码）, `/root/autodl-tmp/structfuse/`（checkpoint/数据）
- Python：`/root/miniconda3/bin/python`（aml-train 镜像，conda base）
- Checkpoint 路径：Qwen → `checkpoints/m2_full_qwen/{strategy}_s{seed}/`; StarCoder → `checkpoints/m2_full_starcoder/`; UniXcoder → `full_m2_unixcoder_outputs/`
- 活跃进程：
  - Qwen 主链 PID 337267 (cuda:0, dataflow_s44, 7/9)
  - StarCoder PID 519791 (cuda:1, embed_s43, 5/8)
  - UniXcoder s43 PID 168000 (cuda:0 共享, random_s43 running)
  - D062 eval PID 158647 (cuda:1 共享, 3/14 checkpoints done)
  - Qwen supplement watcher PID 966920（主链完成后自动触发 embed_s42+dataflow_s42+bm25_s42）

### 3. 📊 当前状态
刚处理完：UniXcoder s42 完成（null result）、D062 query split 第三次尝试成功、修复 UniXcoder s43 conda bug 并重启、kill 重复 D062 eval + 暂停 RepoBench eval 解决 cuda:1 过载。

Registry RUNNING：
- `m2_full_qwen_continued` — Qwen 3-strat 主链 7/9，ETA May 17
- `m2_full_starcoder_resumed` — StarCoder 5/8，ETA May 18
- `unixcoder-3strat-s43` — 刚启动，~3h
- `unixcoder-3strat-s44` — 链式等 s43 ��成后自动启动

等待中：
- D062 eval 完成回调（3/14 done, ~8h remaining）→ 解锁 stratified analysis + bootstrap CI
- Qwen 主链完成 → watcher 自动触发 supplement chain (embed_s42 + dataflow_s42 + bm25_s42)

### 4. 📋 待办
- D062 eval 14 checkpoint 全部完成 → 立即推 plan_005 stratified analysis + bootstrap CI + 重启 RepoBench-R eval
- UniXcoder s43/s44 完成且均 null (Δ<1pp) → ���过 UniXcoder pool=50 eval，paper 报 pool=8 null + footnote
- Qwen supplement chain 完成 (embed_s42) → 这是 Claim 1 的 swing vote，决定 aggregate delta 正负
- StarCoder ��完成 → BM25 Phase 2 watcher 自动触发; 同时启动 pool sensitivity (plan_019)
- GPU 空闲 → 温度 ablation 缩减版 (plan_021: τ=0.05,0.2 × Qwen × s42)
- random_s42 retrain 脚本已就绪 → 先空先跑（cuda:0 或 cuda:1 先释放的那个）

### 5. 🎯 战略上下文
- **Paper**: "What Makes Hard Negatives Work for Code Retrieval?" → EMNLP 2026, ARR May 25
- **核心发现**: Mining 效果是 architecture/scale-dependent（Qwen +, StarCoder -, UniXcoder null）
- **D059 dual-track narrative**: Track A = stratified heterogeneity (when does mining help), Track B = explain small aggregate delta
- **最大风险**: D062 eval 是 Claim 2 全部进展的唯一阻塞点；StarCoder embedding < random 挑战 Claim 1 跨架构泛化
- **易错点**: (1) 别用 pool=8 数据做任何 claim 对比 (2) checkpoint 选择必须用 D062 query split 方法，不能用 D061 的 val_loss (3) StarCoder bm25 从未在日志中出现过（之前有幻影记录），不要引用 (4) Agent 有时虚报 Worker 成功，重要任务需 Reviewer 独立核实
- **决策链**: D059(dual-track) → D060(pool=8不可靠) → D062(query split) → D063(缺口补充) → D064(UniXcoder null支撑TrackB)
