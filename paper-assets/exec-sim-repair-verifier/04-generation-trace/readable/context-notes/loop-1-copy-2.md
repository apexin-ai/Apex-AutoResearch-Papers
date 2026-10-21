# agent / loop_1.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`7914b050abab3dd52e80.json`](../../sessions/79/7914b050abab3dd52e80.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-12T10:53:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- home-1x5090 只分配了 cuda:0（1× RTX 5090），账号 sonny，项目路径 /home/sonny/exec-sim-repair-verifier
- seetacloud-westd-4x5090 分配了 cuda:0, cuda:1（report.md 显示分配 cuda:2/3 但实际跑在 cuda:0/1），账号 root
- llm-judge-32b-zeroshot / llm-judge-8b-zeroshot 状态 PREPARING，**未获批准不能提交**
- CWM baseline 已是 negative 结论（函数级 classification vs generation 差距 <0.2pp），核心假说已 pivot 到 complexity-dependent advantage，repo-level 是决胜战场——不要再在函数级 null result 上浪费 GPU
- trace-then-judge 有方法论缺陷（trace 模板泄漏 mutation type），不要重跑

### 2. 🖥️ 基础设施快照
- **home-1x5090**: 工作目录 /home/sonny/exec-sim-repair-verifier, Python3 系统路径, 无 conda（用系统 pip）
  - 数据: /home/sonny/exec-sim-repair-verifier/data/ (train 15290, test 1890, traj_train 8052, traj_test)
  - Checkpoints: checkpoints_seed{42,123,456}/best/, checkpoints_traj/best/, checkpoints_traj_seed123/best/
  - 活跃: traj-level-seed456 (PID 2542385, tmux, cuda:0)
- **seetacloud-westd-4x5090**: 工作目录 /home/sonny/exec-sim-repair-verifier, conda base (/root/miniconda3), HF_HOME=/root/autodl-tmp/.hf_cache
  - 模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B
  - 活跃: model-size-scaling-cls8b (PID 11443, cuda:0), model-size-scaling-cwm8b (PID 11522, cuda:1)
- W&B: 所有实验用 --no_wandb，无 wandb 数据

### 3. 📊 当前状态
**刚收到 traj-level-seed123 的 CRON 回调**（进程正常退出，ANALYZING）。已派 Worker `worker_analysis_traj-level-seed123_20260512T075126` 去 SSH 读取 eval_traj_seed123.json 提取指标，**Worker 尚未返回**。

Registry 摘要：
- **ANALYZING**: traj-level-seed123（等 Worker 回调后更新 metrics → DONE）
- **RUNNING**: model-size-scaling-cls8b（8B classification，seetacloud cuda:0）, model-size-scaling-cwm8b（8B CWM generation，seetacloud cuda:1）, traj-level-seed456（traj seed=456，home cuda:0）
- **PREPARING**: llm-judge-32b-zeroshot, llm-judge-8b-zeroshot（需 GPU 分配 + 审批）
- **DONE**: 10 个（7 success, 2 negative, 1 failed）

等待中：
- Worker `worker_analysis_traj-level-seed123_20260512T075126` 回调 → 提取 metrics、更新 registry、汇报 Director
- 3 个 RUNNING 实验的 cron 完成回调
- Director 未对 llm-judge 实验做 GPU 分配决策

### 4. 📋 待办（条件触发式）
- Worker analysis 回调到达 → 用 metrics 更新 registry（conclusion/metrics/checkpoint_path/log_path）→ 与 traj-level-finetuned (seed=42, acc=85.66%) 和 per-test classification mean (88.41%) 对比 → 更新 report.md → 汇报 Director（带 [资源] 行）
- traj-level-seed456 完成 → 同样分析流程 → 3 seeds 汇总做 paired t-test / bootstrap（traj mean vs classification mean 88.41%±0.96），确认 gap 统计显著性
- model-size-scaling-cls8b + cwm8b 都完成 → 对比 8B 尺度 classification vs CWM gap，与 4B 尺度 gap（<0.2pp）比较 → 若 gap 随尺度扩大则支持 complexity-dependent hypothesis
- 3 seed traj 全部完成 + 8B scaling 完成 → 向 Director 提交函数级实验总结，请求推进 repo-level SWE-bench 数据构建（关键路径）
- seetacloud cuda:2/3 空闲 → 提醒 Director 分配（llm-judge 或其他任务）

### 5. 🎯 战略上下文
- **核心 narrative**: 函数级 classification ≈ generation（null result），hypothesis pivot 到 complexity-dependent advantage——repo-level 是最后机会（D007/D008）
- **决策链**: D004(P2P~1%前提不成立) → D005(reframe) → D007(complexity-dependent pivot) → D008(repo-level go/no-go 标准: ≥3pp+p<0.05=全力EMNLP, <1pp=kill C1 转 Plan B)
- **时间压力**: ARR May 25 截稿，13 天。关键路径: Docker setup(1d) → SWE-bench 数据构建(1d) → 训练(0.5d) → eval(0.5d) → 写作(3-5d) = 6-8d，零容错
- **易错点**:
  - traj-level 指标（accuracy/unresolved_f1/resolved_f1）和 per-test classification 指标（accuracy/pass_f1/fail_f1）**不能直接对比 F1**——前者是 resolved/unresolved 二分类，后者是 pass/fail 二分类，语义不同。对比只用 accuracy
  - report.md 里 GPU 分配信息可能过时（显示 cuda:2/3 分配但实际跑在 cuda:0/1），以 registry spec 里的 gpu 字段为准
  - Plan B（null result 论文）scope 已定义在 ROADMAP.md，不要自行扩大


---
