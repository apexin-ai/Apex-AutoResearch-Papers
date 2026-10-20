---
loop: 21
reason: idle_timeout
updated: '2026-05-25T14:03:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-41312:cuda:0,1,2,3（仅此 4 张，不可用其他设备）
- 数据路径：训练数据在 `/root/autodl-tmp/provenance_weight_training/`，根分区只有 30GB 不要存大文件
- random_subset_epoch_seed42 是 Round 13 响应的最后一块拼图，DDL 2026-05-25，必须优先重跑
- detect_remove 系列（q03/q05/q07）正在跑，不要 kill 它们——它们是 D&R threshold sweep 的完整数据

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312，4× RTX PRO 6000 96GB
- 工作目录：`/root/autodl-tmp/provenance_weight_training/`（推测，需 Worker 确认）
- Python：预置镜像 `aml-train`，conda 环境 `/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`models/Qwen/Qwen3-0.6B`（相对于工作目录）
- 日志路径格式：`~/runs/provenance_weight_training/{exp_id}.log` 或 output_dir 下 `train.log`
- 活跃进程：
  - detect_remove_q07_seed42_r2: PID 987903, cuda:1
  - detect_remove_q05_seed42: PID 962199, cuda:2, cron 监控中
  - detect_remove_q03_seed42: PID 984296, cron 监控中（GPU 未在 report 中标注，可能 cuda:3）
- cuda:0 空闲（random_subset_epoch_seed42 失败后释放）
- 磁盘：/root 分区 400GB/439GB 可用（4%）

### 3. 📊 当前状态
**刚做完**：Session 初始化（read_registry + reconcile_crons + 读 report/ROADMAP），确认 random_subset_epoch_seed42 failed。已派 Worker `worker_diagnose_random_subset_epoch_seed42_20260524T220206` SSH 查日志诊断根因，已向 Director 汇报。

**等待中**：
- Worker 诊断回调（查 `~/runs/provenance_weight_training/random_subset_epoch_seed42.log` 的 traceback）→ 回调到达后根据根因决定修复+重跑
- detect_remove_q07_seed42_r2 (RUNNING, cuda:1)
- detect_remove_q05_seed42 (RUNNING, cuda:2, cron 活跃)
- detect_remove_q03_seed42 (RUNNING, cron 活跃)
- PREPARING 实验 15 个（大部分是历史遗留，不急）

**Registry 概况**：258 个实验，239 DONE（162 success / 13 negative / 43 failed / 21 killed），3 RUNNING，15 PREPARING

### 4. 📋 待办
- 诊断 Worker 回调到达 → 读根因；若 OOM/临时错误 → 立即在 cuda:0 重跑 random_subset_epoch_seed42（6103 steps，~2-3h）；若代码 bug → 派修复 Worker 再重跑
- detect_remove_q03/q05/q07 任一 cron 回调 → 走 on-experiment-done 流程（更新 registry → 刷 report → 汇报 Director）
- random_subset_epoch_seed42 重跑成功 → 对比 D&R q>0.3 PPL（~17.25）vs random subset PPL，判断 filtering quality 是否 load-bearing → 更新论文 Results
- 所有 D&R sweep + random subset 完成 → 汇总 Table，论文最终更新，准备投稿

### 5. 🎯 战略上下文
- **核心方向**：Analysis paper "When, why, and how does detect-and-reweight work?"。贡献排序：(1) Epoch confound >95% (2) Detector requirements (3) Mechanism decomposition (4) Adaptive b* tool
- **当前阶段**：Round 13 审稿响应，评分 3.0 (Findings)。核心瓶颈（N=3 BH 不显著）已通过 N=5 seeds 解决（p_BH=0.011）。剩余：random-subset baseline + 论文更新
- **random_subset_epoch_seed42 的意义**：证明 D&R 的优势不仅仅来自 multi-epoch exposure（如果 random subset 达不到 D&R 的 PPL，说明 filtering quality 是 load-bearing 的）。这是 Reviewer 要求的 confound control
- **关键数据**：Δ(B=4, ρ=0.4, N=5) = −0.023±0.006, p=0.0012, p_BH=0.011。D&R q>0.3 保留 31.48% 数据（116935 docs），random subset 匹配同样的数据量和步数
- **易错点**：
  - 训练命令用 `--weighting_method uniform`（random subset 本质是 uniform 训练，只是数据是随机子集）
  - 不要混淆 random_subset（随机子集多 epoch）和 random_reweight（随机权重）——前者是 epoch confound control，后者是 weight signal control
  - 审稿历史从 Round 8 (2.5) 到 Round 13 (3.0)，进展缓慢，每次审稿改进都很关键
