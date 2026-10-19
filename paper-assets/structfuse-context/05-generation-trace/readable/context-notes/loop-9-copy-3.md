# reviewer / loop_9.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`534091864d99417a1dc9.json`](../../sessions/53/534091864d99417a1dc9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T04:11:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：bjb1-42106 的 cuda:0 和 cuda:1（历史上有两次越界到 cuda:4/5 和 cuda:0 被 CRITICAL，D005/D012）
- M2 训练数据使用 BM25 排序（非 embedding distance），论文描述已在 D041 修正为 BM25，**不要回退到旧的 embedding similarity 描述**
- plan_005_stratified 的 R@1 metrics 全部是 dry-run mock predictions（D039 确认），**禁止引用为真实实验结果**，仅 cross_tabulation.csv 分布结构有效
- Checkpoint 选择标准统一用 R@1（D036），不用 val_loss 作 primary criterion
- Claim 2 已降级为 exploratory observation（D035），不可作为核心贡献声明

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106(root)，工作目录 /root/structfuse（训练代码）+ /root/structfuse-context（评估脚本）
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：Qwen → /root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B；StarCoder → /root/autodl-tmp/models/bigcode/starcoder2-3b/
- 训练数据：/root/autodl-tmp/structfuse/full_m2_training_data/（含 BM25 数据 train_bm25_s{42,43,44}.jsonl）
- Checkpoints：/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/ 和 m2_full_starcoder/
- 评估脚本：/root/structfuse-context/evaluation/{evaluate_pool50.py, analyze_stratified.py}
- 活跃进程（截至 handoff）：
  - cuda:0 PID 122645：Qwen embedding_distance_s43（tmux=m2_full_qwen，已完成 random×3 seeds）
  - cuda:1 PID 519805：StarCoder random_s43（tmux 内，已完成 random_s42）
  - BM25 watchers：PID 560698/560714，分别监控 Qwen/StarCoder chain 完成后自动启动 BM25 训练
  - M1 reextract v2：4 CPU workers 运行 CodeQL（pydicom/conan/MONAI/moto），~87% 完成

### 3. 📊 当前状态
刚审完两个 worker：
1. **worker_fix_experiments-v1-placeholders** → PASS：plan_005 dry-run v5 通过，evaluate_pool50.py 260行已验证，数据预处理完成，等 M2 checkpoint
2. **worker_doc_mining-impl-diff** → PASS：D041 paper_framing.md 修正确认与 build_m1_training_data.py BM25 实现一致，¬reachable_G formal definition 修正正确

Registry RUNNING/PREPARING：
- **m2_full_qwen_continued** (RUNNING)：Qwen 9-run chain，当前 embedding_distance_s43 (4/9)，ETA ~50-55h
- **m2_full_starcoder_resumed** (RUNNING)：StarCoder 8-run chain，当前 random_s43 (2/8+)，ETA ~55-65h
- **m1_reextract_v2** (RUNNING)：CPU CodeQL 重提取，87%→ETA May 15 17:00-19:00 CST
- **plan_005_stratified** (PREPARING)：等 M2 checkpoint 就绪后执行

Queued：plan_018_bm25 Phase 2（GPU）、plan_015_dynamic

### 4. 📋 待办（条件触发式）
- M2 Qwen random s42/s43/s44 全完成（已完成）+ embedding/dataflow seeds 完成 → 核实 3-seed R@1 一致性 + 检查 early stopping 行为
- M2 任一 subrun 完成 → cron 回调到来时，独立核实 registry metrics 是否与日志/wandb 一致
- m1_reextract_v2 完成 → 核实 all.jsonl 行数是否达到预期 ~44K，检查 moto timeout 对总量的影响
- plan_005_stratified 转 RUNNING → 核实使用真实 checkpoint 而非 dry-run mock
- BM25 watcher 触发 Phase 2 训练 → 核实 CUDA_VISIBLE_DEVICES 正确、数据路径指向 train_bm25_*.jsonl
- 若 plan_015 恢复执行 → **必须先核实 `hard_negative_mining.py` DataFlowAwareMiner 排序方法是否已从 embedding distance 改为 BM25**，否则 static vs dynamic 对比存在 ranking method confound

### 5. 🎯 战略上下文
- **核心结论链**：embedding > random 跨编码器一致 (+1.6-2.0pp, D017)；dataflow 降级为 exploratory (D035)；paper 转型为 systematic analysis + mechanistic insight (D024)
- **DDL**：ARR May 25。M2 ETA ~May 17-18 → post-M2 实验 ~1.7天 → 写作 ~May 20-24
- **最容易判断错的事**：
  1. Registry 中 m2_full_starcoder 状态是 DONE(failed) 但实际 StarCoder chain 仍在跑（由 m2_full_starcoder_resumed 接管，PID 519791→519805）
  2. m2_full_qwen 状态是 ANALYZING 但实际 chain 仍在跑（由 m2_full_qwen_continued 接管，PID 337267→122645）
  3. `hard_negative_mining.py` 的 DataFlowAwareMiner 用 embedding distance，但 M2 实际训练数据用 BM25（build_m1_training_data.py）——代码和论文描述已分别修正，不要混淆
  4. Qwen random_s44 best_R1=0.6009 异常高（s42=0.5527, s43=0.5554），M2 完成后需要特别关注这个 outlier seed 是否拉高了 mean
  5. Go/no-go 阈值（D019）已在结果前锁定：bootstrap 95% CI + paired t-test，不允许事后修改


---
