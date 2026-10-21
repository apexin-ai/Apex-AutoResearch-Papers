# agent / loop_3.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`39199a6736202c0b5249.json`](../../sessions/39/39199a6736202c0b5249.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T13:27:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3 @ westd-47453，禁止用白名单外 GPU
- auto_eval_watcher.py 已改为动态 GPU 选择（PID 99503），不要再硬编码 EVAL_GPU
- grid_b5_0_seed123 经历过重复进程事故（PID 92798 vs 94717），当前正确 PID=94717，retry_count=2。标记 killed 前必须先 SSH kill 实际进程
- D012（adaptive_v2 代码修改）Director 要求"提交审批，不要直接跑"——代码改完必须走 PENDING 审批流程
- submit_training_job 的 command 必须用 `bash -c "..."` 包裹（tmux 用 sh 不是 bash）

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453，账号 root，项目路径 /root/provenance_weight_training
- Python：/root/miniconda3/bin/python（conda base 环境，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：/root/provenance_weight_training/models/Qwen/Qwen3-0.6B
- 数据：/root/provenance_weight_training/data/scored_data.jsonl（371499 条，40% contamination）
- Eval holdout：data/human/eval_holdout.jsonl（~5000 docs, 4M tokens）
- auto_eval_watcher：PID 99503（动态选最低显存 GPU，MIN_FREE_MB=15000）
- 活跃 cron：grid_b_seed42_batch (pid=grid_b_seed42_batch, cuda:0) / grid_b2_0_seed123 (pid=88022, cuda:1) / grid_b3_0_seed123 (pid=90129, cuda:2) / grid_b5_0_seed123 (pid=94717, cuda:3)
- 准备好的脚本：scripts/submit_grid_b_seed456.sh / scripts/run_eval_seed42.sh

### 3. 📊 当前状态
**刚做完**：seed42 adaptive 诊断（n_min=3 钳制问题确认）+ eval_watcher GPU 修复 + related work survey 补录（28 篇）。收到 D012 指令（修复 adaptive 算法 + 准备 adaptive_v2 重跑），尚未开始执行。

**RUNNING 实验**：
| GPU | 实验 | PID | 预计完成 |
|-----|------|-----|---------|
| cuda:0 | grid_b_seed42_batch（当前 b=2.0, 35%）| 50134 | ~22:00-23:00 UTC 全部 |
| cuda:1 | grid_b2_0_seed123 | 88022 | 预计 ~14:30-15:00 UTC |
| cuda:2 | grid_b3_0_seed123 | 90129 | 预计 ~14:30-15:00 UTC |
| cuda:3 | grid_b5_0_seed123 | 94717 | 预计 ~15:30-16:00 UTC |

**无活跃 Worker**，无待处理回调。

### 4. 📋 待办（条件触发式）
- **立即（D012 未完成）**→ spawn worker 修改 pretrain_weighted.py：n_min 降为 `max(1, batch_size//4)` + 加 EMA 平滑 b*（alpha=0.1）→ 准备 adaptive_v2_seed{42,123,456} 提交脚本 → 提交 PENDING 审批
- grid_b2_0_seed123 cron 回调（cuda:1 释放）→ 收集 eval → 提交 adaptive_v2 最高优先（审批通过的话），否则提交 seed456 grid_b0.5
- grid_b3_0_seed123 cron 回调（cuda:2 释放）→ 同上，第二个 adaptive_v2
- grid_b5_0_seed123 cron 回调（cuda:3 释放）→ 同上，第三个 adaptive_v2
- grid_b_seed42_batch 全部完成 → eval 由 watcher 自动处理 → 更新 registry 全部 seed42 metrics → cuda:0 释放后提交 seed456 grid_b0.5（如果还没跑）
- 所有 grid-b seed123 + seed42 出齐 → 汇总对比表 → 确定 grid-best b 值 → MVP 判定（adaptive_v2 vs grid-best）

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25（11 天后）
- **MVP pass criteria**：adaptive 均值 ≥ 90% grid-best PPL 改善量（相对 uniform）
- **已确认趋势**：b↑ → PPL↑（越差），b=0.5 始终最优，跨 seed 一致。Adaptive（v1）seed123/456 有效但 seed42 失效
- **核心发现（D012 诊断）**：adaptive v1 的 n_min=3 + batch_size=4 导致 ESS 被钳制到 75%，weighting 几乎无效。这不是 adaptive 理论的问题，是工程参数的问题。修复后（adaptive_v2）预期 3 个 seed 都能 work
- **GPU 释放后提交优先级**：adaptive_v2×3 > seed456 grid_b0.5 > seed456 高 b 值
- **易踩的坑**：(1) 不要在 registry 标 killed 而不 SSH kill 进程（已经出过事故）(2) eval watcher 已修为动态 GPU，不要改回硬编码 (3) Drayson et al. (EMNLP 2025) 是最直接前驱，paper 中必须作为核心对比项


---
