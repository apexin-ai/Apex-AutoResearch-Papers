---
loop: 2
reason: max_messages
updated: '2026-05-12T18:50:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 / cuda:1（cqa1-21977 上分配的 2×RTX 4090D）。已发生 3 次 GPU 越界事故（D019 等），第三次 kill 了进程
- 所有 GPU 命令必须加 `CUDA_VISIBLE_DEVICES=X` 前缀，无例外（D020 确认）
- v5_cuda1 (PID 263025) 当前无 CUDA_VISIBLE_DEVICES 但在正确 GPU 上运行，不要 kill，下次重启时补上
- AutoDL 实例：pip 前必须 `source /etc/network_turbo`，HF 下载设 `HF_HUB_DISABLE_XET=1`

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977 (connect.cqa1.seetacloud.com)，root 用户
- 工作目录：/root/autodl-tmp/error_diag_dpo_recovery
- Python：conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：Qwen3-8B（v5 数据收集用）、14B-AWQ（错误分类用），路径在 /root/autodl-tmp/ 下
- Expert 数据：/root/autodl-tmp/error_diag_dpo_recovery/data/alfworld_sft.json (3119 条 ETO expert trajectories)
- 活跃进程：v5_cuda0 (PID 266200, cuda:0) + v5_cuda1 (PID 263025, cuda:1)，收集 250 tasks 轨迹，ETA ~04:10-04:20 UTC
- 无 tmux session / 无 wandb / 无 cron

### 3. 📊 当前状态
代码全部就绪，等 v5 完成：
- **datagen_traj_v5_cuda0** RUNNING：8B temp=0.7 收集 250 tasks 轨迹，~25/250 完成
- **datagen_traj_v5_cuda1** RUNNING：同上，~37/250 完成。两卡跑同一 task 集（D020 决策保留，不分片）
- **datagen_classify_v2** PREPARING：classify_errors.py 已就绪（dual-stats Version A/B/C + tautological warning），等 v5 数据
- collect_trajectories_icl.py 已就绪：14B-AWQ + per-task-type ICL few-shot，v5 step-1 diverge >80% 时启动

### 4. 📋 待办
- v5 两卡完成 → 立即跑 `classify_errors.py` 全量分类（14B-AWQ，两卡并行）→ 输出 error_type 分布 + correction_span + p1_analysis.json (Version A/B/C)
- step-1 diverge >80% → 两卡启动 ICL v6 收集（collect_trajectories_icl.py, 14B-AWQ, temp=0.5）
- step-1 diverge ≤80% → 直接做 P1 Kruskal-Wallis 分析，判断 action < verification < planning 是否成立
- Version A/B 显著但 Version C 全不显著 → P1 效应是 task complexity confound，需重新评估定义
- P1 通过 → 进入 DPO pair 构建 + 训练（Day 2 计划）

### 5. 🎯 战略上下文
- **项目**：ETADN——error-type-specific γ 替代 DMPO 单一 γ，核心假设是不同错误类型有不同 correction span
- **阶段**：MVP Day 1，DDL May 25 ARR。立项风险 KILL_triage (19%)，用户决定冲
- **决策链**：D009 pivot（zero-shot 0% → 改用 ETO expert + model failure）→ D012（P1 correction horizon = expert-model divergence 到 expert 完成剩余步数）→ D014/D015（temp sampling 两卡收集）→ D020（两卡重叠保留）→ D021（step-1 diverge 风险应对 + ICL 后备）
- **最容易判断错的事**：dry-run 的 Kruskal-Wallis p=0.000343 是循环论证（rule-based 分类用 correction_span 阈值推 error_type 再检验两者关联），不要当真。真实 p-value 要等 LLM 分类
- **7 次失败历史**：v1-v4 全部 failed（episode boundary bug、action translation bug、GPU 越界、ICL prefix bug）。v5 是修复后的干净版本
- **Reviewer pseudoreplication 建议已落实**：Version B 每 task 取一条去重，Version C 按 task_type 分层控制 confound
