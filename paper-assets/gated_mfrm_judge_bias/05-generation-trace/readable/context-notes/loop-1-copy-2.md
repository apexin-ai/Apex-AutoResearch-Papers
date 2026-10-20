# agent / loop_1.md

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`a1af2bcd60bb9e13119e.json`](../../sessions/a1/a1af2bcd60bb9e13119e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-22T19:14:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 `gpu_ids=[0,1,2,3]` on rtx6000-4x，四张都已分配给本项目，不得用其他服务器/GPU
- exp-012 脚本中 MCMC chains=4 但实际只用 1 GPU sequential（UserWarning 反复出现），不影响正确性但 wall clock 慢 4x——如果需要加速重跑，需要 `numpyro.set_host_device_count(4)`
- submit_training_job 命令必须自带环境激活：`bash -c "cd /root/... && /root/miniconda3/bin/python3 ..."`，不要用 `source activate`
- exp-012 的 EXIT_CODE=129 是假失败（已修正为 success），下次遇到同类 SIGHUP 先 tail 日志确认是否实际完成

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-4x，账号 root
- Python：`/root/miniconda3/bin/python3`（conda base 环境，不是 venv）
- 工作目录：`/root/gated_mfrm_judge_bias/`（各实验子目录 exp001/, exp009/, exp012/ 等）
- 日志目录：`~/runs/gated_mfrm_judge_bias/` (cron 管理的) + `/tmp/` (部分早期实验)
- 磁盘：879G 总量，817G 可用（3% 使用），充裕
- 活跃进程：
  - exp-009: PID 112923, tmux session, cuda:0, log `/tmp/exp009_full.log`
  - exp-001: cuda:2+cuda:3, PID 未记录（多 judge 数据收集 pipeline，vLLM + API）
- Cron：exp-009 有 active cron 监控（reconcile 确认 still running）

### 3. 📊 当前状态
刚处理 exp-012 失败回调：诊断为假失败（SIGHUP after completion），已恢复 conclusion=success 并提取完整 metrics。已向 Director 汇报结果 + 请求 cuda:1 下一个实验指示。

Registry 状态：
- **exp-009** RUNNING cuda:0 — OVB observation（d_j 与 c_n·e_i confounding 的一阶偏差）+ c_n 恢复验证，ETA ~18h（50 seeds × 4 rhos），已跑 ~4h
- **exp-001** RUNNING cuda:2,3 — 8+ LLM judges 数据收集（MT-Bench + Arena-Hard），pairwise evaluation
- **exp-012** DONE(success) — error propagation sensitivity 完成，σ≤0.2 鲁棒 ✓，σ=0.5 退化超预期 ✗
- **mvp_003** DONE(success), **mvp_002** DONE(negative), **mvp_001** DONE(negative)

等待中：
- Director 回复 cuda:1 分配决策
- exp-009 cron 完成回调（预计 ~14h 后）
- exp-001 无 cron 记录（需确认监控状态）

### 4. 📋 待办
- Director 回复 cuda:1 分配 → 按指示准备并提交下一个实验（P1 候选：judge 数量敏感性 / 指标消融 / facet 诊断）
- exp-009 cron 回调 → 走 on-experiment-done：提取 OVB 偏差曲线 + c_n coverage，对标 hypothesis（95% CI coverage ≥0.90），汇报 Director
- exp-001 完成 → 这是 critical path 起点（exp-001→002→003→004/005），数据就绪后立即铺 exp-002（曝光估计）代码
- Worker 池 = 0 → 收到任何新任务立即 spawn，保持 ≥2

### 5. 🎯 战略上下文
- **决策链**：D001(MVP 合成数据验证) → D002(mvp_001 FAIL 但不 kill) → D003(mvp_002 效应验证+收敛未达标) → D004(mvp_003 PASS，进入 research) → D005/D006(Dream R2 Best=3.0 暴露 novelty 天花板)
- **核心结论**：Joint G-MFRM 显著优于 sequential（RMSE -43.8%，p=1e-6），但 novelty 被 Dream 评为 combinatorial（MFRM+1 term + textbook OVB）。应对：identifiability analysis + formal uncertainty propagation + diagnostic framework
- **exp-012 的 paper 价值**：直接支持 "formal e_i uncertainty propagation" novelty 补充点。ConStat r²=0.94 意味着实际 noise σ<0.1，远在鲁棒范围内。cn 比 θ 对噪声更敏感是可写的 insight
- **易错点**：
  - Dream R2 Best=3.0（非 3.5），novelty 天花板已确认，不要再 re-dream
  - UDA baseline 无公开代码，需自行重实现（~400-500 行，3-4 天），已决定先联系作者（D008）
  - exp-001 的监控状态不明确（无 cron 记录），接手后应立即确认
- **目标会议**：AAAI 2027 (July 28, ~67d) / ACL 2027 ARR (Aug 3, ~73d)


---
