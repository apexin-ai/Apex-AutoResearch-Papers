# agent / loop_1.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`6d68be99258d3d2e53d5.json`](../../sessions/6d/6d68be99258d3d2e53d5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T17:10:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- 只能用 **cuda:4**（gpu_ids=[4]），之前 GPU 越界跑 cuda:5 被 Director CRITICAL（D005）
- 训练时的 recall 指标是退化的（pool=4），**不引用不报告**。最终判断只看 eval_p2b.py 的 recall@5（完整候选池）
- 策略名必须用 `embedding_distance` / `dataflow_aware`（不是 embedding/dataflow），之前名称不匹配导致 6/9 runs EXIT_CODE=2
- submit_training_job 必须用 `bash -c "..."` 包装，命令自带环境激活（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- AutoDL 根分区只有 30GB，大文件必须放 `/root/autodl-tmp/`
- train.py 已改为 rolling best+final checkpoint（每 run 最多 ~12GB），**不要恢复中间 checkpoint 保存**

### 2. 🖥️ 基础设施快照
- 服务器：**cqa1-21977**（SSH alias），工作目录 `/root/structfuse`
- Python：`/root/miniconda3/bin/python`，conda base 环境（不是 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型 checkpoint：`/root/autodl-tmp/structfuse/checkpoints/p2b_{strategy}_{seed}/`
- 训练数据：`/root/structfuse/mvp_data/training_data/`（127 instances）
- 基础模型：Qwen2.5-Coder-3B + LoRA，projection head 256-dim
- 磁盘：`/root/autodl-tmp` 约 76GB 可用（清理后），足够 5 runs × 12GB
- CodeQL：`/opt/codeql`（需 export PATH）
- 活跃进程：无确认活跃训练进程（9 runs 中 4 完成、5 失败待重跑）
- Cron：reconcile 返回 0 个活跃 cron

### 3. 📊 当前状态
Director 给了 3 步串行计划，当前进度：

**Step 1 ✅ 完成**：train.py checkpoint 策略已修改（Worker `worker_infra_p2b_disk_cleanup_and_train_fix` done）。4 处变更：import shutil、best_val_loss 初始化、rolling best 覆盖保存（删除中间 ckpt）、磁盘 <15GB 跳过保存。

**Step 2 🔄 Worker 运行中**：`worker_experiment_eval_4runs_v2_20260512T170825` 正在评估 4 个已完成 runs（random_s42/s123/s456 + embedding_distance_s42）的 final checkpoint。之前的 eval Worker 卡死只跑了 random_s42 一个，已取消重派。

**Step 3 ⏳ 待 Step 2 完成**：重跑 5 个失败 runs——dataflow_aware_s42/s123/s456 + embedding_distance_s123/s456。dataflow 优先（核心假设验证）。

Registry：
- `mvp_p2b_contrastive_training` = ANALYZING（4/9 完成，5/9 磁盘满失败）
- `p2b_eval_all` = PREPARING（之前的 submit_training_job 创建的，可能需要清理）
- `mvp_p1_codeql_feasibility` = DONE/success
- `mvp_p2a_linear_proxy` = DONE/success
- 10 个 smoke test entries = DONE/killed（历史残留）

等待回调：`worker_experiment_eval_4runs_v2_20260512T170825`（Step 2 eval）

### 4. 📋 待办（条件触发式）
- eval Worker 回调 → 提取 4 runs 的 recall@1/5/10 表格 → 立即汇报 Director（带 [资源] 行）→ 更新 registry metrics
- Director 确认 Step 2 结果 → 派 Worker 重跑 5 个失败 runs（顺序：dataflow_aware_s42 → s123 → s456 → embedding_distance_s123 → s456），用 submit_training_job 提交
- 5 runs 全部完成 → eval_p2b.py 评估 best+final → 汇总 9 runs 完整结果表
- MVP 判断：≥2/3 seed dataflow_aware recall@5 > random recall@5 ≥ 2pp → PASS → 启动 M1 全量提取（run_m1_extraction.sh 已 ready，3 个 fix 已 applied）
- MVP FAIL → 按 red-section 产 Framing 调整提案，禁止默默跑下一个实验

### 5. 🎯 战略上下文
- **假设链**：H1(CodeQL 可行) ✅ → H2(特征有区分度) ✅ → H3(对比训练增益) 🔄 验证中
- **核心 insight**：词汇相似但数据流不连通的文件是更有效的 hard negatives（正交梯度信号）
- **投稿目标**：EMNLP 2026 ARR deadline 2026-05-25（距今 13 天）
- **已知风险**：random_s42 的 eval recall@1=0.9449 已经很高，dataflow 要 beat 这个 baseline ≥2pp 才算 pass。如果 random baseline 太强（ceiling effect），dataflow 提升空间可能不够
- **embedding_distance_s42 过拟合**：训练 best=0.945 at step 450, final=0.874。重跑时注意 best checkpoint 的 early stopping 效果
- **易错点**：
  - 不要混淆训练时 recall（pool=4，退化指标）和 eval_p2b.py recall（完整候选池，真实指标）
  - run_p2b_all.sh 里策略名必须是 `random embedding_distance dataflow_aware`（全称）
  - `p2b_eval_all` registry 条目是之前 submit_training_job 创建的残留，不是真正的实验
  - batch_extract.py 的 3 个 bug 已修（ClassDef 支持 + min_reachable_files=1 + call_graph.ql Class support），M1 脚本 ready 但不要提前启动


---
