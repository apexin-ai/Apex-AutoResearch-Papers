# agent / loop_12.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`aec57f8910faa1abd2e1.json`](../../sessions/ae/aec57f8910faa1abd2e1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-23T23:52:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-19183 的 cuda:0 和 cuda:1，其他设备号禁止使用
- Bootstrap 实验用 CPU（kernel ridge regression），不占 GPU，但 cron 监控仍绑定 GPU 分配
- Bootstrap v3 用 tmux 启动，cron 监控了启动器 PID 而非实际 worker PID，导致 v1/v2/v3 三次连续被误判 failed——**下一轮不要因为 registry conclusion=failed 就认为实验真的失败了**，必须先 SSH 检查 tmux 和进程
- DDL 硬约束：Abstract 2026-05-26（3天），Paper 2026-05-29（6天），P2 统计重分析是唯一 blocker

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，2× RTX PRO 6000
- 工作目录：/root/autodl-tmp/vla-ssd/
- Python：/root/miniconda3/bin/python（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- Bootstrap 脚本输出：/root/autodl-tmp/vla-ssd/results/bootstrap_r2/（子目录按 arch/suite 组织，结果文件为 `{trained,untrained}.json`）
- 日志：/root/autodl-tmp/vla-ssd/logs/bootstrap_v3_cuda0.log 和 bootstrap_v3_cuda1.log
- tmux sessions（可能仍存活）：bootstrap_v3_cuda0（12 conditions）、bootstrap_v3_cuda1（8 conditions）
- 活跃 Worker：worker_diagnose_clustered_bootstrap_reanalysis_v3_20260523T074926（正在 SSH 诊断 v3 实际状态）

### 3. 📊 当前状态
刚收到 v3 的 cron 失败回调，高度怀疑是误报（与 v1/v2 相同的 cron PID 监控问题）。已派诊断 Worker SSH 到服务器检查 tmux/进程/日志/已完成 conditions 数。

Registry 状态：
- clustered_bootstrap_reanalysis_v3: DONE(failed) — 待诊断确认，可能需要翻转回 RUNNING 或标记 success
- clustered_bootstrap_reanalysis_v2: DONE(failed) — 同样的 cron 误报模式
- clustered_bootstrap_reanalysis_v1: DONE(failed) — 同上
- PREPARING 实验 10 个（tracvla_spatial_full_v2, behavioral_pilot_v2 等），全部等 bootstrap 完成后才推进
- 写作 P0/P1 全部完成 ✅，P2（统计重分析）是当前唯一 blocker

等待中：
- Worker 诊断回调 → 确认 v3 真实状态
- Director 未有待处理指令

### 4. 📋 待办
- 诊断 Worker 返回 actual_status=still_running → update_registry 翻转 v3 状态，注册正确的 cron 监控（监控 tmux 内实际 python PID），汇报 Director "v3 仍在跑，cron 误报已修正"
- 诊断 Worker 返回 actual_status=completed → 收集 20 conditions 的 bootstrap CIs，update_registry conclusion=success，派 Worker 汇总结果表 + 集成到论文，推进 P2→P3
- 诊断 Worker 返回 actual_status=truly_failed → 分析 root cause，修复后重跑（第4次），考虑改用 submit_training_job 正确注册 PID 避免 cron 误报
- P2 bootstrap 全部完成 → 集成 CIs 到论文 Table → Multi-δ TOST → Reviewer 审视（P3）
- P3 完成 → 终稿通知用户

### 5. 🎯 战略上下文
- 核心发现：R² exit collapse 是 VLM→VLA 特异性的（TracVLA 4/4, NORA 2/2 显著；OpenVLA 0/4 不显著；untrained 0/10）
- 决策链：D095 跨架构 framing → D097 Dream 审稿 Weak Reject → D100 NLP control 确认 VLA-specific → D101 Major Revision 执行中
- P2 是 D101 修订的最后 blocker：clustered bootstrap n=1000 的 20 conditions CIs 需要写入论文替代原始 aggregate probing 统计
- 最容易判断错的事：**v1/v2/v3 的 failed 结论可能全是 cron 误报**。memory.md 记录了 bootstrap v2 的关键发现（那些发现就是在"failed"标记下的 tmux 进程跑出来的）。不要看到三个 failed 就认为方法有问题——问题在 cron 监控架构
- Bootstrap 用 CPU 不用 GPU（kernel ridge 4000×4000 矩阵求解），每 condition ~18-20 min，20 conditions 双卡并行预计 ~6h 总耗时
- 速度优化已验证：multiprocessing Pool(100) + cho_factor + OPENBLAS_NUM_THREADS=1，不要回退到 serial 方式


---
