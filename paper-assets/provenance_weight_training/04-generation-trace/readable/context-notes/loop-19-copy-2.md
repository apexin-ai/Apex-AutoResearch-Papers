# agent / loop_19.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`91deaa30035256b57241.json`](../../sessions/91/91deaa30035256b57241.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-23T03:07:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-41312 的 cuda:0/1/2/3，共 4 张 RTX PRO 6000 96GB
- DDL：EMNLP 2026 ARR May 25（距今 ~2 天）
- 所有训练必须用 `submit_training_job`，不能用 Bash nohup
- WANDB_MODE=disabled（所有 epoch-matched 系列实验），metrics 从日志提取
- 训练命令必须 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 开头，不要假设 .venv
- 不存在 uniform_epoch_matched_seed123 实验——这是 3-seed epoch confound 的缺口，需要 Director 决策是否补

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312，工作目录 /root/provenance_weight_training
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：/root/provenance_weight_training/models/Qwen/Qwen3-0.6B
- 数据：/root/provenance_weight_training/data/scored_data.jsonl (371499), scored_data_filtered_q05.jsonl (153725), scored_data_random_shuffle.jsonl
- 输出目录：/root/autodl-tmp/provenance_weight_training/output/models/
- 磁盘充裕：/autodl-pub 5.3T/7.3T 可用，/usr/bin/nvidia-smi 400G/439G 可用
- 活跃进程：
  - random_reweight_v2_seed456: PID 699452, cuda:3
  - detect_remove_q05_v2_seed456: PID 742953, cuda:2
  - uniform_epoch_matched_seed456: PID 748574, cuda:1
- Cron 监控：3 个 cron 对应上述 3 个 RUNNING 实验

### 3. 📊 当前状态
收到 `dr_epoch_matched_seed456`（cuda:0）完成回调。已派 Worker `worker_analysis_dr_epoch_matched_seed456_20260522T102824` 去 SSH 提取日志 metrics。**Worker 尚未回调，metrics 未入 registry。**

Registry 概况：229 实验，DONE 208（success 138, negative 12, failed 39, killed 19），RUNNING 3，ANALYZING 1，PREPARING 17。

- ANALYZING: dr_epoch_matched_seed456（等 Worker 分析）
- RUNNING: random_reweight_v2_seed456 (cuda:3), detect_remove_q05_v2_seed456 (cuda:2), uniform_epoch_matched_seed456 (cuda:1)
- **cuda:0 空闲**——dr_epoch_matched_seed456 跑完后释放，无 QUEUED/ALLOCATED 实验排队

等待中：
1. Worker 回调 → 拿到 dr_epoch_matched_seed456 metrics → update_registry → 汇报 Director
2. 3 个 RUNNING 实验的 cron 完成回调

### 4. 📋 待办
- Worker `worker_analysis_dr_epoch_matched_seed456` 回调 → 读 metrics → update_registry(conclusion, metrics, checkpoint_path, status=DONE) → 与 seed42(17.651)/seed123(17.659) 对比 → 汇报 Director（含 3-seed 均值±std）
- cuda:0 空闲 → 汇报 Director 建议下一步（候选：uniform_epoch_matched_seed123 补 3-seed 缺口）
- uniform_epoch_matched_seed456 完成 → 分析 + 与 seed42(18.062) 配对 → 此时 epoch confound 只有 2-seed uniform，需决策是否补 seed123
- detect_remove_q05_v2_seed456 完成 → 与 seed42(17.285)/seed123(17.272) 配对 → 3-seed D&R full baseline 齐全
- random_reweight_v2_seed456 完成 → 与 seed42(17.958)/seed123(17.945) 配对 → 3-seed random reweight baseline 齐全
- 所有 3-seed baselines 齐全后 → 汇总 epoch confound / detector signal 分析表 → 更新 paper 相关章节

### 5. 🎯 战略上下文
- 项目核心：analysis paper "When, why, and how does detect-and-reweight work?" 贡献排序：(1) Epoch confound (2) Detector requirements (3) Mechanism decomposition (4) Adaptive b* 工具
- Round 8 审稿 2.5-3.0 后 reframe 为 analysis paper（D115）。当前跑 P0 补实验验证 epoch confound claim
- 关键数据：Adaptive 3-seed PPL=17.674±0.007 vs Uniform 3-seed PPL=17.694±0.008，Δ=−0.020 (p=0.025)
- Epoch confound 核心：D&R epoch-matched（2533 steps on filtered data with independent LR）vs Uniform epoch-matched（2533 steps on full data），验证 D&R 看似强的效果其实来自 fewer epochs on less data + 独立 LR schedule
- **易错点**：
  - dr_epoch_matched_indep_lr_seed42（holdout=18.782, FAILED）和 dr_epoch_matched_seed123（holdout=18.332, FAILED）是旧版有 bug 的，不要引用。正确版本是 `_v2_seed42`(17.651) 和 `_seed123_r2`(17.659)
  - uniform_epoch_matched_indep_lr_seed42 的 holdout=18.062 看起来比 D&R 的 17.651 差很多——这正是 epoch confound 的证据（uniform 在 2533 步内学不够，但 D&R 因为数据少 epoch 数更多所以更好）
  - bs16 系列实验已经有 3-seed 完成（bs16_adaptive_tau07 和 bs16_uniform），用于 batch-size amplification claim


---
