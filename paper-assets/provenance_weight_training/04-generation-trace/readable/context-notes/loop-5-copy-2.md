# agent / loop_5.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`58da5d1318c21db4d897.json`](../../sessions/58/58da5d1318c21db4d897.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-14T20:24:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-47453 cuda:0/1/2/3，4 张全用。无其他服务器
- 输出目录必须在 `/root/provenance_weight_training/output/`（根分区只 30GB，D008 教训）
- submit_training_job 命令必须包含 `--eval_data_path data/human/eval_holdout.jsonl --eval_steps 500`（b=2.0/3.0 seed123 曾漏掉 eval 参数，需补跑 eval_perplexity.py）
- 禁止在关键训练运行时共享 GPU 跑诊断/eval（D010 教训：显存打满导致训练速度减半）
- Drayson et al. (EMNLP 2025) 用同公式 w=(1-q)^b（D013），论文必须明确区分 novelty（我们的贡献是 adaptive b* 替代 grid search，不是 weighting 公式本身）
- train_loss 跨方法不可比（weighted CE vs unweighted CE），只能用 held-out eval PPL 对比

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453，4× RTX 6000 Pro 96GB
- 工作目录：`/root/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`，conda base 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- 数据：`data/scored_data.jsonl`（371499 条，含 q-score）、`data/human/eval_holdout.jsonl`（~4.08M tokens）
- Eval 脚本：`eval_perplexity.py`（每次 ~44 min，67823 samples）
- 检测器：`output/detector_tfidf/`（AUC=0.939, ECE=0.048, T=0.204）
- 活跃进程：
  - `grid_b_seed42_batch` — PID 50134, tmux=grid_b_seed42_batch, cuda:0, b=2.0 done / b=3.0~70%
  - `adaptive_fix_seed42` — PID 126796, tmux=adaptive_fix_seed42, cuda:1, 从 checkpoint-1500 恢复
  - `adaptive_fix_seed123` — PID 126939, tmux=adaptive_fix_seed123, cuda:2, 从 checkpoint-1500 恢复
  - `adaptive_fix_seed456` — PID 127280, tmux=adaptive_fix_seed456, cuda:3, 从 checkpoint-1000 恢复
- Cron：4 个活跃（与上述 4 个实验一一对应），reconcile 确认全部 still running

### 3. 📊 当前状态
所有 4 张 GPU 都在跑，处于"等回调"阶段。

**RUNNING (4)**:
- `grid_b_seed42_batch` (cuda:0) — seed42 的 6 个 b 值串行跑，b=0.5/1.0/1.5/2.0 已完成，b=3.0 约 70%，b=5.0 待跑。估计还需 ~6-8h
- `adaptive_fix_seed42` (cuda:1) — D012 修复版（n_min=2, 无 EMA），从 step 1500 恢复，总 6103 步。估计还需 ~5-6h
- `adaptive_fix_seed123` (cuda:2) — 同上，从 step 1500 恢复
- `adaptive_fix_seed456` (cuda:3) — 同上，从 step 1000 恢复（多跑 500 步）

**上一轮 adaptive_fix 曾因 EXIT_CODE=2 失败**（shell syntax error），已清理后重提交成功（从 checkpoint 恢复）。registry 中 adaptive_fix 的 `reproduce.finished_at` 是旧失败时间，不要误判为已完成。

**QUEUED (7)**: grid_b seed456 全 6 值 + detector_modernbert。需等 GPU 空出。
**KILLED (3)**: adaptive_v2 三 seed（D012 修正后取消，改用 adaptive_fix）。

**已完成关键结果**:
| 方法 | seed42 | seed123 | seed456 |
|------|--------|---------|---------|
| uniform | 17.69 | 17.69 | 17.70 |
| grid b=0.5 (best) | 待完成 | 17.638 | 待完成 |
| adaptive (n_min=3) | 17.69 | 17.63 | 17.64 |
| adaptive_fix (n_min=2) | RUNNING | RUNNING | RUNNING |

### 4. 📋 待办（条件触发式）
- adaptive_fix 3 seeds 任一完成 → spawn worker 收集 eval_ppl + b* 轨迹，update_registry metrics
- adaptive_fix 3 seeds 全完成 → 汇总 vs uniform / vs grid-best / vs adaptive(n_min=3)，判定 n_min fix 有效性
- grid_b_seed42_batch 完成 → 提取 6 个 b 值 PPL，确认 seed42 是否也 b=0.5 best
- 上述两项全就绪 → **MVP PASS/FAIL 判定**：adaptive_fix 均值 ≥ 90% grid-best 改善量（即 adaptive_fix PPL ≤ uniform - 0.9×(uniform - grid_best)）
- MVP PASS → 启动 post-mvp-kickoff（paper_framing → experiment_plan → dream_simulate）；grid_b seed456 排队上 GPU
- MVP FAIL → 产出 Framing 调整提案（red-section skill），禁止默默开下一轮
- grid_b2_0_seed123 和 grid_b3_0_seed123 缺 eval → 需补跑 `python eval_perplexity.py --model_path output/models/grid_bX_0_seed123/final/ --data_path data/human/eval_holdout.jsonl`（已在 registry 有 checkpoint_path）。当前 GPU 全满，等有空闲 GPU 时补
- seed123 best-b 在边界(0.5) → 若 seed42 也是边界 → 考虑扩展 grid 到 b=0.1/0.2/0.3

### 5. 🎯 战略上下文
**核心论点**：自适应 b*（基于 α_eff 理论）能免 grid search 达到可比甚至更优的 PPL。这是区别于 Drayson et al. 的新颖性所在。

**决策链关键节点**：
- D011: seed42 adaptive 零改善 → 诊断为 n_min=3 钳制 ESS → D012 修复 n_min=2
- D017: D012 勘误——实际只改了 n_min=2，无 EMA（EMA 代码未写入）。所以 adaptive_fix 与 adaptive 的唯一差异是 n_min(3→2)
- D018: 撤回 D016 混淆变量警告——确认 v1→v2 唯一差异就是 n_min

**最容易判断错的事**：
1. 不要看 registry 中 adaptive_fix 的 `reproduce.finished_at`（~17:38）以为训练已结束——那是旧失败时间，实验已重新提交且 cron 确认 still running
2. PPL 差异很小（0.05-0.3%），不要轻易下"显著改善"结论。必须 3 seeds 汇总后统计
3. Grid-b PPL 随 b 单调递增（seed123 确认），最优在搜索边界 b=0.5。如果 adaptive_fix 的 b* 集中在 0.2-0.8 区间则论文 story 成立；如果 b* 偏高则 story 有危险
4. 投稿日 May 25 距今 11 天，Day 2/12。MVP 判定是关键路径——不要在 MVP 未定之前启动 full experiment matrix 或 paper writing
5. concentration bound (`weighting/alpha_eff.py::compute_concentration_bound()`) 是理论加分项但标记为 full paper 方向，MVP 阶段不碰


---
