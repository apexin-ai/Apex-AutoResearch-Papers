---
loop: 18
reason: idle_timeout
updated: '2026-05-23T20:29:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-11235 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，服务器用 conda 不是 venv
- EMNLP ARR DDL 2026-05-25，所有实验已完成，当前处于提交 pipeline 阶段，不要启动新方向实验
- GPU 编号脚本内始终从 0 开始（框架自动映射物理 GPU）

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235，工作目录 /root/trace-verdict-study
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：Qwen2.5-Coder-7B-Instruct
- 数据：/root/autodl-tmp/trace-verdict-study-data/（full_trace_train.jsonl 4720条, full_trace_test.jsonl 1190条）
- 日志：~/runs/trace-verdict-study/
- 活跃进程：full_trace_seed456 (PID 854746, cuda:0, tmux 管理, cron 监控中)
- 磁盘：/autodl-pub 5.3T/7.3T 可用(24%)，根分区 400G/439G 可用(4%)

### 3. 📊 当前状态
- **刚做完**：收到 full_trace_seed123 的 CRON 完成回调，已派 Worker (`worker_analysis_full_trace_seed123_20260523T041603`) 分析结果，Worker 尚未回调
- **RUNNING**：full_trace_seed456 (cuda:0, PID 854746)——3-seed 的最后一个 seed
- **ANALYZING**：full_trace_seed123 (cuda:1)——Worker 正在提取指标
- **等待中**：
  - Worker 回调 → 需要：update_registry 写入 metrics/conclusion、刷新 report.md、向 Director 汇报完整 3-seed 统计（seed42=81.76%，seed123=待分析，seed456=待完成）
  - full_trace_seed456 cron 回调 → 同样流程分析，之后 3-seed 统计完整
- 已向 Director 发送初步通知（实验完成+Worker 已派发）

### 4. 📋 待办
- Worker `analysis_full_trace_seed123` 回调到达 → 读取 Worker 产出，update_registry(DONE)，刷新 report.md，向 Director 汇报完整指标 + 与 seed42 对比
- full_trace_seed456 cron 回调（进程退出）→ 派 Worker 分析 → 汇报 3-seed 完整统计（mean±std）
- 3-seed 统计完成 → 向 Director 汇报最终 full_trace 3-seed robustness 结果，供论文 rebuttal 使用
- Director 指示进入 final sync / Round 16 → 按提交 pipeline 推进（tar+scp + clean compile + 审稿）

### 5. 🎯 战略上下文
- 核心结论链：D116 reframe "complete traces hurt SFT" + D117 gradient masking 证实 content quality ≥96% → 论文 narrative 是 full trace 反而有害，exception-only 最优
- 关键指标锚点：exception_only accuracy ~83-85%，full_trace ~81.76%（seed42），no_trace ~75%（implicit pathway ceiling）
- full_trace 3-seed 是 rebuttal 用的 robustness 证据，不是核心 claim 的新数据点
- 易错点：
  - full_trace_seed42_v5 才是正确的 parent（之前有 v1-v4 因各种问题被 killed）
  - report.md 趋势显示 accuracy/fail_f1 "↓" 是因为 no_trace 实验（~75%）拉低了近 3 次均值，不代表方法退化
  - 项目有 180 个实验，registry 很大（345K chars），查询时用 filters 或 jq 过滤，不要全量读入 context
