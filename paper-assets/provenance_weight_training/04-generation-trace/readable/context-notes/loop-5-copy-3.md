# reviewer / loop_5.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`e18f04f14913084e9249.json`](../../sessions/e1/e18f04f14913084e9249.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-14T20:23:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目使用 4 张 GPU（cuda:0-3），无 constraints.yaml 限制，但需核对 registry spec 中 gpu 字段与实际 CUDA_VISIBLE_DEVICES 一致
- adaptive_fix 系列实验**不带 inline eval**（`--eval_data_path` / `--eval_steps`），这是 D012 后统一决策。如果发现某 seed 带了 inline eval 而其他没带 → 立即 flag 不一致
- Registry 曾多次出现 status=DONE/failed 但实际进程还在跑的情况（本轮发生 3 次），审查时**必须 SSH 交叉验证 GPU 进程**，不能只信 registry status
- D012 描述"n_min fix + EMA"但实际代码**无 EMA**（D017 勘误确认），论文中不能声称使用了 EMA

### 2. 🖥️ 基础设施快照
- 服务器：`westd-47453`，账号 `root`，工作目录 `/root/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型：`/root/provenance_weight_training/models/Qwen/Qwen3-0.6B`
- 数据：`data/scored_data.jsonl`（371499 条，TF-IDF q-score），eval holdout：`data/human/eval_holdout.jsonl`
- WANDB：DISABLED（`WANDB_MODE=disabled`），不检查 W&B
- 活跃进程（截至 handoff）：
  - GPU 0: PID 112475 — `grid_b3_0_seed42`（grid_b_seed42_batch 的一部分，已完成 b=0.5/1.0/1.5，当前 b=3.0）
  - GPU 1: PID 126801 — `adaptive_fix_seed42`（从 checkpoint-1500 恢复）
  - GPU 2: PID 126944 — `adaptive_fix_seed123`（从 checkpoint-1500 恢复）
  - GPU 3: PID 127285 — `adaptive_fix_seed456`（从 checkpoint-1000 恢复）
- 所有 4 张卡均为 NVIDIA RTX PRO 6000 Blackwell (98GB)，VRAM 各约 46.5GB

### 3. 📊 当前状态
本轮主要工作：审查 `adaptive_fix_seed123` on_failed 触发的 cron 告警。发现并上报：
1. seed42 有两个重复进程 → Worker 已清理
2. seed123/456 带 inline eval 而 seed42 不带 → Worker 已统一为全部无 inline eval 并重提交
3. Registry 状态为 DONE/failed 但实际在跑 → Worker 最终更新为 RUNNING
4. GPU 1 报 100% util / 0 MiB 异常 → 重提交后恢复正常

Registry RUNNING 实验：
- `adaptive_fix_seed42` / `seed123` / `seed456`：D012 n_min=2 修复版 adaptive b*，~25-28% 进度
- `grid_b_seed42_batch`：6 个 b 值串行跑，已完成 0.5/1.0/1.5，当前 b=3.0

无等待中的 Worker 回调或 Director 决策。

### 4. 📋 待办（条件触发式）
- adaptive_fix_seed{42,123,456} 任一完成 → 立即审查：(1) 最终 PPL vs uniform baseline（17.69/17.69/17.70），(2) 与旧版 adaptive（n_min=3）的对比，(3) 3-seed 一致性（D011 要求无 seed 劣于 uniform）
- grid_b_seed42_batch 完成（b=3.0/5.0 剩余）→ 审查 grid-b 全矩阵：seed42 的 best-b 是否与 seed123 一致（seed123 best-b=0.5, PPL=17.638）
- 训练完成但无 inline eval → 需补跑 post-training eval（`--eval_data_path data/human/eval_holdout.jsonl`），确认 Worker 有 eval 脚本（`scripts/run_eval_seed42.sh` 已存在）
- 3-seed adaptive_fix + 3-seed grid-b 全部出齐 → 进行 MVP PASS/FAIL 判定（D011 暂缓的判定）

### 5. 🎯 战略上下文
- 核心假设：adaptive b*（α_eff 理论推导）能免 grid search 达到 comparable PPL。D013 发现 Drayson et al. (EMNLP 2025) 已用同一公式 w=(1-q)^b，我们的差异化是 adaptive b* + lightweight detector
- D014 确认 Path B framing（"comparable + eliminates grid search cost"）而非 Path A（"outperforms"）
- seed42 是高风险种子：旧版 adaptive（n_min=3）零改善（PPL=17.69 = uniform），D012 修复后是否改善是 MVP 关键数据点
- 易踩坑：(1) step_metrics.jsonl 混合了 train+eval 条目，分析时必须过滤（D018）；(2) conclusion 字段残留旧值"failed"即使 status 已改 RUNNING；(3) 本项目 WANDB 已禁用，不要花时间查 W&B


---
