# director / loop_16.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_16.md`
- **Structured JSON:** [`b365da8577a3546f60c4.json`](../../sessions/b3/b365da8577a3546f60c4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_messages
updated: '2026-05-21T18:56:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（westd-41312），绝不使用其他设备
- `scored_data_filtered_q05.jsonl` 必须用 `scripts/filter_high_qscore.py` 生成，生成后验证行数=153,725、depth=0 占 86%+（M055 教训：旧文件方向反转导致结论错误）
- 启动新实验前必须 `df -h /root/autodl-tmp` 检查磁盘（M056 教训：250GB 磁盘被旧 checkpoint 占满导致崩溃）
- eval_perplexity.py 参数：`--checkpoint_paths`（不是 --model_path）、`--data_path`（不是 --eval_data）
- 论文禁止出现："quality vs diversity trade-off"（Reviewer 否决）、"Δ=+0.72"（无效数据产物）、"D&R filtering is worse than uniform"（已证伪）

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312，4× RTX PRO 6000 96GB
- 工作目录：`/root/autodl-tmp/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`（conda base）
- 数据：`data/scored_data.jsonl`（371,499 条全量）、`data/scored_data_filtered_q05.jsonl`（153,725 条，修复后正确版本）
- 磁盘：250GB `/root/autodl-tmp`，刚发生磁盘满事故，Worker 正在清理旧 checkpoint（保留 /final，删除中间 checkpoint-*）
- 活跃进程：
  - cuda:1: `bs16_uniform_seed123`（PID 未确认，tmux=bs16_uniform_seed123）
  - cuda:3: `detect_remove_q05_v2_seed42`（PID 629320，tmux=detect_remove_q05_v2_seed42）
  - cuda:0/2: 空闲
- Worker 正在执行磁盘清理，清理完后重启 `bs16_adaptive_tau07_seed123`（cuda:0）

### 3. 📊 当前状态
**Round 9 审稿 3.0 (Findings)**，目标冲 3.5。EMNLP 2026 ARR May 25 DDL（~2 天）。

Paper Agent 已完成所有论文修改：
- Discussion 扩展 11→50 行 ✅
- Method 压缩 54% ✅
- α_eff discrete/continuous 修正 ✅
- Batch size claim 从 "differences <0.01" 改为正面发现 ✅
- Epoch confound 叙事恢复（D&R v2 作 robustness check）✅
- random_reweight (permuted-score control) 加入 Discussion ✅

等待中的实验：
- `bs16_uniform_seed123`（cuda:1）— B=16 配对实验
- `detect_remove_q05_v2_seed42`（cuda:3）— 正确数据 hard filtering baseline，~1-2h
- `bs16_adaptive_tau07_seed123`（cuda:0）— 待磁盘清理后重启
- 磁盘清理 Worker 回调

### 4. 📋 待办
- 磁盘清理 Worker 完成 → 确认空间 > 50GB → 重启 bs16_adaptive_seed123 (cuda:0)
- detect_remove_q05_v2 完成 → eval (holdout+OWT+Wiki) → 与 adaptive (17.674) 对比，确认 hard filtering vs soft reweighting
- bs16_uniform_seed123 完成 → eval → 计算 seed123 的 Δ(adapt−unif)
- bs16_adaptive_seed123 完成 → eval → 2-seed Δ 均值，决定是否升级 batch size claim
- 所有实验完成 → Paper Agent 最终数据 patch（detect_remove 结果 + B=16 2-seed 数据如果有）→ 编译 → submit_paper_to_review Round 10
- Round 10 后 → 根据评分决定是否还有时间做 Round 11

### 5. 🎯 战略上下文
- **核心叙事**：analysis paper — "when, why, and how detect-and-reweight works"
- **4 个贡献**：(1) Epoch confound >95% (2) Detector requirements: calibration+discrimination (3) Mechanism decomposition: 4-tier hierarchy (4) Adaptive b* tool
- **关键数据**：D&R v2 (17.651) ≈ 原版 epoch-matched (17.657)，差 0.006——确认 epoch confound，LR 不影响。Bootstrap CI 7/7 显著。random_reweight 17.958 > uniform 17.694 → detector signal load-bearing
- **最容易判断错的事**：D&R v2 17.651 vs Uniform 18.062 的 Δ=−0.412 不是 "D&R per-token quality 优势"——Uniform 在 2533 步仅 0.415 content epoch，是 under-trained。正确解读是 epoch confound 的独立确认
- **M055/M056 教训**：(1) 任何过滤数据必须验证统计摘要 (2) 实验前检查磁盘 (3) 完成实验后清理中间 checkpoint
- **决策链**：D115 analysis reframe → D116 LR confound confirms epoch → D117 Round 9 action matrix → paper_framing.md 是战略锚点


---
