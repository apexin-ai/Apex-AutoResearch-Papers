# agent / loop_7.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`90b043d4060c42983322.json`](../../sessions/90/90b043d4060c42983322.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-14T17:56:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 westd-22162 cuda:0/1/2/3，其他设备号（即使 Director 指示）必须 push back
- c2_qw_n500 数据完整性风险：重复进程期间（~8→93/500 s015）可能有交叉写入，最终分析必须验证 profiling_results.json 时间戳单调性 + 问题数=500
- Qwen s015 Cohen's d=0.28 CI 含零，禁止 claim "significant"；已预注册：若 n=500 仍不显著，叙事改为 "compound effect emerges above threshold sparsity ~s020"
- DeepSeek 量级 ~4× Qwen，禁止直接对比绝对值，只比较趋势（ρ=1.0）
- LLaMA II 比 DeepSeek 小 ~40×、比 Qwen 小 ~2-10×，禁止 claim "similar magnitude"，必须 frame 为 "consistent qualitative pattern with architecture-dependent severity"
- DeepSeek skewness 高达 9.5，跨模型对比必须同时报告 median+IQR，不能只用 mean
- c2_qw_n500 用 SCREEN sessions（非 tmux），cron 监控通过 PID 检测，历史上已出 3 次 cron false positive（进程实际在跑但 cron 误报 dead）

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162，工作目录 /root/autodl-tmp/pacs
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 模型路径：DeepSeek-R1-Distill-Qwen-7B / Qwen / DeepSeek-R1-Distill-Llama-8B 均在服务器上（具体路径需 SSH 确认，上一轮未记录到 memory）
- 数据集：/root/autodl-tmp/pacs/data/math500.json（MATH-500，500题）
- 活跃进程：
  - c2_n500_deepseek: cuda:0+1，screen sessions c2_n500_gpu0/gpu1，PID 未记录在 registry spec 中（用 `screen -ls` 或 `ps aux | grep run_c2` 查）
  - c2_qw_n500: cuda:2+3，screen sessions c2_qw_gpu2/gpu3，PID 131864（imp）/ 132002（rand），进度 ~231/500 s015
  - c3_llama: cuda:2+3 共享，bash run_c3_llama_full.sh，父进程 PID 138398，子进程已更替（registry PID 过时）
- Cron 活跃：c2_n500_deepseek / c2_qw_n500 / c3_llama 各有监控 cron
- c5b_pilot 代码已就绪：/root/autodl-tmp/pacs/profiling/run_mitigation_pilot.py（577行），dry-run 通过

### 3. 📊 当前状态
**刚做完**：Session #7 处理了 c3_llama cron escalation（reconcile 报 "process gone miss 1/5"），确认 c2_qw_n500 重复进程已死亡，更新了进度。

**正在进行**：
- Worker `worker_ops_analyze_and_launch_20260514T174507`（turn 24，running）正在做 c3_llama 全 8 conditions 分析 + 检查 GPU 可用性准备 c5b_pilot。Worker 报告 c3_llama s030 已完成。
- c2_n500_deepseek: RUNNING，cuda:0+1，DeepSeek n=500 全 8 conditions，进度未知（需 SSH 查）
- c2_qw_n500: RUNNING，cuda:2+3，Qwen n=500，~231/500 s015，ETA 全部完成 ~May 16 06:00 UTC
- c3_llama: RUNNING（实际 Worker 报告已完成所有 conditions），cuda:2+3 共享

**等待中**：
- Worker 回调：worker_ops_analyze_and_launch 即将返回 c3_llama 分析结果
- c5b_pilot: QUEUED，等 GPU 释放（c3_llama 完成后 cuda:2 或 3 可腾出部分算力）
- c2_n500_deepseek / c2_qw_n500 的 cron 完成回调

### 4. 📋 待办（条件触发式）
- Worker 回调到达（c3_llama 分析完成）→ 更新 registry（c3_llama → DONE/ANALYZING），将 LLaMA 跨架构结果写入 report.md，向 Director 汇报 C3 验证结果
- c3_llama 确认完成 → GPU2/3 负载下降，c2_qw_n500 速率可能提升；评估是否可在共享 GPU 上启动 c5b_pilot
- c2_n500_deepseek cron 回调（完成）→ spawn Worker 做统计分析（n=500 vs n=50 对比，CI 收窄程度），更新论文 tables
- c2_qw_n500 cron 回调（完成）→ spawn Worker 分析，关键看 Qwen s015 在 n=500 下 CI 是否仍跨零 → 决定叙事路径（threshold narrative vs across-the-board）
- c2 + c3 全部完成 → 更新论文 §4/§5 tables + figures（bf16 canonical 数据），提交 Group C full review
- c5b_pilot GPU 分配到位 → submit_on_allocated 启动

### 5. 🎯 战略上下文
- **截稿 2026-05-25（11天）**，论文全文已完成可编译，当前是补充实验冲刺阶段
- 核心发现：importance-based compound severity 随 sparsity 单调递增，cross-model replicated（Cohen's d ρ=1.0, gradient p=0.043）
- C1/C2/C3/C5/C6 confirmed，C4 降级为 §6 supporting（D045/D046）
- **最易判断错的事**：c3_llama cron 经常 false positive（进程实际在跑但 cron 报 dead），不要急着标 FAILED，先 SSH 查进程
- **最易踩的坑**：c2_qw_n500 用 screen 不是 tmux，查进度用 `screen -ls` + `ps aux`；不要 kill 看起来"重复"的进程前先确认 PID 对应哪个 screen session
- 关键决策链：D045/D046（C4降级）→ D047（6-point dose-response）→ D048（paired d_z 替换）→ D049-D053（论文细节修正）
- LLaMA s015 CI 不跨零（[0.031, 0.090]），这是 paper 加分项——三个架构中两个在 s015 显著
- c5b_pilot 是 mitigation 方向（C5b），gate 标准：oracle recovery >30% at s025/s030


---
