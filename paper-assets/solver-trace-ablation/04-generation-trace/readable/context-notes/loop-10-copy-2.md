# agent / loop_10.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`b016b5e8536c32b559db.json`](../../sessions/b0/b016b5e8536c32b559db.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T02:50:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: 只能用 westd-39279 的 cuda:0 和 cuda:1，绝对不碰其他 GPU
- **磁盘 96% 满** (240G/250G data disk): 任何新 output 必须先清理旧 checkpoint，output_dir 必须放 `/root/autodl-tmp/outputs/`，`log_completions=False` + `save_total_limit=1`
- **D062 数据完整性**: exp1 系列 s43/s44 之前用了错误测试集 test_100.jsonl（应为 proofwriter_fol_100.jsonl）。所有 exp1 eval 必须用 proofwriter_fol_100.jsonl，不能用 test_100.jsonl
- **submit_training_job 命令格式**: 必须 `bash -c "export CUDA_VISIBLE_DEVICES=N && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 ..."`，缺任何一段都会导致进程立即死亡
- **kill_job 后必须 SSH 验证子进程已清理**，框架只杀 tmux wrapper 不杀 Python 子进程

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279, 2× RTX PRO 6000 Blackwell 94GB VRAM
- **工作目录**: `/root/solver-trace-ablation/`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **CUDA**: 12.8, PyTorch 2.10.0+cu128
- **模型**: Qwen3-4B（ModelScope 下载，路径在代码 config 中）
- **Solvers**: Prover9 (LADR 编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0
- **磁盘**: 系统盘 30GB / 数据盘 `/root/autodl-tmp/` 250GB (96% 满)
- **活跃进程**: exp1-random-b03-s43-r4 (PID 117566, tmux, cuda:0)
- **Cron**: 本 session 无注册 cron，但 submit_training_job 框架自动注册了 exp1-random-b03-s43-r4 的监控

### 3. 📊 当前状态

**刚发生的事**:
- D067/D068: 磁盘清理误删 s43 checkpoint，触发 ISR s43 和 random s43 重训
- D069: s44 在正确测试集上确认 100% H7 gaming，D060 seed instability 成立
- exp1-isr-b03-s43-r3 成功完成，ISR s43 数据已闭环

**Registry 活跃实验**:
- `exp1-random-b03-s43-r4` — **RUNNING** cuda:0, random β=0.3 s43 重训（第4次尝试，前几次 killed/OOM）
- `exp1-random-b03-s44-r2` — **ANALYZING**, 训练已完成 02:26 UTC, 正被 worker 处理 eval

**活跃 Workers** (2个):
- `worker_ops_cleanup-and-eval-random-s44-r2` — running, 清理磁盘 + eval random s44 r2
- `worker_writing_method-fixes-v2` — running, 修改 Method section 草稿

**等待中**:
- 等 exp1-random-b03-s43-r4 训练完成回调（估计数小时）
- 等上述两个 Worker 完成回调
- 论文其余章节待写（writing_plan.yaml 已 Director approved）

### 4. 📋 待办（条件触发式）
- `worker_ops_cleanup-and-eval-random-s44-r2` 回调 → 读 eval 结果，更新 registry (exp1-random-b03-s44-r2)，确认用了 proofwriter_fol_100.jsonl 正确测试集
- `worker_writing_method-fixes-v2` 回调 → 审查 Method section 修改，推进下一章节写作
- exp1-random-b03-s43-r4 cron 完成回调 → spawn worker eval（**必须用 proofwriter_fol_100.jsonl**），结果出来后 random β=0.3 三 seed 数据全部闭环
- random s43+s44 正确 eval 全部完成 → D066 解锁：可以确认 D060 "Goodhart instability" 叙事是否成立，更新 paper_framing.md §4.3
- 三 seed 全闭环 → 汇报 Director，推进剩余论文章节（Experiments, Results, Discussion）
- 写作期间若 Reviewer 要求补充实验 → 利用空闲 GPU 立即安排

### 5. 🎯 战略上下文
- **DDL**: EMNLP ARR 2026-05-25，剩 11 天，当前处于写作阶段
- **论文 framing**: STA/ISR 作为 GRPO 的 Goodhart 诊断工具 + 案例研究。3 个 Claims 全部实验闭环，但 β=0.3 s43/s44 数据因 D062 错误测试集需要重新 eval 确认
- **核心决策链**: D060→D061→D062→D063→D066 — β=0.3 的叙事从 "dose-response collapse" 改为 "cross-seed Goodhart instability"，但因数据完整性问题暂停，等正确 eval 结果
- **最容易判断错的事**:
  1. 不要把 test_100.jsonl 和 proofwriter_fol_100.jsonl 的结果混用比较——零重叠的测试集
  2. exp1-random-b03-s44-r2 的 ANALYZING 状态——Worker 正在处理，不要重复 spawn eval worker
  3. D051 定论 premise-count-matched 1.06x 是最终结论，不要再引用之前的 2.4x（已作废）
  4. Hacking taxonomy 是 7 种（含 query-as-fact 第 7 种），不是 6 种
  5. 磁盘 96% 满——提交新实验前必须先让 Worker 清理旧 checkpoint


---
