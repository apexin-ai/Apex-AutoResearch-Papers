# agent / loop_3.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`f80701768af325bd66f8.json`](../../sessions/f8/f80701768af325bd66f8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T21:46:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090:cuda:0/1/2/3，禁止用其他设备
- 训练命令必须用 `submit_training_job`，禁止 nohup
- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- GPU 编号脚本内始终从 0 开始（框架自动映射 CUDA_VISIBLE_DEVICES）
- kill 训练进程必须直接 kill python PID，不能只 kill bash wrapper（seed7 事故教训）
- D008 Gate 3a/3b FAIL 不可撤回——recovery eval 是补充分析，不是替代

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3-8B`
- 数据：`data/mini_pipeline_v4/sft_{vanilla,taxei,random}_v4.jsonl`（vanilla 4358, taxei/random 9029 samples）
- Checkpoints：`checkpoints/mini_{vanilla,taxei,random}_sft_v4*`
- Eval 脚本：`eval/recovery.py`（clean eval 用 `--no_inject`），`eval/injected_eval.py`（recovery eval，已 dry-run 通过）
- 活跃进程：
  - v4-taxei-seed0: PID 71822, cuda:1
  - v4-random-seed0: PID 72303, cuda:2
  - v4-vanilla-seed123: PID 77937, cuda:3（OOM 重启过一次，当前 v1）
- Cron 监控这 3 个进程

### 3. 📊 当前状态
刚收到 v4-vanilla-seed0（cuda:0）训练完成回调。已派 Worker `worker_analysis_v4-vanilla-seed0_20260514T184406` 去：
1. SSH 检查训练日志/checkpoint 完整性
2. 更新 registry（DONE + metrics）
3. 在 cuda:0 上用 submit_training_job 启动 v4-vanilla-seed0-eval

**等待中**：
- Worker 回调：`worker_analysis_v4-vanilla-seed0` — 分析 + 启动 eval
- Cron 回调：v4-taxei-seed0 / v4-random-seed0 / v4-vanilla-seed123 训练完成
- 4 个 eval 实验在 PREPARING：v4-vanilla-seed0-eval / v4-taxei-seed0-eval / v4-random-seed0-eval / v4-vanilla-seed123-eval

尚未向 Director 汇报本次回调（等 Worker 产出完整结果后一并汇报）。

### 4. 📋 待办
- Worker `analysis_v4-vanilla-seed0` 回调 → 确认 eval 已启动，更新 report.md，向 Director 简报
- v4-taxei-seed0 cron 完成 → 派 Worker 分析 + 在 cuda:1 启动 v4-taxei-seed0-eval
- v4-random-seed0 cron 完成 → 派 Worker 分析 + 在 cuda:2 启动 v4-random-seed0-eval
- v4-vanilla-seed123 cron 完成 → 派 Worker 分析 + 在 cuda:3 启动 v4-vanilla-seed123-eval
- 全部 4 个 seed eval 完成 → 多种子汇总分析（bootstrap CI + permutation test），汇报 Director
- 多种子分析完成 → Phase 2: recovery eval（用 seed=42 checkpoints，eval/injected_eval.py）
- Recovery eval 完成 → 终止决策：taxei > random → 补充 claim；taxei ≤ random → 转 negative paper

### 5. 🎯 战略上下文
- **核心结论**：v4 同源数据下 TaxEI 无优势（Gate 3a/3b FAIL）。Vanilla=TaxEI=61.7%, Random=66.0%。taxonomy tag 在 clean eval 上无额外价值
- **决策链**：D008(Gate FAIL) → D009(选 Option C: recovery eval + 多种子) → D010(FAIL 不可撤回，recovery 是补充) → D011(McNemar 替代 Fisher)
- **当前执行**：D010 Phase 1 多种子验证中（4 卡全满），Phase 2 recovery eval 待 Phase 1 后
- **终止条件**：recovery eval 若 taxei ≤ random → 项目转 negative result 分析论文
- **易错点**：
  - v3 结果（vanilla 74.5%）和 v4 结果（vanilla 61.7%）差 12.8pp，原因未明，多种子验证正在排查这个波动
  - v3 数据量不平衡（vanilla 4176 vs taxei 7545 vs random 9076），v4 才是正式对比（同源 4358/9029）
  - eval 只有 47 tasks，McNemar 对小样本敏感，p<0.10 是预注册阈值（不是 0.05）
  - PALADIN (2025.09) 是最大竞争者——同为 taxonomy-guided error injection，差异化分析是关键


---
