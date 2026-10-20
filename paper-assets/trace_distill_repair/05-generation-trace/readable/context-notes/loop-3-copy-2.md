# agent / loop_3.md

**trace distill repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`28153b262790049c1086.json`](../../sessions/28/28153b262790049c1086.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-15T09:22:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx6000-diagprobe 的 cuda:0 和 cuda:1，不可用其他设备
- Phase 2 scoring 是 API-only（DeepSeek-V4-Flash），不占 GPU 计算，但 submit_training_job 仍绑定 GPU slot 做监控
- structural scoring 输出文件 phase2_structural_scores.json 会被覆盖——跑新 v3 前旧数据已丢，不可回退
- line scoring 数据量大（51430 segments），max_concurrent=3 是验证过的安全上限，开更多会触发 API rate limit
- segment cap 问题已知但 D016 决定继续用现有数据做初步 MVP 评估，不要自行决定重跑 Phase 1

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe，工作目录 /root/trace_distill_repair/
- Python：需探测（可能是 conda base 或系统 python3，上次 Worker 用的是系统 python3）
- 数据目录：/root/trace_distill_repair/pipeline_output/（所有 trace + scoring 输出）
- 模型已下载（待 Research 阶段用）：Qwen3-8B (16GB), Qwen3-30B-A3B (57GB)，路径未记录在 registry，需 SSH 探查
- W&B：本项目 MVP 阶段未用 W&B（API scoring 无训练 metrics）
- HF cache：未配置（MVP 阶段不需要）
- 活跃进程：mvp_line_scoring_v3 PID=100942, tmux session 名称未记录（submit_training_job 自动创建），cron 监控中
- 活跃 Worker：worker_analysis_mvp_structural_scoring_v3_20260515T062101（正在分析 structural scoring v3 结果，尚未回调）

### 3. 📊 当前状态
收到 mvp_structural_scoring_v3 的 CRON 完成回调（进程正常退出）。已派 Worker SSH 去服务器提取 metrics，**Worker 尚未回调**。

Registry 状态：
- **mvp_structural_scoring_v3**: ANALYZING — Worker 正在提取结果，等回调
- **mvp_line_scoring_v3**: RUNNING (PID 100942) — 仍在跑，但 registry 中 conclusion 字段异常标记为 "killed"（reconcile 确认进程活着，这个 conclusion 值需要核实/修正）
- 其他 10 个实验全部 DONE（5 success, 3 failed, 2 killed）

尚未向 Director 汇报本次回调。

### 4. 📋 待办
- Worker analysis 回调到达 → 读取 metrics → update_registry(status=DONE, conclusion=success/negative, metrics=...) → 刷新 report.md → 汇报 Director（带 [资源] 行）
- 如果 structural scoring v3 error_rate < 5% (hypothesis 成立) → 等 line_scoring_v3 完成 → 两个 v2 scoring 齐备后启动 Phase 3 repair comparison
- 如果 structural scoring v3 error_rate ≥ 5% → 按 red-section 产出 Framing 调整提案，汇报 Director，不默默跑下一个
- mvp_line_scoring_v3 cron 回调到达 → 同样流程分析结果
- mvp_line_scoring_v3 的 conclusion="killed" 异常值 → 核实后 update_registry 修正
- 两个 v3 scoring 都完成后 → Phase 3 repair comparison（run_phase3_repair.py 已就绪）→ MVP 判定

### 5. 🎯 战略上下文
- 目标会议：EMNLP 2026 ARR May，DDL 2026-05-25（距今 10 天）
- 核心 claim：结构感知分段（structural）优于行级过滤（line），修正 EMNLP 2025 "Do Code Semantics Help?" 的负面结论
- Kill 标准：structural win rate ≤ 50% in >2K token subset → 终止项目
- 决策链关键节点：D009 发现 max_tokens=256 导致方向性偏差 → D012 宣布所有旧 structural scoring 不可信 → D013/D014 发现 Phase 1 trace 收集 bug（未用 failing test）→ D015 Phase 1 v2 完成 → D016 确认 segment cap 问题但继续做初步评估
- 易错点：(1) registry 里有大量历史失败实验（mvp_teacher_scoring, mvp_line_scoring_rerun 等），这些是旧服务器 westd-18314 上的残留，与当前 rtx6000-diagprobe 上的 v3 实验无关，不要混淆；(2) phase2_structural_scores.json 被多次覆盖，只有最新一份有效；(3) mvp_line_scoring_v3 的 conclusion="killed" 可能是误标，进程实际还活着


---
