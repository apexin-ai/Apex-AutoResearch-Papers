# agent / loop_7.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`acb2052a17dc20f82c97.json`](../../sessions/ac/acb2052a17dc20f82c97.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-14T05:19:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：home-1x5090:cuda:0, westd-48478:cuda:0, westd-48478:cuda:1。**不可用 westd-48478:cuda:2 或 cuda:3**（虽然 report.md 显示 cls-v5-conda 跑在 cuda:2，这是历史遗留，新实验必须严格用白名单）
- home-1x5090 账户是 **sonny**（不是 root），路径前缀 `/home/sonny/`
- westd-48478 账户是 **root**，路径前缀 `/root/autodl-tmp/`
- home-1x5090 上 CLS v5 残留子进程 PID 2947263 可能仍占用 GPU 显存，**重启任何训练前必须先确认 GPU 已清理**
- transformers 版本必须 4.57.6（westd 系统 Python 是 5.8.0，会导致结果不可比——D054 教训）

### 2. 🖥️ 基础设施快照
- **home-1x5090**：工作目录 `/home/sonny/exec-sim-repair-verifier/`，Python `/home/sonny/exec-sim-repair-verifier/.venv/bin/python3`（transformers 4.57.6），GPU RTX 5090 32GB
- **westd-48478**：工作目录 `/root/autodl-tmp/exec-sim-repair-verifier/`，Python `/root/miniconda3/bin/python`（conda base, transformers 4.57.6），4×RTX 5090
- 数据：home `/home/sonny/exec-sim-repair-verifier/data/swebench_full/` (70748条)；westd `/root/autodl-tmp/exec-sim-repair-verifier/data/swebench_full/`
- 模型：Qwen/Qwen3-4B（LoRA rank=16, alpha=32, max_seq_length=2048）
- 活跃进程：repo-level-cwm-seed123-conda (westd cuda:0, PID 未知), repo-level-cls-v5-conda (westd cuda:2, PID 未知)
- Worker 运行中：`worker_diag_cls-seed123-home-oom_20260514T012018`（诊断 home GPU OOM）

### 3. 📊 当前状态
**刚做完**：收到 `repo-level-cls-seed123-home` 失败 cron 回调，诊断根因为 CLS v5 残留子进程占 GPU 显存导致 OOM。已更新 registry、派 Worker 去 home 清理 GPU、向 Director 汇报。

**RUNNING 实验**：
- `repo-level-cwm-seed123-conda` — westd cuda:0，CWM seed123 conda 环境训练
- `repo-level-cls-v5-conda` — westd cuda:2，CLS v5 conda 环境训练

**等待中**：
- Worker `worker_diag_cls-seed123-home-oom_20260514T012018` 回调 → 清理结果 + checkpoint 情况
- Director 对汇报的决策（特别是 westd-48478:cuda:1 空闲 GPU 分配）

### 4. 📋 待办
- 诊断 Worker 回调 → 若 GPU 已清理且无 checkpoint → 新建实验重启 CLS seed123 训练（home cuda:0）
- 诊断 Worker 回调 → 若有可用 checkpoint（step ≥ 200）→ 向 Director 汇报，建议直接 eval
- Director 分配 westd cuda:1 任务 → 立即提交（当前空闲 = 失职）
- repo-level-cwm-seed123-conda 或 cls-v5-conda 训练完成 cron → 按 on-experiment-done 流程处理，eval pipeline
- D056 要求 early stop + eval pipeline，**所有 5 个训练完成后**需立即启动配对 eval + paired bootstrap + TOST

### 5. 🎯 战略上下文
- **核心结论**：CLS > CWM，gap 随代码复杂度放大（func-level 1.24pp → repo-level 10.3pp）。D052 GO 已确认。
- **当前阶段**：Paper Patch — 论文已 patch §3.6/Abstract/Intro/Conclusion，等 Reviewer Phase E 审查。缺 multi-seed robustness 数据（seed123 配对 + paired bootstrap）。
- **关键决策链**：D052 GO → D053 seed123 westd 无效(transformers版本) → D054 环境一致性修复(conda) → D055 CWM v11 混合版本不可用 → D056 early stop 转 eval
- **易错点**：不要混用 westd 系统 Python (transformers 5.8.0) 和 conda (4.57.6) 训练的 checkpoint 做对比——D053/D054 的核心教训。CWM v11 全量 eval 结果只能作参考数（混合版本 checkpoint）。
- **CWM 75.2% unparseable**（tok1024 下输出平均 3398 tokens）——这是 CWM 劣势的关键证据，不要尝试修复 parsing，这本身就是 finding。


---
